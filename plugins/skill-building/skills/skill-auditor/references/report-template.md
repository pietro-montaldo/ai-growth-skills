# Report template

Use this layout for the audit report. Keep it to what the person needs to decide. Lead with the verdict, no preamble. A worked example follows the template.

## Contents

- Layout
- Rules for the report
- After fixes are applied
- Worked example

## Layout

```markdown
# Audit: <skill-name>

**Verdict:** <Ready to use | Good, a few fixes | Needs work before you rely on it | Needs a rewrite>. <One sentence on why.>
**Size:** SKILL.md is <real number> lines, plus <n> reference files and <n> scripts.
**House rules used:** <file name, or "none found">

## Top 3 things to fix
1. <Most important issue, in plain words, with the fix number>
2. ...
3. ...

## Scorecard

| # | Dimension | Status | Reason |
|---|---|---|---|
| 1 | Single job | pass / needs work / fail | <one line, quoting or pointing to the skill> |
| 2 | Length and token cost | | |
| 3 | Specific description | | |
| 4 | Examples | | |
| 5 | Human in the loop | | |
| 6 | Progressive disclosure | | |
| 7 | Clear wording, no dead weight | | |
| 8 | Valid frontmatter | | |
| 9 | Files and references | | |
| 10 | Safety and privacy | | |
| 11 | Works without connectors | | |
| 12 | Trigger collision | | |

## Proposed fixes

Each fix stands alone. Accept or reject each one.

**Fix 1. <Short title>** (dimension <#>)
Why: <one sentence>
Before:
> <exact current text, or "missing">
After:
> <exact new text>

**Fix 2. ...**

## Optional upgrade (not scored)
<Only if a self-improvement habit would clearly help. Otherwise leave this section out.>

## What next
Reply with the fixes to apply: "all", "all but 3", "only 1 and 2", or ask about any of them. Nothing changes until you answer.
```

## Rules for the report

- Use the real line count, not an estimate.
- Every reason points to something in the skill: a quote, a line number or a file name.
- Order fixes by impact: safety and privacy fails first, then anything that breaks the skill, then the rest.
- For moves into `references/`, say which lines move, the new file name, and the line count after.
- Don't repeat a secret or personal detail in the report. Say where it is.
- Keep reasons to one line and "Why" to one sentence.

## After fixes are applied

```markdown
## Changes applied
Applied: fixes <list>. Skipped: <list>.
Line count: <before> to <after>.

| # | Dimension | Before | After |
|---|---|---|---|
| <only the dimensions the edits touched> | | | |

<One line on anything that got worse, with an offer to undo it. Otherwise: "Nothing got worse.">
```

## Worked example

A made-up skill, `acme-weekly-report`, that turns a CRM export into a weekly sales summary.

```markdown
# Audit: acme-weekly-report

**Verdict:** Good, a few fixes. It does one job well, but it emails the report on its own and the description is too broad.
**Size:** SKILL.md is 212 lines, plus 1 reference file and no scripts.
**House rules used:** none found

## Top 3 things to fix
1. It sends the report by email without showing it first (fix 1).
2. The description fires on any request about "sales" (fix 2).
3. The 70-line chart guide sits in SKILL.md but is only needed for monthly reports (fix 3).

## Scorecard

| # | Dimension | Status | Reason |
|---|---|---|---|
| 1 | Single job | pass | One job: CRM export in, weekly summary out. |
| 2 | Length and token cost | needs work | 212 lines; the chart guide (lines 120 to 190) loads every time. |
| 3 | Specific description | needs work | "Use whenever the user mentions sales" is broad; no "Not for". |
| 4 | Examples | pass | `references/sample-report.md` shows a full filled-in report. |
| 5 | Human in the loop | fail | Step 6: "Email the report to the team." No pause. |
| 6 | Progressive disclosure | needs work | Chart guide should be a reference. |
| 7 | Clear wording, no dead weight | needs work | "ALWAYS round to 2 decimals" has no reason; lines 30 to 38 explain what a CRM is. |
| 8 | Valid frontmatter | needs work | `metadata.version` missing. |
| 9 | Files and references | pass | The one reference exists and is linked. |
| 10 | Safety and privacy | pass | No IDs, names or secrets. |
| 11 | Works without connectors | pass | Accepts a CSV upload when the CRM isn't connected. |
| 12 | Trigger collision | needs work | Shares "sales summary" with your `pipeline-review` skill. |

## Proposed fixes

**Fix 1. Show the report before anyone gets it** (dimension 5)
Why: a wrong number in a team email can't be taken back.
Before:
> 6. Email the report to the team.
After:
> 6. Pause: show the report and wait for approval. Then draft the email for you to send. Never send it yourself.

**Fix 2. Narrow the description** (dimensions 3 and 12)
Why: it switches on for any sales question, including ones your pipeline-review skill should handle.
Before:
> description: "Weekly sales report. Use whenever the user mentions sales."
After:
> description: "Turn a CRM export into a one-page weekly sales summary with wins, losses and next week's focus. Use for \"weekly sales report\", \"summarise this week's deals\", \"sales recap for the team\". Not for reviewing individual deals (use pipeline-review)."

**Fix 3. Move the chart guide into a reference** (dimensions 2 and 6)
Why: it is only needed for monthly reports, but loads every week.
Before:
> Lines 120 to 190: "## Charts ..."
After:
> One line in step 4: "For monthly reports, read `references/charts.md`." The new file holds lines 120 to 190. SKILL.md drops to about 142 lines.

**Fix 4. Give the rounding rule a reason, cut the CRM explainer** (dimension 7)
Why: with the reason, Claude rounds correctly in cases the rule doesn't name.
Before:
> ALWAYS round to 2 decimals.
After:
> Round money to 2 decimals so totals match the finance sheet.
> (And delete lines 30 to 38.)

**Fix 5. Add a version** (dimension 8)
Why: a version number lets you tell which copy is installed.
Before:
> missing
After:
> metadata:
>   version: "1.0.0"

## What next
Reply with the fixes to apply: "all", "all but 3", "only 1 and 2", or ask about any of them. Nothing changes until you answer.
```
