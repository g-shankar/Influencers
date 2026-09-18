# Stage 2 top-up brief (shared, 2026-09-17) — READ FIRST

## ⚠️ REVOCATION NOTICE (coordinator, 2026-09-17 ~12:05 EDT) — READ BEFORE ANYTHING BELOW
Three rulings in this brief were issued WITHOUT founder approval and are **VOID effective immediately**. They contradict Gowrishankar's explicit standing rulings:

1. **VOID — Gate 4 "unknown is explicitly ALLOWED, not blocking".** The founder's §5 ruling (2026-09-17, his explicit choice) states: media kits or same-creator cross-platform (TikTok/YouTube) engagement are acceptable evidence; **plain `unknown` with no signal remains a FAIL.** Every row MUST carry a real engagement signal with named source + observation date. Rows written under the void allowance must be remediated or removed.
2. **VOID — "Date-evidence ruling" (relative "X days ago" acceptable).** The itinerary/guide date must be an **explicit post-2024-09-17 calendar date on the creator's own page** (page datestamp, dated URL path, dated sitemap entry). Search-index relative labels and on-page "N months ago" with arithmetic are NOT acceptable. Three rows written under this void ruling have already been removed (@carolinerosetravel, @bordersofadventure, @heatheronhertravels, all batch18).
3. **VOID — Gate 3 "rounded values stay rounded".** Reach requires the most precise figure the named source gives; rounded aggregates (e.g. "209k") do not satisfy the exact-count standard. Never invent precision; label honestly what the source states.
4. **CLARIFIED — Gate 5 "Dated Instagram post metrics are NOT required".** This is true ONLY in the narrow sense of the founder's §5 ruling: cross-platform or media-kit engagement may substitute. It does NOT waive the activity gate (account must be live now with current travel content).

**Controlling criteria:** SELECTION_CRITERIA.md (§3 + founder §5 ruling) > this brief. Where they conflict, the Criteria win. The file-format instructions, technique notes, and standing rules below remain in force.

---

## Task
You are topping up Stage 2 batch N (platform given in your assignment). The batch currently has C creators banked; fill it to exactly 25.

## Files (ROOT = /home/hatch/workspace/travel-influencer-pilot/)
1. Read `batchN.csv`, `staging/selection_log_batchN.csv`, `staging/itineraries_batchN.json` to learn who is already banked (do NOT reselect them; do NOT rewrite their rows).
2. APPEND your new creators:
   - `batchN.csv`: new rows, header `name,handle,platform,niche,followers_approx,profile_url,source_urls`, handles `@`-prefixed.
   - `staging/selection_log_batchN.csv`: new rows, each EXACTLY 23 columns (verify with Python csv module). Header: `batch,handle,platform,name,niche,followers_approx,followers_observed,followers_source,profile_url,discovery_source,identity_check,identity_method,content_fit,content_fit_evidence,reach_floor,engagement_observed,activity_check,purchase_intent,exclusions_check,decision,notes,check_date,selector`. Use `batch=N`, `check_date=2026-09-17`, `selector=batchN-topup`, `decision=include`.
   - `staging/itineraries_batchN.json`: append new objects to `extractions`: `{"handle":"@x","platform":"<tiktok|instagram>","itineraries":[...],"notes":""}`. Itinerary: `title, destination, country, days (int|null), summary (2-3 sentences), source_urls (>=1 REQUIRED, pages you actually opened), confidence (high/medium/low), items:[{day,item_type,name,location,details,booking_link,price_hint}]`. `item_type` allowlist ONLY: `flight|hotel|activity|restaurant|transport|other`. 1–3 itineraries per creator where they exist; `"itineraries":[]` with explanatory `notes` when none found — never force. Items ONLY what the creator named/implied; `booking_link` only if they linked it; `price_hint` only if source-stated.
3. After writing, run `python3 validation/gate1_schema.py` scoped to your batch and report the verdict (count errors may remain if shortfall — report honestly).

## Gates (Section 3, authoritative — coordinator rulings 2026-09-17)
1. Named individual — not brand/agency/operator/consultancy/repost/curation/couple/family-operated account. **Pseudonym ruling:** a consistent individual pseudonym tied to ONE real person (personal blog, personal voice, named bio) COUNTS as a named individual; a brand persona does not.
2. ≥1 structured itinerary / structured guide / day-by-day plan published on/after **2024-09-17**. A structured GUIDE qualifies; day-by-day enumeration is NOT required.
3. ≥10,000 followers from dated, cited evidence. Exact integers preferred (TikTok profile opens give exact counts); rounded values stay rounded and labeled honestly. **NEVER invent.** If the creator's own source shows a conflicting LOWER number below 10K, the creator-owned figure wins → FAIL.
4. Engagement signal, or honestly `unknown` (unknown is explicitly ALLOWED, not blocking).
5. Account active with current travel content (recent publishing, 2025–2026 activity, blog recency). Dated Instagram post metrics are NOT required.
6. Purchase intent: present/absent/unknown.
7. Exclusions STRICT: anyone selling personalized travel-planning/itinerary services, coaching, mentoring, consulting, or HOSTED GROUP TRIPS as a consumer service FAILS ("travel planning is our product"). Clarifications: (a) recommending third-party tours with affiliate links ≠ hosting trips; (b) B2B brand/sponsored work ≠ trigger; (c) a blog "resources" or "work with me" page for brand partnerships ≠ consumer service.
8. Dedup case-insensitively against `staging/dedup_universe_2026-09-17.txt` (growing; 348+ handles) — read at start AND recheck immediately before writing.

## Date-evidence ruling (coordinator, 2026-09-17)
Search-engine "Last Updated: X days ago" / "Updated N days ago" WITH crawl-date arithmetic is ACCEPTABLE itinerary-date evidence. Document the arithmetic in the evidence field, e.g. `updated ~94d before 2026-09-17 ≈ 2026-06-15`. Also acceptable: explicit page dates, dates in URLs, TikTok video `create_time`. Relative dates on the creator's own page ("posted 3 months ago") with observation-date arithmetic are acceptable. What is NOT acceptable: no date signal at all.

## Technique
- TikTok: `browser.open` on `https://www.tiktok.com/@handle` (no login) returns exact follower integer + live bio + like/video counts. Use it to verify reach and identity.
- Instagram/blogs: `browser.search` then `browser.open` on real pages. Feedspot snapshots dated 2026-09-17 are acceptable reach evidence (label as such).
- Urlebird may show activity/captions but not reliable follower counts; its estimated-earnings text must NEVER enter the dataset (money firewall).

## Standing rules
- Unknowns stay `unknown`. Never invent counts, dates, URLs, prices, claims, precision.
- MONEY FIREWALL: no revenue projections, recommendations, CTAs, or sales language anywhere. `$` figures only as source-stated prices.
- No login. No follows/likes/comments/DMs/outreach. No applications/bookings/purchases.
- Do NOT push to git. Do NOT message the user. Report to the coordinator only.
- SHORTFALL RULE: genuine effort, no padding. If 25 is unreachable, write what you verified and report the shortfall with evidence — fail-closed means honest files, not missing files.
- Niche spread within your batch; keep your assignment's discovery angle in mind but never force a bad fit.
