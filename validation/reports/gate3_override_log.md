# Gate 3 — Override & Resolution Log (2026-09-16)

## Result
- Rerun **2026-09-16**: `GATE 3 [PASS]` — 95 itineraries, 105 unique URLs, 90 script-reachable, **0 errors**.
- 15 itineraries resolved via **manual browser-fetch overrides** (auditable evidence:
  `validation/reports/gate3_override_evidence.json`, keyed per batch/handle/title with
  per-URL method, check date, and content-match summary).

## What happened
The automated gate 3 script uses urllib with a bot User-Agent. Several sites return
404/403/503 or time out **to the script only**, while loading fully in a real browser
fetch. All 12 script-flagged itineraries (plus the @mgtenazas TikTok) were re-checked
by opening each URL in a full browser fetch and reading the page content. In every
case the page loaded and its content matched the extraction record — these were
**script false negatives, not dead sources**.

## Script failure modes observed
- `pilotmadeleine.de` (all 4 URLs): returns 404 to urllib, serves full content to browser.
- `wildweroam.com` (all 3 URLs): returns 404 to urllib, serves full content to browser.
- `lemon8-app.com`: returns 404 to urllib, serves full content to browser.
- `themomtrotter.com` (2 URLs): returns 503 to urllib, serves full content to browser.
- `girlvsglobe.com` (2 URLs): unreachable to urllib, serves full content to browser.
- `farfetch.com`, `sorelleamore.com`, `travelandleisureasia.com`: unreachable to urllib, full content in browser.
- `izea.com/resources/tiktok-travel-influencers/` (secondary source, @mgtenazas): 403 to scripts — bot-block; **not needed** since the primary TikTok source is live.

## Per-URL verification summary (evidence in gate3_override_evidence.json)
| Batch | Handle | Itinerary | Verified URL(s) live | Content match |
|---|---|---|---|---|
| 1 | @girlvsglobe | Things To Do in Segovia in 48 Hours | girlvsglobe.com Segovia page | Explicit Day 1/Day 2 itinerary |
| 1 | @girlvsglobe | 11 Things To Do In Menorca | girlvsglobe.com Menorca page | Recommendation list |
| 1 | @muradosmann | Taiwan travel recommendations | farfetch.com Taiwan feature | Nataly & Murad Taiwan guide |
| 1 | @muradosmann | Egypt group trip via #FollowMeToTour | travelandleisureasia.com interview | Mentions #Followmetotour travel club + Egypt group trip (private pyramid/Sphinx access) |
| 2 | @pilotmadeleine | Abu Dhabi Travel Diary - 3 Days | pilotmadeleine.de Abu Dhabi tips + travel archive p18 | Top-10 tips (Grand Mosque, desert safari, Ferrari World, Yas Mall) |
| 2 | @pilotmadeleine | New Zealand: Nelson & Abel Tasman | pilotmadeleine.de NZ post | Boat Shed, WearableArt, Marahau Lodge, Aqua Packers, Abel Tasman Kayaks |
| 2 | @pilotmadeleine | Hawaii Travel Diary: Oahu Days 1 & 2 | pilotmadeleine.de Hawaii post | Day 1 Waikiki/Duke's, Day 2 Kualoa/Chinaman's Hat/Lanikai |
| 2 | @sorelleamore | Mysterious Mongolia | sorelleamore.com blog post | Named trip highlights |
| 2 | @wildweroam | Cinque Terre Day Plan | wildweroam.com Cinque Terre journal | Levanto base, Camping Acqua Dolce, hikes, ferries |
| 2 | @wildweroam | Two Weeks in Portugal | wildweroam.com Portugal + Berlengas posts | Ilha de Armona, Olhao ferry, Berlengas camping guide |
| 4 | @sightsofsara | Tour du Mont Blanc - Day-by-Day | 2 TikTok videos (Day 1 + Day 2) | Day 1: Les Houches→Les Contamines; Day 2: →Refuge de la Croix du Bonhomme |
| 4 | @sightsofsara | Epic Iceland Road Trip Guide | lemon8-app.com Iceland post | Camper van, Seljalandsfoss, Jokulsarlon, Blue Lagoon |
| 4 | @themomtrotter | Utah National Parks + Southwest RV | themomtrotter.com Utah post | Detailed 10-day day-by-day itinerary |
| 4 | @themomtrotter | St. Croix Family Itinerary | themomtrotter.com St. Croix post | Hotel/activity recommendations |
| 4 | @mgtenazas | Maldives on a Budget | TikTok video (177.9K plays) | Guesthouses, <$150/day, snorkeling/diving incl. Keyodhoo shipwreck |

## Process note
Overrides are keyed per (batch, handle, title) and only applied when the itinerary has
zero script-reachable sources AND the override URLs are a subset of its recorded
source_urls. All 15 entries are recorded under `overridden_script_false_negatives` in
`gate3_report.json` — they are waivers-with-evidence, not silent passes.
