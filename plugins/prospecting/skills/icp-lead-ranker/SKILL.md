---
name: icp-lead-ranker
description: "Take a file of potential leads, research each one with parallel sub-agents, score them 0 to 5 against your ICP, and return a ranked Excel workbook (an overview sorted by fit plus one detail tab per lead) and a short chat summary. Reads your ICP from your GTM context first, and pushes back if it's too vague to score against. Works with web research only; enrichment tools are optional and only used after a credit check. Use for \"are these in my ICP\", \"rank these leads\", \"score this list against my ICP\", \"qualify these leads\", \"who in this file is a fit\", \"sort this list by fit\", or when you hand over a spreadsheet of people and want them ranked. Not for one named lead (too heavy for one person), not for defining your ICP (use the GTM Context Kit's gtm-icp skill) and not for sending outreach."
metadata:
  version: "0.2.0"
---

# ICP Lead Ranker

You hand over a file of leads. You get back a ranked workbook: an Overview tab sorted by fit, one detail tab per lead with the research and sources, and a short summary in chat. In the middle, research sub-agents look up each lead, and every lead gets a 0 to 5 score against your ICP with a one-line reason and a next step. The skill ranks. It never contacts anyone.

**Works best with:** web search for the research sub-agents. Optional: an enrichment connector (Apollo, Clay or similar) or Apify for LinkedIn data, used only after you approve the credit cost. A Google Drive connector helps if the list is a Google Sheet.

## Reference files

- `references/icp-and-scoring.md`: how to turn your ICP into a scoring card, the vague-ICP check, the 0 to 5 scale and the tie-breaks.
- `references/research-brief.md`: the brief each research sub-agent gets, and the dossier it returns.
- `scripts/build_xlsx.py`: builds the ranked workbook from `leads.json`. Needs `openpyxl`.

## Before starting

Find your ICP and offer. Use the first that exists:

1. **GTM context.** A `gtm-hub.md` file means Notion: fetch the ICP page and the Product & offer page it links. A `gtm/README.md` file means the repo: read `gtm/icp.md` and `gtm/product.md`. The ICP page's hard filters, public scoring signals, anti-ICP and buying triggers become the scoring card directly. Never read the CSV banks whole.
2. **A company profile file**, such as `COMPANY-PROFILE.md` or `about-me.md`.
3. **Ask once, in one batch:** what you sell, who buys it (role, company type, size, geography), and who you never want as a customer. Offer to save the answers to `COMPANY-PROFILE.md` so the next skill doesn't ask again.

## Steps

### 1. Pause: confirm the inputs

Ask in one message, and don't assume:

- **The lead file.** A CSV or XLSX in the working folder, or a Google Sheet (read it with your Drive connector, or ask for a CSV export). Don't guess column names until the file is open.
- **Which offer and which ICP.** If the ICP page has more than one ICP, ask which to score against, or score against all and record the best match.
- **Enrichment.** Web research only (free, default), or an enrichment connector or Apify on top (costs credits). The credit count comes in step 4.

### 2. Pause: check the ICP is sharp enough to score

Turn the ICP into a scoring card using `references/icp-and-scoring.md`: must-haves, strong signals, negatives, and who is out.

If the ICP is vague ("good companies", "people who'd like this", "founders", "anyone in marketing"), push back before scoring. Ask:

- "What would make you say yes to a lead in five seconds? Name the role, company type and size."
- "Who looks like a fit on paper but you'd never want to contact? Why?"
- "Which of these must all be true, and which are nice to have?"

Show the scoring card and get an OK. If anything is still unclear after one round, write down how you'll read it and confirm that. Never score against a guessed ICP.

### 3. Read and normalise the file

Load the file and map columns loosely to: `name` (required; the first column if unlabelled), `company`, `role` (title or headline), `linkedin_url` (any column containing "linkedin"), `email`, `location`. Keep every original row. Drop fully empty rows. Flag duplicates but don't remove them.

Report back: number of leads, the columns found, and any criterion on the scoring card that has no matching column and must come from research.

### 4. Pause: plan the research and the cost

Tell you the plan before launching:

- **Batching:** one research sub-agent per lead for under about 15 leads, or 5 to 10 leads per sub-agent for longer lists.
- **Estimate:** about 2 or 3 web searches per lead. Sub-agents run in parallel, so the wait is roughly one batch.
- **Credits, if enrichment was chosen:** the number of lookups and the expected credit cost. Check the connector's credit balance where it shows one. Wait for a clear yes. Without one, research with the web only.

### 5. Research each lead with sub-agents

Launch all research sub-agents in one message so they run at the same time. Use a general-purpose sub-agent with web search. Give each one the brief in `references/research-brief.md`, the scoring card, and its batch of leads.

Sub-agents gather facts. They don't score. They return a short dossier per lead: current role and seniority, company and what it does, size, location, each scoring-card signal found or not found, any competitor or anti-ICP signal, and 2 to 4 source URLs.

If enrichment was approved, run it in batches matched on LinkedIn URL plus name. Flag any match whose returned name or role clearly differs from the file as "verify". Ask for work emails only.

If a sub-agent fails, retry it once, then report which leads it held.

### 6. Score 0 to 5

Score every lead against the scoring card using `references/icp-and-scoring.md`. Set for each:

- `fit` (0 to 5), `band` (Strong 4 to 5, Moderate 3, Weak 0 to 2)
- `top_signal`: the one fact that drives the score
- `rationale`: one or two plain sentences
- `next_step`: the offer or angle to lead with and the hook, or "skip" for 0 to 1

The person's real current role and seniority is the main signal. Anyone who sells what you sell is capped at 2. Thin data means a conservative score, marked provisional. Borderline leads go up, not down: you make the final call.

### 7. Pause: show the summary, then build the workbook

In chat, show the counts per band, the top 3 leads with their one-line reason, and anything off (private profiles, no email, suspected competitors, "verify" matches). Ask before building.

Write `leads.json` in the shape at the top of `scripts/build_xlsx.py`, then run it from this skill's folder:

```bash
python3 <this skill folder>/scripts/build_xlsx.py outputs/leads.json outputs/
```

It writes `<slug>-leads-ranked.xlsx`. Use `YYYY-MM-DD-icp-lead-ranking` as the slug, save in `outputs/` in your working folder, and give the path.

## Rules

- Ranks only. Never sends, connects, messages or adds anyone to a sequence. Hand the ranked file to your outreach tools.
- Never score against a guessed ICP. Push back first.
- Credits: state the count and cost, and wait for a yes, every time.
- Every score shows its evidence. Never invent a role, company size or email. Unknown stays unknown.
- Don't paste emails or phone numbers into the chat summary. They stay in the workbook, in your own folder.
- One file per run. Every row in the file gets a score, and the original file is never changed.
- Rationales and next steps follow the writing style: plain, short, no em dashes.
