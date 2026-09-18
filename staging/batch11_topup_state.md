# Stage 2 batch 11 top-up — working state (2026-09-17)

## Confirmed pool: 13 (all verified 2026-09-17, all require final dedup recheck + activity/exclusion checks before write)

1. @katieosheaaway — Katie O'Shea, 16,400 followers. Video 7536275089478651167, published 2025-08-08. California road trip: Sequoia, Kings Canyon, Yosemite. URL: https://www.tiktok.com/@katieosheaaway/video/7536275089478651167
2. @detouristahq — Marcos, 58,100 followers. Video 7618152560796486933, create_time=1773739380. Six-day Bangkok-area itinerary. URL: https://www.tiktok.com/@detouristahq/video/7618152560796486933
3. @alynnavalbuena — 51,400 followers. Video 7524199296187632903, published 2025-07-07. Seven-day DIY Bali itinerary. URL: https://www.tiktok.com/@alynnavalbuena/video/7524199296187632903
4. @chloeconortravels — 14,800 followers. Video 7594054954680126742, published 2026-01-11. Prague day itinerary. URL: https://www.tiktok.com/@chloeconortravels/video/7594054954680126742
5. @explorinwithnic — 39,500 followers. Video 7607945794917879062, published 2026-02-17. South Island NZ route. URL: https://www.tiktok.com/@explorinwithnic/video/7607945794917879062
6. @lucyinthesskyy — 14,700 followers. Video 7612631506153999638, published 2026-03-02. Greek-island guide. URL: https://www.tiktok.com/@lucyinthesskyy/video/7612631506153999638
7. @_cocoylim — cocoy, 155,600 followers. Video 7617345387824778503, published 2026-03-15. Ten Taiwan day-trip ideas. URL: https://www.tiktok.com/@_cocoylim/video/7617345387824778503
8. @sarah.rh.bashir — Sarah Bashir, 22,100 followers. Video 7634256652715298055, create_time=1777488897 (recorded 2026-04-29). Three-day Morocco Imperial Cities. URL: https://www.tiktok.com/@sarah.rh.bashir/video/7634256652715298055
9. @daniellestravelblog — Danielle, Liverpool, 29,500 followers. Video 7604623136306253078, create_time=1770589305. Italy train route: Milan→Verona→Venice→Florence→Rome→Naples/Amalfi. URL: https://www.tiktok.com/@daniellestravelblog/video/7604623136306253078
10. @catchagypsea — ieva, 491,900 followers. Video 7559954654868589835, create_time=1760189113. Egypt: Giza, Siwa, Aswan, Abu Simbel, Luxor, Marsa Alam. URL: https://www.tiktok.com/@catchagypsea/video/7559954654868589835
11. @eralevich — Erick Enríquez, 32,700 followers. Video 7525598971625000210, create_time=1752190056. Eight-day Switzerland: Zürich, Zermatt, Grindelwald, Interlaken/Spiez, Blausee/Oeschinen, Zürich or Geneva. URL: https://www.tiktok.com/@eralevich/video/7525598971625000210
12. @dg_travel — Denys, 24,500 followers. Video 7581028950634683681, create_time=1765386746 (2025-12-10). Dubai 5-day: Old Dubai (Creek, Gold Souk, abra), Marina/JBR, Palm Jumeirah, Dubai Mall/Burj Khalifa, Desert Safari, Abu Dhabi. URL: https://www.tiktok.com/@dg_travel/video/7581028950634683681
13. @tanya.travels — 47,400 followers. Video 7622835610705693957, published 2026-04-21. Vienna guide: Schönbrunn, Austrian National Library, Prater, Naschmarkt. URL: https://www.tiktok.com/@tanya.travels/video/7622835610705693957

## Pending leads (needs browser verification)
- @haylsa — Hayley Hunter, 430,900 followers. Video 7508514989817269526, create_time=1748212385. "Perfect 2 week itinerary" Sri Lanka — visible route structure not yet secured. Include only if structured text obtained; else reject.
- @tiamo.vietnam — Khanh, dedup-free. Siem Reap/Angkor Wat tips carousel (photo 7620432610728135957). Needs: profile open (reach, identity, current activity), date verification. NOTE: browser_open failed 2026-09-17; retry next turn.

## New rejects logged 2026-09-17
- @hersavvytravels — reach fail (517 followers)
- @nikkionherway — dedup match (line 245)
- @lifeofthetravelingpin — dedup match (line 196)
- @daniel.bun_ — reach fail (2,507 followers)
- @thattravelista — reach fail (641 followers, 0 videos)
- @mccrawsonthemap — couple (Carson and Melissa McCraw)
- @mrandmrsd.adventures — couple (also confirms earlier reject)
- @aidenandmaddy — couple (already rejected)

## Still needed: 8 more (6–7 if both pendings pass)

## Pre-write checklist (run when pool = 21)
1. Final dedup recheck of ALL 21 handles against staging/dedup_universe_2026-09-17.txt
2. Final current-activity + exclusion (personalized planning / group trips) checks on all 21
3. Convert all create_time values to dates via TZ=America/New_York date -d @<ts>
4. Append 21 rows to batch11.csv; 21 rows to staging/selection_log_batch11.csv (23 cols, batch=11, check_date=2026-09-17, selector=batch11-topup, decision=include)
5. Append 21 objects to staging/itineraries_batch11.json (platform:"tiktok", allowed item_types only, opened URL, 2–3 sentence summary, confidence)
6. Run python3 validation/gate1_schema.py scoped to batch 11; separate legacy failures from new errors

## Session 2 update (2026-09-17, continued)

### Banked lead (needs browser verification)
- @eltravel.12 — dedup-free (grep 0). "Eltravel", 1-week Austria itinerary carousel: 2 days Vienna, Melk/Linz, Hallstatt, Salzburg, Innsbruck/Wattens (photo 7498116754338483478). Needs: profile open (reach, identity, current activity), date verification.

### Date conversions (all after 2024-09-17 cutoff)
- eralevich video 7525598971625000210 → 2025-07-10
- detouristahq video 7618152560796486933 → 2026-03-17
- daniellestravelblog video 7604623136306253078 → 2026-02-08
- catchagypsea video 7559954654868589835 → 2025-10-11
- sarah.rh.bashir video 7634256652715298055 → 2026-04-29
- dg_travel video 7581028950634683681 → 2025-12-10

### New rejects
- @itsemandty — couple (already on reject list; Singapore 3-day itinerary belongs to Em & Ty)
- @katieandjoeonthego — couple (Scotland Isle of Skye)

### Count
- Confirmed: 13. Pending verification opens: 3 (@haylsa, @tiamo.vietnam, @eltravel.12). Still needed: 8 total.
- Browser page opens hit a terminal failure this turn; verification opens deferred. Next: open pending profiles + continue discovery for remaining ~5.
