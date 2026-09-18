#!/usr/bin/env python3
"""Wave-3 output for batch10 top-up (2026-09-17).
Builds 8 verified creator additions: batch10.csv rows (7 cols),
staging/selection_log_batch10.csv rows (23 cols), and itinerary JSON objects.
Parent performs the atomic append AFTER rebuilding dedup universe.
Canonical values per parent: decision 'include', selector 'batch10-topup', check_date '2026-09-17'.
No canonical files are touched by this script.
"""
import csv, io, json

SEL = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
       "followers_source","profile_url","discovery_source","identity_check","identity_method",
       "content_fit","content_fit_evidence","reach_floor","engagement_observed","activity_check",
       "purchase_intent","exclusions_check","decision","notes","check_date","selector"]

def sel(handle, name, niche, fapprox, fobs, activity_extra, identity_method, content_evidence,
        reach_floor, engagement, purchase_intent, exclusions, notes,
        identity_check="pass", content_fit="pass"):
    return ["10", handle, "tiktok", name, niche, fapprox, fobs,
            f"TikTok profile {handle}, observed 2026-09-17",
            f"https://www.tiktok.com/{handle}",
            "web discovery 2026-09-17",
            identity_check, identity_method,
            content_fit, content_evidence,
            reach_floor, engagement,
            f"pass — profile live 2026-09-17{activity_extra}",
            purchase_intent, exclusions,
            "include", notes, "2026-09-17", "batch10-topup"]

def csv_row(name, handle, niche, fapprox, urls):
    buf = io.StringIO()
    csv.writer(buf).writerow([name, handle, "tiktok", niche, fapprox,
                              f"https://www.tiktok.com/{handle}", ";".join(urls)])
    return buf.getvalue().rstrip("\r\n")

def item(day, item_type, name, details, location, price_hint=None):
    return {"day": day, "item_type": item_type, "name": name, "details": details,
            "location": location, "price_hint": price_hint, "booking_link": None}

ADD = []

# ---------------------------------------------------------------- 1. @kim_bulan4
u_kim = "https://www.tiktok.com/@kim_bulan4/video/7543998408571243796"
ADD.append({
 "batch10_csv_row": csv_row("Kim Bulan", "@kim_bulan4", "Bali travel", "62.4K", [u_kim]),
 "selection_log_row": sel(
   "@kim_bulan4", "Kim Bulan", "Bali travel", "62.4K", "62400",
   " (3.0M profile likes; 2,480 videos)",
   "profile nickname 'Kim Bulan' resolves to named individual",
   "Creator-owned one-day Ubud route (ATV Adventure, Pemulan Bali Coffee Plantation, "
   "Pura Tirta Empul, Food Monkey Legend, Fold), TikTok video 7543998408571243796 "
   "published 2025-08-29 (in window)",
   "pass — 62,400 >= 10,000",
   "74,400 plays; 2,363 likes; 115 comments; 1,032 shares; 2,102 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — affiliate discount codes; no planning/hosted-trip/agency service",
   "pass — affiliate codes only; no consumer trip planning/coaching, hosted group trips, "
   "or travel-agency booking identified (observed 2026-09-17)",
   "Full 5-venue day-1 item list extracted from creator-owned video; ready for canonical append."),
 "itinerary": {
  "handle": "@kim_bulan4", "platform": "tiktok",
  "notes": "One-day Ubud itinerary; 5 named venues extracted from creator-owned video.",
  "itineraries": [{
   "title": "One-day Ubud itinerary: ATV, coffee plantation, Tirta Empul, food stops",
   "destination": "Ubud, Bali", "country": "Indonesia", "days": 1, "confidence": "high",
   "summary": "Kim Bulan (@kim_bulan4) publishes a creator-owned one-day Ubud route "
              "(TikTok video 7543998408571243796, published 2025-08-29): ATV adventure, "
              "Pemulan Bali Coffee Plantation, Pura Tirta Empul, then Food Monkey Legend and Fold.",
   "guide_date": "2025-08-29",
   "engagement": {"plays": 74400, "likes": 2363, "comments": 115, "shares": 1032, "saves": 2102,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_kim],
   "items": [
    item(1, "activity", "ATV Adventure", "ATV ride, first stop on the creator's one-day Ubud route.", "Ubud, Bali, Indonesia"),
    item(1, "activity", "Pemulan Bali Coffee Plantation", "Coffee plantation visit, second stop on the creator's one-day Ubud route.", "Ubud, Bali, Indonesia"),
    item(1, "activity", "Pura Tirta Empul", "Temple visit, third stop on the creator's one-day Ubud route.", "Ubud, Bali, Indonesia"),
    item(1, "restaurant", "Food Monkey Legend", "Food stop on the creator's one-day Ubud route.", "Ubud, Bali, Indonesia"),
    item(1, "other", "Fold", "Final stop named in the creator's one-day Ubud route; venue type not verifiable from evidence, recorded as 'other'.", "Ubud, Bali, Indonesia"),
   ]}]},
})

