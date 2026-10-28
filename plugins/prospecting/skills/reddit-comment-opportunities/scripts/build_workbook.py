#!/usr/bin/env python3
"""
Build the Reddit comment opportunities workbook.

Usage:
    python3 build_workbook.py posts.json 2026-08-26-reddit-comment-opportunities.xlsx

Input JSON shape:

{
  "run": {
    "date": "2026-08-26",
    "company": "Acme",
    "communities_loaded": 12,
    "posts_scraped": 480,
    "apify_actor": "trudax/reddit-scraper-lite",
    "apify_run_id": "abc123",
    "sort": "new",
    "time_window": "week",
    "posts_per_community": 20,
    "filters": "posts older than 7 days, stickied posts, 50+ comment threads",
    "disclosure": "disclosed",
    "notes": ""
  },
  "communities": [
    {
      "subreddit": "r/smallbusiness",
      "posts_scraped": 20,
      "posts_qualifying": 7,
      "themes": "what the community has been discussing, 2 to 4 lines",
      "recurring_questions": "the questions that came up more than once",
      "voice": "how the room writes: length, bullets or prose, opening move, register, insider words",
      "culture_note": "tone, vendor tolerance, what gets downvoted",
      "opportunity": "where this business fits the conversation, or that it does not",
      "note": ""
    }
  ],
  "posts": [
    {
      "subreddit": "r/smallbusiness",
      "rank_in_community": 1,
      "score": 21,
      "title": "...",
      "url": "https://www.reddit.com/r/...",
      "posted": "2026-08-25",
      "author": "u/someone",
      "upvotes": 31,
      "comments": 4,
      "why_selected": "three sentences",
      "guideline": "the brief: angle, the anchor fact, what to avoid, timing",
      "draft_comment": "the full comment text with \n line breaks",
      "keywords_used": "ai phone agent, missed calls, out of hours",
      "geo_angle": "UK, GDPR call recording",
      "risk_flags": "none",
      "mention_mode": "neutral",
      "commercial_angle": "mention | lead | visibility | none",
      "business_case": "one line on how this post turns into revenue, traffic or a named prospect",
      "dm_draft": "only when commercial_angle is lead: the message to send the poster"
    }
  ]
}

commercial_angle drives the Leads sheet: every post marked "lead" appears there
with its dm_draft. A post marked "none" should not have been selected at all.

Posts are grouped by community and sorted by rank_in_community.
A community with zero qualifying posts still appears on the Summary sheet.
"""

import json
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill("solid", fgColor="1F2937")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
BAND_FILL = PatternFill("solid", fgColor="F3F4F6")
HOT_FILL = PatternFill("solid", fgColor="DCFCE7")
WARM_FILL = PatternFill("solid", fgColor="FEF9C3")
COLD_FILL = PatternFill("solid", fgColor="FEE2E2")
THIN = Side(style="thin", color="D1D5DB")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")

POST_COLUMNS = [
    ("Subreddit", "subreddit", 18),
    ("#", "rank_in_community", 5),
    ("Score", "score", 7),
    ("Post title", "title", 42),
    ("URL", "url", 30),
    ("Posted", "posted", 12),
    ("Author", "author", 16),
    ("Up", "upvotes", 7),
    ("Cmts", "comments", 7),
    ("Why this post was selected", "why_selected", 50),
    ("Comment brief (write it yourself)", "guideline", 46),
    ("Draft comment (edit and post)", "draft_comment", 78),
    ("Keywords used", "keywords_used", 26),
    ("GEO angle", "geo_angle", 24),
    ("Rules risk", "risk_flags", 24),
    ("Mention mode", "mention_mode", 16),
    ("Commercial angle", "commercial_angle", 16),
    ("Business case", "business_case", 44),
]

ANGLE_FILL = {
    "mention": PatternFill("solid", fgColor="DBEAFE"),
    "lead": PatternFill("solid", fgColor="DCFCE7"),
    "visibility": PatternFill("solid", fgColor="FEF9C3"),
    "none": PatternFill("solid", fgColor="FEE2E2"),
}


