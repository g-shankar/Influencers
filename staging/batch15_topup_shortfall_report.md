# Batch 15 top-up — shortfall report (2026-09-17, selector batch15-topup)

Assignment: finish batch15 (20 banked Instagram rows) with up to 5 new strictly-verified creators (target 25).

## Outcome: 0 additions. Final count 20/25. Shortfall of 5, reported honestly — no padding.

## Why
~35 public web searches this turn (plus prior-session research) produced zero creators passing all seven binding gates under the 2026-09-17 revocation standard:
- plain-`unknown` engagement = FAIL (needs creator media kit or same-creator TikTok/YouTube metrics, named source + observation date),
- itinerary date must be an explicit post-2024-09-17 calendar date on the creator's own page,
- reach must be the most precise figure the named source gives.

## Leads researched and rejected this turn
| Handle | Name | Reason |
|---|---|---|
| @heykayadams | Kay Adams | Not a travel creator — NFL sportscaster (content-fit fail) |
| @pang_bang | Nicole Pang | Paid Rexby guides carry no explicit publication dates (date fail) |
| @chaiwalla | Allan Edward Hinton | Photography niche; no creator-owned structured itinerary found |
| @meanderandwander | Rachita Saxena | Old blog content (~2021), Qoruz metrics stale (~3 yrs); no in-window dated guide + current engagement |
| @solotravelinstyle | Ioana Moga | Fully verified earlier but BANKED in batch16.csv — dedup blocked |
| @dreamsinheels | Olga Maria | Guest-contributed itinerary from 2023; no dated own-itinerary by the creator |
| @dangerousbiz | Amanda Williams | Banked in batch20.csv — dedup blocked |
| @sinahsstories | Sinah | Dedup universe hit (1 match) — blocked |
| @bydanawang, @melaniesutra, @joannehollings, @girlborntotravel, @kelleesetgo, @heynadine, @laurabaella, @kailofthewild, @afootprintsstory, @solowithsav | — | No creator-owned explicitly-dated in-window itinerary, or no engagement signal, established |
| @solotravelingsonia, @kailofthewild, @prettyweewanderer, @solowithsav | — | Prior rejects confirmed (no blog / mismatched identity / prior reject) |

## Quarantine additions (validation/quarantine.json, 85 → 88, status=excluded, added 2026-09-17)
- @hutravelstheworld — Feedspot bio "Hosting group trips" (hosted-trip exclusion)
- @lostwithpurpose — Feedspot bio "Join my Pakistan tours" (hosted-trip exclusion)
- @_thehungryhiker — Feedspot bio "Backpacking Coach" (consumer coaching exclusion)
(@girlgoingtravel and @thesojournies were already present as exclusions.)

## Files
- batch15.csv, staging/selection_log_batch15.csv, staging/itineraries_batch15.json: UNCHANGED (20 rows each; no new rows verified).
- validation/quarantine.json: +3 excluded entries (re-read before write).

## Gate 1 (scoped to batches=[15], stage.json restored byte-identically afterwards)
- Verdict: FAIL, errors=2, warnings=32.
- Error 1: batch15 'extractions' = 20, not 25 → the documented shortfall.
- Error 2 (PRE-EXISTING, untouched): batch15[18] @haileyoutside, "7 Days Costa Rica Itinerary | Costa Rica with Kids", items[0].day = 0 — 'day' must be positive int or null.
- All 32 warnings are in the pre-existing 20 rows; no new rows were written.
