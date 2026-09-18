#!/usr/bin/env python3
"""Append @jetset_anna to canonical batch9 files (TikTok re-dispatch t2).
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
    "name": "Anna",
    "handle": "@jetset_anna",
    "niche": "luxury travel",
    "followers_approx": "408.2K",
    "profile_url": "https://www.tiktok.com/@jetset_anna",
    "source_urls": "https://www.tiktok.com/@jetset_anna/video/7667150847817567510",
    "followers_observed": "408,200",
    "followers_source": "TikTok profile state __UNIVERSAL_DATA_FOR_REHYDRATION__, observed 2026-09-17",
    "discovery_source": "TikTok discovery re-dispatch 2026-09-17 (t2); lead from wave3_batch11_log.md top-up pool (prior date-unverifiable rejection resolved with exact video ID + create_time)",
    "identity_check": "pass - mononym 'Anna' (mononym allowed per SELECTION_CRITERIA.md coordinator adjudication 2026-09-17); consistent public operator identity across handle @jetset_anna, email hello@jetsetanna.com, IG @jetset_anna",
    "identity_method": "TikTok profile state nickname/bio + email/IG consistency",
    "content_fit": "pass - 7-day Taiwan itinerary, TikTok video 7667150847817567510, create_time 2026-07-27 (in 2024-09-17..2026-09-17 window), day-by-day with named venues/activities",
    "content_fit_evidence": "video 7667150847817567510 (2026-07-27) 'How to spend a week in Taiwan': Days 1-3 Taipei (Chiang Kai-Shek Memorial Hall guard change, Taipei 101, Din Tai Fung, temples, night markets); Days 4-5 Kenting (high-speed rail south, coastal walks, SUP, night market); Day 6 Tainan (Confucius Temple, Pung-tang candy making, indigo dyeing at Blueprint Park, Shennong Street); Day 7 Shifen & Jiufen (sky lantern release, mountain tea tasting, Jiufen lantern-lit streets)",
    "reach_floor": "pass - 408,200 >= 10,000 (dated observation 2026-09-17)",
    "engagement_observed": "video 7667150847817567510: 47,900 plays; 2,309 likes; 5 comments; 127 shares; 370 saves (creator-owned video metrics, observed 2026-09-17)",
    "activity_check": "pass - TikTok profile live; urlebird latest visible post 2026-08-17",
    "purchase_intent": "video marked 'ad' / in collaboration with @tourtaiwantta_uk (Taiwan Tourism Administration UK) - tourism-board sponsored collaboration, not creator-hosted trip selling",
    "exclusions_check": "pass - tourism-board sponsored itinerary content (brand collaboration, allowed per prior adjudications); no hosted group trips sold by creator; no consumer trip-planning service; no brand/agency/repost account (observed 2026-09-17)",
    "decision": "accept",
    "notes": "UK/Cotswolds luxury travel creator; 7-day Taiwan itinerary (tourism-board collaboration)",
  },
]

def build_extraction(a):
    days = [
        {"day": 1, "summary": "Days 1-3: Taipei", "items": [
            {"type": "activity", "name": "Chiang Kai-Shek Memorial Hall", "detail": "watching the changing of the guards"},
            {"type": "activity", "name": "Taipei 101", "detail": "taking in the views"},
            {"type": "restaurant", "name": "Din Tai Fung", "detail": "in its home country"},
            {"type": "activity", "name": "Taipei temples", "detail": "exploring beautiful temples"},
            {"type": "activity", "name": "Taipei night markets", "detail": "buzzing night markets"}]},
        {"day": 4, "summary": "Days 4-5: Kenting", "items": [
            {"type": "transport", "name": "Taiwan high-speed rail", "detail": "travelling south to Kenting"},
            {"type": "activity", "name": "Kenting coastal walks", "detail": "breathtaking coastal views"},
            {"type": "activity", "name": "SUP in Kenting", "detail": "stand-up paddleboard in crystal-clear waters"},
            {"type": "activity", "name": "Kenting night market", "detail": "eating around the night market"}]},
        {"day": 6, "summary": "Day 6: Tainan", "items": [
            {"type": "activity", "name": "Confucius Temple", "detail": "Tainan"},
            {"type": "activity", "name": "Pung-tang candy making", "detail": "traditional candy making experience"},
            {"type": "activity", "name": "Indigo dyeing at Blueprint Park", "detail": "creative indigo dyeing"},
            {"type": "activity", "name": "Shennong Street", "detail": "wandering the magical streets, evening"}]},
        {"day": 7, "summary": "Day 7: Shifen & Jiufen", "items": [
            {"type": "activity", "name": "Sky lantern release in Shifen", "detail": "releasing a sky lantern"},
            {"type": "activity", "name": "Traditional tea tasting", "detail": "overlooking the mountains"},
            {"type": "activity", "name": "Jiufen lantern-lit streets", "detail": "magical lantern-lit streets; said to have inspired Spirited Away scenes"}]},
    ]
    return {"handle": a["handle"], "platform": PLATFORM,
            "itineraries": [{"title": "How to spend a week in Taiwan", "destination": "Taiwan (Taipei, Kenting, Tainan, Shifen, Jiufen)",
                            "source_url": a["source_urls"], "published_date": "2026-07-27", "days": days}],
            "notes": "7-day structured itinerary from creator's TikTok caption (tourism-board collaboration with Tour Taiwan UK)."}

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