# ---------------------------------------------------------------- 2. @vannytelly
u_van = "https://www.tiktok.com/@vannytelly/video/7585058634669903124"
ADD.append({
 "batch10_csv_row": csv_row("Vanny Tang", "@vannytelly", "Singapore-based travel (Vietnam)", "81.8K", [u_van]),
 "selection_log_row": sel(
   "@vannytelly", "Vanny Tang", "Singapore-based travel (Vietnam)", "81.8K", "81800",
   " (2.2M profile likes; guide video within window)",
   "named individual 'Vanny Tang', supported by 8days.sg and MoneySmartGirl references",
   "Creator-owned complete 6D5N Phu Quoc itinerary, TikTok video 7585058634669903124 "
   "published 2025-12-18 (in window)",
   "pass — 81,800 >= 10,000",
   "63,900 plays; 651 likes; 23 comments; 1,554 shares; 982 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — Klook affiliate promo code; no planning/hosted-trip/agency service",
   "pass — affiliate code only; no consumer trip planning/coaching, hosted group trips, "
   "or travel-agency booking identified (observed 2026-09-17)",
   "Latest profile open 2026-09-17 showed 81,800 followers (not 81,900); using 81,800. "
   "Full 14-item 6-day item list extracted; ready for canonical append."),
 "itinerary": {
  "handle": "@vannytelly", "platform": "tiktok",
  "notes": "Complete 6D5N Phu Quoc itinerary; 14 items extracted from creator-owned video.",
  "itineraries": [{
   "title": "6D5N Phu Quoc detailed itinerary",
   "destination": "Phu Quoc", "country": "Vietnam", "days": 6, "confidence": "high",
   "summary": "Vanny Tang (@vannytelly) publishes a creator-owned complete 6-day/5-night "
              "Phu Quoc itinerary (TikTok video 7585058634669903124, published 2025-12-18): "
              "Scoot arrival, Wyndham Grand Hotel, Vinpearl Safari, Grand World, VinWonders, "
              "island tour with snorkeling, and Dinh Cau Night Market.",
   "guide_date": "2025-12-18",
   "engagement": {"plays": 63900, "likes": 651, "comments": 23, "shares": 1554, "saves": 982,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_van],
   "items": [
    item(1, "flight", "Scoot flight to Phu Quoc", "Arrival flight named in the creator's 6D5N itinerary.", "Phu Quoc International Airport, Vietnam"),
    item(1, "transport", "Private complimentary transfer to hotel", "Airport-to-hotel transfer named in the itinerary.", "Phu Quoc, Vietnam"),
    item(1, "hotel", "Wyndham Grand Hotel", "Hotel check-in on day 1 of the itinerary.", "Phu Quoc, Vietnam"),
    item(1, "restaurant", "Nautilus Restaurant", "Hotel dinner on day 1.", "Wyndham Grand Hotel, Phu Quoc, Vietnam"),
    item(2, "activity", "Vinpearl Safari", "Safari park visit on day 2.", "Phu Quoc, Vietnam"),
    item(2, "activity", "Grand World — Teddy Bear Museum, Love Lake/Gondola, Bamboo Legend", "Grand World entertainment complex stops on day 2.", "Phu Quoc, Vietnam"),
    item(2, "activity", "The Quintessence of Vietnam show", "Evening show on day 2.", "Grand World, Phu Quoc, Vietnam"),
    item(3, "activity", "VinWonders — Typhoon World, Sea Shell aquarium, outdoor theme park, ONCE show", "Theme park day on day 3; ONCE show at 6:45pm.", "Phu Quoc, Vietnam"),
    item(4, "activity", "Phu Quoc Island Tour — May Rut, Gam Ghi snorkeling, sea walking, sea sports", "Island tour with snorkeling and sea sports on day 4; buffet lunch and cable car included in the creator's itinerary.", "Phu Quoc, Vietnam"),
    item(4, "activity", "SunWorld Hon Thom Island Water Park or Kiss Bridge", "Alternative day-4 stops named in the itinerary.", "Phu Quoc, Vietnam"),
    item(5, "activity", "Kids Club / Grand World massage / hotel pool and foam party", "Free-and-easy day 5; foam party at 4pm.", "Phu Quoc, Vietnam"),
    item(5, "restaurant", "Nha Hang Ganh Dau Cang", "Local Vietnamese seafood lunch on day 5.", "Phu Quoc, Vietnam"),
    item(5, "activity", "Dinh Cau Night Market", "Night market visit and dinner on day 5.", "Duong Dong, Phu Quoc, Vietnam"),
    item(6, "flight", "Return flight home", "Free-and-easy day 6, fly home.", "Phu Quoc International Airport, Vietnam"),
   ]}]},
})

