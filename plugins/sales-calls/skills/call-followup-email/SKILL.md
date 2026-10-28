---
name: call-followup-email
description: "Turn a sales call into a follow-up email with three fixed sections (What we discussed, As promised, Next steps split into your side and theirs), written with you, in your voice, and left as a draft threaded into your existing email with the prospect. Asks what to add before writing, asks for the real links and files you promised, checks nothing was already sent, flags what was unclear on the call, and can log your tasks to your task tool or a markdown list. Works from your call recorder or a pasted transcript. Use for \"follow up on my call with Dana\", \"draft the follow-up for the Acme call\", \"post-call email\", \"send a recap\", \"what did I promise on that call\". Not for webinar follow-ups (use webinar-followup-email), proposals (use proposal-from-call), or cold outreach. Never sends."
metadata:
  version: "0.1.0"
---

# Call follow-up email

One call becomes one follow-up email, and optionally a short task list. Every prospect gets the same recognisable recap, so you never rebuild the structure from scratch. You co-write it: the skill drafts from the call, you add what the recording missed, and you send it yourself.

Works best with: your call recorder (Fathom, Granola, Gong, Fireflies or similar) and your email (Gmail, Outlook). Without them, paste the transcript or your notes and you get the email text to paste.

## Reference files

- `references/email-structure.md`: the three sections, voice rules and a worked example. Read it before step 4.
- `references/task-logging.md`: how to turn commitments into tasks. Read it before step 7.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: `gtm-hub.md` means Notion (fetch the pages it links), `gtm/README.md` means the repo (read the pages it links).
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise ask once, in one batch: your name as you sign emails, what you sell, and your email domain (so your colleagues are never treated as recipients). Offer to save the answers to `COMPANY-PROFILE.md`.
2. Voice: use your `<name>-voice` skill if one is installed. Otherwise ask for 3 to 5 emails you wrote and match them. Never write in someone else's voice.

## Steps

### 1. Find the call

- **With a call recorder:** if you named a person, company or date, search for it. Otherwise list your calls from the last 7 days and ask which one if more than one fits. Names are often misspelled in requests: if a search misses, try one spelling variant, then scan recent titles and attendees.
- **Without one:** ask you to paste the transcript or your notes, plus who was on the call and their email addresses.

If several calls with the same person fit, ask which one. A call under about 5 minutes is likely a no-show: flag it and confirm before drafting. If nothing is found, say so and offer to widen the window. Never draft from memory.

Keep the call date, the link (if any) and the external attendees' addresses.

### 2. Pull the content

Read the summary, then the transcript. The summary misses the details that matter for a follow-up: exact commitments, deadlines, numbers, who does what. Look for anything you said you would send, prepare, share or schedule, and anything they said they would decide or do.

### 3. Pause 1: anything to add?

Before writing, share a one or two line gist of what you found and ask:

> Here's what I pulled from the call: [gist]. Is there anything else you said or agreed that should go in, or anything to leave out? Paste it and I'll fold it in.

Wait for the answer. Weave what you add into the right section, don't tack it on at the end. If you say there's nothing, carry on.

### 4. Draft the email

Follow `references/email-structure.md`: one opener line, then **What we discussed**, **As promised**, **Next steps** (on my side, on your side), then a short sign-off in your voice.

**As promised** means only the deliverables you committed to send: links, files, a proposal, a recording, a document. Advice and topics go in the first section. The call usually shows that something was promised but not the thing itself, so ask for the real links, codes or files. Never leave a placeholder like `[LINK]` in a draft. If nothing was promised, drop the section.

Language: the language the call was held in, unless your context or you say otherwise.

### 5. Pause 2: approve the draft

Show in chat:

1. Recipients (all external attendees by default, never your own colleagues), subject and full body.
2. The assets still missing for As promised.
3. An honesty block, two to four lines: what is certain from the call, and what is unclear (garbled passages, numbers said loosely, names not confirmed).

Fold in your edits. Don't move on until you approve. Don't proceed on silence.

### 6. Thread it into your email

With an email connector:

1. Search for past threads with the external attendees.
2. Read the latest thread and check nothing in the draft was already sent (for example, a link you sent right after the call). If something was, tell you and offer to trim it.
3. If a thread exists, create the draft as a reply to its latest message, with `Re:` on the subject. If not, create a new draft to the attendees. Use plain addresses, and give both plain text and HTML (bold headers, bullet lists).

Without one: give the subject and body ready to paste.

### 7. Optional: log your tasks

Ask: "Want me to log the tasks from this call?" If yes, follow `references/task-logging.md`. It goes to the task tool you use (Notion, Asana, ClickUp, Todoist, Trello, Linear or similar), or to `outputs/call-tasks.md` in your working folder. Show the task list first and create it only after you say yes.

### 8. Close out

Say where the draft is (threaded reply or new draft, or the text above), list the tasks logged and where, and give the call link. Say clearly that nothing was sent.

## Rules

- Never send. Drafts only. Never say "sent".
- Never invent commitments, dates, prices, names or company details that weren't on the call or in what you added. A fuzzy next step is written as a proposal ("I'll send it by Friday, does that work?").
- If one side has no next steps, keep the line honest: "Nothing pending from your side for now."
- Don't address your own colleagues by default. Show the recipient list when there's more than one.
- If the draft can't be created, show the full subject and body in chat so nothing is lost.
- If you say the call is an internal exercise, ignore past emails with the contact and skip the draft unless you ask.
