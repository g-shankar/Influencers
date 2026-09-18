#!/usr/bin/env python3
"""Append accepted TikTok creators to canonical batch files (batch9, this run).
Run only AFTER final dedup + all gates. Writes: batch9.csv, selection_log_batch9.csv,
itineraries_batch9.json. Selector: t2-redispatch-2026-09-17. check_date=2026-09-17."""
import csv, json, sys

BASE = '/home/hatch/workspace/travel-influencer-pilot'
CHECK_DATE = '2026-09-17'
SELECTOR = 't2-redispatch-2026-09-17'
PLATFORM = 'tiktok'

def dedup_universe():
    u = set()
    import glob
    for f in glob.glob(f'{BASE}/batch*.csv') + glob.glob(f'{BASE}/influencers.csv'):
        for row in csv.DictReader(open(f, encoding='utf-8')):
            h = (row.get('handle') or '').strip().lower()
            if h: u.add(h)
    try:
        for line in open(f'{BASE}/staging/dedup_handles_batch9.txt', encoding='utf-8'):
            line = line.strip().lower()
            if line: u.add(line)
    except FileNotFoundError:
        pass
    try:
        q = json.load(open(f'{BASE}/validation/quarantine.json', encoding='utf-8'))
        items = q if isinstance(q, list) else q.get('entries', q.get('items', []))
        for e in (items or []):
            h = (e.get('handle') or '').strip().lower()
            if h: u.add(h)
    except FileNotFoundError:
        pass
    return u

# --- accepted creators (batch9) ---
ACCEPTED = [
  {
    "name": "Amanda Viagem",
    "handle": "@amandanaviagem",
    "niche": "Brazil travel",
    "followers_approx": "100.1K",
    "profile_url": "https://www.tiktok.com/@amandanaviagem",
    "source_urls": "https://www.tiktok.com/@amandanaviagem/video/7638748083026660616",
    "followers_observed": "100,100",
    "followers_source": "TikTok profile state __UNIVERSAL_DATA_FOR_REHYDRATION__, observed 2026-09-17",
    "discovery_source": "TikTok discovery re-dispatch 2026-09-17 (t2)",
    "identity_check": "pass - mononym 'Amanda' (mononym allowed per SELECTION_CRITERIA.md); TikTok nickname 'amandanaviagem'",
    "identity_method": "TikTok profile state nickname + handle",
    "content_fit": "pass - 8-day Natal/Pipa/Joao Pessoa route, TikTok video 7638748083026660616, create_time 2026-05-11 (in 2024-09-17..2026-09-17 window), day-by-day with named venues/prices",
    "content_fit_evidence": "video 7638748083026660616 (2026-05-11): Dia 1 4x4 litoral sul R$170; Dia 2 Parrachos do Rio do Fogo R$190; Dia 3 buggy dunas litoral norte R$180; Dia 4 Pipa (praia do Madeiro/golfinhos, praia do amor, falesias); Dia 5 Joao Pessoa (orla, feirinha); Dia 6 Costa do Conde/quadriciclo; Dia 7 Cabedelo/lagoa do Jacare/barco; Dia 8 piscinas naturais do Seixas",
    "reach_floor": "pass - 100,100 >= 10,000 (dated observation 2026-09-17)",
    "engagement_observed": "video 7638748083026660616: 54,200 plays; 2,950 likes; 33 comments; 915 shares; 1,352 saves (creator-owned video metrics, observed 2026-09-17)",
    "activity_check": "pass - TikTok profile live; urlebird latest visible post 2026-09-04",
    "purchase_intent": "affiliate/discount codes present (Bagaggio cupom AMANDA; agency follower discounts @nataltrippasseios, @encontredestinos) - purchase intent present, not a consumer planning service",
    "exclusions_check": "pass - third-party tour operators recommended with discount codes; no hosted group trips by creator; no consumer trip-planning service; no brand/agency/repost (observed 2026-09-17). NOTE: batch9-topup worker rejected an older Ilha Grande video (2024-06-28, out of window); this acceptance rests on the separate in-window 2026-05-11 video.",
    "decision": "accept",
    "notes": "Brazil creator; Portuguese-language 8-day NE Brazil route with per-day prices",
  },
  {
    "name": "Lola Hubner",
    "handle": "@lolahubner",
    "niche": "Australia/Hawaii travel",
    "followers_approx": "32.5K",
    "profile_url": "https://www.tiktok.com/@lolahubner",
    "source_urls": "https://lolahubner.com/blogs/travel/7-day-hawaii-itinerary-maui-oahu",
    "followers_observed": "32,500",
    "followers_source": "TikTok profile state __UNIVERSAL_DATA_FOR_REHYDRATION__, observed 2026-09-17",
    "discovery_source": "TikTok discovery re-dispatch 2026-09-17 (t2)",
    "identity_check": "pass - named individual 'Lola Hubner'; TikTok nickname 'Lola Hubner'",
    "identity_method": "TikTok profile state nickname; personal blog domain lolahubner.com",
    "content_fit": "pass - 7-day Maui/Oahu itinerary, lolahubner.com blog published 2026-03-03 (in window), day-by-day with named hotels/activities; also Alice Springs-Uluru and 19-day Queensland itineraries",
    "content_fit_evidence": "blog 2026-03-03 '7 Day Hawaii Itinerary: Maui & Oahu': Day 1 arrival Maui/Ka'anapali (Royal Lahaina Resort & Bungalows); Day 2 Ka'anapali Beach + Myths of Maui Luau; Day 3 snorkelling + whale watching; Day 4 Waikiki (The Laylow) + 'Auana by Cirque du Soleil; Day 5 Oahu island tour w/ Fun Group Hawai'i (North Shore, Matsumoto Shave Ice); Day 6 Le'ahi (Diamond Head) hike + sunset dinner cruise; Day 7 departure",
    "reach_floor": "pass - 32,500 >= 10,000 (dated observation 2026-09-17)",
    "engagement_observed": "recent TikTok posts (urlebird, observed 2026-09-17): 2026-09-14 1.32K views/158 likes; 978 views/70 likes; 3.85K views/137 likes",
    "activity_check": "pass - TikTok profile live; latest visible post 2026-09-14",
    "purchase_intent": "blog affiliate/ads present; Travello subdomain lists bookable third-party tours - not creator-hosted or consumer planning by her",
    "exclusions_check": "pass - creator-authored itineraries on own blog; third-party bookable tours (Travello) are not her hosted trips; no consumer trip-planning service; no brand/agency/repost (observed 2026-09-17)",
    "decision": "accept",
    "notes": "Australia-based creator; Hawaii + Outback + Queensland structured itineraries",
  },
]

