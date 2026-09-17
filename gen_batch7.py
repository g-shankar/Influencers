#!/usr/bin/env python3
"""Build Batch 7 deliverables: batch7.csv, staging/selection_batch7.csv,
staging/itineraries_batch7.json. Only the 5 fully-gated creators are included.
Shortfall vs 25 is reported, never padded."""
import csv, json, os

BASE = os.path.expanduser("~/workspace/travel-influencer-pilot")
CHECK = "2026-09-16"

creators = [
    dict(
        name="Tanya Khanijow", handle="@tanyakhanijow", niche="travel",
        followers_approx="1.5M", followers_observed="1.5M (Qoruz, Sep 2026); 1,047,532 (StarNgage)",
        followers_source="Qoruz; StarNgage",
        profile_url="https://www.instagram.com/tanyakhanijow/",
        discovery="web research",
        identity="pass — third-party directory corroboration (Qoruz, StarNgage)",
        content_fit="pass — creator-attributed structured itineraries dated 2026-08-18 (Singapore) and 2026-09-15 (Cinque Terre)",
        engagement="1.67% (Qoruz); 24.3K avg likes, 140 avg comments, 572.8K Reel views",
        activity="pass — Cinque Terre itinerary published 2026-09-15 (within 90d)",
        purchase="unknown",
        sources="https://qoruz.com/tanyakhanijow; https://starngage.com/plus/en-us/influencers/instagram/tanyakhanijow",
        notes="Both guides via Whosthat360 editorials summarizing her own published itineraries.",
    ),
    dict(
        name="Shivya Nath", handle="@shivya", niche="slow travel / sustainable travel",
        followers_approx=">130K", followers_observed=">130K Instagram followers",
        followers_source="Famous Birthdays",
        profile_url="https://www.instagram.com/shivya/",
        discovery="web research",
        identity="pass — own blog The Shooting Star (the-shooting-star.com) names her as author",
        content_fit="pass — own-blog structured 3-day Goa itinerary, updated ~2026-08-06",
        engagement="unknown (historical Forbes 2022-23 metrics exist but are stale; not represented as current)",
        activity="pass — own blog updated 2026-08-06; site also announces her 2026 book 'Rootless and Restless' (Penguin, 2026)",
        purchase="unknown",
        sources="https://the-shooting-star.com/perfect-3-day-goa-itinerary/; https://www.famousbirthdays.com/people/shivya-nath.html",
        notes="Engagement unknown as current; historical Forbes figures deliberately excluded.",
    ),
    dict(
        name="Apoorva Rao", handle="@apytravelstories", niche="travel",
        followers_approx="463.9K", followers_observed="463.9K (Qoruz, Sep 2026); 449.8K (Heepsy)",
        followers_source="Qoruz; Heepsy",
        profile_url="https://www.instagram.com/apytravelstories/",
        discovery="web research",
        identity="pass — third-party profile (Local Samosa) identifies her as Hyderabad travel blogger",
        content_fit="pass — her own YouTube Shorts: 3-day Phu Quoc (~2026-04-25) and 7-day Kerala (~2026-04-25) itineraries",
        engagement="1.48% (Qoruz); 1.9% (Heepsy); 6.9K avg likes, 137.1K Reel views",
        activity="pass — directory-reported posting recency 29.91 days (Heepsy)",
        purchase="unknown",
        sources="http://heepsy.com/instagram-profile/apytravelstories; https://www.youtube.com/shorts/haWUOIhreCg; https://www.youtube.com/shorts/RzkqlJVppEU",
        notes="Identity source: https://www.localsamosa.com/2020/12/22/meet-apoorva-rao-a-travel-blogger-from-hyderabad-who-loves-weaving-stories-of-places-she-has-visited/",
    ),
    dict(
        name="Jared Ruttenberg", handle="@jaredincpt", niche="travel photography / Cape Town",
        followers_approx="46.7K", followers_observed="46.7K followers",
        followers_source="Feedspot",
        profile_url="https://www.instagram.com/jaredincpt/",
        discovery="web research",
        identity="pass — own site jaredincpt.com; third-party listicle names him as Cape Town travel journalist/photographer",
        content_fit="pass — own-site structured destination guide 'Cape Town summer magic 2025' (title/URL/asset paths date it to 2025)",
        engagement="unknown",
        activity="pass — site international-travel archive updated ~6 days before check",
        purchase="unknown",
        sources="https://jaredincpt.com/cape-town-summer-magic-2025/",
        notes="Guide is structured by category rather than day-by-day; date evidenced by title, URL slug and Nov 2025 asset paths (no visible pub date).",
    ),
    dict(
        name="Aakanksha Monga", handle="@aakanksha.monga", niche="travel",
        followers_approx="1.4M", followers_observed="1.4M followers (Qoruz, crawled 2026-09-15)",
        followers_source="Qoruz",
        profile_url="https://www.instagram.com/aakanksha.monga/",
        discovery="web research",
        identity="pass — individual travel storyteller, Delhi; Qoruz profile + Harper's Bazaar; Forbes-featured",
        content_fit="pass — creator-attributed 10-day Philippines itinerary (updated 30 May 2025) and Tokyo guide (article crawled Sep 2026)",
        engagement="1.38% (Qoruz); 19.8K avg likes, 121 avg comments, 528.2K Reel views",
        activity="pass — Qoruz profile crawled 2026-09-15 shows active bio with Tokyo guide link and recent-post engagement metrics",
        purchase="unknown",
        sources="https://qoruz.com/aakanksha.monga/instagram; https://www.whosthat360.com/travel/philippines-travel-guide-a-10-day-adventure-for-indians-by-aakanksha-monga-8546177; https://www.whosthat360.com/travel/planning-tokyo-trip-follow-this-easy-itinerary-by-aakanksha-monga-11690742",
        notes="Itinerary content via Whosthat360 editorials summarizing her own Instagram posts/guides.",
    ),
]

