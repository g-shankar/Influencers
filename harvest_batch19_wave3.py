"""Wave-3 harvest: fill items[] for the 4 pending batch19 itineraries.

Sources (fetched and read 2026-09-17 by the wave-3 worker):
- https://travelingblackwidow.com/is-croatia-the-new-italy/
- https://travelingblackwidow.com/visit-south-korea-spring-2025/
- https://thereshegoesagain.org/steinbach-travel-manitoba-canada/
- https://thereshegoesagain.org/quebec-city-itinerary/

Only the 4 pending itinerary objects are touched; all other extraction
objects are preserved byte-for-byte. Item types restricted to the
gate1_schema.py allowlist: flight, hotel, activity, restaurant, transport, other.
"""
import json
from pathlib import Path

P = Path(__file__).parent / "itineraries_batch19.json"
d = json.loads(P.read_text())
exts = d["extractions"]

def item(name, item_type, location, day, details):
    assert item_type in {"flight", "hotel", "activity", "restaurant", "transport", "other"}, item_type
    return {
        "name": name,
        "item_type": item_type,
        "location": location,
        "day": day,
        "details": details,
        "price_hint": None,
        "booking_link": None,
    }

CROATIA_ITEMS = [
    item("Dubrovnik Old Town", "activity", "Dubrovnik, Croatia", None,
         "Historic walled old town, the anchor stop of her Croatia guide."),
    item("Dubrovnik city walls", "activity", "Dubrovnik, Croatia", None,
         "Walk the medieval city walls around the Old Town."),
    item("Rector's Palace", "activity", "Dubrovnik, Croatia", None,
         "Gothic-Renaissance palace in Dubrovnik's Old Town."),
    item("Franciscan Monastery", "activity", "Dubrovnik, Croatia", None,
         "Historic monastery in Dubrovnik's Old Town."),
    item("Sponza Palace", "activity", "Dubrovnik, Croatia", None,
         "16th-century palace in Dubrovnik's Old Town."),
    item("Sea Organ", "activity", "Zadar, Croatia", None,
         "Architectural sound installation on Zadar's waterfront."),
    item("Greeting to the Sun", "activity", "Zadar, Croatia", None,
         "Solar-powered light installation beside the Sea Organ in Zadar."),
    item("Roman Forum", "activity", "Zadar, Croatia", None,
         "Ancient Roman forum ruins in Zadar."),
    item("St. Donatus Church", "activity", "Zadar, Croatia", None,
         "9th-century church on Zadar's Roman Forum."),
    item("Archaeological Museum", "activity", "Zadar, Croatia", None,
         "Museum of regional archaeology in Zadar."),
    item("Kornati Islands National Park", "activity", "Zadar archipelago, Croatia", None,
         "Day trip to the Kornati island national park from Zadar."),
    item("Diocletian's Palace", "activity", "Split, Croatia", None,
         "Roman emperor's palace forming the heart of Split's old town."),
    item("Krka National Park", "activity", "near Split, Croatia", None,
         "Waterfall national park visited from Split."),
    item("Visovac Monastery", "activity", "Krka National Park, Croatia", None,
         "Island monastery inside Krka National Park."),
    item("Zagreb Upper Town", "other", "Zagreb, Croatia", None,
         "Historic hilltop Upper Town (Gornji Grad) district of Zagreb."),
    item("St. Mark's Church", "activity", "Zagreb, Croatia", None,
         "Church with tiled roof in Zagreb's Upper Town."),
    item("Zagreb Lower Town", "other", "Zagreb, Croatia", None,
         "Lower Town (Donji Grad) district of Zagreb."),
    item("Ban Jelacic Square", "activity", "Zagreb, Croatia", None,
         "Central square of Zagreb's Lower Town."),
    item("Lungomare promenade", "activity", "Opatija, Croatia", None,
         "Seafront promenade walk in Opatija."),
    item("Volosko", "other", "Opatija, Croatia", None,
         "Fishing village stop near Opatija."),
    item("Hotel Kvarner", "hotel", "Opatija, Croatia", None,
         "Hotel named in her Opatija section."),
    item("Hotel Imperial", "hotel", "Opatija, Croatia", None,
         "Hotel named in her Opatija section."),
]

