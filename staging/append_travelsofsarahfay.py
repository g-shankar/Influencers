#!/usr/bin/env python3
"""Stage 2 closer: append @travelsofsarahfay (Sarah Fay) to Batch 20.

Evidence gathered 2026-09-17 (non-login sources only). Appends only. Writes:
  - batch20.csv (7 cols)
  - staging/selection_log_batch20.csv (23 cols)
  - staging/itineraries_batch20.json (extraction object)
  - staging/dedup_universe_2026-09-17.txt (new handle)

Engagement: unknown (nonblocking) per the 2026-09-17 Batch 20 final-decision
precedent (third-party engagement tools not publicly accessible 2026-09-17).
Reach is self-reported on the creator's own Clubhouse creator profile - the
same class of evidence as creator-owned media-kit counts used elsewhere in
Batch 20; recorded with the caveat.
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
    ["Sarah Fay", "@travelsofsarahfay", "instagram", "adventure / solo female travel",
     "11165", "https://www.instagram.com/travelsofsarahfay/",
     "https://travelsofsarahfay.com/3-days-in-barbados/"],
]

# ------------------------------------------------------- selection log (23 col)
LOG_ROWS = [
    ["20", "@travelsofsarahfay", "instagram", "Sarah Fay", "adventure / solo female travel",
     "11165", "11,165",
     "Creator's own Clubhouse creator profile observed 2026-09-17 (self-reported: 'Instagram IG "
     "@travelsofsarahfay 11,165'; profile links travelsofsarahfay.com)",
     "https://www.instagram.com/travelsofsarahfay/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Muck Rack journalist profile 'Sarah Fay's Profile | Travels of Sarah Fay'; her first-person Clubhouse "
     "creator profile links travelsofsarahfay.com, describes her as a travel writer/adventure travel blogger "
     "and states the exact handle @travelsofsarahfay",
     "pass",
     "'3 Days in Barbados: A Travel Guide To Short Stays' on own site, bylined January 5, 2026 (homepage "
     "byline; image paths dated 2026/01): The Crane Resort base (affiliate booking.stay22.com link; 1887 "
     "historic resort above Crane Beach), Island 360 Tour with Sweet Life Tours Barbados (5-6 hour island "
     "drive; Speightstown lunch stop; The Orange Street Grocer; Suga Mama ice cream), Oistins Fish Fry "
     "(Friday nights), Rihanna's childhood home in Bridgetown, Crane Beach walks, Azure Restaurant and Zen "
     "Restaurant at The Crane, Cutters of Barbados (cutter sandwich, Rum Punch), Cherry Tree Hill, Bathsheba, "
     "Carlisle Bay, Bridgetown walks, Grantley Adams International Airport arrival; page carries an affiliate "
     "disclosure. Item detail harvested from the opened page. Day numbers are not assigned in the guide, so "
     "items carry null days rather than invented ones.",
     "pass",
     "unknown (nonblocking) - third-party engagement tools not publicly accessible 2026-09-17; per the "
     "2026-09-17 Batch 20 final-decision precedent engagement is nonblocking for all includes",
     "pass (Barbados guide bylined 2026-01-05; homepage crawled 2026-09-16 lists it under Recent Adventures)",
     "present (affiliate disclosure on the guide page; booking.stay22.com affiliate link for The Crane Resort; "
     "named resort, restaurants, and a paid island tour)",
     "pass - targeted 2026-09-17 searches found no consumer itinerary planning/coaching/courses/workshops/"
     "hosted group trips/agency offer tied to Sarah Fay; her Expedia Travel Shop is affiliate curation, not a "
     "service; Yosemite guide's sponsored-trip credit is a press partnership",
     "include",
     "Named individual (Sarah Fay). Qualifying Barbados 3-day guide bylined 2026-01-05 (in window). Reach "
     "11,165 IG self-reported on her own Clubhouse creator profile. Item-level content harvested from the "
     "opened guide page; no day numbers invented.",
     CHECK_DATE, SELECTOR],
]

# ------------------------------------------------- itineraries_batch20.json
EXTRACTIONS = [
    {
        "handle": "@travelsofsarahfay",
        "platform": "instagram",
        "notes": "Sarah Fay: named individual travel writer/adventure travel blogger (Muck Rack journalist "
                 "profile; first-person Clubhouse creator profile). Reach: 11,165 Instagram, self-reported on "
                 "her own Clubhouse creator profile (observed 2026-09-17). Qualifying guide: '3 Days in "
                 "Barbados: A Travel Guide To Short Stays' on her own site (bylined January 5, 2026), with an "
                 "affiliate disclosure, affiliate resort link, and named paid tour and restaurants. Exclusion "
                 "sweep 2026-09-17 found no consumer services. Items harvested from the opened guide page; the "
                 "guide does not assign day numbers, so days are null rather than invented.",
        "itineraries": [
            {
                "title": "3 Days in Barbados: A Travel Guide To Short Stays",
                "destination": "Barbados",
                "country": "Barbados",
                "days": 3,
                "summary": "A 3-day Barbados short-stay guide on the creator's own site (bylined January 5, "
                           "2026): base at The Crane Resort (historic 1887 resort above Crane Beach; affiliate "
                           "booking link), an Island 360 Tour with Sweet Life Tours Barbados (5-6 hour island "
                           "drive with a Speightstown lunch stop, The Orange Street Grocer, Suga Mama ice "
                           "cream), Oistins Fish Fry on Friday night, Rihanna's childhood home in Bridgetown, "
                           "Crane Beach walks, dining at Azure and Zen restaurants at The Crane and Cutters of "
                           "Barbados (cutter sandwich, Rum Punch), plus Cherry Tree Hill, Bathsheba, Carlisle "
                           "Bay and Bridgetown walks.",
                "source_urls": ["https://travelsofsarahfay.com/3-days-in-barbados/"],
                "confidence": "medium",
                "items": [
                    item("transport", "Arrival via Grantley Adams International Airport", 1,
                         "Grantley Adams International Airport - described as efficient and easy to navigate, "
                         "with direct flights from North America and Europe"),
                    item("hotel", "The Crane Resort, Barbados", 1,
                         "Base for the stay: historic resort dating to 1887 perched above Crane Beach, with "
                         "multiple pools, gardens, and a private plunge pool in the author's suite; booked via "
                         "an affiliate link on the guide page"),
                    item("activity", "Island 360 Tour with Sweet Life Tours Barbados", None,
                         "5-6 hour guided island drive (A/C van) covering towns, beaches, churches and historic "
                         "landmarks, with rum provided along the way; 45-minute lunch stop in Speightstown"),
                    item("restaurant", "The Orange Street Grocer, Speightstown", None,
                         "Waterfront cafe stop during the island tour - lattes and snacks"),
                    item("restaurant", "Suga Mama ice cream", None,
                         "Ice cream stop named in the guide (@sugamamabarbados); a nearby bakery where locals "
                         "buy bread and sweets also mentioned"),
                    item("activity", "Oistins Fish Fry on Friday night", None,
                         "Friday-night fish fry (5-7pm prime time) - the guide was not in town on a Friday but "
                         "names it as the place to go"),
                    item("activity", "Rihanna's childhood home, Bridgetown", None,
                         "The humble pastel-colored childhood home near Rihanna Drive - a pilgrimage stop for fans"),
                    item("activity", "Walking Crane Beach", None,
                         "Beach walks beneath the coral cliffs of the Crane Resort - soft cream and pale-pink "
                         "sand, Atlantic surf; reached by elevator or a winding path"),
                    item("restaurant", "Azure Restaurant at The Crane", None,
                         "Breakfast each morning at Azure, overlooking the beach below"),
                    item("restaurant", "Zen Restaurant at The Crane", None,
                         "Japanese and Thai dishes; the author's final (phenomenal) meal - reserve ahead, "
                         "generally closes 9pm and very popular"),
                    item("restaurant", "Cutters of Barbados", None,
                         "Walk from the resort gates for the iconic cutter (Bajan flying-fish sandwich on salt "
                         "bread) and Rum Punch; indoor and outdoor seating"),
                    item("activity", "Cherry Tree Hill viewpoint", None,
                         "Sweeping views of the island's lush interior meeting the distant Atlantic, reached "
                         "through rolling hills and sugarcane fields"),
                    item("activity", "Bathsheba beach", None,
                         "Dramatic surf coastline on the east coast"),
                    item("activity", "Carlisle Bay swimming and snorkeling", None,
                         "Calm, crystal-clear waters near Bridgetown, ideal for swimming and snorkeling"),
                    item("activity", "Bridgetown walking", None,
                         "Walking the capital's streets for colonial history and present-day vibrancy"),
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
