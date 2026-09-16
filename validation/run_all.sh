#!/usr/bin/env bash
# Run validation gates 1-3, fail-fast. Reports -> validation/reports/
# Exit 0 only if every runnable gate passes.
set -u
cd "$(dirname "$0")/.."
mkdir -p validation/reports

run_gate() {
  local n="$1" script="$2"
  echo "== Gate $n =="
  if python3 "$script"; then
    echo "gate $n: PASS"
  else
    code=$?
    if [ "$code" -eq 2 ]; then
      echo "gate $n: NOT READY — inputs missing, stopping."
    else
      echo "gate $n: FAIL — fix the data and re-run. Stopping."
    fi
    exit "$code"
  fi
}

run_gate 1 validation/gate1_schema.py
run_gate 2 validation/gate2_handles.py
run_gate 3 validation/gate3_liveness.py

echo
echo "Gates 1-3 complete. Next: evidence council (gate 4) per evidence_council_brief.md,"
echo "then DB load, then: sqlite3 pilot.db < validation/gate4_reconciliation.sql"
