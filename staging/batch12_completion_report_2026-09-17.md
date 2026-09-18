# batch12 completion report — 2026-09-17

## Outcome
batch12 (tiktok) topped up from 22 → **25** creators across all three deliverables:

- `batch12.csv` — 25 rows, handles unique
- `staging/selection_log_batch12.csv` — 25 include rows, 23 columns each
- `staging/itineraries_batch12.json` — 25 extractions, 1 itinerary each, all source URLs present

## Added creators
| handle | name | followers (observed 2026-09-17) | qualifying TikTok itinerary | engagement |
|---|---|---|---|---|
| @renee.roaming | Renee Roaming | 412,400 | Yorkshire/Wuthering Heights 4-day itinerary (2 nights Haworth + 2 nights Dales), published 2026-02-14 | 44.5K plays, 3,135 likes, 1,207 saves, 451 shares |
| @taytakesatrip | Taylor | 38,800 | Traverse City 2025 vacation day-itinerary (Part 2), published 2025-04-24 | 44.9K plays, 1,409 likes, 824 saves, 438 shares |
| @tavernatravels | Taylor Taverna | 45,200 | Cape Kamui (Shakotan Coast, Hokkaido) day-trip guide, published 2025-08-24 | 243.1K plays, 10.7K likes, 6,802 saves, 2,750 shares |

Purchase intent: **present** for all three (@renee.roaming — Expedia booking disclosures + Expedia hotel picks in bio link; @taytakesatrip — sponsored Traverse City tourism AD with promoted bookable businesses; @tavernatravels — GetYourGuide tour promotion + blog affiliate links).
Exclusions: pass for all three — named individuals, no brands/agencies/couples/shared accounts, no personalized planning services or hosted group trips.

## Pre-write checks (all 2026-09-17)
- Case-insensitive dedup of all three handles vs `influencers.csv` + every `batch*.csv` → CLEAR (tavernatravels only present in the unassigned seed universe list).
- `validation/quarantine.json` grep for all three → no matches.
- All itinerary publish dates after 2024-09-17 (2026-02-14, 2025-04-24, 2025-08-24); follower evidence dated 2026-09-17 from direct TikTok profile opens.

## Gate 1
- `stage.json` temporarily scoped to `batches: [12]`; ran `validation/gate1_schema.py` → **GATE 1 [PASS] errors=0 warnings=30**.
- First run flagged 7 errors: item_type `attraction` is not in the allowed set (flight, hotel, activity, restaurant, transport, other). Fixed my 7 natural-spot items to `other` (matching pre-existing batch12 convention); all 30 warnings are pre-existing.
- `stage.json` restored byte-identically (SHA256 b1be0f44e1cb8e192f4d61891af1d5317e6f22f5d8d44eda2ea47c52051f23fa).

## Rejected / owned during this top-up
- Follower floor: @solofemalewanderer (0), @stephbetravel (331), @elevateditineraries (375).
- Already owned: @staysandgetaways (batch10), @emmaexpedition (batch3), @nessahuangg (batch13), @sivanstravels (batch14), @gokylahgo, @vitortrip, @lisarosanty, @jessieonajourney, @travelsofsarahfay, @wheretarawent, @happytowander, @pocketwanderings, @insidetravellab, @jayneytravels, @thetravelhack.
- Excluded: @fadastravel (customized itinerary planning service), @crisalynlove/@helloangelia (couple signals).
- Parked: @tongchristopher.travel (14K followers, CLEAR) — signature Taipei itinerary is from March 2024, no recent structured itinerary found.
