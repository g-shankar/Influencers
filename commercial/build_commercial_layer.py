#!/usr/bin/env python3
"""Build the commercial prototype layer: 3 complete package structures + per-trip P&L skeletons.

Reads the verified research DB (pilot.db, read-only) and writes commercial/packages.db.

Every supplier-dependent field is explicitly unknown: no supplier access exists yet,
no commercial terms have been agreed, no prices have been fetched. The structure is
complete; the numbers fill in the moment supplier access is granted (Step 5).

Re-run safe: drops and rebuilds the commercial tables from scratch.
"""
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PILOT_DB = ROOT / "pilot.db"
OUT_DB = Path(__file__).resolve().parent / "packages.db"

# (itinerary_id, package name, why this one)
PACKAGES = [
    (42, "Morocco in Two Weeks — creator-led package",
     "15 days, 36 items, high confidence, fully claim-verified 2026-09-16. "
     "International classic; tests the long-haul package thesis."),
    (75, "Japan in Two Weeks — creator-led package",
     "14 days, 49 items, high confidence, fully claim-verified 2026-09-16. "
     "Highest item density; tests activity-heavy packaging."),
    (65, "Oregon to California Coast Road Trip — creator-led package",
     "4 days, 8 items, high confidence, domestic. Low complexity; "
     "tests the short domestic trip thesis."),
]

SUPPLIER_FOR = {
    "flight": "Duffel",
    "hotel": "Booking.com",
    "activity": "Viator",
    "restaurant": "OpenTable",
    "transport": None,   # supplier TBD — no partner identified yet
    "other": None,       # not a bookable component
}

ECONOMIC_LINES = [
    ("supplier_cost_flights", "cost", "SUM of flight component costs"),
    ("supplier_cost_hotels", "cost", "SUM of hotel component costs"),
    ("supplier_cost_activities", "cost", "SUM of activity component costs"),
    ("supplier_cost_dining", "cost", "SUM of restaurant component costs"),
    ("supplier_cost_transport", "cost", "SUM of transport component costs"),
    ("platform_fee", "cost", "per-booking platform/affiliate-network fee, if any"),
    ("payment_processing", "cost", "payment processor % + fixed fee on package price"),
    ("support_overhead", "cost", "allocated customer-support cost per traveler"),
    ("package_price", "revenue", "price charged to the traveler"),
    ("gross_margin", "derived", "package_price - total costs"),
    ("margin_pct", "derived", "gross_margin / package_price * 100"),
]