KOREA_ITEMS = [
    item("Hanbok experience", "activity", "Seoul, South Korea", 1,
         "Traditional Korean hanbok dress-up experience on day one in Seoul."),
    item("Changing of the Royal Guard", "activity", "Gyeongbokgung Palace, Seoul, South Korea", 1,
         "Royal guard changing ceremony at Gyeongbokgung Palace."),
    item("Cosmetic district", "other", "Seoul, South Korea", 1,
         "Seoul cosmetics/beauty shopping district on day one."),
    item("DMZ guided tour", "activity", "DMZ, South Korea", None,
         "Guided tour of the Korean Demilitarized Zone."),
    item("DMZ tunnel descent", "activity", "DMZ, South Korea", None,
         "Train descent into the infiltration tunnel on the DMZ tour."),
    item("DMZ observation area", "activity", "DMZ, South Korea", None,
         "Binocular viewpoint over North Korea at the DMZ."),
    item("Haenyeo culture", "activity", "Jeju Island, South Korea", None,
         "Jeju's female free-diver (haenyeo) culture."),
    item("Gamcheon Culture Village", "activity", "Busan, South Korea", None,
         "Colorful hillside cultural village in Busan."),
    item("Jagalchi Fish Market", "activity", "Busan, South Korea", None,
         "Busan's famous seafood market."),
    item("Pyeongchang mountains", "other", "Pyeongchang, South Korea", None,
         "Mountain region stop in Pyeongchang."),
    item("Bibimbap lunch", "restaurant", "Pyeongchang, South Korea", None,
         "Bibimbap lunch in the Pyeongchang mountain region."),
    item("Temple meditation with monk", "activity", "Andong, South Korea", None,
         "Temple meditation session with a monk in Andong."),
    item("Rice-wine brewery", "activity", "Andong, South Korea", None,
         "Rice-wine brewery visit/activity in Andong."),
    item("Gyeongju Buddhist temples", "activity", "Gyeongju, South Korea", None,
         "UNESCO-listed Buddhist temples of Gyeongju."),
    item("Breakfast buffet", "restaurant", "Gyeongju, South Korea", None,
         "Breakfast buffet in Gyeongju."),
]

STEINBACH_ITEMS = [
    item("Rosedale Chapel Bed & Breakfast", "hotel", "Steinbach, Manitoba, Canada", None,
         "Bed and breakfast stay named in her Steinbach guide."),
    item("Nearby trails", "activity", "Steinbach, Manitoba, Canada", None,
         "Local trails recommended around Steinbach."),
    item("Masagana Flower Farm tinta experience", "activity", "near Steinbach, Manitoba, Canada", None,
         "Flower farm tinta dyeing experience, about 5-6 hours."),
    item("Mennonite Heritage Village", "activity", "Steinbach, Manitoba, Canada", None,
         "Open-air museum of Mennonite heritage in Steinbach."),
    item("Chino's Bistro", "restaurant", "Steinbach, Manitoba, Canada", None,
         "Restaurant recommendation in Steinbach."),
    item("Old Chapel Bakery", "restaurant", "Steinbach, Manitoba, Canada", None,
         "Bakery recommendation in Steinbach."),
    item("Forum & Bistro", "restaurant", "Steinbach, Manitoba, Canada", None,
         "Restaurant recommendation in Steinbach."),
    item("Bothwell Cheese", "other", "near Steinbach, Manitoba, Canada", None,
         "Cheese producer/shop stop near Steinbach."),
    item("Prairie Oil & Provisions", "other", "Steinbach, Manitoba, Canada", None,
         "Food/provisions shop in Steinbach."),
    item("Retro Chique", "other", "Steinbach, Manitoba, Canada", None,
         "Shopping stop in Steinbach."),
]

