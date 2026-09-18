#!/usr/bin/env python3
"""Stage 2 closer: append @globetrottergirls (Dani Heinrich) to Batch 20.

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
    ["Dani Heinrich", "@globetrottergirls", "instagram", "solo female / LGBTQ travel",
     "17800", "https://www.instagram.com/globetrottergirls/",
     "https://globetrottergirls.com/48-hours-in-austin-texas/"],
]

# ------------------------------------------------------- selection log (23 col)
LOG_ROWS = [
    ["20", "@globetrottergirls", "instagram", "Dani Heinrich", "solo female / LGBTQ travel",
     "17800", "17.8K",
     "Feedspot Top 100 Female Travel Influencers 2026 list observed 2026-09-17 (list page itself updated ~24 "
     "days earlier; verbatim URL not retained)",
     "https://www.instagram.com/globetrottergirls/", "Stage 2 batch-20 closer round 2 (batch20-topup)",
     "pass",
     "Dani Heinrich is identified as the writer/photographer behind GlobetrotterGirls.com by Matador Network, "
     "Contiki, and Nomadic Matt bios; Feedspot entry gives exact handle @globetrottergirls with her bio",
     "pass",
     "'48 Hours in Austin, Texas' on own site: 'Last Updated on January 22, 2026'; structured weekend "
     "itinerary - Friday 2pm downtown bike ride (B-Cycle Weekender Pass $19.49, Lady Bird Lake, Zilker Park, "
     "Doug Sahm Hill), food trucks (Tommy Want Wingy, Chi'lantro, Micklethwait Craft Meats), South Congress "
     "stroll, Congress Avenue Bridge bat flight, Rainey Street bar-hopping, Geraldine's at Hotel Van Zandt; "
     "Saturday brunch at 24 Diner, Hope Outdoor Gallery, Torchy's Tacos, Texas State Capitol free tour, "
     "Franklin's BBQ, Azul Rooftop sunset drinks, live music at the Continental Club, Midnight Cowboy "
     "speakeasy; Sunday breakfast tacos (Veracruz All Natural, El Primo, Juan in a million); page links "
     "booking.stay22.com for Austin hotels (affiliate). Full item detail harvested from the opened page.",
     "pass",
     "unknown (nonblocking) - third-party engagement tools not publicly accessible 2026-09-17; per the "
     "2026-09-17 Batch 20 final-decision precedent engagement is nonblocking for all includes",
     "pass (guide page last updated January 22, 2026; Feedspot bio shows current location trail "
     "'Next: Philippines & Mexico'; sitemap-crawl current)",
     "present (affiliate booking.stay22.com hotel links on the guide page; named hotels, restaurants, and "
     "paid activities/transport throughout)",
     "pass - targeted 2026-09-17 searches found no consumer itinerary planning/coaching/courses/workshops/"
     "hosted group trips/agency offer tied to Dani Heinrich or GlobetrotterGirls; site is an editorial travel "
     "blog with affiliate links",
     "include",
     "Named individual (Dani Heinrich). Qualifying 48-hour Austin itinerary last updated 2026-01-22 (in "
     "window). Reach 17.8K IG (Feedspot). Item-level content harvested from the opened guide page.",
     CHECK_DATE, SELECTOR],
]

# ------------------------------------------------- itineraries_batch20.json
EXTRACTIONS = [
    {
        "handle": "@globetrottergirls",
        "platform": "instagram",
        "notes": "Dani Heinrich: named individual writer/photographer behind GlobetrotterGirls.com "
                 "(Matador/Contiki/Nomadic Matt bios; Feedspot entry). Reach: 17.8K Instagram per Feedspot Top "
                 "100 Female Travel Influencers 2026 (observed 2026-09-17). Qualifying guide: '48 Hours in "
                 "Austin, Texas', last updated January 22, 2026, with a structured Friday-to-Sunday itinerary "
                 "and affiliate hotel links. Exclusion sweep 2026-09-17 found no consumer services. Day-by-day "
                 "items harvested from the opened guide page; Friday=day 1, Saturday=day 2, Sunday=day 3.",
        "itineraries": [
            {
                "title": "48 Hours in Austin, Texas",
                "destination": "Austin",
                "country": "United States",
                "days": 3,
                "summary": "A structured weekend itinerary for a first-time Austin trip on the creator's own "
                           "site (last updated January 22, 2026): Friday 2pm downtown bike ride (B-Cycle "
                           "Weekender Pass $19.49, Lady Bird Lake, Zilker Park, Doug Sahm Hill skyline views), "
                           "food trucks, a 5pm South Congress stroll, the 7-8pm Congress Avenue Bridge bat "
                           "flight, and 9pm Rainey Street bar-hopping; Saturday brunch at 24 Diner, Hope "
                           "Outdoor Gallery street art, Torchy's Tacos, a free Texas State Capitol tour, "
                           "Franklin's BBQ dinner, sunset drinks at Azul Rooftop, live music at the "
                           "Continental Club, and the Midnight Cowboy speakeasy; Sunday breakfast tacos.",
                "source_urls": ["https://globetrottergirls.com/48-hours-in-austin-texas/"],
                "confidence": "high",
                "items": [
                    item("transport", "B-Cycle Weekender Pass bike ride around downtown", 1,
                         "Friday 2pm: explore downtown by B-Cycle bike share - Weekender Pass $19.49 for three "
                         "full days; ride 6th Avenue, Congress Avenue, Lady Bird Lake and Zilker Park"),
                    item("activity", "Doug Sahm Hill skyline views in Butler Park", 1,
                         "Stop at Doug Sahm Hill in Butler Park (across the river) for the best downtown "
                         "skyline views"),
                    item("restaurant", "Tommy Want Wingy food truck", 1,
                         "Guide's food truck recommendation: Tommy Want Wingy"),
                    item("restaurant", "Chi'lantro, 823 Congress Ave", 1,
                         "Asian-fusion comfort food truck at 823 Congress Ave"),
                    item("restaurant", "Micklethwait Craft Meats, 1309 Rosewood Ave", 1,
                         "East Side BBQ food truck at 1309 Rosewood Ave; also named: The Peached Tortilla "
                         "(banh mi tacos)"),
                    item("activity", "South Congress stroll: shops and murals", 1,
                         "5pm stroll along South Congress - Uncommon Objects, Allens Boots, Lucy in Disguise "
                         "with Diamonds, the Willie Nelson and 'I Love You So Much' murals"),
                    item("restaurant", "Guero's Taco Bar", 1,
                         "Sundowner margarita at Guero's Taco Bar on South Congress; June's wine bar also named"),
                    item("activity", "Congress Avenue Bridge bat flight at sunset", 1,
                         "7-8pm: watch the Mexican free-tailed bat colony fly out at sunset "
                         "(season: March to October)"),
                    item("activity", "Rainey Street bar-hopping", 1,
                         "9pm: bar-hop along Rainey Street - Banger's Beer Garden (100+ beers on tap), "
                         "Container Bar"),
                    item("restaurant", "Geraldine's at Hotel Van Zandt", 1,
                         "Fancy-dinner option: Geraldine's contemporary restaurant inside Hotel Van Zandt "
                         "(reserve in advance); Via 313 Pizza Truck as the casual alternative"),
                    item("restaurant", "24 Diner brunch, 600 N Lamar", 2,
                         "Saturday 9am brunch at 24 Diner (600 N Lamar); Waterloo Records vinyl store a couple "
                         "of doors down"),
                    item("activity", "Hope Outdoor Gallery street art", 2,
                         "11am: Hope Outdoor Gallery graffiti park (the guide's 2024 update notes it was "
                         "demolished and keeps it to commemorate it); alternative: Umlauf Sculpture Park "
                         "($7 admission)"),
                    item("restaurant", "Torchy's Tacos", 2,
                         "1pm food-truck lunch: Torchy's Tacos"),
                    item("activity", "Texas State Capitol free guided tour", 2,
                         "3pm culture: free half-hour guided tour of the Texas State Capitol (last Saturday "
                         "tours 3:30pm); museum alternatives: Blanton Museum of Art, Bob Bullock Texas State "
                         "History Museum, The Contemporary Austin, Mexic-Arte Museum"),
                    item("restaurant", "Franklin's BBQ, 900 E 11th St", 2,
                         "6pm BBQ dinner: Franklin's at 900 E 11th St (famous; long lines); alternatives La "
                         "Barbecue, Terry Black's BBQ, Stiles Switch BBQ & Brew, Lamberts Barbeque"),
                    item("activity", "Sunset drinks at Azul Rooftop", 2,
                         "8pm sunset drinks: Azul Rooftop on the 20th floor of The Westin (pool, cabanas, craft "
                         "cocktails); alternatives La Piscina (Proper Hotel), 77 Degrees, Edge Rooftop "
                         "(Marriott), Maggie Mae's (6th Street)"),
                    item("activity", "Live music at the Continental Club", 2,
                         "9pm live music: the Continental Club on South Congress (oldest and most popular "
                         "venue); alternatives Antone's (blues), Broken Spoke (two-step), The White Horse "
                         "(country), Stubb's, Mohawk, Cheer Up Charlie's"),
                    item("activity", "Midnight Cowboy speakeasy", 2,
                         "11pm: Midnight Cowboy speakeasy on 6th Street (reservation required to get in); "
                         "less-crowded alternative: Garage, located in a parking garage"),
                    item("restaurant", "Breakfast tacos at Veracruz All Natural", 3,
                         "Sunday 9am Texas-style breakfast: breakfast tacos at El Primo, Veracruz All Natural, "
                         "Juan in a million, Pueblo Viejo or Taqueria Mi Trailita; full Tex-Mex breakfast at "
                         "Curra's Grill or Trudy's Texas Star"),
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
