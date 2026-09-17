# Stage 1 selection record — 100 → 200 creators (batches 5–8)

_Stage of work order `~/workspace/work-orders/travel-influencer-expansion.md`.
Compiled 2026-09-16. This document records what the pilot lacked: explicit,
pre-registered selection rules applied from a recorded selection date._

## Stage parameters
- New creators: 100 — batch 5 (TikTok), batch 6 (TikTok), batch 7 (Instagram), batch 8 (Instagram); 25 per batch.
- Platform quotas: 100 TikTok / 100 Instagram total after load (enforced by `load_db.py` via `stage.json`).
- Selection date: 2026-09-16. Selector: recorded per row in `selection_log.csv`.

## Defined criteria (SELECTION_CRITERIA.md Section 3, made concrete)
1. **Identity:** individual creator, not a brand / tour operator / agency / consultancy / curation-repost account. Handle must resolve to the named person at selection time. Method: open the profile URL, confirm the displayed name and bio match the claimed person.
2. **Content fit (yield lever — pre-screen required):** the creator has published at least one structured trip recommendation (itinerary, guide, or day-by-day plan) in the trailing 24 months (on/after 2024-09-16). Candidates found on listicles without visible itinerary content are screened out before inclusion.
3. **Reach floor:** ≥ 10,000 followers as cited or observed at selection (2026-09-16), AND an engagement signal: recent travel posts show visible public engagement (record the typical likes/views observed; `unknown` if not observable — never estimated).
4. **Purchase-intent signals:** recorded present/absent — affiliate links, "where I stayed / what I booked" content, hotel or tour tags.
5. **Activity:** account live and posting travel content within the trailing 90 days (on/after 2026-06-18).
6. **Balance quotas:** 50 TikTok / 50 Instagram for the stage; niche and geographic mix recorded as achieved, not pre-targeted beyond the discovery lanes below.
7. **Exclusions:** agencies, repost/curation accounts, dead or parked handles, handles that do not resolve, creators with no travel content in 24 months.

## Discovery lanes (collision avoidance across parallel batch workers)
- Batch 5 (TikTok): North America–based travel creators.
- Batch 6 (TikTok): Europe/UK–based travel creators.
- Batch 7 (Instagram): Asia-Pacific / Middle East / Africa–based travel creators.
- Batch 8 (Instagram): Latin America–based travel creators, plus worldwide budget/solo-niche creators.

Lanes are a discovery convenience, not a sampling claim. The achieved geographic/niche mix is reported from the data.

## Dedup
New handles are deduped case-insensitively against all 100 pilot handles (list in `staging/pilot_handles.txt`) at selection time, and across the four new batches at convergence. Any cross-batch collision is resolved by keeping the lower batch number; the higher batch re-picks before gates run.

## Selection log
`selection_log.csv` — one row per included creator: batch, handle, platform, name, niche, followers_approx, followers_observed (value as seen), followers_source (listicle URL or "profile page"), profile_url, discovery_source, identity_check (pass/fail), identity_method, content_fit (pass/fail), content_fit_evidence (URL or description), reach_floor (pass/fail), engagement_observed, activity_check (pass/fail), purchase_intent (present/absent/unknown), exclusions_check (pass/fail), decision (include), notes, check_date, selector. No log row, no inclusion.
