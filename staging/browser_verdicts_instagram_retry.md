# Instagram browser verification RETRY verdicts — 2026-09-16 ~15:30 EDT

Source: read-only live-browser retry task (no login, no follows/likes/comments,
no account actions). Instagram's anonymous rate limit from the 14:00 EDT attempt
had cleared when the retry started; profiles loaded normally again until the
rate limit returned at the 4th handle (@tinboxtraveller, redirect to
/accounts/login/). Task ended promptly per stop condition.

## Verdicts from the retry

### Completed (verbatim observations)

@ytravelblog | followers=28,076 (page showed "28K", profile section "28,076")
| latest_post=September 15, 2026 (latest dated item in post grid; also
September 03 and September 08, 2026 items visible) | identity=couple
("Caz & Craig | Travel Bloggers", bio "Traveling Couple 💕") |
guide_date>=2024-09-16=N/A (highlights: "Nova Scotia Trip", "About Us",
"US Travel", "Road Trips", "Family Travel", "Florida", "Beach Trips" — none
dated; no dated guides/itineraries shown on profile) | verdict=FAIL |
notes=couple operator, not an individual creator

@fivefortheroadblog | followers=20,267 (profile section "20,267", page "20.2K")
| latest_post=August 18, 2026 (most recent date among dated items in grid;
grid order non-chronological — first visible photo dated June 09, 2026, then
Aug 18, Aug 07, Aug 04, Jul 25, Jul 22, Jul 15, Jul 13, Jul 10, Jul 07, 2026) |
identity=individual ("Leah | Theme Parks & Family Travel", she/her,
"Travel writer"; "Family Travel" is the content niche, operator is one named
person) | guide_date>=2024-09-16=N/A (bio: "Travel Itineraries for Your Next
Trip", but no dated guides/itineraries shown on profile page) | verdict=PASS |
notes=followers 20,267 >= 10K; latest post Aug 18, 2026 within 90-day gate
(>= 2026-06-18); individual creator

@travelingmelmt | followers=34,975 (page "34.9K") | latest_post=September 03,
2026 (first items included pinned older posts Jan 06, 2026 / May 20, 2025 /
Oct 15, 2023, then Sep 03, 2026, Aug 25, Aug 15, Aug 07, 2026...) |
identity=individual ("Melynda Harrison - TravelingMel", travel writer/blogger)
| guide_date>=2024-09-16=N/A (no dated guides/itineraries shown; "Group Trips +
1:1 Planning" button and highlights "Group Trips", "Fave Gear", "Portfolio",
"About Us" — none dated) | verdict=PASS | notes=followers 34,975 >= 10K;
latest post Sep 3, 2026 within gate; individual creator. Flag: bio offers
"Group Trips + 1:1 Planning" travel-planning services — noted for coordinator
review, but identity reads as an individual creator.

### NOT attempted (rate limit returned at @tinboxtraveller)

@tinboxtraveller, @itsclaudiatravels, @the5worldexplorers, @boyeatsworld,
@ourfamilypassport, @aladyinlondon, @alexinwanderland, @wanderlustchloe,
@ilovenelz, @2summers, @wanderlust_himani, @gophari, @tanyakhanijow, @shivya,
@apytravelstories, @marcieinmommyland, @travelbabbo, @travelynnfamily,
@mumpacktravel — 19 handles, still UNVERIFIABLE.

### Guide/itinerary-date checks for the 3 partially-verified handles — NOT
attempted (rate limit returned before reaching them)

@globetotting | followers 19,729, latest post Aug 18, 2026, individual
(Katja Gaskell, travel writer) — from first attempt, unchanged. Guide date
STILL UNVERIFIABLE.

@ting_dalton | followers 14,718, latest post Jun 23, 2026, individual
(Ting Dalton, UK travel writer) — from first attempt, unchanged. Guide date
STILL UNVERIFIABLE.

@outsidesuburbia | followers 40,652, latest post Aug 28, 2026, individual
(Priya, bio mentions Itineraries/Travel guides) — from first attempt,
unchanged. Guide date STILL UNVERIFIABLE.

## Status changes vs first attempt (browser_verdicts_instagram.md)

- @ytravelblog: UNVERIFIABLE -> FAIL (couple operator)
- @fivefortheroadblog: UNVERIFIABLE -> PASS (20,267 followers; latest Aug 18, 2026; individual)
- @travelingmelmt: UNVERIFIABLE -> PASS (34,975 followers; latest Sep 03, 2026; individual)
- 19 handles: UNVERIFIABLE (unchanged)
- 3 partials: unchanged; guide dates still UNVERIFIABLE

## Tally

Retry verdicts: PASS 2 | FAIL 1 | still UNVERIFIABLE 19 | partials (guide date pending) 3.

Combined with the first attempt, browser-path coverage for Instagram is now:
PASS 2 (@fivefortheroadblog, @travelingmelmt), FAIL 1 (@ytravelblog), partial
3 (guide dates pending), UNVERIFIABLE 19.

Rate limit pattern: Instagram allowed ~4 anonymous profile loads per window;
window appears to clear in roughly 60-90 minutes. A later retry could cover the
remaining 19 + 3 guide checks, but no further retry is scheduled in this run —
the coordinator's desk-research fallback (verdicts file, "Next step" section)
covers the remainder per the work order's honest-evidence rule.
