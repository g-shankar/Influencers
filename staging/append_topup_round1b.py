#!/usr/bin/env python3
"""Round 1b: fix Raymond Cua's handle spelling + append Aileen Adalid and Amanda O'Brien.
Worknotes evidence (actual-page) uses @TravellinFoodie (Food IG @TravellinFoodie,
travel IG @JourneyTraveler); round-1a wrote @travellingfoodie. Correcting to the
evidence-backed spelling, lowercased per file convention.
"""
import csv, json, os

BASE = "/home/hatch/workspace/travel-influencer-pilot"

def sub(path, old, new):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    n = s.count(old)
    assert n > 0, (path, old)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s.replace(old, new))
    return n

# 1. handle spelling correction (scoped: '@'-prefixed handle + instagram.com path only)
n1 = sub(f"{BASE}/batch15.csv", "@travellingfoodie", "@travellinfoodie")
n2 = sub(f"{BASE}/batch15.csv", "instagram.com/travellingfoodie/", "instagram.com/travellinfoodie/")
n3 = sub(f"{BASE}/staging/selection_log_batch15.csv", "@travellingfoodie", "@travellinfoodie")
n4 = sub(f"{BASE}/staging/selection_log_batch15.csv", "instagram.com/travellingfoodie/", "instagram.com/travellinfoodie/")
n5 = sub(f"{BASE}/staging/itineraries_batch15.json", '"@travellingfoodie"', '"@travellinfoodie"')
print("replacements:", n1, n2, n3, n4, n5)

# also fix the followers_source note in Raymond's log row to record the spelling correction
sub(f"{BASE}/staging/selection_log_batch15.csv",
    "feedspot influencer directory (observed 2026-09-17)",
    "feedspot influencer directory (observed 2026-09-17; handle spelling corrected to @TravellinFoodie per creator's own IG reference in worknotes)") \
    if False else None  # skip: would hit other rows too. Handle in notes only.

# 2. append Aileen + Amanda to batch15.csv
batch_rows = [
    ["Aileen Adalid", "@i_am_aileen", "instagram", "travel", "111.5K",
     "https://www.instagram.com/i_am_aileen/",
     "https://iamaileen.com/about/|https://iamaileen.com/tokyo-itinerary/"],
    ["Amanda O'Brien", "@theboutiqueadventurer", "instagram", "travel", "72.5K",
     "https://www.instagram.com/theboutiqueadventurer/",
     "https://theboutiqueadventurer.com/ive-spent-years-exploring-scotland-heres-the-10-day-itinerary-i-always-recommend/"],
]
with open(f"{BASE}/batch15.csv", "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(batch_rows)

# 3. selection log rows (23 cols)
COLS = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
        "followers_source","profile_url","discovery_source","identity_check","identity_method",
        "content_fit","content_fit_evidence","reach_floor","engagement_observed","activity_check",
        "purchase_intent","exclusions_check","decision","notes","check_date","selector"]

def row(handle, name, niche, fol, ident_method, fit_evidence, activity, exclusions, notes):
    return {
        "batch": "15", "handle": handle, "platform": "instagram", "name": name,
        "niche": niche, "followers_approx": fol, "followers_observed": fol,
        "followers_source": "feedspot influencer directory (observed 2026-09-17)",
        "profile_url": f"https://www.instagram.com/{handle.lstrip('@')}/",
        "discovery_source": "feedspot influencer directory",
        "identity_check": "pass", "identity_method": ident_method,
        "content_fit": "pass", "content_fit_evidence": fit_evidence,
        "reach_floor": "pass", "engagement_observed": "unknown",
        "activity_check": activity, "purchase_intent": "unknown",
        "exclusions_check": exclusions, "decision": "include",
        "notes": notes, "check_date": "2026-09-17", "selector": "batch15-topup",
    }

log_rows = [
    row("@i_am_aileen", "Aileen Adalid", "travel", "111.5K",
        "About page identifies Aileen Adalid as the single individual behind iamaileen.com; first-person voice; no team or staff language.",
        "Own site hosts a structured Tokyo itinerary and DIY travel guide at https://iamaileen.com/tokyo-itinerary/ published 2022-10-17, dateModified 2025-06-22 (actual page meta): day/district structure covering Shibuya, Harajuku, Shinjuku, Asakusa, Akihabara, Sumida and more, with transit, hotel, restaurant and activity guidance.",
        "Homepage shows recent posts (Zambia visa guide, Batanes 2026); actively publishing in 2025-2026.",
        "pass",
        "No trip planning, coaching, or hosted group trips found; affiliate Klook code and B2B brand work only (allowed)."),
    row("@theboutiqueadventurer", "Amanda O'Brien", "travel", "72.5K",
        "Itinerary page identifies Amanda O'Brien as creator and editor; first-person travel voice; on-page bio presents a single individual; no team language.",
        "Own site hosts a detailed 10-day Scottish Highlands itinerary at https://theboutiqueadventurer.com/ive-spent-years-exploring-scotland-heres-the-10-day-itinerary-i-always-recommend/ published and modified 2026-08-09 (actual page meta): route covers Glasgow, Glen Coe/Fort William, Isle of Skye, Ullapool, Durness, Thurso and Inverness, with hotels, restaurants, transport and activities.",
        "Itinerary published 2026-08-09; actively publishing in 2025-2026.",
        "pass",
        "Affiliate disclosure only; no consumer-facing planning, itinerary services, coaching, or hosted group trips found."),
]
with open(f"{BASE}/staging/selection_log_batch15.csv", "a", newline="", encoding="utf-8") as f:
    csv.DictWriter(f, fieldnames=COLS).writerows(log_rows)

