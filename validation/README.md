# Validation Harness — travel influencer pilot

Fail-closed validation between extraction and the database. Nothing loads into
`pilot.db` until every gate passes. Gate order is deliberate: each gate is
cheap, mechanical, and must pass before the expensive human verification runs.

## Gates

| Gate | What | How | Blocks on |
|------|------|-----|-----------|
| 1 | Extraction schema | `gate1_schema.py` | bad JSON, wrong counts, handle/platform mismatch vs batch CSVs, missing source URLs, bad enums, invented-shaped fields |
| 2 | Handle integrity | `gate2_handles.py` + `quarantine.json` | dupes, malformed handles, quarantined handles not yet re-verified |
| 3 | Source liveness | `gate3_liveness.py` | itineraries with zero reachable source URLs (bot-blocked URLs are flagged, not silently passed) |
| 4 | Evidence council | `evidence_council_brief.md` (fresh-context verifiers) | claim-vs-source mismatches; sample escalates to 100% if fail rate > 10% |
| 5 | DB reconciliation | `gate4_reconciliation.sql` | count mismatches, orphans, dupes, missing provenance |
| 6 | Money firewall | `gate5_money_firewall.md` | any dollar figure presented without a FACT/MODEL tag |
| 7 | Final evidence-only audit | `~/workspace/audit/CHARTER.md` | anything the auditor can't verify from files on disk |

## Running

```bash
./validation/run_all.sh        # gates 1-3, fail-fast, reports -> validation/reports/
sqlite3 pilot.db < validation/gate4_reconciliation.sql   # gate 5, after load
```

Gate 4 (evidence council) is launched as fresh-context subagents using
`evidence_council_brief.md` — verifiers get claim + source URL only, never the
builder's notes or transcript.

## Founder validation

`qc_report_template.md` is the report you open to validate the pilot yourself:
per-gate PASS/FAIL, quarantine list, sample evidence links, open issues, and
the exact SQLite commands to check the DB by hand. You are never the first
pair of eyes, but you can always be a pair.

## Rules

- FAIL is fail-closed: fix the data, re-run the gate, never waive.
- NOT READY (inputs missing) is not a pass.
- Unknowns stay unknown. Source-dated follower counts are never "refreshed".
- Quarantined handles (`quarantine.json`) never enter outreach or attribution
  until re-verified and explicitly released.
