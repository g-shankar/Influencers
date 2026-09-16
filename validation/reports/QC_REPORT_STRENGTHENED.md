# QC REPORT — strengthened research pass (2026-09-16)

This report documents the strengthened research pass on the travel-influencer pilot, run under the bar: **"I SHOULD BE ABLE TO VALIDATE THIS — this cannot be some sloppy job."** Unknown remains `unknown`; nothing below invents URLs, destinations, followers, dates, prices, schedules, or precision. Where the original pipeline could not be honestly reconstructed, that is stated instead of backfilled.

Final dataset state (from `pilot.db`, loaded 2026-09-16):
- 94 itineraries · 53 distinct creators · 85 destinations · 1,155 itinerary items · 106 sources · 94 posts
- Confidence: 54 high · 35 medium · 5 low
- Longest trip: 90 days · Trips of 7+ days: 47 · Itineraries with null days: 19 (unknown, not estimated)
- Quarantined: 8 handles + 1 itinerary-level record (id 88) = 9 quarantine records, all excluded from the DB

## 1. Selection honesty

- `SELECTION_CRITERIA.md` records exactly what is known and what is not. `influencers.csv` was compiled **2026-09-15** from 14 source listicles (all named, with row counts), fixed quota 50 Instagram / 50 TikTok.
- Source publication dates: **not recorded / unknown** — stated as unknown rather than reconstructed from memory. One title contains "2025" but that is only a title hint, not a publication date.
- No original eligibility, exclusion, identity, audience-quality, engagement, recency, follower-floor, purchase-intent, niche/geography, or overlap rules were recorded. The file says so.
- A forward-looking criteria set for any future 1,000-creator sample is documented separately from what was actually done.

## 2. Search-record coverage: 100/100

- All 100 creators have documented search records: 52 original successful records, 40 original empty records, 48 dated **2026-09-16 re-search** records (explicitly labeled as re-searches, not reconstructed originals).
- Files: `validation/search_records/original_52.json`, `original_empty_40.json`, `groupA.json`–`groupF.json`.
- Outcomes of the re-search: 46 `NO_ITINERARY_FOUND`; 2 newly found and independently verified (@jessicanabongo, @courtandnate).
- Repairs made during reconciliation: Group B handles normalized to `@handle`; Groups C/D misuse of the `quarantined:true` flag corrected (set false where the handle is not in `quarantine.json`, with dated notes preserving the inspection limitations); the `@lilmsawkward` typo corrected to the real `@limsawkward` (still quarantined — no itinerary attributable, no explicit release); `@marklharriosn` confirmed as a source-list typo for `@marklharrison`.
- Browser/profile/bio-link access failures remain honestly documented, not smoothed over.

## 3. Verification: 93/93 original itineraries + 2 new

- Nine fresh-context workers re-verified all 93 original itineraries against live sources on 2026-09-16: **85 CONFIRMED, 7 CORRECTED, 1 UNVERIFIABLE, 0 FAIL**.
- The 5 showcased itineraries got claim-level verification. Claim records for ids 8, 29, 31 (410 claims) are retained — every worker item-name claim matches the packet item modulo 1-based indexing. **The worker's id-41 and id-73 sections were REJECTED and replaced** (see §5): this pass caught a verifier checking the wrong content, which is the failure mode the "verifiers must check the world, not the brief" rule exists for.
- Full claim-level evidence: `validation/reports/VERIFICATION_LOG_FULL.md` + `verification_log_full.json` (+ `verification_log_full_general.json`). Every claim carries source URL, supporting passage, source date, and explicit/inferred basis. Source dates the workers did not capture are shown as "not recorded", never invented.

## 4. Corrections applied (10 data corrections + 1 exclusion + 2 additions)

1. Id 30 (Ghana, @oneikathetraveller): 7→8 days; all item days nulled; high→medium confidence.
2. Id 32 (Abu Dhabi, @pilotmadeleine): mosque Day 2; sandboarding Day 1 (swapped).
3. Id 34 (Oahu, @pilotmadeleine): Lanikai Beach Day 2.
4. Id 47 (Oahu, @thebucketlistfamily): days 3→null.
5. Id 54 (Great Ocean Road, @theslowtraveler): Sunnymead Hotel named.
6. Id 56→57 (Portugal, @wildweroam): reframed as two separate trip fragments (Armona 2016, Berlengas 2018); title updated.
7. Id 78 (Croatia, @rileejsmith): 10→8 days.
8. Id 8 (@budgettraveller): summary's false "every leg via Skyscanner and Omio" corrected to reflect Flixbus and Deutsche Bahn usage.
9. Id 41 (Morocco, @theblondeabroad): unsupported ~$90 Day-10 taxi price removed (it belonged to a different leg).
10. Id 73 (Japan, @onegirlwandering): day assignments nulled on 15 recommendation rows the source never pins to a day.

