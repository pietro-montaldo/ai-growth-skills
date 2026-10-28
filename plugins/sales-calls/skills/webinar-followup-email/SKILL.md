---
name: webinar-followup-email
description: "Write the follow-up emails after a webinar, workshop or live session: one version for people who attended and one for people who registered but didn't show. Delivers the recording and slides links you supply, pulls 3 to 5 key takeaways from the transcript if you have one, and adds an optional offer block built from your own offer in context, with no codes, prices or deadlines unless you give them. Saved as markdown, ready to paste into your email tool. Use for \"write the webinar follow-up\", \"post-webinar email\", \"recording and slides email\", \"email the no-shows\", \"the session ended, send the recap\". Not for a multi-email launch sequence, or a follow-up after a one-to-one sales call (use call-followup-email). Never sends or schedules."
metadata:
  version: "0.1.0"
---

# Webinar follow-up email

After a live session, two groups need different emails. Attendees want the recording, the slides and a reminder of what they learned. No-shows want to know what they missed and a reason to watch now. Both can carry one clear next step toward your offer, if you want one. This skill writes both, in your voice, and saves them for you to send from your own email tool.

Works best with: your call recorder or webinar platform (for the transcript). Without one, paste the transcript, your slide notes, or a few bullet points of what you covered.

## Reference files

- `references/email-templates.md`: the attendee and no-show layouts, the offer block, and a made-up example. Read it before step 3.

## Before starting

1. Read your context, using the first that exists:
   - GTM context from the GTM Context Kit: `gtm-hub.md` means Notion (fetch the pages it links), `gtm/README.md` means the repo (read the pages it links). Your offer and messaging feed the offer block.
   - A company profile file such as `COMPANY-PROFILE.md` or `about-me.md`.
   - Otherwise you'll be asked in step 1 for the offer, if you want one.
2. Voice: use your `<name>-voice` skill if installed. Otherwise ask for 3 to 5 emails or posts you wrote and match them. Never ship someone else's voice.

## Steps

### 1. Pause 1: collect the inputs

Ask in one batch:

- **Session:** the exact title, the date, and the session page link if there is one. If you give a link, open it to confirm the exact title.
- **Links:** the recording link and the slides link. Any other resources promised during the session (a template, a checklist, a doc).
- **Versions:** attendees, no-shows, or both. If your platform separates them, use its lists; otherwise you choose.
- **Transcript:** from your call recorder or webinar platform, pasted, or none. With none, ask for 3 to 5 bullets of what you covered.
- **Offer block:** yes or no. If yes: which offer (default: the one in your context that fits the session topic), its link, and any incentive you want to mention, with its real terms and deadline. If you give none, the block has no incentive.
- **Sign-off:** how you sign, and an optional link on your name.

If a link is missing, ask for it. Never put a placeholder in the final email.

### 2. Pull the takeaways

From the transcript (or your bullets), pick 3 to 5 takeaways a busy reader can act on. One line each, concrete, in the words used on the session where possible. Also note the best audience question and its answer, if there was one: it often makes the strongest line in the no-show email.

Don't invent anything that wasn't said.

### 3. Draft both versions

Follow `references/email-templates.md`.

- **Attendees:** thanks for joining, the resources up top, the takeaways, the optional offer block, a reply invitation, sign-off.
- **No-shows:** no guilt, a one-line hook on what they missed, the recording up top, the takeaways framed as what's inside, the optional offer block, sign-off. Never pretend they attended.

Subject lines under 60 characters where possible. Give 2 options per version. Body 120 to 220 words each.

### 4. Pause 2: review

Show both emails in full in chat, with the subject options. Ask for edits. Apply them. Don't save on silence.

### 5. Save

Save each version to your working folder (or `outputs/`) as `YYYY-MM-DD-<3-word-slug>-attendees.md` and `YYYY-MM-DD-<3-word-slug>-no-shows.md`, where the date is the session date. Each file has the audience, the subject options and the body, ready to paste into your email tool.

If you want them in your email tool as drafts and a connector can do that, create drafts only, after a yes. Never send or schedule.

## Rules

- No invented links, prices, discount codes, ratings, review counts, attendance numbers or deadlines. Only what you supply or what is in your context.
- Incentives use real terms only. A deadline appears only if it is real. No fake scarcity.
- One clear call to action per offer. At most two offers, and only if you ask for two.
- No em dashes or double dashes. No emojis unless your voice uses them.
- Bold only for key info (the resource labels, an incentive). Minimal formatting otherwise.
- The no-show email never implies they were there.
- Nothing is sent, posted or scheduled by this skill.
