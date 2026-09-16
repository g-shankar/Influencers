# Commercial Validation — Scope

Objective: answer with evidence, for a defined traveler segment, **"Can creator-recommended trips become bookable packages?"** — or kill it. This scope covers the external review's 6 recommendations. Steps 2–4 are already running in the research-strengthening pass; steps 1, 5, 6 are new work scoped below.

## Step 1 — Define the decision (needs Gowrishankar)
- Decision memo: target traveler segment, success criteria (e.g. margin % at a given conversion rate), kill criteria, budget cap for validation.
- Effort: one working session + write-up. This blocks steps 5–6 — nothing commercial is tested until the decision is defined.

## Step 2 — Justify creator selection (in progress)
- Strengthening pass is writing SELECTION_CRITERIA.md (honest reconstruction + forward criteria).
- Remaining after that: apply the forward criteria to re-qualify the 100 into a shortlist worth commercial testing.

## Step 3 — Trace each recommendation to evidence (in progress)
- Full 93/93 verification log with source, check date, and supporting passage per itinerary.

## Step 4 — Make verification consequential (in progress)
- Schedule errors corrected in the data, unsupported claims quarantined, QC report regenerated.

## Step 5 — Test commercial feasibility on 3–5 real trips
For each trip, establish:
- **Partner access** — apply for Viator, Duffel, OpenTable, Booking.com affiliate programs; record actual approval status, commission rates, and API/affiliate terms. Applications take days to weeks: start early, it's the long pole.
- **Availability** — are the trip's key hotels, activities, and restaurants actually bookable now, at what price?
- **Payment & liability** — who charges the customer, who holds the money, who handles refunds/chargebacks?
- **Creator rights** — legal review: can we sell a package derived from a creator's publicly posted itinerary? Permission needed or not?
- **Reconciled cost model** — supplier costs + fees + payment processing + support overhead vs. price the segment will pay. Per-trip P&L.
- Deliverable: per-trip P&L and a feasibility verdict per trip.
- Needs from Gowrishankar: business entity for partner applications, legal counsel on the rights question, margin target.

## Step 6 — Measure demand
Pick one, against the success criteria from Step 1:
- **Landing-page smoke test** — package page + waitlist or refundable deposit; measure conversion.
- **Concierge MVP** — manually fulfill 2–3 real bookings for the test segment; measure willingness to pay and operational friction.
- **Survey** — only if tied to a real offer, not abstract interest.
- Deliverable: conversion data vs. success criteria.
- Needs from Gowrishankar: test budget, access to the target segment/audience.

## Sequencing
- Now: steps 2–4 (running).
- Next: step 1 — his decision (segment, success/kill criteria, budget).
- Then: step 5 partner applications start immediately (long lead time); step 6 runs in parallel once step 1 is set.
- Rough timeline: **4–6 weeks to a go/no-go answer**, partner approvals being the long pole.

## Out of scope — no approval yet
No real bookings, no creator outreach, no paid test spend, no partnership signatures, no public offers. Each of those needs his explicit go-ahead when its step arrives.

## Known pipeline limitation — scaling to 1,000 (flagged 2026-09-16)
`load_db.py` is fail-closed for the pilot: it requires exactly 100 rows in `influencers.csv` and reads `staging/itineraries_batch[1-4].json`. The extraction pipeline was run as four batches of 25. Scaling to 1,000 creators requires generalizing the loader (configurable creator count, N batch files) and the extraction batching — tracked here, not yet implemented.