def style_header(ws, ncols):
    for col in range(1, ncols + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BORDER
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = "A2"


def score_fill(score):
    try:
        score = float(score)
    except (TypeError, ValueError):
        return None
    if score >= 24:
        return HOT_FILL
    if score >= 18:
        return WARM_FILL
    if score >= 15:
        return COLD_FILL
    return None


def build_top_posts(wb, posts):
    ws = wb.create_sheet("Top Posts")
    for idx, (label, _, width) in enumerate(POST_COLUMNS, start=1):
        ws.cell(row=1, column=idx, value=label)
        ws.column_dimensions[get_column_letter(idx)].width = width
    style_header(ws, len(POST_COLUMNS))

    ordered = sorted(
        posts,
        key=lambda p: (str(p.get("subreddit", "")), int(p.get("rank_in_community", 99))),
    )

    row = 2
    band = False
    last_sub = None
    for post in ordered:
        sub = post.get("subreddit", "")
        if sub != last_sub:
            band = not band
            last_sub = sub
        for idx, (_, key, _) in enumerate(POST_COLUMNS, start=1):
            value = post.get(key, "")
            cell = ws.cell(row=row, column=idx, value=value)
            cell.border = BORDER
            cell.alignment = WRAP if isinstance(value, str) and len(value) > 40 else TOP
            if band:
                cell.fill = BAND_FILL
            if key == "url" and value:
                cell.hyperlink = value
                cell.font = Font(color="1D4ED8", underline="single", size=10)
            if key == "score":
                fill = score_fill(value)
                if fill:
                    cell.fill = fill
                cell.font = Font(bold=True, size=11)
            if key == "commercial_angle" and value:
                fill = ANGLE_FILL.get(str(value).strip().lower().split()[0])
                if fill:
                    cell.fill = fill
                cell.font = Font(bold=True, size=10)
        est = len(str(post.get("draft_comment", ""))) / 78 * 14
        ws.row_dimensions[row].height = max(70, min(320, est))
        row += 1

    if row == 2:
        ws.cell(row=2, column=1, value="No qualifying posts this week.").font = Font(italic=True)
    return ws


def build_summary(wb, communities):
    ws = wb.create_sheet("Summary")
    cols = [
        ("Subreddit", "subreddit", 24),
        ("Posts scraped", "posts_scraped", 15),
        ("Posts qualifying", "posts_qualifying", 17),
        ("Best score", "best_score", 12),
        ("Top pick", "top_pick_title", 46),
        ("Top pick URL", "top_pick_url", 34),
        ("Rules risk", "rules_risk", 30),
        ("Note", "note", 40),
    ]
    for idx, (label, _, width) in enumerate(cols, start=1):
        ws.cell(row=1, column=idx, value=label)
        ws.column_dimensions[get_column_letter(idx)].width = width
    style_header(ws, len(cols))

    for r, com in enumerate(communities, start=2):
        for idx, (_, key, _) in enumerate(cols, start=1):
            value = com.get(key, "")
            cell = ws.cell(row=r, column=idx, value=value)
            cell.border = BORDER
            cell.alignment = WRAP
            if key == "top_pick_url" and value:
                cell.hyperlink = value
                cell.font = Font(color="1D4ED8", underline="single", size=10)
            if key == "posts_qualifying" and value in (0, "0"):
                cell.fill = COLD_FILL
        ws.row_dimensions[r].height = 32
    return ws


def build_leads(wb, posts):
    """One row per post whose commercial angle is a named prospect worth a DM."""
    ws = wb.create_sheet("Leads")
    cols = [
        ("Subreddit", "subreddit", 18),
        ("Poster", "author", 18),
        ("What they posted", "title", 46),
        ("Post URL", "url", 32),
        ("Why they are a prospect", "business_case", 46),
        ("DM draft", "dm_draft", 78),
        ("Comment first?", "guideline", 40),
    ]
    for idx, (label, _, width) in enumerate(cols, start=1):
        ws.cell(row=1, column=idx, value=label)
        ws.column_dimensions[get_column_letter(idx)].width = width
    style_header(ws, len(cols))

    leads = [
        p for p in posts
        if str(p.get("commercial_angle", "")).strip().lower().startswith("lead")
    ]
    leads.sort(key=lambda p: (str(p.get("subreddit", "")), -float(p.get("score", 0) or 0)))

    for r, post in enumerate(leads, start=2):
        for idx, (_, key, _) in enumerate(cols, start=1):
            value = post.get(key, "")
            cell = ws.cell(row=r, column=idx, value=value)
            cell.border = BORDER
            cell.alignment = WRAP
            if key == "url" and value:
                cell.hyperlink = value
                cell.font = Font(color="1D4ED8", underline="single", size=10)
        est = len(str(post.get("dm_draft", ""))) / 78 * 14
        ws.row_dimensions[r].height = max(60, min(240, est))

    if not leads:
        ws.cell(row=2, column=1, value="No posts this week were a better DM than a comment.").font = Font(italic=True)
    return ws


def build_pulse(wb, communities):
    """What each community has actually been talking about this week."""
    ws = wb.create_sheet("Community Pulse")
    cols = [
        ("Subreddit", "subreddit", 20),
        ("Posts read", "posts_scraped", 12),
        ("What they are talking about", "themes", 62),
        ("Questions that keep coming up", "recurring_questions", 44),
        ("How they write", "voice", 52),
        ("Culture and vendor tolerance", "culture_note", 36),
        ("Where this business fits", "opportunity", 46),
    ]
    for idx, (label, _, width) in enumerate(cols, start=1):
        ws.cell(row=1, column=idx, value=label)
        ws.column_dimensions[get_column_letter(idx)].width = width
    style_header(ws, len(cols))

    for r, com in enumerate(communities, start=2):
        for idx, (_, key, _) in enumerate(cols, start=1):
            cell = ws.cell(row=r, column=idx, value=com.get(key, ""))
            cell.border = BORDER
            cell.alignment = WRAP
        ws.row_dimensions[r].height = 92
    return ws


def build_run_info(wb, run):
    ws = wb.create_sheet("Run Info")
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 78
    ws.cell(row=1, column=1, value="Field")
    ws.cell(row=1, column=2, value="Value")
    style_header(ws, 2)

    rows = [
        ("Run date", run.get("date", "")),
        ("Company profile", run.get("company", "")),
        ("Communities loaded", run.get("communities_loaded", "")),
        ("Posts scraped", run.get("posts_scraped", "")),
        ("Apify actor", run.get("apify_actor", "")),
        ("Apify run id", run.get("apify_run_id", "")),
        ("Sort", run.get("sort", "")),
        ("Time window", run.get("time_window", "")),
        ("Posts per community", run.get("posts_per_community", "")),
        ("Filters applied", run.get("filters", "")),
        ("Mention mode", run.get("disclosure", "")),
        ("Notes", run.get("notes", "")),
    ]
    for r, (label, value) in enumerate(rows, start=2):
        a = ws.cell(row=r, column=1, value=label)
        b = ws.cell(row=r, column=2, value=value)
        a.font = Font(bold=True)
        for cell in (a, b):
            cell.border = BORDER
            cell.alignment = WRAP
    return ws


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as fh:
        data = json.load(fh)

    posts = data.get("posts", [])
    communities = data.get("communities", [])
    run = data.get("run", {})

    by_sub = {}
    for post in posts:
        by_sub.setdefault(post.get("subreddit", ""), []).append(post)
    for com in communities:
        picks = sorted(
            by_sub.get(com.get("subreddit", ""), []),
            key=lambda p: int(p.get("rank_in_community", 99)),
        )
        if picks:
            com.setdefault("best_score", picks[0].get("score", ""))
            com.setdefault("top_pick_title", picks[0].get("title", ""))
            com.setdefault("top_pick_url", picks[0].get("url", ""))
        else:
            com.setdefault("best_score", "")
            com.setdefault("top_pick_title", "")
            com.setdefault("top_pick_url", "")
            if not com.get("note"):
                com["note"] = "No qualifying posts this week"

    wb = Workbook()
    wb.remove(wb.active)
    build_top_posts(wb, posts)
    build_leads(wb, posts)
    build_pulse(wb, communities)
    build_summary(wb, communities)
    build_run_info(wb, run)
    wb.save(sys.argv[2])
    print(f"Wrote {sys.argv[2]}: {len(posts)} posts across {len(communities)} communities")


if __name__ == "__main__":
    main()
