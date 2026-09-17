#!/usr/bin/env python3
"""Stage 1 remediation pass 2026-09-16: replace weak/empty extractions with
evidence-backed records found in 2026-09-16 web research. Backs up originals.
Unknowns stay unknown: item detail not evidenced is NOT invented."""
import json, csv, shutil, os, copy
from datetime import datetime, timezone

BASE = os.path.expanduser('~/workspace/travel-influencer-pilot/staging')
REP = os.path.expanduser('~/workspace/travel-influencer-pilot/validation/reports')

def ttd(vid):
    return datetime.fromtimestamp(vid >> 32, timezone.utc).strftime('%Y-%m-%d')

def load_batch(b):
    p = os.path.join(BASE, f'itineraries_batch{b}.json')
    bak = os.path.join(BASE, f'_archive_partials/itineraries_batch{b}.json.pre_remediation_2026-09-16')
    shutil.copy2(p, bak)
    return p, json.load(open(p))

def find(ex_list, handle):
    for i, ex in enumerate(ex_list):
        if ex['handle'].lower() == handle.lower():
            return i, ex
    return None, None

def save(p, data):
    json.dump(data, open(p, 'w'), indent=1, ensure_ascii=False)

def item(day, name, location, details, item_type='activity'):
    return {'day': day, 'item_type': item_type, 'name': name,
            'location': location, 'details': details}

REM = 'REMEDIATED 2026-09-16: evidence-backed extraction replaced the prior weak/empty record. See validation/reports/stage1_remediation_2026-09-16.json.'

# ---------------- BATCH 5 ----------------
p, d = load_batch(5)
ex = d['extractions']

# @heroiisa — Costa Brava 4-day (video 7595629165072764191 -> 2026-01-15, indexed caption = 2nd signal)
i, rec = find(ex, '@heroiisa')
rec['itineraries'] = [{
 'title': 'Steal my 4-day Costa Brava itinerary',
 'destination': 'Costa Brava, Spain', 'country': 'Spain', 'days': 4,
 'items': [
  item(1, 'Train Barcelona to Girona (38 min)', 'Girona, Spain',
       'Transfer day: train Barcelona to Girona (38 min); explore Girona; bus Girona to Palafrugell (1h10); check into hotel and explore Palafrugell.'),
  item(2, 'Walk Palafrugell to Calella de Palafrugell (50 min)', 'Calella de Palafrugell, Spain',
       'Explore Calella de Palafrugell; walk to El Golfet via Cami de Ronda (30 min); walk back via Calella (1h30); bus to Begur (15 min); check in and explore Begur.'),
  item(3, 'Cami de Ronda coves walk', 'Begur, Spain',
       'Walk to Cami de Ronda (30 min); Platja Fonda; Cala Malaret; Platja d\'Aiguablava; walk back to Begur (60 min).'),
  item(4, 'Illa Roja and Sa Tuna coves; return to Barcelona', 'Begur / Barcelona, Spain',
       'Walk to Platja de l\'Illa Roja (60 min); Cami de Ronda to Platja de Sa Riera, Cala Aiguafreda, Cala Sa Tuna; walk back to Begur (50 min); bus Begur to Barcelona (2h35); arrive Barcelona ~6pm.'),
 ],
 'source_urls': ['https://www.tiktok.com/@heroiisa/video/7595629165072764191'],
 'summary': 'Day-by-day 4-day Costa Brava itinerary with times and transport: Girona, Palafrugell, Calella de Palafrugell, El Golfet, Begur and Cami de Ronda coves (Platja Fonda, Cala Malaret, Aiguablava, Illa Roja, Sa Riera, Sa Tuna). Guide date 2026-01-15 (video-ID decode) corroborated by the indexed exact-handle caption. A second exact-handle guide video (7611191365967432991, 2026-02-26) is also indexed.',
 'confidence': 'high'}]
rec['notes'] = REM

