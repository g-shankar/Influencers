# Batch 1 — Merge & Repair Log (2026-09-16)

## Canonical file
`staging/itineraries_batch1.json` — merged from the four part files
(`staging/batch1_part1.json` … `staging/batch1_part4.json`) plus five completed
re-extraction replacement files.

## Re-extraction replacements used (noncanonical evidence retained)
The following part-1 records were re-extracted because the originals were
unsupported or incomplete. The five replacement files are retained as noncanonical
evidence but are **not** canonical inputs themselves:
- `staging/batch1_new_karaandnate.json` — @karaandnate: 2 itineraries
  - 7-day Italy Vespa tour — https://karaandnate.com/italy-vespa-tour/
  - 11-day Trans-Siberian guide — https://karaandnate.com/the-ultimate-guide-to-riding-the-trans-siberian-railway/
- `staging/batch1_new_latinamericatravel.json` — @latinamericatravel: zero itineraries.
  Assessed as a brand/thematic aggregator with no attributable original itinerary content.
- `staging/batch1_new_lostleblanc.json` — @lostleblanc: 3 itineraries
  - 9-day Iceland — https://www.tiktok.com/@lostleblanc/video/7394475609621056775
  - Milos guide — https://www.youtube.com/watch?v=_qMcEMjLYhw
  - Bali summary via third-party source — https://www.nomadicnews.com/lost-leblanc/
- `staging/batch1_new_migrationology.json` — @migrationology: 3 high-confidence itineraries
  - 5-day Ghorepani Poon Hill trek — https://migrationology.com/ghorepani-poon-hill-trek-ultimate-guide/
  - 4-day Karakoram Highway trip — https://migrationology.com/journey-to-the-khunjerab-pass/
  - 1-day Luang Prabang itinerary — https://migrationology.com/things-to-do-luang-prabang/
- `staging/batch1_new_muradosmann.json` — @muradosmann: Taiwan medium-confidence
  recommendations + Egypt low-confidence group-trip fragments.

## Merge result
- Batch 1: **25/25 influencers processed, 14 yielded itineraries, 29 itineraries total.**
- Aggregate across all four canonical batches: **100 influencers, 95 itineraries.**
  - Batch 2: 25 processed, 33 itineraries
  - Batch 3: 25 processed, 7 itineraries
  - Batch 4: 25 processed, 26 itineraries

## Repairs applied during merge
- None structural: the merged batch-1 file was verified to carry all required schema
  fields per itinerary (title, destination, days, items with names, source_urls, confidence).
- Gate 1 rerun **2026-09-16** across all four canonical files: `PASS`, 0 errors,
  19 warnings (all warnings are the noncanonical checkpoint/re-extraction files being
  ignored by the gate — expected, informational only).

## Notes for evidence council
- The @lostleblanc Bali record is sourced from a third party (nomadicnews.com),
  not the creator — flagged as a high-risk sample candidate.
- The @muradosmann Egypt record is a low-confidence fragment — flagged for oversampling.
- All batch-1 itineraries are included in the ≥29 stratified council sample.
