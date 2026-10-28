---
name: skill-auditor
description: "Audit one Claude skill against these best practices on 12 dimensions: single job, length and token cost, a specific description, examples, human-in-the-loop pauses, progressive disclosure into references, clear wording, valid frontmatter, files that exist, safety and privacy, fallbacks when a connector is missing, and trigger collisions with your other skills. Returns a verdict, a scorecard and numbered fixes you accept or reject one by one. Use for \"audit this skill\", \"review my skill\", \"check my skill\", \"score this skill\", \"is this skill any good\", \"is this SKILL.md too long\", \"why is this skill expensive\", \"why does this skill trigger at the wrong time\". Not for auditing a whole folder of skills at once, for upgrading a skill to a newer model (use skill-model5-upgrade), or for writing a new skill from scratch."
metadata:
  version: "1.0.0"
---

# Skill auditor

Audits one skill you point to and tells you, in plain words, what is good, what needs work and how to fix it. You get a verdict, a scorecard on 12 dimensions and a numbered list of fixes. Nothing in your skill changes until you accept a fix. You decide, item by item.

## Reference files

- `references/audit-rubric.md`: the 12 dimensions. For each one: what good looks like, how to check it, and when it is pass, needs work or fail. Read it before scoring. Don't score from the summary in this file alone.
- `references/report-template.md`: the layout of the report, with a worked example. Read it before writing the report.

## Before starting

1. **Get the skill.** One skill per run. Any of these works:
   - in Claude Code or Cowork, the path to the skill folder or its SKILL.md
   - an uploaded .zip or .skill file
   - the text of SKILL.md pasted into the chat (then ask for any files in `references/` or `scripts/` too, or note that you couldn't see them)

   If they point at a folder with many skills, ask which one. If they don't know where the skill is: in the Claude apps it is under **Customize, then Skills**; in Claude Code it is in a `.claude/skills/` folder in the project or the home folder, or inside an installed plugin.
2. **Ask at most one question, only if it isn't clear from the skill:** "What does this skill do for you, in one sentence?" This tells you which rules are there for a real reason.
3. **Look for house rules.** If the project has its own rules for skills (a `CONVENTIONS.md`, a `CLAUDE.md` section on skills, or a `skill-audit-notes.md` from an earlier audit), read them and apply them on top of the rubric. Say which file you used.

## Steps

### 1. Read the whole skill

Read SKILL.md end to end. Then list the skill folder and read every file in `references/`, `scripts/` and any other subfolder. You audit the whole skill, not only SKILL.md. Count the lines of SKILL.md (`wc -l` when you have file access, otherwise count the pasted text) and write down the real number.

### 2. Score the 12 dimensions

Read `references/audit-rubric.md` and score each dimension: **pass**, **needs work** or **fail**, with a one-line reason that quotes or points to something in the skill. The 12 dimensions:

1. Single job
2. Length and token cost
3. Specific description
4. Examples
5. Human in the loop
6. Progressive disclosure
7. Clear wording, no dead weight
8. Valid frontmatter
9. Files and references
10. Safety and privacy
11. Works without connectors
12. Trigger collision

For trigger collision, compare the description with the other skills you can see in this session. If you can't see them, ask the person to paste the names and descriptions of skills that do similar work, or mark the dimension as "not checked".

Then check, without scoring, whether the skill would gain from a self-improvement habit (see the end of the rubric). Mention it only when it would clearly help.

### 3. Write the fixes

For every needs work or fail, write at least one fix as a numbered item. Each item stands alone, so the person can accept it without the others. Show the exact before and after text when the fix is a text change. Put the fixes that matter most first.

### 4. Pause: show the report

Write the report using `references/report-template.md`. Lead with the verdict. End by asking which fixes to apply: "all", "all but 3 and 7", "only 1, 2 and 5", or a question.

Change nothing until they answer. Don't apply fixes on silence.

### 5. Apply the accepted fixes

Apply only the accepted items.
- **With file access:** edit the skill files. If the skill sits inside an installed plugin, say first that the next plugin update will overwrite the change, and offer to save an edited copy as the person's own skill instead.
- **Without file access:** give back the full updated SKILL.md (and any changed reference file) as files to download, packaged the way they came in.

Then count the lines again and re-score only the dimensions the edits touched. Show a short before and after: line count, and the status of each touched dimension. If an edit made something worse, say so and offer to undo it.

### 6. Pause: tell them how to install it

Only if you produced a new file. In the Claude apps: **Customize, then Skills**, switch off or remove the old version, then upload the new file. In Claude Code: replace the folder in `.claude/skills/`. For a plugin skill: update it through the plugin (`/plugin install <plugin>@<marketplace>` in Claude Code) or send the fixes to its owner.

## Rules

- One skill per run. Never scan a whole folder of skills.
- Every status has a reason tied to something you saw in the skill. Every needs work or fail has at least one fix.
- The audit is against these best practices and any house rules you found, not your own taste. If a rule in the skill breaks a best practice for a good reason (exact steps for an invoice or a legal form, for example), mark it pass and say why.
- Never run the skill's scripts, and never send, post or connect anything while auditing. You read and propose.
- When the person says a check is wrong, too strict or missing, offer to note it in `skill-audit-notes.md` in their working folder, so the next audit reads it in "Before starting". Write it only after they say yes.
- Plain words, short sentences. Explain a technical word in a few words the first time you use it. No em dashes or double dashes.