# @letravelstyle — California 10-day road trip (creator-owned blog, updated Sept 2026)
i, rec = find(ex, '@letravelstyle')
rec['itineraries'] = [{
 'title': 'The Ultimate 10 Days in California Road Trip Itinerary',
 'destination': 'California, USA', 'country': 'USA', 'days': 10,
 'items': [
  item(1, 'San Diego: Balboa Park, Little Italy, Seaport Village', 'San Diego, USA',
       'Balboa Park; Little Italy (Morning Glory brunch); Seaport Village; USS Midway; Sunset Cliffs.'),
  item(2, 'San Diego: Zoo, Coronado, La Jolla', 'San Diego, USA',
       'San Diego Zoo; Coronado; La Jolla (La Jolla Cove, Scripps Coastal Meander, Torrey Pines Gliderport).'),
  item(3, 'Los Angeles: Griffith, Hollywood, Beverly Hills', 'Los Angeles, USA',
       'Griffith Observatory; Hollywood Sign (Lake Hollywood Park); Beverly Hills (Rodeo Drive).'),
  item(4, 'Los Angeles: Malibu', 'Malibu, USA', 'Malibu (El Matador State Beach, Malibu Pier).'),
  item(5, 'Santa Barbara', 'Santa Barbara, USA', 'Santa Barbara day stop on the coast route north.'),
  item(6, 'Big Sur', 'Big Sur, USA', 'Big Sur coastal drive day.'),
  item(7, 'Carmel-by-the-Sea and Monterey', 'Monterey, USA', 'Carmel-by-the-Sea and Monterey.'),
  item(8, 'Yosemite (day 1)', 'Yosemite, USA', 'Yosemite National Park, first of two days.'),
  item(9, 'Yosemite (day 2)', 'Yosemite, USA', 'Yosemite National Park, second day.'),
  item(10, 'San Francisco', 'San Francisco, USA', 'Finish in San Francisco.'),
 ],
 'source_urls': ['https://letravelstyle.com/california-road-trip-itinerary-10-days/'],
 'summary': 'Creator-owned 10-day California road-trip itinerary: San Diego (2d), Los Angeles (2d), Santa Barbara, Big Sur, Carmel/Monterey, Yosemite (2d), San Francisco. Page updated ~2026-09-03 per search index. Creator identified as Courtney Delfino (travel writer) via creator-owned about page; 153.5K Instagram followers per Heepsy (2026-09-16).',
 'confidence': 'high'}]
rec['notes'] = REM

# @vitortrip — full London 3-day items from indexed caption (video 7600316183270722838 -> 2026-01-28)
i, rec = find(ex, '@vitortrip')
london = {
 'title': 'London 3-Day Itinerary (routes + prices + insider tips)',
 'destination': 'London, UK', 'country': 'UK', 'days': 3,
 'items': [
  item(1, 'Day 1 Royal Vibes: London Eye, Big Ben, Westminster Abbey', 'London, UK',
       'London Eye (walk the capsule for 360 views); Big Ben (St Thomas Hospital side for photos); Westminster Abbey (900-year-old Oldest Door); Buckingham Palace (stamp ticket = 1-year pass); Horse Guards (4pm Dismounting Ceremony); National Gallery (Room 43, Van Gogh Sunflowers); Leicester Sq (TKTS half-price theatre); Shaftesbury Fountain; Carnaby St; Oxford St (Selfridges rooftop bar).'),
  item(2, 'Day 2 Skylines & History', 'London, UK',
       'Tate Modern (10th-floor Blavatnik terrace, free); Borough Market; The Shard (drink at Aqua Shard instead of paying for the view); Tower Bridge (check lift times); Tower of London (Crown Jewels first); St. Dunstan in the East; Sky Garden (tickets drop Monday mornings); Leadenhall Market (Diagon Alley entrance); St. Paul\'s (Golden Gallery climb).'),
  item(3, 'Day 3 Color & Culture', 'London, UK',
       'British Museum (Parthenon Marbles quieter than Rosetta Stone); Neal\'s Yard (go before 10am for crowd-free photos). Caption truncated in index after Day 3 opening.'),
 ],
 'source_urls': ['https://www.tiktok.com/@vitortrip/photo/7600316183270722838'],
 'summary': 'Three-day London itinerary with mapped routes, prices and an insider tip per spot. Guide date 2026-01-28 (video-ID decode) corroborated by the indexed exact-handle caption (58.9K-85.7K likes across indexed versions).',
 'confidence': 'high'}
