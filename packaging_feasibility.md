# Packaging Feasibility: Influencer Itineraries → Sellable Travel Packages

Research date: 2026-09-15. All factual claims carry source URLs. Where exact commercial terms sit behind a partner portal, that is stated explicitly rather than guessed.

---

## 1. VIATOR (activities & tours)

**Program:** Viator Partner Program — free affiliate signup, no minimum traffic or follower requirement (https://phptravels.com/blog/how-to-earn-with-the-viator-affiliate-program).

**Commission:** 8% on eligible completed bookings, with a 30-day attribution window (https://phptravels.com/blog/what-is-viator-api-how-it-works; https://partnerresources.viator.com/travel-content/links/). One aggregator listing also cites 8–10% depending on volume/campaigns (https://staging.themdc.org/scholarship/MxEpC4/4AD150/ViatorPartnerProgram.pdf) — confirm the exact rate in the partner dashboard, as advanced API terms can differ from the standard affiliate rate.

**Tools:** in-text affiliate links to any product/category/destination page, widgets, banners, and an Affiliate API (https://partnerresources.viator.com/travel-content/links/). The Affiliate API has no signup cost and no subscription fee; the commercial model is commission on bookings (https://phptravels.com/blog/what-is-viator-api-how-it-works). Viator is the merchant of record and handles payments + customer service (https://partnerresources.viator.com/travel-content/links/). Inventory: 300,000+ experiences across 2,500 destinations (https://phptravels.com/blog/how-to-earn-with-the-viator-affiliate-program).

**How to get access:** register at the Viator Partner Program (partnerresources.viator.com), enter account + website/content details, get dashboard access, generate links/widgets/API credentials (https://phptravels.com/blog/how-to-earn-with-the-viator-affiliate-program). Viator also runs a separate Travel Agent Program (TAP) for booking on clients' behalf (https://www.travelpulse.ca/news/technology/viator-by-tripadvisor-lets-agents-book-direct).

**Blockers:** none structural. This is the easiest component to wire in — affiliate links work day one; the API needs a partner account but no fee.

---

## 2. OPENTABLE (restaurant tables)

**Partner API:** OpenTable exposes a restricted Partner API (restaurant content, availability, reservations, CRM) through the OpenTable Partner Portal — access is granted to approved partners under contractual agreement (https://github.com/api-evangelist/opentable; portal: https://dev.opentable.com/partner-portal).

**How to get access:** apply via the dev portal ("Become a partner" → application form): applicant info, company name/operating website/address, primary country + years in business, product details (live or not, type, industry), and monthly user counts (https://elfsight.com/blog/how-to-get-and-use-opentable-api/). After submission the application is reviewed for 3–4 weeks; approval comes by email (https://elfsight.com/blog/how-to-get-and-use-opentable-api/). There is also an affiliate/widget track (reservation embeds and restaurant search widgets) for approved partners (https://github.com/api-evangelist/opentable).

**Revenue mechanics for us:** there is no public per-reservation commission paid to referring partners documented in the sources found. OpenTable's own business charges restaurants per seated diner; the referral side is a partnership/widget play, not an affiliate commission line. For the package business, dining is therefore a *completeness feature* (the itinerary includes bookable tables), not a revenue component — unless a rev-share is negotiated in the partner agreement.

**What the booking skill can/can't do:** the `/opt/hatch/skills/booking` routing table lists Restaurant → `native` → `opentable` by default — create, change, cancel reservations (booking/SKILL.md, "Routing" table). That is an agent acting on the user's behalf for the user's own dinner plans, using whatever OpenTable connectivity the runtime has. It does NOT give the package business a public API to programmatically create reservations for arbitrary customers — that requires the business's own OpenTable Partner API approval above.

**Blockers:** partner-gated, 3–4 week review, contractual; self-serve integration is marketing, live access needs affiliate approval (https://github.com/prasanth-kalas/lumo_restaurant_agent_web). Day-one fallback: deep-link to restaurant reservation pages (no tracking revenue) or approved widgets once partner status lands.

---

## 3. DUFFEL (flights)

Per `/opt/hatch/skills/duffel/SKILL.md`:

**Capabilities:** search (one-way, round-trip, multi-city via `--leg`), seat options, `validate-booking`, `book`, `booking-status`, `cancellation-quote`, `cancel-booking`. CLI-driven; offers are live airline inventory (NDC + GDS-style). Results limited to Duffel inventory; no cars ("Duffel cars are not available"); hotel stays exist via a separate stays product ("duffel stays — prepaid rates only; coverage outside the US is unproven" per booking/SKILL.md).

**What booking requires:** (1) search the full itinerary + passenger mix together; (2) traveler picks one offer; (3) collect passenger details — legal name, birth date, title (mr/ms/mrs/miss/dr), gender, trip email/phone, passport details when validation requires; (4) `validate-booking` until `ready_to_book: true`; (5) Stripe Link payment method (`pm_…`); (6) exactly one human-in-the-loop approval for `book`, covering itinerary, passengers, seats, fare conditions, total, and the one-time virtual card/3DS. First booking may require the account owner's email + legal name for a Duffel payment profile. Cancellation quotes must be shown before any irreversible cancel.

**Costs/fees:** Duffel charges the seller ~$3 per confirmed order + 1% of total purchase price, $2 per paid ancillary, and $0.005 per search once the search-to-book ratio exceeds 1,500:1 (https://altexsoft.medium.com/the-unseen-price-of-travel-distribution-costs-and-hidden-payments-10cf044a7232). Airlines pay ~zero commission on air — a seller's flight margin is markup + service fee + ancillaries (https://altexsoft.medium.com/the-unseen-price-of-travel-distribution-costs-and-hidden-payments-10cf044a7232; https://github.com/catalin99/travel-planner-root/blob/HEAD/.github/skills/pricing-strategy/SKILL.md).

**Payments:** Duffel Payments (built with Stripe) lets travel businesses charge customers directly with no upfront capital or bond, add fare markups, and bundle accommodation/travel insurance; it handles refunds behind the scenes (https://uktechnews.co.uk/2022/02/10/duffel-and-stripe-partner-to-make-flight-sales-easier-for-travel-businesses/; https://www.traveldailynews.com/regional-news/duffel-and-stripe-enable-seamless-flight-payments-processing-through-a-powerful-api/).

**Blockers:** no structural blocker to selling flights with markup — Duffel is built for exactly this. Margin is thin (markup-dependent); real "gain share" on air needs private/consolidator fares (see §6).

---

## 4. HOTELS — Booking.com vs Expedia TAAP vs Hotelbeds

### Booking.com Affiliate Program
- **Access:** apply through Booking.com's Partner Hub; approval is gated and usually takes a few days (https://www.adivaha.com/booking-com-affiliate-plugin-wordpress.html). Also distributed via CJ Affiliate in North America (https://www.cj.com/en-gb/publisher/partners/booking.com/sign-up).
- **Commission:** CJ standard terms: 4% commission per materialised (completed-stay) transaction, session-based attribution (no cookie tracking), paid within 60 days after guest checkout (https://www.cj.com/en-gb/publisher/partners/booking.com/sign-up). Tiered structure: commissions are a share (25–40%) of Booking.com's own commission depending on volume tiers — e.g. 25% of Booking.com's ~15% cut ≈ 3.75% of booking value at Tier 1, up to ~40% share for 501+ stays (https://mize.tech/blog/all-about-the-booking-com-affiliate-partner-program-for-travel-agents/; https://www.adivaha.com/booking-com-affiliate-plugin-wordpress.html). Cancelled/no-show bookings earn nothing.
- **Integration:** deep links, banners, search widgets, and API access for qualified partners (https://www.adivaha.com/booking-com-affiliate-plugin-wordpress.html).

### Expedia TAAP (Travel Agent Affiliate Program)
- **Access:** register interest at https://partner.expediagroup.com/en-us/landing-pages/join-taap → create account → Expedia approves → start earning (https://partner.expediagroup.com/en-us/landing-pages/join-taap). 100,000+ agents use it annually; 160,000+ advisors globally (https://partner.expediagroup.com/en-us/landing-pages/join-taap; https://www.travelweek.ca/news/technology-related-travel-news/expedia-taap-launches-lets-get-ready-to-bundle-promotion-for-travel-advisors/).
- **Commission:** paid as a percentage of gross booking value (GBV) of each consumed booking, tier-dependent per the Incentive Plan Page (exact % behind the portal); paid monthly in arrears (https://taap-terms-service-us-west-2-epsdecaf-prod.s3.amazonaws.com/FI/2025-04-01/EN-20250401.pdf). Notably, TAAP pays commission on the *total package price including flights* when bundling (https://www.travelweek.ca/news/technology-related-travel-news/expedia-taap-launches-lets-get-ready-to-bundle-promotion-for-travel-advisors/) — directly relevant to the bundle model.
- **Inventory:** 3M+ properties, 500 airlines, 170,000 tours/attractions via TAAP (https://www.travelweek.ca/news/technology-related-travel-news/expedia-taap-launches-lets-get-ready-to-bundle-promotion-for-travel-advisors/).
- **Rapid API (the developer path):** Expedia's Rapid API gives 700,000+ accommodations with Expedia as merchant of record, but is designed for corporate/mid-to-large partners — requires a corporate entity and business track record (https://dev.to/kouta222/complete-guide-for-individual-developers-recommended-hotel-affiliate-apis-by-region-4c1e).

### Hotelbeds (bed bank)
- **Model:** B2B bed bank — negotiates discounted net hotel rates and sells to travel retailers, who mark up; commission-based model has largely replaced markup (https://altexsoft.medium.com/the-unseen-price-of-travel-distribution-costs-and-hidden-payments-10cf044a7232). Described as "the leading online distributor of transfers, tours, and activities in the travel trade" (https://support.trekksoft.com/connect-to-hotelbeds).
- **Access:** B2B application → assigned account manager (typically within 48h in channel-manager flows) → API certification: implementation checklist verified by internal team, then request/response logs + screenshots submitted to the account manager (https://support.trekksoft.com/connect-to-hotelbeds; http://assets.ctfassets.net/sdx4pteldsvw/5JAVh7PrHOYvf6oxfuGTUC/9c168d85fe326be585032a00954c4f39/Hotel-API-Checklist.pdf).
- **Economics:** margin is the spread between net rate and sell price (typically double-digit % on hotels vs ~4% affiliate) — exact contracted rates are negotiated per account, not published.

**Verdict for the bundle:** Booking.com affiliate is the fastest day-one hotel line (4% on completed stays). Expedia TAAP is the better structural fit for a *bundle* business (commission on total package price incl. flights). Hotelbeds/net-rate model is the margin lever for a merchant-model package (keep the spread), but requires a real travel business + API certification.

---

## 5. CREDIT-CARD CO-BRAND ECONOMICS (the money layer)

### 5.1 How airline co-brand deals actually work — verifying the ~3.5%

The thesis is directionally right but the mechanism needs correcting: **issuers do not pay airlines a % of top-line. Issuers buy miles from airlines at a wholesale per-mile price, plus marketing royalties.** The airline's revenue therefore *scales with* card spend, which is where the ~3.5% intuition comes from.

- **Wholesale mile price:** each mile fetches an airline roughly **1.5–2.5 cents** from the bank (https://news.slashdot.org/story/17/04/10/1326248/airlines-make-more-money-selling-miles-than-seats). United states its internal rate is "roughly two cents apiece" (https://thepointsguy.com/news/economics-of-loyalty-programs/).
- **Accounting split (American Airlines 2024 10-K):** every mile sale has two components — *transportation* (estimated future award value, deferred and recognized on redemption) and *marketing* (brand use, member-list access, advertising — recognized at sale via a sales-based royalty). The marketing component is "the predominant element in these agreements" (https://www.annualreports.com/HostedData/AnnualReports/PDF/NASDAQ_AAL_2024.pdf).
- **Scale (this is the real number):** American Airlines earned **$6.1B cash remuneration from co-brand cards and partners in 2024** (+17% YoY); Citi becomes the exclusive AAdvantage issuer in 2026 under a 10-year deal; American guides ~10% annual growth toward **~$10B/year by end of decade** (https://americanairlines.gcs-web.com/static-files/aa971970-8330-4eb3-b7fb-97c6cd6060e9; https://www.ajot.com/news/american-airlines-reports-fourth-quarter-and-full-year-2024-financial-results). Delta–Amex generated **~$8B in 2025 (~10% of Delta's revenue; ~$2B in Q1 alone)**, targeting $10B long-term (https://markets.financialcontent.com/buffnews/article/finterra-2026-1-14-delta-air-lines-dal-deep-dive-navigating-the-centennial-era-and-the-premium-pivot; https://www.pulse.bot/hotels/video/delta-just-revealed-its-real-business-model-112ab679-9411-4b65-a3dc-468ec1a881e3/).
- **Checking the 3.5%:** a $10K package charged to a 1×-earn co-brand card issues 10,000 miles → issuer pays the airline ~$200 (10,000 × 2¢) = **2% of top-line**. Airline purchases typically earn 2–4× miles → 20,000–40,000 miles → **$400–$800 = 4–8% of top-line**. So ~3.5% is a fair blended estimate of what the *airline* captures per co-brand dollar — it is **not** a share we receive.

### 5.2 The critical inversion: as the merchant, cards are our COST

If we sell the package, **we pay interchange of ~2–2.5% per transaction** — swipe fees "typically between 2% and 2.5% per transaction" (https://paymentsindustryintelligence.com/visa-and-mastercard-agree-revised-settlement-on-us-interchange-fees/), totalling $111.2B in the US in 2024 (National Retail Federation, via same source). The co-brand money flows **issuer → airline** and **merchant → issuer** — as the merchant we are on the paying side of both flows. This is the single most important correction to the model.

### 5.3 Realistic on-ramps for a package seller to participate in card economics

1. **Payment-mix steering (immediate, no BD):** discount for debit/bank-transfer/ACH at checkout to avoid ~2.5% interchange; or surcharge credit (permitted up to 3% with disclosure under the new Visa/Mastercard settlement terms) (https://www.retail-systems.com/rs/Visa_Mastercard_Agree_Revised_Settlement_Interchange_Fees.php).
2. **Co-brand card acquisition affiliate:** issuers pay per approved card application through affiliate networks. (Exact bounty not verified from a citable source in this pass — flagged for BD verification; do not model a number until confirmed.)
3. **Private/consolidator air fares (the real "gain share" on-ramp):** airlines give consolidators discounted net fares (mainly international); agencies mark up, with commissions on consolidator tickets reaching 20–25% (https://www.thefreelibrary.com/Chapter-4+Fares+and+pricing-a0184134075; https://en.wikipedia.org/wiki/Airline_consolidator). Requires travel-agency accreditation/volume — a BD + compliance project, not an API key.
4. **Own co-brand card:** requires a bank partner and massive scale — not a startup on-ramp.

### 5.4 Unit-economics teardown: $10K 7-day Kyoto package (2 travelers, illustrative)

Assumptions (stated, not sourced — model only): flights $3,000 · hotel $3,500 (7×$500) · activities $1,000 · dining $1,500 (no commission). Commission rates are the sourced figures from §§1–4.

| Layer | Revenue to us | Source/assumption |
|---|---|---|
| Flight markup via Duffel (3% markup) | +$90 | markup assumption; Duffel costs us ~$3 + 1% ≈ $33 (https://altexsoft.medium.com/the-unseen-price-of-travel-distribution-costs-and-hidden-payments-10cf044a7232) → net **+$57** |
| Hotel — Booking.com affiliate @4% of $3,500 | +$140 | (https://www.cj.com/en-gb/publisher/partners/booking.com/sign-up) |
| Activities — Viator @8% of $1,000 | +$80 | (https://phptravels.com/blog/what-is-viator-api-how-it-works) |
| Dining — OpenTable | $0 | no partner commission documented (§2) |
| **Gross affiliate/markup take** | **~$277 (2.8%)** | |
| Card interchange on $10K (~2.2%) | −$220 | (https://paymentsindustryintelligence.com/visa-and-mastercard-agree-revised-settlement-on-us-interchange-fees/) |
| **Net (affiliate-only model)** | **~$57 (0.6%)** | |

Meanwhile the co-brand layer on the same $10K (1× earn, ~2¢/mile): issuer pays airline ~$200 (2%); we see $0 of it (§5.1).

**Where the money actually pools — levers that fix the model:**
- **Merchant-model hotel (net rates via Hotelbeds-style bed bank):** 15%+ spread on $3,500 = **$525+** vs $140 affiliate — ~4× the hotel line (https://altexsoft.medium.com/the-unseen-price-of-travel-distribution-costs-and-hidden-payments-10cf044a7232).
- **Consolidator/private air:** 10–20%+ effective margin on $3,000 = **$300–$600** vs $57 Duffel markup (https://www.thefreelibrary.com/Chapter-4+Fares+and+pricing-a0184134075).
- **Payment steering:** moving the $10K off credit saves up to **$220**.
- **Service fee:** flat $99–$199 package fee, standard agency practice.
- Realistic merchant-model package take: **$1,100–$1,600 per $10K package (11–16%)** vs **$57 (0.6%)** affiliate-only. The affiliate path is a lead-gen funnel; the merchant path is the business.

---

## 6. VERDICT — what wires together today vs needs business development

**Wire today (no BD):**
- Viator: affiliate links immediately; Affiliate API with free partner signup (8%, 30-day window).
- Booking.com affiliate: apply via Partner Hub, 4% on completed stays, session-based.
- Duffel: flight search + booking with markup via Stripe/Link; one HITL approval per booking. (~$3 + 1% per order cost.)
- OpenTable: deep-links to reservation pages only.

**Needs business development / accreditation:**
- OpenTable Partner API (3–4 week approval, contractual) for programmatic reservations.
- Expedia Rapid API (corporate entity + track record) or TAAP agency account for package-commission economics.
- Hotelbeds/bed-bank net rates (B2B account + API certification) — the hotel margin lever.
- Airline private/consolidator fares or agency accreditation (IATA/ARC, bonds, volume) — the air gain-share lever.
- Any card-economics participation beyond payment steering (issuer acquisition deals, card-linked offers).
- Seller-of-travel compliance: wholesalers selling packages through retail channels generally need no special federal permission in the US, but state Seller of Travel registrations apply where the agency is registered (https://www.travelweekly.com/Content/GenericPage.aspx?ptgpk=53168864&requrl=/Mark-Pestronk/Launching-wholesale-division-raises-questions-terms); public charter rules apply only if chartering aircraft.

**Bottom line:** an affiliate-assembled package is buildable this week and earns ~2.8% gross / ~0.6% net after interchange — a marketing funnel, not a business. The merchant model (net hotel rates + consolidator air + payment steering + service fee) takes it to 11–16% per package but requires real travel-business accreditation and partner approvals. The co-brand card billions are real — $6–8B/year per major airline — but they flow issuer→airline; our participation is via acquisition bounties and payment economics, not a cut of their 3.5%.
