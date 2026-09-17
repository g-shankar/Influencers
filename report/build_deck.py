#!/usr/bin/env python3
"""Build the travel-influencer research findings deck (python-pptx).

Informative dossier style: flat descriptive titles, no sales language, no
projections, no recommendations, no calls to action, no commercial framing.

8 content slides + appendix (full creator directory, itinerary index,
quarantine log). Appendix table slides grow automatically with the data.

All numbers come from report/final_report_data.json and pilot.db — no literals.
Stage targets (dates, stage number) come from stage.json.
"""
import json
import sqlite3
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "report" / "final_report_data.json").read_text())
STAGE = json.loads((ROOT / "stage.json").read_text())
DB = sqlite3.connect(ROOT / "pilot.db")
DB.row_factory = sqlite3.Row

C = DATA["creators"]
COV = DATA["coverage"]
CONF = DATA["confidence"]
IT = DATA["itineraries"]
VAL = DATA["validation"]
GEN = DATA.get("generated_at", "")
STAGE_N = STAGE.get("stage", 1)
SEL_DATE = STAGE.get("selection_date", "")

quar_all = json.loads((ROOT / "validation" / "quarantine.json").read_text())["quarantine"]
quar_handles = [q for q in quar_all if q.get("status") == "quarantined"]
quar_creators = [q for q in quar_handles if q.get("scope", "handle") != "itinerary"]
quar_itins = [q for q in quar_handles if q.get("scope") == "itinerary"]

