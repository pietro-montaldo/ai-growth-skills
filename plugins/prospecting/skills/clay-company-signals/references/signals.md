# Signals

If the Clay plugin's `signals` skill is installed, follow it for the mechanics. `clay signals create --help` is the authority on each type's settings and on the exact allowed values (seniority, news topics, schedules). Never guess a value: a misspelt one matches nothing and the signal looks broken.

## From ICP triggers to signal types

Read the ICP card's buying triggers and map each one:

| A trigger like | Clay signal type | Watches |
|---|---|---|
| "they are hiring for X", "the job post mentions the tool", "a team is being built" | `JobPost` | companies |
| "a new Head of X just joined", "new leader in the buyer role" | `NewHire` | companies |
| "just raised", "new leader announced", "launched a new initiative", "acquired" | `News` (topics such as Fundraising, Executive Appointment, New Initiatives and Programs) | companies |
| "they are researching our category" | `CompanyTopicIntent` | companies |
| "our champion changed jobs" | `JobChange` | people, not this watchlist |

Pick the 2 or 3 strongest. Name them for the user in plain words, for example "a job post at a watched company mentions <tool>" or "a watched company hires a Head of <function>".

**Topic intent** tells you a company is researching a topic. Use it to rank or alert, not as the opening line of an email: "I saw you were researching X" reads as creepy. It is also turned on separately in Clay, so `create` can fail with an auth error on plans where other signals work.

## Settings

All signals here watch the watchlist segment: `"entityType": "ACCOUNT", "segmentIds": ["<watchlist segment id>"]`. Never put a segment's name where its id goes.

- **JobPost:** `filters` with `"startFrom": "ClayTableOfCompanies"` (required), and `job_description_keywords` or `job_title_keywords` from the trigger, plus `max_num_days_since_posted` (30 is a good default) and `limit_per_company` (3).
- **NewHire:** `filters` with `"start_from_method": "query"`, `job_title_keywords` for the buyer roles, `job_title_seniority_levels_v2` (for example `c-suite, vp, director, head`), `current_role_max_months_since_start_date` (3). `lookBackTimeWindowInMonths` sets a one-time look back on the first run (3 is a good default).
- **News:** `filters.topics` from the fixed list in `create --help`, and `autoAdvanceEarliestPublishDate: true` so each run reads only new articles.
- **CompanyTopicIntent:** topic ids come from `clay signals search-topics --query "<plain words>" --entity-type company`. Never copy ids from another signal.

Name each signal "Signals: <what it watches> (<watchlist>)". Schedule: weekly is a good start.

## Cost, before creating anything

Two ways Clay charges:

- **Per company checked**, on every run, whether or not anything happened: JobPost, NewHire, topic intent (times each topic). Cost per month is about companies × runs per month × the per-check price.
- **Per result**: News. Cost depends on how many articles come back, so a tight topic list is the cost lever.

There is no CLI command that prices a signal. Use the price Clay shows: after creating a signal (paused), open Companies, Data hub, Signals, and read its "Credit spend" and per-run cost. When this skill was written, Clay showed about 0.2 credits per company per run for JobPost and NewHire. So for two weekly signals:

| Companies | Credits a month, about |
|---|---|
| 100 | 170 |
| 250 | 430 |
| 500 | 860 |

Treat these as a rough guide. Read the real number in Data hub and say it before resuming.

## Create, read back, resume

1. `clay signals list` first. If a signal of the same type already watches the same companies, reuse it instead.
2. `clay signals create --type <T> --name "<name>" --schedule weekly --input <file>`. It is created **paused**.
3. `clay signals get <id>` and check `input.audiences.segmentIds` and `signal.inputs.filters` are what you meant. Note `signal.id` (`sig_...`): the workflow trigger needs it.
4. Show the settings and the cost. Only after a clear yes: `clay signals resume <id>`.

`update --input` replaces each key you send whole. To change filters, read the current ones with `get`, edit, and send the whole object back.

## Where to see them

In the Clay app: **Companies, Data hub, Signals**. Signals that watch segments are listed there, with cadence, segments, credit spend and hits. The sidebar Signals page may show only table-based signals, such as website visitors.

Hits are saved on each company, not in a table. Read them with `clay audiences signals get --segment-id <id> --since <date> --signal-types JobPost,NewHire`. Hits can take a while to show up there after a run.

## What to expect

Signals only see changes after they start. NewHire looks back once, on the first run. A new watchlist mostly pays off in the weeks after setup.