rec['itineraries'] = [london] + [x for x in rec['itineraries'] if 'London' not in x.get('title','')]
rec['notes'] = 'REMEDIATED 2026-09-16: London guide strengthened with full stop-level items from the indexed exact-handle caption; two-signal date 2026-01-28.'

# @sheyhernandez96 — keep Chicago record, add two-signal audit note
i, rec = find(ex, '@sheyhernandez96')
rec['notes'] = 'Two-signal date confirmed 2026-09-16: video 7603593031815580941 decodes to 2026-02-06; indexed exact-handle caption corroborates. 9-stop Chicago photo guide; indexed engagement 11.9K-20.2K likes.'

# @lexxhidalgo — 5-day California series (video 7648002741138148621 -> 2026-06-05, oEmbed = 2nd signal)
i, rec = find(ex, '@lexxhidalgo')
rec['itineraries'] = [{
 'title': '5-day California road trip series',
 'destination': 'California, USA', 'country': 'USA', 'days': 5,
 'items': [
  item(2, 'Day 2: Morro Bay, Carmel, Big Sur', 'Central Coast, USA',
       'Day-two leg of the 5-day California road-trip series: Morro Bay, Carmel, Big Sur. All five day-itineraries were posted the same day; stops for days 1, 3, 4 and 5 were not captured in indexed evidence and are not invented here.'),
 ],
 'source_urls': ['https://www.tiktok.com/@lexxhidalgo/video/7648002741138148621'],
 'summary': 'Five-day California road-trip itinerary series ("DAY TWO ITINERARY!!! (posting all 5 today)"). Guide date 2026-06-05 (video-ID decode) corroborated by TikTok oEmbed data. Creator: Lexi Hidalgo; 2.7M TikTok / 815K Instagram followers per official Singapore Tourism Board 2026 KOL document.',
 'confidence': 'medium'}]
rec['notes'] = REM

# @chubbydiaries — Sonoma 72-hour food itinerary (structure verified, item detail not captured)
i, rec = find(ex, '@chubbydiaries')
rec['itineraries'] = [{
 'title': 'Everything I ate in Sonoma County in 72 hours',
 'destination': 'Sonoma County, USA', 'country': 'USA', 'days': 3,
 'items': [],
 'source_urls': [],
 'summary': 'Jeff Jenkins (founder of Chubby Diaries, National Geographic/Disney+ host) published a 72-hour Sonoma County food itinerary (~2025-08-07: video-ID decode corroborated by live-browser verification 2026-09-16). The guide structure (72-hour food itinerary, Sonoma County) is verified; individual restaurant/food stops were not captured in indexed evidence and are not invented here.',
 'confidence': 'low'}]
rec['notes'] = 'REMEDIATED 2026-09-16: identity strongly corroborated (Jeff Jenkins, Chubby Diaries founder, NatGeo host); guide existence and two-signal date verified; item-level detail still needed. See five-criteria report.'

# @lilmsawkward — handle correction + two-signal date + reach evidence
i, rec = find(ex, '@lilmsawkward')
rec['notes'] = ('REMEDIATED 2026-09-16: @lilmsawkward confirmed as the genuine handle (Alexa Moore; indexed Instagram showed 113K followers); '
 '@limsawkward appears to be the typo. Guide video 7682824671422647582 decodes to 2026-09-07; Urlebird mirror corroborates (two-signal). '
 'African diaspora cultural-experiences extraction retained; formal guide-qualification verdict pending council review.')