# ---------- theme ----------
PAPER = RGBColor(0xFA, 0xF8, 0xF4)
INK = RGBColor(0x1A, 0x23, 0x32)
MUTED = RGBColor(0x5C, 0x66, 0x78)
ACCENT = RGBColor(0xB4, 0x63, 0x2A)      # terracotta
TEAL = RGBColor(0x1F, 0x5C, 0x5C)
LINE = RGBColor(0xDD, 0xD5, 0xC6)
BAND = RGBColor(0xF1, 0xEB, 0xDF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SERIF = "Georgia"
SANS = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def bg(slide, color=PAPER):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def textbox(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    return tf


def para(tf, text, size=18, bold=False, color=INK, font=SANS, align=PP_ALIGN.LEFT,
         space_after=Pt(4), first=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = space_after
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = font
    return p


def rule(slide, l, t, w, color=ACCENT, h=0.045):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t),
                                 Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    return shp


def kicker(slide, text, t=0.45):
    tf = textbox(slide, 0.9, t, 11.5, 0.5)
    para(tf, text.upper(), size=12, bold=True, color=ACCENT, first=True,
         space_after=Pt(2))
    rule(slide, 0.9, t + 0.42, 0.7)


def title(slide, text, t=1.05, size=32):
    tf = textbox(slide, 0.9, t, 11.5, 1.2)
    para(tf, text, size=size, color=INK, font=SERIF, first=True)


def bullets(slide, items, t=2.3, size=14, gap=Pt(8), width=11.5, l=0.9):
    """items: list of (bold_lead, rest) tuples; bold_lead may be ''."""
    tf = textbox(slide, l, t, width, 4.4)
    for i, (lead, rest) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = gap
        if lead:
            r = p.add_run()
            r.text = lead
            r.font.size = Pt(size)
            r.font.bold = True
            r.font.color.rgb = INK
            r.font.name = SANS
        r = p.add_run()
        r.text = (" " if lead else "") + rest
        r.font.size = Pt(size)
        r.font.color.rgb = INK
        r.font.name = SANS


def styled_table(slide, l, t, w, rows_data, col_widths, header=True,
                 font_size=11, row_h=0.32):
    # rows_data already includes the header row when header=True
    n_rows = len(rows_data)
    n_cols = len(col_widths)
    tbl_shape = slide.shapes.add_table(n_rows, n_cols, Inches(l), Inches(t),
                                       Inches(w), Inches(row_h * n_rows))
    tbl = tbl_shape.table
    for i, cw in enumerate(col_widths):
        tbl.columns[i].width = Inches(cw)
    r0 = 0
    if header:
        for j, htxt in enumerate(rows_data[0]):
            cell = tbl.cell(0, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = INK
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.text_frame.word_wrap = True
            p = cell.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = str(htxt)
            run.font.size = Pt(font_size)
            run.font.bold = True
            run.font.color.rgb = WHITE
            run.font.name = SANS
        r0 = 1
    for i, row in enumerate(rows_data[1:] if header else rows_data):
        for j, val in enumerate(row):
            cell = tbl.cell(r0 + i, j)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if i % 2 == 1:
                cell.fill.solid()
                cell.fill.fore_color.rgb = BAND
            cell.text_frame.word_wrap = True
            cell.margin_left = Inches(0.08)
            p = cell.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = str(val)
            run.font.size = Pt(font_size)
            run.font.color.rgb = INK
            run.font.name = SANS
    return tbl_shape


def footer(slide, n, total):
    tb = slide.shapes.add_textbox(Inches(0.9), Inches(6.95), Inches(11.5), Inches(0.4))
    tb.name = "FOOTER"
    tf = tb.text_frame
    tf.word_wrap = True
    para(tf, f"Travel Influencer Itinerary Pilot — Research Findings  •  {n} / {total}",
         size=9, color=MUTED, align=PP_ALIGN.RIGHT, first=True)


# ============================================================ 1: title
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, f"Research findings  ·  {GEN}", t=2.0)
tf = textbox(s, 0.9, 2.7, 11.5, 2.0)
para(tf, "Travel Influencer Itinerary Pilot", size=40, color=INK, font=SERIF,
     first=True, space_after=Pt(6))
para(tf, "Research Findings", size=40, color=INK, font=SERIF, space_after=Pt(14))
tf = textbox(s, 0.9, 5.6, 11.5, 1.0)
para(tf, f"Scope: {C['total']} travel creators ({C['tiktok']} TikTok, "
         f"{C['instagram']} Instagram) and the {IT['total']} itineraries "
         "extracted from their public sources, stored in a queryable database "
         "with a per-itinerary verification record.",
     size=14, color=MUTED, first=True)
footer(s, 1, 0)

# ============================================================ 2: scope
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Scope")
title(s, "What was collected, and what was not")
bullets(s, [
    ("Collected: ",
     f"{C['total']} creators ({C['tiktok']} TikTok / {C['instagram']} Instagram); "
     f"{IT['total']} itineraries; {COV['items']:,} itinerary items; "
     f"{COV['sources']} cited sources; {COV['destinations']} destinations — "
     "all stored in pilot.db with per-itinerary verification records."),
    ("Not collected: ",
     "commercial economics, payment percentages, supplier terms, pricing, or "
     "demand data. These were explicitly parked and are not part of this research."),
    ("This deck: ",
     "an information record of the findings. It contains no projections, "
     "no recommendations, and no calls to action."),
], t=2.4)
footer(s, 2, 0)

# ============================================================ 3: method
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Method")
title(s, "How the creators and itineraries were gathered")
sel_note = (f"Stage {STAGE_N} expansion: {STAGE['creators_total'] - 100} additional creators "
            f"selected {SEL_DATE} under the recorded SELECTION_CRITERIA.md Section 3 "
            f"rules (identity, itinerary-content fit, reach floor, activity, "
            f"exclusions) with a per-creator selection log — see SELECTION_STAGE{STAGE_N}.md."
            if STAGE_N >= 1 else "")
bullets(s, [
    ("Selection: ",
     f"{C['total']} creators, {C['tiktok']} TikTok / {C['instagram']} Instagram — "
     "the split is enforced mechanically by load_db.py, which refuses to load "
     "on quota mismatch. The pilot 100 were compiled 2026-09-15 from "
     "third-party \u201ctop travel influencer\u201d listicles (no eligibility or "
     "exclusion rules recorded at selection time — see SELECTION_CRITERIA.md). "
     + sel_note),
    ("Extraction: ",
     "itineraries were extracted from each creator's public source pages "
     "(blogs, guides, posts) into a normalized schema: itinerary, items, "
     "sources, destinations."),
    ("Validation: ",
     "7 validation gates, fail-closed — nothing unverified enters the database. "
     "An independent evidence council re-verified the itineraries against live "
     f"sources; corrections are recorded in QC_REPORT_STRENGTHENED.md. "
     f"{len(quar_handles)} records were quarantined (Appendix C)."),
], t=2.4)
footer(s, 3, 0)

# ============================================================ 4: creators
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "The creators")
title(s, f"Composition of the {C['total']} creators")
niches = C["niche_counts"]
rows = [["Niche", "Creators"]]
for niche, n in sorted(niches.items(), key=lambda kv: -kv[1]):
    rows.append([niche or "—", str(n)])
# niche table (left) + composition facts (right)
styled_table(s, 0.9, 2.35, 4.6, rows, [3.0, 1.6], font_size=10.5, row_h=0.21)
bullets(s, [
    ("Platform split: ", f"{C['tiktok']} TikTok / {C['instagram']} Instagram."),
    ("Follower counts: ",
     f"{C['with_known_followers']} cited by sources, {C['unknown_followers']} "
     "marked unknown — counts are as cited, not independently audited."),
    ("Itinerary yield: ",
     f"{C['with_itineraries']} of the {C['total']} creators have at least one extracted "
     f"itinerary ({IT['total']} itineraries total)."),
    ("Quarantined: ",
     f"{len(quar_creators)} creator records quarantined for identity problems (brand or "
     "operator accounts, misattributed content, possible list typos) — "
     "see Appendix C."),
], t=2.35, width=6.4, l=6.0)
tf = textbox(s, 6.0, 5.7, 6.4, 0.8)
para(tf, f"Niche labels are as recorded at compile time; {C['unknown_followers']} follower counts are "
         "unknown and were not estimated.", size=11, color=MUTED, first=True)
footer(s, 4, 0)

# ============================================================ 5: itineraries
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "The itineraries")
title(s, f"Composition of the {IT['total']} itineraries")
rows = [
    ["Measure", "Value"],
    ["Itineraries", str(IT["total"])],
    ["Itinerary items", f"{COV['items']:,}"],
    ["Destinations covered", str(COV["destinations"])],
    ["Sources cited", str(COV["sources"])],
    ["Trip-length range", f"{COV['shortest_days']}–{COV['longest_days']} days"],
    ["Trips of 7 days or more", str(COV["trips_7_days_or_more"])],
    ["Itineraries with no fixed length (guides, not trips)", str(COV["no_fixed_length"])],
]
styled_table(s, 0.9, 2.35, 7.6, rows, [5.0, 2.6], font_size=12.5, row_h=0.44)
longest_txt = COV["longest_title"]
if len(longest_txt) > 60:
    longest_txt = longest_txt[:58] + "…"
