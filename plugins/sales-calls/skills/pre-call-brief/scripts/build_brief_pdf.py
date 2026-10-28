#!/usr/bin/env python3
"""
Build the pre-call briefing PDF from a JSON data file.

Usage:
    python3 build_brief_pdf.py brief.json output.pdf

Why this exists: hand-rolled PDF layouts come out crowded. This renders one consistent,
spacious document via HTML + WeasyPrint, so the skill can focus on research and hand
structured data to a known-good template.

Look: neutral by default (see references/brand.md). Pass a "brand" object in the JSON to use
your own colours, font, logo and company name. The JSON schema is in
references/brief-data-schema.md. Any field may be omitted.

Money is never struck through. Unknown amounts render as a visible "$XXX" placeholder.
Figures listed in "redact" become solid bars and their digits are removed from the file.

If WeasyPrint is not installed, the script writes an HTML file instead (same name, .html),
which can be opened in a browser and printed to PDF.
"""
import html
import json
import os
import sys

DEFAULTS = {
    "primary": "#2F6FEB",
    "dark": "#111827",
    "ink": "#374151",
    "muted": "#6B7280",
    "soft": "#F5F6F8",
    "font": "Inter",
}


def esc(x):
    return html.escape(str(x)) if x is not None else ""


def tint(hex_color, amount=0.9):
    """Mix a hex colour with white. amount=0.9 gives a very light tint for callouts."""
    h = hex_color.lstrip("#")
    if len(h) != 6:
        return "#F5F6F8"
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (round(c + (255 - c) * amount) for c in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"


def header_mark(brand):
    """Logo image if given, else the company name as text, else nothing."""
    if brand.get("logo"):
        return f'<div class="mark"><img src="{esc(brand["logo"])}" alt="{esc(brand.get("name", ""))}"></div>'
    if brand.get("name"):
        return f'<div class="mark"><span class="mark-text">{esc(brand["name"])}</span></div>'
    return ""


def li_list(items, cls=""):
    if not items:
        return ""
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<ul class="{cls}">{lis}</ul>'


def people_cards(people):
    cards = []
    for p in people or []:
        role = f'<span class="role-pill">{esc(p["role"])}</span>' if p.get("role") else ""
        cards.append(f"""
        <div class="person">
          <div class="person-head"><h3>{esc(p.get('name', ''))}</h3>{role}</div>
          <p class="person-title">{esc(p.get('title', ''))}</p>
          <p class="person-notes">{esc(p.get('notes', ''))}</p>
        </div>""")
    return "".join(cards)


def stat_row(stats):
    if not stats:
        return ""
    cells = "".join(
        f'<div class="stat"><div class="stat-val">{esc(s.get("value") or "$XXX")}</div>'
        f'<div class="stat-lab">{esc(s.get("label", ""))}</div></div>'
        for s in stats
    )
    return f'<div class="stats">{cells}</div>'


def footer_text(d, brand):
    parts = [brand.get("name"), d.get("footer_date"), "Confidential"]
    return "  ·  ".join(esc(p) for p in parts if p)


def build_html(d):
    brand = {**DEFAULTS, **{k: v for k, v in (d.get("brand") or {}).items() if v}}
    primary, dark = brand["primary"], brand["dark"]
    ink, muted, soft = brand["ink"], brand["muted"], brand["soft"]
    font = f"'{brand['font']}', 'Helvetica Neue', Arial, sans-serif"
    light = tint(primary, 0.9)

    banner = f'<div class="banner">{esc(d["banner"])}</div>' if d.get("banner") else ""
    company_profile = "".join(f"<p>{esc(p)}</p>" for p in d.get("company_profile", []))
    history_title = esc(d.get("history_title", "Relationship history"))

    commitments = ""
    if d.get("open_commitments"):
        commitments = f"""
        <div class="callout">
          <div class="callout-label">Open commitments</div>
          {li_list(d['open_commitments'])}
        </div>"""

    risks_block = ""
    if d.get("risks"):
        risks_block = f"""
        <section class="block">
          <div class="rule"></div><h2>Risks to watch</h2>
          {li_list(d['risks'], 'warn')}
        </section>"""

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{
  size: A4; margin: 0;
  @bottom-center {{
    content: "{footer_text(d, brand)}";
    font-family: {font}; font-size: 7.5pt; color: {muted};
    margin-bottom: 9mm;
  }}
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: {font}; color:{ink}; font-size:10pt; line-height:1.6; }}
.page {{ padding: 0 18mm; }}
.content {{ padding: 9mm 0 12mm; }}

