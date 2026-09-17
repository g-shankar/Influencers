# Slide calculations — provenance for every displayed number

Review date: 2026-09-16 (UTC). Database version below. Every number on the
information deck must be reproducible from these queries. Two mismatches were
found against `report/final_report_data.json` and are flagged for correction.

## Database version

- File: `~/workspace/travel-influencer-pilot/pilot.db`
- SHA-256: `3b68b96a8806cf1aaafb185ffe7de740a1034513ac3f15e816e2eba25ddf29e6`
- SQLite: 3.45.1. File mtime: 2026-09-15 22:14:20 -0400 (report JSON generated
  2026-09-15 22:18:33 -0400, i.e. from this DB version).
- Row counts: influencers 100, itineraries 93, itinerary_items 1142,
  itinerary_sources 106, posts 93, vendors 6.

## Reproducible numbers (all verified 2026-09-16)

| Deck number | Query | Result | Status |
|---|---|---|---|
| 100 creators | `SELECT COUNT(*) FROM influencers` | 100 | MATCH |
| 50 TikTok / 50 Instagram | `SELECT platform, COUNT(*) FROM influencers GROUP BY platform` | 50 / 50 | MATCH |
| 73 known follower counts | `SELECT COUNT(*) FROM influencers WHERE followers_approx != 'unknown'` | 73 | MATCH |
| 27 unknown | `SELECT COUNT(*) FROM influencers WHERE followers_approx = 'unknown'` | 27 | MATCH |
| 52 creators with itineraries | `SELECT COUNT(DISTINCT influencer_id) FROM itineraries` | 52 | MATCH |
| 93 itineraries | `SELECT COUNT(*) FROM itineraries` | 93 | MATCH |
| 1,142 items | `SELECT COUNT(*) FROM itinerary_items` | 1142 | MATCH |
| 106 sources | `SELECT COUNT(*) FROM itinerary_sources` | 106 | MATCH |
| 84 destinations | `SELECT COUNT(DISTINCT destination) FROM itineraries` | 84 | MATCH |
| Shortest trip 1 day | `SELECT MIN(days) FROM itineraries` | 1 | MATCH |
| Confidence 53 high / 34 med / 6 low | `SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence` | 53 / 34 / 6 | MATCH |
| 8 quarantined | `validation/quarantine.json` (not in DB) | 8 handles | MATCH |

## MISMATCHES — flagged for correction

1. **Longest trip.** Deck/report says 30 days. `SELECT MAX(days) FROM itineraries`
   returns **90** — "3-Month Southeast Asia Itinerary: The Banana Pancake Trail"
   (id 44, medium confidence). Deck slide "1–30-day trips" is wrong; correct
   range is 1–90 days.
2. **Trips of 7+ days.** Report says 57. `SELECT COUNT(*) FROM itineraries WHERE
   days >= 7` returns **47**. No alternative query against this DB reproduces 57
   (checked: >=7 items → 70; days>=7 OR NULL → 65). The 57 is not reproducible
   and must be corrected to 47 or re-derived with a documented query.
3. Note: 18 itineraries have NULL `days` (destination guides without a fixed
   length). Any "trip length" statistic must state how NULLs are treated.

## Top-10 creators by reach (derivation)

`followers_approx` is text ("9.3M", "2.4M", "unknown"), so ranking is done in
Python: parse numeric prefix × (M=1e6, K=1e3), sort descending, "unknown" last.
Verified 2026-09-16 the parse reproduces the deck's top 10 exactly
(@erikakullberg 9.3M … @gypsea_lust 1.8M), with per-handle itinerary counts from
`SELECT COUNT(*) FROM itineraries i JOIN influencers inf ON ... WHERE
inf.handle=? AND inf.platform=?`. Tie note: @taramilktea also 1.8M sits at #11;
tie-break order between equal values is arbitrary and should be stated.

## Flagship itineraries (retrieval)

Each flagship was re-fetched 2026-09-16 by handle and title; days, item counts,
confidence, and destinations all match the deck. Item counts come from
`SELECT COUNT(*) FROM itinerary_items WHERE itinerary_id=?`. Destination strings
in the DB are more detailed than the deck's shortened labels (e.g. full
"Northern Sweden: Luleå, Umeå, …" vs deck "Northern Sweden: Luleå to Uppsala") —
shortening is editorial, not a data change.

## Action required

- Correct `final_report_data.json`: longest_days 30 → 90; trips_7_days_or_more
  57 → 47 (or documented re-derivation).
- Correct deck slide 5: "1–30-day trips" → "1–90-day trips".
- These corrections belong in the strengthening pass's regenerated report.
