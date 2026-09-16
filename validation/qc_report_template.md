# Pilot QC Report — founder validation copy

Date: __________
Validator: __________

## Gate verdicts

| Gate | Check | Verdict | Evidence |
|------|-------|---------|----------|
| 1 | Extraction schema | PASS / FAIL / NOT READY | `validation/reports/gate1_report.json` |
| 2 | Handle integrity | PASS / FAIL | `validation/reports/gate2_report.json` |
| 3 | Source liveness | PASS / FAIL | `validation/reports/gate3_report.json` |
| 4 | Evidence council | PASS / FAIL (fail rate ___%) | council verdict table (link) |
| 5 | DB reconciliation | PASS / FAIL | `sqlite3 pilot.db < validation/gate4_reconciliation.sql` output |
| 6 | Money firewall | PASS / FAIL | every $ figure tagged FACT/MODEL |
| 7 | Final evidence-only audit | PASS / FAIL | `~/workspace/audit/CHARTER.md` verdict |

All seven must be PASS. Any FAIL blocks the completion claim.

## Counts (verify against gate1 + gate5)
- Influencers: ___ (tiktok ___ / instagram ___)
- With source-reported follower counts: ___ / unknown: ___
- Influencers yielding ≥1 itinerary: ___
- Itineraries: ___ / items: ___
- Confidence: high ___ / medium ___ / low ___

## Quarantine
| Handle | Platform | Reason | Status |
|--------|----------|--------|--------|
| @africansafari | instagram | possible brand account | quarantined / released |
| @limsawkward | tiktok | possible typo | quarantined / released |
| @marklharriosn | tiktok | possible typo | quarantined / released |

## Evidence sample (spot-check these yourself)
| # | Itinerary | Source URL | Council verdict |
|---|-----------|------------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Open issues
- (anything FAIL, UNVERIFIABLE, or waived — with reason and who approved)

## Check it yourself (SQLite)
```bash
cd ~/workspace/travel-influencer-pilot
sqlite3 pilot.db "SELECT platform, COUNT(*) FROM influencers GROUP BY platform;"
sqlite3 pilot.db "SELECT confidence, COUNT(*) FROM itineraries GROUP BY confidence;"
sqlite3 pilot.db "SELECT destination, COUNT(*) FROM itineraries GROUP BY destination ORDER BY 2 DESC LIMIT 10;"
```
