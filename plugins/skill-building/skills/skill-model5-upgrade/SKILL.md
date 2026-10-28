---
name: skill-model5-upgrade
description: "Rewrites a skill made for older Claude models so it works well on Claude 5 models. Checks it against a 12-point list, proposes numbered changes you accept or reject one by one, builds the upgraded file and offers a blind A/B test before you install it. Use for \"upgrade my skill for Claude 5\", \"update this skill for the new model\", \"is this skill still good on Opus 5.5\", \"my skill got worse after the model update\", \"check this skill for Claude 5\". Not for a full quality audit of a skill (use skill-auditor) or for writing a new skill from scratch."
metadata:
  version: "1.0.0"
---

# Skill model 5 upgrade

Claude 5 models work like an experienced colleague. They plan a whole task, check their own work, and keep going until it is done. Many skills were written for older models, which needed more hand holding: rules in capital letters, step by step orders, "double check your answer". On Claude 5 those habits make results worse and use more of your usage allowance. This skill finds those habits in one skill and rewrites them, with your approval for every change.

The person using this skill is usually not technical. They built a skill by chatting with Claude or downloaded one, and they want it to keep working well. Talk to them the way you would explain it to a smart colleague from marketing or finance: plain words, short sentences, no jargon. When a technical word is unavoidable (like "subagent"), explain it in one short phrase the first time.

## What done looks like

The person ends up with:
1. A short, plain language summary: how many changes you suggest and the two or three that matter most.
2. A numbered list of changes, each with the old text, the new text and one sentence on why. They can accept or reject each one.
3. The upgraded skill as a file they can install, with only the changes they accepted, plus short steps to replace the old version.
4. If they want it, a blind A/B test result showing the new version does at least as well as the old one before they install it.

Keep the original skill name so it replaces the old one instead of creating a duplicate.

## Steps

**1. Get the skill.** Ask the person to share it. Any of these works:
- the skill file (.zip or .skill)
- just the SKILL.md file
- the text of the skill pasted into the chat
- in Claude Code, the path to the skill folder

If they don't know where to find it: in the Claude apps, open **Customize, then Skills**, open the skill, and copy its instructions into the chat. In Claude Code, skills live in a `.claude/skills/` folder in the project or in your home folder, or inside an installed plugin. Read every file you receive, including any extra files inside the skill folder, so your suggestions fit the whole skill.

**2. Ask at most two quick questions, only if the answer isn't clear from the skill:**
- What does the skill do for you, in one sentence? (This tells you which rules are there for a real reason.)
- Which Claude model do you usually use? If they don't know, assume Opus 5.5 and say so.

**3. Check the skill against the list below.** Quote the exact words from the skill for every issue you find.

**4. Pause: show the results.** Start with the plain summary, then the numbered list, grouped by type of issue. Some old style rules still earn their place, for example exact steps for an invoice, a legal form or anything that can't be undone. Mark those as "keep" and say why in one sentence, so the person knows you looked at them.

**5. Wait for their choice.** They might say "all of them", "all but 3 and 7", or ask a question. Change nothing until they decide.

**6. Build the upgraded skill.** Apply only the accepted changes. Keep the original name in the file's top section (the frontmatter). Package it the same way it came in: a .zip with the skill folder inside if they gave you a .zip or .skill file, an updated folder if they gave you a folder, otherwise a SKILL.md file. Give the file a clear name, for example the skill name plus "-upgraded".

**7. Pause: offer an A/B test before they install it.** Explain it simply: we give the same requests to the old and the new version and a neutral judge compares the answers without knowing which is which, like a blind taste test. Recommend it for skills that handle money, clients or anything published. Skip it for a small skill if they prefer.

How to run it:
- **Pick 3 test requests with the person.** One everyday request, one that touches a part you changed, and one with a detail missing, to see if the skill asks the right question. Use realistic but made up details (for example a fake client) so nothing real is created.
- **In Cowork or Claude Code, use subagents.** Start one helper per request and version, all at the same time (3 requests means 6 helpers). Each helper gets only one skill version, one request and its own test folder. Tell each helper: the user is not available, so if the skill says to ask something, stop and write the question down. Also tell it never to send, publish, pay or delete anything, and to use test values for any website it can't reach.
- **Compare the files.** If the skill creates documents, compare the old and new files yourself. Identical files are good news: the upgrade didn't break anything.
- **Blind judge.** Relabel the answers A and B in random order and keep a note of which is which. Start one more helper as the judge. It sees only the requests and the A and B answers, and picks a winner per request with one sentence of reason. Then reveal which was old and which was new.
- **In the Claude apps without subagents,** run the requests one at a time with each version and let the person compare.

Show the result as a small table: request, winner, reason. Be honest about the size: 3 requests run once each shows problems and clear wins, not small differences. If the new version loses on a request, find which change caused it and offer to undo or adjust that change before installing.

