-- Travel influencer itinerary pilot — database schema
-- SQLite. Created 2026-09-15.

CREATE TABLE IF NOT EXISTS influencers (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    handle          TEXT NOT NULL,
    platform        TEXT NOT NULL CHECK (platform IN ('tiktok','instagram')),
    niche           TEXT,
    followers_approx TEXT,              -- as cited by source, or 'unknown'; never invented
    profile_url     TEXT,
    source_urls     TEXT,               -- pipe-separated sources
    created_at      TEXT DEFAULT (datetime('now'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_influencers_handle_platform ON influencers(handle, platform);

CREATE TABLE IF NOT EXISTS posts (
    id              INTEGER PRIMARY KEY,
    influencer_id   INTEGER NOT NULL REFERENCES influencers(id),
    post_url        TEXT,
    platform        TEXT,
    posted_at       TEXT,
    caption_excerpt TEXT,
    extracted_at    TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS itineraries (
    id              INTEGER PRIMARY KEY,
    influencer_id   INTEGER NOT NULL REFERENCES influencers(id),
    title           TEXT NOT NULL,
    destination     TEXT,
    country         TEXT,
    days            INTEGER,
    summary         TEXT,
    source_post_id  INTEGER REFERENCES posts(id),
    confidence      TEXT CHECK (confidence IN ('high','medium','low')),
    created_at      TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS itinerary_items (
    id              INTEGER PRIMARY KEY,
    itinerary_id    INTEGER NOT NULL REFERENCES itineraries(id),
    day             INTEGER,
    item_type       TEXT CHECK (item_type IN ('flight','hotel','activity','restaurant','transport','other')),
    name            TEXT NOT NULL,
    location        TEXT,
    details         TEXT,
    booking_link    TEXT,
    price_hint      TEXT
);
CREATE INDEX IF NOT EXISTS idx_items_itinerary ON itinerary_items(itinerary_id);

-- Gate 4/5 support: one row per evidence source per itinerary.
-- Added 2026-09-15 for the validation harness (extraction JSON carries
-- source_urls; posts.source_post_id alone cannot hold them).
CREATE TABLE IF NOT EXISTS itinerary_sources (
    id              INTEGER PRIMARY KEY,
    itinerary_id    INTEGER NOT NULL REFERENCES itineraries(id),
    source_url      TEXT NOT NULL,
    reachable       TEXT,               -- gate3 verdict: reachable|unreachable|unchecked
    verified_at     TEXT
);
CREATE INDEX IF NOT EXISTS idx_sources_itinerary ON itinerary_sources(itinerary_id);

CREATE TABLE IF NOT EXISTS vendors (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    type            TEXT,               -- flights | hotels | activities | dining
    partner_program TEXT,               -- how to get access
    commission_notes TEXT,
    api_available   TEXT,               -- yes/no/unknown + notes
    source_url      TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);