# 4. extractions
def item(item_type, name, location, details, day=None):
    return {"booking_link": "unknown", "day": day, "details": details,
            "item_type": item_type, "location": location, "name": name,
            "price_hint": "unknown"}

extractions = [
    {
        "handle": "@i_am_aileen", "platform": "instagram",
        "itineraries": [{
            "confidence": "medium", "country": "Japan", "days": None,
            "destination": "Tokyo, Japan",
            "source_url": "https://iamaileen.com/tokyo-itinerary/",
            "published": "2022-10-17", "modified": "2025-06-22",
            "items": [
                item("activity", "Shibuya district guide", "Shibuya, Tokyo",
                     "District section of the Tokyo itinerary covering Shibuya sights and activities."),
                item("activity", "Harajuku district guide", "Harajuku, Tokyo",
                     "District section of the Tokyo itinerary covering Harajuku sights and activities."),
                item("activity", "Shinjuku district guide", "Shinjuku, Tokyo",
                     "District section of the Tokyo itinerary covering Shinjuku sights and activities."),
                item("activity", "Asakusa district guide", "Asakusa, Tokyo",
                     "District section of the Tokyo itinerary covering Asakusa sights and activities."),
                item("activity", "Akihabara district guide", "Akihabara, Tokyo",
                     "District section of the Tokyo itinerary covering Akihabara sights and activities."),
                item("activity", "Sumida district guide", "Sumida, Tokyo",
                     "District section of the Tokyo itinerary covering Sumida sights and activities."),
                item("transport", "Tokyo transit guidance", "Tokyo",
                     "Guide covers transit options for moving between districts; specific lines not captured in this extraction."),
                item("hotel", "Tokyo hotel recommendations", "Tokyo",
                     "Guide includes hotel recommendations; specific properties not captured in this extraction."),
                item("restaurant", "Tokyo restaurant recommendations", "Tokyo",
                     "Guide includes restaurant recommendations; specific venues not captured in this extraction."),
            ]}],
        "notes": "Structured Tokyo itinerary and DIY travel guide published 2022-10-17, dateModified 2025-06-22 by Aileen Adalid. District-level structure extracted; per-venue names were not captured in this pass and should be completed on re-verification before the pilot consumes it.",
    },
    {
        "handle": "@theboutiqueadventurer", "platform": "instagram",
        "itineraries": [{
            "confidence": "medium", "country": "United Kingdom", "days": 10,
            "destination": "Scottish Highlands: Glasgow > Glen Coe/Fort William > Isle of Skye > Ullapool > Durness > Thurso > Inverness",
            "source_url": "https://theboutiqueadventurer.com/ive-spent-years-exploring-scotland-heres-the-10-day-itinerary-i-always-recommend/",
            "published": "2026-08-09", "modified": "2026-08-09",
            "items": [
                item("activity", "Glasgow", "Glasgow, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Glen Coe and Fort William", "Scottish Highlands",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Isle of Skye", "Isle of Skye, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Ullapool", "Ullapool, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Durness", "Durness, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Thurso", "Thurso, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("activity", "Inverness", "Inverness, Scotland",
                     "Stop on the 10-day Scottish Highlands itinerary route."),
                item("transport", "Self-drive routing", "Scottish Highlands",
                     "Driving route connecting the itinerary stops across the 10 days; specific transport bookings not captured in this extraction."),
                item("hotel", "Highlands hotel recommendations", "Scottish Highlands",
                     "Guide names hotels along the route; specific properties not captured in this extraction."),
                item("restaurant", "Highlands restaurant recommendations", "Scottish Highlands",
                     "Guide names restaurants along the route; specific venues not captured in this extraction."),
            ]}],
        "notes": "Detailed 10-day Scottish Highlands itinerary published/modified 2026-08-09 by Amanda O'Brien. Route-level structure extracted; per-stop days, venues and bookings were not captured in this pass and should be completed on re-verification before the pilot consumes it.",
    },
]

path = f"{BASE}/staging/itineraries_batch15.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)
data["extractions"].extend(extractions)
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("round 1b done: handle fixed, 2 creators appended")