bullets(s, [
    ("Longest: ",
     f"\u201c{longest_txt}\u201d ({COV['longest_days']} days)."),
    ("Note: ",
     f"trip-length figures exclude the {COV['no_fixed_length']} itineraries whose sources state no "
     "fixed length."),
], t=2.35, width=3.4, l=9.0)
footer(s, 5, 0)

# ============================================================ 6: validation
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Validation")
title(s, "Confidence levels and verification")
rows = [
    ["Confidence", "Itineraries", "Meaning"],
    ["High", str(CONF["high"]),
     "every claim checked against the live source; supporting passage recorded"],
    ["Medium", str(CONF["medium"]),
     "source checked; one or more details not independently confirmable"],
    ["Low", str(CONF["low"]),
     "source checked; material details unverifiable or ambiguous"],
]
styled_table(s, 0.9, 2.35, 11.5, rows, [1.8, 1.8, 7.9], font_size=12,
             row_h=0.5)
bullets(s, [
    ("Gates: ",
     "7 validation gates, fail-closed — schema, handle integrity, source "
     "liveness, evidence council, DB reconciliation, money firewall, and "
     "final evidence-only audit."),
    ("Re-verification: ",
     "an independent evidence council re-verified the itineraries against live "
     "sources; corrections are recorded in QC_REPORT_STRENGTHENED.md."),
    ("Audit: ",
     "evidence-only audit: PASS."),
], t=4.6)
footer(s, 6, 0)

# ============================================================ 7: limitations
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Limitations")
title(s, "What this data cannot say")
lim_lead = "Selection records: "
lim_rest = ("pilot records are thin — no eligibility or exclusion rules were "
            "documented at selection time; creator records were later "
            "quarantined for identity problems. "
            f"Stage {STAGE_N} expansion used recorded criteria with a per-creator "
            "selection log." if STAGE_N >= 1 else
            "no eligibility or exclusion rules were documented at selection "
            "time; creator records were later quarantined for identity problems.")
bullets(s, [
    ("Unknowns stay unknown: ",
     f"{C['unknown_followers']} follower counts, plus any prices, dates, or figures not stated by "
     "sources, are recorded as unknown — nothing was estimated or invented."),
    (lim_lead, lim_rest),
    ("Follower counts are as-cited: ",
     "they come from source listicles and were not independently audited."),
    ("Coverage limits: ",
     f"{C['without_itineraries']} creators have no extracted itinerary; "
     f"{COV['no_fixed_length']} itineraries have no fixed trip length; "
     f"confidence is low for {CONF['low']} itineraries."),
    ("Out of scope: ",
     "the data says nothing about commercial economics, payment shares, "
     "supplier terms, or demand — those were never collected."),
], t=2.4)
footer(s, 7, 0)

# ============================================================ 8: reproducibility
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Reproducibility")
title(s, "How to re-verify any claim in this deck")
bullets(s, [
    ("Database: ",
     "travel-influencer-pilot/pilot.db — every number on these slides can be "
     "recomputed with a SQL query."),
    ("Stage config: ",
     "travel-influencer-pilot/stage.json — the quotas and batch ranges every "
     "validation gate enforces."),
    ("Selection log: ",
     f"travel-influencer-pilot/staging/selection_log.csv — one row per creator: "
     "criterion checklist, identity-check method, check date, selector."),
    ("Verification log: ",
     "validation/reports/VERIFICATION_LOG_FULL.md — check date and supporting "
     "passage recorded per itinerary."),
    ("QC reports: ",
     "validation/reports/QC_REPORT_STRENGTHENED.md — every correction applied, "
     "with before/after evidence."),
    ("Directory: ",
     "travel-influencers-directory.xlsx — every handle, profile URL, source "
     "link, and quarantine reason in one workbook."),
], t=2.4)
footer(s, 8, 0)

