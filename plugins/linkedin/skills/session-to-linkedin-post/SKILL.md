---
name: session-to-linkedin-post
description: "Turn one of your live sessions, webinars, workshops or calls into a LinkedIn post. Reads the transcript, checks what has worked on your LinkedIn before, proposes post ideas, then hooks, then 3 full drafts in your voice, with your pick at every step. Use for \"turn this webinar into a post\", \"post ideas from this call\", \"what should I post from my session\", \"read this transcript and give me LinkedIn ideas\", or when you share a transcript and want content. Not for reviewing a draft you already wrote (use linkedin-post-reviewer) or writing hooks only (use linkedin-hook-generator)."
metadata:
  version: "0.1.0"
---

# Session to LinkedIn post

Live sessions are full of opinions, setups and numbers your audience never sees in your posts. This skill mines one session for post ideas, grounds them in what has actually worked on your LinkedIn, and takes one idea all the way to a ready-to-paste draft.

It runs in 4 checkpoints. You choose at each one, because you know which angle you want and which numbers are true. Never skip ahead to drafting before you pick.

**Works best with:** a call recorder connector (Fathom, Granola, Zoom, Gong or similar) and a `linkedin-weekly-review` report. Neither is required: you can paste the transcript and your top posts.

## Reference files

- `references/reading-the-numbers.md`: how to read past post performance, and what to do with little or no data.
- `references/ideas-and-drafts.md`: how to pull ideas from a transcript, hook patterns, the 3 draft angles and output formats.

## Before starting

1. **Audience and offer.** If the project has `gtm-hub.md`, fetch the Product, ICP and Messaging pages it links. If it has `gtm/README.md`, read `gtm/product.md`, `gtm/icp.md` and `gtm/messaging.md`. Otherwise read `COMPANY-PROFILE.md` or `about-me.md`. If none exist, ask once: "Who are your posts for, and what do you sell, in one sentence each?" Offer to save the answers to `COMPANY-PROFILE.md`.
2. **Voice.** If you have a `<name>-voice` skill installed, use it in Step 4. Otherwise ask for 3 to 5 posts you wrote and liked, and match them.

## Steps

### 1. Gather the two sources

Get both at the same time.

**The transcript.** Use the first that works:
- A connected call recorder: search for the session by a few keywords from its title and a recent date, then read the transcript.
- A transcript file in the working folder (`.txt`, `.vtt`, `.docx`, `.pdf`).
- Paste it into the chat.

If several recordings match, list them with date and title and ask which one.

**Past post performance.** Use the first that exists:
- `linkedin-weekly-review` data files in `outputs/` (`*-linkedin-weekly-review.csv`). Read all of them, newest capture per post.
- A LinkedIn analytics export in the working folder (Analytics, then Export).
- Paste your 5 to 10 best posts with their impressions and saves, if you know them.
- Nothing at all: say the ideas will be grounded in the transcript and your voice only, and continue.

### 2. Checkpoint 1: propose ideas

Follow `references/reading-the-numbers.md` for what resonated, and `references/ideas-and-drafts.md` for what to pull from the transcript.

Give about 8 ideas. For each one:
- A working hook line.
- One or two sentences on the angle.
- Why it should work, tied to a specific past post and metric when you have data, or to your audience's pain when you don't.

Flag overlap with posts you already published. End with your top 3 and ask you to pick.

Keep what the data shows separate from what you infer. Any number you said loosely in the session ("I don't know, maybe a thousand") is flagged for you to check.

### 3. Checkpoint 2: hook options

For the idea you pick, write about 6 hooks. Each borrows a pattern from one of your own high-performing posts. Name the model post and its key metric next to each hook, so you can see why it is there. With no data, use the patterns in `references/ideas-and-drafts.md` and say so.

Only use a quote hook if someone really said it to you. Recommend one hook and a backup, then ask you to pick. For more hook options, offer the `linkedin-hook-generator` skill.

### 4. Checkpoint 3: three post versions

Write 3 text-only versions with the chosen hook, each a different angle (see `references/ideas-and-drafts.md`). Use your voice skill or your sample posts.

After the drafts, say in one line which version you'd pick and why, and list what you must check before posting: numbers, placeholders like `[link]`, and any claim taken from the session.

### 5. Checkpoint 4: hand it over

When you pick a version, give it back as clean copy-paste text in one block, exactly as approved, with nothing around it that you'd need to delete.

If you use a drafts tool like AuthoredUp and it's connected, offer to save it there as a draft. Only on a yes. Don't set a profile, schedule or reminder unless asked.

Confirm in one or two lines: where the text is, that nothing was posted or scheduled, and the numbers you still need to check.

## Rules

- You pick at every checkpoint. Don't write on silence.
- Never invent facts, results, numbers or quotes. Use placeholders like `[number]` or `[link]` and flag them.
- Never name prospects, clients, attendees or students from the session. Use roles ("a founder in the session asked...").
- Ignore the session's sales pitch and logistics. Mine the ideas.
- No em dashes or double dashes in drafts, unless your own posts use them.
- Nothing is ever posted, published or scheduled by this skill.
- If you say a line doesn't sound like you, fix the draft. If you have a voice skill, offer to add the correction to it.
