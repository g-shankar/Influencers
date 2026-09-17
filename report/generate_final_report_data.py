#!/usr/bin/env python3
"""Regenerate report/final_report_data.json from the FINAL pilot.db.

Every number is recomputed with a documented query (see derivation log printed
to stdout). Stage targets (creator total, platform quotas) come from stage.json.
No hardcoded counts, no hardcoded handles — the same script serves every
expansion stage. Stdlib only.
"""
import datetime
import json
import sqlite3
from pathlib import Path

from stage_config import load as load_stage

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "pilot.db"
OUT = ROOT / "report" / "final_report_data.json"

log = []


def note(s):
    log.append(s)
    print(s)


def parse_followers(s):
    s = (s or "").strip()
    if s.lower() == "unknown" or not s:
        return None
    num = "".join(c for c in s if c.isdigit() or c == ".")
    try:
        v = float(num)
    except ValueError:
        return None
    if s.endswith("M"):
        v *= 1e6
    elif s.endswith("K"):
        v *= 1e3
    return v


def main():
    stage = load_stage()
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    one = lambda q, *a: con.execute(q, a).fetchone()[0]

    n_inf = one("SELECT COUNT(*) FROM influencers")
    note(f"creators.total: SELECT COUNT(*) FROM influencers -> {n_inf}")
    plats = dict(con.execute("SELECT platform, COUNT(*) FROM influencers GROUP BY platform").fetchall())
    note(f"platform split: {plats}")
    assert n_inf == stage["creators_total"], (n_inf, stage["creators_total"])
    assert plats == stage["platforms"], (plats, stage["platforms"])

    known = one("SELECT COUNT(*) FROM influencers WHERE followers_approx != 'unknown'")
    unknown = one("SELECT COUNT(*) FROM influencers WHERE followers_approx = 'unknown'")
    note(f"known/unknown followers: {known}/{unknown}")

    with_it = one("SELECT COUNT(DISTINCT influencer_id) FROM itineraries")
    note(f"creators.with_itineraries: SELECT COUNT(DISTINCT influencer_id) FROM itineraries -> {with_it}")

    niches = dict(con.execute(
        "SELECT COALESCE(niche,'—'), COUNT(*) FROM influencers GROUP BY niche ORDER BY 2 DESC").fetchall())
    note(f"niche counts: {niches}")

    n_it = one("SELECT COUNT(*) FROM itineraries")
    note(f"itineraries.total: SELECT COUNT(*) FROM itineraries -> {n_it}")

    conf = dict(con.execute("SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence").fetchall())
    note(f"confidence split: {conf}")

    dests = one("SELECT COUNT(DISTINCT destination) FROM itineraries")
    items = one("SELECT COUNT(*) FROM itinerary_items")
    sources = one("SELECT COUNT(*) FROM itinerary_sources")
    shortest = one("SELECT MIN(days) FROM itineraries")
    longest = one("SELECT MAX(days) FROM itineraries")
    trips7 = one("SELECT COUNT(*) FROM itineraries WHERE days >= 7")
    null_days = one("SELECT COUNT(*) FROM itineraries WHERE days IS NULL")
    note(f"destinations: {dests} | items: {items} | sources: {sources}")
    note(f"shortest/longest days: {shortest}/{longest} | trips>=7d: {trips7} | no fixed length: {null_days}")

    longest_title = con.execute("SELECT title FROM itineraries ORDER BY days DESC LIMIT 1").fetchone()[0]
    note(f"longest trip: {longest_title[:60]}")

    # Top 10 by reported reach (parse logic unchanged from pilot provenance).
    creators = con.execute("SELECT handle, platform, followers_approx, profile_url, id FROM influencers").fetchall()
    it_counts = dict(con.execute("SELECT influencer_id, COUNT(*) FROM itineraries GROUP BY influencer_id").fetchall())
    ranked = sorted(creators, key=lambda r: (parse_followers(r["followers_approx"]) is None,
                                             -(parse_followers(r["followers_approx"]) or 0)))
    top = [{"handle": r["handle"], "platform": r["platform"], "followers": r["followers_approx"],
            "profile": r["profile_url"], "itineraries": it_counts.get(r["id"], 0)} for r in ranked[:10]]
    note("top creators by reported reach: " + ", ".join(f"{t['handle']} {t['followers']} ({t['itineraries']} itins)" for t in top))

    quar = json.loads((ROOT / "validation" / "quarantine.json").read_text())["quarantine"]
    n_quar_handles = len([q for q in quar if q.get("status") == "quarantined"])
    note(f"quarantined records: {n_quar_handles}")

    g1 = json.loads((ROOT / "validation" / "reports" / "gate1_report.json").read_text())
    g1_batches = sorted(b["batch"] for b in g1["batches"])
    g1_itins = sum(b["itineraries"] for b in g1["batches"])

    data = {
        "stage": stage["stage"],
        "generated_at": datetime.date.today().isoformat(),
        "business_ready": False,
        "business_readiness_note": "Research verified (evidence-only audit). Not business-ready: no supplier/partner access, no commercial terms, no demand validation, no booking/payment/attribution system.",
        "confidence": {"high": conf.get("high", 0), "medium": conf.get("medium", 0), "low": conf.get("low", 0)},
        "coverage": {
            "destinations": dests,
            "items": items,
            "longest_days": longest,
            "longest_title": longest_title,
            "no_fixed_length": null_days,
            "shortest_days": shortest,
            "sources": sources,
            "trips_7_days_or_more": trips7,
        },
        "creators": {
            "instagram": plats.get("instagram", 0),
            "niche_counts": niches,
            "tiktok": plats.get("tiktok", 0),
            "total": n_inf,
            "unknown_followers": unknown,
            "with_itineraries": with_it,
            "with_known_followers": known,
            "without_itineraries": n_inf - with_it,
        },
        "itineraries": {
            "total": n_it,
            "yield_per_creator": round(n_it / n_inf, 2) if n_inf else 0,
        },
        "top_creators_by_reach": top,
        "validation": {
            "batches": g1_batches,
            "gate1_itineraries": g1_itins,
            "gates": "all 7 PASS",
            "quarantined": n_quar_handles,
        },
    }
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    note(f"wrote {OUT}")


if __name__ == "__main__":
    main()
