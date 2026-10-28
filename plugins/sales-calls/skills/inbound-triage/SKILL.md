---
name: inbound-triage
description: "Weekly review of your inbound buying interest. Finds people who reached out in the last 7 days wanting to buy what you sell, across the channels you choose (email, LinkedIn DMs, your booking tool such as cal.com or Calendly, website forms, or anything you paste), checks every open lead in your CRM or lead log, and gives you one numbered report with a recommended next action per lead. Then drafts replies and follow-ups and updates your CRM, CSV or markdown lead log only for what you pick. Never sends. Use for \"review my inbound\", \"who reached out this week\", \"did I answer everyone\", \"which leads need a nudge\", \"update my CRM with this week's inbound\". Not for partnerships or collaborations (flagged only), outbound prospecting, or post-call follow-ups (use call-followup-email)."
metadata:
  version: "0.1.0"
---

# Inbound triage

One job: keep your commercial pipeline current. Each week, find the new inbound interest, check every lead that is already open, and tell you what needs you. You decide. The skill drafts and updates only what you pick. Nothing is ever sent.

Works best with: your email, your CRM, your booking tool, and a LinkedIn messages connector. None is required. You can paste threads or upload exports for any channel.

## Reference files

- `references/channels.md`: how to collect each channel, with the paste or export fallback. Read it before step 2.
- `references/classification.md`: what counts as an opportunity, interest levels, status and follow-up timing. Read it before step 3.
- `references/lead-log-schema.md`: the columns for a CSV or markdown lead log, and how to map them to a CRM.
- `references/review-layout.md`: the report layout, a made-up example, and the rules for drafts.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: `gtm-hub.md` means Notion (fetch the pages it links), `gtm/README.md` means the repo (read the pages it links). Your offers and ICP decide what counts as an opportunity and how good a fit it is.
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise ask once, in one batch: what you sell (each offer, with its link if public), who it is for, and your email domain(s).
2. **Setup, first run only.** Look for an "Inbound setup" section in `COMPANY-PROFILE.md`. If it's missing, ask once, in one batch:
   - Which channels to check: email, LinkedIn DMs, booking tool (which one), website or form tool (which one), anything else. Each is optional.
   - Where leads are logged: your CRM (which one, if connected), or a lead log in this folder (`leads.csv` or `leads.md`). If there's none yet, offer to create `leads.csv` from `references/lead-log-schema.md`.
   - Your offer categories, if you sell more than one thing (for example: product, done-for-you service, training, sponsorship).
   Offer to save the answers under "Inbound setup" in `COMPANY-PROFILE.md`, so later runs skip this.
3. Voice: use your `<name>-voice` skill if installed. Otherwise ask for 3 to 5 replies you wrote and match them.

## Steps

### 1. Load the open pipeline

Read every lead whose stage is not Won or Lost, from your CRM (filter by stage, don't pull everything) or your lead log. Keep name, company, email, LinkedIn, stage, last contact, next step, latest communication. This list is used twice: to match this week's inbound to existing leads, and for the sweep in step 4.

### 2. Collect the last 7 days

For each channel you chose, follow `references/channels.md`. Collect only threads with a message (either way) in the last 7 days, and bookings or form entries created in the last 7 days. You can widen the window for one run.

For a channel with no connector, ask you to paste the threads or upload the export. If you skip it, mark it "not checked" in the report. Never estimate.

For a big week (more than about 40 candidate threads), hand each channel to a separate subagent in parallel and ask each for a compact table, so the main run keeps only conclusions.

### 3. Classify

Follow `references/classification.md`. For each person (merge channels, one person counts once): bucket (opportunity, flagged or noise), offer category, interest (high, medium, low), match to an existing lead, and status (needs reply, waiting, follow-up due, closed no response, done). Judge fit against your ICP from context.

Check your email drafts so you never propose a draft for a thread that already has one.

### 4. Sweep the open pipeline

For every open lead from step 1, whether or not it showed up this week: is the next step due or past due? How many days since last contact? Did anything happen this week? If you need the follow-up count, open the thread. Don't guess.

Turn each into one recommended action: reply, follow up (say which number, 1 to 3), update the next step, move the stage, or close as Lost. Flag any open lead that isn't a commercial opportunity and propose removing it.

### 5. Pause 1: report and ask

Write one numbered report, laid out as in `references/review-layout.md`, so you can answer "draft 2 and 5, move 7, close 9". Every lead gets a recommended next action.

Ask what to draft, what to log and which moves to make. Don't draft, log or change a stage before you pick. In a scheduled run with nobody there, stop here and save the report to `outputs/inbound/YYYY-MM-DD-inbound-review.md`.

### 6. Do what you picked

- **Drafts:** follow the draft rules in `references/review-layout.md`. Email replies become drafts threaded to the latest message. LinkedIn and other DM replies are text, ready to paste.
- **Logging:** search your CRM or lead log (email, LinkedIn, name, company) before creating. Update instead of duplicating. Before each new entry, check once more: would this person pay you? If not, don't log it and say why.
- Show the exact rows or field changes before writing them, then write.

### 7. Close out

List the drafts created and where, the leads logged or updated, and anything not checked. Offer to save the report to `outputs/inbound/`.

## Rules

- **Commercial only.** A lead is someone who would pay you for one of your offers. Partnerships, collaborations, affiliate or revenue-share offers, favours, feedback requests and existing clients handling logistics are flagged in one line, never logged.
- **Recommend first.** No draft, no new entry and no stage change before you pick.
- **Never send.** Never archive, label or delete email. Never accept or decline bookings.
- Counts come only from what was actually read. Say how far paging got if it stopped early. Write "not checked" instead of guessing.
- Separate what you read from what you inferred.
- Never invent a link, date, price or discount code. Use links from your context, or ask.
- No enrichment or profile lookups unless you ask, and then say how many lookups and whether they spend credits first.
- When you correct a category, stage or draft, offer to add the correction to your "Inbound setup" notes.
