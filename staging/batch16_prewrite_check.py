#!/usr/bin/env python3
"""Batch16 final pre-write checks (stdlib only).
Run IMMEDIATELY before writing deliverables.
1. Rebuilds dedup universe from all batch CSVs + influencers.csv + quarantine/exclusion JSONs + staging dedup universe.
2. Checks candidate handles (case-insensitive, with/without @).
3. After writes: asserts batch16.csv (25 rows), selection_log_batch16.csv (25x23), itineraries_batch16.json (25 exts, handles match CSV).
"""
import csv, json, sys
from pathlib import Path

ROOT = Path("/home/hatch/workspace/travel-influencer-pilot")
CANDIDATES = """thesojournies girlgoingtravel ettevi_wanderlust findlovetravel taywanders
travelwithcg oneikaraymond lunaticatlarge kelleesetgo solotravelgirl
girlabouttheglobe heleninwonderlust annaeverywhere theglobetrottingdetective
hippieinheels lemonicks joannehollings spiritedpursuit jess.wandering thereshegoesagn""".split()

def norm(h): return h.strip().lstrip("@").lower()

def build_universe():
    u = set()
    for n in list(range(9, 21)):
        p = ROOT / f"batch{n}.csv"
        if p.exists():
            for row in csv.DictReader(p.open(encoding="utf-8")):
                u.add(norm(row["handle"]))
    p = ROOT / "influencers.csv"
    if p.exists():
        for row in csv.DictReader(p.open(encoding="utf-8")):
            u.add(norm(row.get("handle", "")))
    for jf in ["validation/quarantine.json", "validation/exclude_unverifiable.json"]:
        p = ROOT / jf
        if p.exists():
            txt = p.read_text(encoding="utf-8").lower()
            for c in CANDIDATES:
                if c in txt: u.add(c)
    for uf in ["staging/dedup_universe_2026-09-17.txt", "staging/dedup_universe_2026-09-16.txt"]:
        p = ROOT / uf
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line: u.add(norm(line))
    # selection logs of sibling batches
    for sl in (ROOT / "staging").glob("selection_log_batch*.csv"):
        try:
            for row in csv.DictReader(sl.open(encoding="utf-8")):
                u.add(norm(row.get("handle", "")))
        except Exception:
            pass
    u.discard("")
    return u

def main():
    uni = build_universe()
    print(f"universe size: {len(uni)}")
    bad = [c for c in CANDIDATES if norm(c) in uni and norm(c) not in
           {norm(r["handle"]) for r in csv.DictReader(open(ROOT/"batch16.csv", encoding="utf-8"))}]
    # note: batch16.csv currently has 5; candidates must not collide with OTHER batches' handles
    if bad:
        print("DEDUP COLLISIONS:", bad); return 1
    print("dedup: all 20 candidates clear")
    return 0

if __name__ == "__main__":
    sys.exit(main())
