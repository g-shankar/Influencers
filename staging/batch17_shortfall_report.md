# Stage 2 Batch 17 — Evidenced Shortfall Report
**Date:** 2026-09-17  
**Worker:** batch17-worker (subagent)  
**Status:** SHORTFALL — 25 fully-gated creators could not be established. No batch files written (per "do not pad" rule).

## Summary
After extensive public research on 2026-09-17, **zero creators** fully pass all gates with watertight evidence. One candidate (@indianahannah_blog) is close but has an unresolved identity-branding question. Five others are partial with specific blockers. The remaining discovery pool is exhausted or blocked.

**Do not write** `batch17.csv`, `staging/selection_log_batch17.csv`, or `staging/itineraries_batch17.json` — none would meet the 25-creator requirement.

## Candidate-by-Candidate Evidence

### CLOSEST: @indianahannah_blog (Indiana Hannah)
- **Identity:** Hannah, individual Indiana travel/lifestyle blogger. Her site says "Hey I’m Hannah!" (Muck Rack) and "follow me @indianahannah_blog (Indiana Hannah)". Her Lemon8 bio states: "With my two best friends as my sidekicks, my husband and toddler, we spend our free time exploring Indiana and beyond." The husband/toddler are travel companions ("sidekicks"), not account operators. The blog is written in singular first-person ("hand-picked by me"). **Verdict:** Individual operator, but "Indiana Hannah" appears to be a brand/pseudonym, not a full legal name. The gate requires "Named individual" — this is borderline.
- **Reach:** 24.6K (Feedspot, observed 2026-09-17 per prior research). ≥10K. **Verdict:** PASS (if Feedspot date is accepted).
- **Itinerary:** "50 of Coolest Summer Things to Do in Indiana" — structured guide with 50+ destinations, interactive map. URL contains explicit date: `https://indianahannahblog.com/2026/06/22/the-coolest-summer-things-to-do-in-indiana/` (2026-06-22, after 2024-09-17). **Verdict:** PASS (date-in-URL is explicit; day-by-day not required).
- **Activity:** "60+ of the Best Fall Things to Do in Indiana" — `https://indianahannahblog.com/2026/09/02/50-of-the-best-places-to-visit-in-indiana-during-the-fall/` (2026-09-02, 14 days ago per search). Very recent. **Verdict:** PASS.
- **Exclusions:** Work With Me page offers "Destination Visit" (B2B: she visits a destination for a tourism-board client) and "Product Promotion" (B2B). No consumer trip planning, no hosted consumer trips, no coaching. **Verdict:** PASS (B2B only, allowed).
- **Dedup:** Handle-clear (not in 348-line universe, not in batch 20).
- **Blocker:** "Indiana Hannah" may be a pseudonym/brand, not a full named individual. If the gate requires a full legal name, this FAILS. If a consistent individual pseudonym is acceptable, this PASSES.

### PARTIAL: @heatheronhertravels (Heather Cowper)
- **Identity:** Heather Cowper, individual UK travel blogger. **Verdict:** PASS.
- **Reach:** 16.1K (Feedspot). **Verdict:** PASS.
- **Itinerary:** "Things to do in Piraeus" — `https://www.heatheronhertravels.com/things-to-do-in-piraeus/` — structured one-day itinerary. **Blocker:** No exact visible publication/update date found on page. Search shows relative dates only.
- **Exclusions:** B2B work/policies appear allowable, but not fully confirmed she doesn't offer consumer planning.
- **Verdict:** BLOCKED on exact itinerary date.

### PARTIAL: @bordersofadventure (Becki Enright)
- **Identity:** Becki Enright, individual. **Verdict:** PASS.
- **Reach:** 14.1K (Feedspot). **Verdict:** PASS.
- **Itinerary:** "Travel to Mongolia guide" — `https://www.bordersofadventure.com/travel-to-mongolia-guide/` — rich three-week/day-by-day itinerary. **Blocker:** Only relative "Last Updated: 69 days ago" found; no exact visible date. Hosted-trip exclusion not fully closed.
- **Verdict:** BLOCKED on exact itinerary date + exclusion.

### PARTIAL: @myadventuresacrosstheworld (Claudia Tavani)
- **Identity:** Claudia Tavani, individual. **Verdict:** PASS (presumed; About page not fully inspected).
- **Reach:** 37.8K (Feedspot). **Verdict:** PASS.
- **Itinerary:** Multiple structured itineraries found:
  - "The Best 4 Days Istanbul Itinerary" — `https://myadventuresacrosstheworld.com/4-days-istanbul-itinerary/` (search: "Last Updated: 47 days ago")
  - "4 Days In New York" — `https://myadventuresacrosstheworld.com/4-days-in-new-york-itinerary/` ("279 days ago")
  - "4 Days In Rome" — `https://myadventuresacrosstheworld.com/4-days-in-rome-itinerary/` ("178 days ago")
  **Blocker:** Page text extraction shows NO exact visible date (searched for "2026", "2024", "Last updated" — none found). Search-engine relative dates are insufficient.
- **Verdict:** BLOCKED on exact itinerary date.

### PARTIAL: @globetrottergirls (Dani Heinrich)
- **Identity:** Dani Heinrich. Blog founded by Dani + former partner Jessica (2010); Dani solo since 2014 per public background. **Blocker:** Couple-origin is a flag under "Reject couples, duos". Current solo operation of the IG account not definitively proven. Old posts still reference "Dani and Jess" / "my girlfriend".
- **Reach:** 17.8K (Feedspot, per prior research).
- **Itinerary:** Old content found (Patagonia route updated 2025-02-11; Iceland 7-day). **Blocker:** No recent (2024-09-17+) structured itinerary with exact date confirmed. Content appears stale.
- **Verdict:** BLOCKED on couple-origin flag + stale itinerary.

