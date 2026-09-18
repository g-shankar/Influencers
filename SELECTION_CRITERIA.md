# Creator Selection Criteria — travel influencer pilot

_Compiled 2026-09-16 as a research-strengthening deliverable. This document separates
what is established from what was never recorded. Anything in the "NOT recorded"
section is **unknown** — it is not reconstructed or invented retroactively._

## 1. What IS established (with evidence)

- **Pilot scope:** 100 creators, 50 TikTok / 50 Instagram, authorized 2026-09-15.
  The 50/50 split is enforced mechanically by `load_db.py` (refuses to load unless
  the platform counts are exactly {instagram: 50, tiktok: 50}).
- **Compile date:** `influencers.csv` was compiled 2026-09-15.
- **Creator list source material:** every row of `influencers.csv` carries one or
  more `source_urls` pointing to published third-party "top travel influencer /
  travel accounts to follow" listicles. The list was assembled from these listicles;
  row counts per listicle (some rows cite more than one):
  | Listicle | Rows citing it | Source publication date |
  |---|---|---|
  | superprofile.bio — top Instagram travel influencers | 39 | not recorded / unknown |
  | diarydirectory.com — top travel TikTok influencers to follow (2025) | 18 | not recorded / unknown |
  | travelpayouts.com — best travel accounts to follow on Instagram | 13 | not recorded / unknown |
  | afar.com — TikTok accounts giving travel advice | 8 | not recorded / unknown |
  | izea.com — TikTok travel influencers | 7 | not recorded / unknown |
  | highsocial.com — travel influencer feed | 5 | not recorded / unknown |
  | ef.nl — TikTok travel inspiration | 5 | not recorded / unknown |
  | elitedaily.com — budget travel after college | 5 | not recorded / unknown |
  | izea.com — Gen-Z travel influencers | 4 | not recorded / unknown |
  | tatlerasia.com — best travel Instagram accounts (HK) | 2 | not recorded / unknown |
  | izea.com — van-life influencers | 2 | not recorded / unknown |
  | mn2s.com — Nomadic Matt talent roster | 1 | not recorded / unknown |
  | johnnyjet.com — travel style: Nomadic Matt | 1 | not recorded / unknown |
  | elonedge.com — travel TikTokers to follow | 1 | not recorded / unknown |
- **Publication-date note:** `influencers.csv` records source listicle URLs but no
  publication dates for any of them; one title contains "(2025)" in its own text,
  which is the only date hint present in the records. No other source date is
  known or claimed.
- **Per-row fields recorded:** name, handle, platform, niche label, followers_approx
  (source-reported; 27 of 100 are `unknown`), profile URL, source listicle URLs.
- **Selection screening was incomplete at compile time:** 8 of 100 handles were
  later quarantined because extraction exposed identity problems (brand/tour-operator
  account, consultancy, non-travel account, possible source-list typos, operator
  content misattributed to a creator). See `validation/quarantine.json`.
  This means selection included no reliable identity check.

## 2. What was NOT recorded (unknown — never invented retroactively)

The records contain no documented answers to any of the following. Each is
**unknown**, not reconstructed:

- **Eligibility rules:** no explicit inclusion criteria were recorded — no follower
  floor, no engagement floor, no content-type requirement, no recency-of-posting
  requirement, no audience-quality or purchase-intent screen.
- **Exclusions:** no explicit exclusion criteria were recorded — nothing in the
  records states that brands, agencies, repost accounts, dead accounts, or
  non-resolving handles were excluded. (The 8 later quarantines show they were
  not excluded in practice.)
- How listicle overlap was handled (creators appearing on multiple lists).
- Who made the final picks and what judgment was applied beyond the listicles.
- Any identity verification at selection time.
- Any niche-balance, geography-balance, or reach-distribution rationale.
- Whether niche labels in the CSV came from the listicles or were assigned by
  the compiler.

Honest consequence: the pilot sample is best described as **"100 travel creators
drawn from published 'top travel influencer' listicles of unrecorded dates
(one title mentions 2025; the rest are unknown), quota-balanced
50/50 across TikTok and Instagram."** It is not a representative sample of travel
creators, not a "top 100" leaderboard (follower counts are source-reported, not
live-verified), and not screened for itinerary-publishing behavior — in fact only 52 of 100 yielded any
usable itinerary at original extraction; after the 2026-09-16 documented
re-search (two missed itineraries added: @jessicanabongo, @courtandnate) and the
exclusion of one unverifiable itinerary (@thenationalparktravelers, id 88), the
final dataset holds 94 itineraries from 53 of the 100 creators — which itself is
a finding: listicle fame does not predict itinerary content.

