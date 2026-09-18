#!/usr/bin/env python3
"""Append @sinahsstories and @gracefkim extractions to itineraries_batch20.json.
All items harvested from pages opened and read by this worker 2026-09-17.
Nothing invented: booking_link null everywhere (full affiliate URLs not captured)."""
import json
from pathlib import Path

ROOT = Path.home() / "workspace" / "travel-influencer-pilot"
P = ROOT / "staging" / "itineraries_batch20.json"

SINAH_URL = "https://sinahsstories.com/2025/05/30/ultimate-puglia-7-day-itinerary/"
GRACE_URL = "https://gracefkim.com/10-day-guatemala-itinerary/"

def it(t, n, d, desc, day=None):
    return {"item_type": t, "name": n, "day": day, "description": desc,
            "booking_link": None, "price_hint": None}

sinah_items = [
    it("flight", "Fly into Bari (BRI) or Brindisi (BDS) airport", None,
       "Guide recommends flying into Bari Airport or Brindisi Airport, then grabbing a rental car", None),
    it("transport", "Rental car (Sicily by Car)", None,
       "Guide states a rental car is needed - public transport is limited; they booked with Sicily by Car (link on page)", None),
    it("hotel", "La Cas\u00e8dde", None,
       "Charming guesthouse in Cisternino with breakfast and pool; one of two bases the creator stayed at and recommends (booking.com link on page)", None),
    it("hotel", "Sopra I Sassi", None,
       "Trulli house complex near Ostuni; second base the creator stayed at and recommends (booking.com link on page)", None),
    it("activity", "Alberobello trulli village", 1,
       "Wander 2-3 hours: Via Monte S. Michele to Largo Martellotta, Church of Saint Lucia viewpoint, Villa Comunale Belvedere Parco, Rione Aia Piccola (400 authentic trulli), Trullo Siamese; go early/late to avoid tour buses", 1),
    it("activity", "Locorotondo old town", 1,
       "Afternoon: Church of Saint George Martyr (18th c., free entry), cream-colored old-town streets with artisan shops, Belvedere di Locorotondo terrace over Valle d'Itria", 1),
    it("activity", "Porto Antico, Monopoli", 2,
       "Historic fishing harbor - watch boats unload the fresh catch; seafood lunch nearby", 2),
    it("activity", "Monopoli old town walk", 2,
       "Via Porto promenade with sea views, Church of Saint Vitus Martyr (18th c. Baroque), Palazzo Palmieri facade, Cattedrale Maria Santissima della Madia, Cala Porta Vecchia rocky beach (check access)", 2),
    it("activity", "Basilica San Nicola, Bari", 3,
       "11th-century basilica housing the relics of Saint Nicholas; \u20ac3 crypt tour", 3),
    it("activity", "Bari old town and seafront", 3,
       "Piazza Mercantile (coffee), 5km Lungomare Imperatore Augusto promenade, Basilica Cattedrale San Sabino (Byzantine mosaics), Arco Basso 'Pasta Street' - watch nonnas hand-roll orecchiette, fresh pasta ~\u20ac5/kilo", 3),
    it("activity", "Lama Monachile, Polignano a Mare", 4,
       "Iconic small cove between cliffs with turquoise water; best enjoyed from the belvedere above", 4),
    it("activity", "Polignano a Mare old town", 4,
       "Belvedere su Lama Monachile terrace, Piazza Vittorio Emanuele II cafes, Pendma Chiatt (Pietra Piatta) rocky stairs near the Domenico Modugno statue for sea views/sunset", 4),
    it("activity", "Cisternino old town", 5,
       "Morning: hill village at 394m known for fornelli rustici open-grill butchers; narrow alleys, cream-colored buildings, linen shops; ~1.5 hours", 5),
    it("activity", "Ostuni, the White City", 5,
       "Afternoon/evening for sunset light: Duomo di Santa Maria Assunta (Gothic), Via F. Incalzi Antonelli ('Heaven's Door' / blue-door house photo spot), Piazza della Libert\u00e0 for gelato", 5),
    it("restaurant", "Borgo Antico Bistro, Ostuni", 5,
       "Eatery in the old quarter that doubles as a famous viewpoint/photo spot; consider reserving", 5),
    it("activity", "Lecce Baroque center", 6,
       "'Florence of the South', ~5 hours: Basilica Santa Croce (1549-1695 facade), Piazza Sant'Oronzo over Roman amphitheater ruins, San Matteo (1667), Santa Chiara di Lecce (1687), Cattedrale di Lecce (bell tower views, entry fee), Porta Napoli; pasticciotto pastries nearby", 6),
    it("activity", "Spiaggia di Torre Pozzelle", 7,
       "Flexible last day: natural beach on the Ionian coast near Ostuni/Cisternino - peaceful, dunes, clear water; or pool day / revisit a favorite town", 7),
]

