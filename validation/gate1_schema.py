#!/usr/bin/env python3
"""Gate 1 — extraction schema validation (fail-closed).

Checks staging/itineraries_batch{1..4}.json against EXTRACTION_BRIEF.md and
cross-checks handle/platform against batch{1..4}.csv.

Exit codes: 0 PASS, 1 FAIL, 2 NOT READY (expected inputs missing).
Writes validation/reports/gate1_report.json. Stdlib only.
"""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stage_config import load as load_stage

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
REPORTS = ROOT / "validation" / "reports"

CONFIDENCES = {"high", "medium", "low"}
ITEM_TYPES = {"flight", "hotel", "activity", "restaurant", "transport", "other"}
STAGE = load_stage()
BATCHES = STAGE["batches"]
EXPECTED_FILES = {f"itineraries_batch{n}.json" for n in BATCHES}


def is_url(u):
    return (
        isinstance(u, str)
        and u.lower().startswith(("http://", "https://"))
        and bool(urlparse(u).netloc)
    )


def load_batch_csv(n):
    pairs = set()
    with open(ROOT / f"batch{n}.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pairs.add((row["handle"].strip(), row["platform"].strip().lower()))
    return pairs


def validate_batch(n):
    errors, warnings = [], []
    sp = STAGING / f"itineraries_batch{n}.json"
    result = {"batch": n, "status": "NOT READY", "extractions": 0, "itineraries": 0}

    if not sp.exists():
        result["reason"] = f"missing {sp.name}"
        return result, errors, warnings
    try:
        data = json.loads(sp.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"batch{n}: invalid JSON: {e}")
        result["status"] = "FAIL"
        return result, errors, warnings

    if not isinstance(data, dict) or data.get("batch") != n:
        errors.append(f"batch{n}: top-level 'batch' must equal {n}")
    exts = data.get("extractions")
    try:
        expected = load_batch_csv(n)
    except FileNotFoundError:
        errors.append(f"batch{n}: batch{n}.csv not found for cross-check")
        expected = set()
    # Expected extraction count = actual batch CSV size (Stage 2 accepted partial
    # batches per founder 2026-09-18; the old hardcoded 25 no longer applies).
    if not isinstance(exts, list) or (expected and len(exts) != len(expected)):
        got = len(exts) if isinstance(exts, list) else type(exts).__name__
        errors.append(f"batch{n}: 'extractions' must be a list of exactly {len(expected)} (got {got})")
        exts = exts if isinstance(exts, list) else []

    seen_handles = set()
    seen_itins = set()
    itin_count = 0
    for i, ex in enumerate(exts):
        tag = f"batch{n}[{i}]"
        if not isinstance(ex, dict):
            errors.append(f"{tag}: extraction must be an object")
            continue
        h = ex.get("handle")
        p = str(ex.get("platform", "")).lower()
        if not h or not p:
            errors.append(f"{tag}: missing handle/platform")
            continue
        if (h, p) in seen_handles:
            errors.append(f"{tag}: duplicate extraction for {h} ({p})")
        seen_handles.add((h, p))
        if expected and (h, p) not in expected:
            errors.append(f"{tag}: {h} ({p}) not in batch{n}.csv")
        if p not in ("tiktok", "instagram"):
            errors.append(f"{tag}: platform must be tiktok|instagram (got {p!r})")

        itins = ex.get("itineraries")
        if not isinstance(itins, list):
            errors.append(f"{tag}: 'itineraries' must be a list")
            continue
        if not isinstance(ex.get("notes"), str):
            warnings.append(f"{tag}: 'notes' should be a string")
        for j, it in enumerate(itins):
            itag = f"{tag}.itineraries[{j}]"
            itin_count += 1
            if not isinstance(it, dict):
                errors.append(f"{itag}: itinerary must be an object")
                continue
            for field in ("title", "summary"):
                v = it.get(field)
                if not isinstance(v, str) or not v.strip():
                    errors.append(f"{itag}: '{field}' must be a non-empty string")
            dest = it.get("destination")
            # destination may be null (unknown) per honesty rules — e.g. a general
            # guide with no single destination. DB schema allows null.
            if dest is not None and (not isinstance(dest, str) or not dest.strip()):
                errors.append(f"{itag}: 'destination' must be a non-empty string or null")
            country = it.get("country")
            if country is not None and (not isinstance(country, str) or not country.strip()):
                errors.append(f"{itag}: 'country' must be a non-empty string or null")
            days = it.get("days")
            if days is not None and (not isinstance(days, int) or isinstance(days, bool) or days <= 0):
                errors.append(f"{itag}: 'days' must be a positive integer or null")
            if it.get("confidence") not in CONFIDENCES:
                errors.append(f"{itag}: 'confidence' must be one of {sorted(CONFIDENCES)}")
            urls = it.get("source_urls")
            if not isinstance(urls, list) or not urls or not all(is_url(u) for u in urls):
                errors.append(f"{itag}: 'source_urls' must be a non-empty list of http(s) URLs")
            items = it.get("items")
            if not isinstance(items, list):
                errors.append(f"{itag}: 'items' must be a list")
                continue
            for k, item in enumerate(items):
                ktag = f"{itag}.items[{k}]"
                if not isinstance(item, dict):
                    errors.append(f"{ktag}: item must be an object")
                    continue
                if item.get("item_type") not in ITEM_TYPES:
                    errors.append(f"{ktag}: bad item_type {item.get('item_type')!r}")
                name = item.get("name")
                if not isinstance(name, str) or not name.strip():
                    errors.append(f"{ktag}: 'name' must be a non-empty string")
                day = item.get("day")
                if day is not None and (not isinstance(day, int) or isinstance(day, bool) or day <= 0):
                    errors.append(f"{ktag}: 'day' must be a positive integer or null")
                bl = item.get("booking_link")
                if bl is not None and not is_url(bl):
                    errors.append(f"{ktag}: 'booking_link' must be a URL or null")
            key = (str(it.get("title")).strip().lower(), str(it.get("destination")).strip().lower())
            if key in seen_itins:
                warnings.append(f"{itag}: possible duplicate title+destination within batch")
            seen_itins.add(key)

    result["extractions"] = len(exts)
    result["itineraries"] = itin_count
    result["status"] = "FAIL" if errors else "PASS"
    return result, errors, warnings


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    all_errors, all_warnings = [], []
    batches = []
    for n in BATCHES:
        res, errs, warns = validate_batch(n)
        batches.append(res)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    # Unexpected files in staging: workers checkpointing is fine, but the gate
    # only trusts the four canonical filenames. Anything else gets flagged.
    if STAGING.exists():
        for f in sorted(STAGING.glob("*.json")):
            if f.name not in EXPECTED_FILES:
                all_warnings.append(f"staging/{f.name}: non-canonical file ignored by gates")

    if any(b["status"] == "NOT READY" for b in batches):
        status, code = "NOT READY", 2
    elif all_errors:
        status, code = "FAIL", 1
    else:
        status, code = "PASS", 0

    report = {
        "gate": 1,
        "name": "extraction schema",
        "status": status,
        "batches": batches,
        "errors": all_errors,
        "warnings": all_warnings,
    }
    (REPORTS / "gate1_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"GATE 1 [{status}] errors={len(all_errors)} warnings={len(all_warnings)}")
    for e in all_errors[:20]:
        print("  FAIL:", e)
    if len(all_errors) > 20:
        print(f"  ... +{len(all_errors) - 20} more (see validation/reports/gate1_report.json)")
    return code


if __name__ == "__main__":
    sys.exit(main())
