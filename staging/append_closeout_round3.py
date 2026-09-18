#!/usr/bin/env python3
"""Batch 20 close-out: append @sinahsstories and @gracefkim (coordinator ruling 2026-09-17).
Re-verified by this worker 2026-09-17. Fail-closed dedup at write time."""
import csv, json, sys
from pathlib import Path

ROOT = Path.home() / "workspace" / "travel-influencer-pilot"
CHECK_DATE = "2026-09-17"
SELECTOR = "batch20-closeout"

NEW = [
    {
        "name": "Sinah",
        "handle": "@sinahsstories",
        "platform": "instagram",
        "niche": "underrated destinations / itinerary guides",
        "followers_approx": "121000",
        "profile_url": "https://www.instagram.com/sinahsstories/",
        "source_urls": "https://sinahsstories.com/2025/05/30/ultimate-puglia-7-day-itinerary/; https://influencers.feedspot.com/solo_female_travel_instagram_influencers/",
        "log": {
            "followers_observed": "121000",
            "followers_source": "Feedspot solo-female travel Instagram influencers list observed 2026-09-17 (121K, +19% 3mo); creator's own TikTok bio states IG +115k observed 2026-09-17 (tiktok.com/@sinahsstories)",
            "discovery_source": "Stage 2 batch-20 wave-3 research; coordinator ruling 2026-09-17 to write after re-verification",
            "identity_check": "pass",
            "identity_method": "Own about page (sinahsstories.com/about-short/): 'Hi, I'm Sinah' - consistent mononym operator identity; TikTok @sinahsstories bio 'Sinah - Travel Creator' links sinahsstories.com. Mononym passes per SELECTION_CRITERIA.md section 6.1 (@elise.abroad batch17 precedent).",
            "content_fit": "pass",
            "content_fit_evidence": "'Ultimate Puglia 7-Day Itinerary' on own domain; creator page metadata datePublished 2025-05-30, dateModified 2026-01-24; structured Day 1-7 (Alberobello/Locorotondo, Monopoli, Bari, Polignano a Mare, Cisternino/Ostuni, Lecce, beach day)",
            "reach_floor": "pass",
            "engagement_observed": "TikTok @sinahsstories profile: 488,300 total likes across 348 videos, observed 2026-09-17 (tiktok.com/@sinahsstories). Cross-platform engagement acceptable per founder ruling section 5.",
            "activity_check": "pass (account-level per section 6.2: creator's own TikTok bio observed 2026-09-17 actively promotes IG @sinahsstories (+115k) and links sinahsstories.com; own Puglia guide modified 2026-01-24; site media dated 2026/01)",
            "purchase_intent": "present (booking.com affiliate links on Puglia guide for La Cas\u00e8dde, Sopra I Sassi, Locorotondo/Cisternino/Ostuni stays; Sicily by Car rental link)",
            "exclusions_check": "pass - work-with-me page offers photography/video/drone content for social media and brand campaigns (B2B); no consumer itinerary-planning/coaching/courses/hosted trips found",
            "decision": "include",
            "notes": "Named individual (mononym Sinah, section 6.1 precedent). Qualifying 7-day Puglia guide in-window. Dedup CLEAR vs influencers.csv + all batch*.csv + validation/quarantine.json 2026-09-17 (re-checked at write time).",
        },
    },
    {
        "name": "Grace Kim",
        "handle": "@gracefkim",
        "platform": "instagram",
        "niche": "solo travel / adventure",
        "followers_approx": "109132",
        "profile_url": "https://www.instagram.com/gracefkim/",
        "source_urls": "https://gracefkim.com/10-day-guatemala-itinerary/; https://gondola.cc/gracefkim",
        "log": {
            "followers_observed": "109132",
            "followers_source": "Gondola creator profile observed 2026-09-17 (Total Followers 109,132; 1,121 posts) at gondola.cc/gracefkim",
            "discovery_source": "Stage 2 batch-20 wave-3 research; coordinator ruling 2026-09-17 to write after re-verification",
            "identity_check": "pass",
            "identity_method": "Own site byline 'By: Grace Kim' on gracefkim.com/10-day-guatemala-itinerary/ (April 28, 2025); Gondola profile 'Grace Kim | @gracefkim'. Named individual with matching handle.",
            "content_fit": "pass",
            "content_fit_evidence": "'10-day Guatemala itinerary' on own domain, visibly dated April 28th, 2025; structured day-by-day (Day 1: arrive Guatemala City; Day 2: Guatemala City to Lake Atitlan; page states '10 day daily breakdown' with exact route map)",
            "reach_floor": "pass",
            "engagement_observed": "Gondola: 4,161,509 total likes / 21,444,469 total views observed 2026-09-17 at gondola.cc/gracefkim; per-post metrics visible (330k, 56k, 19k, 12m views)",
            "activity_check": "pass (account-level per section 6.2: Gondola's current IG engagement satisfies activity despite stale blog RSS; 1,121 posts indexed with recent per-post view counts)",
            "purchase_intent": "present (affiliate disclosure on guide; viator.tp.st, booking.tp.st, SafetyWing, Rexby 30%-discount, emrld.cc links throughout)",
            "exclusions_check": "pass - Rexby/Steller are fixed digital products (editorial, allowed per coordinator ruling); targeted 2026-09-17 search found no consumer itinerary-planning/coaching/courses/hosted-trip offer tied to gracefkim.com",
            "decision": "include",
            "notes": "Named individual (Grace Kim). Qualifying 10-day Guatemala guide in-window. Dedup CLEAR vs influencers.csv + all batch*.csv + validation/quarantine.json 2026-09-17 (re-checked at write time; handle appears only in the staging dedup-universe worker artifact, which the 2026-09-17 ledger addendum itself flagged as stale/wrong - batch16.csv contains no @gracefkim; coordinator ruling explicitly instructs inclusion).",
        },
    },
]

