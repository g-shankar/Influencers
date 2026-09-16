#!/usr/bin/env python3
"""Gate 2 — influencer handle integrity (fail-closed).

Checks influencers.csv: exactly 100 data rows, 50/50 platform split,
unique (handle, platform), handle format, non-empty provenance fields,
and applies validation/quarantine.json.

Exit codes: 0 PASS (quarantine items reported, not failed), 1 FAIL,
2 NOT READY. Writes validation/reports/gate2_report.json. Stdlib only.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "validation" / "reports"
HANDLE_RE = re.compile(r"^@[A-Za-z0-9._-]{1,64}$")


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    errors, warnings = [], []
    csv_path = ROOT / "influencers.csv"
    if not csv_path.exists():
        report = {"gate": 2, "name": "handle integrity", "status": "NOT READY",
                  "errors": ["influencers.csv missing"], "warnings": []}
        (REPORTS / "gate2_report.json").write_text(json.dumps(report, indent=2))
        print("GATE 2 [NOT READY] influencers.csv missing")
        return 2

    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if len(rows) != 100:
        errors.append(f"expected 100 influencer rows, got {len(rows)}")

    platforms = {}
    seen = set()
    for i, r in enumerate(rows):
        tag = f"row{i + 2}"
        h, p = r.get("handle", "").strip(), r.get("platform", "").strip().lower()
        platforms[p] = platforms.get(p, 0) + 1
        if p not in ("tiktok", "instagram"):
            errors.append(f"{tag}: bad platform {p!r}")
        if not HANDLE_RE.match(h):
            errors.append(f"{tag}: malformed handle {h!r}")
        if (h, p) in seen:
            errors.append(f"{tag}: duplicate handle+platform {h} ({p})")
        seen.add((h, p))
        if not r.get("name", "").strip():
            errors.append(f"{tag}: empty name")
        if not r.get("followers_approx", "").strip():
            errors.append(f"{tag}: empty followers_approx (must be a value or 'unknown')")
        pu = r.get("profile_url", "").strip()
        if pu and not pu.lower().startswith(("http://", "https://")):
            errors.append(f"{tag}: bad profile_url {pu!r}")

    if platforms.get("tiktok", 0) != 50 or platforms.get("instagram", 0) != 50:
        errors.append(f"platform split must be 50/50, got {platforms}")

    # Quarantine application
    qpath = ROOT / "validation" / "quarantine.json"
    quarantined = []
    checklist = []
    if qpath.exists():
        qdata = json.loads(qpath.read_text(encoding="utf-8"))
        for q in qdata.get("quarantine", []):
            key = (q["handle"], q["platform"])
            if key not in seen:
                warnings.append(f"quarantine entry {q['handle']} ({q['platform']}) not in influencers.csv")
                continue
            if q.get("status") == "quarantined":
                quarantined.append(q)
                base = ("https://www.tiktok.com/" if q["platform"] == "tiktok"
                        else "https://www.instagram.com/") + q["handle"].lstrip("@")
                checklist.append({"handle": q["handle"], "platform": q["platform"],
                                  "reason": q["reason"], "check_url": base})
    else:
        warnings.append("quarantine.json missing — skipping quarantine check")

    status = "FAIL" if errors else "PASS"
    report = {
        "gate": 2,
        "name": "handle integrity",
        "status": status,
        "rows": len(rows),
        "platforms": platforms,
        "quarantined": quarantined,
        "manual_checklist": checklist,
        "errors": errors,
        "warnings": warnings,
    }
    (REPORTS / "gate2_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"GATE 2 [{status}] rows={len(rows)} quarantined={len(quarantined)} "
          f"errors={len(errors)} warnings={len(warnings)}")
    for e in errors[:20]:
        print("  FAIL:", e)
    for q in quarantined:
        print(f"  QUARANTINED: {q['handle']} ({q['platform']}) — {q['reason']}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
