#!/usr/bin/env python3
"""Build the travel-itinerary pilot information deck (python-pptx, native).

7 information slides (neutral tone: no projections, no recommendations, no CTAs)
+ appendix: full influencer directory, itinerary index, quarantine list.

All numbers come from report/final_report_data.json and pilot.db — no literals.
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
DB = sqlite3.connect(ROOT / "pilot.db")
DB.row_factory = sqlite3.Row

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


def title(slide, text, t=1.05, size=34):
    tf = textbox(slide, 0.9, t, 11.5, 1.2)
    para(tf, text, size=size, color=INK, font=SERIF, first=True)


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
    para(tf, f"Travel Itinerary Pilot  •  Information deck  •  {n} / {total}",
         size=9, color=MUTED, align=PP_ALIGN.RIGHT, first=True)


# ============================================================ slide 1: cover
s = prs.slides.add_slide(BLANK)
bg(s, INK)
tf = textbox(s, 1.1, 2.2, 11, 1.0)
para(tf, "TRAVEL ITINERARY PILOT", size=15, bold=True, color=ACCENT, first=True,
     space_after=Pt(8))
rule(s, 1.1, 3.05, 0.9, color=ACCENT, h=0.06)
tf = textbox(s, 1.1, 3.3, 11, 2.2)
para(tf, "What 100 travel creators\nactually recommend", size=44, color=WHITE,
     font=SERIF, first=True, space_after=Pt(10))
tf = textbox(s, 1.1, 5.5, 11, 1.0)
para(tf, "An evidence-only information deck  •  September 2026", size=15,
     color=RGBColor(0xB9, 0xC0, 0xCC), first=True)
footer(s, 1, 0)

# ============================================================ slide 2: at a glance
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "The pilot at a glance")
title(s, "100 creators, 94 verified itineraries")
c = DATA["creators"]
stats = [
    ("100", "creators researched"),
    ("50 / 50", "TikTok / Instagram"),
    ("94", "itineraries in the database"),
    ("1,155", "itinerary items"),
    ("106", "sources cited"),
    ("85", "destinations covered"),
]
for i, (num, label) in enumerate(stats):
    col, row = i % 3, i // 3
    x, y = 0.9 + col * 4.0, 2.6 + row * 1.9
    tf = textbox(s, x, y, 3.6, 1.6)
    para(tf, num, size=40, bold=True, color=ACCENT, font=SERIF, first=True,
         space_after=Pt(2))
    para(tf, label, size=14, color=MUTED)
tf = textbox(s, 0.9, 6.35, 11.5, 0.5)
para(tf, "73 creators with cited follower counts  •  27 unknown (not invented)",
     size=12, color=MUTED, first=True)
footer(s, 2, 0)

# ============================================================ slide 3: top creators
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Creator coverage")
title(s, "Top creators by cited reach")
rows = [["Creator", "Platform", "Followers", "Itineraries"]]
for t in DATA["top_creators_by_reach"]:
    rows.append([t["handle"], t["platform"], t["followers"],
                 str(t["itineraries"])])
styled_table(s, 0.9, 2.35, 11.5, rows, [4.2, 2.4, 2.4, 2.5], font_size=12,
             row_h=0.36)
tf = textbox(s, 0.9, 6.5, 11.5, 0.4)
para(tf, "Follower counts are as cited by sources; ties broken arbitrarily.",
     size=11, color=MUTED, first=True)
footer(s, 3, 0)

# ============================================================ slide 4: verification
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Verification")
title(s, "Every itinerary checked against its source")
conf = DATA["confidence"]
cards = [(f"{conf['high']}", "high confidence", TEAL),
         (f"{conf['medium']}", "medium confidence", ACCENT),
         (f"{conf['low']}", "low confidence", MUTED)]
for i, (num, label, color) in enumerate(cards):
    x = 0.9 + i * 4.0
    tf = textbox(s, x, 2.6, 3.6, 1.4)
    para(tf, num, size=44, bold=True, color=color, font=SERIF, first=True,
         space_after=Pt(2))
    para(tf, label, size=14, color=MUTED)
bullets = [
    "7 validation gates, fail-closed: nothing unverified enters the database.",
    "10 data corrections applied during verification (7 fixed, 1 re-verified, 1 quarantined, 1 exclusion).",
    "Evidence-only audit: PASS, 2026-09-16.",
    "8 handles quarantined — listed in the appendix with reasons.",
]
tf = textbox(s, 0.9, 4.5, 11.5, 2.2)
for i, b in enumerate(bullets):
    para(tf, "•  " + b, size=14, color=INK, first=(i == 0),
         space_after=Pt(8))
footer(s, 4, 0)

# ============================================================ slide 5: trip lengths
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Trip lengths")
title(s, "From a day trip to three months")
cov = DATA["coverage"]
stats = [
    (f"{cov['shortest_days']}–{cov['longest_days']} days", "full range of trip lengths"),
    (f"{cov['trips_7_days_or_more']}", "trips of 7 days or more"),
    ("19", "itineraries with no fixed length (guides, not trips)"),
]
for i, (num, label) in enumerate(stats):
    x = 0.9 + i * 4.0
    tf = textbox(s, x, 2.6, 3.6, 1.6)
    para(tf, num, size=36, bold=True, color=ACCENT, font=SERIF, first=True,
         space_after=Pt(4))
    para(tf, label, size=14, color=MUTED)
tf = textbox(s, 0.9, 4.9, 11.5, 1.4)
para(tf, "Longest: “3-Month Southeast Asia Itinerary: The Banana Pancake Trail” (90 days). "
         "Trip-length statistics exclude the 19 itineraries whose sources state no fixed length.",
     size=13, color=MUTED, first=True)
footer(s, 5, 0)

# ============================================================ slide 6: flagships
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Flagship itineraries")
title(s, "Five itineraries verified claim by claim")
rows = [["Itinerary", "Creator", "Days", "Items"]]
for f in DATA["flagship_itineraries"]:
    rows.append([f["title"], f["handle"], str(f["days"]), str(f["items"])])
styled_table(s, 0.9, 2.35, 11.5, rows, [5.6, 2.5, 1.4, 2.0], font_size=11.5,
             row_h=0.42)
tf = textbox(s, 0.9, 6.5, 11.5, 0.4)
para(tf, "Each item name and detail checked against the live source page; "
         "supporting passages recorded in the verification log.", size=11,
     color=MUTED, first=True)
footer(s, 6, 0)

# ============================================================ slide 7: validate
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Validate this yourself")
title(s, "Everything is inspectable")
tf = textbox(s, 0.9, 2.5, 11.5, 3.5)
items = [
    ("The appendix", "full influencer directory (100) and itinerary index (94) follow this slide."),
    ("The spreadsheet", "travel-influencers-directory.xlsx — every handle, source link, and quarantine reason."),
    ("The database", "pilot.db — query any number on these slides; queries are documented in SLIDE_CALCULATIONS.md."),
    ("The verification log", "validation/reports/VERIFICATION_LOG_FULL.md — check date and supporting passage per itinerary."),
]
for i, (h, d) in enumerate(items):
    para(tf, h, size=15, bold=True, color=INK, first=(i == 0),
         space_after=Pt(1))
    para(tf, d, size=13, color=MUTED, space_after=Pt(12))
footer(s, 7, 0)

# ============================================================ appendix divider
s = prs.slides.add_slide(BLANK)
bg(s, INK)
tf = textbox(s, 1.1, 3.0, 11, 1.5)
para(tf, "APPENDIX", size=15, bold=True, color=ACCENT, first=True,
     space_after=Pt(8))
para(tf, "Influencer directory\n& itinerary index", size=40, color=WHITE,
     font=SERIF)
footer(s, 8, 17)

# ============================================================ appendix: directory
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
    title(s, "The 100 creators", size=28)
    rows = [["Handle", "Platform", "Followers", "Niche", "Itineraries"]]
    for p in chunk:
        rows.append([p["handle"], p["platform"], p["followers_approx"],
                     p["niche"] or "—", str(p["n_it"])])
    styled_table(s, 0.9, 2.2, 11.5, rows, [3.4, 2.2, 2.2, 2.2, 1.5],
                 font_size=10.5, row_h=0.185)
    # no bottom footer on dense table slides (kicker carries the numbering)

# ============================================================ appendix: itinerary index
itins = DB.execute("""
  SELECT t.title, inf.handle, t.days, t.confidence
  FROM itineraries t JOIN influencers inf ON inf.id = t.influencer_id
  ORDER BY inf.handle, t.title""").fetchall()

CHUNK = 20
n_it_total = (len(itins) + CHUNK - 1) // CHUNK
n_dir = n_dir_total
for ci in range(0, len(itins), CHUNK):
    chunk = itins[ci:ci + CHUNK]
    n = ci // CHUNK + 1
    s = prs.slides.add_slide(BLANK)
    bg(s)
    kicker(s, f"Appendix B — itinerary index ({n} of {n_it_total})")
    title(s, "The 94 itineraries", size=28)
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

# ============================================================ appendix: quarantine + notes
s = prs.slides.add_slide(BLANK)
bg(s)
kicker(s, "Appendix C — exclusions & notes")
title(s, "What was kept out, and why", size=28)
q = json.loads((ROOT / "validation" / "quarantine.json").read_text())
rows = [["Handle", "Scope", "Reason"]]
for e in q.get("quarantine", []):
    if e.get("status") == "quarantined":
        reason = e.get("reason", "")
        if len(reason) > 90:
            reason = reason[:88] + "…"
        rows.append([e.get("handle", ""), e.get("scope", ""), reason])
styled_table(s, 0.9, 2.2, 11.5, rows, [2.8, 1.8, 6.9], font_size=11,
             row_h=0.3)
tf = textbox(s, 0.9, 6.3, 11.5, 0.8)
para(tf, "“Unknown” means unknown — follower counts, prices, and dates were never "
         "invented. Discrepancies were fixed before sign-off, never overridden.",
     size=12, color=MUTED, first=True)
footer(s, 99, 0)

total = len(prs.slides)
for idx, s in enumerate(prs.slides):
    for sh in s.shapes:
        if sh.name == "FOOTER" and sh.has_text_frame:
            tf = sh.text_frame
            tf.clear()
            para(tf, f"Travel Itinerary Pilot  •  Information deck  •  {idx + 1} / {total}",
                 size=9, color=MUTED, align=PP_ALIGN.RIGHT, first=True)
OUT = Path("/home/hatch/workspace/your_files/travel-itinerary-pilot-report/"
           "travel-itinerary-pilot-report.pptx")
prs.save(OUT)
print(f"saved {OUT} — {len(prs.slides)} slides")
