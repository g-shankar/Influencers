#!/usr/bin/env python3
"""Stage 2 CLOSER round 2: append 7 genuine-pass top-ups to Batch 20.

Appends only. Writes:
  - batch20.csv (7 cols)
  - staging/selection_log_batch20.csv (23 cols)
  - staging/itineraries_batch20.json (extraction objects)
  - staging/dedup_universe_2026-09-17.txt (new handles)

Evidence basis: browser evidence gathered 2026-09-17. No invented fields.
Every booking_link is None. Items exist only where grounded in opened pages.
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
    ["Jayne Gorman", "@jayneytravels", "instagram", "Austria / European weekend travel",
     "72000", "https://www.instagram.com/jayneytravels/",
     "https://jayneytravels.com/weekend-guide-to-linz-the-donau-region-upper-austria/; "
     "https://jayneytravels.com/wp-content/uploads/2026/03/jayneytravels-media-kit-2026-hotels.pdf"],
    ["Christina Guan", "@happytowander", "instagram", "Europe backpacking / city guides",
     "66100", "https://www.instagram.com/happytowander/",
     "https://happytowander.com/western-europe-backpacking-itinerary/; https://happytowander.com/work-with-me/"],
    ["Michael Turtle", "@michaelturtle", "instagram", "slow / cultural travel",
     "15534", "https://www.instagram.com/michaelturtle/",
     "https://www.timetravelturtle.com/greece/three-days-in-athens-itinerary/; https://www.timetravelturtle.com/work-with-me/"],
    ["Clint Johnston", "@triphackr", "instagram", "Central America / adventure travel",
     "150000", "https://www.instagram.com/triphackr/",
     "https://triphackr.com/now-is-the-time-to-discover-el-salvador/; https://triphackr.com/work-with-me/"],
    ["Matthew Karsten", "@expertvagabond", "instagram", "adventure / road-trip travel",
     "131100", "https://www.instagram.com/expertvagabond/",
     "https://expertvagabond.com/ring-road-trip-iceland/"],
    ["Christine Tran Ferguson", "@tourdelust", "instagram", "city travel guides / luxury travel",
     "533400", "https://www.instagram.com/tourdelust/",
     "https://tourdelust.com/istanbul-travel-guide-3-day-itinerary/; https://tourdelust.com/about/"],
    ["Lauren Carey", "@girlgoneabroad", "instagram", "Arctic / northern lights / photography travel",
     "100800", "https://www.instagram.com/girlgoneabroad/",
     "https://www.girlgoneabroad.com/blog/tromso-northern-lights-guide-with-photography-tips"],
]

# ------------------------------------------------------- selection log (23 col)
LOG_ROWS = [
    ["20", "@jayneytravels", "instagram", "Jayne Gorman", "Austria / European weekend travel",
     "72000", "72000",
     "https://jayneytravels.com/wp-content/uploads/2026/03/jayneytravels-media-kit-2026-hotels.pdf",
     "https://www.instagram.com/jayneytravels/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Creator-owned 2026 media kit and site identify Jayne Gorman (jayneytravels.com)",
     "pass",
     "Weekend guide to Linz & the Donau region (Upper Austria); page states it is the itinerary she recommends "
     "based on her trip; search-indexed plan lists Ryanair to Linz, Riverresort Donauschlinge / Hotel Wesenufer, "
     "e-bikes, Linz Card",
     "pass", "8% per creator-owned 2026 media kit",
     "pass (creator-owned 2026 media kit; sitemap timestamp 2025-07-30; site active)",
     "present (hotel and transport recommendations: named hotels, Linz Card)",
     "pass - work-with-me offers social campaigns, blog posts, UGC, press trips to brands/tourism boards (B2B); "
     "no consumer itinerary-planning/coaching/courses/hosted trips",
     "include",
     "Named individual. Qualifying Linz long-weekend itinerary. Reach from creator-owned 2026 media kit "
     "(72K IG, 8% engagement).",
     CHECK_DATE, SELECTOR],
    ["20", "@happytowander", "instagram", "Christina Guan", "Europe backpacking / city guides",
     "66100", "66100",
     "Keepface influencer profile snapshot for instagram.com/happytowander observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/happytowander/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Own site identifies Christina Guan; Keepface profile links instagram.com/happytowander; own post copy signs "
     "'I'm Christina from @happytowander'",
     "pass",
     "Western Europe backpacking itinerary (guide title carries '2026 Update'); structured 1.5-month route; "
     "search-indexed content covers Brussels Days 1-3 and Amsterdam Days 1-3 with walking tours, city cards, and day trips",
     "pass", "2,519 engagements per Keepface snapshot",
     "pass (guide titled 2026 Update; own site active)",
     "present (city cards, tours, intercity transport recommendations)",
     "pass - work-with-me offers tourism-board/brand campaigns (B2B); Europe planner is a free fillable PDF lead "
     "magnet in the VIP Zone, not a paid course; no consumer planning/coaching/hosted trips",
     "include",
     "Named individual (Christina Guan). Qualifying 1.5-month Western Europe itinerary. Free planner PDF is a lead "
     "magnet, not a paid course.",
     CHECK_DATE, SELECTOR],
    ["20", "@michaelturtle", "instagram", "Michael Turtle", "slow / cultural travel",
     "15534", "15534",
     "Keepface influencer profile snapshot explicitly linked to instagram.com/michaelturtle observed 2026-09-17 "
     "(verbatim URL not retained)",
     "https://www.instagram.com/michaelturtle/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Own author pages identify Michael Turtle; Keepface profile explicitly links instagram.com/michaelturtle",
     "pass",
     "Three-day Athens itinerary guide on own site; page states the guide is current 'As of July 2026'",
     "pass", "0.66% per Keepface snapshot",
     "pass (Athens guide 'As of July 2026'; Keepface shows Tokyo 2025 posts with #PR brand activity)",
     "unknown",
     "pass - own work-with-me offers sponsored trips/posts, photography/content production, social events, "
     "speaking, affiliate marketing (all B2B); contact page distinguishes business collaboration from reader "
     "questions; no consumer planning/coaching/courses/hosted trips",
     "include",
     "Named individual. Qualifying 3-day Athens itinerary. Item-level content not harvested this session; "
     "no items invented.",
     CHECK_DATE, SELECTOR],
    ["20", "@triphackr", "instagram", "Clint Johnston", "Central America / adventure travel",
     "150000", "150000",
     "https://triphackr.com/work-with-me/",
     "https://www.instagram.com/triphackr/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Own author page (triphackr.com/author/clint/) identifies Clint Johnston; El Salvador guide explicitly "
     "authored by Clint Johnston",
     "pass",
     "'Sample 5-Day Route from Coco Surf' in the El Salvador guide, explicitly authored by Clint Johnston; "
     "Day 1-5 items harvested from the opened page",
     "pass", "1.03% per Keepface snapshot",
     "pass (creator-owned work page cites 150,000+ verified Instagram; guide live)",
     "present (hotel base, surf and activity spend)",
     "pass - own work-with-me offers partnerships with brands, tourism boards, hotels, airlines, and travel "
     "companies (B2B); no consumer planning/coaching/courses/hosted trips",
     "include",
     "Named individual. Qualifying El Salvador 5-day sample route. Day 1-5 items harvested from opened guide.",
     CHECK_DATE, SELECTOR],
    ["20", "@expertvagabond", "instagram", "Matthew Karsten", "adventure / road-trip travel",
     "131100", "131100",
     "Heepsy influencer snapshot observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/expertvagabond/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Own site (expertvagabond.com) identifies Matthew 'Matt' Karsten",
     "pass",
     "Iceland Ring Road itinerary guide on own site (detailed 7-10 day itinerary; author did 10 days); "
     "day-by-day structure (Days 1-7, Days 8-10) harvested from the guide's table of contents; page metadata "
     "published 2015-02-12, modified 2025-03-28",
     "pass", "0.10% per Heepsy snapshot",
     "pass (guide modified 2025-03-28; own sitemap shows 156 entries dated 2024-2026)",
     "unknown",
     "pass - own work-with-me offers sponsored trips, sponsored posts, photography/content production, speaking, "
     "affiliate marketing (all B2B); targeted searches found no consumer planning/coaching/course/tour offer",
     "include",
     "Named individual (Matthew Karsten). Qualifying Iceland Ring Road guide. Day-by-day items from the guide's "
     "own table of contents.",
     CHECK_DATE, SELECTOR],
    ["20", "@tourdelust", "instagram", "Christine Tran Ferguson", "city travel guides / luxury travel",
     "533400", "533400",
     "qoruz.com/tourdelust/instagram snapshot as of September 2026 observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/tourdelust/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Own about page (tourdelust.com/about/) identifies Christine Tran Ferguson; TikTok @tourdelust bio is 'Christine'",
     "pass",
     "Istanbul 3-day travel guide and itinerary on own site with structured Day 1/2/3; page metadata published "
     "2024-09-18, modified 2025-07-21",
     "pass", "0.18% per Qoruz snapshot",
     "pass (interview published 2025-09-07 updated 2026-07-21 describes her as active travel/lifestyle influencer; "
     "TikTok active; guide modified 2025-07-21)",
     "unknown",
     "pass - own about page says she shares travel guides and itineraries; no service offer listed; targeted "
     "search found no consumer planning/coaching/courses/hosted trips",
     "include",
     "Named individual. Qualifying Istanbul 3-day itinerary. Reach 533.4K IG (Qoruz, Sep 2026). Item-level content "
     "not harvested this session; no items invented.",
     CHECK_DATE, SELECTOR],
    ["20", "@girlgoneabroad", "instagram", "Lauren Carey", "Arctic / northern lights / photography travel",
     "100800", "100800",
     "Feedspot Amsterdam travel-instagram-influencers list observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/girlgoneabroad/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "iHeart/Podchaser podcast bios identify Lauren Carey as creator of the Girl Gone Abroad brand "
     "(@GirlGoneAbroad on Instagram/Facebook/TikTok)",
     "pass",
     "Tromso northern lights guide with tour timeline, lodging, activities, and photography guidance on own site; "
     "guide sitemap date 2025-12-17",
     "pass", "unknown",
     "pass (own sitemap shows posts dated 2026-05-27, 2026-06-28, 2026-08-24)",
     "present (structured tour timeline and lodging recommendations)",
     "pass - targeted searches found no consumer itinerary-planning/coaching/course/hosted-trip offer; described "
     "work is travel photography/property storytelling (B2B)",
     "include",
     "Named individual (Lauren Carey). Qualifying Tromso northern lights guide. Item-level content not harvested "
     "this session; no items invented.",
     CHECK_DATE, SELECTOR],
]

# ------------------------------------------------- itineraries_batch20.json
EXTRACTIONS = [
    {
        "handle": "@jayneytravels",
        "platform": "instagram",
        "notes": "Jayne Gorman: named individual travel creator (creator-owned 2026 media kit, "
                 "jayneytravels.com). Reach: 72K Instagram followers, 8% engagement per own media kit. "
                 "Qualifying guide: structured Linz/Donau long-weekend itinerary the page says is her "
                 "recommended plan from her own trip.",
        "itineraries": [
            {
                "title": "Weekend Guide to Linz & the Donau Region",
                "destination": "Linz & the Donau Region",
                "country": "Austria",
                "days": 3,
                "summary": "A long-weekend itinerary for Linz and the Donau region of Upper Austria that the "
                           "creator says is the itinerary she recommends based on her own trip: fly Ryanair "
                           "into Linz, stay at a Danube-side hotel (Riverresort Donauschlinge or Hotel "
                           "Wesenufer), explore by e-bike, and use the Linz Card.",
                "source_urls": ["https://jayneytravels.com/weekend-guide-to-linz-the-donau-region-upper-austria/"],
                "confidence": "medium",
                "items": [
                    item("flight", "Ryanair flight to Linz", None,
                         "Guide's recommended itinerary flies Ryanair into Linz (per search-indexed guide "
                         "content); day placement not evidenced"),
                    item("hotel", "Riverresort Donauschlinge", None,
                         "Lodging named in the guide's recommended itinerary (per search-indexed guide content)"),
                    item("hotel", "Hotel Wesenufer", None,
                         "Lodging named in the guide's recommended itinerary (per search-indexed guide content)"),
                    item("other", "Linz Card", None,
                         "City card in the guide's recommended itinerary"),
                    item("activity", "E-bike cycling along the Danube", None,
                         "Cycling named as transport/activity in the guide's recommended itinerary"),
                ],
            }
        ],
    },
    {
        "handle": "@happytowander",
        "platform": "instagram",
        "notes": "Christina Guan: named individual (own site; Keepface links instagram.com/happytowander). "
                 "Reach: ~66.1K IG audience per Keepface snapshot. Qualifying guide: 1.5-month Western Europe "
                 "backpacking itinerary titled '2026 Update'. Work-with-me is B2B brand/tourism-board campaigns; "
                 "the Europe planner is a free fillable PDF, not a paid course.",
        "itineraries": [
            {
                "title": "Western Europe Backpacking Itinerary (2026 Update)",
                "destination": "Western Europe",
                "country": "Belgium / Netherlands",
                "days": 45,
                "summary": "A 1.5-month Western Europe backpacking route (guide title carries a '2026 Update') "
                           "built as a sequence of city legs; search-indexed content covers a Brussels leg "
                           "(Days 1-3: Grand Place walking tour, waffles and beer, Brussels Card, Bruges/Antwerp/"
                           "Ghent day trips) and an Amsterdam leg (Days 1-3: Rijksmuseum, Van Gogh Museum, canal "
                           "tour, biking, iAmsterdam card, Giethoorn/Keukenhof day trips), connected by "
                           "Flixbus/Thalys/Omio. Day count is 1.5 months per the guide title.",
                "source_urls": ["https://happytowander.com/western-europe-backpacking-itinerary/"],
                "confidence": "medium",
                "items": [
                    item("activity", "Grand Place walking tour, Brussels", None,
                         "Brussels leg: walking tour of the Grand Place (per search-indexed guide content)"),
                    item("restaurant", "Belgian waffles and beer tasting", None,
                         "Brussels leg: waffles and beer; Cafe Delirium named in guide"),
                    item("other", "Brussels Card", None,
                         "Brussels leg: Brussels Card recommended in guide"),
                    item("activity", "Day trip to Bruges, Antwerp or Ghent", None,
                         "Brussels leg: day-trip options from Brussels"),
                    item("activity", "Rijksmuseum visit, Amsterdam", None,
                         "Amsterdam leg: Rijksmuseum named in guide"),
                    item("activity", "Van Gogh Museum visit, Amsterdam", None,
                         "Amsterdam leg: Van Gogh Museum named in guide"),
                    item("activity", "Amsterdam canal tour", None,
                         "Amsterdam leg: canal tour named in guide"),
                    item("activity", "Biking in Amsterdam", None,
                         "Amsterdam leg: biking named in guide"),
                    item("activity", "Day trip to Giethoorn or Keukenhof", None,
                         "Amsterdam leg: day-trip options from Amsterdam"),
                    item("transport", "Flixbus between Brussels and Amsterdam", None,
                         "Intercity transport named in guide"),
                    item("transport", "Thalys train", None,
                         "Rail option named in guide"),
                    item("other", "iAmsterdam city card", None,
                         "Amsterdam leg: iAmsterdam card recommended in guide"),
                    item("other", "Omio transport booking", None,
                         "Booking platform named in guide"),
                ],
            }
        ],
    },
    {
        "handle": "@michaelturtle",
        "platform": "instagram",
        "notes": "Michael Turtle: named individual (own author pages; Keepface profile explicitly links "
                 "instagram.com/michaelturtle). Reach: 15,534 IG audience, 0.66% engagement per Keepface. "
                 "Qualifying guide: three-day Athens itinerary, page states 'As of July 2026'. Own work-with-me "
                 "is B2B (sponsored trips/posts, photography, speaking, affiliate).",
        "itineraries": [
            {
                "title": "Three Days in Athens Itinerary",
                "destination": "Athens",
                "country": "Greece",
                "days": 3,
                "summary": "A three-day Athens itinerary on the creator's own site; the page states the guide "
                           "is current 'As of July 2026'. Item-level content was not harvested this session, "
                           "so no items are listed rather than invented.",
                "source_urls": ["https://www.timetravelturtle.com/greece/three-days-in-athens-itinerary/"],
                "confidence": "low",
                "items": [],
            }
        ],
    },
    {
        "handle": "@triphackr",
        "platform": "instagram",
        "notes": "Clint Johnston: named individual (own author page triphackr.com/author/clint/; El Salvador "
                 "guide explicitly authored by him). Reach: 150,000+ verified Instagram per own work page. "
                 "Qualifying guide: 'Sample 5-Day Route from Coco Surf' with full Day 1-5 content harvested from "
                 "the opened page. Work-with-me is B2B partnerships only.",
        "itineraries": [
            {
                "title": "Now Is the Time to Discover El Salvador: Sample 5-Day Route from Coco Surf",
                "destination": "El Salvador",
                "country": "El Salvador",
                "days": 5,
                "summary": "A 'Sample 5-Day Route from Coco Surf' through El Salvador, explicitly authored by "
                           "Clint Johnston: Day 1 surf at El Conchalio, stroll and pupusas in El Tunco with "
                           "sunset at Monkey Lala; Day 2 Santa Ana volcano hike and Lake Coatepeque swim; "
                           "Day 3 Jiquilisco Bay boat tour (monkeys, birds) ending with sunset beers in El Zonte; "
                           "Day 4 surf at La Bocana or Punta Roca; Day 5 Tamanique waterfall hike and a villa "
                           "massage.",
                "source_urls": ["https://triphackr.com/now-is-the-time-to-discover-el-salvador/"],
                "confidence": "high",
                "items": [
                    item("hotel", "Coco Surf Tropical Village", 1,
                         "Base for the full route: the guide presents a 'Sample 5-Day Route from Coco Surf'"),
                    item("activity", "Surf at El Conchalio Beach", 1,
                         "Day 1: first surf of the trip at El Conchalio"),
                    item("activity", "Stroll around El Tunco", 1,
                         "Day 1: afternoon stroll around El Tunco"),
                    item("restaurant", "Pupusas in El Tunco", 1,
                         "Day 1 dinner: pupusas"),
                    item("restaurant", "Sunset drinks at Monkey Lala, El Tunco", 1,
                         "Day 1: sunset at Monkey Lala"),
                    item("activity", "Hike the Santa Ana volcano", 2,
                         "Day 2: Santa Ana volcano hike"),
                    item("activity", "Swim in Lake Coatepeque", 2,
                         "Day 2: post-hike swim in Lake Coatepeque"),
                    item("activity", "Boat tour of Jiquilisco Bay", 3,
                         "Day 3: boat tour spotting endemic monkeys and birds"),
                    item("restaurant", "Sunset beers in El Zonte", 3,
                         "Day 3 ends with sunset beers at El Zonte"),
                    item("activity", "Surf La Bocana or Punta Roca", 4,
                         "Day 4: surf La Bocana or Punta Roca"),
                    item("activity", "Hike to the Tamanique waterfall", 5,
                         "Day 5: Tamanique waterfall hike on the final day"),
                    item("activity", "Massage at the villa", 5,
                         "Day 5: villa massage to cap the trip"),
                ],
            }
        ],
    },
    {
        "handle": "@expertvagabond",
        "platform": "instagram",
        "notes": "Matthew 'Matt' Karsten: named individual (expertvagabond.com). Reach: ~131.1K IG, 0.10% per "
                 "Heepsy. Qualifying guide: Iceland Ring Road 7-10 day itinerary (author did 10 days); "
                 "day-by-day structure harvested from the guide's table of contents on his own site. Own "
                 "work-with-me is B2B (sponsored trips/posts, photography, speaking, affiliate); no consumer "
                 "services found.",
        "itineraries": [
            {
                "title": "Iceland Ring Road Trip Itinerary",
                "destination": "Iceland Ring Road",
                "country": "Iceland",
                "days": 10,
                "summary": "A 7-10 day self-drive Ring Road itinerary around Iceland's Route 1 on the "
                           "creator's own site (the author gave himself 10 days): Day 1 Golden Circle; Day 2 "
                           "South Coast; Day 3 iceberg lagoons and ice caves; Day 4 Egilsstaðir and the Eastern "
                           "Fjords; Day 5 Mývatn and waterfalls; Day 6 Akureyri and North Iceland; Day 7 "
                           "Snæfellsnes Peninsula; Days 8-10 Reykjavik.",
                "source_urls": ["https://expertvagabond.com/ring-road-trip-iceland/"],
                "confidence": "medium",
                "items": [
                    item("activity", "Golden Circle drive", 1,
                         "Day 1 of the Ring Road itinerary: the Golden Circle (per guide's day-by-day structure)"),
                    item("activity", "South Coast drive", 2,
                         "Day 2: Iceland's South Coast"),
                    item("activity", "Iceberg lagoons and ice caves", 3,
                         "Day 3: Iceberg Lagoons & Ice Caves"),
                    item("activity", "Egilsstaðir and the Eastern Fjords", 4,
                         "Day 4: Egilsstaðir & The Eastern Fjords"),
                    item("activity", "Lake Mývatn and waterfalls", 5,
                         "Day 5: Mývatn & More Waterfalls"),
                    item("activity", "Akureyri and North Iceland", 6,
                         "Day 6: Akureyri & North Iceland"),
                    item("activity", "Snæfellsnes Peninsula", 7,
                         "Day 7: Snæfellsnes Peninsula"),
                    item("activity", "Explore Reykjavik", 8,
                         "Days 8-10: explore Reykjavik (per guide's day-by-day structure)"),
                ],
            }
        ],
    },
    {
        "handle": "@tourdelust",
        "platform": "instagram",
        "notes": "Christine Tran Ferguson: named individual (own about page; TikTok @tourdelust bio "
                 "'Christine'). Reach: 533.4K IG per Qoruz (Sep 2026). Qualifying guide: Istanbul 3-day "
                 "itinerary (published 2024-09-18, modified 2025-07-21). Exclusion sweep found no consumer "
                 "planning/coaching/courses/hosted trips.",
        "itineraries": [
            {
                "title": "Istanbul Travel Guide: 3-Day Itinerary",
                "destination": "Istanbul",
                "country": "Turkey",
                "days": 3,
                "summary": "A 3-day Istanbul travel guide and itinerary on the creator's own site (published "
                           "2024-09-18, modified 2025-07-21) with a structured Day 1/2/3 plan. Item-level "
                           "content was not harvested this session, so no items are listed rather than invented.",
                "source_urls": ["https://tourdelust.com/istanbul-travel-guide-3-day-itinerary/"],
                "confidence": "low",
                "items": [],
            }
        ],
    },
    {
        "handle": "@girlgoneabroad",
        "platform": "instagram",
        "notes": "Lauren Carey: named individual (podcast bios identify her as creator of the Girl Gone Abroad "
                 "brand). Reach: ~100.8K IG per Feedspot. Qualifying guide: Tromso northern lights guide with "
                 "tour timeline, lodging, activities, photography guidance (sitemap 2025-12-17; site posts "
                 "through 2026-08-24). Exclusion sweep found no consumer travel-planning/coaching/course/"
                 "hosted-trip offer; described work is travel photography/property storytelling (B2B).",
        "itineraries": [
            {
                "title": "Tromso Northern Lights Guide with Photography Tips",
                "destination": "Tromso",
                "country": "Norway",
                "days": None,
                "summary": "A Tromso northern-lights guide on the creator's own site with a tour timeline, "
                           "lodging, activities, and photography guidance (guide sitemap date 2025-12-17). "
                           "Item-level content was not harvested this session, so no items are listed rather "
                           "than invented.",
                "source_urls": ["https://www.girlgoneabroad.com/blog/tromso-northern-lights-guide-with-photography-tips"],
                "confidence": "low",
                "items": [],
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
