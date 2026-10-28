---
name: newsletter-writer
description: "Write one newsletter edition in your own voice from material you already have: posts, guides, templates, videos, events and your offer. Asks whether the edition teaches one idea in depth or rounds up several resources, and whether it promotes something or only teaches, then returns a full markdown draft with 5 subject lines and a preview line, and pauses before the final polish. Works for Substack, Beehiiv, Kit, LinkedIn newsletters and similar. Use for \"write a newsletter\", \"new edition\", \"draft this week's newsletter\", \"turn these posts into a newsletter\", \"write edition 12\", or when you hand over a list of resources to include. Not for launch emails or email sequences, cold outreach, or LinkedIn posts."
metadata:
  version: "0.1.0"
---

# Newsletter Writer

You bring the raw material for one edition: a post you wrote, a guide or template, a video, an event, maybe your offer. This skill turns it into a scannable edition that teaches first, sends readers to one main link, and sounds like you, not like AI. It drafts. You paste it into your platform and send it yourself.

Works best with: Notion or Google Docs (to read your guides), a browser (to check event pages), your newsletter platform's archive (for past editions). Every step also works by pasting text into the chat.

## Reference files

- `references/inputs-checklist.md`: what to collect before drafting, and how to ask for it in one batch.
- `references/edition-types.md`: teaching and roundup editions, their skeletons, and a guide to each section.
- `references/teaching-not-selling.md`: tone rules, sentence shapes to avoid, how to turn a post or guide into a section, and where an offer goes.
- `references/subject-lines.md`: subject line approaches, preview line rules, and the output format.
- `references/platform-formatting.md`: formatting markers and how to apply them in Substack, Beehiiv, Kit and LinkedIn newsletters.

## Before starting

1. **Read your context**, using the first of these that exists:
   1. GTM context. A `gtm-hub.md` file means it lives in Notion: fetch the Product & offer, ICP and Messaging pages it links. A `gtm/README.md` file means it lives in the repo: read `gtm/product.md`, `gtm/icp.md` and `gtm/messaging.md`.
   2. A company profile file, such as `COMPANY-PROFILE.md` or `about-me.md`.
   3. Neither: ask once, in one batch: what you sell and the link people use to buy or book, who reads the newsletter, and the newsletter's name and platform. Offer to save the answers to `COMPANY-PROFILE.md` so the next skill doesn't ask again.

   From it, keep: who reads, what you sell, your main offer and its link, words your buyers use, and words to avoid.
2. **Find your voice.** If a `<name>-voice` skill is installed, use it. Otherwise ask for 3 to 5 things you wrote. Two or three past editions are best, because they also show your structure, labels and sign-off. Note how you open, how long your sentences are, how you sign off, and whether you number editions. Never fall back on a generic voice or someone else's.
3. **Know your platform.** Substack, Beehiiv, Kit, LinkedIn newsletter or other. It changes how the preview line works and how formatting is applied (`platform-formatting.md`).

## Steps

### 1. Collect the raw material

Read everything you hand over. Fetch links when a connector or browser can open them. If one can't, ask you to paste the text. For each event, get the real date, time and time zone from its page.

Pick the strongest item as the main piece: the one most readers will want. Map the rest to sections using `edition-types.md`.

### 2. Pause: choices and missing inputs

Ask in one message:
- **Edition type.** Teaching (the email explains one idea, the link holds the full version) or roundup (a short index of several resources, each teased with a link). Recommend one based on the material: one deep resource suits teaching, several lighter ones suit a roundup.
- **Promote or only teach.** "Does this edition promote something, like your offer, a call or an event, or does it only teach?" If it promotes, confirm which offer from your context, its link, and any real deadline. Don't invent urgency.
- **Everything still missing** from `inputs-checklist.md`, as one short list.

Don't draft with placeholders. Wait for the answers.

### 3. Draft the edition

Follow the skeleton for the chosen type in `edition-types.md` and the tone in `teaching-not-selling.md`. In short:
- No warm-up sentence. Open with the edition number or title, then a short list of what's inside.
- One main link carries the edition. Build interest before the button: the story or reason it matters, then 3 to 5 highlights, then the link. Don't dump the full contents of the resource into the email.
- Rewrite posts, don't paste them. Cut about half, drop the hooks and hype, keep the facts and results.
- If the edition promotes, add one offer block where `teaching-not-selling.md` says. If it only teaches, leave the offer out.
- "Next time" lists only topics you gave. Never invent them.
- Close with your own sign-off from your samples. If you have none, invite replies.
- Mark headings, buttons, images and dividers with the markers in `platform-formatting.md`.

### 4. Write subject lines and a preview line

Write 5 subject lines, each from a different approach in `subject-lines.md`, with a one-line note on why it could work. Recommend one. Then write one preview line that pairs with the recommended subject and adds new information instead of repeating it.

### 5. Pause: show the draft

Show it in the output format from `subject-lines.md`: subject lines, preview line, then the full draft in markdown. Below it, list anything you assumed in one line each. Ask:
- "Which subject line, or should I mix two?"
- "Is the main link the one you want most readers to click?"
- "Anything to cut, add or say differently?"

Apply the edits. Don't polish on silence.

### 6. Final polish

Run the checks at the end of `teaching-not-selling.md`: voice against your samples, structure, one main link, no hype shapes, no em dashes or double dashes, every date and link filled in. If you changed the subject line, rewrite the preview line to match. Format for your platform and hand back the paste-ready version.

Offer to save it to `outputs/newsletter-<date>.md` in your working folder. Save only if you say yes.

## Rules

- Never publish, schedule or send anything, and never connect to the newsletter platform to post. You paste and send.
- No placeholders in the final draft. Missing inputs are asked for, not guessed.
- One main link per edition. If you can't say which link carries the edition, it isn't ready.
- Teach, don't sell. At most one offer block, and only when you said this edition promotes something.
- Never invent numbers, results, quotes, dates, guest credentials or "next time" topics. Use only what you or your context gave.
- Name a reader, customer or guest only as you gave it, and quote a customer only if you say it's shareable.
- No em dashes or double dashes in the draft, subject lines or preview line.
- The email stays shorter than the resource it points to.
