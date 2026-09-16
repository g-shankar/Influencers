#!/usr/bin/env python3
"""Gate 3 — source URL liveness (fail-closed).

For every itinerary in the four canonical staging files, fetches each
source_url and records reachability. An itinerary with ZERO reachable
sources fails the gate.

Caveat, stated plainly: some sites block bots, so UNREACHABLE here means
"not fetchable by script" — the evidence council (gate 4 brief) does the
human check in a real browser. Nothing marked unreachable is silently passed.

Exit codes: 0 PASS, 1 FAIL, 2 NOT READY. Writes
validation/reports/gate3_report.json. Stdlib only.
"""
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "staging"
REPORTS = ROOT / "validation" / "reports"
TIMEOUT = 12
WORKERS = 8
UA = {"User-Agent": "Mozilla/5.0 (pilot-validation-gate3; contact: pilot)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return url, r.status, None
    except Exception as e:  # noqa: BLE001 - HEAD often blocked; retry GET
        try:
            req = urllib.request.Request(url, headers=UA, method="GET")
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                r.read(65536)
                return url, r.status, None
        except Exception as e2:  # noqa: BLE001
            return url, None, f"{type(e2).__name__}: {e2}"


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    files = [STAGING / f"itineraries_batch{n}.json" for n in range(1, 5)]
    missing = [f.name for f in files if not f.exists()]
    if missing:
        report = {"gate": 3, "name": "source liveness", "status": "NOT READY",
                  "errors": [f"missing staging files: {missing}"], "warnings": []}
        (REPORTS / "gate3_report.json").write_text(json.dumps(report, indent=2))
        print(f"GATE 3 [NOT READY] missing: {missing}")
        return 2

    itineraries = []  # (batch, handle, title, [urls])
    for n, f in enumerate(files, start=1):
        data = json.loads(f.read_text(encoding="utf-8"))
        for ex in data.get("extractions", []):
            for it in ex.get("itineraries", []):
                itineraries.append((n, ex.get("handle"), it.get("title"),
                                    it.get("source_urls", [])))

    urls = sorted({u for _, _, _, us in itineraries for u in us})
    results = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for url, status, err in pool.map(fetch, urls):
            results[url] = {"status": status, "error": err,
                            "reachable": status is not None and 200 <= status < 400}

    errors, warnings, overridden = [], [], []
    dead_itins = []
    overrides = {}
    ovf = REPORTS / "gate3_override_evidence.json"
    if ovf.exists():
        odata = json.loads(ovf.read_text(encoding="utf-8"))
        for o in odata.get("overrides", []):
            overrides[(o["batch"], o["handle"], o["title"])] = o.get("verified_urls", [])
    for n, handle, title, us in itineraries:
        live = [u for u in us if results.get(u, {}).get("reachable")]
        dead = [u for u in us if not results.get(u, {}).get("reachable")]
        if not live:
            ov = overrides.get((n, handle, title), [])
            ov_urls = {e["url"] for e in ov}
            if ov and ov_urls.issubset(set(us)):
                overridden.append({
                    "batch": n, "handle": handle, "title": title,
                    "verified_by_manual_browser_fetch": sorted(ov_urls),
                    "script_statuses": {u: results.get(u, {}).get("status") for u in us},
                    "evidence_file": "validation/reports/gate3_override_evidence.json",
                })
                continue
            dead_itins.append({"batch": n, "handle": handle, "title": title, "urls": us})
            errors.append(f"batch{n} {handle} '{title}': zero reachable sources")
        elif dead:
            warnings.append(f"batch{n} {handle} '{title}': {len(dead)} unreachable URL(s), "
                            f"{len(live)} reachable")

    status = "FAIL" if errors else "PASS"
    report = {
        "gate": 3,
        "name": "source liveness",
        "status": status,
        "itineraries_checked": len(itineraries),
        "urls_checked": len(urls),
        "urls_reachable": sum(1 for r in results.values() if r["reachable"]),
        "dead_itineraries": dead_itins,
        "overridden_script_false_negatives": overridden,
        "url_results": results,
        "errors": errors,
        "warnings": warnings,
        "caveat": "UNREACHABLE means not fetchable by script (bot-blocking possible); "
                  "the evidence council verifies these in a real browser before any waiver.",
    }
    (REPORTS / "gate3_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"GATE 3 [{status}] itineraries={len(itineraries)} urls={len(urls)} "
          f"reachable={report['urls_reachable']} errors={len(errors)}")
    for e in errors[:20]:
        print("  FAIL:", e)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
