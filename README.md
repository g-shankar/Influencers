# Influencers — Travel Itinerary Pilot

Pilot: AI-extracted itineraries from 100 travel creators (50 TikTok + 50 Instagram),
validated through a fail-closed gate harness before anything enters the database.

- `influencers.csv` — the 100-creator list (handles, platforms, niches, source-reported follower counts)
- `schema.sql` / `pilot.db` — SQLite database (populated only after validation gates pass)
- `staging/` — raw extraction output per batch (canonical `itineraries_batchN.json` files)
- `validation/` — 7-gate validation harness (gate scripts, evidence-council briefs, quarantine log)
- `report/` — reporting inputs
- `packaging_feasibility.md` — packaging feasibility notes
