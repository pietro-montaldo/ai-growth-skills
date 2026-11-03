# The buyer workflow

One Clay workflow, run once per signal hit. If the Clay plugin's `workflows`, `workflows-claygent` and `workflows-campaign-enrollment` skills are installed, read them before building: they hold the exact input shapes. Run each command's `--help` before first use. Build it as a draft and never publish from the CLI.

Name: "Signals: find buyer (<watchlist>)".

## The steps

```
Signal triggers → 1 Read → 2 90-day check → 3 Qualify → 4 Job post or new hire?
   job post → 5 Find signers → 6 Pick buyer → found?
   new hire → the hired person
→ 7 Chosen person → 8 Work email → found? → 9 Email lines → 10 Save buyer → [11 Enrol] → 12 Mark company
```

Every "stop" is a rules conditional with `endRunOnNoMatch: true` and no fallback edge.

**Triggers.** One `audience_signal` trigger per signal, `entityType: "ACCOUNT"`, bound to the signal's `signal.id` (`sig_...`), not its `td_...` id. Clay accepted several signal triggers sharing one trigger node (pass `workflowNodeId`). Triggers stay off until the workflow is published.

**What a hit carries.** `$.fields.*` is the company's Audiences record by display name (`$.fields.Domain`, `$.fields['Company name']`, `$.fields.Industry`, `$.fields.id` for the record id, and any custom fields such as the watch field). `$.signal.signalType` and `$.signal.data` hold the event. A JobPost event's `data.jobPostData` has the title, URL, company, location and posted date, but **not the job description**. The shape of NewHire and News events can differ by workspace: `assets/read_signal.py` reads them defensively. Check the first real one and adjust.

1. **Read** (code node, `assets/read_signal.py`). Outputs a flat record: signal type, job title and URL, the hired person's name, title and LinkedIn URL, the company's id, name, domain and LinkedIn URL, the source (from the source fields you name), and whether the company was added in the last 90 days.
2. **90-day check** (rules). Continue only if the company was not added in the last 90 days and the domain is not empty. It comes first so nothing is spent on companies that would be skipped anyway.
3. **Qualify** (agent node, `assets/qualify_prompt.md`, outputs `qualified` and `reason`). For a job post it opens the posting URL to read the description, or searches the web for it if the page needs a login.
4. **Job post or new hire?** (rules on signal type).
5. **Find signers** (tool node, Clay's "Find contacts at company", `cpj-find-lists-of-people-v2`). Map the company domain, set `job_title_seniority_levels_v2` to the signing levels (for example `founder, owner, partner, c-suite, vp, director, head`), `job_title_keywords` to the buyer roles from the ICP card, and `limit` to 10 (the most it accepts). Avoid keywords that also match other roles, such as "President", which matches sales Vice Presidents. Clay's managed "Find People at Company" function returns a random handful of staff, so it is the wrong tool here.
6. **Pick buyer** (agent node, `assets/pick_buyer_prompt.md`, outputs `found`, `full_name`, `title`, `linkedin_url`, `reason`). Feed it the whole result of step 5.
7. **Chosen person** (code node). The picked buyer, or the hired person on the new-hire path. Merge nodes may be switched off in a workspace; a small code node does the same job.
8. **Work email** (tool node, Clay's managed "Work Email" function). Map full name, company name, domain, company LinkedIn and person LinkedIn. Then a rules node: stop if the email is empty.
9. **Email lines** (code node, `assets/email_lines.py`). Splits first and last name, and writes the opener and proof line the copy uses.
10. **Save buyer** (tool node, `upsert-audiences-record`, CONTACT). Look up by email and LinkedIn URL. Write `first_name`, `last_name`, `name`, `title`, `email`, `linkedin_url`, and people fields you create first: "Signals: signal", "Signals: detail", "Signals: source", "Signals: opener", "Signals: proof", "Signals: company". Link the company with `associations|accountId` = the company id. **Set first_name explicitly**: Clay does not fill it from the full name, and the campaign needs it.
11. **Enrol** (only in step 7 of SKILL.md, see `campaign.md`).
12. **Mark company** (tool node, `upsert-audiences-record`, ACCOUNT, looked up by domain): today's date in a company field "Signals: last added". It runs after the save, and after the enrol step once that exists, so a company is only stamped when someone was really added.

Then create a people segment, "Signals buyers · <watchlist>", filtered on "Signals: opener" not empty. That is the buyer list.

Group the nodes on the canvas (see the Clay `workflows` skill, `node-groups.md`). Run `clay workflows graph validate`.

## Testing

Test once before the user publishes, and quote the cost first: a full job-post run was about 3 data credits and 5 action credits when this was written. Each test uses one workflow run.

- Build the test input from a real hit (`clay audiences signals get ...`) or a sample: `{"fields": {...the company record by display name...}, "signal": {"signalType": "JobPost", "data": {...}}}`.
- Before a full test, disconnect step 12 (set its `incomingEdges` to `[]`), so the test doesn't stamp a real company for 90 days. Reconnect it after. Save the edges first.
- `clay workflows runs test <id> --inputs <file>`, then `runs get <runId> --wait 300` and `runs get <runId> --verbose` to read every step.
- To retest one step cheaply: `clay workflows nodes test <id> <nodeId> --source-run <runId>`. If it needs inputs from a branch the source run didn't take, use `--inputs` instead.

Show the user, step by step, what happened and who was picked. If the pick is not someone who can sign, fix the lookup keywords or the pick order and retest. Expect one or two rounds.

## Going live in list mode

Give the user the workflow link and ask them to press Publish in Clay. Then check: `clay workflows versions list <id>` shows a version, and `clay workflows triggers get <triggerId>` shows a `snapshotId` that is no longer `latest`. Hits from before publishing are not processed later.
