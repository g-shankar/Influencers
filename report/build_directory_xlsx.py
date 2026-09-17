#!/usr/bin/env python3
"""Regenerate the influencer directory workbook from pilot.db.

Sheets: Influencers (one row per creator), Itineraries (one row per
itinerary), Quarantined (one row per quarantine record). Fully data-driven:
no hardcoded counts. Stdlib + openpyxl.
"""
import json
import sqlite3
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "pilot.db"
OUT = Path("/home/hatch/workspace/your_files/travel-itinerary-pilot-report/"
           "travel-influencers-directory.xlsx")

HDR_FONT = Font(bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor="1A2332")


def sheet_setup(ws, headers, widths):
    ws.append(headers)
    for j, h in enumerate(headers, 1):
        c = ws.cell(row=1, column=j)
        c.font = HDR_FONT
        c.fill = HDR_FILL
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row

    wb = Workbook()

    # ---- Sheet 1: Influencers ----
    ws = wb.active
    ws.title = "Influencers"
    sheet_setup(ws,
                ["Handle", "Name", "Platform", "Niche", "Followers (as cited)",
                 "Profile URL", "# Itineraries", "Itinerary titles"],
                [22, 24, 12, 14, 18, 42, 13, 80])
    rows = con.execute("""
        SELECT i.handle, i.name, i.platform, i.niche, i.followers_approx,
               i.profile_url, i.id
        FROM influencers i ORDER BY i.platform, i.handle""").fetchall()
    for r in rows:
        itins = con.execute(
            "SELECT title FROM itineraries WHERE influencer_id = ? ORDER BY title",
            (r["id"],)).fetchall()
        titles = [t["title"] for t in itins]
        ws.append([r["handle"], r["name"], r["platform"], r["niche"] or "",
                   r["followers_approx"], r["profile_url"] or "",
                   len(titles), " | ".join(titles)])

    # ---- Sheet 2: Itineraries ----
    ws2 = wb.create_sheet("Itineraries")
    sheet_setup(ws2,
                ["Handle", "Platform", "Itinerary", "Days", "Confidence", "Sources"],
                [22, 12, 55, 8, 12, 70])
    rows2 = con.execute("""
        SELECT inf.handle, inf.platform, t.title, t.days, t.confidence, t.id
        FROM itineraries t JOIN influencers inf ON inf.id = t.influencer_id
        ORDER BY inf.handle, t.title""").fetchall()
    for r in rows2:
        srcs = [s["source_url"] for s in con.execute(
            "SELECT source_url FROM itinerary_sources WHERE itinerary_id = ? ORDER BY id",
            (r["id"],))]
        ws2.append([r["handle"], r["platform"], r["title"],
                    r["days"] if r["days"] is not None else "",
                    r["confidence"], " | ".join(srcs)])

    # ---- Sheet 3: Quarantined ----
    ws3 = wb.create_sheet("Quarantined")
    sheet_setup(ws3, ["Handle", "Reason", "Scope"], [24, 90, 14])
    quar = json.loads((ROOT / "validation" / "quarantine.json").read_text())["quarantine"]
    for q in quar:
        if q.get("status") == "quarantined":
            ws3.append([q.get("handle", ""), q.get("reason", ""),
                        q.get("scope", "") or "creator"])

    wb.save(OUT)
    print(f"saved {OUT}: {ws.max_row - 1} creators, {ws2.max_row - 1} itineraries, "
          f"{ws3.max_row - 1} quarantined")


if __name__ == "__main__":
    main()