LOG_COLS = ["batch","handle","platform","name","niche","followers_approx","followers_observed",
"followers_source","profile_url","discovery_source","identity_check","identity_method","content_fit",
"content_fit_evidence","reach_floor","engagement_observed","activity_check","purchase_intent",
"exclusions_check","decision","notes","check_date","selector"]

def build_extraction(a):
    if a["handle"] == "@amandanaviagem":
        days = [
            {"day": 1, "summary": "4x4 no litoral sul, passando por lagoas e finalizando no por do sol", "items": [
                {"type": "activity", "name": "4x4 no litoral sul", "detail": "lagoas; por do sol; R$170; agency @nataltrippasseios, desconto avisando que e seguidor"}]},
            {"day": 2, "summary": "Parrachos do Rio do Fogo", "items": [
                {"type": "activity", "name": "Parrachos do Rio do Fogo", "detail": "R$190; agency @nataltrippasseios"}]},
            {"day": 3, "summary": "Buggy nas dunas do litoral norte", "items": [
                {"type": "activity", "name": "Buggy nas dunas do litoral norte", "detail": "parada para brincadeiras (skibunda, tirolesa, cobrados a parte); R$180; agency @nataltrippasseios"}]},
            {"day": 4, "summary": "Ida para Pipa", "items": [
                {"type": "activity", "name": "Praia do Madeiro", "detail": "Pipa, 80km de Natal; possivel ver golfinhos"},
                {"type": "activity", "name": "Praia do Amor", "detail": "Pipa; visual das falesias; centrinho charmoso a noite"}]},
            {"day": 5, "summary": "Ida para Joao Pessoa; dia de chegada", "items": [
                {"type": "activity", "name": "Orla de Joao Pessoa", "detail": "chegada; feirinha de artesanatos; recomenda alugar carro ou onibus/transfer"},
                {"type": "transport", "name": "Pipa -> Joao Pessoa", "detail": "~3 horas; carro alugado ou onibus/transfer"}]},
            {"day": 6, "summary": "Litoral sul em Joao Pessoa: Costa do Conde", "items": [
                {"type": "activity", "name": "Costa do Conde", "detail": "passeio de quadriciclo aos mirantes (adicional); agency @encontredestinos"}]},
            {"day": 7, "summary": "Cabedelo", "items": [
                {"type": "activity", "name": "Praias de Cabedelo", "detail": "Uber; por do sol na lagoa do Jacare; passeio de barco com agency @encontredestinos"}]},
            {"day": 8, "summary": "Piscinas naturais do Seixas", "items": [
                {"type": "activity", "name": "Piscinas naturais do Seixas", "detail": "depende da mare baixa; consultar agency @encontredestinos"}]},
        ]
        return {"handle": "@amandanaviagem", "platform": "tiktok",
                "itineraries": [{"title": "8-day Natal / Pipa / Joao Pessoa route", "destination": "Natal, Pipa, Joao Pessoa, Brazil",
                                "source_url": "https://www.tiktok.com/@amandanaviagem/video/7638748083026660616",
                                "published_date": "2026-05-11", "days": days}],
                "notes": "Day-by-day creator itinerary with per-day prices; third-party agencies with follower discounts (not creator-hosted)."}
    if a["handle"] == "@lolahubner":
        days = [
            {"day": 1, "summary": "Arrival in Maui; Ka'anapali", "items": [
                {"type": "hotel", "name": "Royal Lahaina Resort & Bungalows", "detail": "Ka'anapali, Maui; beachfront bungalow"},
                {"type": "activity", "name": "Sunset beach walk", "detail": "Ka'anapali; dinner nearby"}]},
            {"day": 2, "summary": "Beach day & luau", "items": [
                {"type": "activity", "name": "Ka'anapali Beach", "detail": "morning beach; pool at resort"},
                {"type": "activity", "name": "Myths of Maui Luau", "detail": "evening Polynesian show; fire knife finale"},
                {"type": "restaurant", "name": "Myths of Maui Luau", "detail": "evening dinner show"}]},
            {"day": 3, "summary": "Coastal snorkelling & whale watching", "items": [
                {"type": "activity", "name": "Snorkelling cruise", "detail": "Maui; three-story boat; breakfast/lunch served"},
                {"type": "activity", "name": "Whale watching", "detail": "February peak humpback season; multiple breaches"}]},
            {"day": 4, "summary": "Waikiki & evening show", "items": [
                {"type": "hotel", "name": "The Laylow", "detail": "Waikiki, O'ahu; retro, near beach"},
                {"type": "activity", "name": "'Auana by Cirque du Soleil", "detail": "evening show in Waikiki"}]},
            {"day": 5, "summary": "Full day O'ahu island tour", "items": [
                {"type": "activity", "name": "O'ahu island tour with Fun Group Hawai'i", "detail": "lookouts, local eateries, North Shore"},
                {"type": "restaurant", "name": "Matsumoto Shave Ice", "detail": "Haleiwa, North Shore"}]},
            {"day": 6, "summary": "Le'ahi (Diamond Head) & sunset cruise", "items": [
                {"type": "activity", "name": "Le'ahi (Diamond Head) hike", "detail": "45-90 min return; tunnels/stairs; book entry"},
                {"type": "activity", "name": "Waikiki Beach", "detail": "surfboard rental"},
                {"type": "activity", "name": "Sunset dinner cruise", "detail": "Waikiki coastline; Friday fireworks"}]},
            {"day": 7, "summary": "Departure", "items": [
                {"type": "restaurant", "name": "Breakfast in Waikiki", "detail": "final morning before Sydney flight"}]},
        ]
        return {"handle": "@lolahubner", "platform": "tiktok",
                "itineraries": [{"title": "7-day Hawaii itinerary: Maui & O'ahu", "destination": "Maui, O'ahu, Hawaii",
                                "source_url": "https://lolahubner.com/blogs/travel/7-day-hawaii-itinerary-maui-oahu",
                                "published_date": "2026-03-03", "days": days}],
                "notes": "Creator-authored blog itinerary; also has Alice Springs-Uluru and 19-day Queensland itineraries."}
    raise ValueError(a["handle"])

