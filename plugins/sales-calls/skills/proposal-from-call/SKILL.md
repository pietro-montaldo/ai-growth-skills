---
name: proposal-from-call
description: "Turn a discovery or scoping call into a services proposal (consulting, agency, training, implementation or any done-for-you work) plus the email that delivers it, each step gated on your approval. Reads the full call for scope, outcomes, budget signals and every number said out loud, writes a working structure doc you correct first, builds a short proposal with a ladder of options (usually 3) and checks the ladder reads as fair value, then drafts the delivery email. Prices and packages come from your context or from you, never invented. Output is markdown or HTML, PDF optional. Use for \"build the proposal\", \"turn this call into a proposal\", \"proposal for Acme\", \"price this project\", \"draft the proposal email\". Not for invoices, cold outreach, or the simple post-call recap (use call-followup-email). Never sends."
metadata:
  version: "0.1.0"
---

# Proposal from call

One sales call becomes a proposal package, each piece approved by you before the next: a working structure doc, the proposal (3 to 5 pages), an optional detailed scope held back until the client picks an option, and the delivery email as a draft. The know-how is in reading the call properly and pricing honestly. The layout is the easy part.

Works best with: your call recorder (Fathom, Granola, Gong or similar) and your email. Without them, paste the transcript and you get the email text to paste.

## Reference files

- `references/call-extraction.md`: what to pull from the transcript. Read it before step 2.
- `references/proposal-structure.md`: page by page structure, style rules, option patterns. Read it before step 4.
- `references/pricing-ladder.md`: the ladder check, spoken numbers, currency. Read it before step 3.
- `references/delivery-email.md`: the delivery email. Read it before step 6.
- `assets/proposal-template.html`: a print-ready HTML layout for the proposal.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: `gtm-hub.md` means Notion (fetch the pages it links), `gtm/README.md` means the repo (read the pages it links). You need your offer, packages, price ranges, proof and objections.
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise ask once (in step 1's batch) for what you sell, your packages and your price ranges. Offer to save them to `COMPANY-PROFILE.md`.
2. Voice: use your `<name>-voice` skill if installed. Otherwise ask for 3 to 5 emails or proposals you wrote and match them.
3. Brand: use your colours, fonts and logo if they are in your context. Otherwise ask whether to pull them from your website, or use the template's neutral default. Never use a client's brand.
4. If past proposals or proposal emails sit in your working folder, read the most recent one or two and match their structure and density.

## Steps

### 1. Pause 1: one question batch

Ask everything at once, before drafting:

- **Delivery mode:** remote, in person, or not decided. If not decided, write "Remote as standard, in person possible". Never assume.
- **Ladder shape:** how many options (3 is the default) and on which axes, for example how much scope (core vs full) and how tailored (standard vs customised).
- **Price anchors:** your list prices or day rate, and any number already said on the call. Spoken numbers are binding. You set the rest.
- **Add-ons:** any optional extras, with price and whether to include them.
- **Limits to print:** participant cap, hours, revisions, timeline.
- **Proof:** which client names, results or testimonials are cleared to print. Never assume a name said on a call is cleared.
- **Exclusions:** anything to leave out.
- **Format and currency:** markdown, HTML or PDF; main currency and any second currency.

### 2. Pull the call and extract

Use the full transcript, never just the summary. Without a recorder, ask you to paste it. Follow `references/call-extraction.md`: who the champion and the approver are and when they decide, scope, outcomes in their words, every number and promise said aloud, budget signals, constraints, objections, what was declined.

### 3. Pause 2: the working structure doc

Write `YYYY-MM-DD-<client>-proposal-structure.md` in your working folder: what the proposal has to achieve, the client picture with time-stamped quotes, the option set, the pricing table with the ladder check from `references/pricing-ladder.md`, and open items. Proposed in-between prices are marked as proposals.

Show the key points and ask you to correct the numbers and options. Build nothing until you do. Log every later correction at the bottom of this doc.

### 4. Pause 3: draft the proposal

Follow `references/proposal-structure.md`. Write it in markdown first (or straight into `assets/proposal-template.html` if you chose HTML or PDF). If the work needs a detailed scope (session plan, project plan, deliverables list), build it as a separate document, saved but not sent until the client picks an option.

Show the full draft and wait for approval. Apply edits. Don't move on on silence.

### 5. Render

- **Markdown:** save `YYYY-MM-DD-<client>-proposal.md`.
- **HTML:** fill the template, save `YYYY-MM-DD-<client>-proposal.html`.
- **PDF (optional):** print the HTML to PDF from a browser, or use a PDF tool if one is installed (headless Chrome or WeasyPrint). Look at every rendered page as an image: fix footer overlaps, orphaned boxes and half-empty pages before you share it.

### 6. Pause 4: the delivery email

After the proposal is approved, draft the email from `references/delivery-email.md`. Show it in full and wait for approval. Then, with an email connector, create a draft in the existing thread with the client. Without one, give the text to paste. Tell you which file to attach (the proposal only, not the held-back scope). Most email connectors can't attach files, so say so plainly.

### 7. Check and archive

- Recheck every sum against the final prices and every headcount or quantity from the call.
- Search all outputs for em dashes, double dashes, leftover placeholders, uncleared client names, and any mention of the held-back scope document.
- Save the final email as `YYYY-MM-DD-<client>-proposal-email.md`, so the next run can match it.

## Rules

- Never send. Drafts only.
- Never invent a price, package, client name, result or rating. They come from your context or from you.
- Every number said on the call either matches the proposal exactly or gets one explicit line in the email explaining the change. Never silently.
- Client names, logos and results in print only when you cleared them.
- No legal, compliance or security claims from memory. If the client raised one, link the official source in the email and say it isn't legal advice.
- Don't promise deliverables (files, templates, handovers) you didn't confirm.
- Name the client's people by role in the proposal, not by name, unless you want names in it.