# ---------------------------------------------------------------- 3. @somay.mekdi
u_som = "https://www.tiktok.com/@somay.mekdi/video/7624855363052997908"
ADD.append({
 "batch10_csv_row": csv_row("Jeje Jaelani", "@somay.mekdi", "Bandung travel (Indonesia)", "354.5K", [u_som]),
 "selection_log_row": sel(
   "@somay.mekdi", "Jeje Jaelani", "Bandung travel (Indonesia)", "354.5K", "354500",
   " (17.2M profile likes; guide video within window)",
   "named individual 'Jeje Jaelani'",
   "Creator-owned standalone one-day Bandung itinerary (self-contained despite 'Part.2' label), "
   "TikTok video 7624855363052997908, create_time 1775299989 = 2026-04-04 UTC (in window); "
   "five day-1 venues transcribed from the creator-owned video description: BMB Burger, "
   "The Deli Bakes Pudak, Sate Pak Hartono, Aksara Hotel, Tahu Priangan",
   "pass — 354,500 >= 10,000",
   "212,000 plays; 6,153 likes; 37 comments; 2,011 shares; 4,307 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — affiliate/product mentions; no planning service",
   "pass — brand/campaign contact email is not consumer trip planning; no hosted trips "
   "or agency booking identified (observed 2026-09-17)",
   "Day-1 venue names extracted from the creator-owned video description 2026-09-17; "
   "in-video order not verifiable from text evidence — all recorded as day 1. "
   "Ready for canonical append."),
 "itinerary": {
  "handle": "@somay.mekdi", "platform": "tiktok",
  "notes": "One-day Bandung itinerary; 5 venues transcribed from the creator-owned video description.",
  "itineraries": [{
   "title": "One-day Bandung itinerary (Part.2, self-contained)",
   "destination": "Bandung", "country": "Indonesia", "days": 1, "confidence": "high",
   "summary": "Jeje Jaelani (@somay.mekdi) publishes a creator-owned standalone one-day Bandung "
              "itinerary (TikTok video 7624855363052997908, labeled 'Part.2' but self-contained, "
              "create_time 1775299989 = 2026-04-04 UTC): BMB Burger, The Deli Bakes Pudak, "
              "Sate Pak Hartono, Aksara Hotel, Tahu Priangan.",
   "guide_date": "2026-04-04",
   "engagement": {"plays": 212000, "likes": 6153, "comments": 37, "shares": 2011, "saves": 4307,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_som],
   "items": [
    item(1, "restaurant", "BMB Burger", "Named in the creator's one-day Bandung route.", "Bandung, Indonesia"),
    item(1, "restaurant", "The Deli Bakes Pudak", "Named in the creator's one-day Bandung route.", "Bandung, Indonesia"),
    item(1, "restaurant", "Sate Pak Hartono", "Named in the creator's one-day Bandung route.", "Bandung, Indonesia"),
    item(1, "hotel", "Aksara Hotel", "Hotel named in the creator's one-day Bandung route.", "Bandung, Indonesia"),
    item(1, "restaurant", "Tahu Priangan", "Named in the creator's one-day Bandung route.", "Bandung, Indonesia"),
   ]}]},
})

