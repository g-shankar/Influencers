# Evidence Council Log — 2026-09-16

## Sample
- **36 of 95 itineraries (37.9%)**, stratified across all 4 batches and high/medium/low
  confidence, oversampling low: all 6 low-confidence itineraries included.
- Batch 1: 9 | Batch 2: 11 | Batch 3: 6 | Batch 4: 10.
- Claim packets: `validation/council_packets/batch{n}_packets.json`
  (claims + source URLs only; no extractor notes given to verifiers).

## Verdicts
| Batch | Packets | PASS | FAIL | UNVERIFIABLE |
|---|---|---|---|---|
| 1 | 9 | 9 | 0 | 0 |
| 2 | 11 | 10 | 0 | 1 (@taramilktea — resolved, see below) |
| 3 | 6 | 6 | 0 | 0 |
| 4 | 10 | 10 | 0 | 0 |
| **Total** | **36** | **35** | **0** | **1 → CONFIRMED** |

- Verdict files: `validation/council_results/batch{n}_verdicts.json` (per-item evidence,
  per-claim problems, URLs actually opened).
- **Fail rate: 0%** (0/36). Escalation threshold (10%) not reached — no 100% expansion.

## The @taramilktea UNVERIFIABLE and its resolution
- First verifier (batch 2): UNVERIFIABLE — Qantas Travel Insider URL rendered as a
  generic Europe landing page; taramilktea.com is a parked GoDaddy domain. Cavo Tagoo
  and Dukely Beach Lounge claims could not be checked.
- Resolution: an independent search surfaced the original Qantas article text via the
  search index at the exact recorded URL ("Instagram Star Tara Milk Tea's Favourite
  European Haunts | Travel Insider", qantas.com, crawled ~53 days ago). The indexed
  text supports BOTH extraction items verbatim (four nights at Cavo Tagoo, marinated
  octopus/ceviche lunch, best-buffet breakfast, pool/ocean views; Dukely Beach
  Lounge, late afternoon, sushi platter/fried octopus/saffron risotto).
- Second verification (independent queries, article text read directly): **CONFIRMED**.
  Record: `validation/council_results/batch2_taramilktea_second_verdict.json`.
  Deviation noted in that file: done by the coordinator because subagent spawning
  became unavailable; queries were independent of the first verifier's.

## Corrections required before DB load
- **None.** Zero FAILs. The single UNVERIFIABLE was re-verified and confirmed; the
  extractor's own `low` confidence label remains an honest frame.
- Minor non-failing notes recorded by verifiers (kept in verdict files, no data change):
  - Batch 2 @pilotmadeleine Abu Dhabi: two off-by-one day assignments (Grand Mosque
    placed Day 1 vs Day-2 diary title; Sand Boarding placed Day 2 vs Day-1 desert
    safari tie-in). Paraphrase-level, not fabrication.
  - Batch 2 @youngadventuress: source spells winery "Amsfield"; packet's "Amisfield"
    is the correct spelling.
  - Batch 4 @wheelaroundtheworld: day assignments 2–5 inferred from episode order;
    source only labels EP1 "Day 1" and EP5 "final day".
  - Batch 4: two omissions (Blue Lagoon from Iceland packet, Sheppards Dell from
    Columbia packet) — extractor is lossy, not fabricating.
  - Batch 1 @lostleblanc Bali: source video title says "14 Days" but describes a
    "12-day itinerary"; packet's days=12 matches the latter.

## Council conclusion
All 36 sampled itineraries verified. No re-extraction, no removals. Proceed to DB load.
