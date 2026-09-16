#!/usr/bin/env python3
"""Apply 2026-09-16 full-verification corrections to the canonical staging files.

Each correction comes from an independent verifier's verdict in
validation/council_results_full/workerN_verdicts.json (or showcase_claims.json).
Corrections are annotated in the itinerary summary with a dated note; confidence
is adjusted where the original record contained invented structure.

Idempotent: skips corrections already applied (checks for the note marker).
Writes validation/corrections_applied.json log. Does NOT touch the DB — run
load_db.py afterwards (with --exclude-json for quarantined id 88).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
MARK = "[Correction 2026-09-16]"

def load(n):
    p = STAGING / f"itineraries_batch{n}.json"
    return p, json.loads(p.read_text())

def save(p, data):
    p.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")

def find(data, handle, title_start):
    for ex in data.get("extractions", []):
        if ex["handle"] == handle:
            for it in ex.get("itineraries", []):
                if it["title"].startswith(title_start):
                    return it
    raise KeyError(f"not found: {handle} / {title_start}")

def annotate(it, note):
    if MARK not in (it.get("summary") or ""):
        it["summary"] = (it.get("summary") or "") + f" {MARK} {note}"
    else:
        it["summary"] += f" | {note}"

applied = []

# --- id 32 @pilotmadeleine Abu Dhabi: day swap per source diary titles ---
p, d = load(2)
it = find(d, "@pilotmadeleine", "Abu Dhabi Travel Diary")
for item in it["items"]:
    if "Grand Mosque" in item["name"] or "Sheikh Zayed" in item["name"]:
        item["day"] = 2
    if "Sand Boarding" in item["name"]:
        item["day"] = 1
annotate(it, "Day assignments corrected to the source's own diary titles: Sheikh Zayed Grand Mosque -> Day 2 ('Abu Dhabi Travel Diary Day 2'), Sand Boarding -> Day 1 (desert safari in 'Day 1' post).")
save(p, d); applied.append("id32: Grand Mosque day 1->2, Sand Boarding day 2->1")

# --- id 34 @pilotmadeleine Hawaii: Lanikai Beach day null -> 2 ---
p, d = load(2)
it = find(d, "@pilotmadeleine", "Hawaii Travel Diary: Oahu")
for item in it["items"]:
    if item["name"] == "Lanikai Beach":
        item["day"] = 2
annotate(it, "Lanikai Beach day set to 2: source places it in the 'Hawaii Day 2' section ('Around sunset we went to my favorite beach: Lanikai Beach').")
save(p, d); applied.append("id34: Lanikai Beach day null->2")

# --- id 54 @theslowtraveler: name the hotel per source ---
p, d = load(2)
it = find(d, "@theslowtraveler", "Epic 3-Day Road Trip")
for item in it["items"]:
    if item["name"] == "Hotel in Aireys Inlet (unnamed)":
        item["name"] = "Sunnymead Hotel (Aireys Inlet)"
annotate(it, "Day-1 hotel named per source: 'We spent the night in the Sunnymead Hotel'.")
save(p, d); applied.append("id54: hotel named 'Sunnymead Hotel (Aireys Inlet)'")

# --- id 47 @thebucketlistfamily Oahu: days 3 -> null (source: 'The few days') ---
p, d = load(2)
it = find(d, "@thebucketlistfamily", "Hawaii family stop")
it["days"] = None
annotate(it, "Day count removed: source says only 'The few days'; the packet's days=3 was an inference, not a source claim.")
save(p, d); applied.append("id47: days 3->null")

# --- id 56 @wildweroam: separate 2016 and 2018 fragments ---
p, d = load(2)
it = find(d, "@wildweroam", "Two Weeks in Portugal")
it["title"] = "Portugal trip fragments: Armona 2016 + Berlengas camping 2018"
annotate(it, "Temporal framing corrected: the 2016 'two weeks' claim belongs to the Armona post (2017/11/28); the Berlengas camping post is dated 2018/09/27 and describes planning for 2019. They are separate trips, not one 2016 itinerary.")
save(p, d); applied.append("id56: retitled; summary separates 2016 Armona and 2018 Berlengas fragments")

# --- id 30 @oneikathetraveller Ghana: days 7 -> 8; day numbers -> null ---
p, d = load(2)
it = find(d, "@oneikathetraveller", "The Ultimate One-Week Ghana")
it["days"] = 8
for item in it["items"]:
    item["day"] = None
it["confidence"] = "medium"
annotate(it, "Day count corrected 7->8: source body states 'exactly eight days' (sections 4+2+2; 'one week' is headline shorthand). Item day-numbers removed: the source organizes by city section (Accra / Kumasi / Cape Coast) and never numbers days; the packet's specific day assignments were invented. Confidence high->medium.")
save(p, d); applied.append("id30: days 7->8, item day-numbers nulled, confidence high->medium")

# --- id 78 @rileejsmith: days 10 -> 8 ---
p, d = load(4)
it = find(d, "@rileejsmith", "Croatia: Hvar & Dubrovnik")
it["days"] = 8
annotate(it, "Day count corrected 10->8: source body says '8-day Hvar + Dubrovnik itinerary'; '10 Days in Croatia' is the paid product's listing name, not the itinerary length.")
save(p, d); applied.append("id78: days 10->8")

# --- id 8 @budgettraveller: summary booking-channel correction (showcase claim-level pass, coordinator-verified against live source) ---
p, d = load(1)
it = find(d, "@budgettraveller", "How to Visit 15 European Cities")
old_phrase = "with every intercity transport leg booked 2 months ahead via Skyscanner and Omio"
new_phrase = ("with transport legs priced ~2 months ahead: Skyscanner (London to Paris flight), Omio (Paris to Amsterdam, "
              "Amsterdam to Rotterdam), Flixbus booked directly (Rotterdam to Ghent, Ghent to Leuven), Deutsche Bahn/bahn.com (Leuven to Cologne)")
assert old_phrase in it["summary"], "id8 summary phrase not found"
it["summary"] = it["summary"].replace(old_phrase, new_phrase)
annotate(it, "Booking-channel claim corrected: source's per-leg lines show 'Found via Flixbus' (Rotterdam->Ghent, Ghent->Leuven) and 'Found via Deutsche Bahn website' (Leuven->Cologne); 'every leg via Skyscanner and Omio' was contradicted by the source.")
save(p, d); applied.append("id8: summary booking channels corrected (Flixbus x2, bahn.com x1)")

# --- id 41 @theblondeabroad Morocco: item 18 taxi price misattribution (coordinator re-verification of live source) ---
# The showcase worker's 6 'corrections' for id 41 were REJECTED: they verified a stale/older version of the page
# ('The Ultimate 2 Week Morocco Itinerary': Riad El Fenn, Dar Seffarine, Days 1-3/4-6/7-8/11-13/13-15), not the
# packet's record ('Itinerary for Two Weeks in Morocco', Riad Yasmine/La Mamounia/Tangier/Chefchaouen/Casablanca),
# which matches the live page fetched 2026-09-16. Only one real correction found:
p, d = load(2)
it = find(d, "@theblondeabroad", "Itinerary for Two Weeks in Morocco")
for item in it["items"]:
    if item["name"] == "Taxi to Marrakech" and item.get("day") == 10:
        item["details"] = ("Taxi from Essaouira to Marrakech (Day 10 per source). No price stated for this leg in the source; "
                           "the ~$90 figure appears in the source's Essaouira-arrival paragraph describing a different taxi ride.")
annotate(it, "Item 'Taxi to Marrakech' price corrected: the ~$90 in the source belongs to the taxi described in the Essaouira arrival section, not the Day-10 Essaouira->Marrakech leg (no price stated).")
save(p, d); applied.append("id41: Taxi to Marrakech ~$90 price removed (misattributed)")

# --- id 73 @onegirlwandering Japan: null days on recommendation rows with no source-pinned day ---
# The showcase worker's id-73 verification was also REJECTED (it verified a different item set: 5/40 name matches
# vs the packet). Coordinator re-verified the packet's 49 items directly against the live source 2026-09-16:
# items [0]-[32] carry source-explicit days 1-11; [33]/[34] sit at the range-start of the source's explicit
# Days 12-14 block (accepted packet convention, consistent with id 29). The rows below have no source-pinned day.
p, d = load(4)
it = find(d, "@onegirlwandering", "The Perfect Two Week Itinerary")
null_names = {"Wakkoqu", "Nikko day trip",
              "Maguroya Kurogin", "Gonpachi", "Ichiran Ramen",
              "Gogyo Ramen", "Katsukura", "Chibo Okonomiyaki",
              "Park Hyatt Tokyo", "APA Hotel Asakusa Kaminarimon",
              "The Ritz-Carlton Kyoto", "Hyatt Regency Kyoto", "Dormy Inn Premium Kyoto Ekimae",
              "Swissotel Nankai Osaka", "Dormy Inn Osaka Tanimachi"}
nulled = 0
for item in it["items"]:
    if item["name"] in null_names:
        item["day"] = None
        nulled += 1
annotate(it, f"Day assignments removed from {nulled} recommendation rows (city-level hotel/restaurant picks and the Nikko option): the source never pins them to a specific day; the packet's days were conventions, not source claims. Items [0]-[32] keep source-explicit days 1-11; teamLab/Disney keep day 12 as range-start of the source's explicit Days 12-14 block.")
save(p, d); applied.append(f"id73: {nulled} recommendation-row days nulled")

log = {"applied_at": "2026-09-16", "corrections": applied,
       "note": "id 88 (@thenationalparktravelers, UNVERIFIABLE) is excluded at load time via --exclude-json and recorded in quarantine.json, not edited here."}
(ROOT / "validation" / "corrections_applied.json").write_text(json.dumps(log, indent=1) + "\n")
print("\n".join(applied))
print("corrections log written; staging files updated (idempotent).")
