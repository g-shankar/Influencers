-- Gate 5 — DB reconciliation queries (run after load, before the report).
-- Every query should return the expected value in the comment, or it is a FAIL.
-- Run: sqlite3 pilot.db < validation/gate4_reconciliation.sql

.headers on
.mode column

-- 1. Influencer counts: expect 100 total, 50/50 split
SELECT 'influencers_total' AS check_name, COUNT(*) AS value FROM influencers;
-- expect: 100
SELECT platform, COUNT(*) FROM influencers GROUP BY platform;
-- expect: instagram 50, tiktok 50

-- 2. Follower provenance: no empty values, unknowns stay unknown
SELECT 'empty_followers' AS check_name, COUNT(*) AS value FROM influencers
WHERE followers_approx IS NULL OR TRIM(followers_approx) = '';
-- expect: 0
SELECT followers_approx, COUNT(*) FROM influencers GROUP BY followers_approx
ORDER BY 2 DESC LIMIT 5;

-- 3. Duplicate handles: expect zero
SELECT handle, platform, COUNT(*) FROM influencers
GROUP BY handle, platform HAVING COUNT(*) > 1;
-- expect: no rows

-- 4. Itinerary / item counts reconcile with gate1 report totals
SELECT 'itineraries_total' AS check_name, COUNT(*) AS value FROM itineraries;
SELECT 'items_total' AS check_name, COUNT(*) AS value FROM itinerary_items;
SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence;
-- compare against validation/reports/gate1_report.json batches[].itineraries

-- 5. Orphans: expect zero everywhere
SELECT 'orphan_items' AS check_name, COUNT(*) AS value FROM itinerary_items i
LEFT JOIN itineraries t ON t.id = i.itinerary_id WHERE t.id IS NULL;
-- expect: 0
SELECT 'orphan_itineraries' AS check_name, COUNT(*) AS value FROM itineraries t
LEFT JOIN influencers f ON f.id = t.influencer_id WHERE f.id IS NULL;
-- expect: 0
SELECT 'orphan_posts' AS check_name, COUNT(*) AS value FROM posts p
LEFT JOIN influencers f ON f.id = p.influencer_id WHERE f.id IS NULL;
-- expect: 0

-- 6. Every itinerary has >=1 source: expect zero violations
SELECT 'itineraries_without_source' AS check_name, COUNT(*) AS value FROM itineraries t
LEFT JOIN itinerary_sources s ON s.itinerary_id = t.id WHERE s.id IS NULL;
-- expect: 0

-- 7. Duplicate itineraries (same influencer, same title+destination): review list
SELECT influencer_id, title, destination, COUNT(*) FROM itineraries
GROUP BY influencer_id, title, destination HAVING COUNT(*) > 1;
-- expect: no rows (any row = manual review)

-- 8. Quarantined handles must not be attributed: expect zero itineraries
-- (fill in handles from validation/quarantine.json with status=quarantined)
SELECT 'quarantined_with_itineraries' AS check_name, COUNT(*) AS value
FROM itineraries t JOIN influencers f ON f.id = t.influencer_id
WHERE f.handle IN ('@africansafari', '@limsawkward', '@marklharriosn');
-- expect: 0 until a quarantine entry is explicitly released

-- 9. Distribution sanity
SELECT country, COUNT(*) FROM itineraries GROUP BY country ORDER BY 2 DESC LIMIT 15;
SELECT destination, COUNT(*) FROM itineraries GROUP BY destination ORDER BY 2 DESC LIMIT 15;
