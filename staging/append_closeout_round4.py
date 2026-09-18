#!/usr/bin/env python3
"""Closeout round 4 appender: writes verified TikTok creators to batch9/10/11.

For each verified creator dict:
  1. REBUILD dedup universe (quarantine + influencers.csv + ALL batch*.csv) AT WRITE TIME.
  2. Case-insensitive handle dedup; on collision -> DROP (report).
  3. Append row to batch{N}.csv (7 cols), selection_log_batch{N}.csv (23 cols),
     and one extraction to staging/itineraries_batch{N}.json.

Usage: edit the CANDIDATES list, run. Exits nonzero if any candidate was dropped.
"""
import csv
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BATCH_FIELDS = ["name", "handle", "platform", "niche", "followers_approx",
                "profile_url", "source_urls"]
LOG_FIELDS = ["batch", "handle", "platform", "name", "niche", "followers_approx",
              "followers_observed", "followers_source", "profile_url",
              "discovery_source", "identity_check", "identity_method",
              "content_fit", "content_fit_evidence", "reach_floor",
              "engagement_observed", "activity_check", "purchase_intent",
              "exclusions_check", "decision", "notes", "check_date", "selector"]

CHECK_DATE = "2026-09-17"
SELECTOR = "batch-closeout-worker"


def rebuild_universe():
    """Returns (all_handles_lower, quarantined_handles_lower)."""
    allh = set()
    for f in glob.glob(str(ROOT / "batch*.csv")):
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                h = (r.get("handle") or "").strip().lower()
                if h:
                    allh.add(h)
    with open(ROOT / "influencers.csv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            h = (r.get("handle") or "").strip().lower()
            if h:
                allh.add(h)
    q = json.loads((ROOT / "validation" / "quarantine.json").read_text())
    entries = q["quarantine"] if isinstance(q, dict) else q
    quarantined = {str(e.get("handle") or "").strip().lower()
                   for e in entries if e.get("handle")}
    return allh, quarantined


def append_creator(c, universe, quarantined):
    h = c["handle"].strip()
    hl = h.lower()
    if hl in universe:
        print(f"  DROP (collision in dataset): {h}")
        return False
    if hl in quarantined:
        print(f"  DROP (quarantined): {h}")
        return False

    n = c["batch"]
    batch_csv = ROOT / f"batch{n}.csv"
    log_csv = ROOT / "staging" / f"selection_log_batch{n}.csv"
    itin_json = ROOT / "staging" / f"itineraries_batch{n}.json"

    # 1) batch csv
    with open(batch_csv, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=BATCH_FIELDS)
        w.writerow({k: c["batch_row"][k] for k in BATCH_FIELDS})

    # 2) selection log
    with open(log_csv, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=LOG_FIELDS)
        lr = dict(c["log_row"])
        lr.setdefault("batch", str(n))
        lr.setdefault("handle", h)
        lr.setdefault("platform", "tiktok")
        lr.setdefault("check_date", CHECK_DATE)
        lr.setdefault("selector", SELECTOR)
        w.writerow({k: lr.get(k, "") for k in LOG_FIELDS})

    # 3) itineraries json
    data = json.loads(itin_json.read_text(encoding="utf-8"))
    data["extractions"].append(c["extraction"])
    itin_json.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    universe.add(hl)
    print(f"  WROTE: {h} -> batch{n}")
    return True


def main():
    universe, quarantined = rebuild_universe()
    dropped = []
    for c in CANDIDATES:
        ok = append_creator(c, universe, quarantined)
        if not ok:
            dropped.append(c["handle"])
    print(f"done: {len(CANDIDATES) - len(dropped)} written, {len(dropped)} dropped")
    return 1 if dropped else 0


CANDIDATES = [
    # ---- @antavialauren: fully gated 2026-09-17, re-verified this run ----
    {
        "batch": 10,
        "handle": "@antavialauren",
        "batch_row": {
            "name": "Tav (Tav Reviews Everything)",
            "handle": "@antavialauren",
            "platform": "tiktok",
            "niche": "itineraries & food travel",
            "followers_approx": "79.5K",
            "profile_url": "https://www.tiktok.com/@antavialauren",
            "source_urls": "https://www.tiktok.com/@antavialauren/video/7488843573119536415",
        },
        "log_row": {
            "name": "Tav (Tav Reviews Everything)",
            "niche": "itineraries & food travel",
            "followers_approx": "79.5K",
            "followers_observed": "79,500",
            "followers_source": "TikTok profile @antavialauren (79,500 followers, 296 videos, 1.6M total likes), observed 2026-09-17",
            "profile_url": "https://www.tiktok.com/@antavialauren",
            "discovery_source": "prior gated candidate file staging/work/gated_candidates.json; re-verified this run",
            "identity_check": "pass",
            "identity_method": "Single named individual: display name 'Tav Reviews Everything', bio 'sharing my fav eats, itineraries, & life in between' (Atlanta + beyond); Knoxville tourism Q2 FY26 report names her 'Antavia Lauren, Atlanta-based content creator'; business email tav@tavreviewseverything.com; no duo/couple/brand signals",
            "content_fit": "pass",
            "content_fit_evidence": "tiktok.com/@antavialauren/video/7488843573119536415 '48 Hours in Miami - Save this Itinerary!' published 2025-04-02 (create_time 1743632306, within trailing 24 months): full caption lists STAY (Elser Hotel & Residences; Savoy Hotel beach club), EAT (Nick's Pizza, Big Pink, Carbone, Miam Cafe, Sky Coffee), PLAY (Miami Heat game, Rooftop Cinema Club, Brickell City Centre, Design District) - structured 2-day itinerary",
            "reach_floor": "pass",
            "engagement_observed": "211,100 plays; 9,253 likes; 151 comments; 3,202 shares; 8,526 saves on itinerary video (creator-owned video metrics, observed 2026-09-17)",
            "activity_check": "pass",
            "purchase_intent": "unknown",
            "exclusions_check": "pass",
            "decision": "include",
            "notes": "Individual creator; itinerary + food travel; Knoxville tourism FAM host (FYE26 Q2 quarterly report, visitknoxville, observed 2026-09-17); Myrtle Beach partnership video 2026-05-06 = paid brand partnership, not consumer planning; dedup clear 2026-09-17 (not in quarantine.json); no TrovaTrip/WeTravel, no group-trip hosting, no trip-planning services.",
        },
        "extraction": {
            "handle": "@antavialauren",
            "platform": "tiktok",
            "itineraries": [
                {
                    "title": "48 Hours in Miami – Save this Itinerary!",
                    "destination": "Miami",
                    "country": "USA",
                    "days": 2,
                    "confidence": "high",
                    "summary": "Tav (@antavialauren) publishes a structured 48-hour Miami itinerary in the caption of her TikTok video (2025-04-02): where to STAY (Elser Hotel & Residences; Savoy Hotel beach club access), EAT (Nick's Pizza South Beach, Big Pink, Carbone, Miam Cafe, Sky Coffee) and PLAY (Miami Heat game, Rooftop Cinema Club, Brickell City Centre, Design District).",
                    "source_urls": ["https://www.tiktok.com/@antavialauren/video/7488843573119536415"],
                    "items": [
                        {"day": 1, "item_type": "hotel", "name": "The Elser Hotel & Residences", "location": "Miami, USA", "details": "Studio Suite with bay view, full kitchen, washer + dryer; rooftop pool with skyline views; 2-story gym.", "booking_link": None, "price_hint": None},
                        {"day": 1, "item_type": "hotel", "name": "The Savoy Hotel and Beach Club", "location": "Miami Beach, USA", "details": "Beach club access: chairs, umbrellas, towels + poolside food.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "restaurant", "name": "Nick's Pizza South Beach", "location": "Miami Beach, USA", "details": "Giant 2-foot pizza + a pizza flight.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "restaurant", "name": "Big Pink", "location": "Miami, USA", "details": "Spinach dip, cheesy + crispy.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "restaurant", "name": "Carbone", "location": "Miami, USA", "details": "Spicy rigatoni, tortellini, baked clams.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "restaurant", "name": "Miam Café", "location": "Miami, USA", "details": "Dulce de leche pancakes.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "restaurant", "name": "Sky Coffee", "location": "Miami, USA", "details": "Coffee shop inside an airplane.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "activity", "name": "Miami Heat game", "location": "Miami, USA", "details": "Watch a Miami Heat basketball game.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "activity", "name": "Rooftop Cinema Club", "location": "Miami, USA", "details": "Outdoor late-night cinema under the stars.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "activity", "name": "Brickell City Centre", "location": "Miami, USA", "details": "Shopping district for retail therapy.", "booking_link": None, "price_hint": None},
                        {"day": None, "item_type": "activity", "name": "Design District", "location": "Miami, USA", "details": "Luxury shopping and retail.", "booking_link": None, "price_hint": None},
                    ],
                }
            ],
            "notes": "",
        },
    },
]

if __name__ == "__main__":
    sys.exit(main())
