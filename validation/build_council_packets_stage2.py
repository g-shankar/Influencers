#!/usr/bin/env python3
"""Build Gate 4 evidence-council claim packets for Stage 2 batches (9-20).

Per validation/evidence_council_brief.md each packet carries ONLY the claim
(handle, platform, title, destination, country, days, summary, items,
source_urls, confidence) - no worker notes, no transcripts, no reasoning.
Reviewers must be fresh-context and a genuinely different model family from
the builders; if that requirement cannot be met, Gate 4 is NOT VERIFIED.

Writes validation/council_packets/stage2_batch<N>_packets.json for each
Stage 2 batch, plus a stratified sample manifest
(>=30% of itineraries, spread across all batches and confidence levels,
oversampling low) at validation/council_packets/stage2_sample_manifest.json.

Stdlib only.
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
OUT = ROOT / "validation" / "council_packets"

sys.path.insert(0, str(ROOT))
from stage_config import load as load_stage

STAGE2_BATCHES = [n for n in load_stage()["batches"] if n >= 9]

ITEM_FIELDS = ["day", "item_type", "name", "location", "details",
               "booking_link", "price_hint"]


def build_packets():
    packets = {}  # batch -> [packet]
    for n in STAGE2_BATCHES:
        f = STAGING / f"itineraries_batch{n}.json"
        data = json.loads(f.read_text(encoding="utf-8"))
        batch_packets = []
        for ex in data.get("extractions", []):
            for it in ex.get("itineraries", []):
                batch_packets.append({
                    "batch": n,
                    "handle": ex.get("handle"),
                    "platform": ex.get("platform"),
                    "title": it.get("title"),
                    "destination": it.get("destination"),
                    "country": it.get("country"),
                    "days": it.get("days"),
                    "summary": it.get("summary"),
                    "items": [{k: item.get(k) for k in ITEM_FIELDS}
                              for item in it.get("items", [])],
                    "source_urls": it.get("source_urls", []),
                    "confidence": it.get("confidence"),
                })
        packets[n] = batch_packets
    return packets


def stratified_sample(packets, seed=20260918):
    """>=30% of itineraries, spread across all batches and confidence
    levels, oversampling low confidence. Returns list of (batch, idx)."""
    rng = random.Random(seed)
    # group by (batch, confidence)
    groups = {}
    for n, plist in packets.items():
        for i, p in enumerate(plist):
            groups.setdefault((n, p.get("confidence") or "unknown"), []).append(i)
    sample = set()
    for (n, conf), idxs in sorted(groups.items()):
        # low confidence: take 60%; else 30%
        frac = 0.6 if conf == "low" else 0.3
        k = max(1, round(len(idxs) * frac)) if idxs else 0
        sample.update((n, i) for i in rng.sample(idxs, min(k, len(idxs))))
    # ensure overall >= 30%
    total = sum(len(v) for v in packets.values())
    target = max(1, round(total * 0.30))
    if len(sample) < target:
        remaining = [(n, i) for n, plist in packets.items()
                     for i in range(len(plist)) if (n, i) not in sample]
        rng.shuffle(remaining)
        sample.update(remaining[:target - len(sample)])
    return sorted(sample)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    packets = build_packets()
    total = sum(len(v) for v in packets.values())
    for n, plist in packets.items():
        (OUT / f"stage2_batch{n}_packets.json").write_text(
            json.dumps({"batch": n, "packets": plist,
                        "built": "2026-09-18",
                        "note": "Claim packets only (no worker notes/transcripts). "
                                "Reviewers must be fresh-context and a different "
                                "model family from the builders."},
                       indent=2, ensure_ascii=False),
            encoding="utf-8")
    sample = stratified_sample(packets)
    by_conf, by_batch = {}, {}
    for n, i in sample:
        c = packets[n][i].get("confidence") or "unknown"
        by_conf[c] = by_conf.get(c, 0) + 1
        by_batch[n] = by_batch.get(n, 0) + 1
    (OUT / "stage2_sample_manifest.json").write_text(json.dumps({
        "built": "2026-09-18",
        "method": "stratified sample: >=30% of itineraries across all Stage 2 "
                  "batches and confidence levels, low confidence oversampled "
                  "at 60%; deterministic seed 20260918",
        "total_itineraries": total,
        "sample_size": len(sample),
        "sample_fraction": round(len(sample) / total, 4) if total else 0,
        "by_confidence": by_conf,
        "by_batch": by_batch,
        "sample": [{"batch": n, "packet_index": i,
                    "handle": packets[n][i]["handle"],
                    "title": packets[n][i]["title"],
                    "confidence": packets[n][i]["confidence"]}
                   for n, i in sample],
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"packets: {total} itineraries across {len(packets)} batches; "
          f"sample={len(sample)} "
          f"({round(len(sample)/total*100, 1) if total else 0}%)")


if __name__ == "__main__":
    main()
