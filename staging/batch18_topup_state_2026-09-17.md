# Batch 18 top-up research state (2026-09-17, selector batch18-topup)
# WORKING FILE — not a deliverable. check_date for all evidence: 2026-09-17.

## FINAL RESULT: 0 new creators added. Batch remains at 9.
## Shortfall: 16 (target was 16 new, 25 total)

### Why zero additions
Both strongest candidates failed on re-verification 2026-09-17:

1. **@tavernatravels (Taylor Taverna)** — DEDUP BLOCKED
   - Found in batch12.csv: `Taylor Taverna,@tavernatravels,tiktok,travel guides,45200`
   - Same handle already in system. Cannot add to batch18 (Instagram) as duplicate.
   - Was otherwise fully gated (SocialVeins 64.4K/0.25%, Kyrgyzstan guide 2025-04-13).

2. **@grrrltraveler (Christine Kaaloa)** — DEDUP BLOCKED + EXCLUSION FAIL
   - Found in influencers.csv AND batch8.csv: `Christine Ka'aloa,@grrrltraveler,instagram,solo travel guides,20.8K`
   - Same handle already in system. Cannot add.
   - ALSO fails exclusion: operates hosted group tours
     (https://grrrltraveler.com/group-tours-solo-travel/fall-japan-group-trip/ —
     "11 Day Fall Japan Adventure Trip"; Udaipur guide states "scout it as one of
     the cities for my group tour").

### Other candidates checked 2026-09-17 (all rejected or insufficient)
- @sarowly: Already in batch18.csv (existing row). Not a new addition.
- @bridgesandballoons (75.8K): Couple/family-run (Victoria + Steve) — fails individual gate.
- @outdoorsydiva (43.9K): Offers "curated group adventure trips" — fails hosted-trip exclusion.
- @therichaunt (37K): Sells "Customized Travel Plan" ($299.99) — fails trip-planning exclusion.
- @tiffpenguin (337.2K): Photographer, no structured itinerary/guide found.
- @brokegirltravelguide: Identity confusion (vs Bon Voyage Jackie); no blog verified.
- @marissamcgarr: No creator-owned blog with guides found.
- @jessieonajourney: Likely exclusion failure (NYC photo tours operator).
- @evs_adventures: REJECT (group trips).
- @thesojournies: REJECT (hosted Costa Rica group tour).
- @theglobetrottingdetective: REJECT (women-only Afghanistan tour).

### Pools exhausted
- POOL A (batch16 carryover): All 16 either rejected, insufficient evidence, or no qualifying guide.
- POOL B (Feedspot solo-female): All 11 either rejected, insufficient, or identity issues.
- POOL C: @tavernatravels blocked (above); @dreamsinheels weak/deprioritized.

### Deliverables status
- batch18.csv: UNCHANGED (9 rows)
- staging/selection_log_batch18.csv: UNCHANGED (9 rows)
- staging/itineraries_batch18.json: UNCHANGED (9 extractions)
- No files modified. No Gate 1 run (nothing to validate).

### Known issue (unchanged)
Existing 9 batch18 rows all have engagement_observed=unknown. Remediation out of scope.

## Fourth-attempt working notes (2026-09-17, selector batch18-topup)
- batch18.csv confirmed at PROJECT ROOT: ~/workspace/travel-influencer-pilot/batch18.csv (11 rows, NOT staging/).
- @migrationology DEDUP-BLOCKED: found in batch1.csv AND influencers.csv (Mark Wiens, 1.3M) — recorded to validation/quarantine.json with status quarantined per task rule (in dataset -> Gate 5 adjudication). NOT re-researched.
- Fresh shortlist (all CLEAR of quarantine + universe at 2026-09-17 check): @emmacruises, @bearfoottheory, @socalhiker, @modernhiker, @lifewellcruised, @garybembridge, @livethevanlife, @alisontravels, @ulteriorepicure, @kathi_daniela, @eternal_expat, @mylittleworldoftravelling, @prof.cruise, @girleatworld.
- Identity confirmed so far: Kristen Bor = bearfoottheory.com/about (named individual; hiking+vanlife blogger).
- Reach sources so far: Feedspot "100 Hiking Blogs 2026" (Bearfoot Theory IG 54.2K, SoCal Hiker 17.6K, Modern Hiker 39K); Sail Away top-100 UK cruise IG (Emma Cruises 47.1K, table updated 2024-12-02); Feedspot "80 Best Cruise Blogs 2026" (Tips For Travellers Gary Bembridge IG 12.8K, Prof. Cruise IG 15.6K, Life Well Cruised Ilana Schattauer IG 80.9K); Feedspot "Top 90 Van Life Influencers 2026" (livethevanlife Shane Jordan 40.3K, alisontravels Alison Turner 35.2K); Feedspot "60 Best Food Travel Blogs 2026" (Girl Eat World Melissa Hie IG 294.4K; Travelling Foodie 32.6K); Feedspot "90 Best Expat Blogs 2026" (Kathi Daniela IG 23.4K); TPG food photographers (Bonjwing Lee @ulteriorepicure 21.8K, publication date unknown — needs named dated source).
- Still needed per candidate: in-window own-site guide (date after 2024-09-17), engagement signal (media kit or cross-platform metrics, named source + date), identity method evidence for all.

## Fourth attempt — completed 2026-09-17 (batch18-topup)
- Added 2 verified creators (not 14): @bearfoottheory (Kristen Bor) and @girlonahike (Alicia Baker). Batch now 13/25.
- Quarantine: added @emmacruises (excluded — travel agency operator; own site: "I've Launched My Own Travel Agency") and @thesocalhiker (excluded — hosted group trip; Trovatrip "Iceland with Jeff Hester & Social Hikers" Jan 2025). Both absent from dataset at fresh 2026-09-17 dedup. Quarantine 64 -> 66 entries (concurrent edits ongoing; read-modify-write used).
- Dedup universe at write time: 393 handles; both new handles clear.
- Decided NOT to include: @lifewellcruised (no in-window structured itinerary found; "Group cruise" bio link = hosted-trip risk), @garybembridge (travel-agency booking operation = operator risk, same class as @emmacruises exclusion), @modernhiker (no in-window guide), @prof.cruise (insufficient evidence), food-travel leads (unverified, gates too costly at this budget).
- Gate 1 (scoped to [18]): exit 1 with exactly one error — batch-size rule "extractions must be a list of exactly 25 (got 13)". Zero schema warnings on the 2 new rows. stage.json restored byte-identically (sha256 b1be0f44... verified).
- Evidence audit: 31/31 checks passed across batch18.csv (13 rows, 7 cols), selection log (13 rows, 23 cols), itineraries JSON (13 extractions, real extracted items, allowed item types), quarantine (66 entries).
- Honest shortfall: 12 rows short of 25. Only these 2 candidates cleared all gates watertight; the rest failed on agency/hosted-trip exclusions or missing evidence that could not be verified without inventing facts.

## Continuation notes (2026-09-17, selector batch18-topup)
- @jayneytravels (Jayne Gorman, 72K IG per own 2026 media kit) — DEDUP-BLOCKED: already in batch20.csv (Austria/European weekend travel row). Passed most gates (media-kit engagement 8%, Parga 2026 guide, no WeTravel/TrovaTrip trips, no planning/coaching service) but cannot be re-added. NOT appended.
- @travelherstory (Michelle L. Jensen) — REJECTED on reach: own contact page (travelherstory.com/contact/) reports 3,700 Instagram followers (below 10K). Also flags: "teaches blogging as a business" + free Travel Blogging Guide (coaching-adjacent). Do not revisit.
- @solotravelinstyle (Ioana Moga) — DEDUP-BLOCKED: already in batch16.csv. NOT re-researched.
- @aladyinlondon — quarantined as excluded (paid travel-planning service); @passporttofriday, @luxurycolumnist exclusions noted but not yet recorded (need re-check before adding).
- Six banked rows (@absolutelylucy, @sarowly, @bucketlistjourney, @learningescapes, @indianahannah_blog, @malaysiaasia) have now-prohibited engagement_observed=unknown; some reach values rounded (14K/36K). NOT edited; surfaced to parent/coordinator for adjudication.
- batch18.csv still 9 data rows at last verification; additions target remains 16.
- @earthtosarahphoto (Sarah Rohrbach, 36.2K Feedspot) — REJECTED: her business "Earth to Sarah Media" offers Social Media Consulting + "Travel Planning/Advice" (findglocal listing) — consulting/planning exclusion. Do not revisit.
- @solowithsav (Savanna Crowell, 107.8K Feedspot) — REJECTED: own blog Egypt post states "I host group trips for solo female travelers to Egypt" — hosted-group-trips exclusion. Do not revisit.
- Dedup-blocked from Feedspot micro list: @marissa.daily, @jessica_traveler, @liveloveruntravel (all in batch19.csv); @janelleonajet quarantined/excluded.
- @aliki_travel_blog (Aliki, 18K Feedspot) — REJECTED: own site guides show search-index "Last Updated: 1689 days ago" (~2021-22); no in-window own-page content; bio pivots to video. Do not revisit.
- @findlovetravel (Samantha Oppenheimer, 18K Feedspot) — REJECTED: own guides "Last Updated" ~899-970 days ago (2023-early 2024); homepage latest-guide images dated 2024/03-2024/07 (pre-cutoff); site dormant. Do not revisit.
- @travelwithcg (Charu Goyal, 43.3K Feedspot) — REJECTED: own sitemap post-sitemap.xml lastmod 2023-09-15; site dormant since 2023; no in-window own-page content. Do not revisit.
- @toosha_z (Toosha Z, 25.5K Feedspot) — REJECTED: no own blog/qualifying structured itinerary found; Instagram-only creator. Do not revisit.
- @thatbackpacker (Audrey Bergner) — REJECTED: operator exclusion. Own about page states "1 Boutique Hotel currently under restoration in Argentina" (https://thatbackpacker.com/about/) — hospitality operator. Also runs Che Argentina Travel. Do not revisit.
- @dreamsinheels (Olga Maria Czarkowski, 29.4K Feedspot) — REJECTED: no in-window structured itinerary content found; own site's indexed guides are 6+ years old (Costa Rica itinerary "Last Updated" ~2289 days; bucket list ~3535 days). Do not revisit.
- @floratheexplorer (Flora, 12K Feedspot) — REJECTED: own site dormant; indexed itineraries ~7 years old (Colombia ~2715 days, Cuba ~2725 days). Do not revisit.
- @glographics / @theblogabroad (Gloria Atanmo, 255.1K Feedspot) — REJECTED: own site dormant (newest indexed posts ~6 years old) AND coaching exclusion ("After coaching hundreds of bloggers and entrepreneurs in the last 3 years" — theblogabroad.com). Do not revisit.
- @paulinaperrucci (Paulina Perrucci, 38.5K Feedspot) — REJECTED: no qualifying own-site structured itinerary content surfaced (searches returned only unrelated AI-generated itineraries); primarily a wedding photographer/luxury lifestyle influencer. Do not revisit.
- @officialcoleelder (Cole Elder, 38.1K Feedspot) — REJECTED: no own-site structured itinerary content surfaced (coleephoto.com; photographer, no guide content found). Do not revisit.
- @lattesnluggage (Raven Patzke) — ACCEPTED as batch18 row #10 (2026-09-17): solo-travel, 27.5K Feedspot. Gates: identity pass (Collabstr/shoutoutmiami/own media kit); content fit pass (own blog Berlin post 2026-04-03 explicit URL date; Key West guide 2025-04-07); reach pass (27.5K, Feedspot list fetched 2026-09-17); engagement pass via same-creator TikTok per-post metrics (46.7K likes/442 comments; 14.3K likes/115 comments; Collabstr 41.72% engagement, avg 6.3k likes/163 comments) + YouTube short (61 likes/1 comment); IG activity pass (wildernessresort.com featured her IG travel post, crawled 2026-09-08; blog 2026-04-03; TikTok 57.5K followers/2396 videos fetched 2026-09-17); WeTravel/TrovaTrip clean (no hosted trips found); exclusions pass (no planning/coaching/operator); purchase intent present (affiliate links, RAVEN5 hotel code, ticket discount codes). Appended to batch18.csv, selection_log_batch18.csv, itineraries_batch18.json (2 itineraries: Berlin 15 items, Key West 19 items). Dedup/quarantine clear. Scoped Gate 1: 1 error (10/25 extractions — expected shortfall), 0 batch18 warnings; stage.json restored byte-identically.
