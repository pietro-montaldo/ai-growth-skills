---
name: clay-company-signals
description: "Build a company signals system in your own Clay workspace: pick one of your best customers, find lookalike companies, put them on a watchlist, watch them for buying signals (job posts, new hires, news, research intent) that match the triggers in your GTM context, and when a signal fires, find one person who can sign, find their work email, and add them to a buyer list or a Clay campaign. Recommends 100 companies to start. Asks before every write and every step that spends Clay credits. Use for \"set up Clay signals\", \"monitor a list of companies for signals\", \"build a lookalike watchlist\", \"alert me when target accounts hire or post jobs\", \"signal-based outbound in Clay\", \"enrol people when a signal fires\", \"add companies to my signals watchlist\". Not for one-off lead lists (use icp-lead-ranker), not for website visitor tracking, and it never launches a campaign or sends an email itself."
metadata:
  version: "0.1.0"
---

# Clay company signals

You end up with a system that runs by itself in your Clay workspace. A watchlist of companies that look like your best customer. Clay signals that watch them every week for the buying triggers in your ICP. A Clay workflow that, when a signal fires, checks it is real, finds one person who can sign, finds their work email and saves them to a buyer list, ready for a campaign. The skill builds and tests every piece with you. You launch the campaign and switch on emailing yourself, in Clay.

**Works best with:** the Clay CLI signed in (`clay whoami`), a Clay plan with Search, Signals, Audiences, Workflows and Campaigns, and at least one sender inbox connected in Clay. Your GTM context. Without the CLI, every step has a "do it in Clay" version in the reference files.

## Reference files

- `references/clay-setup-check.md`: run it first. Checks the CLI, the plan features, credits and inboxes.
- `references/lookalikes.md`: from one seed company to a reviewed list of N lookalikes.
- `references/watchlist.md`: the watch field, the watchlist segment, and the workflow that adds companies later.
- `references/signals.md`: how your ICP triggers become Clay signals, their settings, and the cost.
- `references/workflow.md`: the buyer workflow, node by node, and how to test it.
- `references/campaign.md`: the email copy, the workflow-type campaign, and the order for going live.
- `references/gotchas.md`: things Clay does that are easy to get wrong. Read it before building.
- `assets/read_signal.py`, `assets/email_lines.py`: code for the two Clay code steps.
- `assets/qualify_prompt.md`, `assets/pick_buyer_prompt.md`: prompts for the two AI steps. Fill them from your GTM context.

## Before starting

1. **GTM context.** A `gtm-hub.md` file means Notion: fetch the ICP, Product & offer, Messaging and Customers pages it links. A `gtm/README.md` file means the repo: read `gtm/icp.md`, `gtm/product.md`, `gtm/messaging.md` and filter `gtm/customers.csv`. You need: the ICP cards (who buys, company size, industry, titles, buying triggers, disqualifiers), the offer, proof you may share, and your customers.
2. **A company profile file**, such as `COMPANY-PROFILE.md`, if there is no GTM context.
3. **Ask once, in one batch,** for anything still missing: what you sell, who signs the deal (titles), what makes a company ready to buy now, and who you never want to contact. Offer to save it to `COMPANY-PROFILE.md`.
4. **Do-not-contact.** If `~/.claude/CLAUDE.md` has a `do-not-contact:start` block, use the check-do-not-contact skill in steps 2 and 7. If not, say the list is unchecked and suggest build-do-not-contact.
5. **Voice.** Use your `<name>-voice` skill if installed. Otherwise ask for 2 or 3 cold emails you wrote that got replies.

Then run `references/clay-setup-check.md`.

## Steps

### 1. Pause: agree the plan

Ask in one message:

- **Which offer and ICP card** this watchlist is for. One card per watchlist keeps the copy and the buyer pick sharp.
- **The seed company.** Suggest 2 or 3 from your best customers (the ones who came back for more), with one line each on why. You pick one.
- **How many companies to monitor.** Recommend **100** to start: enough for a few hits a month, cheap to watch while you tune it. Show the weekly signal cost for 100, 250 and 500 from `references/signals.md`.
- **Which signals.** Map the ICP's buying triggers to Clay signal types with `references/signals.md` and show the 2 or 3 that fit best.
- **Mode.** Start in **list mode**: the workflow saves buyers to a list and nobody is emailed. Emailing comes in step 7, once you trust the list.

### 2. Pause: build and review the lookalike list

Follow `references/lookalikes.md`. Draft the search from the seed company and the ICP card, pull a sample of 10, show it, and adjust until you say it looks right. Then pull N plus a buffer, drop customers, open deals, competitors and do-not-contact companies, and save `outputs/<date>-signals-watchlist.csv`. Show the counts and wait for an OK.

### 3. Pause: create the watchlist in Clay

Follow `references/watchlist.md`. List what will be created (one company field, one segment, one small workflow) and how many workflow runs adding the companies uses. After a yes, build it, add the companies, and show the segment count against the CSV.

### 4. Pause: create the signals

Follow `references/signals.md`. Show each signal's settings in plain words, the schedule, and the cost forecast. Create them **paused**, read them back, and resume only after a clear yes. Tell you where to see them: Companies, Data hub, Signals.

### 5. Pause: build and test the buyer workflow

Follow `references/workflow.md`. Fill `assets/qualify_prompt.md` and `assets/pick_buyer_prompt.md` from the ICP card and show both. Build the workflow as a draft in list mode, then test it once on a real or sample hit. Quote the cost first (about 3 to 5 credits). Show what each step did and who was picked. Fix and retest until the pick is a real signer.

### 6. Pause: you publish it in list mode

Give the workflow link and ask you to press **Publish** in Clay. In list mode nobody is emailed: every qualified signal from then on adds one person to the buyer list. Then check the published version with the CLI and show where the list lives.

### 7. Pause: emailing, only when you ask

Follow `references/campaign.md`. Write the copy from your own wording, show 2 versions filled in for a real person on the list, and agree one. Run the spam check. You create the workflow-type campaign in Clay. The skill adds the copy, then you upload your do-not-contact blocklist and press Launch. The skill adds the enrol step to the draft workflow. **You press Publish in Clay yourself.** That is the moment emails start.

## Rules

- Never send, launch, resume or publish. You press Publish, Launch and Resume in Clay yourself.
- Every Clay write is listed first and waits for a yes. Every credit-spending step quotes the count and the cost first.
- Signals are created paused and read back before they run.
- One person per company, and a company is skipped for 90 days after someone there was added.
- Pick only people who can sign. If nobody fits, add nobody.
- Never invent a role, email or company detail. Never guess an email address.
- Proof in emails comes only from customers who gave permission, as recorded in your GTM context.
- No names, emails or company details in segment, field, campaign or workflow names.
- Write in plain language, short sentences, no em dashes.
