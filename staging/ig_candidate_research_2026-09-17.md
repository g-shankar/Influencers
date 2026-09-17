# Instagram Replacement Candidate Research — 2026-09-17

## Objective

Find 2–3 fresh Instagram travel creators to replace the quarantined Instagram slot(s) in the Stage 1 database. Each candidate was evaluated against all five hard requirements:

1. **Identity:** One named individual (not a brand/agency/repost). About page must show name and photo.
2. **Followers:** Exact Instagram follower INTEGER ≥ 10,000 from a named, dated source. Rounded forms (`80K+`, `87.1K`, "over 150K", "115,000") do NOT satisfy.
3. **Recent post:** Directly verifiable Instagram travel post dated on or after **2026-06-18**. Prefer a public Instagram embed on the creator's own blog. Need post URL, visible date, caption.
4. **Itinerary:** Travel niche + structured guide/itinerary in the required window. Handle absent from canonical `influencers.csv` (checked case-insensitively, 2026-09-17).
5. **Not excluded:** Not one of the seven excluded handles (`@travelingwithtals`, `@nytoanywhere`, `@polkadotpassport`, `@goingwithnicole`, `@chloe__trips`, `@chubbydiaries`, `@boyeatsworld`).

## Executive Summary

**Zero candidates clear all five requirements.** The strict exact-integer follower standard (Requirement 2) is the blocker across every candidate investigated. Instagram's login wall prevents direct profile verification; all follower figures come from secondary sources, which universally round or abbreviate.

**Top-ranked near-miss:** Alyssa Ramos / `@mylifesatravelmovie` meets 4 of 5. Her own official "Work With Me" page (crawled 2026-09-14) states "209k" — a named, dated source, but rounded, not an exact integer. Everything else (identity, recent IG posts embedded on her own blog with full captions, itinerary) is strong.

---

## Ranked Candidates (best-first)

### #1 — Alyssa Ramos / @mylifesatravelmovie — 4/5 (BLOCKED: exact follower integer)

**Handle:** `@mylifesatravelmovie`
**Real name:** Alyssa Ramos
**Niche:** Solo female adventure travel; "misunderstood destinations"; group trips; 150+ countries, all 7 continents.

**Requirement 1 — Identity: ✅ PASS**
- Named individual, extensively documented across independent sources.
- Jupiter Magazine profile: "Jupiter Native Alyssa Ramos Talks To Us About Traveling Solo To 84 Countries" — https://www.jupitermag.com/jupiter-native-alyssa-ramos-talks-to-us-about-traveling-solo-to-84-countries/
- CanvasRebel interview: "Meet Alyssa Ramos" — https://canvasrebel.com/meet-alyssa-ramos/
- Muck Rack journalist profile (Yahoo Life / HuffPost contributor) — https://muckrack.com/alyssa-ramos/articles
- Her own site's tagline pages identify her by full name with photo (mylifesamovie.com).
- Beau Monde Traveler luxury magazine profile (crawled 2026-09-16): "Solo Travel Success: Meet Influencer Alyssa Ramos" — https://beaumondetraveler.com/content/solo-travel-influencer-alyssa-ramos/

**Requirement 2 — Exact follower integer: ❌ FAIL (rounded)**
- Best source: her OWN official "Work With Me" page (mylifesamovie.com/work-with-me/, crawled 3 days ago ≈ 2026-09-14), "Social Media Numbers" section. Exact quote:
  > "Instagram – @MyLifesATravelMovie – 209k"
- "209k" is rounded, not an exact integer. Does NOT meet the strict standard (same category as "87.1K").
- The same page lists her secondary account exactly: "Instagram – @MyLifesATravelTRIBE (group trips) – 9,890" — exact integer, but BELOW the 10,000 floor and a different handle.
- Other sources (all rounded): Feedspot "210.4K" (crawled 2026-09-16); osmessn/Daily Express mirror "203k followers"; Jupiter Magazine "more than 200,000 followers"; 2017 media kit "101k" (stale).
- No source found stating an exact full integer (e.g., 209,XXX) for @mylifesatravelmovie.

