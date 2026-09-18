# Batch 17 Top-Up — Completion Report (shortfall documented)
**Date:** 2026-09-17 (America/New_York)
**Worker:** batch17-topup (subagent)

## Outcome: SHORTFALL — 4 of 25 verified, written honestly, no padding

Three output files were written with **only verified records**:

- `batch17.csv` — 4 rows, 7 columns ✓
- `staging/selection_log_batch17.csv` — 4 rows, 23 columns ✓
- `staging/itineraries_batch17.json` — batch 17, 4 extractions, 4 itineraries, 59 items, all `booking_link` null ✓

Per the top-up brief ("genuine shortfall is preferable to padding"), no unverified or
borderline creators were included to reach 25.

## Verified creators (all dedup-clear vs 443-line universe, rechecked at write time)

| # | Handle | Name | Reach (observed 2026-09-17) | Itinerary (after 2024-09-17 floor) |
|---|--------|------|------------------------------|--------------------------------------|
| 1 | @charlies_wanderings | Charlotte Lint | 127.8K (SocialVines) | 7-day Tenerife (2025-08-10 via search-age arithmetic) |
| 2 | @talesofabackpacker | Claire Sturzaker | 23.1K (Feedspot snapshot) | 2-day Barcelona (updated 2025-12-10) |
| 3 | @elise.abroad | Elise (one-person pseudonym) | 28K (Feedspot snapshot) | 24 Hours in Athens (2025-05-09) |
| 4 | @theworldtravelguy | David Leiter | 12.2K (Feedspot snapshot) | 10-day Buton & Muna, day-by-day (updated ≈2026-08-26) |

All four: identity ✓, reach ≥10K ✓, recent structured creator-owned itinerary ✓,
2025–2026 activity ✓, exclusions (no consumer planning/coaching/hosted group trips) ✓.
Evidence and methods are recorded per-row in `staging/selection_log_batch17.csv`.

## Scoped Gate 1 result: FAIL (expected — this is the honest shortfall signal)

- `stage.json` backed up byte-for-byte (md5 `52bc45768314456ad919d35e85f91a41`), batches
  temporarily scoped to `[17]`, `validation/gate1_schema.py` run, original restored and
  verified byte-identical via `cmp`.
- `validation/reports/gate1_report.json` now contains **only batch 17**: 1 error —
  `'extractions' must be a list of exactly 25 (got 4)`; 26 warnings, all
  "non-canonical file ignored by gates" for other batches' files (expected under scoping).
- **Zero schema errors** in the 4 extractions: titles, destinations, summaries, source URLs,
  confidences, and item types all validate. The single FAIL is the count rule vs the
  genuine shortfall — not concealed, not bypassed.

## Binding rejects applied during this run (with cause)

- `@fivelittledoves` — family brand: site presents "Five Little Doves" as a family
  travel & lifestyle blog ("we share our lives"; "Laura and her little doves… plus Mr Dove").
  Falls under the families/shared-accounts exclusion.
- `@globalgallivanting` — her own blog ("My 2021 Travel and Life Round Up") states she was
  "running my first group tour in Kerala". Hosted group-trip operator evidence → excluded
  fail-closed.
- `@tigerlillyquinn` — referenced 3-day Lisbon itinerary post URL not recoverable without
  page fetch (barred this run); reach citation (~102K) uncited; family/shared-account risk
  unresolved. Not watertight → dropped.
- `@thesweetwanderlust` — itinerary page URL not recoverable; reach citation uncited;
  university group-travel planning history adds exclusion ambiguity. Dropped.
- `@thirdeyetraveller` — no Instagram reach citation found (only Pinterest 12.9K, wrong
  platform). Dropped.
- `@journeywithjarv` — no recent structured creator-owned itinerary found (site page
  ~2019/2452d old). Dropped.
- `@jessicasample`, `@wanderwithjo`, `@boundlessroads`, `@travelikealocalma` — multiple
  gates open each; discovery pool exhausted. Dropped.
- Prior binding rejects (operators, planners, couples, duos, family/shared accounts)
  remain excluded; dedup hits (`@findingalexx`, `@dangerousbiz`, `@em_luxton`,
  `@myadventuresacrosstheworld`, `@indianahannah_blog`, `@vickyflipflop`,
  `@heatheronhertravels`, `@bordersofadventure`, `@globetrottergirls`,
  `@thebackpackingmom`, etc.) were not reused.

## Aggregates

- Verified additions: **4** creators; **4** with itineraries; **4** itineraries; **59** items.
- Niche mix: travel itineraries, backpacking travel, city guides, adventure travel.
- Richest source: `theworldtravelguy.com/muna-island/` (25 items, day-by-day).
- Rejects this run: 6 hard + 4 cold-pool = 10 documented above.

## Notes for parent

- No login, outreach, engagement, booking, purchase, DB load, git push, or external
  message occurred. No other batch files were touched; `stage.json` is byte-identical.
- A fresh-context independent auditor subagent could not be spawned from this worker
  (`can_spawn=no`); a rigorous evidence-only self-audit was performed instead. An
  independent audit is recommended before any completion claim.
- Completion remains the user's call; this batch is a documented 4/25 shortfall.
