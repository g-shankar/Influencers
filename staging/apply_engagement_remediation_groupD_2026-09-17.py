#!/usr/bin/env python3
"""Group D engagement remediation (batches 18/19/20) — 2026-09-17.

Writes ONLY the engagement_observed cell for the 10 qualifying handles.
Every other column, every other row, and row order are preserved byte-for-byte
(other than the single edited cell's quoted value). Field-level diffs are
produced for the gate audit.
"""
import csv
import hashlib
import json
import os

BASE = os.path.expanduser("~/workspace/travel-influencer-pilot/staging")

UPDATES = {
    "18": {
        "@sarowly": (
            "Same-creator TikTok evidence (observed 2026-09-17): @sar.owly (SF Blogger; "
            "bio says 'IG: @sarowly', creator name 'Sarah (@sarowly) SF Blogger', links "
            "sarowly.me) post https://www.tiktok.com/@sar.owly/video/7614949447289589022 "
            "('The best 2-days itinerary to San Francisco'): 11,300 plays, 321 likes, "
            "6 comments, 51 shares, 312 saves. Source: TikTok creator video page "
            "(direct open). §5 cross-platform engagement signal."
        ),
        "@indianahannah_blog": (
            "Same-creator TikTok evidence (observed 2026-09-17): @indianahannah_blog "
            "(Indiana Hannah, IN travel/lifestyle blogger; handle matches Instagram "
            "handle exactly) post "
            "https://www.tiktok.com/@indianahannah_blog/photo/7612457310710926606 "
            "('50 Unexpected Things to Do in Indiana This Spring'): 30.1K likes, "
            "103 comments (search-index observation 2026-09-17; direct photo page "
            "confirmed author handle but rendered no metrics). Source: TikTok. "
            "§5 cross-platform engagement signal."
        ),
        "@bucketlistjourney": (
            "Creator-published media kit (observed 2026-09-17): "
            "https://bucketlistjourney.net/media-kit/ identifies creator Annette and "
            "Instagram @bucketlistjourney; states over 750,000 monthly visitors. "
            "§5 engagement signal."
        ),
        "@absolutelylucy": (
            "Creator-published work-with-me page with audience stats (observed "
            "2026-09-17): https://absolutelylucy.com/work-with-me/ (creator Lucy, "
            "Absolutely Lucy): 455,000 engaged audience; 100,000 monthly page views; "
            "745,000 annual page views; 6M+ social views in 2025. §5 media-kit "
            "engagement signal."
        ),
    },
    "19": {
        "@jessica_traveler": (
            "Same-creator TikTok evidence (observed 2026-09-17): creator-owned site "
            "https://www.myfeetwillleadme.com/contact-us/ (Jessica Carpenter; links "
            "Instagram and TikTok as @jessica_traveler) identifies both handles; TikTok "
            "post https://www.tiktok.com/@jessica_traveler/video/7617879174191107342: "
            "1,914 plays, 107 likes, 3 comments, 50 shares, 76 saves. Source: TikTok "
            "(direct open). §5 cross-platform engagement signal."
        ),
        "@marissa.daily": (
            "Same-creator TikTok evidence (observed 2026-09-17): 2026 creator "
            "interview transcript states Marissa Strang's Instagram is @marissa.daily "
            "and TikTok is @marissadaily_ "
            "(https://www.themaverickshow.com/wp-content/uploads/2026/05/"
            "390_Marissa_Strang_Part_2_Transcript.pdf); TikTok post "
            "https://www.tiktok.com/@marissadaily_/video/7605292254936288543 "
            "(Osaka 24-hour itinerary): 175,400 plays, 8,537 likes, 77 comments, "
            "2,884 shares, 8,232 saves. Source: TikTok (direct open). §5 "
            "cross-platform engagement signal."
        ),
        "@travelrealizations": (
            "Same-creator TikTok evidence (observed 2026-09-17): @travelrealizations "
            "(Chirasree Banerjee; handle matches Instagram handle exactly; content "
            "identifies #TravelRealizations) post "
            "https://www.tiktok.com/@travelrealizations/video/7608610032212544782 "
            "(General Sherman/Sequoia): 16,700 plays, 696 likes, 120 comments, "
            "82 shares, 61 saves. Source: TikTok (direct open). §5 cross-platform "
            "engagement signal."
        ),
        "@liveloveruntravel": (
            "Same-creator TikTok evidence (observed 2026-09-17): @liveloveruntravel "
            "(Christine, Travel Blogger; handle matches Instagram handle exactly) post "
            "https://www.tiktok.com/@liveloveruntravel/video/7596883031420357901 "
            "(Page, Arizona sand cave): 650,700 plays, 52,900 likes, 539 comments, "
            "11,100 shares, 26,420 saves. Source: TikTok (direct open). §5 "
            "cross-platform engagement signal."
        ),
    },
    "20": {
        "@vickyflipflop": (
            "Creator-published 2025 media kit (observed 2026-09-17): "
            "https://vickyflipfloptravels.com/wp-content/uploads/2025/07/"
            "VickyFlipFlop-Media-Pack.pdf identifies Victoria Philpott / "
            "VickyFlipFlopTravels and @vickyflipflop; states over 1 million YouTube "
            "views, 35,000 monthly page views, over 40K social-media followers. "
            "§5 engagement signal."
        ),
        "@expertvagabond": (
            "Creator-published engagement stats on own contact/partnership page "
            "(observed 2026-09-17): https://expertvagabond.com/contact/ (Matthew "
            "Karsten); 'expertvagabond.com reaches 6 million people annually'; Online "
            "Reach: 300,000 monthly site visitors; 15,000 newsletter subscribers; "
            "140,000 Instagram followers; 60,000 YouTube subscribers; 110,000 "
            "Facebook followers; 29,000 Twitter followers. §5 engagement signal."
        ),
    },
}

FIELD = "engagement_observed"

report = {"batches": {}, "total_updates": 0}
for b, updates in UPDATES.items():
    path = os.path.join(BASE, f"selection_log_batch{b}.csv")
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fieldnames = rows and list(rows[0].keys())
    assert FIELD in fieldnames, f"{b}: missing {FIELD} column"
    changed = []
    for r in rows:
        h = (r.get("handle") or "").strip()
        if h in updates:
            old = r[FIELD]
            r[FIELD] = updates[h]
            changed.append({"handle": h, "old": old, "new": updates[h]})
            assert len(updates[h]) > 0
    assert len(changed) == len(updates), (
        f"{b}: expected {len(updates)} updates, applied {len(changed)}")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    report["batches"][b] = {"rows": len(rows), "updated": [c["handle"] for c in changed]}
    report["total_updates"] += len(changed)
    # per-row verification readback
    with open(path, newline="", encoding="utf-8") as f:
        back = {r["handle"]: r[FIELD] for r in csv.DictReader(f)}
    for h, v in updates.items():
        assert back[h] == v, f"{b} {h}: readback mismatch"
    print(f"{b}: {len(rows)} rows, updated {len(changed)} cells, readback OK")

out = os.path.join(BASE, "engagement_remediation_groupD_edit_report_2026-09-17.json")
json.dump(report, open(out, "w", encoding="utf-8"), indent=2)
print("total updates:", report["total_updates"], "->", out)
