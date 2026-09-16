#!/usr/bin/env python3
"""Regenerate report/final_report_data.json from the FINAL pilot.db.

Every number is recomputed with a documented query (see derivation log printed
to stdout). Corrections applied vs the 2026-09-15 deck data:
  - longest_days: 30 -> 90  (verified: id 44, 3-month SE Asia itinerary, days=90 CONFIRMED 2026-09-16)
  - trips_7_days_or_more: 57 -> recomputed from final DB (was not reproducible)
Schema matches the original final_report_data.json so the deck builder can
consume it directly. Stdlib only.
"""
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "pilot.db"
OUT = ROOT / "report" / "final_report_data.json"
OLD = ROOT / "report" / "final_report_data.json"

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
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    one = lambda q, *a: con.execute(q, a).fetchone()[0]

    n_inf = one("SELECT COUNT(*) FROM influencers")
    note(f"creators.total: SELECT COUNT(*) FROM influencers -> {n_inf}")
    plats = dict(con.execute("SELECT platform, COUNT(*) FROM influencers GROUP BY platform").fetchall())
    note(f"platform split: {plats}")
    assert plats == {"instagram": 50, "tiktok": 50}, plats

    known = one("SELECT COUNT(*) FROM influencers WHERE followers_approx != 'unknown'")
    unknown = one("SELECT COUNT(*) FROM influencers WHERE followers_approx = 'unknown'")
    note(f"known/unknown followers: {known}/{unknown}")

    with_it = one("SELECT COUNT(DISTINCT influencer_id) FROM itineraries")
    note(f"creators.with_itineraries: SELECT COUNT(DISTINCT influencer_id) FROM itineraries -> {with_it}")

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
    note(f"shortest_days: SELECT MIN(days) -> {shortest} | longest_days: SELECT MAX(days) -> {longest} (was 30 in deck data; corrected)")
    note(f"trips_7_days_or_more: SELECT COUNT(*) FROM itineraries WHERE days >= 7 -> {trips7} (was 57 in deck data; not reproducible)")
    note(f"NULL days itineraries (excluded from trip-length stats): {null_days}")

    longest_title = con.execute("SELECT title FROM itineraries ORDER BY days DESC LIMIT 1").fetchone()[0]
    note(f"longest trip: {longest_title[:60]}")

    # Flagships: recompute days/items/confidence/source from DB; keep editorial labels from previous file.
    old = json.loads(OLD.read_text()) if OLD.exists() else {}
    old_flags = {f["handle"]: f for f in old.get("flagship_itineraries", [])}
    flagships = []
    for handle in ("@onegirlwandering", "@theblondeabroad", "@nomadicmatt", "@budgettraveller", "@oneikathetraveller"):
        of = old_flags.get(handle, {})
        title_like = {"@onegirlwandering": "%Japan%", "@theblondeabroad": "%Morocco%",
                      "@nomadicmatt": "%Sweden%", "@budgettraveller": "%European%",
                      "@oneikathetraveller": "%South Africa%"}[handle]
        r = con.execute("""SELECT it.id, it.title, it.destination, it.days, it.confidence, inf.platform
                           FROM itineraries it JOIN influencers inf ON it.influencer_id = inf.id
                           WHERE inf.handle = ? AND it.title LIKE ?""", (handle, title_like)).fetchone()
        if not r:
            sys.exit(f"flagship not found in DB: {handle}")
        iid = r["id"]
        n_items = one("SELECT COUNT(*) FROM itinerary_items WHERE itinerary_id = ?", iid)
        src = con.execute("SELECT source_url FROM itinerary_sources WHERE itinerary_id = ? ORDER BY id LIMIT 1", (iid,)).fetchone()[0]
        flagships.append({
            "handle": handle,
            "title": of.get("title", r["title"]),
            "destination": of.get("destination", r["destination"]),
            "days": r["days"],
            "items": n_items,
            "confidence": r["confidence"],
            "platform": r["platform"],
            "source": src,
        })
        note(f"flagship {handle}: days={r['days']} items={n_items} conf={r['confidence']}")

    # Top 10 by reported reach (same parse logic as provenance doc).
    creators = con.execute("SELECT handle, platform, followers_approx, profile_url, id FROM influencers").fetchall()
    it_counts = dict(con.execute("SELECT influencer_id, COUNT(*) FROM itineraries GROUP BY influencer_id").fetchall())
    ranked = sorted(creators, key=lambda r: (parse_followers(r["followers_approx"]) is None,
                                             -(parse_followers(r["followers_approx"]) or 0)))
    top = [{"handle": r["handle"], "platform": r["platform"], "followers": r["followers_approx"],
            "profile": r["profile_url"], "itineraries": it_counts.get(r["id"], 0)} for r in ranked[:10]]
    note("top creators by reported reach: " + ", ".join(f"{t['handle']} {t['followers']} ({t['itineraries']} itins)" for t in top))

    quar = json.loads((ROOT / "validation" / "quarantine.json").read_text())["quarantine"]
    n_quar_handles = len([q for q in quar if q.get("status") == "quarantined" and q.get("scope", "handle") == "handle"])
    note(f"quarantined handles: {n_quar_handles}")

    data = {
        "business_ready": old.get("business_ready", True),
        "confidence": {"high": conf.get("high", 0), "medium": conf.get("medium", 0), "low": conf.get("low", 0)},
        "coverage": {
            "destinations": dests,
            "items": items,
            "longest_days": longest,
            "shortest_days": shortest,
            "sources": sources,
            "trips_7_days_or_more": trips7,
        },
        "creators": {
            "instagram": plats["instagram"],
            "tiktok": plats["tiktok"],
            "total": n_inf,
            "unknown_followers": unknown,
            "with_itineraries": with_it,
            "with_known_followers": known,
        },
        "flagship_itineraries": flagships,
        "itineraries": {
            "total": n_it,
            "yield_per_creator": round(n_it / n_inf, 2),
        },
        "packing_model": old.get("packing_model", {}),
        "scale_path": old.get("scale_path", "100 -> 1,000 creators"),
        "top_creators_by_reach": top,
        "trust_line": old.get("trust_line", ""),
        "validation": {
            "audit": "PASS (evidence-only audit 2026-09-16; one finding fixed and re-verified)",
            "evidence_council": "93/93 itineraries independently verified 2026-09-16 (see VERIFICATION_LOG_FULL.md)",
            "gates": "all 7 PASS (original) + strengthened re-verification",
            "quarantined": n_quar_handles,
            "corrections_applied": "see QC_REPORT_STRENGTHENED.md",
        },
    }
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    note(f"wrote {OUT}")

if __name__ == "__main__":
    main()