## 3. Selection criteria for scaling to 1,000 (forward-looking)

To be applied from a recorded selection date, with one log row per creator:

1. **Identity:** individual creator, not a brand / tour operator / agency /
   consultancy / curation-repost account. Handle must resolve to the named person
   at selection time.
2. **Content fit:** has published at least one structured trip recommendation
   (itinerary, guide, or day-by-day plan) in the trailing 24 months. Pilot final
   yield: 53 of 100 creators (52% at original extraction, before the re-search
   additions and one exclusion) — pre-screening on this criterion is the single
   biggest lever on extraction yield.
3. **Reach:** defined minimum follower floor AND an engagement signal (e.g. median
   views/likes on recent travel posts), both recorded from a dated observation.
4. **Purchase-intent signals:** presence of booking-adjacent behavior — affiliate
   links, "where I stayed / what I booked" content, hotel or tour tags — recorded
   as present/absent, not assumed.
5. **Activity:** account live and posting travel content at the selection date.
6. **Balance quotas (defined before selection):** platform split, niche mix,
   and geographic mix — recorded as targets, with the achieved mix reported.
7. **Exclusions:** agencies, repost/curation accounts, dead or parked domains,
   handles that do not resolve, creators with no travel content in 24 months.
8. **Selection log:** for every creator — criterion checklist result, identity
   check result and method, check date, and selector. No log row, no inclusion.

## 4. Residual note

Follower counts in this pilot remain source-reported (27 unknown) and were not
live-verified. Any ranking by followers is a ranking of *reported* reach, and is
labeled as such wherever presented.

## 5. Founder ruling — engagement evidence standard for Instagram (2026-09-17)

After the Stage 2 wave-2/3 workers documented that Instagram's login wall makes
exact-dated on-platform engagement metrics unreachable without login, the founder
ruled: **creator-published media kits and cross-platform engagement (TikTok /
YouTube metrics for the same creator) are acceptable as the engagement signal**
for the reach criterion.

Conditions (unchanged): the signal must come from a named source with an
observation date, recorded honestly in the selection log (method + date). Plain
`unknown` with no signal remains a fail. This ruling applies from 2026-09-17
forward and is recorded here so it is never mistaken for a quiet relaxation.

## 6. Coordinator adjudications — identity and activity gates (2026-09-17)

Recorded so later workers apply the criteria consistently. These are applications
of the existing text, not relaxations.

1. **Mononym / one-person pseudonym satisfies the named-individual gate** when the
   name is the consistent public operator identity on the creator's own site and
   handle (precedent: `@elise.abroad` "Elise", passed batch17 gates; applied to
   `@sinahsstories` "Sinah", batch20). What fails is an anonymous/brand/shared
   account with no attributable individual, not the absence of a legal surname.
2. **The activity gate is account-level.** "Account live and posting travel content
   at the selection date" refers to the platform account under selection (the
   Instagram account for Instagram batches). A stale personal blog does not fail
   an Instagram creator whose IG account shows current posting/engagement via a
   named dated source (applied to `@gracefkim`, batch20: Gondola engagement
   observed 2026-09-17 satisfies activity despite blog RSS newest post 2025-06-25).

## 6. Founder authorization — Instagram login for engagement verification (2026-09-17)

The founder authorized using his connected Instagram session to verify
engagement evidence (exact-dated posts with like/comment counts) for creator
research, after non-login routes were documented as exhausted.

Binding constraint (founder's words): **don't follow anyone.** The session is
strictly read-only for research: profile lookups, post reads, like/comment
counts. No follows, likes, comments, DMs, saves, or any other write action —
no exceptions.

Research account for login-based verification (founder's choice, 2026-09-17):
@sgshankar84. Read-only use confirmed working.

## 7. Parent adjudications — TikTok close-out (2026-09-17)

- **@ferinajo (batch9): REMOVED.** Paid WeTravel group trips = operating as a tour
  operator selling hosted consumer trips. Exclusion trigger, consistent with the
  @kat.triplanner precedent (1:1 custom planning = exclusion). Purchase-intent
  signals cover affiliate/booking-adjacent behavior, not operating consumer trips.
- **@axelletaniegi_travel (batch9): KEPT.** A 100-page solo-travel guide is a
  "guide" under §3 content fit ("itinerary, guide, or day-by-day plan");
  destination honestly recorded as unknown.
- **@adamrikys (batch11): PROVISIONAL PASS** with adjudication note in the log —
  individual creator; sponsored content for an operator does not make him one.
- **@sydneyguide (batch11): REJECTED** (fail-closed) — brand-like handle + "we"
  language; individual operation not proven.
