# Audit rubric

The 12 dimensions a skill is scored on. Each one has what good looks like, how to check it, and the line between pass, needs work and fail. These best practices combine the rules students in this repo follow with Anthropic's public skill-authoring guidance (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

When house rules exist (a `CONVENTIONS.md`, a skills section in `CLAUDE.md`, or `skill-audit-notes.md`), they win over this file where they disagree. Say so in the report.

## Contents

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
- Not scored: self-improvement habits

---

## 1. Single job

**Good:** the skill does one workflow with one kind of result. You can say what it does in one sentence without "and also".

**How to check:** look for the four signs of a skill doing too much:
- it produces two unrelated results (a report and an email campaign, say)
- the output changes shape depending on context ("if X, write a post; if Y, build a sheet")
- many "but only when" clauses that carve out special cases
- the steps drift away from the job named in the description

**Pass:** one job, none of the signs. **Needs work:** one sign, or a side task that could move into its own skill. **Fail:** two or more signs, or two clearly separate jobs. The fix is usually to split it, and say which part becomes which skill.

## 2. Length and token cost

**Good:** SKILL.md is short. The target in this repo is under about 150 lines. Anthropic's ceiling is 500 lines for the body. Every line loads on every run and competes with the conversation for space.

**How to check:** use the real line count from step 1. Then look for what makes each run heavier than it needs to be:
- detail that is only needed in some runs (templates, long lists, tool docs) sitting in SKILL.md instead of `references/`
- the same instruction said twice, in two sections
- long examples where a short one would do
- big tables or reference data inline

**Pass:** under about 150 lines and nothing obvious to cut. **Needs work:** 150 to 500 lines, or under 150 with clear cuts available. **Fail:** over 500 lines. Fixes name the exact lines to cut or move, and the estimated line count after.

## 3. Specific description

**Good:** the frontmatter `description` says what the skill does and when to use it, with phrases people actually type. It ends with "Not for X" so it stays out of nearby jobs. It is one quoted string, at most 1,024 characters, and describes the skill rather than talking as "I" ("I can help you...").

**How to check:**
- Does it say what the result is?
- Does it list at least 3 trigger phrases in quotes?
- Does it say what it is not for?
- Count the characters.
- Look for broad phrases that make it fire on the wrong requests: "use for anything related to", "if in doubt, use this skill", "whenever the user mentions marketing".

**Pass:** all of the above. **Needs work:** missing "Not for", fewer than 3 trigger phrases, or one broad phrase. **Fail:** vague ("Helps with documents"), over 1,024 characters, or empty. Fixes give the full rewritten description.

## 4. Examples

**Good:** where the quality of the result depends on style or format, the skill shows what success looks like: a short input and output pair, or a filled-in template. Examples use made-up companies and people.

**How to check:** find the examples in SKILL.md and `references/`. Are they concrete, not abstract placeholders? Do they match what the steps ask for? A simple utility (rename files, convert a CSV) may need none.

**Pass:** concrete examples where they matter, or none needed. **Needs work:** examples are vague, out of date with the steps, or only in the person's head. **Fail:** a writing or judgment skill (posts, emails, scoring) with no example at all.

## 5. Human in the loop

**Good:** the skill shows a draft before anything is written, saved, logged or changed, and waits for an answer. Pauses are numbered steps, easy to spot. Nothing is ever sent, posted, published, scheduled or connected by the skill: it drafts, the person sends. Silence is not approval.

**How to check:** list every step that writes, saves, updates a record, sends, posts or spends credits. Is there a pause before each one? Does any step say "send", "post", "publish" or "schedule" without the person doing it?

**Pass:** a pause before every write, nothing sent by the skill. **Needs work:** pauses exist but one write slips through, or a pause is buried in a paragraph. **Fail:** the skill sends, posts or publishes on its own, or writes data with no pause at all.

## 6. Progressive disclosure

**Good:** SKILL.md is the map. Detail that is only needed for some steps lives in `references/` and loads only when a step points to it. Every reference is linked directly from SKILL.md (one level deep, no file that points to another file that holds the real content). Reference files over 100 lines start with a short contents list. Scripts sit in `scripts/` and SKILL.md says whether to run them or read them.

**How to check:** for each block in SKILL.md, ask: is this needed on every run? If not, it belongs in a reference. Check that each reference is named in SKILL.md with what it holds and when to read it.

**Pass:** lean map, references linked one level deep. **Needs work:** one or two blocks that should move, a reference that points on to another reference, or a long reference with no contents list. **Fail:** everything in one big file, or references that SKILL.md never tells Claude to read.

## 7. Clear wording, no dead weight

