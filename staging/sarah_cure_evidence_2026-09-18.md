# Sarah De Gheselle slot — quarantine cure evidence (2026-09-18)

Slot: Stage 1 batch 7 Instagram slot, originally @sarahdegheselle, quarantined by Gate 4 council 2026-09-16.
The invalid 2026-09-17 swap to @mylifesatravelmovie was fully repaired on 2026-09-18 (removed from
influencers.csv, batch7.csv, staging/itineraries_batch7.json, staging/selection_log.csv; candidate
material retained only under staging/itineraries_ig_slot_2026-09-17.json,
staging/ig_candidate_research_2026-09-17.md, validation/council_results/ig_slot_*).

## Cure attempt (single compliant replacement attempt, read-only Instagram @sgshankar84)

- Probe: `instagram-cli accounts` — clear, no 429. All subsequent reads: profile, posts, post-by-URL.
- Zero writes: no follows, likes, comments, DMs, saves. Session stayed read-only.

## Gate evidence (all observed 2026-09-18, America/New_York)

1. **Named individual:** profile display name "Sarah De Gheselle 📸 Belgian travel photographer";
   identity previously confirmed via WP user record, visit.gent.be, bartsboekje interview, Feedspot.
2. **Exact follower integer ≥ 10,000:** 85,038 from the Instagram profile header (and repeated on post records),
   observed 2026-09-18 via read-only login. Named source + observation date recorded.
3. **Directly verifiable IG travel post, absolute date ≥ 2026-06-18:**
   - https://www.instagram.com/p/DdRTrIyipym/ — "Postcards from Antwerp", 2026-09-14 07:04:08, 102 comments
   - https://www.instagram.com/reel/DdB2ZYVKp2q/ — "Planning a trip to the Cotswolds? Save this 3-day itinerary", 2026-09-08 07:00:19, 71 comments
   - Reels on 2026-09-15, 2026-09-16, 2026-09-17 also observed.
4. **Structured itinerary/guide in window:** Dalat guide dated 2026-03-10 via WP REST API + JSON-LD
   (two date signals, in-window; per 2026-09-16 notes). Plus the IG-native Cotswolds 3-day itinerary reel (2026-09-08).
5. **Absent from DB/exclusions:** already the canonical Stage 1 slot holder; not on the exclusions list;
   not a brand/agency/repost account.

## Engagement signal (founder §5 ruling)
Login-verified exact-dated posts with comment counts (102 / 71), observed 2026-09-18.

## Purchase intent: present
Hotel tags where she stayed (@alexandrabarcelonahotel, @neuhaus.zillertal, @movenpicklactunis,
@casaalsoleortisei) + sponsored tourism-board partnerships (@catalunyaexperience, @visit_luxembourg,
@discover_tunisia.be — labeled "Advertentie").

## Flag for Gate 4 (transparent)
A story highlight advertises "Women Photography Retreat in Marrakech & Ourika Valley".
Recorded as a workshop product, not agency trip-selling (exclusion precedents: @ferinajo's paid WeTravel
group trips, @kat.triplanner's 1:1 custom itinerary planning service). Council may re-adjudicate.

## Records updated 2026-09-18
- validation/quarantine.json: @sarahdegheselle → resolved (cure evidence above)
- staging/selection_log.csv: 23-col cure row appended (batch 7)
- influencers.csv / batch7.csv: followers_approx unknown → 85038
- staging/itineraries_batch7.json: notes updated (itineraries remain [] per original extraction)