# @skylietravels — Scotland 5-day (video 7685861774561791263 -> 2026-09-15, Urlebird uploadDate = 2nd signal)
i, rec = find(ex, '@skylietravels')
rec['itineraries'] = [{
 'title': '5-day Scotland itinerary (under $1,000)',
 'destination': 'Scotland (Edinburgh to Isle of Skye)', 'country': 'UK', 'days': 5,
 'items': [
  item(None, 'Edinburgh', 'Edinburgh, UK', 'Route start: Edinburgh.'),
  item(None, 'Isle of Skye', 'Isle of Skye, UK', 'Route end: Isle of Skye.'),
 ],
 'source_urls': ['https://www.tiktok.com/@skylietravels/video/7685861774561791263'],
 'summary': 'Five-day Scotland itinerary from Edinburgh to the Isle of Skye framed under $1,000. Guide date 2026-09-15: video-ID decode corroborated by Urlebird uploadDate 2026-09-15T21:29:25Z (two-signal). Day-by-day stops are delivered in-video and were not transcribed; route anchors and budget framing are as stated in staged evidence. Creator reach staged at 70.3K TikTok followers.',
 'confidence': 'medium'}]
rec['notes'] = REM

# @nytoanywhere — flag unresolved
i, rec = find(ex, '@nytoanywhere')
rec['notes'] = ('STILL UNRESOLVED 2026-09-16: exact-handle search surfaced @thescenicpassport instead of @nytoanywhere; identity, reach, activity and '
 'the claimed 3-day Zion guide remain unverified. Flagged as a replacement candidate.')

# @travelingwithtals — flag unresolved
i, rec = find(ex, '@travelingwithtals')
rec['notes'] = ('STILL UNRESOLVED 2026-09-16: exact-handle web search returned no attributable structured guide; staged evidence cites 526.9K followers and '
 '"Granola group trips" but no specific qualifying itinerary was found. Flagged as a replacement candidate.')

save(p, d)

# ---------------- BATCH 6 ----------------
p, d = load_batch(6)
ex = d['extractions']

# @juliatraveltips — NYC 5-day (video 7597870726225448214 -> 2026-01-21, indexed caption = 2nd signal)
i, rec = find(ex, '@juliatraveltips')
rec['itineraries'] = [{
 'title': 'New York City 5-day itinerary (Julia Ghile)',
 'destination': 'New York City, USA', 'country': 'USA', 'days': 5,
 'items': [
  item(None, 'The Edge NYC', 'New York City, USA',
       'Featured viewpoint in the 5-day NYC itinerary video; itinerary covers Manhattan and Brooklyn neighborhoods with a day-by-day plan, timings, map of curated spots and restaurant recommendations.'),
  item(None, 'Manhattan and Brooklyn neighborhoods', 'New York City, USA',
       'Itinerary structure: five days across Manhattan and Brooklyn with hour-by-hour planning on the creator\'s site (Rome/Paris/Amalfi/Dublin itineraries follow the same format). Full per-day stop list is inside the creator\'s itinerary product and is not invented here.'),
 ],
 'source_urls': ['https://juliatraveltips.com/itineraries/new-york-city',
                 'https://www.tiktok.com/@juliatraveltips/video/7597870726225448214'],
 'summary': 'Julia Ghile\'s creator-owned site (juliatraveltips.com) sells structured itineraries with daily plans and maps; the TikTok video (2026-01-21: video-ID decode corroborated by indexed exact-handle caption) promotes the 5-day NYC map+itinerary (114K-130K likes). A Rome 5-day guide video (7592355923432246551, 2026-01-06) is also indexed. Structure verified; full stop list behind the product paywall.',
 'confidence': 'medium'}]
rec['notes'] = REM

