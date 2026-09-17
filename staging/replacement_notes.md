# Stage 1 replacement notes — batch 9 (2026-09-16/17)

## What this batch does
Replaces **7 excluded creators** from the Stage 1 200-creator dataset, preserving the
100 TikTok / 100 Instagram platform split: **6 TikTok + 1 Instagram** replacements.

## Excluded handles (slots to fill)
| # | Handle | Platform | Reason (per coordinator/verification findings) |
|---|--------|----------|-----------------------------------------------|
| 1 | @travelingwithtals | tiktok | no qualifying itinerary evidence |
| 2 | @nytoanywhere | tiktok | no qualifying itinerary evidence |
| 3 | @polkadotpassport | tiktok | no qualifying itinerary evidence |
| 4 | @goingwithnicole | tiktok | no qualifying itinerary evidence |
| 5 | @chloe__trips | tiktok | no qualifying itinerary evidence |
| 6 | @boyeatsworld | instagram | no qualifying itinerary evidence |
| 7 | @chubbydiaries | tiktok | claimed Sonoma 72-hour food guide has no capturable creator-attributable URL (parallel verification agent finding, 2026-09-16) |

All 7 handles are present in `staging/dedup_handles_batch9.txt` (confirmed for
@chubbydiaries by coordinator grep, 2026-09-17).

## Replacement rows (in `staging/selection_batch9_replacements.csv` + `staging/itineraries_batch9_replacements.json`)
| # | Replacement | Platform | Followers (exact, observed) | Itinerary | Verdict |
|---|-------------|----------|-----------------------------|-----------|---------|
| 1 | @heleneinbetween (Helene Sula) | tiktok | 375,900 (TikTok profile JSON, 2026-09-16) | 10-day Cotswold Way | include |
| 2 | @travelwithveronicca (Veronika, first-name-only) | tiktok | 86,600 (TikTok profile JSON, 2026-09-16) | 3-day Prague | include (caveats below) |
| 3 | @gopharitravels (Farirai Sanyika) | tiktok | 227,300 (TikTok profile page, 2026-09-16) | 10-day Garden Route | include |
| 4 | @travelwithkna (Audy, first-name-only) | tiktok | 31,800 (TikTok profile page, 2026-09-16) | 2-day Niagara Falls | include (caveat below) |
| 5 | @evapzc (Eva, first-name-only) | tiktok | 47,400 (TikTok profile HTML, 2026-09-17) | 18-day West Coast USA | include (caveats below) |
| 6 | @trip.on.the.road (Eleonora, first-name-only) | tiktok | 12,000 (TikTok profile HTML, 2026-09-17) | 5-day Lake Constance | include (caveats below) |
| 7 | @psimonmyway (Trisha Velarmino) | instagram | ~62.8K (Feedspot 2026; exact not directly observed) | 7-day Tokyo | **conditional — activity gate BLOCKED** |

**Excluded→replacement mapping is the coordinator's call.** The natural platform-preserving
assignment is @psimonmyway → @boyeatsworld (IG→IG); the 6 TikTok replacements map 1:1 to
the 6 excluded TikTok slots.

## Caveats the verifier must see
1. **@travelwithveronicca** — identity is first-name-only ("Veronika"); surname unconfirmed.
   Guide date signals (video-ID decode 2026-04-28 + embedded `createTime` 1777404478) derive
   from the same underlying timestamp — they agree but are not fully independent.
2. **@travelwithkna** — identity rests on her own site + TikTok bio (no third-party press);
   proportionate for a 31.8K creator, flagged for the verifier.
3. **@evapzc** — caption provides the 18-day duration and ordered 9-stop route; the per-day
   breakdown is in the video (TikTok CDN blocked direct download for OCR) and was not invented.
4. **@trip.on.the.road** — video discloses "In collaborazione con @bodensee.eu" (tourism board
   partnership, not an operator account).