**Good:** plain language a non-technical founder would follow. Short sentences. Rules come with a reason. The same thing has the same name throughout. Nothing explains what Claude already knows.

**How to check:** look for:
- explanations Claude doesn't need ("A PDF is a file format that...")
- shouting: CRITICAL, MUST, NEVER in capitals, many exclamation marks
- "think step by step", "double check your work", "verify your answer" with no concrete test behind it
- rules with no reason ("Never do X")
- jargon with no short explanation
- mixed terms for one thing ("lead", "prospect", "contact" for the same row)
- dates that will go stale ("before March, use the old form")
- em dashes or double dashes, if the house rules ban them

**Pass:** none, or one small slip. **Needs work:** several of the above. **Fail:** most of the skill is filler, or shouted rules contradict each other.

## 8. Valid frontmatter

**Good:** the top block is valid YAML between `---` lines with:
- `name`: lowercase letters, numbers and hyphens, at most 64 characters, matches the folder name, does not contain "anthropic" or "claude"
- `description`: as in dimension 3
- `metadata.version` set, for example `"1.0.0"`

**How to check:** read the block. Look for tabs, unclosed quotes, a colon inside an unquoted description, a name that differs from the folder.

**Pass:** all present and valid. **Needs work:** only `metadata.version` missing, or a small style issue. **Fail:** broken YAML, missing `name` or `description`, a name that breaks the rules or differs from the folder.

## 9. Files and references

**Good:** every file SKILL.md mentions exists, at the path given. No orphan files that nothing points to. No `__pycache__`, `.pyc`, `.DS_Store` or test leftovers. Paths use forward slashes.

**How to check:** list every path named in SKILL.md and in the references, then list the folder. Compare both ways: named but missing, present but never named.

**Pass:** everything matches. **Needs work:** an orphan file or a leftover. **Fail:** a file the steps depend on is missing. The fix either writes the missing file or removes the step that needs it.

## 10. Safety and privacy

**Good:** the skill can be shared publicly without leaking anything or hurting anyone's data.

**How to check** in SKILL.md, references and scripts:
- secrets: API keys, tokens, passwords, webhook URLs
- personal data: real names, emails, phone numbers, LinkedIn URLs or handles, client names, quotes or deal details
- hardcoded IDs: Notion page or database IDs, Google Sheet or Drive IDs, calendar IDs, MCP tool IDs like `mcp__1a2b3c...`
- local paths from someone's machine (`/Users/...`, `C:\Users\...`)
- prices, promo codes or course links tied to one business
- destructive commands (deleting files or records, force pushes, overwriting without a backup) with no pause
- scripts that call unknown websites or send data out

**Pass:** none found. **Needs work:** a hardcoded ID, local path or business detail that should come from the user's context instead. **Fail:** a secret, real personal data, or a destructive step with no pause. A fail here comes first in the fixes. Never repeat a found secret in the report: say where it is and that it should be removed and rotated.

## 11. Works without connectors

**Good:** every step that uses a connector (email, CRM, call recorder, Notion, a scraper) has a way to do it by hand: paste the text, upload an export, paste the link. A short "Works best with" line says which tools make it faster. Tools are named by what they do ("your call recorder"), not by a tool ID. Steps that spend credits say how many lookups or runs and ask first.

**How to check:** list each connector step. Is there a fallback? Does the skill stop dead if the connector is missing? Does any credit-spending step run without asking?

**Pass:** every connector step has a fallback, credit steps ask first. A skill with no connectors passes. **Needs work:** one step with no fallback, or no "Works best with" line. **Fail:** the skill can't run at all without a specific connector, or spends credits without asking.

## 12. Trigger collision

**Good:** the description is different enough from the person's other skills that the right one switches on. Where two skills are close, each one's "Not for" names the other.

**How to check:** compare this description with the other skills visible in the session, or the ones the person pasted. Look for shared trigger phrases and the same job described two ways. Name the other skill and the overlapping phrases.

**Pass:** no real overlap, or overlap handled with "Not for". **Needs work:** a few shared phrases with no "Not for". **Fail:** two skills that would fire on the same everyday request. **Not checked:** you couldn't see the other skills. Say so.

---

## Not scored: self-improvement habits

Two habits help skills that rely on judgment or voice (writing posts, emails, scoring leads). They add nothing to simple utilities, so mention them only when they would clearly help the skill in front of you, and never score them.

- **Update rule:** when the person says "stop doing X", the skill offers to write that into its own rules or a notes file, after they approve.
- **Saved examples:** approved outputs get saved as examples in `references/examples/`, so the next run matches what worked.