QUEBEC_ITEMS = [
    item("Fairmont Le Chateau Frontenac", "hotel", "Quebec City, Canada", 1,
         "Iconic hotel stay on day 1 of her 3-day Quebec City itinerary."),
    item("Place d'Armes and Old Quebec", "activity", "Quebec City, Canada", 1,
         "Old Quebec exploration around Place d'Armes on day 1."),
    item("Restaurant Pub D'Orsay", "restaurant", "Quebec City, Canada", 1,
         "Day 1 dinner spot."),
    item("Bügel de Fabrique", "restaurant", "Quebec City, Canada", 2,
         "Bagel stop on day 2."),
    item("Montmorency Falls", "activity", "near Quebec City, Canada", 2,
         "Waterfall visit on day 2."),
    item("Ile d'Orleans drive", "activity", "Ile d'Orleans, Quebec, Canada", 2,
         "Scenic island drive on day 2."),
    item("Bistro du Hangar", "restaurant", "Quebec City, Canada", 2,
         "Day 2 dining stop."),
    item("Quai de Saint-Jean", "activity", "Ile d'Orleans, Quebec, Canada", 2,
         "Wharf stop on Ile d'Orleans, day 2."),
    item("Ferme Laval Gagnon", "activity", "Ile d'Orleans, Quebec, Canada", 2,
         "Farm stop on Ile d'Orleans, day 2."),
    item("Cassis Monna & Filles", "activity", "Ile d'Orleans, Quebec, Canada", 2,
         "Blackcurrant producer visit on Ile d'Orleans, day 2."),
    item("Don Vegan", "restaurant", "Quebec City, Canada", 2,
         "Vegan restaurant on day 2."),
    item("Cafe Le Cousins", "restaurant", "Quebec City, Canada", 3,
         "Day 3 cafe stop."),
    item("Plains of Abraham", "activity", "Quebec City, Canada", 3,
         "Historic battlefield park on day 3."),
    item("Joan of Arc Garden", "activity", "Quebec City, Canada", 3,
         "Garden stop on day 3."),
    item("St-Hubert", "restaurant", "Quebec City, Canada", 3,
         "Rotisserie restaurant on day 3."),
    item("Parliament gardens", "activity", "Quebec City, Canada", 3,
         "Gardens by the Parliament Building on day 3."),
    item("Rue Saint-Louis", "activity", "Quebec City, Canada", 3,
         "Historic street walk on day 3."),
    item("Dufferin Terrace", "activity", "Quebec City, Canada", 3,
         "Terrace boardwalk by the Chateau on day 3."),
    item("Rue de Buade and Rue Port Dauphin", "activity", "Quebec City, Canada", 3,
         "Old-town streets on day 3."),
    item("Escalier Casse-Cou", "activity", "Quebec City, Canada", 3,
         "Breakneck Stairs in Old Quebec on day 3."),
    item("Rue du Petit Champlain", "activity", "Quebec City, Canada", 3,
         "Shopping street in Lower Town on day 3."),
    item("Le Lapin Saute", "restaurant", "Quebec City, Canada", 3,
         "Rabbit-specialty restaurant on day 3."),
    item("Umbrella Alley", "activity", "Quebec City, Canada", 3,
         "Umbrella art installation alley on day 3."),
    item("Place Royale", "activity", "Quebec City, Canada", 3,
         "Historic square in Lower Town on day 3."),
    item("Notre-Dame-des-Victoires", "activity", "Quebec City, Canada", 3,
         "Stone church at Place Royale on day 3."),
    item("Fresque des Quebecois", "activity", "Quebec City, Canada", 3,
         "Mural in Old Quebec on day 3."),
]

HARVESTS = {
    ("@travelingblackwidow", "https://travelingblackwidow.com/is-croatia-the-new-italy/"): CROATIA_ITEMS,
    ("@travelingblackwidow", "https://travelingblackwidow.com/visit-south-korea-spring-2025/"): KOREA_ITEMS,
    ("@thereshegoesagn", "https://thereshegoesagain.org/steinbach-travel-manitoba-canada/"): STEINBACH_ITEMS,
    ("@thereshegoesagn", "https://thereshegoesagain.org/quebec-city-itinerary/"): QUEBEC_ITEMS,
}

touched = 0
for e in exts:
    if e["handle"] not in ("@travelingblackwidow", "@thereshegoesagn"):
        continue
    for it in e["itineraries"]:
        key = (e["handle"], it["source_urls"][0])
        if key in HARVESTS:
            assert it["items"] == [], f"expected empty items for {key}"
            it["items"] = HARVESTS[key]
            touched += 1
    e["notes"] = ("Items harvested 2026-09-17 by wave-3 worker from the creator-owned "
                  "source pages listed in source_urls; stops named explicitly in the source text.")

assert touched == 4, f"touched={touched}"
P.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
print(f"OK: filled items for {touched} itineraries")