# ---------------------------------------------------------------- 4. @viajaland
u_via = "https://www.tiktok.com/@viajaland/video/7640281987332279573"
ADD.append({
 "batch10_csv_row": csv_row("Alan Huitron", "@viajaland", "Peru budget travel", "386K", [u_via]),
 "selection_log_row": sel(
   "@viajaland", "Alan Huitron", "Peru budget travel", "386K", "386000",
   " (5.8M profile likes; 543 videos; guide video within window)",
   "named individual 'Alan Huitron' (profile nickname 'Viajaland - Alan Huitron')",
   "Creator-owned complete 3-day Tingo Maria route with per-activity Soles prices, "
   "TikTok video 7640281987332279573, create_time 1778891785 = 2026-05-16 UTC (in window)",
   "pass — 386,000 >= 10,000",
   "228,500 plays; 11,100 likes; 153 comments; 3,872 shares; 4,386 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — named hotel with room prices, named restaurants, transport prices; no affiliate codes observed",
   "pass — TikTok profile bio ('Viajes | Planes | Foodie | Lifestyle / Colaboraciones al DM') "
   "shows no consumer trip planning, coaching, hosted group trips, or agency booking "
   "(observed 2026-09-17). Profile links beacons.ai/alanhuitron — that link page could not be "
   "inspected this session (browser tool failure); parent may confirm it carries no planning/agency offer.",
   "Exclusions confirmed on the TikTok profile bio 2026-09-17; beacons link unchecked "
   "(browser block). Full 14-item 3-day item list extracted; ready for canonical append."),
 "itinerary": {
  "handle": "@viajaland", "platform": "tiktok",
  "notes": "3-day Tingo Maria itinerary with source-stated Soles prices; 14 items.",
  "itineraries": [{
   "title": "3-day Tingo Maria itinerary with full budget",
   "destination": "Tingo Maria", "country": "Peru", "days": 3, "confidence": "high",
   "summary": "Alan Huitron (@viajaland) publishes a creator-owned complete 3-day Tingo Maria "
              "route (TikTok video 7640281987332279573, create_time 1778891785 = 2026-05-16 UTC) "
              "with source-stated Soles prices: Hotel Kukama, Kotomono647, Cueva de las Lechuzas, "
              "Rio Monzon, waterfalls, caves, lagoons, and El Encanto de la Selva.",
   "guide_date": "2026-05-16",
   "engagement": {"plays": 228500, "likes": 11100, "comments": 153, "shares": 3872, "saves": 4386,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_via],
   "items": [
    item(1, "transport", "GM Internacional bus", "Bus to Tingo Maria, 12-hour trip.", "Tingo Maria, Peru", "from S/65"),
    item(1, "hotel", "Hotel Kukama", "Stay named in the itinerary; rooms include breakfast and views; rooftop restaurant Kotomono647 on the top floor.", "Tingo Maria, Peru", "rooms from S/100 per night for two people"),
    item(1, "restaurant", "Kotomono647", "Rooftop restaurant with author drinks and typical food.", "Hotel Kukama rooftop, Tingo Maria, Peru"),
    item(1, "activity", "Cueva de las Lechuzas", "Day 1 itinerary stop.", "Tingo Maria, Peru", "S/12"),
    item(1, "activity", "Paseo Extremo Rio Monzon", "Day 1 itinerary stop.", "Tingo Maria, Peru", "S/10"),
    item(1, "activity", "Roca Flotante", "Day 1 itinerary stop.", "Tingo Maria, Peru", "S/3"),
    item(1, "activity", "Mirador Jacintillo", "Day 1 itinerary stop.", "Tingo Maria, Peru", "S/0"),
    item(1, "activity", "Mirador Santa Cruz", "Day 1 itinerary stop.", "Tingo Maria, Peru", "S/0"),
    item(2, "activity", "Catarata Honolulu", "Day 2 itinerary stop.", "Tingo Maria, Peru", "S/5"),
    item(2, "activity", "Cueva 1000 encantos", "Day 2 itinerary stop.", "Tingo Maria, Peru", "S/5"),
    item(3, "activity", "Laguna de los Milagros", "Day 3 itinerary stop.", "Tingo Maria, Peru", "S/5"),
    item(3, "activity", "Laguna Mistica", "Day 3 itinerary stop.", "Tingo Maria, Peru", "S/5"),
    item(3, "activity", "Paddle", "Day 3 itinerary stop.", "Tingo Maria, Peru", "S/15"),
    item(None, "restaurant", "El Encanto de la Selva", "Lunch spot recommended in the itinerary; day not specified by creator.", "Tingo Maria, Peru"),
   ]}]},
})

# ---------------------------------------------------------------- 5. @marymatheustraveler
u_mar = "https://www.tiktok.com/@marymatheustraveler/video/7567550908217773343"
ADD.append({
 "batch10_csv_row": csv_row("Mary", "@marymatheustraveler", "Tennessee/US travel", "322.5K", [u_mar]),
 "selection_log_row": sel(
   "@marymatheustraveler", "Mary", "Tennessee/US travel", "322.5K", "322500",
   " (6.2M profile likes; 1,973 videos; guide video within window)",
   "named individual 'Mary'; full surname not conclusively established — canonical name kept as 'Mary'",
   "Creator-owned complete three-day Tennessee itinerary with named venues and source-stated "
   "prices, TikTok video 7567550908217773343, create_time 1761957759 = 2025-11-01 UTC "
   "(in window); day-by-day items transcribed from the creator-owned video caption",
   "pass — 322,500 >= 10,000",
   "947,000 plays; 37,600 likes; 236 comments; 29,000 shares; 23,439 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — named hotels and attractions with source-stated prices; no planning service observed",
   "pass — bio promotes travel tips/recommendations/itineraries; no consumer trip planning, "
   "coaching, hosted group trips, or agency booking identified (observed 2026-09-17)",
   "Day-1..3 items extracted from the creator-owned caption 2026-09-17; caption carries "
   "source-stated prices — exact per-venue figures not transcribed this session, parent may "
   "add them. Canonical name is 'Mary' (surname not established). Ready for canonical append."),
 "itinerary": {
  "handle": "@marymatheustraveler", "platform": "tiktok",
  "notes": "3-day Tennessee itinerary; items transcribed from the creator-owned caption; prices in caption not transcribed.",
  "itineraries": [{
   "title": "Three-day Tennessee itinerary: Gatlinburg, Pigeon Forge, Knoxville",
   "destination": "Tennessee (Gatlinburg, Pigeon Forge, Knoxville)", "country": "USA",
   "days": 3, "confidence": "high",
   "summary": "Mary (@marymatheustraveler) publishes a creator-owned three-day Tennessee itinerary "
              "(TikTok video 7567550908217773343, create_time 1761957759 = 2025-11-01 UTC) with "
              "named venues and source-stated prices. Day 1 Gatlinburg: Ober Mountain, downtown "
              "Gatlinburg, The Village Shops, a liquor shop at 643 Parkway, and the Howard Johnson "
              "by Wyndham Gatlinburg. Day 2 Pigeon Forge: Titanic Museum Attraction, Sunliner "
              "Diner, The Inn at Christmas Place, and The Island. Day 3 Knoxville: Ancient Lore Village.",
   "guide_date": "2025-11-01",
   "engagement": {"plays": 947000, "likes": 37600, "comments": 236, "shares": 29000, "saves": 23439,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_mar],
   "items": [
    item(1, "activity", "Ober Mountain", "Day 1 Gatlinburg stop.", "Gatlinburg, Tennessee, USA"),
    item(1, "other", "Downtown Gatlinburg", "Day 1 Gatlinburg stop.", "Gatlinburg, Tennessee, USA"),
    item(1, "other", "The Village Shops", "Day 1 Gatlinburg stop.", "Gatlinburg, Tennessee, USA"),
    item(1, "other", "Unnamed liquor shop (643 Parkway)", "Liquor shop at 643 Parkway named on day 1; shop name not given in caption.", "Gatlinburg, Tennessee, USA"),
    item(1, "hotel", "Howard Johnson by Wyndham Gatlinburg", "Hotel named on day 1.", "Gatlinburg, Tennessee, USA"),
    item(2, "activity", "Titanic Museum Attraction", "Day 2 Pigeon Forge stop.", "Pigeon Forge, Tennessee, USA"),
    item(2, "restaurant", "Sunliner Diner", "Day 2 Pigeon Forge stop.", "Pigeon Forge, Tennessee, USA"),
    item(2, "hotel", "The Inn at Christmas Place", "Hotel named on day 2.", "Pigeon Forge, Tennessee, USA"),
    item(2, "activity", "The Island", "Entertainment complex named on day 2.", "Pigeon Forge, Tennessee, USA"),
    item(3, "other", "Ancient Lore Village", "Day 3 Knoxville stop; venue type not verifiable from evidence, recorded as 'other'.", "Knoxville, Tennessee, USA"),
   ]}]},
})