**8. Tell them how to install it.**
- **In the Claude apps:** go to **Customize, then Skills**. Remove or switch off the old version first, so Claude doesn't have two skills with the same name. Then click **+**, choose to upload a skill and select the new file. Menu names change from time to time, so if something looks different, look for the Skills section in Customize or Settings.
- **In Claude Code:** if the skill is your own, replace the old folder in `.claude/skills/` (in the project or your home folder) with the new one. Claude Code picks up the change without a restart.
- **If the skill came from a plugin:** don't edit the installed copy, because the next plugin update overwrites it. Send the changes to the plugin's owner, or save the upgraded version as your own skill under a new name and switch the plugin skill off. Plugins install with `/plugin install <plugin>@<marketplace>` in Claude Code, or from Customize in the Claude apps.

## What to check

Each point says what to look for, what to do, and why. Use the "why" when you explain the change to the person.

1. **Shouting.** Words in capitals like CRITICAL, IMPORTANT, MUST, NEVER, ALWAYS, or lots of exclamation marks. Rewrite in normal case and add the reason. Why: Claude 5 gives shouted rules too much weight and follows them even when they don't fit.

2. **Rules without a reason.** "Never do X" or "avoid Y" with no explanation. Rewrite as what to do plus why. Example: "Never include a point without a source" becomes "Back every point with a source, so every claim can be proven." Why: with the reason, Claude handles situations the rule never mentioned.

3. **"Double check your work."** Lines like "verify your output", "review before answering", "use a second agent to check the result". Remove them. Why: Claude 5 already checks its own work. Asking again adds a second round that costs usage without better results. Keep a check only when it is a concrete test outside Claude's head, like "make sure the totals match the bank statement".

4. **"Think step by step."** Also "explain your reasoning" or "think carefully before answering". Remove. Why: newer models decide on their own how much to think, and asking them to write out their reasoning can even get the request declined.

5. **Too many orders.** Long numbered lists telling Claude exactly what to do for work it can plan itself. Rewrite as four short parts: the job, who it's for and why, the rules to respect, and what the finished result looks like. Keep exact steps where order really matters: payments, legal documents, publishing, deleting, sending. Why: Claude 5 was trained to plan whole tasks, and micromanaging makes the result worse.

6. **No finish line.** Nothing says when the task is complete or what the result should look like. Add it: length, format, number of items, where the file should go. Why: Claude 5 tends to do too much, not too little. Without a finish line it keeps going.

7. **No guidance on style.** If people read the result and the skill says nothing about length or tone, add one or two lines on it. If the skill has examples of good output, keep them. Why: some Claude 5 models write long and use jargon by default. Examples are still one of the best ways to show the style you want.

8. **Helpers used for everything.** (This is about the skill being upgraded. The A/B test in step 7 is a good use of helpers: independent, parallel pieces.) If the skill tells Claude to use subagents (helper copies of Claude that work in parallel), add a limit: only for big jobs that split into independent pieces, like researching 20 companies. Not for small tasks or for checking its own work. Why: Claude 5 is quick to call helpers, which multiplies usage.

9. **Forced progress reports.** "Summarize after each step", "announce what you'll do next", "ask if I want you to continue". Remove, unless the person uses Fable (see below). Why: Opus 5.5 gives short updates on its own, and these instructions can make it stop halfway.

10. **Too broad a description.** The description at the top decides when the skill switches on. Phrases like "use for anything related to" or "if in doubt, use this skill" make it switch on for the wrong requests. Keep specific phrases people would actually say. Remove the broad ones. Why: newer models follow the description more readily.

11. **Doing more than asked.** If the skill can send, publish, delete or buy something, add: do what was asked and stop before anything beyond it. Why: Claude 5 sometimes adds steps nobody requested.

12. **Things that did not change.** These basics still apply, so flag them if they're missing: one job per skill, a clear description, the main file kept short (under about 500 lines) with extra detail in separate files, and testing the skill before trusting it.

## Differences between models

- **Opus 5:** writes long, checks its own work, calls helpers readily, sometimes does more than asked. Points 3, 6, 7, 8 and 11 matter most.
- **Opus 5.5:** always thinks before answering, finishes with less effort, and tends to end with a summary. Points 4 and 9 matter most.
- **Fable 5:** the opposite on updates and formatting. It gives fewer progress updates and uses less formatting. Don't remove requests for progress updates or structure. Do remove lines asking it to keep updates short.
- **Sonnet 5:** use the general points above.

Anthropic releases new models often. If the person uses a model not listed here (for example a newer Sonnet, Haiku or Fable version), say that this checklist may be partly out of date for it. The table at the top of Anthropic's "Prompting best practices" page links to a prompting page for each current model.

## If they ask where this comes from

Point them to Anthropic's own pages:
- Prompting Claude Opus 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Prompting Claude Opus 5.5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Skill writing best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

## Rules

- Short sentences and everyday words, as if explaining to a colleague who has never written code. Lead with what you recommend. One sentence of reason per change. Use commas or periods instead of dashes.
- If you're not sure a change is right, say so and let the person decide.
- Change nothing in the skill until the person accepts it, and never install, upload or publish anything for them.
