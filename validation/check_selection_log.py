#!/usr/bin/env python3
"""Convergence pre-check: selection-log integrity (fail-closed).

For every row in staging/selection_batch{N}.csv (N in stage.json new_batches):
- exactly stage.json batch_size rows per batch
- decision=include requires ALL of: identity_check=pass, content_fit=pass,
  reach_floor=pass, activity_check=pass, exclusions_check=pass
- handle/platform match the corresponding batch{N}.csv
- no case-insensitive handle collisions vs pilot or across new batches
- check_date and selector present

Exit 0 only if every included row fully passes. Writes
validation/reports/selection_check.json. Stdlib only.
"""
import csv
import json
import sys
from pathlib import Path

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stage_config import load as load_stage

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
REPORTS = ROOT / "validation" / "reports"

REQUIRED_PASS = ["identity_check", "content_fit", "reach_floor",
                 "activity_check", "exclusions_check"]


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    stage = load_stage()
    errors, warnings = [], []
    batches = {}

    pilot = set()
    ph = STAGING / "pilot_handles.txt"
    if ph.exists():
        pilot = {l.strip().lower() for l in ph.read_text().splitlines() if l.strip()}

    seen_new = {}
    for n in stage["new_batches"]:
        sp = STAGING / f"selection_batch{n}.json".replace(".json", ".csv")
        sp = STAGING / f"selection_batch{n}.csv"
        bcsv = ROOT / f"batch{n}.csv"
        result = {"batch": n, "rows": 0, "included": 0, "non_passing": []}
        if not sp.exists():
            errors.append(f"batch{n}: staging/selection_batch{n}.csv missing")
            batches[n] = result
            continue
        rows = list(csv.DictReader(sp.read_text(encoding="utf-8").splitlines()))
        result["rows"] = len(rows)
        if len(rows) != stage["batch_size"]:
            errors.append(f"batch{n}: expected {stage['batch_size']} selection rows, got {len(rows)}")
        brow_handles = set()
        if bcsv.exists():
            brow_handles = {(r["handle"].strip(), r["platform"].strip().lower())
                            for r in csv.DictReader(bcsv.read_text(encoding="utf-8").splitlines())}
        for i, r in enumerate(rows):
            tag = f"batch{n} row{i + 2} ({r.get('handle', '?')})"
            h = (r.get("handle") or "").strip()
            p = (r.get("platform") or "").strip().lower()
            if str(n) != (r.get("batch") or "").strip():
                errors.append(f"{tag}: batch column != {n}")
            if (h, p) not in brow_handles:
                errors.append(f"{tag}: handle/platform not in batch{n}.csv")
            if not (r.get("check_date") or "").strip():
                errors.append(f"{tag}: missing check_date")
            if not (r.get("selector") or "").strip():
                errors.append(f"{tag}: missing selector")
            hl = h.lower()
            if hl in pilot:
                errors.append(f"{tag}: handle collides with pilot dataset")
            if hl in seen_new:
                errors.append(f"{tag}: handle collides with batch{seen_new[hl]}")
            seen_new[hl] = n
            if (r.get("decision") or "").strip().lower() == "include":
                result["included"] += 1
                failing = [c for c in REQUIRED_PASS
                           if (r.get(c) or "").strip().lower() != "pass"]
                if failing:
                    result["non_passing"].append({"handle": h, "failing": failing,
                                                  "notes": (r.get("notes") or "")[:200]})
                    warnings.append(f"{tag}: decision=include but {failing} != pass")
        batches[n] = result

    # fail-closed: any included-but-not-passing row is an error
    for n, b in batches.items():
        for np_ in b["non_passing"]:
            errors.append(f"batch{n} {np_['handle']}: included without passing {np_['failing']}")

    status = "FAIL" if errors else "PASS"
    (REPORTS / "selection_check.json").write_text(json.dumps(
        {"status": status, "batches": batches, "errors": errors,
         "warnings": warnings}, indent=2), encoding="utf-8")
    print(f"SELECTION CHECK [{status}] errors={len(errors)} warnings={len(warnings)}")
    for e in errors[:25]:
        print("  FAIL:", e)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
