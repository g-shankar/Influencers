# TikTok Discovery Worker — Lead Pipeline Handoff (2026-09-17)

Worker operated WITHOUT browser.open (terminal restriction after @explorewithmairy profile-open failure).
All verification below is via browser.search only. NOTHING was written to batch CSVs — no creator
could be verified to the watertight bar on search evidence alone.

## Current batch counts (verified 2026-09-17)
- batch9: 14/25 — needs 11
- batch10: 14/25 — needs 11
- batch11: 13/25 — needs 12
- batch13: 24/25 — needs 1
- TOTAL STILL NEEDED: 35

## Search patterns that WORK (use these)
1. Reach via TikTok profile page in search index:
   `"<handle>" tiktok followers <FirstName> travel`
   Returns "@handle N Followers, M Following, X Likes" with crawl date. CHECK the crawl date —
   reach gate needs source dated within 90 days of check (2026-09-17).
   Proven: @explorewithmairy → 172.4k followers (but crawl 157 days old = STALE, fails 90-day rule).
2. Content-fit via quoted handle + topic:
   `"<handle>" tiktok itinerary travel guide`
   Works for distinctive handles (@ladytrailmix returned her video). Fails for common handles
   (fuzzy matching, e.g. @thechaoticnomad matched @thenorfolknomad).
3. Itinerary video harvest (no handle): `tiktok <destination> itinerary "day 1"` etc.
   Yields ~5 candidates/call WITH content-fit + engagement + date (video ID decodes to date).
   Missing piece is always reach — then apply pattern #1.

## Bulk reach-verified source (crawled 2026-09-17, TODAY — freshest reach evidence)
Feedspot Australian travel TikTok list:
https://creators.feedspot.com/australian_travel_tiktok_influencers/?_src=creatorshome
Feedspot Australian camping TikTok list:
https://creators.feedspot.com/australian_camping_tiktok_influencers/?_src=FS_homepage
Leads with EXACT reach + named identity (all dedup-clean at check 2026-09-17 EXCEPT noted):
| handle | name | followers | content-fit status |
|---|---|---|---|
| @sydneyguide | Evelien Langeveld | 36.8K | UNKNOWN — bio says "self-guided itineraries"; EXCLUSION RISK (may sell itinerary products) |
| @mollyrdixon | Molly Dixon | 92.8K | UNKNOWN |
| @thechaoticnomad | Ellie | 31.4K | UNKNOWN — quoted search fuzzy-matched wrong account |
| @melbournewithkids | Tanya Husnu | 27.6K | UNKNOWN |
| @mymelbournediary | Sanjana | 35.9K | UNKNOWN |
| @bee.wac | Bianca | 37.1K | LIKELY POOR FIT — posts single-spot "things to do" Melbourne videos (Lake Daylesford 839 likes/52.6K views), no structured itineraries seen |
| @whereiskapa | Kapa | 30.5K | UNKNOWN |
| @ausbackpacker | Dom | 60.9K | UNKNOWN |
| @lolahubner | Lola Hubner | 32.3K | UNKNOWN |
| @explorewithmahdi | Mahdi | 106.6K | UNKNOWN |
| @adamrikys | Adam Rikys | 100.9K | UNKNOWN |
| @weninmelb | Wen | 79.8K | UNKNOWN |
| @lovelylivingtravel | Lexi | 160.1K | UNKNOWN |
| @florence.anja | Flo | 79.9K | UNKNOWN |
| @anna.fack | Anna | 104.3K | UNKNOWN |
| @outbackmike | Michael Atkinson | 49K | UNKNOWN — survival content, travel-fit risk |
| @mermaidbodhi | Bodhi | 10.2K | UNKNOWN — freediver, travel-fit risk |
| @amber.moran | Amber Moran | 79.2K | LIKELY REJECT — bio is custom fly screens (camping), not travel |
Dedup hits (DO NOT ADD): @wildroadwanderers, @ourtouringlife, @bushandbay (couples);
@annathingbutanimals (hosts vegan group trips); @jadesimkins, @postcardsfromayana,
@travelwsammy, @travelingterry, @anniesbucketlist, @adventuresofkatelyn.

## Heepsy September 2026 travel-TikTok list (crawled 3 days before 2026-09-17 — FRESH reach)
http://heepsy.com/top-tiktok/travel — harvested rows 8–11:
- Row 8: Charlie Cuadrado — 42K followers, 0.1% ER, avg likes 18 → REJECT (dead engagement)
- Row 9: Jonathan Mejia — 18.7K followers, 0.1% ER, avg likes 17.5 → REJECT (dead engagement)
- Row 10: @sire.aventuras — 66.7K followers, 4.1% ER, avg likes 2.5K, Mexican travel/food.
  Reach FRESH. Content-fit search did NOT surface the account (only @seliganoroteiro couple
  and others). NEED: content-fit, identity, activity, purchase intent, exclusions.
- Row 11: @thetravelingjuanes — 12.4K followers, 0.2% ER, avg likes 25 → borderline;
  ER very low, name suggests possible couple/shared ("juanes" plural). NEED full gate.
