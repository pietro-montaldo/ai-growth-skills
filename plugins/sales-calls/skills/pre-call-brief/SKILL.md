---
name: pre-call-brief
description: "Research the people and company on your next sales call and turn it into a short briefing PDF plus a slide deck you can glance at during the call. Tells a first call from a follow-up and shapes the brief to match, runs a research waterfall (CRM, email, call recordings, web, LinkedIn) where every source is optional, keeps a sourced fact log, and styles both files in your brand colours or a clean default. Use for \"prep my next call\", \"who am I talking to tomorrow\", \"pre-call brief\", \"call prep for Acme\", \"get me ready for the 3pm demo\", or any upcoming sales conversation you want context on. Not for writing the follow-up after the call (use call-followup-email) or for researching a whole lead list."
metadata:
  version: "0.1.0"
---

# Pre-call brief

Two deliverables for one sales call: a 2 to 4 page briefing PDF and a 5 to 7 slide HTML deck. The value is in the research, not the formatting. A brief that tells you something you didn't know about the people on the call is a success. A pretty document full of generic filler is a failure.

Works best with: a calendar, your CRM, your email, your call recorder (Fathom, Granola, Gong or similar) and web search. None is required. You can paste the invite, past emails and call notes instead.

## Reference files

- `references/research-playbook.md`: what to pull from each source, in what order, and how to keep the fact log. Read it before step 4.
- `references/brief-data-schema.md`: the JSON the PDF script reads, with a filled example. Read it before step 7.
- `references/brand.md`: the default palette and how to use your own brand instead. Read it before step 6.
- `scripts/build_brief_pdf.py`: renders the PDF from the JSON. Call it by its full path in this skill's folder.
- `assets/slides-template.html`: the deck template.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: a `gtm-hub.md` file means it lives in Notion (fetch the pages it links), a `gtm/README.md` file means it lives in the repo (read the pages it links). Product, ICP, competitors and objections all sharpen the brief.
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise ask once, in one batch: what you sell, who buys it, your company name, and your email domain (so the skill can tell internal people from external ones). Offer to save the answers to `COMPANY-PROFILE.md`.
2. Check which tools are connected (calendar, CRM, email, call recorder, web search, a browser, any enrichment tool). Note what is missing. Never stop because one is missing.

## Steps

### 1. Identify the call

If you named a person, company or time, find that event. Otherwise take the next event in the coming 7 days with at least one attendee outside your email domain. With no calendar connected, ask who the call is with and when, or ask you to paste the invite. If several calls qualify, list them and let you pick.

### 2. Check it is a sales call

Signals, most reliable first: the attendee is in your CRM with a deal or as a lead; the title or description uses sales words (intro, demo, discovery, proposal, pricing, pilot, renewal); past emails read as a commercial conversation. If the signals conflict, ask one short question ("Is your 2pm with Jane at Acme a sales call?"). Don't guess.

### 3. First call or follow-up

Decide early, because it shapes the whole brief.

- **Follow-up** if your CRM shows logged meetings or emails, a deal exists (open or closed), there are real email threads (not just scheduling), or a past call recording exists.
- **First call** if the relationship is cold or only scheduling so far.

A first-call brief leads with the company, the people, a guess at why they took the call, and qualification questions. A follow-up brief leads with what happened last time: what each side promised (flag what is still open), deal stage and history, and what changed since the last touch.

### 4. Research waterfall

Run the sources in the order in `references/research-playbook.md`: CRM, email, call recordings, web, then enrichment and LinkedIn only for gaps. Every source is optional. If none are connected, ask you to paste what you have (the invite, the last email thread, call notes, the LinkedIn profile text) and research the company on the web.

Before any step that spends credits (an enrichment tool, a LinkedIn scraper), say how many lookups it is and ask first.

Depth scales with importance. A first call with a new company gets the full waterfall. A fourth follow-up with a known contact mostly needs the CRM, email and the last call, read deeply.

Keep a fact log as you go, one line per fact with its source. The brief is written from this log.

### 5. Pause 1: show what you found

Show in chat: first call or follow-up, the 3 most useful findings, the open commitments, and the gaps (sources missing or empty). Ask: "Anything to add, correct or leave out? Is this brief for your eyes only, or will you share it?" If it will be shared, ask which money figures to hide. Don't build the files on silence.

### 6. Pick the look

Read `references/brand.md`. Use your brand colours and logo if they are in your context. If not, ask once: "Do you want your brand colours and logo on this? Give me your website and I'll pull them, or say no and I'll use the clean default." Save what you find to `COMPANY-PROFILE.md` if you agree, so the next run doesn't ask.

### 7. Build the files

Save both in your working folder (or `outputs/`), named `YYYY-MM-DD-<company>-call-brief.pdf` and `YYYY-MM-DD-<company>-call-deck.html`, where the date is the call date.

**PDF.** Don't hand-roll the layout. Build the JSON from `references/brief-data-schema.md`, then run:

```
python3 <this skill folder>/scripts/build_brief_pdf.py brief.json YYYY-MM-DD-<company>-call-brief.pdf
```

Section order: header, objective, company profile with 2 or 3 big stats, who's on the call, relationship history (or why this call, for a first call) with open commitments, 3 to 5 talking points, risks, 3 to 5 questions that prove you did your homework. If WeasyPrint is missing, the script saves an HTML file instead. Tell you to open it in a browser and print to PDF, or offer to install WeasyPrint (`pip install weasyprint`).

**Deck.** Copy `assets/slides-template.html`, fill the placeholders, keep it one self-contained file. One idea per slide, large type: title, company snapshot, who's who, history or hypothesis, talking points, questions and the top risk.

### 8. Deliver

Share both files with a 3 or 4 sentence summary that leads with the single most useful finding ("Heads up: the CTO from the last call left in March"). Name the research gaps plainly. Don't restate the brief.

## Rules

- Read only. Never send an email, create a CRM record or change a calendar event.
- No fabrication. Every claim traces to a fact log line. If something couldn't be checked, say so in the brief ("No past email found"). Mark guesses as guesses ("Likely evaluating X, based on...").
- Money stays visible by default. Deal values and prices show in full. An unknown amount shows as `$XXX`, never a missing field, never struck through. Hide a figure only when you ask, using the `redact` list in the JSON.
- Contradictions between sources (CRM says 200 staff, LinkedIn says 80) go in the brief. Stale data is useful to know.
- Use what is publicly visible about attendees in a professional setting. No home addresses, family details or private social accounts.
- Keep the brief to 4 pages. Cut content before you shrink the type.
