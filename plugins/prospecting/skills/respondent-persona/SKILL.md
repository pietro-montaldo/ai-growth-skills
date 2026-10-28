---
name: respondent-persona
description: "Build a persona from a list of people who signed up for something: webinar or event registrants, lead-magnet downloads, waitlist sign-ups, form fills or survey respondents. Does light, web-only research per person with parallel sub-agents, then gives you one composite 'average person' plus how the list spreads across seniority, function, industry, company size and region, with the unknowns shown honestly. The persona describes roles and company types, never individuals. Use for \"create a persona from this list\", \"who signed up for my webinar\", \"who are the people who filled this form\", \"profile my respondents\", \"who is on my waitlist\", \"what's the average person on this list\", \"build an audience persona\". Not for deep research on one lead, not for scoring leads against your ICP (use icp-lead-ranker), and not for analysing what people wrote in their survey answers."
metadata:
  version: "0.2.0"
---

# Respondent Persona

Take a list of people who signed up for something and answer one question: who are these people, on average, and how do they spread out? You get a persona doc describing the composite "average sign-up", and a spread workbook with the breakdown on every dimension. Research is light per person on purpose. A long list doesn't need a dossier on each name. It needs a fast, honest read on the group.

It works the same for webinar and event registrants, lead-magnet sign-ups, waitlists, newsletter or community joins, and form or survey respondents.

**Works best with:** web search for the research sub-agents. No paid enrichment is used. The list can be a CSV or Excel export from your form, webinar, event or email tool, or pasted text.

## Reference files

- `references/dimensions-and-schema.md`: the five dimensions, their fixed buckets, and the `respondents.json` shape.
- `references/research-agent-prompt.md`: the brief each research sub-agent gets.
- `references/persona-template.md`: the layout of the persona doc.
- `scripts/build_persona_outputs.py`: builds the spread workbook and CSV from `respondents.json`. Needs `openpyxl`.

## Before starting

Read your context, so the persona can be compared with who you want to reach. Use the first that exists:

1. **GTM context.** A `gtm-hub.md` file means Notion: fetch the ICP page it links. A `gtm/README.md` file means the repo: read `gtm/icp.md`.
2. **A company profile file**, such as `COMPANY-PROFILE.md` or `about-me.md`.
3. **Nothing found:** skip the comparison, or ask one question: "Who did you hope would sign up?"

Writing voice for the persona doc: use your `<name>-voice` skill if installed, otherwise plain and short.

## Steps

### 1. Pause: confirm the inputs

Ask in one message:

- **Which list, and what it is.** The file, and what people signed up for (a webinar, a lead magnet, a waitlist, a survey). If you point at a folder, name the file you found and confirm it.
- **How much to research.** For lists over about 150 rows, offer a random sample (default 100) and project the spread, because web-only lookups on a long tail are slow and thin. Say which you're doing.

If the list already has rich fields (job title, company, industry, country), say so: research will mostly confirm and group rather than discover.

### 2. Load and normalise

Read the file (CSV, Excel, HTML export or pasted text). You need at least a name or an email per row. Map what exists into the fields in `references/dimensions-and-schema.md`.

Derive what you can with no research:

- **Company from the email domain**, unless it's a free provider (gmail, outlook, yahoo, icloud, proton, hotmail and similar). Free-domain emails get no company guess.
- **Self-reported fields** (title, company, country, company size) that the form collected. These outrank anything research finds. Keep them.

Drop or flag junk (test entries, blank rows, duplicate emails). Report how many rows loaded and how many you dropped.

### 3. Research with sub-agents (web only)

Don't research the list in the main conversation. Split respondents into chunks of about 25 and launch general-purpose research sub-agents, one per chunk, all in one message so they run in parallel (up to about 5 at a time, queue the rest).

Give each the brief in `references/research-agent-prompt.md` plus its chunk as JSON. Each does at most two web searches per person, fills the dimension fields, sets a confidence, and returns JSON rows. Web search only: no paid enrichment, no LinkedIn scraping, no browsing behind a login.

Merge results back by email, or by name when there's no email. Anything a sub-agent couldn't find stays `unknown`, never a guess dressed as fact.

### 4. Aggregate into a persona and a spread

For each dimension (seniority, function, industry, company size, region), count respondents per bucket and compute the share. `unknown` is its own bucket and is reported, not hidden.

Then write the **average sign-up**: a short composite built from the most common bucket on each dimension, for example "a mid-level marketing manager at a 50 to 200 person B2B software company in Western Europe". If a dimension is mostly unknown or evenly split, say so instead of forcing one label.

Be honest about confidence. If 40% of the list is `unknown` on industry, the persona says the industry read is weak. Keep what the data shows apart from what you infer.

If you have an ICP, add a short comparison: what share of the list looks like your ICP, and the biggest gap (for example "mostly individual contributors, while your ICP is heads of department").

### 5. Pause: show the read, then build the files

Show the average sign-up, the headline numbers per dimension and the unknown rates in chat. Ask before writing files.

Write `respondents.json` (shape in `references/dimensions-and-schema.md`) to `outputs/` in your working folder, then run the script from this skill's folder:

```bash
python3 <this skill folder>/scripts/build_persona_outputs.py outputs/respondents.json outputs/
```

It writes `<slug>-spread.xlsx` (Spread, Average respondent and Respondents sheets) and `<slug>-spread.csv`. Add `--anonymous` for a copy without names and emails that you can share.

Then write `<slug>-persona.md` by hand using `references/persona-template.md`. Use `YYYY-MM-DD-respondent-persona` as the slug, and give the paths.

## Rules

- **The persona describes the group, never individuals.** The persona doc and the chat summary use roles and company types only. No names, emails, LinkedIn URLs or "for example, Jane at Acme". Company names only when the respondent self-reported them and only as counts ("12 people from software companies"), never tied to a person.
- The Respondents sheet keeps names and emails so you can audit the read. Keep that file private, and use `--anonymous` for anything you share.
- Web-only research. No enrichment tools, no scrapers, no logging in.
- Self-reported form fields outrank researched guesses. Never overwrite what a respondent told you.
- `unknown` is a real answer. Report the unknown rate per dimension. Don't make the persona sound more certain than the data is.
- One list per run.