# @polkadotpassport — flag unresolved
i, rec = find(ex, '@polkadotpassport')
rec['notes'] = ('STILL UNRESOLVED 2026-09-16: exact-handle search found only single-venue London posts (videos 7639330642592828692 / 2026-05-13 and '
 '7646107397869833493 / 2026-05-31); no multi-stop qualifying guide found. Reach/activity strong per staging but guide criterion unmet. Flagged as a replacement candidate.')

# @abdulwanders — France mini-guide + Aswan guide (both two-signal, indexed captions)
i, rec = find(ex, '@abdulwanders')
rec['itineraries'] = [
 {
 'title': 'France mini guide',
 'destination': 'France', 'country': 'France', 'days': None,
 'items': [
  item(None, 'Getting around: TGV + rental car', 'France', 'Best combination: high-speed trains (TGV) between cities; rental car for regions, countryside and coastal routes.'),
  item(None, 'Fly into Paris (alternates: Lyon, Nice, Marseille)', 'Paris, France', 'Paris is the main hub; Lyon, Nice and Marseille work depending on itinerary.'),
  item(None, 'Historic & cultural France', 'Paris / Versailles / Chantilly, France', 'Paris, Versailles, Chantilly, museums, monuments.'),
  item(None, 'Regional heritage routes', 'Loire Valley, France', 'Loire Valley chateaux, medieval towns, historic estates.'),
  item(None, 'Coastal France', 'French Riviera / Brittany / Normandy, France', 'French Riviera, Brittany, Normandy cliffs and seaside towns.'),
  item(None, 'Countryside France', 'Dordogne / Provence / Burgundy, France', 'Dordogne, Provence, Burgundy: vineyards, villages.'),
  item(None, 'Mountain regions', 'French Alps / Pyrenees, France', 'French Alps and Pyrenees for nature and outdoor travel.'),
  item(None, 'Distinct regional cultures', 'Alsace / northern France', 'Alsace, northern France and culturally unique regions.'),
 ],
 'source_urls': ['https://www.tiktok.com/@abdulwanders/video/7644887247384349985'],
 'summary': 'France mini guide: plan by regions not landmarks; transport (TGV + rental car); gateways; eight regional experience blocks. Guide date 2026-05-28 (video-ID decode) corroborated by the indexed exact-handle caption (12.7K likes).',
 'confidence': 'high'},
 {
 'title': 'Aswan, Egypt guide',
 'destination': 'Aswan, Egypt', 'country': 'Egypt', 'days': None,
 'items': [
  item(None, 'Getting there', 'Aswan, Egypt', 'Arrive by plane, train or car from Cairo or Luxor.'),
  item(None, 'Getting around', 'Aswan, Egypt', 'Boats commonly used to reach islands and Nile attractions.'),
  item(None, 'Philae Temple', 'Aswan, Egypt', 'Don\'t-miss stop.'),
  item(None, 'Nile islands and riverside viewpoints', 'Aswan, Egypt', 'Don\'t-miss stops.'),
  item(None, 'Nubian culture experiences', 'Aswan, Egypt', 'Nubian culture, colorful riverside houses, local markets; best time October to April.'),
 ],
 'source_urls': ['https://www.tiktok.com/@abdulwanders/video/7646742765174361377'],
 'summary': 'Aswan guide: Nubian culture along the Nile; logistics (getting there/around); Philae Temple, Nile islands, riverside viewpoints; best time Oct-Apr. Guide date 2026-06-02 (video-ID decode) corroborated by the indexed exact-handle caption (69.8K-229K likes across indexed versions).',
 'confidence': 'high'}]
rec['notes'] = REM

# @chloe__trips — stays excluded, note strengthened
i, rec = find(ex, '@chloe__trips')
rec['notes'] = ('STILL EXCLUDED 2026-09-16: exact profile confirmed (20.6K followers, French travel creator "Je t\'aide a voyager"); the only detailed Quebec '
 'itinerary found was attributed to a generic Chloe result with a malformed URL and cannot be attributed to @chloe__trips. No qualifying exact-handle guide. Replacement candidate.')

