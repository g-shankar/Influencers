#!/usr/bin/env python3
"""Top-up append for TikTok batch11: @de_knees__ + 11 quarantine exclusions.
Run once 2026-09-17. Uses csv module for exact column handling."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = "2026-09-17"

PROFILE = "https://www.tiktok.com/@de_knees__"
BEIJING_VIDEO = (
    "https://www.tiktok.com/@de_knees__/video/7638622335053909268?_r=1"
    "&_d=secCgYIASAHKAESPgo8KRahB7WIOrjLq%2FJf9g6KgimGQ7ZKzczFRj6I9NYswse9A7V9X31UQ"
    "%2F%2BhYG9AugYowc156XrJaYqcQ0yWGgA%3D&_svg=1&biz_cover_on=1"
    "&checksum=7e11e0dadef0b0de69fb08f6077080e4dfbb8a5b483b2750a2064e997526f2a2"
    "&item_author_type=2&link_reflow_popup_iteration_sharer=%7B%22follow_to_play_duration%22%3A-1%2C%22dynamic_cover%22%3A1%2C%22profile_clickable%22%3A1%7D"
    "&mid=7638622449101261576&preview_pb=0&reflow_page_type=1&reflow_sign_scene=1&region=SG"
    "&rgssign=2.1.6aS3j0JJHrk_3j9wij-U&sec_user_id=MS4wLjABAAAAFK2FjJMIm-v2t0UKeoFZbtNeKtQtv47MM1KaGwNLznt3p-P0iGkp9wvxUJWookeW"
    "&share_app_id=1180&share_item_id=7638622335053909268&share_link_id=B5CE3F97-701D-4DB2-ACEB-A50BF9C897F1"
    "&share_region=SG&share_scene=2&sharer_language=en&social_share_type=0&source=h5_t&sp_level=1"
    "&sp_root_d=secCgYIASAHKAESPgo8KRahB7WIOrjLq%2FJf9g6KgimGQ7ZKzczFRj6I9NYswse9A7V9X31UQ%2F%2BhYG9AugYowc156XrJaYqcQ0yWGgA%3D"
    "&sp_root_share_link_id=B5CE3F97-701D-4DB2-ACEB-A50BF9C897F1&sp_root_u=e669jma2l7l57g&timestamp=1778696969"
    "&tt_from=facebook&u_code=e669jma2l7l57g&ug_btm=b2001&user_id=7194122490075022337&utm_campaign=client_share&utm_medium=ios&utm_source=facebook"
)

# --- dedup: fail closed if handle exists anywhere canonical ---
UNIVERSE = []
for f in [ROOT / "influencers.csv", *[ROOT / f"batch{n}.csv" for n in range(1, 21)]]:
    if f.exists():
        UNIVERSE.append(f)
seen = set()
for f in UNIVERSE:
    with open(f, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            seen.add(row["handle"].strip().lower())
assert "@de_knees__" not in seen, "DEDUP COLLISION: @de_knees__ already selected"

# --- 1. batch11.csv (7 cols) ---
with open(ROOT / "batch11.csv", "a", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow([
        "Denise", "@de_knees__", "tiktok", "asia travel itineraries", "35800",
        PROFILE, f"{PROFILE} | {BEIJING_VIDEO}",
    ])

# --- 2. selection_log_batch11.csv (23 cols) ---
log_cols = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
            "followers_source","profile_url","discovery_source","identity_check","identity_method",
            "content_fit","content_fit_evidence","reach_floor","engagement_observed","activity_check",
            "purchase_intent","exclusions_check","decision","notes","check_date","selector"]
with open(ROOT / "staging" / "selection_log_batch11.csv", "a", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow([
        "11", "@de_knees__", "tiktok", "Denise", "asia travel itineraries", "35800", "35800",
        "TikTok profile card 2026-09-17", PROFILE, "Direct TikTok profile verification",
        "pass", "Named individual: 'Denise | Travels & Lifestyle' on TikTok profile",
        "pass",
        "3D2N Beijing day-by-day itinerary video (Day 1: Grand Metropark Hotel, Taikooli Sanlitun, "
        "Yang Mei Zhu Xie Jie; Day 2: Great Wall of China, Still Water Cafe, cheongsam shopping; "
        "Day 3: Forbidden City, Peking duck); published 2026-05-11",
        "pass",
        "Beijing 3D2N TikTok video: 29,800 plays; 669 likes; 7 comments; 526 shares; 671 saves "
        "(observed 2026-09-17)",
        "pass",
        "Klook Kreator affiliate: captions direct followers to creator's Klook Kreator Shop "
        "(search DENISETANKLOOK) / promo code DENISEKLOOK for extra 5% off activities, stays, "
        "tickets, transport",
        "pass", "include",
        "Profile shows email only, no bio link; no TrovaTrip/WeTravel/personalized-planning or "
        "hosted group-trip services found; Taiwan 5-day trip (Feb 17-21, 2026) video confirms "
        "current 2026 travel posting",
        CHECK, "tiktok-topup-worker",
    ])

# --- 3. itineraries_batch11.json ---
p = ROOT / "staging" / "itineraries_batch11.json"
data = json.loads(p.read_text(encoding="utf-8"))
assert data["batch"] == 11
data["extractions"].append({
    "handle": "@de_knees__",
    "platform": "tiktok",
    "itineraries": [{
        "confidence": "high",
        "country": "China",
        "days": 3,
        "destination": "Beijing",
        "items": [
            {"booking_link": None, "day": 1,
             "details": "Check-in at Grand Metropark Hotel; shop at Taikooli Sanlitun; walk the cultural streets at Yang Mei Zhu Xie Jie.",
             "item_type": "hotel", "location": "Beijing",
             "name": "Grand Metropark Hotel & Sanlitun", "price_hint": None},
            {"booking_link": None, "day": 2,
             "details": "Great Wall of China; Still Water Cafe; cheongsam shopping at 戚薇国风服饰 or stroll at Nan Luo Gu Xiang.",
             "item_type": "activity", "location": "Beijing",
             "name": "Great Wall & cheongsam shopping", "price_hint": None},
            {"booking_link": None, "day": 3,
             "details": "Forbidden City; Peking duck at 四季民福 (Siji Minfu).",
             "item_type": "activity", "location": "Beijing",
             "name": "Forbidden City & Peking duck", "price_hint": None},
        ],
        "source_urls": [BEIJING_VIDEO],
        "summary": "Denise (@de_knees__) publishes a 3D2N Beijing day-by-day itinerary on TikTok covering "
                   "Sanlitun shopping and hutong streets (Day 1), the Great Wall with cheongsam shopping "
                   "(Day 2), and the Forbidden City with Peking duck (Day 3); published 2026-05-11.",
        "title": "3D2N Beijing itinerary",
    }],
    "notes": "Day-by-day 3D2N Beijing itinerary from TikTok video caption; specific stops per day; "
             "published within trailing 24 months (2026-05-11 raw create_time).",
})
p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# --- 4. quarantine.json: 11 new excluded handles ---
q_path = ROOT / "validation" / "quarantine.json"
q = json.loads(q_path.read_text(encoding="utf-8"))
existing = {e["handle"].lower() for e in q["quarantine"]}
new_fails = [
    ("@diana_travels_", "TikTok profile 2026-09-17: 2,137 followers (< 10,000 reach floor)"),
    ("@emilyytravelss", "TikTok profile 2026-09-17: 2,499 followers (< 10,000 reach floor)"),
    ("@mydestinationdiaries", "TikTok profile 2026-09-17: 4,773 followers (< 10,000 reach floor)"),
    ("@dg_travel", "Shared/couple account: TikTok bio 'Giulia & Donato' observed 2026-09-17 (13,400 followers); no named individual established"),
    ("@ladytrailmix", "TikTok profile 2026-09-17: 1,599 followers (< 10,000 reach floor)"),
    ("@vannypacktravels", "TikTok profile 2026-09-17: 186 followers (< 10,000 reach floor)"),
    ("@global.and.beyond.travel", "Excluded during 2026-09-17 TikTok top-up verification (failure detail in worker notes); handle not selected in any batch"),
    ("@dailyblissna2", "Excluded during 2026-09-17 TikTok top-up verification (failure detail in worker notes); handle not selected in any batch"),
    ("@gabstraveljournal", "Excluded during 2026-09-17 TikTok top-up verification (failure detail in worker notes); handle not selected in any batch"),
    ("@thisatravels", "Excluded during 2026-09-17 TikTok top-up verification (failure detail in worker notes); handle not selected in any batch"),
    ("@bellahoppa", "Excluded during 2026-09-17 TikTok top-up verification (failure detail in worker notes); handle not selected in any batch"),
]
added = 0
for handle, reason in new_fails:
    if handle.lower() in existing:
        continue
    q["quarantine"].append({"added": CHECK, "handle": handle, "platform": "tiktok",
                            "reason": reason, "status": "excluded"})
    added += 1
q_path.write_text(json.dumps(q, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print(f"de_knees__ appended to batch11 (+1); quarantine added {added} new entries; "
      f"quarantine total now {len(q['quarantine'])}")
