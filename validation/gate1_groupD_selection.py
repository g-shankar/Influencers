#!/usr/bin/env python3
"""Scoped Gate 1 (selection-log integrity) for Group D engagement remediation.

For one batch n (18/19/20):
 1. Row count and handle order identical to pristine backup.
 2. No cell changed except engagement_observed for the batch's qualifying handles.
 3. Every qualifying engagement_observed cell names a source, an exact URL, and
    the observation date 2026-09-17.
 4. Every non-qualifying Group D handle retains its prior cell value verbatim.
Exit 0 PASS, 1 FAIL. Writes validation/reports/gate1_groupD_batch{n}.json.
Stdlib only.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
PRISTINE = STAGING / "_pristine_groupD_20260917"
REPORTS = ROOT / "validation" / "reports"

QUALIFIED = {
    18: ["@sarowly", "@indianahannah_blog", "@bucketlistjourney", "@absolutelylucy"],
    19: ["@jessica_traveler", "@marissa.daily", "@travelrealizations", "@liveloveruntravel"],
    20: ["@vickyflipflop", "@expertvagabond"],
}
GROUPD = {
    18: ["@sarowly", "@indianahannah_blog", "@bucketlistjourney", "@absolutelylucy",
         "@learningescapes", "@malaysiaasia"],
    19: ["@jessica_traveler", "@marissa.daily", "@travelrealizations", "@liveloveruntravel",
         "@wheretarawent", "@thetravelbunny", "@adventuresfromelle", "@tomiko.harvey",
         "@minoritynomad", "@travelingblackwidow", "@thereshegoesagn"],
    20: ["@vickyflipflop", "@expertvagabond", "@kirstenalana", "@em_luxton",
         "@findingalexx", "@girlgoneabroad"],
}
URL = re.compile(r"https://\S+")
DATE = "2026-09-17"


def run(n):
    errors, warnings = [], []
    with open(PRISTINE / f"selection_log_batch{n}.csv", encoding="utf-8") as f:
        old = list(csv.DictReader(f))
    with open(STAGING / f"selection_log_batch{n}.csv", encoding="utf-8") as f:
        new = list(csv.DictReader(f))
    if len(old) != len(new):
        errors.append(f"batch{n}: row count {len(old)} -> {len(new)}")
    if [r["handle"] for r in old] != [r["handle"] for r in new]:
        errors.append(f"batch{n}: handle order changed")
    fields = list(old[0].keys())
    oldm = {r["handle"]: r for r in old}
    newm = {r["handle"]: r for r in new}
    for h in GROUPD[n]:
        if h not in newm:
            errors.append(f"batch{n} {h}: handle missing after edit")
            continue
    for i, (o, nw) in enumerate(zip(old, new)):
        for f_ in fields:
            if o[f_] != nw[f_]:
                tag = f"batch{n} row{i+2} {o['handle']}[{f_}]"
                if o["handle"] in QUALIFIED[n] and f_ == "engagement_observed":
                    v = nw[f_]
                    if DATE not in v:
                        errors.append(f"{tag}: edited cell lacks observation date {DATE}")
                    if not URL.search(v):
                        errors.append(f"{tag}: edited cell lacks an exact URL")
                else:
                    errors.append(f"{tag}: UNEXPECTED change (non-target cell)")
    for h in QUALIFIED[n]:
        v = newm[h]["engagement_observed"]
        if oldm[h]["engagement_observed"] == v:
            errors.append(f"batch{n} {h}: expected engagement_observed update, none found")
    for h in GROUPD[n]:
        if h not in QUALIFIED[n] and h in oldm and h in newm:
            if oldm[h]["engagement_observed"] != newm[h]["engagement_observed"]:
                errors.append(f"batch{n} {h}: non-qualifying handle cell changed")
    # handle integrity vs root batch CSV (handles must still exist)
    bcsv = ROOT / f"batch{n}.csv"
    if bcsv.exists():
        have = {(r["handle"].strip(), r["platform"].strip().lower())
                for r in csv.DictReader(open(bcsv, encoding="utf-8"))}
        for h in GROUPD[n]:
            p = newm[h]["platform"].strip().lower()
            if (h, p) not in have:
                warnings.append(f"batch{n} {h}: handle/platform not in root batch{n}.csv")
    status = "FAIL" if errors else "PASS"
    res = {
        "gate": "1-scoped",
        "remediation_group": "D",
        "batch": n,
        "status": status,
        "rows": len(new),
        "qualified_updated": QUALIFIED[n],
        "remove_candidates_unchanged": [h for h in GROUPD[n] if h not in QUALIFIED[n]],
        "errors": errors,
        "warnings": warnings,
    }
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / f"gate1_groupD_batch{n}.json").write_text(
        json.dumps(res, indent=2), encoding="utf-8")
    print(f"GATE 1-scoped batch{n} [{status}] errors={len(errors)} warnings={len(warnings)}")
    for e in errors:
        print("  FAIL:", e)
    for w in warnings:
        print("  WARN:", w)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    n = int(sys.argv[1])
    sys.exit(run(n))
