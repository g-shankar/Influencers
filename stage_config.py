#!/usr/bin/env python3
"""Shared stage configuration loader (stdlib only).

Reads stage.json at the pilot root. Single source of truth for stage targets
so no script hardcodes creator counts, platform quotas, or batch ranges.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]


def load():
    cfg = json.loads((ROOT / "stage.json").read_text(encoding="utf-8"))
    cfg["batches"] = list(cfg["batches"])
    return cfg


if __name__ == "__main__":
    print(json.dumps(load(), indent=2))