# ---------------------------------------------------------------- 6. @sonhealtoviagens
u_son = "https://www.tiktok.com/@sonhealtoviagens/video/7609058815115382034"
ADD.append({
 "batch10_csv_row": csv_row("Mariana", "@sonhealtoviagens", "Brazil travel (Itacaré)", "501.9K", [u_son]),
 "selection_log_row": sel(
   "@sonhealtoviagens", "Mariana", "Brazil travel (Itacaré)", "501.9K", "501900",
   " (12.5M profile likes; 917 videos; guide video within window)",
   "named individual 'Mariana'; profile nickname 'Mariana | Sonhe Alto Viagens'; "
   "first-person singular bio indicates individual account",
   "Creator-owned complete six-day Itacaré itinerary, TikTok video 7609058815115382034, "
   "create_time 1771628400 = 2026-02-20 UTC (in window); day-by-day items transcribed "
   "from the creator-owned video caption",
   "pass — 501,900 >= 10,000",
   "16,500 plays; 953 likes; 41 comments; 158 shares; 178 saves "
   "(creator-owned video metrics, observed 2026-09-17)",
   "present — pre-made editorial guide products mentioned ('Meus guias de Paris, Londres e "
   "Japão e descontos'); editorial, not prohibited",
   "pass — 'my guides' indicates pre-made editorial products, not 1:1 consumer trip "
   "planning/coaching, hosted trips, or agency booking (decision recorded 2026-09-17). "
   "Linktree could not be fetched; no contents observed",
   "Day-1..6 items extracted from the creator-owned caption 2026-09-17; venue types not "
   "verifiable from caption evidence are recorded as 'other'. Ready for canonical append."),
 "itinerary": {
  "handle": "@sonhealtoviagens", "platform": "tiktok",
  "notes": "6-day Itacaré itinerary; items transcribed from the creator-owned caption.",
  "itineraries": [{
   "title": "Six-day Itacaré itinerary",
   "destination": "Itacaré", "country": "Brazil", "days": 6, "confidence": "high",
   "summary": "Mariana (@sonhealtoviagens) publishes a creator-owned complete six-day Itacaré "
              "itinerary (TikTok video 7609058815115382034, create_time 1771628400 = "
              "2026-02-20 UTC). Day 1: Aldeia do Mar, Uça, Praia da Concha, Hawaiian canoe, "
              "Saravá. Day 2: Resende/Tiririca/Costa/Ribeira beaches, treetop course, Tia Deth. "
              "Day 3: Rio de Contas boat trip, Villa Rosa cacao farm, Noré and Cleandro "
              "waterfalls, Auri, Ponta do Xaréu. Day 4: four-beach trail, Itacarezinho "
              "Restaurante, Café com Cacau. Day 5: Jeribucaçu, La Cabana, Jiló. Day 6: Prainha, "
              "Ilhéus, Serra Grande viewpoint.",
   "guide_date": "2026-02-20",
   "engagement": {"plays": 16500, "likes": 953, "comments": 41, "shares": 158, "saves": 178,
                  "source": "creator-owned video metrics, observed 2026-09-17"},
   "source_urls": [u_son],
   "items": [
    item(1, "other", "Aldeia do Mar", "Day 1 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(1, "other", "Uça", "Day 1 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(1, "activity", "Praia da Concha", "Day 1 beach stop.", "Itacaré, Brazil"),
    item(1, "activity", "Hawaiian canoe", "Day 1 activity.", "Itacaré, Brazil"),
    item(1, "other", "Saravá", "Day 1 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(2, "activity", "Resende, Tiririca, Costa and Ribeira beaches", "Day 2 beach stops.", "Itacaré, Brazil"),
    item(2, "activity", "Treetop course (arvorismo)", "Day 2 activity.", "Itacaré, Brazil"),
    item(2, "other", "Tia Deth", "Day 2 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(3, "activity", "Rio de Contas boat trip", "Day 3 activity.", "Itacaré, Brazil"),
    item(3, "activity", "Villa Rosa cacao farm", "Day 3 activity.", "Itacaré, Brazil"),
    item(3, "activity", "Noré waterfall", "Day 3 waterfall stop.", "Itacaré, Brazil"),
    item(3, "activity", "Cleandro waterfall", "Day 3 waterfall stop.", "Itacaré, Brazil"),
    item(3, "other", "Auri", "Day 3 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(3, "activity", "Ponta do Xaréu", "Day 3 stop.", "Itacaré, Brazil"),
    item(4, "activity", "Four-beach trail", "Day 4 activity.", "Itacaré, Brazil"),
    item(4, "restaurant", "Itacarezinho Restaurante", "Day 4 stop.", "Itacaré, Brazil"),
    item(4, "other", "Café com Cacau", "Day 4 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(5, "activity", "Jeribucaçu beach", "Day 5 beach stop.", "Itacaré, Brazil"),
    item(5, "other", "La Cabana", "Day 5 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(5, "other", "Jiló", "Day 5 stop; venue type not verifiable from evidence.", "Itacaré, Brazil"),
    item(6, "activity", "Prainha", "Day 6 beach stop.", "Itacaré, Brazil"),
    item(6, "activity", "Ilhéus", "Day 6 stop.", "Ilhéus, Brazil"),
    item(6, "activity", "Serra Grande viewpoint", "Day 6 stop.", "Serra Grande, Brazil"),
   ]}]},
})

# ---------------------------------------------------------------- 7. @valkengoedtravel
u_val = "https://www.tiktok.com/@valkengoedtravel/photo/7602549629825142049"
ADD.append({
 "batch10_csv_row": csv_row("Ishry van Valkengoed", "@valkengoedtravel", "Philippines travel", "13.1K", [u_val]),
 "selection_log_row": sel(
   "@valkengoedtravel", "Ishry van Valkengoed", "Philippines travel", "13.1K", "13100",
   " (102,300 profile likes; 535 videos; guide within window)",
   "named individual 'Ishry van Valkengoed'",
   "Creator-owned complete Philippines day sequence (Manila through Coron), TikTok photo "
   "carousel 7602549629825142049, TikTok-ID-derived date 2026-02-03 UTC (formula calibrated "
   "on 4 known create_time pairs; diffs within minutes; in window)",
   "pass — 13,100 >= 10,000",
   "10,700 likes; 137 comments (indexed third-party snapshot, observed 2026-09-17)",
   "present — not yet verifiable from carousel content without live view",
   "pass — no planning/hosted-trip/agency indicators observed (observed 2026-09-17)",
   "Profile follower count (13,100) per prior worker's live observation 2026-09-17; not "
   "re-opened this session (browser tool failure). Day sequence and engagement from dated "
   "public index of the creator-posted carousel; carousel slides were not viewable live, so "
   "confidence is medium and parent may confirm the displayed carousel date."),
 "itinerary": {
  "handle": "@valkengoedtravel", "platform": "tiktok",
  "notes": "20-day Philippines sequence from indexed creator-posted carousel; medium confidence (slides not live-viewed).",
  "itineraries": [{
   "title": "20-day Philippines itinerary: Manila to Coron",
   "destination": "Philippines (Manila, Bohol, Siquijor, Dumaguete, Moalboal, Boracay, El Nido, Coron)",
   "country": "Philippines", "days": 20, "confidence": "medium",
   "summary": "Ishry van Valkengoed (@valkengoedtravel) publishes a creator-owned 20-day Philippines "
              "itinerary as a photo carousel (TikTok photo 7602549629825142049, TikTok-ID-derived "
              "date 2026-02-03 UTC). Day 1 Manila. Days 2–3 Bohol: Loboc River, Alona Beach, "
              "Kawasan Falls, Chocolate Hills, tarsiers, sea of clouds. Days 4–5 Siquijor. Day 6 "
              "Dumaguete/Apo Island. Days 7–8 Moalboal. Days 9–11 Boracay. Days 12–15 El Nido. "
              "Days 16–20 Coron: Kayangan Lake, Barracuda Lake, Malcapuya Island, hot springs.",
   "guide_date": "2026-02-03",
   "engagement": {"likes": 10700, "comments": 137,
                  "source": "indexed third-party snapshot, observed 2026-09-17"},
   "source_urls": [u_val],
   "items": [
    item(1, "activity", "Manila", "Day 1: Manila.", "Manila, Philippines"),
    item(2, "activity", "Loboc River", "Days 2–3: Bohol.", "Bohol, Philippines"),
    item(2, "activity", "Alona Beach", "Days 2–3: Bohol.", "Bohol, Philippines"),
    item(2, "activity", "Kawasan Falls", "Days 2–3: Bohol region (as listed in the carousel).", "Philippines"),
    item(2, "activity", "Chocolate Hills", "Days 2–3: Bohol.", "Bohol, Philippines"),
    item(2, "activity", "Tarsiers", "Days 2–3: Bohol.", "Bohol, Philippines"),
    item(2, "activity", "Sea of clouds", "Days 2–3: Bohol.", "Bohol, Philippines"),
    item(4, "activity", "Siquijor", "Days 4–5: Siquijor.", "Siquijor, Philippines"),
    item(6, "activity", "Dumaguete / Apo Island", "Day 6: Dumaguete and Apo Island.", "Philippines"),
    item(7, "activity", "Moalboal", "Days 7–8: Moalboal.", "Cebu, Philippines"),
    item(9, "activity", "Boracay", "Days 9–11: Boracay.", "Boracay, Philippines"),
    item(12, "activity", "El Nido", "Days 12–15: El Nido.", "Palawan, Philippines"),
    item(16, "activity", "Kayangan Lake", "Days 16–20: Coron.", "Coron, Philippines"),
    item(16, "activity", "Barracuda Lake", "Days 16–20: Coron.", "Coron, Philippines"),
    item(16, "activity", "Malcapuya Island", "Days 16–20: Coron.", "Coron, Philippines"),
    item(16, "activity", "Hot springs", "Days 16–20: Coron.", "Coron, Philippines"),
   ]}]},
})

# ---------------------------------------------------------------- 8. @ginacwiklinski
u_gin_a = "https://www.tiktok.com/@ginacwiklinski/photo/7641692886282620168"
u_gin_r = "https://www.tiktok.com/@ginacwiklinski/photo/7606448536602856711"
ADD.append({
 "batch10_csv_row": csv_row("Gina", "@ginacwiklinski",
                            "Italy/France travel (Amalfi Coast, French Riviera)",
                            "19.0K", [u_gin_a, u_gin_r]),
 "selection_log_row": sel(
   "@ginacwiklinski", "Gina", "Italy/France travel (Amalfi Coast, French Riviera)",
   "19.0K", "19000",
   " (99,900 profile likes; 179 videos; both guides within window)",
   "named individual 'Gina'",
   "Creator-owned complete itinerary carousels: Amalfi Coast structured guide (Arienzo Beach "
   "Club, Positano old town, Luisa Positano, Franco's Bar, La Sponda at Le Sirenuse, Capri "
   "boat day, Da Vincenzo), TikTok photo 7641692886282620168, ID-derived 2026-05-19 UTC; "
   "five-day French Riviera itinerary (Nice; Antibes + Cannes/La Guérite; Èze + Monaco; "
   "Menton; boat day + Villefranche-sur-Mer/Paloma Beach), TikTok photo 7606448536602856711, "
   "ID-derived 2026-02-13 UTC — both in window",
   "pass — 19,000 >= 10,000",
   "Amalfi: 1,183 likes; 121 comments. Riviera: 732 likes; 28 comments "
   "(indexed third-party snapshots, observed 2026-09-17)",
   "present — partnership email only; no planning service observed",
   "pass — partnership email only; no consumer trip planning, coaching, hosted group "
   "trips, or agency booking identified (observed 2026-09-17)",
   "Two guides from indexed creator-posted carousels with full day-by-day captions; carousel "
   "slides were not viewable live (browser tool failure), confidence medium. Venue types not "
   "verifiable from evidence are recorded as 'other'. Dedup-checked 2026-09-17 — not present. "
   "Ready for canonical append."),
 "itinerary": {
  "handle": "@ginacwiklinski", "platform": "tiktok",
  "notes": "Two guides: Amalfi structured guide (no day numbering) + 5-day French Riviera.",
  "itineraries": [
   {
    "title": "Amalfi Coast structured guide",
    "destination": "Amalfi Coast", "country": "Italy", "days": None, "confidence": "medium",
    "summary": "Gina (@ginacwiklinski) publishes a creator-owned structured Amalfi Coast guide "
               "(TikTok photo carousel 7641692886282620168, TikTok-ID-derived date 2026-05-19 UTC) "
               "with named venues: Arienzo Beach Club, Positano old town, Luisa Positano, "
               "Franco's Bar, La Sponda at Le Sirenuse, a Capri boat day, and Da Vincenzo. "
               "No explicit day numbering is given in the indexed caption.",
    "guide_date": "2026-05-19",
    "engagement": {"likes": 1183, "comments": 121,
                   "source": "indexed third-party snapshot, observed 2026-09-17"},
    "source_urls": [u_gin_a],
    "items": [
     item(None, "activity", "Arienzo Beach Club", "Named in the creator's Amalfi Coast guide.", "Positano, Italy"),
     item(None, "activity", "Positano old town", "Named in the creator's Amalfi Coast guide.", "Positano, Italy"),
     item(None, "other", "Luisa Positano", "Named in the creator's Amalfi Coast guide; venue type not verifiable from evidence.", "Positano, Italy"),
     item(None, "restaurant", "Franco's Bar", "Named in the creator's Amalfi Coast guide.", "Positano, Italy"),
     item(None, "other", "La Sponda at Le Sirenuse", "Named in the creator's Amalfi Coast guide; venue type not verifiable from evidence.", "Positano, Italy"),
     item(None, "activity", "Capri boat day", "Boat day to Capri named in the creator's Amalfi Coast guide.", "Capri, Italy"),
     item(None, "other", "Da Vincenzo", "Named in the creator's Amalfi Coast guide; venue type not verifiable from evidence.", "Positano, Italy"),
    ],
   },
   {
    "title": "Five-day French Riviera itinerary",
    "destination": "French Riviera", "country": "France", "days": 5, "confidence": "medium",
    "summary": "Gina (@ginacwiklinski) publishes a creator-owned five-day French Riviera itinerary "
               "(TikTok photo carousel 7606448536602856711, TikTok-ID-derived date 2026-02-13 UTC). "
               "Day 1: Nice. Day 2: Antibes and Cannes/La Guérite. Day 3: Èze and Monaco. "
               "Day 4: Menton. Day 5: boat day and Villefranche-sur-Mer/Paloma Beach.",
    "guide_date": "2026-02-13",
    "engagement": {"likes": 732, "comments": 28,
                   "source": "indexed third-party snapshot, observed 2026-09-17"},
    "source_urls": [u_gin_r],
    "items": [
     item(1, "activity", "Nice", "Day 1.", "Nice, France"),
     item(2, "activity", "Antibes", "Day 2.", "Antibes, France"),
     item(2, "activity", "Cannes", "Day 2.", "Cannes, France"),
     item(2, "other", "La Guérite", "Day 2 stop; venue type not verifiable from evidence.", "Cannes, France"),
     item(3, "activity", "Èze", "Day 3.", "Èze, France"),
     item(3, "activity", "Monaco", "Day 3.", "Monaco"),
     item(4, "activity", "Menton", "Day 4.", "Menton, France"),
     item(5, "activity", "Boat day", "Day 5: boat day.", "French Riviera, France"),
     item(5, "activity", "Villefranche-sur-Mer", "Day 5.", "Villefranche-sur-Mer, France"),
     item(5, "activity", "Paloma Beach", "Day 5.", "Saint-Jean-Cap-Ferrat, France"),
    ],
   },
  ]},
})

out = {
 "_WARNING": "NOT CANONICAL — wave-3 output for the parent coordinator. Parent must rebuild "
             "the dedup universe and re-check all 8 handles immediately before the atomic append.",
 "batch": 10, "platform": "tiktok", "wave": 3, "date": "2026-09-17",
 "conversions": 8, "target_additions": 21, "shortfall_after_this_wave": 13,
 "additions": ADD,
}

p = "/home/hatch/workspace/travel-influencer-pilot/staging/WAVE3_batch10_output_2026-09-17.json"
with open(p, "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("wrote", p)

# ---- self-checks ----
assert all(len(a["selection_log_row"]) == 23 for a in ADD), "sel row cols"
csv_fields = 7
for a in ADD:
    assert a["batch10_csv_row"].count(",") >= csv_fields - 1
handles = [a["selection_log_row"][1] for a in ADD]
assert len(handles) == len(set(handles)) == 8
handles2 = [a["itinerary"]["handle"] for a in ADD]
assert handles == handles2, "handle alignment"
ITEM_TYPES = {"flight","hotel","activity","restaurant","transport","other"}
for a in ADD:
    for it in a["itinerary"]["itineraries"]:
        assert it["title"].strip() and it["destination"].strip() and it["summary"].strip()
        assert it["confidence"] in {"low","medium","high"}
        d = it["days"]; assert d is None or (isinstance(d, int) and d > 0)
        assert isinstance(it["source_urls"], list) and it["source_urls"]
        for it2 in it["items"]:
            assert it2["item_type"] in ITEM_TYPES, it2
print("self-checks OK: 8 creators, 23-col sel rows, aligned handles, valid item types")
