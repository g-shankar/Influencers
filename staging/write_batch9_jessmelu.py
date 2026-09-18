#!/usr/bin/env python3
"""Append @jessmelu to canonical batch9 files (TikTok re-dispatch t2).
Writes: batch9.csv, staging/selection_log_batch9.csv, staging/itineraries_batch9.json.
Selector: t2-redispatch-2026-09-17. check_date=2026-09-17."""
import csv, json, sys, glob

BASE = '/home/hatch/workspace/travel-influencer-pilot'
CHECK_DATE = '2026-09-17'
SELECTOR = 't2-redispatch-2026-09-17'
PLATFORM = 'tiktok'

def dedup_universe():
    u = set()
    for f in glob.glob(f'{BASE}/batch*.csv') + glob.glob(f'{BASE}/influencers.csv'):
        for row in csv.DictReader(open(f, encoding='utf-8')):
            h = (row.get('handle') or '').strip().lower()
            if h: u.add(h)
    try:
        for line in open(f'{BASE}/staging/dedup_handles_batch9.txt', encoding='utf-8'):
            line = line.strip().lower()
            if line: u.add(line)
    except FileNotFoundError:
        pass
    try:
        q = json.load(open(f'{BASE}/validation/quarantine.json', encoding='utf-8'))
        items = q if isinstance(q, list) else q.get('entries', q.get('items', []))
        for e in (items or []):
            h = (e.get('handle') or '').strip().lower()
            if h: u.add(h)
    except FileNotFoundError:
        pass
    return u

ACCEPTED = [
  {
    "name": "Jess",
    "handle": "@jessmelu",
    "niche": "Croatia/Europe travel",
    "followers_approx": "538.7K",
    "profile_url": "https://www.tiktok.com/@jessmelu",
    "source_urls": "https://www.tiktok.com/@jessmelu/video/7505783025502932246",
    "followers_observed": "538,700",
    "followers_source": "TikTok profile state __UNIVERSAL_DATA_FOR_REHYDRATION__, observed 2026-09-17",
    "discovery_source": "TikTok discovery re-dispatch 2026-09-17 (t2); web search for day-by-day itinerary creators",
    "identity_check": "pass - mononym 'Jess' (mononym allowed per SELECTION_CRITERIA.md coordinator adjudication 2026-09-17); TikTok nickname 'Jessmelu | Travel Creator', bio 'Swiss girl, Dubai'",
    "identity_method": "TikTok profile state nickname/bio",
    "content_fit": "pass - 3-day Split Croatia itinerary, TikTok video 7505783025502932246, create_time 2025-05-18 (in 2024-09-17..2026-09-17 window), day-by-day with named venues/activities",
    "content_fit_evidence": "video 7505783025502932246 (2025-05-18) '3 Days in Split, Croatia - The Perfect Itinerary': Day 1 Split Old Town & sea views (coffee on Riva, Diocletian's Palace & Peristyle, Old Town alleys, Marjan Hill sunset, dinner at local konoba); Day 2 island hopping Hvar & Brac (full-day speedboat tour, swim hidden coves Brac, Pakleni Islands dip, lunch in Hvar + old town & fortress); Day 3 adventure in Omis (45 min from Split; zipline over Cetina River canyon, white-water rafting/canyoning, Omis Old Town + riverside lunch); hotel AC Hotel Split",
    "reach_floor": "pass - 538,700 >= 10,000 (dated observation 2026-09-17)",
    "engagement_observed": "video 7505783025502932246: 1,000,000 plays; 65,100 likes; 1,231 comments; 13,100 shares; 9,635 saves (creator-owned video metrics, observed 2026-09-17)",
    "activity_check": "pass - TikTok profile live; urlebird latest visible post 2026-09-16",
    "purchase_intent": "Grayline Croatia boat tour + AC Hotel Split mentioned as recommendations - third-party purchase intent, not creator-hosted",
    "exclusions_check": "pass - individual travel creator; Grayline Croatia/AC Hotel are third-party recommendations, not hosted trips; no consumer trip-planning service; no brand/agency/repost account (observed 2026-09-17)",
    "decision": "accept",
    "notes": "Swiss creator based in Dubai; 3-day Split/Hvar/Brac/Omis itinerary",
  },
]