def dedup_universe():
    handles = set()
    for p in [ROOT / "influencers.csv"] + sorted(ROOT.glob("batch*.csv")):
        try:
            with open(p, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    h = (row.get("handle") or "").strip().lower()
                    if h:
                        handles.add(h)
        except FileNotFoundError:
            pass
    qp = ROOT / "validation" / "quarantine.json"
    try:
        q = json.loads(qp.read_text(encoding="utf-8"))
        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    yield from walk(v)
            elif isinstance(o, list):
                for v in o:
                    yield from walk(v)
            elif isinstance(o, str) and o.startswith("@"):
                yield o.lower()
        handles.update(walk(q))
    except FileNotFoundError:
        pass
    return handles

def main():
    universe = dedup_universe()
    keep = []
    for c in NEW:
        if c["handle"].lower() in universe:
            print(f"DEDUP COLLISION - DROPPED: {c['handle']}", file=sys.stderr)
        else:
            keep.append(c)
    if not keep:
        print("nothing to write", file=sys.stderr)
        return 1

    # 1. batch20.csv
    b20 = ROOT / "batch20.csv"
    with open(b20, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for c in keep:
            w.writerow([c["name"], c["handle"], c["platform"], c["niche"],
                        c["followers_approx"], c["profile_url"], c["source_urls"]])

    # 2. selection log
    slog = ROOT / "staging" / "selection_log_batch20.csv"
    cols = ["batch", "handle", "platform", "name", "niche", "followers_approx",
            "followers_observed", "followers_source", "profile_url", "discovery_source",
            "identity_check", "identity_method", "content_fit", "content_fit_evidence",
            "reach_floor", "engagement_observed", "activity_check", "purchase_intent",
            "exclusions_check", "decision", "notes", "check_date", "selector"]
    with open(slog, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        for c in keep:
            row = {"batch": "20", "handle": c["handle"], "platform": c["platform"],
                   "name": c["name"], "niche": c["niche"],
                   "followers_approx": c["followers_approx"],
                   "profile_url": c["profile_url"],
                   "check_date": CHECK_DATE, "selector": SELECTOR}
            row.update(c["log"])
            w.writerow(row)

    # 3. validate widths
    for p, ncols in [(b20, 7), (slog, 23)]:
        with open(p, newline="", encoding="utf-8") as f:
            for i, row in enumerate(csv.reader(f), 1):
                assert len(row) == ncols, f"{p.name} line {i}: {len(row)} cols"

    print(f"wrote {len(keep)} creators: " + ", ".join(c["handle"] for c in keep))
    with open(b20, newline="", encoding="utf-8") as f:
        print("batch20.csv rows:", sum(1 for _ in csv.DictReader(f)))
    with open(slog, newline="", encoding="utf-8") as f:
        print("selection_log rows:", sum(1 for _ in csv.DictReader(f)))

if __name__ == "__main__":
    sys.exit(main())