Exclusion: packet/original id 88 (@thenationalparktravelers, "Columbia River Gorge Waterfall Drive") — **UNVERIFIABLE** verdict; no reachable supporting source. Quarantined at itinerary level and excluded from the DB. (Note: the live DB's own itinerary id 88 is an unrelated legitimate record, @themomtrotter's Utah road trip; the excluded record never received a final DB id.) It stays out unless a supporting source is produced.

Additions (verified live by the coordinator before loading):
- @jessicanabongo — "Georgia Trip - Food & Wine small-group trip (Sept 27 - Oct 2, 2024)", 6 days, 13 items (final DB id 16).
- @courtandnate — "Oregon to California Costal Road Trip" (source headline spelling preserved), 4 days, 8 items (final DB id 65).

DB reconciliation: 93 original + 2 additions − 1 exclusion = 94 itineraries; 0 orphan items, 0 orphan itineraries, 0 itineraries without sources, 0 quarantined handles with itinerary attribution.

Headline corrections vs the earlier draft report data: `longest_days` 30→**90**; `trips_7_days_or_more` 57→**47**.

## 5. Process incident: rejected verifier output

The showcase worker's id-41 output verified a stale/older version of the Morocco page and a different item set (2/24 name matches vs the packet). Its id-73 output verified a different item set (5/40 name matches vs the packet's 49 items). Both sections were **rejected, not patched**, and the coordinator re-verified all 36 + 49 packet items directly against the live pages. The rejected sections remain in `showcase_claims.json` for the record; the authoritative claim records for ids 41 and 73 are the coordinator's, dated 2026-09-16, in `verification_log_full.json`.

## 6. Residual limitations (what this pass does not claim)

- Inaccessible profiles and bio links: where a profile or bio link could not be reached, the search record says so; those creators' itineraries were not invented to fill gaps.
- Source publication dates for the general itineraries were not consistently captured; shown as "not recorded".
- Item day assignments within the source's explicit day ranges (ids 8, 29, 31) are packet conventions and are marked inferred in the verification log.
- 19 itineraries have null days; 5 low-confidence records remain in the DB, labeled as such.
- The two new itineraries (jessicanabongo, courtandnate) were verified by the coordinator, not by a separate fresh-context worker — they are the coordinator-verified exception, and are labeled as such.
- Corrections are idempotent-in-name only: `apply_corrections.py` must not be re-run without hardening, as annotation notes could duplicate.

## 7. How Gowrishankar can validate this

- `validation/reports/VERIFICATION_LOG_FULL.md` — every itinerary, verdict, source URL, and correction.
- `validation/reports/verification_log_full.json` — every claim with source URL, supporting passage, source date, explicit/inferred basis.
- `validation/search_records/` — all 100 creators' documented search attempts.
- `validation/quarantine.json` + `validation/exclude_unverifiable.json` — the 9 excluded records and why.
- `pilot.db` — the final dataset; all counts above are reproducible from it.

## 8. Evidence-only audit (2026-09-16) and one fix

A fresh-context auditor verified all claims against evidence only (DB queries, files on disk). It returned FAIL on one point: the id-41 "Taxi to Marrakech" correction had rewritten the item's `details` but left its structured `price_hint` as `~$90 USD taxi` in `pilot.db` — internally inconsistent and still readable as $90 by any DB consumer. Fixed 2026-09-16: `price_hint` cleared (NULL) on that row; the other three priced legs on the Morocco itinerary (SIM card, Tangier→Chefchaouen taxi $60, Fes→Casablanca train $12–$25) were re-checked against the live source and are correctly priced. All other audit claims passed (8/10; the remaining two were the not-yet-pushed GitHub state and the quarantine record count, both confirmed). The re-audit after the fix returned a clean PASS.
