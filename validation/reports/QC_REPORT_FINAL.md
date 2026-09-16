# Pilot QC Report — founder validation copy

Date: 2026-09-16
Validator: (Gowrishankar — everything below is independently checkable)

## Gate verdicts

| Gate | Check | Verdict | Evidence |
|------|-------|---------|----------|
| 1 | Extraction schema | PASS | `validation/reports/gate1_report.json` — 0 errors, 19 warnings (noncanonical evidence files ignored, expected) |
| 2 | Handle integrity | PASS | `validation/reports/gate2_report.json` — 100 rows, 50/50 split, 8 quarantined |
| 3 | Source liveness | PASS | `validation/reports/gate3_report.json` — 95 itineraries, 105 URLs, 0 errors; 15 script false-negatives waived with browser-fetch evidence (`gate3_override_evidence.json` + `gate3_override_log.md`) |
| 4 | Evidence council | PASS — fail rate **0%** | 36/95 itineraries (37.9%) verified claim-by-claim by fresh-context verifiers; verdicts in `validation/council_results/batch{n}_verdicts.json`; log in `validation/reports/evidence_council_log.md` |
| 5 | DB reconciliation | PASS | Output below; run it yourself: `sqlite3 pilot.db < validation/gate4_reconciliation.sql` |
| 6 | Money firewall | PASS | This report contains zero dollar figures. Vendor rows in the DB carry inline `[FACT - <source>]` tags with named, dated sources |
| 7 | Final evidence-only audit | pending (runs before completion message) | `~/workspace/audit/CHARTER.md` |

## Counts
- Influencers: **100** (TikTok 50 / Instagram 50)
- Follower counts: **73 known** (as reported by sources), **27 unknown** (stays `unknown` — never invented)
- Influencers yielding ≥1 itinerary in DB: **52**
- Itineraries extracted: **95** → **93 loaded into DB** (2 excluded: both belong to quarantined @africansafari)
- Items: **1142** | Sources: **106** | Posts: **93**
- Confidence (DB): high **53** / medium **34** / low **6**
- Vendors: **6** (Viator, OpenTable, Duffel, Booking.com/CJ, Expedia TAAP, Hotelbeds)

## Gate 5 reconciliation output (verify yourself)
- influencers_total: 100; instagram 50, tiktok 50
- empty_followers: 0
- itineraries_total: 93; items_total: 1142
- orphan_items / orphan_itineraries / orphan_posts: 0
- itineraries_without_source: 0
- quarantined_with_itineraries: 0 (all 8 quarantined handles)
- duplicate handles: none; duplicate itineraries: none

## Quarantine
| Handle | Platform | Reason | Status |
|--------|----------|--------|--------|
| @africansafari | instagram | possible brand/tour-operator account | quarantined — 2 itineraries excluded from DB |
| @limsawkward | tiktok | possible source-list typo | quarantined — 0 itineraries |
| @marklharriosn | tiktok | possible typo ('harrison'?) | quarantined — 0 itineraries |
| @nastasiawong | instagram | resolves to unrelated non-travel account | quarantined — 0 itineraries |
| @nomadicmovement | instagram | resolves to unrelated non-travel account | quarantined — 0 itineraries |
| @oceanwanderer | instagram | resolves to unrelated non-travel account | quarantined — 0 itineraries |
| @rachid_dahnoun | instagram | resolves to unrelated non-travel account | quarantined — 0 itineraries |
| @sidewalkerdaily | tiktok | influencer-marketing consultancy, not a travel creator | quarantined — 0 itineraries |

Platform labels for the 5 batch-2/batch-4 handles were corrected 2026-09-16 (see
`validation/reports/gate2_platform_correction_log.md`).

## Repairs & merges (auditable)
- `validation/reports/batch1_merge_repair_log.md` — batch-1 merge from 4 parts + 5 re-extractions
- `validation/gate1_fix_batch2.json`, `validation/gate1_fix_batch4.json` — earlier gate-1 repairs
- `validation/reports/gate3_override_log.md` + `gate3_override_evidence.json` — 15 script false-negatives

## Evidence sample (spot-check these yourself — all council-verified PASS)
| # | Itinerary | Source URL | Council |
|---|-----------|------------|---------|
| 1 | @migrationology — Ghorepani Poon Hill Trek (5-day) | https://migrationology.com/ghorepani-poon-hill-trek-ultimate-guide/ | PASS, prices down to rupee level |
| 2 | @girlvsglobe — Segovia 48 Hours | https://girlvsglobe.com/things-to-do-in-segovia-48-hours/ | PASS, 12/12 items |
| 3 | @themomtrotter — Utah National Parks RV | https://themomtrotter.com/utah-national-parks-southwest-road-trip/ | PASS, 21/21 items incl. exact costs |
| 4 | @shetravelledtheworld — Kyrgyzstan 2-week | (batch 4 source) | PASS, 14/14 items incl. som/£/$ figures |
| 5 | @taramilktea — Europe highlights | https://www.qantas.com/travelinsider/en/explore/europe/travelling-in-europe-with-instagram-star-tara-milk-tea.html | UNVERIFIABLE → independently CONFIRMED |

## Open issues
- None blocking. Non-failing verifier notes (day-assignment paraphrases, 2 omissions)
  are recorded in `validation/reports/evidence_council_log.md` — extraction is lossy,
  not fabricating.
- @lostleblanc Bali record is sourced from a third party (nomadicnews.com), not the
  creator — verified PASS; noted for packaging.

## Check it yourself (SQLite)
```bash
cd ~/workspace/travel-influencer-pilot
sqlite3 pilot.db "SELECT platform, COUNT(*) FROM influencers GROUP BY platform;"
sqlite3 pilot.db "SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence;"
sqlite3 pilot.db "SELECT t.title, f.handle FROM itineraries t JOIN influencers f ON f.id=t.influencer_id ORDER BY t.id LIMIT 10;"
sqlite3 pilot.db "SELECT name, type FROM vendors;"
```
