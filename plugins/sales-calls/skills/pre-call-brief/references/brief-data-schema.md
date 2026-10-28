# Brief data schema

`scripts/build_brief_pdf.py` renders the PDF from one JSON file. Do the research first, build this object from the fact log, then run:

```
python3 <this skill folder>/scripts/build_brief_pdf.py brief.json YYYY-MM-DD-<company>-call-brief.pdf
```

WeasyPrint does the rendering. If it isn't installed, the script writes an HTML file next to the PDF path instead, which you can open in a browser and print to PDF.

Every field is optional and the layout copes with gaps, but a strong brief fills them all. All names below are made up.

```json
{
  "brand": {
    "name": "Brightlane Consulting",
    "logo": "logo.png",
    "primary": "#2F6FEB",
    "dark": "#111827",
    "font": "Inter"
  },
  "redact": ["$24,000"],
  "company": "Acme Corp",
  "call_type": "Follow-up · 3rd conversation",
  "date_time": "Tue 10 Jun 2026, 15:00 CEST",
  "their_side": ["Dana, VP Marketing", "Sam, RevOps lead"],
  "our_side": ["You (Founder, Brightlane)"],
  "banner": "No calendar invite found. Assuming a check-in next week.",
  "objective": "One sentence on the goal of this specific call.",
  "company_profile": ["What they do.", "Stage and recent news."],
  "stats": [
    {"value": "$24,000", "label": "Open deal, proposal stage"},
    {"value": "200+", "label": "Employees"},
    {"value": "Day 14", "label": "Since last touch"}
  ],
  "people": [
    {"name": "Dana", "title": "VP Marketing", "role": "Decision maker",
     "notes": "Background, time in role, rapport hooks, recent posts."}
  ],
  "history_title": "Relationship history",
  "history": ["Dated timeline line.", "Another."],
  "open_commitments": ["Ours: send the revised scope (still open).", "Theirs: confirm budget."],
  "talking_points": ["Specific point grounded in the research.", "..."],
  "risks": ["A competitor is in play.", "Thread stalled since May."],
  "questions": ["A question that proves you did your homework.", "..."],
  "footer_date": "2026-06-08"
}
```

## Field notes

- `brand`: all keys optional. `name` shows at the top of the header and in the footer. `logo` is an image path (relative to the JSON file) or a URL; it replaces the text name in the header. `primary` is the accent colour, `dark` the header band and headings, `font` a font installed on the machine. Leave `brand` out to get the neutral default from `brand.md`. With no `name`, the footer shows only the date and "Confidential".
- `call_type`: "First call" or "Follow-up · Nth conversation".
- `history_title`: "Relationship history" for follow-ups, "Why this call" for first calls.
- `people[].name`: use the name as it appears on the invite. This brief is for you, not for a public page. Don't add personal emails or phone numbers.
- `redact`: exact strings to hide. See below.

## Money rule

Put deal values, contract amounts and prices in `stats` and in `history` or `open_commitments` as full figures. Never strike them through. If an amount is unknown, set the stat value to `"$XXX"` so the gap is obvious and you can chase it. Don't drop the stat.

To hide a figure on purpose (a copy you will share), list the exact strings in `redact`. Each match becomes a solid bar and the digits are removed from the file, so the number can't be copied out. Use each figure exactly as it appears in the content (both `"$20,000"` and `"EUR 17,000"` if both forms are used). Only redact what you asked for. Leave non-money numbers alone.