# @amyenvoyage — Helsinki 4-day (creator-owned page)
i, rec = find(ex, '@amyenvoyage')
rec['itineraries'] = [{
 'title': 'Best Things to Do in Helsinki: 4-Day Itinerary + Hidden Gems',
 'destination': 'Helsinki, Finland', 'country': 'Finland', 'days': 4,
 'items': [
  item(1, 'Solo Sokos Hotel Pier 4; Rue Madame dinner', 'Helsinki, Finland',
       'Base: Solo Sokos Hotel Pier 4 (Katajanokka, walkable harbour district); dinner at Rue Madame.'),
  item(2, 'Architecture & design day', 'Helsinki, Finland',
       'Guided architecture & design tour; Finlandia Hall; Design District; Helsinki Central Railway Station; Oodi Library; Temppeliaukio Church (Rock Church); evening sauna boat (M/Y Fortune).'),
  item(3, 'Market Square, Suomenlinna, spa evening', 'Helsinki, Finland',
       'Market Square; ferry to Suomenlinna Sea Fortress; Usva Spa (whisking/vihta ritual); Hansa Cafe Bar & Brasserie; Kupoli Cocktail Bar.'),
  item(4, 'Bike & food tour, parks, cathedrals', 'Helsinki, Finland',
       'Guided bike & food tour (HELtours); Central Park; Seurasaari Open-Air Museum; Huvilakatu; Pohjola Building; Helsinki Cathedral; Uspenski Cathedral; Restaurant Jason.'),
  item(None, 'Lyme Regis guide (TikTok)', 'Lyme Regis, UK',
       'Second guide: Lyme Regis TikTok video 7625544703433379094 (2026-04-06 video-ID decode; single-signal date).'),
 ],
 'source_urls': ['https://www.amyenvoyage.com/best-things-to-do-in-helsinki-4-day-itinerary-hidden-gems/',
                 'https://www.tiktok.com/@amyenvoyage/video/7625544703433379094'],
 'summary': 'Creator-owned 4-day Helsinki itinerary with explicit daily plans and named stops. Page carries affiliate-link disclosure (not an exclusion). Replaces the prior vague two-item Lyme Regis/Helsinki blend.',
 'confidence': 'high'}]
rec['notes'] = REM

