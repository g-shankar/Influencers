#!/usr/bin/env python3
"""Append 4 confirmed batch-15 top-up creators (round 1).
Evidence for each creator is already on record in staging/worknotes_batch15.md.
Round 1: @travellingfoodie, @pocketwanderings, @araioflight, @mrsoaroundtheworld.
"""
import csv, json, os

BASE = os.path.dirname(os.path.abspath(__file__)) + "/.."

# ---------- batch15.csv (name,handle,platform,niche,followers_approx,profile_url,source_urls)
batch_rows = [
    ["Raymond Cua", "@travellingfoodie", "instagram", "food travel", "10.5K",
     "https://www.instagram.com/travellingfoodie/",
     "https://travellingfoodie.net/about/|https://travellingfoodie.net/turkish-coast-2-week-turkey-itinerary/"],
    ["Jessie Moore", "@pocketwanderings", "instagram", "luxury travel", "133K",
     "https://www.instagram.com/pocketwanderings/",
     "https://pocketwanderings.com/about/|https://www.pocketwanderings.com/three-day-rome-itinerary/"],
    ["Raihaan", "@araioflight", "instagram", "travel", "68.6K",
     "https://www.instagram.com/araioflight/",
     "https://www.araioflight.com/drive-portland-to-san-francisco-road-trip-best-stops/|https://www.araioflight.com/epic-quest-bucket-list/"],
    ["Ana Silva O'Reilly", "@mrsoaroundtheworld", "instagram", "luxury travel", "18.1K",
     "https://www.instagram.com/mrsoaroundtheworld/",
     "https://mrsoaroundtheworld.com/about/|https://mrsoaroundtheworld.com/luxury-travel/europe/5-day-piedmont-itinerary-turin-langhe/"],
]
with open(f"{BASE}/batch15.csv", "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(batch_rows)

# ---------- selection_log_batch15.csv (23 columns)
COLS = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
        "followers_source","profile_url","discovery_source","identity_check","identity_method",
        "content_fit","content_fit_evidence","reach_floor","engagement_observed","activity_check",
        "purchase_intent","exclusions_check","decision","notes","check_date","selector"]

def row(handle, name, niche, fol, fol_src, ident_method, fit_evidence, activity,
        exclusions, notes, engagement="unknown"):
    return {
        "batch": "15", "handle": handle, "platform": "instagram", "name": name,
        "niche": niche, "followers_approx": fol, "followers_observed": fol,
        "followers_source": fol_src,
        "profile_url": f"https://www.instagram.com/{handle.lstrip('@')}/",
        "discovery_source": "feedspot influencer directory" if "feedspot" in fol_src else "influencer directory (keepface)",
        "identity_check": "pass", "identity_method": ident_method,
        "content_fit": "pass", "content_fit_evidence": fit_evidence,
        "reach_floor": "pass", "engagement_observed": engagement,
        "activity_check": activity, "purchase_intent": "unknown",
        "exclusions_check": exclusions, "decision": "include",
        "notes": notes, "check_date": "2026-09-17", "selector": "batch15-topup",
    }