### PARTIAL: @girlswanderlust (Daphne)
- **Identity:** Daphne, individual (runs solo since Aug 2022 per video source). **Verdict:** PASS (presumed).
- **Itinerary:** "3 Days in Jakarta" — `https://girlswanderlust.com/3-days-in-jakarta-itinerary/` — structured. **Blocker:** No exact visible date found; no valid ≥10K reach evidence; service/hosted-trip exclusions not closed.
- **Verdict:** BLOCKED on reach + date + exclusions.

### PARTIAL: @carolinerosetravel (Caroline Rose)
- **Identity:** Caroline Rose, solo female traveler (blog: "by a Solo Female Traveler"). **Verdict:** PASS (individual).
- **Reach:** 18K (Feedspot, crawled ~2026-09-16). **Verdict:** PASS.
- **Itinerary:** "Peru's Huayhuash Trek: Ultimate Guide" — `https://carolinerosetravel.com/hiking-the-cordillera-huayhuash-trek-everything-you-need-to-know-by-a-solo-female-traveler/` — detailed 8-day day-by-day trek itinerary (Day 1–Day 8 with stats). **Blocker:** No exact visible date on page (searched for "2024" — none found). Images from 2022. Search says "Last Updated: 667 days ago" (~Nov 2024) but not visible on page.
- **Verdict:** BLOCKED on exact itinerary date.

## Confirmed Rejects (with reasons)

| Handle | Reason |
|--------|--------|
| @bucketlistly / @peachananr | Pete Rojwongsuriya already selected in batch 16 as @bucketlistly. Alternate handle would duplicate creator. |
| @annasherchand | In 348-line dedup universe (line 27). Also inspected itineraries lack exact dates. |
| @vickyflipflop | In dedup universe; also in batch 20. |
| @kirstenalana, @findingalexx, @dangerousbiz, @em_luxton | In batch 20 (dedup). |
| @fivelittledoves, @tigerlillyquinn | Confirmed family-operated. |
| @theworldtravelguy, @thebackpackingmom | Likely couple/family. |
| @solotravelinstyle, @kirstyleannetravels | Hosted trips/services. |
| @mylifesatravelmovie (Alyssa Ramos) | Runs group trips via @MyLifesATravelTRIBE — hosted consumer trips (disqualifying). |
| @sologirlstravelguide (Alexa West) | Guidebooks are paid products, not freely-accessible structured itineraries; "TRIPS" in bio suggests hosted trips; no qualifying blog itinerary with date found. |
| @aprylwanders | TikTok-based; no structured blog itinerary found. |
| @jetsetsarah (Sarah Greaves-Gabbadon) | Journalist; no structured itinerary with date found. |
| @dawn.traveler | Unresolved identity linkage (Isha Wakankar ≠ proven link to @dawn.traveler). |
| @meanderandwander (Rachita Saxena) | Egypt page is a planning guide, not structured itinerary; no exact date; possible hosted trip via Wander XO (unproven but flagged). |
| @bonnierakhit (Bonnie Rakhit) | Paris itinerary is structured but images from Aug 2022; no exact date ≥2024-09-17. |
| @jesslitras | Unresolved linkage. |
| @exponentialtravels (9.5K), @solopassport (9.1K), @globegazers (9.1K) | Below 10K reach floor. |
| @solotravelingsonia, @krystenkaladkarin, @shweta.wanders | No qualifying itinerary found. |

## Systemic Blockers (why 25 is not achievable)

1. **Exact-date bottleneck:** The gate requires itineraries "published or explicitly updated on/after 2024-09-17" with an exact visible date. Most WordPress travel blogs do NOT display exact dates in extractable page text. Search engines provide relative dates ("X days ago") which do not satisfy "explicitly". Only two reliable patterns found:
   - Dates embedded in URLs (e.g., indianahannahblog.com/2026/06/22/...) — rare.
   - Medium articles (show exact dates) — but identity linkage to IG often fails.
   This single gate eliminated 5 of 7 partial candidates.

2. **Dedup saturation:** The 348-line universe + batch 20 + prior batches block many obvious candidates (@vickyflipflop, @annasherchand, @kirstenalana, etc.).

3. **Exclusion strictness:** Hosted group trips (Alyssa Ramos), couple-origins (GlobetrotterGirls), and family-operation flags eliminate otherwise-strong candidates.

4. **Discovery exhaustion:** Feedspot lists were mined; remaining handles either lack itineraries, lack dates, or fail exclusions. The 11 "dedup-clear partials" from prior research (@brokegirltravelguide, @carolinerosetravel, @marissamcgarr, @tashamalik, @adventara, @whereis_brittany, @woman_who_wanderz, @thekatielynn, @laurabaella, @jetsetsarah, @thisisorsi) were triaged; @carolinerosetravel was the strongest but blocked on date; others lacked qualifying itineraries or had exclusion issues.

## Files Written
- This report: `staging/batch17_shortfall_report.md`
- No batch CSV, selection log, or itinerary JSON written (per "do not pad" rule).

## Recommendation
Batch 17 cannot reach 25 with public evidence meeting the watertight bar. Options:
1. **Accept shortfall:** Document the 1 close candidate (@indianahannah_blog) if the pseudonym is acceptable, or 0 if not.
2. **Relax the date gate:** Accept search-engine "Last Updated: X days ago" with crawl-date arithmetic (would unlock @myadventuresacrosstheworld, @bordersofadventure, @carolinerosetravel, @heatheronhertravels — potentially 4-5 creators).
3. **Expand discovery:** Fresh Feedspot mining beyond the lists already checked, or different niches.

The date-gate relaxation (option 2) is the highest-leverage change; it would likely yield 4-6 verifiable creators, though still short of 25.
