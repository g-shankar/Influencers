# Commercial Prototype Layer

Built 2026-09-16. This is the reviewer's recommended "prove three complete packages"
step, taken as far as it can go **without** supplier access, commercial agreements,
or any external commitment.

## What exists

- `packages.db` — SQLite, rebuilt from scratch by `build_commercial_layer.py`
  (re-run safe). References `pilot.db` itinerary IDs; never modifies `pilot.db`.
  - `packages` — 3 prototype packages (see below).
  - `package_components` — 96 bookable-component slots mapped 1:1 from verified
    itinerary items, each with a proposed supplier (Duffel / Booking.com / Viator /
    OpenTable). **Every cost is NULL** — no supplier access exists yet.
  - `package_economics` — per-package P&L skeleton (11 line items each):
    supplier costs, platform fee, payment processing, support overhead, package
    price, gross margin, margin %. **Every amount is NULL** with the formula
    recorded; amounts fill in when supplier terms exist.
- `STEP1_DECISION_MEMO.md` — the decision Gowrishankar must make before Step 5
  (segment, success/kill criteria, budget).

## The three packages

1. **Morocco in Two Weeks** (itinerary 42, @theblondeabroad) — 15 days, 36 items.
   International classic; tests the long-haul thesis.
2. **Japan in Two Weeks** (itinerary 75, @onegirlwandering) — 14 days, 49 items.
   Activity-heavy; tests packaging density.
3. **Oregon to California Coast Road Trip** (itinerary 65, @courtandnate) —
   4 days, 8 items. Domestic, simple; tests the short-trip thesis.

Each package includes a flight stub (round-trip air, origin TBD — traveler-dependent).

## Honesty rules (same as the research layer)

- `unknown` stays unknown. Source price hints are recorded as notes marked
  "unverified, do not use as supplier cost" — never as costs.
- No supplier row claims access that doesn't exist. All `supplier_status` values
  are `no_access`, `supplier_tbd`, or `not_bookable`.
- No revenue terms exist. All `terms_status` = `no_agreement`.

## What unblocks the numbers (Step 5)

1. Gowrishankar decides Step 1 (see `STEP1_DECISION_MEMO.md`).
2. Business entity exists for partner applications.
3. Apply to Viator, Duffel, OpenTable, Booking.com affiliate programs; record
   actual approval status, commission rates, API/affiliate terms.
4. Fill `estimated_cost` + `cost_basis` per component from live supplier quotes;
   fill `revenue_terms`; the P&L then computes from the stored formulas.
5. Measure demand (Step 6) against the Step 1 success criteria → go/no-go.
