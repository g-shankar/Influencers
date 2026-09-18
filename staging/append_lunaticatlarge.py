#!/usr/bin/env python3
"""Stage 2 closer: append @lunaticatlarge (Kristin Luna) to Batch 20.

Evidence gathered 2026-09-17 (non-login sources only). Appends only. Writes:
  - batch20.csv (7 cols)
  - staging/selection_log_batch20.csv (23 cols)
  - staging/itineraries_batch20.json (extraction object)
  - staging/dedup_universe_2026-09-17.txt (new handle)

Engagement: unknown (nonblocking) per the 2026-09-17 Batch 20 final-decision
precedent (third-party engagement tools not publicly accessible 2026-09-17).
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK_DATE = "2026-09-17"
SELECTOR = "batch20-topup"


def item(item_type, name, day, description):
    return {
        "item_type": item_type,
        "name": name,
        "day": day,
        "description": description,
        "booking_link": None,
        "price_hint": None,
    }


# ---------------------------------------------------------------- batch20.csv
BATCH_ROWS = [
    ["Kristin Luna", "@lunaticatlarge", "instagram", "travel / food / design journalism",
     "27700", "https://www.instagram.com/lunaticatlarge/",
     "https://www.camelsandchocolate.com/best-things-to-do-in-tupelo-mississippi/"],
]

# ------------------------------------------------------- selection log (23 col)
LOG_ROWS = [
    ["20", "@lunaticatlarge", "instagram", "Kristin Luna", "travel / food / design journalism",
     "27700", "27.7K",
     "Feedspot Top 100 Female Travel Influencers 2026 list observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/lunaticatlarge/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Kristin Luna identified as a travel writer/photographer whose personal blog is Camels & Chocolate "
     "(Gala Darling interview); Feedspot entry gives exact handle @lunaticatlarge with her bio ('Journalist "
     "of travel, food + design; Photographer of people + places; Public art curator + mural lover; Tennessean') "
     "and camelsandchocolate.com/blog",
     "pass",
     "'How to Spend a Weekend in Tupelo, Mississippi: A Travel Guide' on own site (search index: last updated "
     "~29 days before 2026-09-17; image paths dated 2026/06): structured Day 1/2/3 - Day 1 downtown Tupelo "
     "(murals and It's Electric Neon Lights Trail; MLM Clothiers, Bolt, Reed's; Caron Gallery, GumTree Museum "
     "of Art; Lost + Found Coffee Co.; Queen's Reward Meadery tasting; Stables Downtown Grill), Day 2 Elvis "
     "footsteps (Talbot House Bakery & Cafe; Elvis Presley Birthplace; Johnnie's Drive-In; Elvis' Tupelo "
     "Driving Tour; Tupelo Hardware Company; Forklift dinner; Blue Canoe live music), Day 3 (Natchez Trace "
     "Parkway Visitor Center milepost 266; Chickasaw Village Site; Tombigbee State Park; Oren Dunn City "
     "Museum; Crave Tupelo dessert bar); named hotels Hotel Tupelo and Holiday Inn & Suites Tupelo North. "
     "Full item detail harvested from the opened page. Post created in partnership with Visit Tupelo "
     "(press partnership, not a consumer service).",
     "pass",
     "unknown (nonblocking) - third-party engagement tools not publicly accessible 2026-09-17; per the "
     "2026-09-17 Batch 20 final-decision precedent engagement is nonblocking for all includes",
     "pass (Tupelo guide updated ~mid-August 2026 per search index; Pickwick Lake guide updated ~17 days "
     "before 2026-09-17; Elvis-in-Tupelo guide updated ~74 days before)",
     "present (named hotels: Hotel Tupelo, Holiday Inn & Suites Tupelo North; named restaurants, paid tours "
     "and activities throughout)",
     "pass - targeted 2026-09-17 searches found no consumer itinerary planning/coaching/courses/workshops/"
     "hosted group trips/agency offer tied to Kristin Luna or @lunaticatlarge; described work is professional "
     "travel journalism (guidebook/magazine assignments) and editorial blogging",
     "include",
     "Named individual (Kristin Luna). Qualifying Tupelo weekend guide updated mid-August 2026 (in window). "
     "Reach 27.7K IG (Feedspot). Item-level content harvested from the opened guide page.",
     CHECK_DATE, SELECTOR],
]

# ------------------------------------------------- itineraries_batch20.json
EXTRACTIONS = [
    {
        "handle": "@lunaticatlarge",
        "platform": "instagram",
        "notes": "Kristin Luna: named individual travel writer/photographer; Camels & Chocolate is her "
                 "personal blog (interview bio; Feedspot entry). Reach: 27.7K Instagram per Feedspot Top 100 "
                 "Female Travel Influencers 2026 (observed 2026-09-17). Qualifying guide: 'How to Spend a "
                 "Weekend in Tupelo, Mississippi' on her own site (updated ~mid-August 2026), structured "
                 "Day 1/2/3 with named hotels, restaurants and paid activities. Exclusion sweep 2026-09-17 "
                 "found no consumer services; the Visit Tupelo credit is a press partnership. Items harvested "
                 "from the opened guide page.",
        "itineraries": [
            {
                "title": "How to Spend a Weekend in Tupelo, Mississippi: A Travel Guide",
                "destination": "Tupelo, Mississippi",
                "country": "United States",
                "days": 3,
                "summary": "A structured 3-day Tupelo weekend on the creator's own site (updated ~mid-August "
                           "2026): Day 1 downtown Tupelo (murals and the It's Electric Neon Lights Trail, "
                           "shopping at MLM Clothiers/Bolt/Reed's, Caron Gallery and GumTree Museum of Art, "
                           "Lost + Found Coffee Co., Queen's Reward Meadery tasting, dinner at Stables "
                           "Downtown Grill); Day 2 Elvis footsteps (Talbot House Bakery & Cafe, Elvis Presley "
                           "Birthplace, Johnnie's Drive-In, Elvis' Tupelo Driving Tour, Tupelo Hardware "
                           "Company, Forklift dinner, Blue Canoe live music); Day 3 Natchez Trace Parkway "
                           "Visitor Center, Chickasaw Village Site, Tombigbee State Park, Oren Dunn City "
                           "Museum, and Crave Tupelo dessert bar.",
                "source_urls": ["https://www.camelsandchocolate.com/best-things-to-do-in-tupelo-mississippi/"],
                "confidence": "high",
                "items": [
                    item("hotel", "Hotel Tupelo", 1,
                         "Boutique hotel in downtown Tupelo close to restaurants, shops and live music; "
                         "alternative: Holiday Inn & Suites Tupelo North"),
                    item("activity", "Downtown Tupelo murals and It's Electric Neon Lights Trail", 1,
                         "Day 1: explore downtown murals and neon installations; the guide recommends "
                         "downloading the It's Electric: Neon Lights Trail for public art after dark"),
                    item("activity", "Downtown shopping: MLM Clothiers, Bolt, Reed's", 1,
                         "Day 1: MLM Clothiers (one of Mississippi's oldest menswear stores), Bolt "
                         "(rock-and-roll aesthetic boutique), Reed's (Tupelo institution since 1905) and "
                         "Reed's GumTree Bookstore"),
                    item("activity", "Caron Gallery and GumTree Museum of Art", 1,
                         "Day 1: browse contemporary Southern artists at the Caron Gallery, then the "
                         "GumTree Museum of Art (showcasing regional artists for 40+ years)"),
                    item("restaurant", "Lost + Found Coffee Co.", 1,
                         "Day 1 caffeine break: specialty roastery; the guide orders a cereal milk latte or "
                         "pour-over with a pastry"),
                    item("activity", "Queen's Reward Meadery tasting", 1,
                         "Day 1: Mississippi's first and only meadery - guided tasting flights, mead-and-cheese "
                         "pairings and mead slushie flights from the female-owned, small-batch producer"),
                    item("restaurant", "Stables Downtown Grill", 1,
                         "Day 1 dinner: blackened catfish nachos and Southern classics; the alley patio is "
                         "one of Tupelo's best outdoor dining spots"),
                    item("restaurant", "Talbot House Bakery & Cafe", 2,
                         "Day 2 breakfast: house-made pastries, cinnamon rolls in various flavors and enormous "
                         "chocolate chip cookies"),
                    item("activity", "Elvis Presley Birthplace", 2,
                         "Day 2: the modest two-room shotgun house built by Vernon Presley, plus the museum, "
                         "the Assembly of God church where Elvis discovered gospel music, memorial gardens, "
                         "the Becoming sculpture and the Reflections area"),
                    item("restaurant", "Johnnie's Drive-In", 2,
                         "Day 2 lunch: the cash-only diner serving Tupelo since 1945 where Elvis was a "
                         "regular - order a doughburger and ask for the famous Elvis booth"),
                    item("activity", "Elvis' Tupelo Driving Tour", 2,
                         "Day 2 afternoon: the driving tour past the original Reed's Department Store, "
                         "Elvis' schools and the historic Shake Rag neighborhood"),
                    item("activity", "Tupelo Hardware Company", 2,
                         "Day 2: the store where an 11-year-old Elvis arrived hoping for a bicycle and left "
                         "with a $7.75 guitar; being preserved as an interpretive attraction"),
                    item("restaurant", "Forklift", 2,
                         "Day 2 dinner: elevated Southern cuisine with creative cocktails and seasonal menus; "
                         "patio tables on warm evenings"),
                    item("activity", "Blue Canoe live music", 2,
                         "Day 2 late night: Southern comfort food, craft beer and live music at Blue Canoe; "
                         "its Cathead Stage hosted Chris Stapleton, Jason Isbell and others pre-fame"),
                    item("activity", "Natchez Trace Parkway Visitor Center (milepost 266)", 3,
                         "Day 3: start at the Parkway Visitor Center at milepost 266 for exhibits and ranger "
                         "trail recommendations along the 444-mile scenic route"),
                    item("activity", "Chickasaw Village Site", 3,
                         "Day 3: short interpretive trail through the former Chickasaw village site with "
                         "exhibits on Chickasaw life and culture"),
                    item("activity", "Tombigbee State Park", 3,
                         "Day 3 outdoor excursion: the park around Lake Lee offers hiking, fishing, paddling "
                         "and disc golf, plus cabins and campsites"),
                    item("activity", "Oren Dunn City Museum at Ballard Park", 3,
                         "Day 3: restored dairy barn museum tracing Tupelo's history through its people, "
                         "industries and events; caboose and relics for photos"),
                    item("restaurant", "Crave Tupelo dessert bar", 3,
                         "Day 3 finale: downtown dessert bar known for over-the-top sweets; opens evenings on "
                         "Sundays"),
                ],
            }
        ],
    },
]


def main():
    # 1. batch20.csv (append, 7 cols)
    bp = ROOT / "batch20.csv"
    with open(bp, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(BATCH_ROWS)

    # 2. selection log (append, 23 cols)
    lp = ROOT / "staging" / "selection_log_batch20.csv"
    with open(lp, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(LOG_ROWS)

    # 3. itineraries json (append extractions)
    jp = ROOT / "staging" / "itineraries_batch20.json"
    data = json.loads(jp.read_text(encoding="utf-8"))
    data["extractions"].extend(EXTRACTIONS)
    jp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # 4. universe (append new handles)
    up = ROOT / "staging" / "dedup_universe_2026-09-17.txt"
    existing = {ln.strip().lower() for ln in up.read_text(encoding="utf-8").splitlines() if ln.strip()}
    new_handles = [ex["handle"] for ex in EXTRACTIONS]
    dupes = [h for h in new_handles if h.lower() in existing]
    if dupes:
        raise SystemExit(f"DEDUP VIOLATION: already in universe: {dupes}")
    with open(up, "a", encoding="utf-8") as f:
        for h in new_handles:
            f.write(h + "\n")

    print(f"appended {len(BATCH_ROWS)} batch rows, {len(LOG_ROWS)} log rows, "
          f"{len(EXTRACTIONS)} extractions, {len(new_handles)} universe handles")


if __name__ == "__main__":
    main()
