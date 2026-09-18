#!/usr/bin/env python3
"""Stage 2 closer: append @thatbackpacker (Audrey Bergner) to Batch 20.

Evidence gathered 2026-09-17 (non-login sources only). Appends only. Writes:
  - batch20.csv (7 cols)
  - staging/selection_log_batch20.csv (23 cols)
  - staging/itineraries_batch20.json (extraction object)
  - staging/dedup_universe_2026-09-17.txt (new handle)

Identity adjudication (documented in selection-log notes): the Instagram bio
reads "Samuel & Audrey / Travel Family", but the creator-owned site's about
page names Audrey Bergner as founder/writer, the contact page states ALL site
content is written by her, and Travel Massive's verified profile identifies
Audrey Bergner as THE That Backpacker travel blogger/video host. The extracted
itinerary is her authored work. Recorded as a pass with the duo label disclosed.

Engagement: third-party engagement tools (Social Blade, HypeAuditor) were not
publicly accessible on 2026-09-17; recorded as unknown (nonblocking) per the
2026-09-17 Batch 20 final-decision precedent, which applies the same treatment
to all existing includes. One creator-reported datapoint is cited honestly.
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
    ["Audrey Bergner", "@thatbackpacker", "instagram", "backpacking / budget travel",
     "50400", "https://www.instagram.com/thatbackpacker/",
     "https://thatbackpacker.com/one-month-india-travel-itinerary/; https://thatbackpacker.com/about/"],
]

# ------------------------------------------------------- selection log (23 col)
LOG_ROWS = [
    ["20", "@thatbackpacker", "instagram", "Audrey Bergner", "backpacking / budget travel",
     "50400", "50.4K",
     "Feedspot solo-female travel Instagram influencers list observed 2026-09-17 (verbatim URL not retained)",
     "https://www.instagram.com/thatbackpacker/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Creator-owned about page (thatbackpacker.com/about) names Audrey Bergner as founder/writer; contact page "
     "states all site content is written by her; Travel Massive verified profile identifies Audrey Bergner as "
     "the That Backpacker travel blogger/video host; exact Instagram handle @thatbackpacker confirmed via "
     "search. Note: IG bio reads 'Samuel & Audrey / Travel Family' (shared family positioning) - adjudicated "
     "pass because the named individual authors all content (see notes).",
     "pass",
     "30-day India travel itinerary on own site with a full day-by-day plan: Days 1-4 Delhi (Red Fort, Jama "
     "Masjid, Humayun's Tomb, Lodhi Gardens; Tara Palace), Days 5-7 Jaisalmer (fort, Jain temples, Thar Desert "
     "camel trek, Bada Bagh; Tokyo Palace Hotel), Days 8-10 Jodhpur (Mehrangarh Fort, Sardar Market/Clock Tower; "
     "Jewel Palace Haweli), Days 11-13 Jaipur (Amber/Nahargarh/Jaigarh Forts, City Palace, Jantar Mantar, Hawa "
     "Mahal; Jai Niwas Garden Hotel), 4-day Agra leg (Agra Fort, Taj Mahal, Baby Taj, Mehtab Bagh; Coral Court "
     "Homestay), 4-day Varanasi leg (Ganges ghats, boat ride), Kolkata final leg; page carries affiliate "
     "disclosure; search index showed page updated ~69 days before 2026-09-17 (July 2026)",
     "pass",
     "unknown (nonblocking) - third-party engagement tools (Social Blade, HypeAuditor) not publicly accessible "
     "2026-09-17; per the 2026-09-17 Batch 20 final-decision precedent engagement is nonblocking for all "
     "includes; one creator-reported datapoint: her first-person tededer.com interview cites one Instagram "
     "video at 3,700 views with 86 saves, 28 shares, 39 comments",
     "pass (5 guides - India, Peru, Easter Island, South Africa, Hamburg - indexed as updated 68-73 days before "
     "2026-09-17; India guide carries 100+ comments; IG bio lists a current Argentina hotel-renovation project)",
     "present (itinerary page carries an affiliate disclosure; named hotels link to HotelsCombined and other "
     "booking partners, e.g. Tara Palace, Tokyo Palace Hotel, Jewel Palace Haweli, Jai Niwas Garden Hotel, "
     "Coral Court Homestay)",
     "pass - targeted 2026-09-17 searches (own 'how to start a travel blog' tutorial, Worldpackers/partner "
     "mentions, hosted-press-trip writeups) show only B2B brand partnerships/hosted stays for content and "
     "content licensing; no consumer itinerary planning/coaching/courses/workshops/hosted group trips/agency "
     "offer found",
     "include",
     "Named individual (Audrey Bergner) behind creator-owned thatbackpacker.com; qualifying 30-day India "
     "itinerary updated July 2026. Duo-label adjudication: IG bio 'Samuel & Audrey / Travel Family' is family "
     "positioning; all content is written by Audrey Bergner per her contact page and verified third-party "
     "profile - identity gate satisfied via the named author. Reach 50.4K IG (Feedspot).",
     CHECK_DATE, SELECTOR],
]

# ------------------------------------------------- itineraries_batch20.json
EXTRACTIONS = [
    {
        "handle": "@thatbackpacker",
        "platform": "instagram",
        "notes": "Audrey Bergner: named individual founder/writer of thatbackpacker.com (contact page states "
                 "all site content is written by her; Travel Massive verified profile). Reach: 50.4K Instagram "
                 "per Feedspot (observed 2026-09-17). Qualifying guide: 30-day India itinerary, page updated "
                 "July 2026 (~69 days before 2026-09-17 per search index), with a full day-by-day plan and "
                 "affiliate booking links for named hotels. Exclusion sweep 2026-09-17 found no consumer "
                 "planning/coaching/courses/hosted trips. Day-by-day items harvested from the opened guide "
                 "page and its indexed day-by-day table.",
        "itineraries": [
            {
                "title": "One Month in India Travel Itinerary - Detailed Day-By-Day Plan",
                "destination": "India",
                "country": "India",
                "days": 30,
                "summary": "A 30-day day-by-day India route on the creator's own site: Days 1-4 Delhi (Red "
                           "Fort, Jama Masjid, Chandni Chowk, Humayun's Tomb, Lodhi Gardens; Tara Palace), "
                           "Days 5-7 Jaisalmer (fort, Jain temples, Thar Desert camel trek, Bada Bagh; Tokyo "
                           "Palace Hotel), Days 8-10 Jodhpur (Mehrangarh Fort, Sardar Market/Clock Tower; "
                           "Jewel Palace Haweli), Days 11-13 Jaipur (Amber/Nahargarh/Jaigarh Forts, City "
                           "Palace, Jantar Mantar, Hawa Mahal; Jai Niwas Garden Hotel), a 4-day Agra leg "
                           "(Agra Fort, Taj Mahal, Baby Taj, Mehtab Bagh; Coral Court Homestay), a 4-day "
                           "Varanasi leg (Ganges ghats, boat ride), and a final Kolkata leg. The page carries "
                           "an affiliate disclosure and hotel booking links.",
                "source_urls": ["https://thatbackpacker.com/one-month-india-travel-itinerary/"],
                "confidence": "high",
                "items": [
                    item("activity", "Old Delhi walking tour: Red Fort, Jama Masjid, Chandni Chowk", 1,
                         "Day 1: explore Old Delhi on foot - Red Fort, Jama Masjid, Chandni Chowk "
                         "(per guide's day-by-day table)"),
                    item("activity", "New Delhi: Humayun's Tomb and Lodhi Gardens", 2,
                         "Day 2: New Delhi - Humayun's Tomb, Lodhi Gardens (per guide's day-by-day table); "
                         "the guide also names India Gate and Qutub Minar for the Delhi leg"),
                    item("hotel", "Tara Palace, Delhi", 1,
                         "Delhi base named in the guide (affiliate booking links on the page); "
                         "the guide budgets three Delhi nights"),
                    item("transport", "Overnight train from Delhi to Jaisalmer", 4,
                         "Day 4: overnight train from Delhi to Jaisalmer (per guide's day-by-day table)"),
                    item("activity", "Jaisalmer Fort, Raj Mahal and Jain Temples", 5,
                         "Day 5: explore Jaisalmer's fort complex, Raj Mahal and the Jain Temples"),
                    item("activity", "Sunset camel trek in the Thar Desert", 6,
                         "Day 6: sunset camel trek into the Thar Desert (per guide's day-by-day table)"),
                    item("activity", "Bada Bagh cenotaphs", 7,
                         "Day 7: Bada Bagh; evening bus onward to Jodhpur (per guide's day-by-day table)"),
                    item("hotel", "Tokyo Palace Hotel, Jaisalmer", 5,
                         "Jaisalmer lodging named in the guide (affiliate booking links on the page)"),
                    item("activity", "Mehrangarh Fort", 8,
                         "Day 8: Mehrangarh Fort; lunch at Cafe Mehran (per guide's day-by-day table)"),
                    item("activity", "Sardar Market and Clock Tower", 9,
                         "Day 9: Sardar Market and the Clock Tower; dinner at Jhankar restaurant"),
                    item("hotel", "Jewel Palace Haweli, Jodhpur", 8,
                         "Jodhpur lodging named in the guide (affiliate booking links on the page)"),
                    item("activity", "Amber, Nahargarh and Jaigarh Forts", 11,
                         "Day 11: Jaipur's Amber, Nahargarh and Jaigarh Forts (per guide's day-by-day table)"),
                    item("activity", "City Palace, Jantar Mantar and Hawa Mahal", 12,
                         "Day 12: Jaipur City Palace, Jantar Mantar and Hawa Mahal "
                         "(per guide's day-by-day table)"),
                    item("hotel", "Jai Niwas Garden Hotel, Jaipur", 11,
                         "Jaipur lodging named in the guide (affiliate booking links on the page)"),
                    item("transport", "Drive from Jaipur to Agra", 13,
                         "Day 13: drive Jaipur to Agra (per guide's day-by-day table)"),
                    item("activity", "Taj Mahal and Agra Fort", 14,
                         "Day 14: Agra - Agra Fort and the Taj Mahal; the guide's 4-day Agra leg also names "
                         "the Baby Taj (Itimad-ud-Daulah), Mehtab Bagh and the Taj Protected Forest"),
                    item("hotel", "Coral Court Homestay, Agra", 14,
                         "Agra lodging named in the guide (affiliate booking links on the page)"),
                    item("activity", "Varanasi: Ganges ghats and boat ride", None,
                         "4-day Varanasi leg: sunrise/sunset along the Ganges ghats and a boat ride; "
                         "exact day placement within the 30-day plan not evidenced"),
                    item("activity", "Kolkata exploration", None,
                         "Final leg of the 30-day plan in Kolkata (Howrah Bridge area per the guide); "
                         "exact day placement not evidenced"),
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
