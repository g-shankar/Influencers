# Guide-date independent verification — summary

**Date:** 2026-09-16
**Scope:** 36 unresolved rows from `validation/reports/tiktok_two_signal_audit_batch5_6_2026-09-16.json`
(9 previously VERIFIED_TWO_SIGNAL rows and 6 replacement candidates excluded, left untouched).
**Output copy:** `validation/reports/tiktok_two_signal_audit_batch5_6_2026-09-16_verified.json` (original audit NOT modified).

## Final tally (36 rows in scope)

- **VERIFIED_TWO_SIGNAL: 35**
- **STILL_SINGLE_SIGNAL: 0**
- **REPLACEMENT_NEEDED: 1** (@chubbydiaries)

## Method

Trailing-24-month window: **2024-09-16 → 2026-09-16**.

- **TikTok video rows (22 rows / 23 videos):** Signal 1 = TikTok video-ID timestamp decode (validated method, cross-checked against browser relative dates in Stage 1). Signal 2 = third-party mirror metadata fetched independently:
  - 8 videos via Urlebird `uploadDate` (exact calendar-date match)
  - 15 videos via tikwm API `create_time` (exact calendar-date match)
- **Blog guide rows (5):** Signal 1 = creator-owned page JSON-LD `datePublished`; Signal 2 = JSON-LD `dateModified`.
- **NO_VIDEO_ID guide-discovery rows (8):** qualifying guide found on the creator's Urlebird profile; video-ID decode and Urlebird `uploadDate` agree on the date.
- Caveat recorded in the JSON: both TikTok channels ultimately derive from TikTok platform data — they are independent fetch/render paths, not independent publications. The guard this buys is against misattribution and decode error, not against TikTok itself misreporting.

## Verified rows (35)

**Via Urlebird uploadDate (video rows):**
| Handle | Guide | Date |
|---|---|---|
| @carissamonyce | guide video | 2026-05-08 |
| @christian.the.creative | guide video | 2026-08-31 |
| @natyexplora | guide video | 2025-10-17 |
| @twirlliketalia | guide video | 2026-02-02 |
| @wanderingcreator_meghana | guide video | 2026-05-07 |
| @elisetanriverdi | guide video | 2025-08-13 |
| @gokylahgo | Machu Picchu / Lima 4-day Peru | 2026-09-14 |
| @thoughtsofatraveller | 5-day Chiang Mai itinerary | 2026-03-10 |

**Via tikwm create_time (video rows):**
| Handle | Guide | Date |
|---|---|---|
| @callmecandace.tv | El Salvador itinerary | 2025-03-09 |
| @detouristahq | Bangkok itinerary | 2026-03-17 |
| @epicamerica_ | 5-day LA itinerary | 2026-03-10 |
| @explorewithsofs | 2-week Italy itinerary | 2026-04-17 |
| @jessmelu | 3-day Split, Croatia | 2025-05-18 |
| @kristinacors | NYC guide | 2026-03-23 |
| @letravelstyle | California road trip itinerary | 2025-07-02 |
| @lisarosanty | 3-day San Francisco itinerary | 2026-01-28 |
| @vitortrip | London 3-day itinerary | 2026-01-28 |
| @vitortrip | Athens 3-day guide | 2026-02-08 |
| @aintthattobi | Puerto Rico itinerary | 2026-01-17 |
| @amyenvoyage | UK escape video (Helsinki blog covers the extracted guide) | 2026-04-06 |
| @benihunyadi2 | 5-day Amalfi Coast | 2026-01-22 |
| @shewandersabroad | 5-day Amalfi Coast itinerary | 2025-12-31 |
| @wawawandering__ | Stockholm Part 1 | 2025-05-21 |

**Via creator blog JSON-LD (datePublished + dateModified):**
| Handle | Guide | Published | Modified |
|---|---|---|---|
| @thegingerwanderlust | Norway 10-day itinerary | 2024-10-03 | 2024-10-03 |
| @herjoliejourney | 1-week Iceland itinerary | 2026-01-17 | 2026-07-24 |
| @theblondeflamingo | One week in Zurich | 2025-03-13 | 2025-03-13 |
| @chloejadetravels | 10-day Japan itinerary | 2024-10-09 | 2024-10-10 |
| @thecuriouspixie | Malaysia itinerary | 2022-05-26 (out of window) | 2026-02-17 (in-window update) |

**Guide discovered via Urlebird profile (ID decode + uploadDate agree):**
| Handle | Guide | Date |
|---|---|---|
| @uktravel | Wales 5-day road trip series | 2026-09-14 |
| @nikitabathia | Abu Dhabi Day 1 icons | 2026-07-08 |
| @sandymakessense | Palermo food guide | 2026-08-05 |
| @CandaceAbroad | 3-day Kuala Lumpur itinerary | 2026-08-02 |
| @nospaceinmypassport | Perfect day in Menorca | 2026-08-24 |
| @makisantos_ | Phu Quoc 24h / 2-day itinerary | 2026-09-02/03 |
| @travelcheapwithchloe | Manchester / Peak District guides | 2026-09-14 (also 2026-09-03, 2026-08-26, 2026-04-20, 2025-10-05) |
| @postcardsbyhannah | 1-week Route 66 itinerary | 2026-08-13 |

## Replacement needed (1)

- **@chubbydiaries** — the claimed Sonoma 72-hour food guide has no capturable creator-attributable URL. Two independent web searches (exact-handle and guide-title variants) returned no qualifying post/video URL. Without a URL there is nothing to date-verify. → REPLACEMENT_NEEDED.

## Notes for the parent

- `@amyenvoyage`: the audit's attached TikTok video (decoded 2026-04-06, a UK escape video) is a different guide from the extracted Helsinki itinerary, but the Helsinki blog itself carries in-window JSON-LD dates (published 2026-04-15, modified 2026-05-10), so the row passes on the blog evidence.
- `@thecuriouspixie`: original publish (2022-05-26) is outside the 24-month window; the row passes on the substantive in-window update (2026-02-17). Flagged in the JSON.
- `@makisantos_`: ID decode 2026-09-02 vs Urlebird 2026-09-03 — a UTC/timezone boundary, treated as agreement.
- Internet Archive CDX returned HTTP 503 during this pass, so no archive-capture evidence was available.
- TikTok's own page HTML exposes `createTime` but from the same TikTok object as the ID, so it was not counted as independent.
- Temporary evidence files used: `/tmp/scriptA_results.json`, `/tmp/scriptB_results.json`, `/tmp/scriptC_results.json`, `/tmp/scriptD_results.json`, `/tmp/blog_dates.json`, `/tmp/ub_results.json`.
