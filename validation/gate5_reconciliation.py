#!/usr/bin/env python3
"""Gate 5 — DB reconciliation (fail-closed).

Runs after load_db.py, before the report. Every check is derived from
stage.json (expected creator total + platform quotas) and
validation/quarantine.json (quarantined handles) — nothing hardcoded,
so the same script serves every expansion stage.

Exit codes: 0 PASS, 1 FAIL. Writes validation/reports/gate5_report.json.
Stdlib only.
"""
import json
import sqlite3
import sys
from pathlib import Path

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stage_config import load as load_stage

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "pilot.db"
REPORTS = ROOT / "validation" / "reports"


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    stage = load_stage()
    errors, results = [], {}

    def check(name, value, expect, cmp="eq"):
        ok = (value == expect) if cmp == "eq" else (value != expect)
        results[name] = {"value": value, "expected": expect, "pass": bool(ok)}
        if not ok:
            errors.append(f"{name}: got {value}, expected {expect}")

    con = sqlite3.connect(DB)
    one = lambda q, *a: con.execute(q, a).fetchone()[0]

    # 1. counts vs stage quotas
    check("influencers_total", one("SELECT COUNT(*) FROM influencers"),
          stage["creators_total"])
    plats = dict(con.execute("SELECT platform, COUNT(*) FROM influencers GROUP BY platform").fetchall())
    for p, q in stage["platforms"].items():
        check(f"platform_{p}", plats.get(p, 0), q)

    # 2. follower provenance: no empty values
    check("empty_followers",
          one("SELECT COUNT(*) FROM influencers WHERE followers_approx IS NULL OR TRIM(followers_approx) = ''"), 0)

    # 3. duplicate handles: none
    check("duplicate_handles",
          one("SELECT COUNT(*) FROM (SELECT handle, platform FROM influencers GROUP BY handle, platform HAVING COUNT(*) > 1)"), 0)

    # 4. totals reconcile with gate1 report
    g1 = json.loads((REPORTS / "gate1_report.json").read_text(encoding="utf-8"))
    g1_itins = sum(b["itineraries"] for b in g1["batches"])
    db_itins = one("SELECT COUNT(*) FROM itineraries")
    results["itineraries_total"] = {"value": db_itins, "gate1_total": g1_itins}
    quar = {q["handle"] for q in
            json.loads((ROOT / "validation" / "quarantine.json").read_text(encoding="utf-8"))["quarantine"]
            if q.get("status") == "quarantined"}
    g1_skipped = sum(1 for b in g1["batches"] for e in b.get("errors", []) if "quarantin" in e.lower())
    # load-time skip accounting lives in db_load_report.json
    load_rep = json.loads((REPORTS / "db_load_report.json").read_text(encoding="utf-8"))
    skipped = len(load_rep["stats"].get("skipped_quarantined", [])) + len(load_rep["stats"].get("skipped_council", []))
    if db_itins != g1_itins - skipped:
        errors.append(f"itineraries_total: db={db_itins} != gate1({g1_itins}) - skipped({skipped})")
    else:
        results["itineraries_reconciled"] = {"value": db_itins, "pass": True}
    results["items_total"] = {"value": one("SELECT COUNT(*) FROM itinerary_items")}
    results["confidence_split"] = dict(con.execute("SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence").fetchall())

    # 5. orphans: zero everywhere
    check("orphan_items",
          one("SELECT COUNT(*) FROM itinerary_items i LEFT JOIN itineraries t ON t.id=i.itinerary_id WHERE t.id IS NULL"), 0)
    check("orphan_itineraries",
          one("SELECT COUNT(*) FROM itineraries t LEFT JOIN influencers f ON f.id=t.influencer_id WHERE f.id IS NULL"), 0)
    check("orphan_posts",
          one("SELECT COUNT(*) FROM posts p LEFT JOIN influencers f ON f.id=p.influencer_id WHERE f.id IS NULL"), 0)

    # 6. every itinerary has >=1 source
    check("itineraries_without_source",
          one("SELECT COUNT(*) FROM itineraries t LEFT JOIN itinerary_sources s ON s.itinerary_id=t.id WHERE s.id IS NULL"), 0)

    # 7. duplicate itineraries (same influencer, title+destination): list for review
    dupes = con.execute(
        "SELECT influencer_id, title, destination, COUNT(*) c FROM itineraries "
        "GROUP BY influencer_id, title, destination HAVING c > 1").fetchall()
    results["duplicate_itineraries"] = [dict(zip(["influencer_id", "title", "destination", "n"], d)) for d in dupes]
    if dupes:
        errors.append(f"duplicate_itineraries: {len(dupes)} groups need manual review")

    # 8. quarantined handles must not be attributed (handles from quarantine.json)
    if quar:
        qmarks = ",".join("?" * len(quar))
        check("quarantined_with_itineraries",
              one(f"SELECT COUNT(*) FROM itineraries t JOIN influencers f ON f.id=t.influencer_id WHERE f.handle IN ({qmarks})",
                  *quar), 0)
    results["quarantined_handles"] = sorted(quar)

    # 9. distribution sanity (informational)
    results["top_countries"] = con.execute(
        "SELECT country, COUNT(*) FROM itineraries GROUP BY country ORDER BY 2 DESC LIMIT 15").fetchall()
    results["top_destinations"] = con.execute(
        "SELECT destination, COUNT(*) FROM itineraries GROUP BY destination ORDER BY 2 DESC LIMIT 15").fetchall()

    status = "FAIL" if errors else "PASS"
    (REPORTS / "gate5_report.json").write_text(
        json.dumps({"gate": 5, "name": "db reconciliation", "status": status,
                    "results": results, "errors": errors}, indent=2), encoding="utf-8")
    print(f"GATE 5 [{status}] errors={len(errors)}")
    for e in errors[:20]:
        print("  FAIL:", e)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
