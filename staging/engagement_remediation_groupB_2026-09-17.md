# Group B engagement remediation — 2026-09-17

**Scope:** 32 TikTok creators in batches 12, 13, 14 whose `engagement_observed`
was `unknown` or relied on third-party analytics (StarNgage screenshot).

**Founder ruling applied:** evidence must be creator-owned — a creator-published
media kit, or observable engagement on the creator's own public TikTok/YouTube/
Instagram posts. Third-party analytics estimates (StarNgage, Socialveins,
Heepsy, Collabstr) are invalid. Plain `unknown` is a FAIL.

**Result: 31 remediated / 1 REMOVE-CANDIDATE.**

Only the `engagement_observed` column was changed, in:
- `staging/selection_log_batch12.csv` (7 rows)
- `staging/selection_log_batch13.csv` (14 rows)
- `staging/selection_log_batch14.csv` (10 rows)

All other columns verified byte/logically unchanged via quote-aware
record-level diff against pre-edit backups.

## Remediated evidence (all observed 2026-09-17)

### Batch 12 — creator-owned TikTok video pages (direct page open)

| Handle | Video page | Plays | Likes | Comments | Shares | Saves |
|---|---|---:|---:|---:|---:|---:|
| @meghanorourkee | [/video/7438522433746881835](https://www.tiktok.com/@meghanorourkee/video/7438522433746881835) | 653,700 | 39,800 | 267 | 9,594 | 20,996 |
| @darrenshavae | [/video/7523587289868455181](https://www.tiktok.com/@darrenshavae/video/7523587289868455181) | 145,200 | 6,036 | 89 | 1,006 | 4,621 |
| @tzatchickie | [/video/7610847293901688097](https://www.tiktok.com/@tzatchickie/video/7610847293901688097) | 26,400 | 526 | 21 | 128 | 437 |
| @minywander | [/video/7636776828895497503](https://www.tiktok.com/@minywander/video/7636776828895497503) | 27,600 | 914 | 44 | 331 | 1,097 |
| @dwanders | [/video/7513684450497006904](https://www.tiktok.com/@dwanders/video/7513684450497006904) | 188,900 | 6,341 | 48 | 960 | 3,420 |
| @seewithjosie | [/video/7631669355092233494](https://www.tiktok.com/@seewithjosie/video/7631669355092233494) | 167,000 | 8,621 | 52 | 2,519 | 9,609 |
| @ashlaygoose | [/video/7575342985991195959](https://www.tiktok.com/@ashlaygoose/video/7575342985991195959) | 128,000 | 16,900 | 53 | 2,705 | 5,130 |

### Batch 13 — creator-owned TikTok video pages (direct page open)

| Handle | Video page | Plays | Likes | Comments | Shares | Saves |
|---|---|---:|---:|---:|---:|---:|
| @kawaiiicoco | [/video/7634412121131879693](https://www.tiktok.com/@kawaiiicoco/video/7634412121131879693) | 345,500 | 67,700 | 180 | 6,578 | 19,836 |
| @kirstenwendlandt | [/video/7645735640369204501](https://www.tiktok.com/@kirstenwendlandt/video/7645735640369204501) | 80,500 | 1,438 | 33 | 743 | 899 |
| @asyatravels | [/video/7596373989673405727](https://www.tiktok.com/@asyatravels/video/7596373989673405727) | 126,700 | 7,509 | 29 | 3,664 | 5,657 |
| @amomexplores | [/video/7427141383615614254](https://www.tiktok.com/@amomexplores/video/7427141383615614254) | 72,700 | 2,377 | 31 | 1,102 | 2,135 |
| @japantravelbasics | [/video/7608893409436192001](https://www.tiktok.com/@japantravelbasics/video/7608893409436192001) | 73,000 | 2,026 | 13 | 1,398 | 2,668 |
| @nessahuangg | [/video/7369207226285772033](https://www.tiktok.com/@nessahuangg/video/7369207226285772033) | 613,700 | 24,700 | 116 | 1,349 | 2,732 |
| @lifeofthetravelingpin | [/video/7480394699061284142](https://www.tiktok.com/@lifeofthetravelingpin/video/7480394699061284142) | 327,800 | 14,300 | 125 | 5,452 | 12,657 |
| @zozomccormack | [/video/7631632559805451528](https://www.tiktok.com/@zozomccormack/video/7631632559805451528) | 349,800 | 23,100 | 65 | 3,002 | 18,955 |
| @marco.miglionico_ | [/video/7608041596633845006](https://www.tiktok.com/@marco.miglionico_/video/7608041596633845006) | 1,100,000 | 106,400 | 264 | 28,800 | 22,322 |
| @findingalexxtravel | [/video/7475540148290243847](https://www.tiktok.com/@findingalexxtravel/video/7475540148290243847) | 231,300 | 12,200 | 136 | 3,515 | 12,704 |
| @barefoot.blaze | [/video/7514575758677839122](https://www.tiktok.com/@barefoot.blaze/video/7514575758677839122) | 46,400 | 1,525 | 10 | 728 | 1,553 |
| @pointstopointtravel | [/video/7573477725353135373](https://www.tiktok.com/@pointstopointtravel/video/7573477725353135373) | 269,200 | 23,300 | 1,323 | 4,109 | 9,969 |
| @deccadotcom | [/video/7582695666606935326](https://www.tiktok.com/@deccadotcom/video/7582695666606935326) | 369,100 | 22,500 | 414 | 6,994 | 21,385 |
| @adventuresofkatelyn | [/video/7291576263859309825](https://www.tiktok.com/@adventuresofkatelyn/video/7291576263859309825) | 60,600 | 1,025 | 16 | 724 | 671 |

### Batch 14 — creator-owned TikTok video pages (direct page open)

| Handle | Video page | Plays | Likes | Comments | Shares | Saves |
|---|---|---:|---:|---:|---:|---:|
| @outdoorswithlau | [/video/7607885107382275350](https://www.tiktok.com/@outdoorswithlau/video/7607885107382275350) | 630,800 | 27,300 | 70 | 10,200 | 15,048 |
| @marianawengorovius | [/video/7620460271911390496](https://www.tiktok.com/@marianawengorovius/video/7620460271911390496) | 146,200 | 33,000 | 58 | 1,666 | 6,582 |
| @ioviaggiosola45 | [/video/7622308775302630679](https://www.tiktok.com/@ioviaggiosola45/video/7622308775302630679) | 102,000 | 6,736 | 124 | 1,347 | 5,129 |
| @helloshayne_ | [/video/7543960475990592769](https://www.tiktok.com/@helloshayne_/video/7543960475990592769) | 307,900 | 10,900 | 250 | 8,008 | 8,090 |
| @jvwanderer | [/video/7613120581881318677](https://www.tiktok.com/@jvwanderer/video/7613120581881318677) | 46,500 | 1,515 | 31 | 722 | 1,828 |
| @markodea8 | [/video/7599983438338379029](https://www.tiktok.com/@markodea8/video/7599983438338379029) | 218,000 | 4,503 | 20 | 1,060 | 1,760 |
| @himemet | [/video/7626729068020485384](https://www.tiktok.com/@himemet/video/7626729068020485384) | 90,200 | 3,576 | 111 | 1,350 | 3,312 |
| @_travelcuriosity_ | [/video/7648666157196610849](https://www.tiktok.com/@_travelcuriosity_/video/7648666157196610849) | 370,300 | 23,900 | 56 | 8,613 | 17,621 |
| @amymarietta | [/video/7605805860270443807](https://www.tiktok.com/@amymarietta/video/7605805860270443807) | 331,700 | 17,500 | 138 | 4,198 | 13,674 |

### @karenendique (batch 14) — search-index snapshot of creator-owned posts

The creator-owned TikTok photo page
([/photo/7542331047359368456](https://www.tiktok.com/@karenendique/photo/7542331047359368456))
rendered no metrics on direct open. Evidence comes from the search-index
snapshots (Google-cached `og:description`) of her own TikTok posts, recorded
with crawl dates:
- Itinerary-format photo post 7542331047359368456: **253 likes, 14 comments**
  (crawled ~210 days before 2026-09-17).
- Bangkok 5D4N itinerary video: **1,153 likes, 42 comments**
  (crawled ~160 days before 2026-09-17).
- Kamakura/Enoshima day-trip video: **431 likes, 9 comments**
  (crawled ~168 days before 2026-09-17).

These are metrics of the creator's own public posts, not third-party
estimates, and satisfy the ruling.

## REMOVE-CANDIDATE

### @wherejesstravels (batch 13)

No valid engagement evidence after **7 distinct attempts** (2026-09-17).
Row left with `engagement_observed=unknown`; recommend removal from the pilot.

1. **TikTok profile page opened** — 73,300 followers, 6.6M total profile likes,
   853 videos. Profile aggregate only; no per-post metrics visible. Profile
   totals are not per-post engagement evidence under the ruling.
2. **Creator-owned YouTube Short opened**
   (`https://www.youtube.com/shorts/0hA_R_lUV7E`, "The best things to do in
   Mallorca") — fetched text carried no engagement figures.
3. **Creator's own blog itinerary opened**
   (`https://wherejesstravels.com/7-day-mallorca-itinerary/`) — no engagement
   metrics on the page.
4. **`site:tiktok.com wherejesstravels video` search** — no video pages of this
   creator returned (only unrelated accounts).
5. **Quoted search `"wherejesstravels" tiktok video likes`** — returned only a
   third-party travel-guide aggregator (airial.travel) quoting her numbers
   (invalid per ruling) and unrelated accounts.
6. **Search `"@wherejesstravels" itinerary tiktok`** — only her own blog posts,
   no metrics.
7. **Search `wherejesstravels media kit "work with me"`** — no creator-published
   media kit with engagement metrics found.

Her prior `engagement_observed` was a StarNgage third-party estimate and has
been treated as invalid.

## Verification

- Edit script applied changes only to `engagement_observed` for the 31 listed
  handles; quote-aware record-level diff against pre-edit backups confirmed
  every other cell in every row byte/logically unchanged.
- Scoped Gate 1 run for batches 12, 13, 14 after edits (see below).
- No itinerary CSV/JSON, no other column, and no other batch file was touched.
- No logins, follows, likes, comments, outreach, or git operations performed.
