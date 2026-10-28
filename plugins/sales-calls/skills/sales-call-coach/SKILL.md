---
name: sales-call-coach
description: "Review your recent sales calls like a sales coach would. Pulls your external calls from your call recorder (or transcripts you paste or upload), works out which ones were sales calls from what was said, coaches each one on call basics (talk ratio, monologues, questions, missed buying signals, next step) plus the framework that fits the call (SPIN, Sandler, MEDDIC, Challenger, or a quick health check), and writes one review with the action items you owe prospects. Use for \"coach my sales calls\", \"review my calls this week\", \"weekly sales review\", \"what should I do better on calls\", \"coach the Acme call\", or \"what do I owe prospects this week\". Not for writing the follow-up email (use call-followup-email) or for preparing a call that hasn't happened (use pre-call-brief)."
metadata:
  version: "0.1.0"
---

# Sales call coach

Act like a sales coach you hired, not a note taker. Tell you where you talked too much, where you missed a buying signal, where the next call should pick up, and what you owe the prospect this week. Pick the framework that fits each call. Don't force MEDDIC on a 12 minute intro call.

Works best with: a call recorder (Fathom, Granola, Gong, Fireflies or similar). Without one, paste the transcripts or drop the transcript files in your working folder.

## Reference files

- `references/call-classifier.md`: is it a sales call, and which type. Read it before step 2.
- `references/coaching-rubric.md`: the call basics, checked on every sales call.
- `references/frameworks.md`: which framework fits which call type, and what to check.
- `references/review-template.md`: the layout of the review file.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: `gtm-hub.md` means Notion (fetch the pages it links), `gtm/README.md` means the repo (read the pages it links). Your offer, ICP and objections help judge pitch and fit.
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise ask once, in one batch: what you sell, who buys it, and the email domain(s) you and your team use.
2. You need your own email domain to tell internal calls from external ones. If it isn't in your context, ask once and offer to save it to `COMPANY-PROFILE.md`.
3. Window: the last 7 days, ending today, unless you name another range. If you name one call, coach only that call and skip the weekly roll-up.

## Steps

### 1. Collect the calls

- **With a call recorder:** list the meetings you recorded in the window that had at least one attendee outside your domain. Page through all results. Keep each call's title, date, length, attendees, summary, action items and link.
- **Without one:** ask you to paste the transcripts or point to the files (plain text, `.vtt`, `.srt`, `.docx` exports all work). One call per file or paste block. Ask for the date and the other side's company if they aren't in the text.

If there are no calls, say so plainly and stop. Never invent a call.

Skip calls under 5 minutes (likely a no-show or a reschedule). List them in the report, don't coach them.

### 2. Classify each call

Follow `references/call-classifier.md`. For each call, answer two questions from what was said, not the calendar title:

1. Sales call or not: `sales`, `client_delivery`, `peer_or_network`, `internal` or `unclear`.
2. If sales, which type: `discovery`, `intro_inbound`, `scoping`, `demo_or_pitch`, `proposal_or_close`, `objection_or_negotiation` or `follow_up`.

Read the summary first. If it is ambiguous, read the first 3 to 5 minutes of the transcript plus any part about price or next steps. When unsure, tag `unclear` rather than guess.

Several calls with the same prospect in the window: treat them as one deal and note how it moved between calls.

### 3. Coach each sales call

Two layers on every sales call:

- **Layer A, call basics:** run every item in `references/coaching-rubric.md`. Give a one-line read with evidence for each. If an item is fine, say so in a few words, so you can see it was checked.
- **Layer B, the framework that fits:** pick one from the table in `references/frameworks.md` and state in one sentence why. If two fit, pick the simpler one. The framework is a lens, not a checklist.

Then:

- **What you did well and what to change:** at most 3 of each, each tied to a moment in the call. Write actions, not labels: "Ask what it costs them before you show the plan" not "consider better discovery".
- **Action items:** every commitment from the call, with an owner (you or the prospect) and a deadline if one was said. Start from the recorder's action items and add what the transcript shows it missed.

Coach in the second person, short and direct: "You spent 9 minutes on the plan before asking what they struggle with. Flip that next call." Quote only lines you actually have. If you don't have the exact words, describe what happened and give the time range.

Calls in another language: write the coaching in your language (ask once if unsure), and quote evidence in the original language.

### 4. Pause 1: show the review

Show in chat: number of sales calls coached, the biggest strength and the biggest pattern to fix across the window, the top 3 action items you owe with deadlines, and anything tagged `unclear`. Ask: "Any call I classified wrong, or anything to change? Shall I save the full review?" Fold in corrections. Don't save on silence.

### 5. Save the review

Default: a markdown file in your working folder, `outputs/sales-call-coach/YYYY-MM-DD-to-YYYY-MM-DD-call-review.md` (or `YYYY-MM-DD-<company>-call-coaching.md` for one call), laid out as in `references/review-template.md`.

Only if you ask for it: create a Notion page instead, using the same layout. Ask where it should live. If the page fails, save the markdown file so nothing is lost.

Single call mode can stay in chat if you prefer. Ask.

### 6. Report back

Keep the chat report under 150 words: calls coached, one strength, one pattern to fix, the top 3 action items with deadlines, the file path, and what you should correct (`unclear` calls). The detail lives in the file.

## Rules

- Never invent calls, quotes, numbers or commitments. Talk ratios from a transcript without timestamps are estimates by word count. Say so.
- Don't force a full framework on short or early calls. A 10 minute intro doesn't need a MEDDIC scorecard.
- No hedging "things to consider" block. It is an action item or it isn't there.
- Don't restate your own offer back to you, or define the frameworks. The name is enough.
- Use the prospect's first name and company in your own review. Don't copy their email addresses or phone numbers into the file.
- Read only. Never email, message or update a CRM from this skill.
- When you correct a classification, offer to add the signal to `references/call-classifier.md` for next time.
