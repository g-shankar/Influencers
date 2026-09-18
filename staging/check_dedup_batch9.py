#!/usr/bin/env python3
"""Dedup check for batch9 topup worker: case-insensitive handle lookup across
influencers.csv, dedup_universe_2026-09-17.txt, quarantine.json,
exclude_unverifiable.json, and all batch CSVs."""
import csv, json, sys
from pathlib import Path

ROOT = Path("/home/hatch/workspace/travel-influencer-pilot")
seen = {}

def add(h, src):
    k = h.strip().lstrip("@").lower()
    if k:
        seen.setdefault(k, []).append(src)

for p in [ROOT / "influencers.csv"] + sorted(ROOT.glob("batch*.csv")):
    try:
        for row in csv.DictReader(p.open(encoding="utf-8")):
            h = row.get("handle") or ""
            if h:
                add(h, p.name)
    except FileNotFoundError:
        pass

for line in (ROOT / "staging/dedup_universe_2026-09-17.txt").read_text().splitlines():
    add(line, "dedup_universe_2026-09-17.txt")

try:
    q = json.loads((ROOT / "validation/quarantine.json").read_text())
    for e in q.get("quarantine", []):
        add(e.get("handle", ""), "quarantine.json")
except Exception:
    pass
try:
    ex = json.loads((ROOT / "validation/exclude_unverifiable.json").read_text())
    items = ex if isinstance(ex, list) else ex.get("exclusions", [])
    for e in items:
        if isinstance(e, dict) and e.get("handle"):
            add(e["handle"], "exclude_unverifiable.json")
except Exception:
    pass

for h in sys.argv[1:]:
    k = h.strip().lstrip("@").lower()
    srcs = seen.get(k)
    print(("COLLISION: " if srcs else "CLEAR: ") + h + (f"  <- {sorted(set(srcs))}" if srcs else ""))