5. **@psimonmyway** — BLOCKING: no directly verified Instagram travel post on/after 2026-06-18.
   Bio maintenance and follower growth are circumstantial and do not satisfy the 90-day
   activity gate. A backup Instagram research worker is running; if it qualifies a candidate
   with direct post-cutoff IG activity, swap this row. Do NOT mark this row PASS until the
   activity gap is closed or the backup replaces it.
6. **@gopharitravels** — Day 5 of the 10-day series has no published video; left unknown, not invented.

## Backup Instagram candidate (needs live browser to qualify)
- **@sarahdegheselle** (Sarah De Gheselle, Belgian travel photographer/blogger) — investigated by
  backup worker, verdict BLOCKED on two gates, honest research package at
  `staging/itineraries_replacements_ig_2026-09-16.json`. Gates cleared: named individual
  (WP user record, visit.gent.be, bartsboekje interview, Feedspot), structured guide
  ("15 epic things to do in Dalat, Vietnam" — WP API + JSON-LD datePublished 2026-03-10),
  dedup-clean, purchase intent present. Blockers: exact follower integer unknown (only
  87.1K Heepsy / 81.8K Feedspot / 82.5K Socialveins — all abbreviated) and no directly dated
  IG post ≥2026-06-18 (Heepsy "recency 3.45 days" at ~2026-09-15 crawl is not a direct post).
  Instagram profile pages are login-walled for anonymous fetch (coordinator confirmed
  2026-09-17: no follower data in fetched HTML). **Live-browser step needed for both
  @sarahdegheselle and @psimonmyway: read the exact follower integer from the profile
  header and the latest post date from the post grid.** If either clears (exact ≥10,000 +
  travel post ≥2026-06-18), it takes the IG slot; if both clear, prefer the stronger
  overall evidence.

## Vetted spare (not in batch 9 files)
- **@sunkissedblonde.travels** (Laura, first-name-only) — TikTok, 19,400 exact (profile
  `authorStats`, 2026-09-16). One-day Split guide video 7606473972049349910 (2026-02-13);
  activity within window (Urlebird post ~4h before 2026-09-16 check). Cut from the final six
  only because @travelwithveronicca outscored it on reach (86.6K vs 19.4K) and itinerary depth
  (3-day vs 1-day). Same date-signal caveat as @travelwithveronicca. First alternate if any
  batch-9 TikTok row fails Gate 4 review.

## Rejected during this round (do not re-propose)
- TikTok: @sinahsstories (7,467 followers), @comejoinmyjourney (2,504), @hungrypursuit
  (couple: Mel & Andy), @comfortculturetravel (5,065), @vivomunditraveldiaries (5,762),
  @arshielife (only itinerary video 2023-09-02, too old), @jevanajourneys (6,158),
  @desolaalafia (8,086), @seenbyamy (8,712); worker 1/3 round: mishel_travel (inactive),
  sarah.rh.bashir, vani.vieira, vanniabenavides_, itsmelissablanche, campsbaygirl,
  ceylantravel (couple), edward.wonder, gabstraveljournal (3,078), beths_backpacking
  (4,345), daniel.bun_ (2,508); worker 4 round: 12 more (see
  `itineraries_replacements3_2026-09-16.json`), incl. aureliestoryy (2.4M, no structured
  itinerary — held as backup).
- Instagram: none rejected this round (only @psimonmyway qualified; backup worker running).

## Evidence files
- `staging/selection_batch9_replacements.csv` — 7 selection-log rows
- `staging/itineraries_batch9_replacements.json` — 7 extractions, 132 itinerary items
- Worker source files: `itineraries_replacements_2026-09-16.json` (heleneinbetween),
  `itineraries_replacements_tiktok_2026-09-16.json` + `selection_replacements_tiktok_2026-09-16.csv`
  (gopharitravels, travelwithkna), `itineraries_replacements3_2026-09-16.json` (evapzc,
  trip.on.the.road); @travelwithveronicca + @psimonmyway from worker-3 handoff
  (no worker JSON written — extraction captured directly into batch-9 files by coordinator).