def main():
    u = dedup_universe()
    for a in ACCEPTED:
        if a["handle"].lower() in u:
            print("DEDUP HIT, skipping:", a["handle"]); sys.exit(1)
    # batch9.csv
    with open(f'{BASE}/batch9.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for a in ACCEPTED:
            w.writerow([a["name"], a["handle"], PLATFORM, a["niche"], a["followers_approx"], a["profile_url"], a["source_urls"]])
    # selection log
    with open(f'{BASE}/staging/selection_log_batch9.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for a in ACCEPTED:
            w.writerow(["batch9", a["handle"], PLATFORM, a["name"], a["niche"], a["followers_approx"],
                        a["followers_observed"], a["followers_source"], a["profile_url"], a["discovery_source"],
                        a["identity_check"], a["identity_method"], a["content_fit"], a["content_fit_evidence"],
                        a["reach_floor"], a["engagement_observed"], a["activity_check"], a["purchase_intent"],
                        a["exclusions_check"], a["decision"], a["notes"], CHECK_DATE, SELECTOR])
    # itineraries json
    ip = f'{BASE}/staging/itineraries_batch9.json'
    d = json.load(open(ip, encoding='utf-8'))
    for a in ACCEPTED:
        d["extractions"].append(build_extraction(a))
    json.dump(d, open(ip, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("wrote", len(ACCEPTED), "to batch9")
    # progress log (first 2 of 5 toward the 5-acceptance line)
    with open(f'{BASE}/staging/tiktok_t2_progress.md', 'a', encoding='utf-8') as f:
        for a in ACCEPTED:
            f.write(f"- 2026-09-17 {SELECTOR}: {a['handle']} -> batch9 | gates: identity pass / itinerary in-window / reach {a['followers_approx']} / engagement public / exclusions pass\n")
    print("progress logged")

if __name__ == '__main__':
    main()