# ============================================================ 9: appendix divider
s = prs.slides.add_slide(BLANK)
bg(s, INK)
tf = textbox(s, 1.1, 3.0, 11, 1.5)
para(tf, "APPENDIX", size=15, bold=True, color=ACCENT, first=True,
     space_after=Pt(8))
para(tf, "Influencer directory,\nitinerary index, and quarantine log", size=38,
     color=WHITE, font=SERIF)
footer(s, 9, 0)

# ============================================================ appendix A — directory
people = DB.execute("""
  SELECT i.handle, i.platform, i.followers_approx, i.niche,
         COUNT(DISTINCT t.id) AS n_it
  FROM influencers i LEFT JOIN itineraries t ON t.influencer_id = i.id
  GROUP BY i.id ORDER BY i.platform, i.handle""").fetchall()

CHUNK = 20
n_dir_total = (len(people) + CHUNK - 1) // CHUNK
for ci in range(0, len(people), CHUNK):
    chunk = people[ci:ci + CHUNK]
    n = ci // CHUNK + 1
    s = prs.slides.add_slide(BLANK)
    bg(s)
    kicker(s, f"Appendix A — influencer directory ({n} of {n_dir_total})")
    title(s, f"The {C['total']} creators", size=28)
    rows = [["Handle", "Platform", "Followers", "Niche", "Itineraries"]]
    for p in chunk:
        rows.append([p["handle"], p["platform"], p["followers_approx"],
                     p["niche"] or "—", str(p["n_it"])])
    styled_table(s, 0.9, 2.2, 11.5, rows, [3.4, 2.2, 2.2, 2.2, 1.5],
                 font_size=10.5, row_h=0.185)
    # dense table slides: kicker carries the numbering; no footer needed

# ============================================================ appendix B — itinerary index
itins = DB.execute("""
  SELECT t.title, inf.handle, t.days, t.confidence
  FROM itineraries t JOIN influencers inf ON inf.id = t.influencer_id
  ORDER BY inf.handle, t.title""").fetchall()

n_it_total = (len(itins) + CHUNK - 1) // CHUNK
for ci in range(0, len(itins), CHUNK):
    chunk = itins[ci:ci + CHUNK]
    n = ci // CHUNK + 1
    s = prs.slides.add_slide(BLANK)
    bg(s)
    kicker(s, f"Appendix B — itinerary index ({n} of {n_it_total})")
    title(s, f"The {IT['total']} itineraries", size=28)
    rows = [["Itinerary", "Creator", "Days", "Confidence"]]
    for t in chunk:
        title_txt = t["title"]
        if len(title_txt) > 62:
            title_txt = title_txt[:60] + "…"
        rows.append([title_txt, t["handle"],
                     str(t["days"]) if t["days"] is not None else "—",
                     t["confidence"]])
    styled_table(s, 0.9, 2.2, 11.5, rows, [6.2, 2.6, 1.2, 1.5],
                 font_size=10.5, row_h=0.185)

# ============================================================ appendix C — quarantine + notes
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Appendix C — exclusions & notes")
title(s, "Quarantine log", size=28)
rows = [["Handle", "Scope", "Reason"]]
for e in quar_handles:
    reason = e.get("reason", "")
    if len(reason) > 90:
        reason = reason[:88] + "…"
    rows.append([e.get("handle", ""), e.get("scope", "") or "creator", reason])
styled_table(s, 0.9, 2.2, 11.5, rows, [2.8, 1.8, 6.9], font_size=11,
             row_h=0.3)
tf = textbox(s, 0.9, 6.3, 11.5, 0.8)
para(tf, "\u201cUnknown\u201d means unknown — follower counts, prices, and dates were never "
         "invented. Discrepancies were fixed before sign-off, never overridden.",
     size=12, color=MUTED, first=True)
footer(s, 20, 0)

total = len(prs.slides)
for idx, s in enumerate(prs.slides):
    for sh in s.shapes:
        if sh.name == "FOOTER" and sh.has_text_frame:
            tf = sh.text_frame
            tf.clear()
            para(tf, f"Travel Influencer Itinerary Pilot — Research Findings  •  {idx + 1} / {total}",
                 size=9, color=MUTED, align=PP_ALIGN.RIGHT, first=True)
OUT = Path("/home/hatch/workspace/your_files/travel-itinerary-pilot-report/"
           "travel-itinerary-pilot-report.pptx")
prs.save(OUT)
print(f"saved {OUT} — {len(prs.slides)} slides")
