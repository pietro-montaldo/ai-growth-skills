# Research playbook

What to pull from each source and in what order. Tool names differ between setups, so find each tool by what it does (the descriptions mention calendar, CRM, email, recordings and so on). If a tool is deferred, load it before use.

Order: CRM first, because it is your own ground truth. Outside sources only fill gaps.

## Calendar (or the pasted invite)

- List events for the next 7 days, or the window you named.
- External attendee = email domain differs from yours. Some people have two internal domains (a company domain plus a personal one). When unsure, ask.
- From the chosen event, pull: title, description (often has an agenda or links), start time, organiser, every attendee and whether they accepted.

No calendar: ask for the attendee names, their company, the time, and anything in the invite description.

## CRM (HubSpot, Pipedrive, Attio, Salesforce, a Notion database or similar)

Work contact, then company, then deals, then activity:

1. **Contacts:** search each external attendee by email. Pull name, title, lifecycle stage, owner, source, created date, last activity date, and any custom field that looks relevant.
2. **Company:** from the contact link or a domain search. Pull industry, size, location, revenue fields if present, lifecycle stage.
3. **Deals:** every deal linked to these contacts or the company, open and closed. Pull stage, amount, close date, pipeline and history. A deal lost last year is critical: find out why (check its notes and emails).
4. **Activity:** logged emails, meetings, calls, notes and tasks. Rep notes often hold the real story (objections, who decides).
5. **Recordings:** call activities may link to a recording or transcript.

The number and dates of past activities is the strongest first-call vs follow-up signal.

No CRM: ask "Have you spoken with them before? Any deal or proposal in play?" and use the answer.

## Email (or a pasted thread)

Search threads, then read the messages that matter:

- Per attendee: messages from or to their address.
- Per domain: messages from or to their company domain. This catches colleagues who are not on this call.
- Read newest first. Separate substance (questions, requirements, pricing, objections) from logistics (scheduling, invites). Only substance counts toward follow-up status.
- Pull: who started the relationship, what each side promised in writing, what was already sent (proposals, decks, so you know what they have seen), changes in tone, and any unanswered message. An email from you that they ignored is a landmine. Flag it.

## Call recordings (Fathom, Granola, Gong, Fireflies or similar, or pasted notes)

- Search meetings by attendee name, email and company name.
- For the most recent call, read the summary first. Read the transcript when the summary is thin or you need exact promises and objections.
- Pull: what each side promised, objections raised and how they landed, who spoke most, agreed next steps, and names of people mentioned who are not yet in your CRM (likely other stakeholders).

## Web search (always run)

Run it even for follow-ups. It catches what your CRM can't know.

- `<company> funding OR raised OR acquisition`: stage and money news.
- `<company> news`, last 3 months: leadership changes, launches, layoffs.
- `<company> <what they sell>`: their product and who they sell to.
- `"<attendee name>" <company>`: talks, podcasts, articles, job changes.

A recent funding round, acquisition or leadership change almost always belongs in the brief.

## Enrichment tool (only for gaps, ask first)

Use it only if one is connected AND the CRM left a specific gap: title and seniority, headcount, tools they use. Say how many lookups it is and ask before running, because it spends credits. Don't re-pull what the CRM already has. In the brief, call it "public company data".

## LinkedIn (only for gaps)

Only for person-level gaps left after the above. Three routes, in order of preference:

- **Pasted profile:** ask you to paste the profile text. Free and reliable.
- **Browser:** open the profile in a browser tool that is signed in, read only.
- **Scraper:** a LinkedIn scraper (for example an Apify actor), after saying it spends credits and getting a yes.

Pull: current title and time in role, past roles (a former customer at a past company is gold), recent posts and topics they care about, events they attended, visible mutual connections.

## Fact log

Keep a running log while you research, one fact per line, with the source:

```
[CRM/deal] Open deal "Acme, onboarding project": stage Proposal, $24,000, created 2026-04-12
[Email 2026-05-28] Dana asked about pricing for a second team; we sent the PDF, no reply since
[Recording 2026-05-14] Dana raised budget timing: "nothing approved before July"
[Web] Acme raised a $30M Series B on 2026-05-20 (trade press)
```

Write the brief from this log. If a sentence in the draft has no log line behind it, cut it or mark it as a guess. When sources disagree, put both in the brief.
