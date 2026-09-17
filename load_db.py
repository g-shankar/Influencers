#!/usr/bin/env python3
"""Load validated pilot data into pilot.db. Fail-closed.

Inputs: canonical staging/itineraries_batch{N}.json (N from stage.json),
        influencers.csv, validation/reports/gate3_report.json (per-URL reachability),
        validation/quarantine.json (status=quarantined -> zero itinerary attribution).
Stage targets (creator total, per-platform quotas) come from stage.json;
the loader still refuses to load on any quota mismatch.
Optional: --exclude-json path to a JSON array of {"batch":n,"handle":h,"title":t}
        entries the evidence council marked FAIL/UNVERIFIABLE. These are skipped.

Nothing invented: followers_approx loads as-is ('unknown' stays 'unknown').
Quarantined handles keep their influencer row but get ZERO itineraries.

Writes validation/reports/db_load_report.json. Exit 1 on any inconsistency.
Stdlib only.
"""
import csv
import json
import sqlite3
import sys
from pathlib import Path

from stage_config import load as load_stage

ROOT = Path(__file__).resolve().parents[0]
DB = ROOT / "pilot.db"
REPORTS = ROOT / "validation" / "reports"
STAGE = load_stage()


def main():
    exclude = set()
    if len(sys.argv) > 1 and sys.argv[1] == "--exclude-json":
        entries = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        exclude = {(e["batch"], e["handle"], e["title"]) for e in entries}

    g3 = json.loads((REPORTS / "gate3_report.json").read_text(encoding="utf-8"))
    if g3.get("status") != "PASS":
        sys.exit("refusing to load: gate3_report.json is not PASS")
    url_reach = {u: r.get("reachable") for u, r in g3.get("url_results", {}).items()}
    overridden = set()
    for o in g3.get("overridden_script_false_negatives", []):
        for u in o["verified_by_manual_browser_fetch"]:
            overridden.add(u)

    quar = {q["handle"] for q in
            json.loads((ROOT / "validation" / "quarantine.json").read_text(encoding="utf-8"))["quarantine"]
            if q.get("status") == "quarantined"}

    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    for t in ("itinerary_sources", "itinerary_items", "itineraries", "posts", "influencers"):
        cur.execute(f"DELETE FROM {t}")

    # 1. influencers from influencers.csv
    with open(ROOT / "influencers.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != STAGE["creators_total"]:
        sys.exit(f"refusing to load: influencers.csv has {len(rows)} rows, expected {STAGE['creators_total']}")
    seen = set()
    for r in rows:
        key = (r["handle"].strip(), r["platform"].strip())
        if key in seen:
            sys.exit(f"duplicate influencer in csv: {key}")
        seen.add(key)
        cur.execute(
            "INSERT INTO influencers (name, handle, platform, niche, followers_approx, profile_url, source_urls)"
            " VALUES (?,?,?,?,?,?,?)",
            (r["name"].strip(), r["handle"].strip(), r["platform"].strip(),
             (r.get("niche") or "").strip() or None,
             (r.get("followers_approx") or "").strip() or "unknown",
             (r.get("profile_url") or "").strip() or None,
             (r.get("source_urls") or "").strip() or None))
    inf_id = {h: i for h, i in cur.execute("SELECT handle, id FROM influencers")}
    plats = dict(cur.execute("SELECT platform, COUNT(*) FROM influencers GROUP BY platform"))
    quota = STAGE["platforms"]
    if plats != quota:
        sys.exit(f"platform split wrong after load: {plats} (quota: {quota})")

    # 2. itineraries + items + sources + posts
    stats = {"itineraries": 0, "items": 0, "sources": 0, "posts": 0,
             "skipped_quarantined": [], "skipped_council": []}
    for n in STAGE["batches"]:
        data = json.loads((ROOT / "staging" / f"itineraries_batch{n}.json").read_text(encoding="utf-8"))
        for ex in data.get("extractions", []):
            handle = ex["handle"]
            if handle not in inf_id:
                sys.exit(f"staging handle not in influencers.csv: {handle}")
            iid = inf_id[handle]
            for it in ex.get("itineraries", []):
                key = (n, handle, it["title"])
                if handle in quar:
                    stats["skipped_quarantined"].append({"batch": n, "handle": handle, "title": it["title"]})
                    continue
                if key in exclude:
                    stats["skipped_council"].append({"batch": n, "handle": handle, "title": it["title"]})
                    continue
                if it.get("confidence") not in ("high", "medium", "low"):
                    sys.exit(f"bad confidence on {key}")
                cur.execute(
                    "INSERT INTO itineraries (influencer_id, title, destination, country, days, summary, confidence)"
                    " VALUES (?,?,?,?,?,?,?)",
                    (iid, it["title"], it.get("destination"), it.get("country"),
                     it.get("days"), it.get("summary"), it.get("confidence")))
                tid = cur.lastrowid
                stats["itineraries"] += 1
                for item in it.get("items", []):
                    if not (item.get("name") or "").strip():
                        sys.exit(f"unnamed item in {key}")
                    cur.execute(
                        "INSERT INTO itinerary_items (itinerary_id, day, item_type, name, location, details, booking_link, price_hint)"
                        " VALUES (?,?,?,?,?,?,?,?)",
                        (tid, item.get("day"), item.get("item_type"), item["name"].strip(),
                         item.get("location"), item.get("details"),
                         item.get("booking_link"), item.get("price_hint")))
                    stats["items"] += 1
                urls = it.get("source_urls", [])
                if not urls:
                    sys.exit(f"itinerary with no sources: {key}")
                for u in urls:
                    if u in overridden:
                        verdict = "reachable"
                    elif u in url_reach:
                        verdict = "reachable" if url_reach[u] else "unreachable"
                    else:
                        verdict = "unchecked"
                    cur.execute(
                        "INSERT INTO itinerary_sources (itinerary_id, source_url, reachable, verified_at)"
                        " VALUES (?,?,?,date('now'))", (tid, u, verdict))
                    stats["sources"] += 1
                cur.execute(
                    "INSERT INTO posts (influencer_id, post_url, platform, extracted_at)"
                    " VALUES (?,?,?,datetime('now'))",
                    (iid, urls[0], ex.get("platform")))
                pid = cur.lastrowid
                stats["posts"] += 1
                cur.execute("UPDATE itineraries SET source_post_id=? WHERE id=?", (pid, tid))

    # 3. invariants
    def one(q, *a):
        return cur.execute(q, a).fetchone()[0]
    checks = {
        "influencers": one("SELECT COUNT(*) FROM influencers"),
        "itineraries": one("SELECT COUNT(*) FROM itineraries"),
        "orphan_items": one("SELECT COUNT(*) FROM itinerary_items i LEFT JOIN itineraries t ON t.id=i.itinerary_id WHERE t.id IS NULL"),
        "orphan_itineraries": one("SELECT COUNT(*) FROM itineraries t LEFT JOIN influencers f ON f.id=t.influencer_id WHERE f.id IS NULL"),
        "itineraries_without_source": one("SELECT COUNT(*) FROM itineraries t LEFT JOIN itinerary_sources s ON s.itinerary_id=t.id WHERE s.id IS NULL"),
        "quarantined_with_itineraries": one(
            "SELECT COUNT(*) FROM itineraries t JOIN influencers f ON f.id=t.influencer_id WHERE f.handle IN ("
            + ",".join("?" * len(quar)) + ")", *quar),
    }
    bad = [k for k, v in checks.items()
           if (k in ("influencers", "itineraries") and v <= 0) or (k not in ("influencers", "itineraries") and v != 0)]
    if checks["influencers"] != STAGE["creators_total"]:
        bad.append(f"influencers!={STAGE['creators_total']}")
    if bad:
        con.rollback()
        sys.exit(f"load invariants failed: {checks}")
    con.commit()
    report = {"db": str(DB), "status": "loaded", "stats": stats, "checks": checks}
    (REPORTS / "db_load_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("DB LOAD OK:", json.dumps(stats))
    print("checks:", json.dumps(checks))


if __name__ == "__main__":
    main()
