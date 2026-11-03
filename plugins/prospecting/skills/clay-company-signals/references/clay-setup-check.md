# Clay setup check

Run these before step 1. They only read. Stop and tell the user plainly at the first one that fails.

## 1. The Clay CLI is signed in

```bash
clay whoami
```

It prints the user and the workspace. Say the workspace name back and ask if it is the right one: signals, segments and campaigns are created there.

- `clay: command not found`: the CLI is not installed. If the Clay plugin's `setup` skill is available, run it. Otherwise point the user to Clay's CLI docs and stop.
- An auth error: run the `setup` skill or `clay login`.

**Without the CLI:** the user can do every step in the Clay app. The reference files say where each thing lives in the app. It is slower, and the skill becomes a guide that writes the prompts, code and copy for them to paste.

## 2. The features this needs

```bash
clay signals list
clay audiences list --entity-type companies
clay workflows list
clay campaigns list
clay campaigns options sender-accounts
```

- `signals list` failing with an auth error (exit 3) means Signals is not on the plan or not enabled. The system can't run without it.
- `campaigns list` failing means Campaigns (Clay's sequencer) is not available. List mode still works: the buyers are saved, and the user can export them to another sending tool later.
- `sender-accounts` with no active inbox: list mode works, emailing doesn't until an inbox is connected in Clay (Campaigns, Email accounts).

Note what already exists. If there are signals or segments with similar names, ask before creating new ones: two signals watching the same companies are charged twice.

## 3. Credits

```bash
clay credits balance
```

Say the balance in one line. The costs come later, in each step, with a yes before spending.

## 4. Search room

The lookalike list uses Clay Search. Every `run` result shows `periodQuota` (limit, used, remaining). If a pull would leave under 15% of the limit, say so and ask. If Search returns `quota_exceeded`, stop the pull and tell the user: the plan's search cap is reached. Never create extra searches to get around a cap.

## 5. Run allowance on free and trial plans

On some plans each workflow can run 100 times in its lifetime. Adding companies with the watchlist workflow and every signal hit each use a run. If the user is on such a plan, say so when sizing the list in step 1.