**Requirement 3 — Dated IG post ≥ 2026-06-18: ✅ PASS (embed on own blog; post URL not extractable via search)**
- Her own blog (mylifesamovie.com) embeds her Instagram feed. Multiple tag/author pages (crawled 2026-09-10 through 2026-09-16) show recent posts with full captions and relative dates.
- Post A — Lake Ohrid, North Macedonia. Caption: "Add Lake Ohrid in North Macedonia to your 'affordable European water destinations', especially if you're not a fan of salt water and chaotic crowds! [Comment 'Balkans' and I'll send the full itinerary!]... This is probably the prettiest lake I've seen in Europe, and I've been to almost every European country!! Would you go here??" — Visible date: "2 weeks ago" (page crawled ~2026-09-11 → post ≈ late Aug 2026, AFTER 2026-06-18). Source: https://mylifesamovie.com/tag/travel-guide/
- Post B — Underwater Wine Cellar, Kotor, Montenegro. Caption: "Went to the viral Underwater Wine Cellar in Kotor, Montenegro and here's my honest feedback as someone who lives on a vineyard by the sea in Italy! [Comment 'Kotor' and I'll send you the extensive detailed Balkans Roadtrip itinerary and tips I just made, including all the info to go here!]... The wine was pretty good, not sure about the pricing at €55 per bottle minimum..." — Visible date: "2 weeks ago" (≈ late Aug 2026). Source: https://mylifesamovie.com/tag/travel-guide/
- Post C — Lake Ohrid "beach". Caption: "No salt, sharks, or crowds at this crystal clear 'beach' in North Macedonia! That's because it's a lake!... Commend 'Balkans' and I'll send you my full customized roadtrip itinerary for here and some of the other Balkans like Kosovo, Albania, and Montenegro!" — Visible date: "1 week ago" (≈ early Sep 2026). Source: https://mylifesamovie.com/tag/travel-guide/
- Each embed shows a "View on Instagram |" link (the direct post URL exists in page HTML but is not extractable via web search; would require browser fetch of the page).
- All three are travel content, dated after 2026-06-18 by the relative-date + crawl-date bound.

**Requirement 4 — Itinerary: ✅ PASS**
- Site is branded "Solo Female Adventure Travel & Itineraries" (mylifesamovie.com).
- Kotor post explicitly offers: "the extensive detailed Balkans Roadtrip itinerary and tips I just made."
- Published itinerary example: "11 Day Antarctica Peninsula Itinerary" — https://mylifesamovie.com/11-day-antarctica-peninsula-itinerary
- Travel-guide tag archive with structured guides: https://mylifesamovie.com/tag/travel-guide/
- Handle NOT in canonical influencers.csv (verified 2026-09-17, case-insensitive).

**Requirement 5 — Not excluded: ✅ PASS** (not among the seven).

**Weakest evidence link:** Requirement 2. The exact follower integer is missing. Her own official page rounds to "209k". No independent source states a full integer.