def build_extraction(a):
    days = [
        {"day": 1, "summary": "Day 1: Split Old Town & sea views", "items": [
            {"type": "restaurant", "name": "Coffee on the Riva", "detail": "start with coffee on the Riva promenade"},
            {"type": "activity", "name": "Diocletian's Palace & the Peristyle", "detail": "explore the palace complex"},
            {"type": "activity", "name": "Split Old Town alleys", "detail": "wander the charming Old Town alleys"},
            {"type": "activity", "name": "Marjan Hill", "detail": "hike or drive up for sunset views"},
            {"type": "restaurant", "name": "Local konoba", "detail": "dinner; fresh seafood by the sea"}]},
        {"day": 2, "summary": "Day 2: Island hopping - Hvar & Brac", "items": [
            {"type": "activity", "name": "Full-day speedboat tour from Split", "detail": "island hopping tour"},
            {"type": "activity", "name": "Hidden coves around Brac", "detail": "swim in hidden coves"},
            {"type": "activity", "name": "Pakleni Islands", "detail": "stop for a dip"},
            {"type": "restaurant", "name": "Lunch in Hvar", "detail": "lunch + explore Hvar old town & fortress"}]},
        {"day": 3, "summary": "Day 3: Adventure in Omis", "items": [
            {"type": "transport", "name": "Split to Omis", "detail": "45 min from Split"},
            {"type": "activity", "name": "Zipline over Cetina River canyon", "detail": "epic canyon views"},
            {"type": "activity", "name": "White-water rafting or canyoning", "detail": "Cetina River"},
            {"type": "activity", "name": "Omis Old Town", "detail": "stroll + riverside lunch"},
            {"type": "hotel", "name": "AC Hotel Split", "detail": "highest building in Split; recommended stay"}]},
    ]
    return {"handle": a["handle"], "platform": PLATFORM,
            "itineraries": [{"title": "3 Days in Split, Croatia - The Perfect Itinerary", "destination": "Split, Hvar, Brac, Omis, Croatia",
                            "source_url": a["source_urls"], "published_date": "2025-05-18", "days": days}],
            "notes": "3-day structured itinerary from creator's TikTok caption; includes stay, transport, food, activities."}

def main():
    u = dedup_universe()
    for a in ACCEPTED:
        if a["handle"].lower() in u:
            print("DEDUP HIT, skipping:", a["handle"]); sys.exit(1)
    with open(f'{BASE}/batch9.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for a in ACCEPTED:
            w.writerow([a["name"], a["handle"], PLATFORM, a["niche"], a["followers_approx"], a["profile_url"], a["source_urls"]])
    with open(f'{BASE}/staging/selection_log_batch9.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for a in ACCEPTED:
            w.writerow(["batch9", a["handle"], PLATFORM, a["name"], a["niche"], a["followers_approx"],
                        a["followers_observed"], a["followers_source"], a["profile_url"], a["discovery_source"],
                        a["identity_check"], a["identity_method"], a["content_fit"], a["content_fit_evidence"],
                        a["reach_floor"], a["engagement_observed"], a["activity_check"], a["purchase_intent"],
                        a["exclusions_check"], a["decision"], a["notes"], CHECK_DATE, SELECTOR])
    ip = f'{BASE}/staging/itineraries_batch9.json'
    d = json.load(open(ip, encoding='utf-8'))
    for a in ACCEPTED:
        d["extractions"].append(build_extraction(a))
    json.dump(d, open(ip, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("wrote", len(ACCEPTED), "to batch9")
    with open(f'{BASE}/staging/tiktok_t2_progress.md', 'a', encoding='utf-8') as f:
        for a in ACCEPTED:
            f.write(f"- 2026-09-17 {SELECTOR}: {a['handle']} -> batch9 | gates: identity pass (mononym) / itinerary in-window / reach {a['followers_approx']} / engagement public / exclusions pass\n")
    print("progress logged")

if __name__ == '__main__':
    main()