def main() -> None:
    if not PILOT_DB.exists():
        sys.exit(f"pilot.db not found at {PILOT_DB}")
    if OUT_DB.exists():
        OUT_DB.unlink()

    src = sqlite3.connect(PILOT_DB)
    src.row_factory = sqlite3.Row
    dst = sqlite3.connect(OUT_DB)
    cur = dst.cursor()

    cur.executescript("""
        CREATE TABLE packages (
            package_id          INTEGER PRIMARY KEY,
            itinerary_id        INTEGER NOT NULL,
            name                TEXT NOT NULL,
            days                INTEGER,
            selection_rationale TEXT NOT NULL,
            verification_status TEXT NOT NULL,
            package_status      TEXT NOT NULL,
            created_at          TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE package_components (
            component_id      INTEGER PRIMARY KEY,
            package_id        INTEGER NOT NULL REFERENCES packages(package_id),
            itinerary_item_id INTEGER,           -- NULL for package-level stubs (flights)
            day               INTEGER,
            component_type    TEXT NOT NULL,     -- flight|hotel|activity|dining|transport|other
            description       TEXT NOT NULL,
            proposed_supplier TEXT,              -- Duffel|Booking.com|Viator|OpenTable|NULL
            supplier_status   TEXT NOT NULL,     -- no_access|supplier_tbd|not_bookable
            estimated_cost    REAL,              -- NULL until supplier access exists
            cost_basis        TEXT NOT NULL,     -- unknown until a supplier quote exists
            notes             TEXT
        );
        CREATE TABLE package_economics (
            package_id    INTEGER NOT NULL REFERENCES packages(package_id),
            line_item     TEXT NOT NULL,
            kind          TEXT NOT NULL,         -- cost|revenue|derived
            amount        REAL,                  -- NULL until supplier terms exist
            amount_basis  TEXT NOT NULL,         -- unknown|formula
            formula       TEXT,
            revenue_terms TEXT,                  -- NULL until a commercial agreement exists
            terms_status  TEXT NOT NULL,         -- no_agreement
            notes         TEXT,
            PRIMARY KEY (package_id, line_item)
        );
    """)

    for pkg_seq, (itin_id, name, rationale) in enumerate(PACKAGES, start=1):
        itin = src.execute(
            "SELECT id, title, days FROM itineraries WHERE id = ?", (itin_id,)).fetchone()
        assert itin, f"itinerary {itin_id} missing from pilot.db"
        cur.execute(
            """INSERT INTO packages
               (package_id, itinerary_id, name, days, selection_rationale,
                verification_status, package_status)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (pkg_seq, itin_id, name, itin["days"], rationale,
             "itinerary verified against live source 2026-09-16 (evidence-only audit PASS)",
             "prototype — structure complete; all supplier costs and revenue terms unknown"))
        items = src.execute(
            "SELECT id, day, item_type, name, location, price_hint "
            "FROM itinerary_items WHERE itinerary_id = ? ORDER BY id", (itin_id,)).fetchall()

        # Package-level flight stub: round-trip air is required for every package,
        # origin unknown (traveler-dependent), no Duffel access yet.
        cur.execute(
            """INSERT INTO package_components
               (package_id, itinerary_item_id, day, component_type, description,
                proposed_supplier, supplier_status, estimated_cost, cost_basis, notes)
               VALUES (?, NULL, NULL, 'flight', ?, 'Duffel', 'no_access', NULL,
                       'unknown — no supplier access',
                       'Round-trip air, origin TBD (traveler-dependent). Needs Duffel access.')""",
            (pkg_seq, f"Round-trip flights for: {itin['title']}"))

        for it in items:
            itype = it["item_type"]
            supplier = SUPPLIER_FOR[itype]
            if itype in ("flight", "hotel", "activity", "restaurant"):
                status, basis = "no_access", "unknown — no supplier access"
            elif itype == "transport":
                status, basis = "supplier_tbd", "unknown — no supplier identified"
            else:
                status, basis = "not_bookable", "n/a — not a bookable component"
            desc = it["name"] + (f" ({it['location']})" if it["location"] else "")
            notes = None
            if it["price_hint"]:
                notes = (f"Source price hint (unverified, do not use as supplier cost): "
                         f"{it['price_hint']}")
            cur.execute(
                """INSERT INTO package_components
                   (package_id, itinerary_item_id, day, component_type, description,
                    proposed_supplier, supplier_status, estimated_cost, cost_basis, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, ?)""",
                (pkg_seq, it["id"], it["day"], itype, desc, supplier, status, basis, notes))

        for line, kind, formula in ECONOMIC_LINES:
            cur.execute(
                """INSERT INTO package_economics
                   (package_id, line_item, kind, amount, amount_basis, formula,
                    revenue_terms, terms_status, notes)
                   VALUES (?, ?, ?, NULL, ?, ?, NULL, 'no_agreement',
                           'Fills in when supplier access + commercial terms exist (Step 5).')""",
                (pkg_seq, line, kind,
                 "formula" if kind == "derived" else "unknown", formula))

    dst.commit()

    n_pkg = cur.execute("SELECT COUNT(*) FROM packages").fetchone()[0]
    n_comp = cur.execute("SELECT COUNT(*) FROM package_components").fetchone()[0]
    n_unk = cur.execute(
        "SELECT COUNT(*) FROM package_components WHERE estimated_cost IS NULL").fetchone()[0]
    n_econ = cur.execute("SELECT COUNT(*) FROM package_economics").fetchone()[0]
    by_type = cur.execute(
        "SELECT component_type, COUNT(*) FROM package_components GROUP BY 1 ORDER BY 1").fetchall()
    print(f"COMMERCIAL LAYER OK: packages={n_pkg} components={n_comp} "
          f"(unknown_cost={n_unk}) economics_rows={n_econ}")
    print("components by type:", dict(by_type))
    print(f"wrote {OUT_DB}")
    src.close()
    dst.close()


if __name__ == "__main__":
    main()
