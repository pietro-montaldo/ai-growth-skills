# Sub-agent research brief

Paste this brief into each general-purpose research sub-agent (one with web search), then append that agent's chunk of respondents as JSON. One agent per chunk of ~25, run in parallel.

---

You are profiling a chunk of people who signed up for something: a webinar or event, a lead magnet, a waitlist, a form or a survey. For each person, do a quick, superficial read of who they are professionally. This is light research for a group persona, not a deep dossier. Spend at most one or two web searches per person, then move on.

## Rules

- **Web search only.** No paid enrichment tools, no LinkedIn scraping, no logging into anything, no browsing profiles behind a login. Public web results only.
- **Two searches max per person.** Typical query: the person's name plus their company or email domain. If nothing useful comes back, stop and mark the fields `unknown`. Do not keep digging.
- **Never invent.** If you cannot establish a field from what you found, it is `unknown`. A confident wrong label is worse than an honest unknown.
- **Respect self-reported fields.** If the row already has a title, company, or country from the form, trust it over anything you find. Only research the gaps.
- **Don't write personal details into `evidence`.** Describe the source ("title from company About page"), not the person's private information.
- **Email domain is a free signal.** A non-free domain usually names the company. Free domains (gmail, outlook, yahoo, icloud, proton, hotmail, etc.) tell you nothing about the company, so leave company `unknown` unless a search surfaces it.

## For each person, return these fields

Use the exact bucket values from the dimensions list (seniority, function, industry, company_size, region). Assign:

- `seniority`, `function`, `industry`, `company_size`, `region`: one bucket each, or `unknown`.
- `company` and `company_source` (`self_reported`, `email_domain`, `research`, or `unknown`).
- `confidence`: `high` if self-reported or a clearly named source; `medium` if a reasonable inference from a found page; `low` if thin or indirect.
- `evidence`: one short, specific line on what the read is based on.

## Output

Return only a JSON array of objects, one per person in your chunk, matching the respondents schema. No prose around it. Preserve the `name` and `email` exactly as given so the rows can be merged back.