# @explorewithcriostoir — scenic-drive guides (3 videos, each two-signal via indexed captions)
i, rec = find(ex, '@explorewithcriostoir')
rec['itineraries'] = [{
 'title': 'Ireland scenic-drive guides + recommendations map',
 'destination': 'Ireland', 'country': 'Ireland', 'days': None,
 'items': [
  item(None, 'Copper Coast Drive', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Molls Gap', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Doolough Valley', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Causeway Coastal Route', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Fanad Drive', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Ring of Kerry', 'Ireland', 'Scenic drive guide (indexed caption).'),
  item(None, 'Ireland recommendations travel map', 'Ireland', 'Creator offers an Ireland recommendations travel map and personalized itineraries.'),
 ],
 'source_urls': ['https://www.tiktok.com/@explorewithcriostoir/video/7611266906783354134',
                 'https://www.tiktok.com/@explorewithcriostoir/video/7615356204503649558',
                 'https://www.tiktok.com/@explorewithcriostoir/video/7622023952445050134'],
 'summary': 'Ireland scenic-drive guide series (Copper Coast Drive, Molls Gap, Doolough Valley, Causeway Coastal Route, Fanad Drive, Ring of Kerry) plus a recommendations travel map and personalized-itinerary offer. Dates: 2026-02-26, 2026-03-09, 2026-03-27 (video-ID decodes corroborated by indexed exact-handle captions).',
 'confidence': 'medium'}]
rec['notes'] = REM

# @kellyprincewright — Dublin literary guide replaces too-old Wales guide
i, rec = find(ex, '@kellyprincewright')
rec['itineraries'] = [{
 'title': 'Dublin literary guide',
 'destination': 'Dublin, Ireland', 'country': 'Ireland', 'days': None,
 'items': [
  item(None, 'The Shelbourne', 'Dublin, Ireland', 'Literary Dublin stop (indexed caption).'),
  item(None, "Sweny's Pharmacy", 'Dublin, Ireland', 'Literary Dublin stop (indexed caption).'),
  item(None, "Oscar Wilde's Home", 'Dublin, Ireland', 'Literary Dublin stop (indexed caption).'),
 ],
 'source_urls': ['https://www.tiktok.com/@kellyprincewright/video/7516513590250048790'],
 'summary': 'Dublin literary guide naming The Shelbourne, Sweny\'s Pharmacy and Oscar Wilde\'s Home. Guide date 2025-06-16 (video-ID decode) corroborated by the indexed exact-handle caption. Caption discloses a Tourism Ireland partnership (AD) — disclosed, not an exclusion. Replaces the Wales guide (2023-09-23, outside the recency window).',
 'confidence': 'medium'}]
rec['notes'] = REM

save(p, d)

# ---------------- BATCH 7 ----------------
p, d = load_batch(7)
ex = d['extractions']

# @the5worldexplorers — Hong Kong 5-day (creator-owned page, full detail)
i, rec = find(ex, '@the5worldexplorers')
rec['itineraries'] = [{
 'title': '5 Days in Hong Kong: What We Did, What We Missed, and Why That\'s Perfectly Okay',
 'destination': 'Hong Kong', 'country': 'China', 'days': 5,
 'items': [
  item(1, 'Hong Kong Disneyland Hotel', 'Hong Kong',
       'Check into Hong Kong Disneyland Hotel; explore the grounds (maze, gardens); character dinner buffet.'),
  item(2, 'City day: Bakehouse, Avenue of Stars', 'Hong Kong',
       'MTR to the city; Bakehouse bakery; Avenue of Stars (Tsim Sha Tsui waterfront) and Bruce Lee statue; mall food courts and grocery shopping.'),
  item(3, 'Hong Kong Disneyland', 'Hong Kong',
       'Hong Kong Disneyland: Iron Man Experience, Fantasyland, Mystic Manor, Grizzly Gulch, Frozen attractions; fireworks.'),
  item(4, 'Resort rest day', 'Hong Kong',
       'Tai Chi with Donald Duck; rest day. Planned pink-dolphin tour, Tian Tan Buddha and Tai O fishing village were NOT done (page is explicit) and are recorded here as planned-not-done, not as visited stops.'),
  item(5, 'Peak day: escalator, gardens, Victoria Peak', 'Hong Kong',
       'Phi Coffee & Pancake; Mid-Levels Escalator; Hong Kong Zoological and Botanical Gardens; Peak Tram; Victoria Peak; Hong Kong double-decker tram.'),
 ],
 'source_urls': ['https://www.the5worldexplorers.com/5-days-in-hong-kong/'],
 'summary': 'Creator-owned 5-day Hong Kong itinerary with explicit Days 1-5 and named stops. Page published 2025-04-12, modified 2026-09-07 (creator-owned metadata; formal evidence persistence pending). Replaces the prior zero-item record.',
 'confidence': 'high'}]
rec['notes'] = REM

# @boyeatsworld — flag unresolved
i, rec = find(ex, '@boyeatsworld')
rec['notes'] = ('STILL UNRESOLVED 2026-09-16: direct page fetch of the staged Busan guide failed and was not treated as inspected; identity corroborated '
 '(BoyEatsWorld by Aleney de Winter; family/food/culture/travel); a creator-owned Busan food guide dated 2026-02-26 exists but its contents were not captured. '
 'Needs another accessible structured guide or replacement.')

save(p, d)
print('batches 5-7 updated OK')
