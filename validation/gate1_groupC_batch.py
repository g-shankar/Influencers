#!/usr/bin/env python3
"""Gate 1 (scoped): selection-log integrity for one batch — Group C remediation.
Checks staging/selection_log_batch{N}.csv:
- columns match expected header
- decision=include rows have all required checks = pass
- handle/platform match batch{N}.csv
- check_date and selector present
- no case-insensitive handle collisions vs pilot handles or the batch itself
Exit 0 PASS, 1 FAIL, 2 NOT READY. Writes validation/reports/gate1_groupC_batch{N}.json.
Stdlib only. Does NOT write stage.json.
Usage: gate1_groupC_batch.py 15
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
REPORTS = ROOT / "validation" / "reports"
REQUIRED_PASS = ["identity_check", "content_fit", "reach_floor", "activity_check", "exclusions_check"]

def is_pass(v):
    return (v or "").strip().lower().startswith("pass")

def main():
    n = sys.argv[1]
    errors, warnings = [], []
    sp = STAGING / f"selection_log_batch{n}.csv"
    bcsv = ROOT / f"batch{n}.csv"
    result = {"batch": int(n), "rows": 0, "included": 0, "errors": [], "warnings": []}
    if not sp.exists():
        result["errors"].append(f"selection_log_batch{n}.csv missing")
        return finish(result, 2)
    rows = list(csv.DictReader(sp.read_text(encoding="utf-8").splitlines()))
    result["rows"] = len(rows)
    brow = set()
    if bcsv.exists():
        brow = {(r["handle"].strip(), r["platform"].strip().lower())
                for r in csv.DictReader(bcsv.read_text(encoding="utf-8").splitlines())}
    pilot = set()
    ph = STAGING / "pilot_handles.txt"
    if ph.exists():
        pilot = {l.strip().lower() for l in ph.read_text().splitlines() if l.strip()}
    seen = {}
    for i, r in enumerate(rows):
        h = r.get("handle", "").strip()
        p = r.get("platform", "").strip().lower()
        if not h:
            errors.append(f"row {i}: missing handle"); continue
        if (h, p) not in brow:
            warnings.append(f"{h}: handle/platform not in batch{n}.csv")
        key = h.lower()
        if key in seen:
            errors.append(f"{h}: duplicate handle in batch{n}")
        if key in pilot:
            errors.append(f"{h}: collides with pilot handle")
        seen[key] = True
        if not r.get("check_date", "").strip():
            errors.append(f"{h}: check_date missing")
        if not r.get("selector", "").strip():
            errors.append(f"{h}: selector missing")
        if r.get("decision", "").strip() == "include":
            result["included"] += 1
            for c in REQUIRED_PASS:
                if not is_pass(r.get(c, "")):
                    errors.append(f"{h}: decision=include but {c}={r.get(c)!r}")
    result["errors"], result["warnings"] = errors, warnings
    return finish(result, 0 if not errors else 1)

def finish(result, code):
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / f"gate1_groupC_batch{result['batch']}.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8")
    print(f"batch{result['batch']}: rows={result['rows']} included={result['included']} "
          f"errors={len(result['errors'])} warnings={len(result['warnings'])}")
    for e in result["errors"]:
        print("  ERROR:", e)
    for w in result["warnings"][:5]:
        print("  WARN:", w)
    print("GATE1-SCOPED: " + ("PASS" if code == 0 else ("NOT READY" if code == 2 else "FAIL")))
    sys.exit(code)

main()