log_rows = [
    row("@travellingfoodie", "Raymond Cua", "food travel", "10.5K",
        "feedspot influencer directory (observed 2026-09-17)",
        "About page states Travelling Foodie was created by Raymond Cua in 2014; contact text uses first-person singular ('contact me'); no staff or team language found.",
        "Own site hosts a structured 2-week Turkish Coast road trip itinerary at https://travellingfoodie.net/turkish-coast-2-week-turkey-itinerary/ published and modified 2025-03-26: Antalya 3 nights > Kas 2 > Marmaris 2 > Bodrum 2 > Selcuk/Ephesus 2 > Izmir 2 nights/3 days, with rental car, exact drive durations, attractions, restaurants and six named hotels.",
        "Site published travel content in 2025-2026; itinerary modified 2025-03-26.",
        "pass",
        "Plural 'Travelling Foodies' on site appears generic, not identifying contributors. No consumer travel-planning services, coaching, or hosted group trips found."),
    row("@pocketwanderings", "Jessie Moore", "luxury travel", "133K",
        "feedspot influencer directory (observed 2026-09-17)",
        "About page titled 'Luxury Travel Blog by Jessie Moore', written entirely in first-person singular ('I started blogging in 2015'). Her consultancy (pocketdigitalgroup.com) sells digital marketing and content creation services to luxury travel and lifestyle brands only - B2B brand work, which is allowed.",
        "Own site hosts a structured 3-day Rome itinerary at https://www.pocketwanderings.com/three-day-rome-itinerary/ published 2025-01-01, modified 2026-04-09: Day 1 Colosseum / Roman Forum / Palatine Hill / Capitoline Hill / Castel Sant'Angelo; Day 2 Vatican Museums / Sistine Chapel / St Peter's Basilica / Trastevere; Day 3 Trevi Fountain / Pantheon / Piazza Navona / Galleria Borghese / Villa Borghese Gardens; named restaurants incl. Ristorante Aroma, Osteria da Fortunata, Da Enzo al 29, Pierluigi, Pipero Roma, Felice a Testaccio, Il Goccetto, Terrazza Les Etoiles.",
        "Itinerary modified 2026-04-09; blog actively publishing in 2025-2026.",
        "pass",
        "Consultancy is B2B for travel/lifestyle brands (allowed); no consumer-facing planning, itinerary services, coaching, or hosted trips found."),
    row("@araioflight", "Raihaan", "travel", "68.6K",
        "Keepface influencer profile for @araioflight (page crawled 2026-01-05): 68.6K Instagram audience, 2.12% engagement rate; profile links https://instagram.com/araioflight",
        "Site author pages identify 'Raihaan (araioflight)'; posts sign off 'Your fellow explorer, Raihaan'; own site links Instagram @araioflight. Consistent one-person pseudonym (first name + handle).",
        "Own site hosts a structured Portland-to-San Francisco road trip itinerary at https://www.araioflight.com/drive-portland-to-san-francisco-road-trip-best-stops/ published and modified 2025-06-17, authored by Raihaan.",
        "Homepage shows travel posts dated 2026-07-30, 2026-06-15 and 2026-06-01; active in 2025-2026.",
        "pass",
        "Reach figure is third-party (Keepface), not creator-stated; Instagram profile itself requires login and was not directly viewed. Site sells custom art commissions (paintings), not travel services. No consumer travel-planning services, coaching, or hosted group trips found.",
        engagement="2.12% (Keepface)"),
    row("@mrsoaroundtheworld", "Ana Silva O'Reilly", "luxury travel", "18.1K",
        "feedspot influencer directory (observed 2026-09-17)",
        "About page at https://mrsoaroundtheworld.com/about/ identifies Ana Silva O'Reilly as the individual behind the site and @mrsoaroundtheworld.",
        "Own site hosts a structured 5-day Piedmont itinerary at https://mrsoaroundtheworld.com/luxury-travel/europe/5-day-piedmont-itinerary-turin-langhe/ published 2026-07-13, modified 2026-07-16: four-night/five-day route Milan Malpensa > Turin (2 nights) > La Morra/Langhe (2 nights) > Milan, with flights, car hire, Turin walking/sightseeing, La Morra, Barolo winery lunch, hotels and an optional Vicolungo outlet stop.",
        "Itinerary published and modified July 2026; active in 2025-2026.",
        "pass",
        "Only B2B brand partnerships observed; no consumer-facing planning, itinerary services, coaching, or hosted group trips found."),
]
with open(f"{BASE}/staging/selection_log_batch15.csv", "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writerows(log_rows)

# ---------- itineraries_batch15.json
def item(item_type, name, location, details, day=None):
    return {"booking_link": "unknown", "day": day, "details": details,
            "item_type": item_type, "location": location, "name": name,
            "price_hint": "unknown"}

extractions = [
    {
        "handle": "@travellingfoodie", "platform": "instagram",
        "itineraries": [{
            "confidence": "high", "country": "Turkiye", "days": 14,
            "destination": "Turkish Coast: Antalya > Kas > Marmaris > Bodrum > Selcuk/Ephesus > Izmir",
            "source_url": "https://travellingfoodie.net/turkish-coast-2-week-turkey-itinerary/",
            "published": "2025-03-26", "modified": "2025-03-26",
            "items": [
                item("flight", "Arrival flight to Antalya", "Antalya (AYT)",
                     "Itinerary starts with arrival in Antalya; departs from Izmir at the end.", day=1),
                item("transport", "Rental car (Cizgi Rent a Car)", "Turkish Coast",
                     "Rental car for the full 2-week coastal road trip; guide gives exact drive durations between each stop.", day=1),
                item("hotel", "Mai Inci Hotel", "Antalya", "Hotel for the 3-night Antalya stay.", day=1),
                item("activity", "Kaleici old town", "Antalya", "Historic old town exploration in Antalya.", day=1),
                item("activity", "Duden Waterfalls", "Antalya", "Waterfall visit near Antalya.", day=2),
                item("hotel", "Dantel Butik ev Pansiyon", "Kas", "Pension for the 2-night Kas stay.", day=4),
                item("activity", "Antiphellos Theater", "Kas", "Ancient theater visit in Kas.", day=4),
                item("hotel", "Myra Hotel", "Marmaris", "Hotel for the 2-night Marmaris stay.", day=6),
                item("activity", "Marmaris Castle", "Marmaris", "Castle visit in Marmaris.", day=6),
                item("hotel", "Agan Pansiyon", "Bodrum", "Pension for the 2-night Bodrum stay.", day=8),
                item("activity", "Castle of St. Peter", "Bodrum", "Crusader castle visit in Bodrum.", day=8),
                item("activity", "Mausoleum at Halicarnassus", "Bodrum", "Ancient wonder site in Bodrum.", day=9),
                item("hotel", "Anz Guesthouse", "Selcuk", "Guesthouse for the 2-night Selcuk/Ephesus stay.", day=10),
                item("activity", "Ephesus ancient city", "Selcuk", "Full ancient city exploration, including the Library of Celsus.", day=10),
                item("hotel", "st945 Palas Otel", "Izmir", "Hotel for the final 2-night Izmir stay.", day=12),
                item("activity", "Kemeraltı Market", "Izmir", "Historic bazaar visit in Izmir.", day=12),
                item("activity", "Konak Square", "Izmir", "Central square and clock tower visit in Izmir.", day=13),
                item("restaurant", "Restaurants en route", "Turkish Coast",
                     "Guide recommends restaurants at each stop; individual names not captured in this extraction.", day=None),
                item("flight", "Departure flight from Izmir", "Izmir (ADB)",
                     "Itinerary ends with departure from Izmir after 2 nights/3 days.", day=14),
            ]}],
        "notes": "Structured 2-week road trip itinerary published/modified 2025-03-26 by Raymond Cua. Route, hotels, car rental and attractions extracted from the guide body.",
    },
    {
        "handle": "@pocketwanderings", "platform": "instagram",
        "itineraries": [{
            "confidence": "high", "country": "Italy", "days": 3,
            "destination": "Rome, Italy",
            "source_url": "https://www.pocketwanderings.com/three-day-rome-itinerary/",
            "published": "2025-01-01", "modified": "2026-04-09",
            "items": [
                item("activity", "Colosseum", "Rome", "Morning visit, recommended early to avoid crowds.", day=1),
                item("activity", "Roman Forum", "Rome", "Ancient government buildings visited after the Colosseum.", day=1),
                item("activity", "Palatine Hill", "Rome", "Panoramic views over Rome's archaeological ruins.", day=1),
                item("restaurant", "Ristorante Aroma", "Rome", "Michelin-star Mediterranean restaurant lunch across from Palatine Hill.", day=1),
                item("activity", "Capitoline Hill", "Rome", "Temples and museums wander after lunch.", day=1),
                item("transport", "Taxi to Castel Sant'Angelo", "Rome", "Taxi recommended to Castel Sant'Angelo.", day=1),
                item("activity", "Castel Sant'Angelo", "Rome", "Hallways, artworks, artefacts and viewing platforms; museum cafe for aperitifs.", day=1),
                item("restaurant", "Osteria da Fortunata", "Rome", "Dinner; noted for homemade pasta.", day=1),
                item("other", "La Botticella pub", "Rome", "Evening drinks at a treasured Roman pub.", day=1),
                item("activity", "Vatican Museums", "Rome", "Morning visit to the papal collections.", day=2),
                item("activity", "Sistine Chapel", "Rome", "Michelangelo's ceiling frescoes; Gregorian Egyptian Museum if time permits.", day=2),
                item("activity", "St Peter's Basilica", "Rome", "Reached via the secret passageway from the Sistine Chapel with a skip-the-line tour.", day=2),
                item("transport", "Bus line 116 to Trastevere", "Rome", "Bus ride to Trastevere for lunch away from crowds.", day=2),
                item("restaurant", "Da Enzo al 29", "Trastevere, Rome", "Authentic Italian lunch in a quiet alley near the Tiber.", day=2),
                item("activity", "Trastevere neighbourhood", "Rome", "Afternoon wander through the charming neighbourhood; gelato.", day=2),
                item("activity", "Santa Maria in Trastevere", "Rome", "Basilica visit, noted for ceilings and columns.", day=2),
                item("activity", "Villa Farnesina", "Rome", "Art museum, former elite banquet villa.", day=2),
                item("restaurant", "Pierluigi", "Rome", "Elegant dinner across Ponte Giuseppe Mazzini; modern take on traditional food.", day=2),
                item("restaurant", "Il Goccetto", "Rome", "Tapas and drinks before returning to the hotel.", day=2),
                item("activity", "Trevi Fountain", "Rome", "Morning visit on the final day.", day=3),
                item("activity", "Pantheon", "Rome", "Architectural wonder reached via Via del Seminario.", day=3),
                item("activity", "Piazza Navona", "Rome", "Lively square with cafes, terraces and excavation sites.", day=3),
                item("restaurant", "Pipero Roma", "Rome", "Michelin restaurant lunch; noted mussel soup.", day=3),
                item("activity", "Galleria Borghese", "Rome", "Antiques, paintings and sculptures in the palace.", day=3),
                item("activity", "Villa Borghese Gardens", "Rome", "Relaxing afternoon in the 80-hectare gardens; bike or golf cart rental suggested.", day=3),
                item("transport", "Bike/golf cart rental", "Villa Borghese, Rome", "Suggested to cover the extensive gardens.", day=3),
                item("restaurant", "Felice a Testaccio", "Rome", "Final dinner; go-to order is Cacio e Pepe.", day=3),
                item("other", "Terrazza Les Etoiles rooftop bar", "Rome", "Drinks and dessert with sweeping city views to end the trip.", day=3),
            ]}],
        "notes": "Structured 3-day Rome itinerary published 2025-01-01, modified 2026-04-09 by Jessie Moore. Day-by-day activities, restaurants and transport extracted from the guide body.",
    },
    {
        "handle": "@araioflight", "platform": "instagram",
        "itineraries": [{
            "confidence": "medium", "country": "USA", "days": None,
            "destination": "Portland to San Francisco road trip",
            "source_url": "https://www.araioflight.com/drive-portland-to-san-francisco-road-trip-best-stops/",
            "published": "2025-06-17", "modified": "2025-06-17",
            "items": [],
        }],
        "notes": "Structured Portland-to-San Francisco road trip guide published/modified 2025-06-17 by Raihaan (@araioflight). Itinerary-level metadata recorded; per-stop item extraction was not captured in this pass and should be completed on re-verification before the pilot consumes it.",
    },
    {
        "handle": "@mrsoaroundtheworld", "platform": "instagram",
        "itineraries": [{
            "confidence": "high", "country": "Italy", "days": 5,
            "destination": "Piedmont: Milan > Turin > La Morra/Langhe > Milan",
            "source_url": "https://mrsoaroundtheworld.com/luxury-travel/europe/5-day-piedmont-itinerary-turin-langhe/",
            "published": "2026-07-13", "modified": "2026-07-16",
            "items": [
                item("flight", "Flights via Milan Malpensa", "Milan Malpensa (MXP)",
                     "Round-trip routing through Milan Malpensa for the 5-day Piedmont itinerary.", day=1),
                item("transport", "Car hire", "Piedmont",
                     "Car hire for the Turin > Langhe driving route.", day=1),
                item("hotel", "Turin hotel", "Turin",
                     "Hotel for the 2-night Turin stay; specific property name not captured in this extraction.", day=1),
                item("activity", "Turin walking and sightseeing", "Turin",
                     "Walking/sightseeing in Turin across the 2-night stay.", day=2),
                item("hotel", "La Morra / Langhe hotel", "La Morra",
                     "Hotel for the 2-night La Morra/Langhe stay; specific property name not captured in this extraction.", day=3),
                item("activity", "La Morra village visit", "La Morra",
                     "Village exploration in the Langhe wine region.", day=3),
                item("restaurant", "Barolo winery lunch", "Barolo",
                     "Winery lunch in Barolo.", day=4),
                item("other", "Vicolungo outlet stop (optional)", "Vicolungo",
                     "Optional outlet shopping stop on the return toward Milan.", day=5),
                item("flight", "Return via Milan Malpensa", "Milan Malpensa (MXP)",
                     "Itinerary closes back in Milan for departure.", day=5),
            ]}],
        "notes": "Structured 5-day Piedmont itinerary published 2026-07-13, modified 2026-07-16 by Ana Silva O'Reilly. Route, transport and activity structure extracted; specific hotel property names were not captured in this pass.",
    },
]

path = f"{BASE}/staging/itineraries_batch15.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)
data["extractions"].extend(extractions)
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("appended:", len(batch_rows), "creators")