grace_items = [
    it("flight", "Direct flight to La Aurora International Airport (GUA)", 1,
       "Creator flew direct JFK (NYC) to Guatemala City, ~5 hour flight; GUA is the main entry point", 1),
    it("transport", "Uber from GUA airport to hotel", 1,
       "Late-night arrival: Uber straightforward, cost 44 GTQ ($5.75 USD)", 1),
    it("hotel", "Good Hotel Guatemala City", 1,
       "Zone 4, 10-minute Uber from the airport; creator spent first night here (booking.tp.st affiliate link on page)", 1),
    it("transport", "Tourist shuttle Guatemala City to Antigua", 1,
       "Suggested pre-booked shuttle option if starting the trip in Antigua instead of Lake Atitlan (viator.tp.st link on page)", 1),
    it("transport", "Uber Guatemala City to Lake Atitlan", 2,
       "3.5-hour journey after the hotel night; UberX ~650 GTQ ($85); after two cancellations driver Chris accepted - private driver contact via Whatsapp +502 3921 8677 for Atitlan/Semuc Champey/Flores runs", 2),
    it("transport", "Shared tourist shuttle Antigua-Panajachel (Lake Atitlan)", None,
       "Booked the night before; $20 USD per person (153 GTQ); door-to-door hotel/hostel pickups (viator.tp.st link on page)", None),
    it("activity", "Acatenango volcano hike", None,
       "Guided hike referenced in the guide with tour-guide photos (viator.tp.st link on page); creator notes rainy-season hikes are much harder", None),
    it("other", "SafetyWing Nomad Insurance", None,
       "Travel medical insurance the creator says she has depended on numerous times - covers medical, evacuation, theft, trip cancellation (safetywing.com link on page)", None),
    it("other", "Rexby Guatemala route map and guide", None,
       "Creator's exact 10-day route map on Rexby - downloadable, customizable day-by-day; 30% discount noted until 5/31 (www.rexby.com link on page)", None),
]

EXTRACTIONS = [
    {
        "handle": "@sinahsstories",
        "platform": "instagram",
        "notes": "Sinah: named individual (mononym, section 6.1 precedent - consistent public operator identity on own site and handle). Reach: 121K IG (Feedspot, obs 2026-09-17); creator's own TikTok bio states IG +115k (obs 2026-09-17). Engagement: 488,300 TikTok likes / 348 videos (obs 2026-09-17), cross-platform per founder ruling section 5. Activity: account-level per section 6.2 (bio promotes IG; guide modified 2026-01-24). Purchase intent: booking.com affiliate links on guide. Exclusions: work-with-me is B2B brand-campaign content only. Qualifying guide: 7-day Puglia itinerary, creator metadata datePublished 2025-05-30 (in-window). All 17 items harvested from the opened guide page; no items invented.",
        "itineraries": [
            {
                "title": "Ultimate Puglia 7-Day Itinerary",
                "destination": "Puglia",
                "country": "Italy",
                "days": 7,
                "summary": "Seven-day Puglia road trip from Bari to Lecce built around a central base (Locorotondo/Cisternino/Ostuni): trulli villages, fishing ports, Baroque Lecce and a flexible beach day, with driving times and crowd-avoidance timing (April-May or September-October).",
                "source_urls": [SINAH_URL],
                "confidence": "high",
                "items": sinah_items,
            }
        ],
    },
    {
        "handle": "@gracefkim",
        "platform": "instagram",
        "notes": "Grace Kim: named individual (own-site byline). Reach: 109,132 IG followers (Gondola, obs 2026-09-17). Engagement: 4,161,509 likes / 21,444,469 views (Gondola, obs 2026-09-17). Activity: account-level per section 6.2 (Gondola current IG engagement; 1,121 posts). Purchase intent: affiliate disclosure + viator/booking/SafetyWing/Rexby links. Exclusions: Rexby/Steller are fixed digital products (allowed); no consumer planning/coaching/hosted-trip offer found. Qualifying guide: 10-day Guatemala itinerary dated April 28, 2025 (in-window). Items harvested from the observed portion of the guide (intro through Day 2); page content beyond Day 2 was not opened this session. No items invented; day numbers only where the guide assigns them.",
        "itineraries": [
            {
                "title": "10-day Guatemala itinerary",
                "destination": "Guatemala",
                "country": "Guatemala",
                "days": 10,
                "summary": "Ten-day Guatemala route the creator calls the best use of limited time: Guatemala City arrival, Lake Atitlan, Antigua and Tikal highlights, with transport logistics (shuttles, Uber, chicken buses), budget tiers, safety guidance and a customizable Rexby route map.",
                "source_urls": [GRACE_URL],
                "confidence": "high",
                "items": grace_items,
            }
        ],
    },
]

def main():
    data = json.loads(P.read_text(encoding="utf-8"))
    assert data["batch"] == 20
    have = {e["handle"] for e in data["extractions"]}
    added = 0
    for ex in EXTRACTIONS:
        if ex["handle"] in have:
            print(f"SKIP (already present): {ex['handle']}")
            continue
        # validate item types / fields like gate1
        for itn in ex["itineraries"]:
            assert itn["confidence"] in {"high", "medium", "low"}
            assert itn["source_urls"] and all(u.startswith("http") for u in itn["source_urls"])
            for it in itn["items"]:
                assert it["item_type"] in {"flight", "hotel", "activity", "restaurant", "transport", "other"}, it["item_type"]
                assert it["name"] and it["name"].strip()
                assert it["day"] is None or (isinstance(it["day"], int) and it["day"] > 0)
                assert it["booking_link"] is None
        data["extractions"].append(ex)
        added += 1
    P.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"appended {added} extractions; total now {len(data['extractions'])}")

if __name__ == "__main__":
    main()