.hero {{ background:{dark}; color:#fff; padding: 16mm 18mm 13mm; }}
.mark {{ margin-bottom: 12mm; }}
.mark img {{ max-height: 12mm; max-width: 60mm; }}
.mark-text {{ font-size:9pt; font-weight:600; letter-spacing:.2em; text-transform:uppercase; color:#fff; }}
.eyebrow {{ font-size:8.5pt; font-weight:600; letter-spacing:.22em; text-transform:uppercase;
  color:{tint(primary, 0.35)}; margin-bottom:7mm; }}
.hero h1 {{ font-size:30pt; font-weight:700; line-height:1.08; margin-bottom:7mm; }}
.pill {{ display:inline-block; background:{primary}; color:#fff; font-size:8.5pt; font-weight:600;
  letter-spacing:.06em; padding:5px 13px; border-radius:99px; }}
.meta {{ margin-top:8mm; display:grid; grid-template-columns:1fr 1.3fr 1.1fr; gap:8mm; }}
.meta > div {{ min-width:0; }}
.meta .k {{ font-size:7.5pt; letter-spacing:.16em; text-transform:uppercase; color:#A3AAB5;
  margin-bottom:3px; }}
.meta .v {{ font-size:9.5pt; color:#EEF1F4; line-height:1.5; word-wrap:break-word; }}

.banner {{ background:{light}; border-left:3px solid {primary}; color:{ink};
  font-size:8.5pt; padding:8px 12px; margin: 7mm 0 0; border-radius:0 6px 6px 0; }}

.block {{ margin-top: 11mm; }}
.rule {{ width:30px; height:3px; background:{primary}; margin-bottom:5mm; border-radius:2px; }}
h2 {{ font-size:14pt; font-weight:600; color:{dark}; margin-bottom:5mm; }}
p {{ margin-bottom: 3.5mm; color:{ink}; }}
.lead {{ font-size:11pt; }}

.stats {{ display:flex; gap:9mm; margin: 9mm 0 2mm; }}
.stat {{ flex:1; }}
.stat-val {{ font-size:22pt; font-weight:700; color:{primary}; line-height:1; }}
.stat-lab {{ font-size:7.5pt; letter-spacing:.1em; text-transform:uppercase; color:{muted};
  margin-top:3mm; line-height:1.4; }}

ul {{ list-style:none; margin-top:2mm; }}
li {{ position:relative; padding-left:7mm; margin-bottom:4mm; color:{ink}; }}
li::before {{ content:""; position:absolute; left:0; top:2.6mm; width:7px; height:7px;
  background:{primary}; border-radius:2px; }}
ul.warn li::before {{ background:{dark}; }}

.people {{ display:flex; flex-wrap:wrap; gap:7mm; }}
.person {{ flex:1 1 calc(50% - 4mm); background:#fff; border:1px solid #E5E7EB;
  border-radius:10px; padding:6mm 6mm 5mm; }}
.person-head {{ display:flex; align-items:baseline; justify-content:space-between; gap:6px; }}
.person h3 {{ font-size:11.5pt; font-weight:600; color:{dark}; }}
.person-title {{ color:{primary}; font-weight:600; font-size:8.5pt; margin:1mm 0 3mm; }}
.person-notes {{ font-size:8.5pt; line-height:1.55; margin:0; }}
.role-pill {{ font-size:6.5pt; font-weight:600; letter-spacing:.08em; text-transform:uppercase;
  color:{primary}; border:1px solid {primary}; border-radius:99px; padding:2px 7px; white-space:nowrap; }}

.callout {{ background:{soft}; border-radius:10px; padding:5mm 6mm; margin-top:6mm; }}
.callout-label {{ font-size:7.5pt; font-weight:600; letter-spacing:.12em; text-transform:uppercase;
  color:{dark}; margin-bottom:2mm; }}
.callout li {{ margin-bottom:2.5mm; font-size:9pt; }}

.avoid-break {{ break-inside: avoid; }}
.redact {{ display:inline-block; background:{dark}; border-radius:3px; height:0.95em;
  vertical-align:-0.13em; }}
</style></head><body>

<div class="hero">
  {header_mark(brand)}
  <div class="eyebrow">Pre-call brief</div>
  <h1>{esc(d.get('company', ''))}</h1>
  <div><span class="pill">{esc(d.get('call_type', ''))}</span></div>
  <div class="meta">
    <div><div class="k">When</div><div class="v">{esc(d.get('date_time', ''))}</div></div>
    <div><div class="k">Them</div><div class="v">{'<br>'.join(esc(x) for x in d.get('their_side', []))}</div></div>
    <div><div class="k">Us</div><div class="v">{'<br>'.join(esc(x) for x in d.get('our_side', []))}</div></div>
  </div>
  {banner}
</div>

<div class="page"><div class="content">

  <section class="block">
    <div class="rule"></div><h2>Objective</h2>
    <p class="lead">{esc(d.get('objective', ''))}</p>
  </section>

  <section class="block avoid-break">
    <div class="rule"></div><h2>Company profile</h2>
    {company_profile}
    {stat_row(d.get('stats'))}
  </section>

  <section class="block">
    <div class="rule"></div><h2>Who's on the call</h2>
    <div class="people">{people_cards(d.get('people'))}</div>
  </section>

  <section class="block">
    <div class="rule"></div><h2>{history_title}</h2>
    {li_list(d.get('history'))}
    {commitments}
  </section>

  <section class="block avoid-break">
    <div class="rule"></div><h2>Talking points</h2>
    {li_list(d.get('talking_points'))}
  </section>

  {risks_block}

  <section class="block avoid-break">
    <div class="rule"></div><h2>Smart questions</h2>
    {li_list(d.get('questions'))}
  </section>

</div></div>
</body></html>"""


def apply_redactions(html_str, terms):
    """Replace each sensitive term with a solid bar sized to the original text. The characters
    are dropped from the document, so a shared file leaks nothing."""
    for t in terms or []:
        et = html.escape(str(t))
        if not et:
            continue
        width = max(2.5, len(str(t)) * 0.52)
        html_str = html_str.replace(et, f'<span class="redact" style="width:{width:.1f}em"></span>')
    return html_str


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 build_brief_pdf.py brief.json output.pdf")
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    doc = apply_redactions(build_html(data), data.get("redact", []))
    base = os.path.dirname(os.path.abspath(src))
    try:
        from weasyprint import HTML
    except ImportError:
        html_out = os.path.splitext(out)[0] + ".html"
        with open(html_out, "w", encoding="utf-8") as f:
            f.write(doc)
        print("WeasyPrint is not installed. Wrote", html_out)
        print("Open it in a browser and print to PDF, or install WeasyPrint: pip install weasyprint")
        return
    HTML(string=doc, base_url=base).write_pdf(out)
    print("Wrote", out)


if __name__ == "__main__":
    main()
