# Itinerary Extraction Brief — travel influencer pilot

## Goal
For each influencer in your assigned batch CSV, find the travel itineraries they actually promote and extract structured data.

## Method per influencer
1. Search the web for the handle + itinerary/guide keywords, e.g. `"@handle itinerary"`, `"@handle" "7 day" Japan`, `"@handle" travel guide`.
2. Check their bio link (Linktree/beacons/blog) for itinerary or guide posts; open 1–3 of the most itinerary-like pages.
3. Use `social.search` for the handle to find recent itinerary-style posts.
4. Extract 1–3 itineraries per influencer where they genuinely exist. If an influencer posts no extractable itinerary content (only photos, no plans/guides), record `"itineraries": []` and explain in `notes` — never force one.

## What counts as an itinerary
A named trip/plan with a destination and some structure: day-by-day plans, "3 days in X" guides, hotel/activity/restaurant recommendations tied to a trip. A single pretty photo with "Santorini 😍" is NOT an itinerary.

## Extraction fields (per itinerary)
- title, destination, country, days (integer, null if unclear), summary (2–3 sentences)
- source_urls: every page/post you pulled facts from (required — no source, no itinerary)
- confidence: high (day-by-day plan from their own guide/post) / medium (recommendation list tied to a trip) / low (fragmentary mentions pieced together)
- items: array of {day, item_type, name, location, details, booking_link, price_hint}
  - item_type ∈ flight | hotel | activity | restaurant | transport | other
  - Only include items the influencer actually named or clearly implied. booking_link only if they linked it.

## Honesty rules (hard)
- NEVER invent hotels, restaurants, activities, prices, or day counts. If the source doesn't say it, the field is null.
- Follower counts and bio facts come from the batch CSV — do not re-verify, do not change.
- Every itinerary must have ≥1 source_url. Unsourced = deleted.

## Deliverable
Write `~/workspace/travel-influencer-pilot/staging/itineraries_batchN.json` (N = your batch number) with this shape:
{
  "batch": N,
  "extractions": [
    {
      "handle": "@x",
      "platform": "instagram",
      "itineraries": [ { "title": "...", "destination": "...", "country": "...", "days": 7, "summary": "...", "source_urls": ["..."], "confidence": "high", "items": [ {"day": 1, "item_type": "hotel", "name": "...", "location": "...", "details": "...", "booking_link": null, "price_hint": null} ] } ],
      "notes": ""
    }
  ]
}

## When done
Reply with: how many influencers processed, how many yielded ≥1 itinerary, total itineraries extracted, and the single richest itinerary source you found (handle + what it contained).
