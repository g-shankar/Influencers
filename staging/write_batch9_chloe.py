#!/usr/bin/env python3
"""Append @chloeconortravels to canonical batch9 files (TikTok re-dispatch t2).
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
    "name": "Chloe Conor",
    "handle": "@chloeconortravels",
    "niche": "budget Europe travel",
    "followers_approx": "14.8K",
    "profile_url": "https://www.tiktok.com/@chloeconortravels",
    "source_urls": "https://www.tiktok.com/@chloeconortravels/video/7594054954680126742",
    "followers_observed": "14,800",
    "followers_source": "TikTok profile state __UNIVERSAL_DATA_FOR_REHYDRATION__, observed 2026-09-17",
    "discovery_source": "TikTok discovery re-dispatch 2026-09-17 (t2); lead from batch10_verified_7_handoff.json candidate pipeline",
    "identity_check": "pass - named individual 'Chloe' (surname Conor from handle + contact@chloeconorcontent.com); TikTok nickname 'Chloe | UGC Travel Creator'",
    "identity_method": "TikTok profile state nickname + handle/email",
    "content_fit": "pass - full-day Prague itinerary, TikTok video 7594054954680126742, create_time 2026-01-11 (in 2024-09-17..2026-09-17 window), structured: stay, food, transport, activities",
    "content_fit_evidence": "video 7594054954680126742 (2026-01-11) 'How to spend a day in Prague': stay Prague 1 (central, affordable); architecture walk (Powder Tower, Jakubsky Obvod); brekky at Bakeshop Bakery; Manes Bridge walk toward Prague Castle; Charles Bridge views; tram 22/23 up to Prazsky hrad; panoramic city views; hourly guard change; Kunsthalle Praha; 50-min evening river cruise (GetYourGuide); Groove Bar (cocktails/DJs); Czech meal at Stracha",
    "reach_floor": "pass - 14,800 >= 10,000 (dated observation 2026-09-17)",
    "engagement_observed": "video 7594054954680126742: 49,100 plays; 2,411 likes; 31 comments; 406 shares; 1,765 saves (creator-owned video metrics, observed 2026-09-17)",
    "activity_check": "pass - TikTok profile live; urlebird latest visible post 2026-09-17",
    "purchase_intent": "GetYourGuide 50-min river cruise recommendation (third-party booking) - purchase intent present, not creator-hosted",
    "exclusions_check": "pass - UGC creator (brand content production, not an agency); GetYourGuide cruise is a third-party recommendation, not a hosted trip; no consumer trip-planning service; no brand/agency/repost account (observed 2026-09-17)",
    "decision": "accept",
    "notes": "UK budget-travel creator; Prague full-day itinerary + London content",
  },
]

LOG_COLS = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
"followers_source","profile_url","discovery_source","identity_check","identity_method","content_fit",
"content_fit_evidence","reach_floor","engagement_observed","activity_check","purchase_intent",
"exclusions_check","decision","notes","check_date","selector"]

def build_extraction(a):
    days = [
        {"day": 1, "summary": "Full day in Prague: stay, sights, food, evening cruise", "items": [
            {"type": "hotel", "name": "Stay in Prague 1", "detail": "super central but still affordable"},
            {"type": "activity", "name": "Architecture walk", "detail": "Powder Tower; Jakubsky Obvod street beautiful buildings"},
            {"type": "restaurant", "name": "Bakeshop Bakery", "detail": "breakfast"},
            {"type": "activity", "name": "Manes Bridge walk", "detail": "walk toward Prague Castle; views of Charles Bridge"},
            {"type": "transport", "name": "Tram 22 or 23", "detail": "up the hill to Prazsky hrad (Prague Castle)"},
            {"type": "activity", "name": "Prague Castle panoramic views", "detail": "city panoramas from the castle"},
            {"type": "activity", "name": "Guard change", "detail": "every hour on the hour"},
            {"type": "activity", "name": "Kunsthalle Praha", "detail": "cool modern art gallery"},
            {"type": "activity", "name": "50-minute evening river cruise", "detail": "book via GetYourGuide; scenic views of everything lit up at night"},
            {"type": "restaurant", "name": "Groove Bar", "detail": "cocktails with DJs, nice vibes"},
            {"type": "restaurant", "name": "Stracha", "detail": "Czech meal"},
        ]},
    ]
    return {"handle": a["handle"], "platform": PLATFORM,
            "itineraries": [{"title": "How to spend a day in Prague", "destination": "Prague, Czechia",
                            "source_url": a["source_urls"], "published_date": "2026-01-11", "days": days}],
            "notes": "Single-day structured itinerary from creator's TikTok caption; includes stay, transport, food, activities."}

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
            f.write(f"- 2026-09-17 {SELECTOR}: {a['handle']} -> batch9 | gates: identity pass / itinerary in-window / reach {a['followers_approx']} / engagement public / exclusions pass\n")
    print("progress logged")

if __name__ == '__main__':
    main()
