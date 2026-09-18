#!/usr/bin/env python3
"""Bring the 6 round-1 top-up extractions (indices 6-11) into full gate1 schema
compliance: add title/summary/source_urls, drop singular source_url,
booking_link 'unknown' -> null. Does NOT touch the 6 pre-existing extractions.
"""
import json

BASE = "/home/hatch/workspace/travel-influencer-pilot"
path = f"{BASE}/staging/itineraries_batch15.json"
data = json.load(open(path, encoding="utf-8"))

META = {
    "@travellinfoodie": {
        "title": "2-Week Turkish Coast Road Trip",
        "summary": "Raymond Cua's structured 14-day road trip along Turkiye's coast: Antalya (3 nights) > Kas (2) > Marmaris (2) > Bodrum (2) > Selcuk/Ephesus (2) > Izmir (2 nights/3 days), with rental car, exact drive durations, attractions, restaurants and six named hotels. Published and modified 2025-03-26.",
        "source_urls": ["https://travellingfoodie.net/turkish-coast-2-week-turkey-itinerary/",
                        "https://travellingfoodie.net/about/"],
    },
    "@pocketwanderings": {
        "title": "Ultimate 3-Day Rome Itinerary",
        "summary": "Jessie Moore's structured 3-day Rome itinerary (published 2025-01-01, modified 2026-04-09): Day 1 ancient Rome (Colosseum, Roman Forum, Palatine Hill, Capitoline Hill, Castel Sant'Angelo); Day 2 Vatican Museums, Sistine Chapel, St Peter's Basilica and Trastevere; Day 3 Trevi Fountain, Pantheon, Piazza Navona, Galleria Borghese and Villa Borghese Gardens, with named restaurants each day.",
        "source_urls": ["https://www.pocketwanderings.com/three-day-rome-itinerary/",
                        "https://pocketwanderings.com/about/"],
    },
    "@araioflight": {
        "title": "Portland to San Francisco Road Trip: Best Stops",
        "summary": "Raihaan's structured Portland-to-San Francisco road trip guide (published and modified 2025-06-17) listing the best stops along the route. Per-stop item extraction was not captured in this pass and is flagged for re-verification.",
        "source_urls": ["https://www.araioflight.com/drive-portland-to-san-francisco-road-trip-best-stops/"],
    },
    "@mrsoaroundtheworld": {
        "title": "5-Day Piedmont Itinerary: Turin & Langhe",
        "summary": "Ana Silva O'Reilly's structured 5-day Piedmont itinerary (published 2026-07-13, modified 2026-07-16): Milan Malpensa > Turin (2 nights) > La Morra/Langhe (2 nights) > Milan, with flights, car hire, Turin walking/sightseeing, La Morra, a Barolo winery lunch and an optional Vicolungo outlet stop.",
        "source_urls": ["https://mrsoaroundtheworld.com/luxury-travel/europe/5-day-piedmont-itinerary-turin-langhe/",
                        "https://mrsoaroundtheworld.com/about/"],
    },
    "@i_am_aileen": {
        "title": "Tokyo Itinerary & DIY Travel Guide",
        "summary": "Aileen Adalid's structured Tokyo itinerary and DIY travel guide (published 2022-10-17, dateModified 2025-06-22) with day/district structure covering Shibuya, Harajuku, Shinjuku, Asakusa, Akihabara, Sumida and more, plus transit, hotel and restaurant guidance.",
        "source_urls": ["https://iamaileen.com/tokyo-itinerary/",
                        "https://iamaileen.com/about/"],
    },
    "@theboutiqueadventurer": {
        "title": "10-Day Scottish Highlands Itinerary",
        "summary": "Amanda O'Brien's detailed 10-day Scottish Highlands itinerary (published and modified 2026-08-09): Glasgow > Glen Coe/Fort William > Isle of Skye > Ullapool > Durness > Thurso > Inverness, with hotels, restaurants, transport and activities along the route.",
        "source_urls": ["https://theboutiqueadventurer.com/ive-spent-years-exploring-scotland-heres-the-10-day-itinerary-i-always-recommend/"],
    },
}

for ex in data["extractions"][6:]:
    h = ex["handle"]
    assert h in META, h
    for it in ex["itineraries"]:
        it["title"] = META[h]["title"]
        it["summary"] = META[h]["summary"]
        it["source_urls"] = META[h]["source_urls"]
        it.pop("source_url", None)
        it.pop("published", None)
        it.pop("modified", None)
        for item in it["items"]:
            if item.get("booking_link") == "unknown":
                item["booking_link"] = None

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("schema repair done for:", sorted(META))
