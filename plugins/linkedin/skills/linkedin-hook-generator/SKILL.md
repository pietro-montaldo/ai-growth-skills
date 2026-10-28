---
name: linkedin-hook-generator
description: "Write scroll-stopping LinkedIn hooks (the lines before \"see more\") in your own voice. Finds the one thing the reader gets from your post, writes 10 hooks with different formulas and exact character counts, then 3 variations of the one you pick. Use for \"write me hooks\", \"hook ideas for this post\", \"opening line for LinkedIn\", \"how should I start this post\", \"LinkedIn post about [topic]\", or when you share a topic or a draft and need a strong opening. Not for reviewing a full draft (use linkedin-post-reviewer) or writing the whole post from a call (use session-to-linkedin-post)."
metadata:
  version: "0.1.0"
---

# LinkedIn hook generator

The hook is the first 1 or 2 lines of a post, before LinkedIn cuts it off with "see more". If the hook doesn't stop the scroll, nothing else in the post gets read. This skill finds the real value of your post first, then writes hooks around it, in the way you actually write.

## Reference files

- `references/formula-library.md`: the two-line structure, 11 hook formulas with example hooks, the output format and edge cases. Read it before Step 3.
- `scripts/count_chars.py`: exact character counts for each hook. Call it by its full path in this skill's folder.

## Before starting

1. **Audience.** Read your GTM context to know who the posts are for. If the project has `gtm-hub.md`, fetch the ICP and Messaging pages it links. If it has `gtm/README.md`, read `gtm/icp.md` and `gtm/messaging.md`. Otherwise read `COMPANY-PROFILE.md` or `about-me.md` if one exists. If none exist, ask once: "Who are your posts for, in one sentence?" Offer to save the answer to `COMPANY-PROFILE.md`.
2. **Voice.** If you have a `<name>-voice` skill installed, use it. Otherwise ask for your 5 best LinkedIn posts (paste the text, or point to a `linkedin-weekly-review` report). From them, note:
   - Sentence length and rhythm (full sentences or short bursts).
   - Person: "I built" or "we built".
   - How numbers are written ("450 marketers" or "hundreds of marketers").
   - Contractions ("Here is" or "Here's"), caps, emojis, arrows.
   - Phrases you repeat, and how you name your audience.
   - The shape of your best hooks: one line or two, claim or question.

   If you don't have 5 posts yet, use what you have and say the voice match will be lighter.

## Steps

### 1. Intake

Ask three things, in a natural way, not like a form:

1. **What is the post about?** Topic, tool, result or opinion. If you already said it, confirm it back in one sentence.
2. **Do you have a draft?** Ask to paste it. Drafts hold numbers, angles and phrasing worth keeping.
3. **Any direction for the hook?** A mood, an angle, a hook you liked before. Optional.

Don't ask what you already know. If there's enough context, say what you have and move on.

### 2. Find the primary value

Before writing any hook, answer: **what is the one thing the reader gets from this post?**

The primary value is not the topic. The topic is "client onboarding". The primary value is "the 6-step onboarding checklist that cut a 20-person agency's first-month churn in half, free to copy".

Think through:
- What outcome, asset or insight does the reader walk away with?
- Is there a number that makes it concrete?
- What is the tension? (expensive vs free, old way vs new way, hype vs reality)
- Who exactly benefits? Use the audience from your context.

State the primary value in one sentence. If it isn't clear, ask: "What is the one thing the reader walks away with?" Don't guess.

### 3. Write 10 hooks

Write exactly 10 hooks using the two-line structure and the formulas in `references/formula-library.md`. Each hook:
- Leads with the primary value.
- Uses a different formula, labelled in brackets.
- Sounds like your 5 best posts, not like the examples in the formula library.
- Uses only true facts and numbers from you. Put `[number]` where a number would help but you haven't given one.
- Has a one-line note on why it works.

Then run the character count script on all 10:

```bash
python3 <this skill's folder>/scripts/count_chars.py "hook 1" "hook 2" ...
```

Fix any hook the script tags WARNING or REJECT before showing them. If the script can't run, use `python3 -c "print(len('hook text'))"` for each one. Never estimate.

Mark the strongest with a star and put it first. Show them in the output format from the formula library.

### 4. Pause: pick and refine

Ask: **"Which one do you like most? I'll write 3 variations of it."**

When you pick, write 3 variations:
- **A:** shorter and tighter.
- **B:** more energy or stronger emotion.
- **C:** a different specific detail or angle.

Same labels, same counts (run the script again), same one-line notes. Repeat if you want to keep going. Stop when you're happy.

## Rules

- Your voice comes from your voice skill or your own posts. Never copy the tone of the examples in this skill.
- Never invent results, numbers, quotes or names. Use placeholders and flag them.
- No hashtags in hooks. No emojis unless your own posts use them, and then at most one (for example a single 👇 at the end).
- No corporate or copywriter phrases unless they appear in your own posts: "I'm excited to share", "In today's landscape", "Here's the thing", "game-changer", "Let's dive in".
- Keep your natural register. If you write informally, or English is not your first language, don't polish your phrasing into corporate English. Fix clear typos only.
- Match the formula to the content: no Giveaway hook on an opinion post, no Callout on a tutorial.
- Shorter is almost always better. A 90-character hook that lands beats a 200-character one that barely fits.
- This skill writes hooks. It never posts anything.