**Proposed itinerary:** "Balkans Roadtrip itinerary" (North Macedonia / Kosovo / Albania / Montenegro) — referenced in her Kotor and Lake Ohrid posts, offered to commenters; or the published "11 Day Antarctica Peninsula Itinerary" (https://mylifesamovie.com/11-day-antarctica-peninsula-itinerary).

---

### #2 — Evelina Krusinskaite / @evs_adventures — 2/5 (BLOCKED: exact count + qualifying post)

**Handle:** `@evs_adventures`
**Real name:** Evelina Krusinskaite (Evelina)
**Niche:** Adventure travel; digital nomad; content creator.

**Requirement 1 — Identity: 🔶 PARTIAL**
- Her own newsletter (evs-adventures-newsletter.beehiiv.com) identifies her as Evelina, "content creator, adventurer, and digital nomad": https://evs-adventures-newsletter.beehiiv.com/p/welcome-to-evs-adventures
- Full surname "Krusinskaite" from prior research; photo/name About page not firmly established via search.

**Requirement 2 — Exact follower integer: ❌ FAIL (rounded)**
- Her own newsletter states "45k" (rounded, her own words).
- Feedspot: "46.7K"–"46.8K" (rounded).
- No exact integer found.

**Requirement 3 — Dated IG post ≥ 2026-06-18: ❌ FAIL**
- Public aggregators surfaced Ireland travel content from her account, but no direct Instagram post URL with a visible absolute date on/after 2026-06-18 was found.
- A Wayback/Instagram profile fetch failed (terminal for that route; not retried via alternate methods per instruction).

**Requirement 4 — Itinerary: 🔶 UNVERIFIED**
- Niche is travel/adventure, but no specific structured guide/itinerary with source URL was confirmed in the required window.
- Handle NOT in canonical influencers.csv (verified 2026-09-17). Not excluded.

**Requirement 5 — Not excluded: ✅ PASS.**

**Weakest evidence link:** Requirements 2 and 3 — no exact count, no qualifying dated post.

---

### #3 — Daisy Dyke / @daisystraveldiaries — 2/5 (BLOCKED: exact count + qualifying post + identity depth)

**Handle:** `@daisystraveldiaries`
**Real name:** Daisy Dyke (per Feedspot only)
**Niche:** Digital nomad / travel.

**Requirement 1 — Identity: 🔶 WEAK**
- Name "Daisy Dyke" appears only via Feedspot directory listing. No creator-owned About page with name + photo verified via search.

**Requirement 2 — Exact follower integer: ❌ FAIL (rounded)**
- Feedspot: "258.4K" (crawled 2026-09-16); older result "234.2K". Both rounded.
- No creator-owned media kit or exact integer found.

**Requirement 3 — Dated IG post ≥ 2026-06-18: ❌ FAIL**
- Search surfaced current travel captions on TikTok, not a qualifying Instagram post. No directly dated IG post URL found.

**Requirement 4 — Itinerary: 🔶 UNVERIFIED**
- No specific structured itinerary source confirmed.
- Handle NOT in canonical influencers.csv (verified 2026-09-17). Not excluded.

**Requirement 5 — Not excluded: ✅ PASS.**

**Weakest evidence link:** Requirements 1–3 — thin identity, rounded count only, no qualifying post.

---

## Rejected Near-Misses (documented honestly)

| Candidate | Best follower evidence | Why rejected |
|---|---|---|
| Ioana Moga (The Solo Travel in Style Blog) | Feedspot "79.8K" / "81K" (rounded) | Rounded count; exact IG handle unverified; no qualifying dated IG post. Identity page exists (thesolotravelinstyleblog.com/about/ — names Ioana, photo) and site has detailed itineraries, but Requirements 2 and 3 fail. |
| Stephanie Barry Woods / @stephmylife | Irish Times article 2026-04-11 states "115,000" | Explicitly in the parent's "potentially rounded editorial figures" rejection category; no qualifying IG post on/after 2026-06-18 verified. |
| @in_giro_con_fluppa | Exact 2,215 (Mar 2026) | Below the 10,000 floor. |
| @nishiv | "9K+" (Apr 2026) | Below floor and rounded. |
| @myadventuresacrosstheworld | "43,600+" (May 2023 media kit) | Not exact ("+"); stale (2023). |
| @jayneytravels | "60K" | Rounded. |
| Anna-Katri Raiha | "more than 11,000" (2021-07-21) | Rounded and stale. |
| Jess Wandering | "785K" (older) | Rounded and stale. |
| @juliiathompson | Appeared in IG search results with recent NZ travel-guide captions | No follower count, no identity package, no itinerary source, no absolute post date established. Lead not pursued further. |

---

## Search Strategy (what was exhausted)

- **WordPress REST APIs** for creator blogs (mylifesamovie.com, thesolotravelinstyleblog.com) — confirmed post/itinerary archives.
- **Feedspot influencer directories** (solo travel, digital nomad) — universally decimal-K rounded; useful for discovery, useless for exact counts.
- **Creator-owned media kits / "Work With Me" pages** — Alyssa Ramos's official page was the strongest source found (named, dated 3 days ago) but rounds the main account to "209k".
- **Press profiles** (Jupiter Magazine, CanvasRebel, Beau Monde Traveler, Daily Express/osmessn mirror, Irish Times) — all round or use "more than"/"over".
- **Podcast show notes** (Buzzsprout, Podtail) — no exact counts.
- **Muck Rack journalist profile** — confirms identity/profession, not counts.
- **Direct Instagram profile fetch** — blocked by login wall (no login attempted per protocol).
- **Wayback Machine** — profile fetch failed; per prior instruction the failure was terminal for that turn and not reproduced via alternates.
- **Google-indexed instagram.com/p/ URLs** — the search engine does not return Alyssa's individual post URLs; only her blog's embeds.

## Conclusion

**No candidate clears all five requirements under the strict exact-integer standard.** The Instagram login wall makes direct exact-count verification impossible without login (which is not authorized), and every secondary source rounds.

**Recommendation for parent decision:**
- **Alyssa Ramos / @mylifesatravelmovie** is the clear best-first pick (4/5). The single gap is mechanical: her own official page says "209k" instead of a full integer. If the parent accepts her official "Work With Me" figure as the named/dated source with the integer recorded as unknown (rather than lowering the bar), she can proceed to Gate 4. If the bar is absolute, the search must continue — likely requiring either (a) authorized Instagram login, or (b) a creator whose exact count appears in a tourism-board case study or campaign report.
- Evelina Krusinskaite and Daisy Dyke are documented here as #2/#3 but are materially weaker (missing qualifying posts and exact counts) and are **not** recommended as replacements without substantial further research.
- Whether `@psimonmyway` also requires replacement (it remains Gate 4 quarantined alongside `@sarahdegheselle`) is unresolved and needs a parent ruling before final Stage 1 PASS.
