# Batch 13 close-out shortfall — 2026-09-17 (selector: batch13-closeout)

Batch 13 remains at **24/25** — no creator added, no padding. All four
remaining leads were re-checked today; two definitively fail the reach
floor on live observations, two fail the dated-observation requirement.

## REJECTED — below reach floor (live TikTok profile observations 2026-09-17)

- **@gabstraveljournal** — profile observed 2026-09-17:
  `https://www.tiktok.com/@gabstraveljournal` — **3,081 followers**,
  406,900 total likes, 137 videos. Individual (bio: "your average travel
  obsessed girlie", NYC based). Egypt 7-day itinerary video exists
  (7592047605551484191) but reach floor FAIL → **REJECT**.
- **@thisatravels** — profile observed 2026-09-17:
  `https://www.tiktok.com/@thisatravels` — **6,947 followers**,
  170,100 total likes, 241 videos. Individual ("Thisa Travels"; bio links
  GetYourGuide affiliate, purchase-intent present). Sri Lanka 7-day video
  (7597466346220174594) but reach floor FAIL → **REJECT**.

Both leads have strong content-fit but the 10K follower gate is hard.
Do not re-verify these handles unless their follower counts change.

## REJECTED — reach floor not verifiable (UNKNOWN RULE, no padding)

- **@explorewithmairy** — profile page fetch failed on 2026-09-17 (TikTok
  tool failure, retry banned this session). Evidence gathered from
  TikTok's own public pages via search:
  * "Colombia 10 day itinerary with best places to visit and things to do
    in Colombia" — photo post 7455375288315268385 (within trailing 24mo),
    **100.3K likes, 1,390 comments** (strong content-fit + engagement).
  * TikTok SEO snapshot: "@explorewithmairy 172.4k Followers, 5.5m Likes"
    — but the snapshot's last crawl is ~Apr 2026 (157 days stale), not a
    2026-09-17 observation. Identity: individual ("Mairy | Travel &
    Lifestyle"). Reach gate cannot be verified today → **REJECT**.
- **@wherejesstravels** — coordinator state claims reach >=10K was
  verified by a prior batch-13 worker on 2026-09-17, but no count was
  recorded and no TikTok follower number is retrievable today (no fresh
  profile observation; searches surface only her Instagram 166.7K and
  blog wherejesstravels.com). Content-fit is real (travel blogger Jess
  Inions; TikTok video 7603849360576744726 "Albania itinerary" Day 1-7),
  but TikTok-side reach is unverifiable → **REJECT**.

## Files untouched

No rows appended to `batch13.csv`, `staging/selection_log_batch13.csv`,
or `staging/itineraries_batch13.json` — no qualifying creator found.

## Note for coordinator

If a fresh TikTok profile fetch succeeds for @explorewithmairy (likely
~172K followers) or @wherejesstravels, either would be a clean close-out
pick with the content-fit evidence above. Both have strong itinerary
content; the only missing piece is a dated live follower observation.