Rows 1–7 and 12+ NOT yet harvested — next worker should continue the harvest.

## Content-fit VERIFIED leads (need reach via pattern #1 or browser profile open)
1. @emwanderstheworld — South of France route video 7602631551158963469 (2026-02-03):
   Nice base, train day trips Menton/Antibes/Cannes/St-Jean-Cap-Ferrat/Grasse, Old Town stay.
   14.9K likes, 73 comments. Identity "Em" (mononym). Purchase intent: weak (stay rec only).
   NEED: reach ≥10K (≤90d source), current activity, exclusions, stronger purchase-intent read.
   URL: https://www.tiktok.com/@emwanderstheworld/video/7602631551158963469
2. @amandanaviagem — Brazilian solo-travel creator "Amanda". MULTIPLE structured itineraries:
   - Video 7617605752869620999 (2026-03-15): solo destinations Jericoacoara/Jalapão/Ilha Grande
     with hotel (pousada Villa Chic) + tour operators + discount codes. 5,620 likes, 39 comments.
   - Video 7638748083026660616 (~2026-05): Natal/Pipa/João Pessoa 6-day with prices (R$170/190/180).
   - Ushuaia/El Calafate guide with prices (32.7K likes, 105 comments).
   - Holambra video: 35K likes / 685.3K views (airial.travel page).
   Purchase intent PRESENT (cupom AMANDA, 15% Bagaggio, R$100 nativosjalapao, "Publi" tags).
   NEED: reach ≥10K (≤90d source) — two search attempts failed to surface profile page.
   Identity "Amanda" (mononym). NEED: current activity confirmation, exclusions.
3. @gupaireuy — Thai creator, Sydney walking/running route video 7640005714446109972 (2026-05-15):
   St James/Museum station, Hyde Park, Archibald Fountain, St Mary's, NSW Gallery, bay path,
   Opera House. 457 likes, 9 comments. NEED: reach, named identity, activity, exclusions.
4. @lunanomadbooks — Italy route video 7631707242386967821 (2026-04-22). LIKELY REJECT —
   source language says "we" (shared account) + free guide/side-hustle promotion.
5. @sevenpointss ("Seven Points") — "2 WEEKS in Australia? ULTIMATE itinerary"
   video 7537511058844486942 (~2025-08-11), 260 likes/5 comments. NEED: identity, reach.

## Batch13 final slot
- @explorewithmairy — PARKED. Colombia 10-day itinerary video 7455375288315268385 (~2026-02),
  100.3K likes; "Mairy | Travel & Lifestyle", 172.4k followers per TikTok profile page BUT
  crawl is 157 days old → FAILS 90-day reach rule. Third-party validation: City Live Glasgow
  article (2025-02-20) names her a notable TikTok travel influencer. NEED: fresher reach source
  (browser profile open), current activity, purchase intent, exclusions.
- @thisatravels — REJECT (6,947 followers, below floor, observed 2026-09-17).
- @gabstraveljournal — REJECT (3,080 followers, below floor, observed 2026-09-17).

## Batch11 notes
- @tanya.travels — prior worker's topup pool claims "verified 2026-09-17": 47,400 followers,
  Vienna guide video 7622835610705693957 (2026-04-21, Schönbrunn/Austrian National Library/
  Prater/Naschmarkt). Search re-verification FAILED to surface her (results were other Tanyas).
  Treat as UNVERIFIED until browser pass. Do NOT write on pool note alone.
- Pool members @detouristahq (dedup), @dg_travel (couple) are CONFIRMED REJECTS —
  batch11_topup_state.md "confirmed pool" is STALE/CONTAMINATED. All other pool members are
  already written to batch11.csv.

## Prior rejections to retain (do not re-add)
@tourwithliesner (quarantined, never re-add); @wherejesstravels (quarantined 2026-09-17,
missing engagement evidence); @haylsa (hosted Morocco trip); @karenexplores (sells itineraries);
@nicolemsunderland (travel planning/consulting); @helenemoo (hosts retreats); @sarahfunkyy
(Funky Experiences tours); @mafearoundtheworld (duo + bookable trips); @wheretogoinitaly (couple);
@inmarcuswetrust (flytravelhq sells tours); @puretravelmoments (5,054 followers);
@nonstop_sarah (603 followers); @ate.icia (itinerary pre-cutoff); @017tv (no real name);
@talegatravel (travel agency); @mimirojas.co (trip planning + group trips); @shida_lainn
(hosted group trip); @followmeaway (couple); @chasingchyna (identity not proven);
@lauravogelle/@tiamo.vietnam/@eltravel.12 (need browser verification).

## Recommended next step for parent
The remaining 35 need browser.profile opens (reach ≤90d + activity + exclusions + identity).
Search-only verification caps at ~1 creator per 3–5 searches with frequent recency failures.
A delegated browser task (or lifting the browser_open restriction) is the unblock.
Priority order: batch13 (1) → batch9 (11) → batch10 (11) → batch11 (12).
