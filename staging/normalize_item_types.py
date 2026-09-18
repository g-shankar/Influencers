#!/usr/bin/env python3
"""Normalize invalid item_type values in staging/itineraries_batch*.json to the
Gate 1 allowlist {flight, hotel, activity, restaurant, transport, other}.
Run AFTER all top-up workers complete, BEFORE the final Gate 1-7 run.
Writes a report of every change to validation/reports/item_type_normalization.json.
Stdlib only. Idempotent.
"""
import json
import glob
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[0]
STAGING = ROOT / "staging"
REPORTS = ROOT / "validation" / "reports"

ALLOW = {"flight", "hotel", "activity", "restaurant", "transport", "other"}

# Conservative mapping: attraction/experience/place -> activity if it names an
# attraction-like thing is risky; safest honest mapping:
#   attraction -> activity (a visited attraction is an activity)
#   experience -> activity
#   place -> other (generic)
#   guide -> other (a guide reference is not a bookable item)
#   destination -> other
MAP = {
    "attraction": "activity",
    "experience": "activity",
    "place": "other",
    "guide": "other",
    "destination": "other",
    "sight": "activity",
    "tour": "activity",
    "food": "restaurant",
    "stay": "hotel",
    "transportation": "transport",
}

def main():
    changes = []
    counts = Counter()
    bl_fixes = 0
    files = sorted(glob.glob(str(STAGING / "itineraries_batch*.json")))
    for f in files:
        p = Path(f)
        data = json.loads(p.read_text(encoding="utf-8"))
        dirty = False
        for e in data.get("extractions", []):
            for it in e.get("itineraries", []) or []:
                for item in it.get("items", []) or []:
                    t = item.get("item_type")
                    if t not in ALLOW:
                        new_t = MAP.get(str(t).lower().strip(), "other")
                        changes.append({
                            "file": p.name,
                            "handle": e.get("handle"),
                            "itinerary": (it.get("title") or "")[:60],
                            "item": (item.get("name") or "")[:60],
                            "from": t, "to": new_t,
                        })
                        item["item_type"] = new_t
                        counts[(t, new_t)] += 1
                        dirty = True
                    # Gate 1 requires booking_link to be a URL or null;
                    # empty strings fail. Normalize "" -> None.
                    if item.get("booking_link") == "":
                        item["booking_link"] = None
                        bl_fixes += 1
                        dirty = True
        if dirty:
            p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = {
        "total_changes": len(changes),
        "booking_link_empty_to_null": bl_fixes,
        "mapping_counts": {f"{a}->{b}": c for (a, b), c in sorted(counts.items())},
        "changes": changes,
    }
    (REPORTS / "item_type_normalization.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"normalized {len(changes)} items across {len(files)} files")
    for (a, b), c in sorted(counts.items()):
        print(f"  {a} -> {b}: {c}")

if __name__ == "__main__":
    main()