# ---- batch7.csv ----
with open(os.path.join(BASE, "batch7.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "handle", "platform", "niche", "followers_approx", "profile_url", "source_urls"])
    for c in creators:
        w.writerow([c["name"], c["handle"], "instagram", c["niche"], c["followers_approx"], c["profile_url"], c["sources"]])

# ---- staging/selection_batch7.csv ----
sel_path = os.path.join(BASE, "staging", "selection_batch7.csv")
with open(sel_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["batch", "handle", "platform", "name", "niche", "followers_approx",
                "followers_observed", "followers_source", "profile_url", "discovery_source",
                "identity_check", "identity_method", "content_fit", "content_fit_evidence",
                "reach_floor", "engagement_observed", "activity_check", "purchase_intent",
                "exclusions_check", "decision", "notes", "check_date", "selector"])
    for c in creators:
        w.writerow([7, c["handle"], "instagram", c["name"], c["niche"], c["followers_approx"],
                    c["followers_observed"], c["followers_source"], c["profile_url"], c["discovery"],
                    c["identity"].split(" — ")[0], c["identity"].split(" — ", 1)[1],
                    c["content_fit"].split(" — ")[0], c["content_fit"].split(" — ", 1)[1],
                    "pass (>=10K cited/observed 2026-09-16)", c["engagement"],
                    c["activity"].split(" — ")[0], c["purchase"], "pass",
                    "include", c["notes"], CHECK, "batch7-worker"])

# ---- staging/itineraries_batch7.json ----
def item(day, itype, name, location, details, price=None, booking=None):
    return {"day": day, "item_type": itype, "name": name, "location": location,
            "details": details, "price_hint": price, "booking_link": booking}

extractions = [
    {
        "handle": "@tanyakhanijow",
        "itineraries": [
            {
                "title": "Singapore itinerary: top attractions, tips & hidden gems",
                "destination": "Singapore", "country": "Singapore", "days": None,
                "summary": "Tanya Khanijow's Singapore travel guide covering Marina Bay icons, cultural neighbourhoods (Chinatown, Little India, Kampong Glam/Haji Lane), Bugis Street shopping, Southern Ridges and Botanic Gardens, Marina Barrage sunsets, Sentosa/Universal Studios/Singapore Flyer (booked via Headout) and Changi Airport. Published via Whosthat360 ~2026-08-18; day-by-day breakdown not given, so items carry no day numbers.",
                "confidence": "medium",
                "source_urls": ["https://www.whosthat360.com/travel/tanya-khanijows-singapore-itinerary-top-attractions-tips-hidden-gems-10854816"],
                "items": [
                    item(None, "activity", "Marina Bay Sands SkyPark", "Singapore", "For sweeping skyline views."),
                    item(None, "activity", "Gardens by the Bay", "Singapore", "Free to explore with a few ticketed attractions."),
                    item(None, "activity", "Chinatown", "Singapore", "Cultural neighbourhood with distinct cultural flavours."),
                    item(None, "activity", "Little India", "Singapore", "Cultural neighbourhood with distinct cultural flavours."),
                    item(None, "activity", "Kampong Glam and Haji Lane", "Singapore", "Cultural neighbourhoods with distinct cultural flavours."),
                    item(None, "other", "Bugis Street", "Singapore", "Street shopping."),
                    item(None, "activity", "Southern Ridges", "Singapore", "Lush outdoor experience."),
                    item(None, "activity", "Singapore Botanic Gardens", "Singapore", "Lush outdoor experience."),
                    item(None, "activity", "Marina Barrage", "Singapore", "Stunning sunset skyline views."),
                    item(None, "activity", "Sentosa Island", "Singapore", "Booked through Headout using combo offers and discounts."),
                    item(None, "activity", "Universal Studios", "Sentosa, Singapore", "Booked through Headout using combo offers and discounts."),
                    item(None, "activity", "Singapore Flyer", "Singapore", "Booked through Headout using combo offers and discounts."),
                    item(None, "other", "Changi Airport", "Singapore", "Award-winning airport; booked through Headout combo offers."),
                ],
            },
            {
                "title": "Cinque Terre 3-4 day itinerary",
                "destination": "Cinque Terre", "country": "Italy", "days": None,
                "summary": "Tanya Khanijow's 3-4 day Cinque Terre plan: explore one or two villages per day (Riomaggiore, Manarola, Corniglia, Vernazza, Monterosso) combining sightseeing, cafe hopping, beach time and short hikes; evenings for sunset views and seaside dining. September named best month; mid-range cost from India estimated at INR 1-1.2 lakh per person (Schengen visa ~INR 9,000; return flights to Rome INR 35,000-40,000; train INR 2,750-3,000; accommodation 3-4 days INR 35,000-40,000). Published via Whosthat360 ~2026-09-15. Items carry no day numbers because the source gives no day-by-day mapping.",
                "confidence": "medium",
                "source_urls": ["https://www.whosthat360.com/travel/planning-a-cinque-terre-trip-tanya-khanijow-shares-the-perfect-4-day-italy-itinerary-11585313"],
                "items": [
                    item(None, "activity", "Riomaggiore", "Cinque Terre, Italy", "One of the five villages; colourful cliffside houses and narrow alleyways."),
                    item(None, "activity", "Manarola", "Cinque Terre, Italy", "One of the five villages, each with a distinct atmosphere."),
                    item(None, "activity", "Corniglia", "Cinque Terre, Italy", "One of the five villages, each with a distinct atmosphere."),
                    item(None, "activity", "Vernazza", "Cinque Terre, Italy", "One of the five villages, each with a distinct atmosphere."),
                    item(None, "activity", "Monterosso", "Cinque Terre, Italy", "One of the five villages; Monterosso Beach is the most popular sandy stretch."),
                    item(None, "activity", "Monterosso Beach", "Monterosso, Italy", "Most popular sandy stretch, perfect for leisurely sunbathing."),
                    item(None, "activity", "Guvano Beach", "Cinque Terre, Italy", "More secluded vibe, a quieter escape."),
                    item(None, "activity", "Sentiero Azzurro (Blue Trail)", "Cinque Terre, Italy", "Iconic coastal hiking route connecting the villages through coastal paths, hills and cliffs."),
                    item(None, "flight", "Return flights to Rome", "India to Rome, Italy", "Mid-range estimate for the trip.", "INR 35,000-40,000"),
                    item(None, "transport", "Train to Cinque Terre", "Rome to Cinque Terre, Italy", "Rail leg to the coast.", "INR 2,750-3,000"),
                    item(None, "hotel", "Accommodation (3-4 days)", "Cinque Terre, Italy", "Mid-range accommodation estimate for the stay.", "INR 35,000-40,000"),
                    item(None, "other", "Schengen visa", "India", "Visa cost component of the estimate.", "approx. INR 9,000"),
                ],
            },
        ],
    },
    {
        "handle": "@shivya",
        "itineraries": [
            {
                "title": "Perfect 3-Day Goa Itinerary for Slow Travel",
                "destination": "Goa", "country": "India", "days": 3,
                "summary": "Shivya Nath's own-blog 3-day slow-travel Goa plan, updated ~2026-08-06. North Goa: Day 1 — explore the Goan neighbourhood (walks, bakery, market), cycle/e-bike Chorao island with Cycling Zens or B:Live, thrift at Good Karma (Vagator), shop organic fair-trade at No Nasties (Assagao). Day 2 — hike to a secret waterfall/swimming hole with Beatroute Explorers or The Local Beat. Day 3 — surfing lesson with Salty Soul (Mandrem), lazy beach day at Morjim/Ashwem/Keri. Stay picks: Cancio's House (Aldona), Siolim House, Jardin d'Ulysse, Botanique, Mojigao, The Secret Garden; South Goa: Casa Jaali, Tanshikar Spice Farm, Mangaal Farmstay, Cabo Serai, Alila Diwa. Eat: Kokni Kanteen, Mum's Kitchen (Panjim), Bloom & Brew, The Rice Mill, Bean Me Up, Moka.",
                "confidence": "high",
                "source_urls": ["https://the-shooting-star.com/perfect-3-day-goa-itinerary/"],
                "items": [
                    item(1, "hotel", "Cancio's House", "Aldona, Goa, India", "500-year-old traditional Goan homestay hosted by three generations of the Amaral family; outhouse cottage."),
                    item(1, "activity", "Cycle or e-bike on Chorao island", "Chorao, Goa, India", "Guided cycling or e-biking ride with Cycling Zens or B:Live; mangroves, paddy fields, old houses."),
                    item(1, "other", "Good Karma thrift store", "Vagator, Goa, India", "Pre-loved clothes, accessories, shoes and books; profits partly to WAG."),
                    item(1, "other", "No Nasties", "Assagao, Goa, India", "Homegrown organic fair-trade clothing store."),
                    item(1, "restaurant", "Kokni Kanteen", "Goa, India", "True blue Goan thali; good starting point for Goan food."),
                    item(1, "restaurant", "Mum's Kitchen", "Panjim, Goa, India", "Favourite Goan restaurant (avoid the Assagao branch); uddamethi and tamdi bhaji with sanna."),
                    item(1, "restaurant", "Bloom & Brew", "Assagao, Goa, India", "Vegan-friendly cafe favourite."),
                    item(1, "restaurant", "The Rice Mill", "Morjim, Goa, India", "Vegan-friendly cafe favourite."),
                    item(1, "restaurant", "Bean Me Up", "Vagator, Goa, India", "Vegan-friendly cafe favourite."),
                    item(1, "restaurant", "Moka", "Siolim, Goa, India", "Vegan-friendly cafe favourite."),
                    item(2, "activity", "Hike to a secret waterfall or swimming hole", "Western Ghats, Goa, India", "Forest hike and swim with Beatroute Explorers or The Local Beat; homemade lunch with a local family."),
                    item(3, "activity", "Surf lesson with Salty Soul", "Mandrem, Goa, India", "Surf lesson run by two Goan surfers; gentle waves, good for beginners."),
                    item(3, "activity", "Lazy beach day", "Morjim/Ashwem/Keri, Goa, India", "Sun, sand and sunset evening on North Goa beaches."),
                    item(None, "hotel", "Siolim House", "Siolim, Goa, India", "Restored 17th century heritage house turned boutique hotel."),
                    item(None, "hotel", "Jardin d'Ulysse", "Morjim, Goa, India", "Across the beach from Morjim; vegan-friendly food; huts out back."),
                    item(None, "hotel", "Botanique", "Assagao, Goa, India", "Restored Goan house hotel; Japanese food at Izumi in its backyard."),
                    item(None, "hotel", "Mojigao", "Assagao, Goa, India", "Wood and tiled roof cottages in Assagao wilderness; cafe, yoga, music gigs."),
                    item(None, "hotel", "The Secret Garden", "Saligao, Goa, India", "Traditional Goan house refurbished by a Goan-British couple; food forest."),
                    item(None, "hotel", "Casa Jaali", "Patnem, Goa, India", "Cottages overlooking the coast; vegan-friendly in-house cafe."),
                    item(None, "hotel", "Tanshikar Spice Farm", "Sanguem, Goa, India", "Working family-run organic farm; huts among cashew and black pepper plantations."),
                    item(None, "hotel", "Mangaal Farmstay", "Quepem, Goa, India", "Working organic farm; private waterfall 1.5 hour trek away."),
                    item(None, "hotel", "Cabo Serai", "Canacona, Goa, India", "Eco-lodge near Cabo de Rama Fort, accessible by short hike; pinewood and thatched huts."),
                    item(None, "hotel", "Alila Diwa", "Majorda, Goa, India", "Luxury resort with Balinese/Goan architecture; infinity pool over rice paddies."),
                ],
            },
        ],
    },
    {
        "handle": "@apytravelstories",
        "itineraries": [
            {
                "title": "3-Day Phu Quoc Itinerary",
                "destination": "Phu Quoc", "country": "Vietnam", "days": 3,
                "summary": "Apoorva Rao's own 3-day Phu Quoc island itinerary from her YouTube Short description (~2026-04-25): Day 1 — VinWonders, Starfish Beach. Day 2 — Venice Canal boat ride at Grand World, Phu Quoc Night Market. Day 3 — world's longest sea cable car, Sun World plus beach time. Best time to visit: November to April.",
                "confidence": "high",
                "source_urls": ["https://www.youtube.com/shorts/haWUOIhreCg"],
                "items": [
                    item(1, "activity", "VinWonders", "Phu Quoc, Vietnam", "Nonstop fun theme park."),
                    item(1, "activity", "Starfish Beach", "Phu Quoc, Vietnam", "Crystal-clear waters."),
                    item(2, "activity", "Venice Canal boat ride at Grand World", "Phu Quoc, Vietnam", "Canal boat ride at Grand World."),
                    item(2, "restaurant", "Phu Quoc Night Market", "Phu Quoc, Vietnam", "Food and vibes at the night market."),
                    item(3, "activity", "World's longest sea cable car", "Phu Quoc, Vietnam", "Sea cable car ride."),
                    item(3, "activity", "Sun World + beach time", "Phu Quoc, Vietnam", "Sun World park and beach time."),
                ],
            },
            {
                "title": "7 Day Kerala Itinerary",
                "destination": "Kerala", "country": "India", "days": 7,
                "summary": "Apoorva Rao's 7-day Kerala itinerary, published as her own YouTube Short (~2026-04-25). The Short's metadata confirms the 7-day Kerala itinerary exists; day-by-day item detail lives in the video itself and was not extractable from the text page. Item list left empty rather than invented.",
                "confidence": "medium",
                "source_urls": ["https://www.youtube.com/shorts/RzkqlJVppEU"],
                "items": [],
            },
        ],
    },
    {
        "handle": "@jaredincpt",
        "itineraries": [
            {
                "title": "Cape Town summer magic 2025",
                "destination": "Cape Town", "country": "South Africa", "days": None,
                "summary": "Jared Ruttenberg's own-site structured seasonal destination guide (2025): curated Cape Town summer recommendations spanning dining, spa, adventure, wine tasting and villa stay. Not day-by-day; items carry no day numbers. Date evidenced by title, URL slug and Nov 2025 asset paths; no visible publication date on the page.",
                "confidence": "medium",
                "source_urls": ["https://jaredincpt.com/cape-town-summer-magic-2025/"],
                "items": [
                    item(None, "restaurant", "Terrarium Restaurant", "Cape Town, South Africa", "Featured dining recommendation in the summer guide."),
                    item(None, "activity", "Westin Heavenly Spa", "Cape Town, South Africa", "Featured spa recommendation in the summer guide."),
                    item(None, "activity", "Cape Kayak Adventures", "Cape Town, South Africa", "Featured kayak adventure recommendation in the summer guide."),
                    item(None, "activity", "Steenberg wine tasting", "Steenberg, Cape Town, South Africa", "Featured wine tasting recommendation in the summer guide."),
                    item(None, "hotel", "Spindrift Villa", "Cape Town, South Africa", "Featured villa stay recommendation in the summer guide."),
                ],
            },
        ],
    },
    {
        "handle": "@aakanksha.monga",
        "itineraries": [
            {
                "title": "10-Day Philippines Itinerary",
                "destination": "Philippines", "country": "Philippines", "days": 10,
                "summary": "Aakanksha Monga's 10-day Philippines itinerary (updated 30 May 2025, via Whosthat360 summarizing her own Instagram post): Day 1 — land in Cebu (cheap flights, buzzing vibes). Day 2-3 — Moalboal: sardine swim, waterfalls, Casino Hill sunsets; skip Oslob (unethical shark swimming). Day 4 — fly to Coron: hike for epic sunsets, local markets. Day 5-7 — island-hop Coron to El Nido: secret beaches, turquoise lagoons, WWII shipwreck snorkels. Day 8 — chill in El Nido: sun, surf, party. Day 9 — Puerto Princesa: UNESCO heritage cave, then fly to Manila. Day 10 — explore Manila: shop, eat, hidden speakeasies. Sustainable travel tips, local food, hidden spots and budget hacks throughout.",
                "confidence": "medium",
                "source_urls": ["https://www.whosthat360.com/travel/philippines-travel-guide-a-10-day-adventure-for-indians-by-aakanksha-monga-8546177"],
                "items": [
                    item(1, "flight", "Cheap flights to Cebu", "India to Cebu, Philippines", "Cheap flights as the starting point; buzzing vibes."),
                    item(2, "activity", "Sardine swim and waterfalls", "Moalboal, Cebu, Philippines", "Swim with sardines, chase waterfalls."),
                    item(3, "activity", "Casino Hill sunsets", "Moalboal, Cebu, Philippines", "Sunset viewpoint in Moalboal."),
                    item(4, "flight", "Fly to Coron", "Cebu to Coron, Philippines", "Domestic flight leg."),
                    item(4, "activity", "Hike for epic sunsets and local markets", "Coron, Philippines", "Sunset hike and explore local markets."),
                    item(5, "activity", "Island-hopping from Coron to El Nido", "Coron to El Nido, Philippines", "Secret beaches, turquoise lagoons, WWII shipwreck snorkels."),
                    item(8, "activity", "Chill in El Nido", "El Nido, Philippines", "Sun, surf and party like a local."),
                    item(9, "activity", "UNESCO heritage cave", "Puerto Princesa, Philippines", "Visit the UNESCO heritage cave."),
                    item(9, "flight", "Fly to Manila", "Puerto Princesa to Manila, Philippines", "Domestic flight leg."),
                    item(10, "other", "Explore Manila", "Manila, Philippines", "Shop, eat well, find the city's hidden speakeasies."),
                ],
            },
            {
                "title": "Tokyo 3-5 day itinerary",
                "destination": "Tokyo", "country": "Japan", "days": None,
                "summary": "Aakanksha Monga's Tokyo guide (Whosthat360 article crawled Sep 2026; no byline date displayed): practical plan — Day 1 central neighbourhoods and local streets/food; Day 2 cultural landmarks, temples, traditional experiences; Day 3 shopping districts and modern attractions; optional extension into quieter neighbourhoods, parks and hidden cafes. Tips: prepaid travel card, station coin lockers, October as ideal month, tipping not customary. Item list reflects the described day structure; no booking links or prices given in the source.",
                "confidence": "medium",
                "source_urls": ["https://www.whosthat360.com/travel/planning-tokyo-trip-follow-this-easy-itinerary-by-aakanksha-monga-11690742"],
                "items": [
                    item(1, "activity", "Central neighbourhoods exploration", "Tokyo, Japan", "Explore central neighbourhoods, local streets and food spots; get familiar with the city."),
                    item(2, "activity", "Cultural landmarks and temples", "Tokyo, Japan", "Cultural landmarks, temples and traditional experiences."),
                    item(3, "activity", "Shopping districts and modern attractions", "Tokyo, Japan", "Shopping districts and modern attractions."),
                    item(None, "other", "Quieter neighbourhoods, parks and hidden cafes", "Tokyo, Japan", "Optional extension for longer stays; area-focused days reduce travel fatigue."),
                ],
            },
        ],
    },
]

doc = {"batch": 7, "extractions": extractions}
with open(os.path.join(BASE, "staging", "itineraries_batch7.json"), "w") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print("wrote 3 files")
