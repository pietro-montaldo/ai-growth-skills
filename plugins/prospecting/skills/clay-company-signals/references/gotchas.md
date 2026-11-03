# Things Clay does that are easy to get wrong

Each of these cost a real build an hour or more. Check them before building.

## Segments and the watchlist

- **A segment holds only what its filter says.** A segment named "website visitors" that only filters on "best offer" also holds every other company with that offer. When a list looks bigger than expected, read its filter with `clay audiences get <id>`.
- **Keep one tag for "watched".** Don't reuse a source field (lookalike campaign, visit date) to decide who is watched. The watch field does that job, and the source fields only say where a company came from.

## Signals

- **Signals that watch segments are under Companies, Data hub, Signals** in the app, not on the sidebar Signals page.
- **A created signal is paused** until `resume`. A created signal with a typo in a fixed value, such as a seniority or a news topic, runs and finds nothing.
- **`signal.id` (`sig_...`) and the signal's own id (`td_...`) are different.** Workflow triggers want `sig_`. `clay signals get` wants `td_`.
- **Hits from before a workflow is published are never processed by it.**

## Workflows

- **Record fields need an input, not a fixed value.** To write a fixed value such as "yes", make it a trigger input or a code output.
- **A tool node can't switch from a Clay function to a Clay action.** Delete it and create a new one, then rewire the next node's inputs and edges. Deleting a node clears the inputs that pointed at it.
- **`incomingEdges` on update replaces all of a node's incoming edges.** Read them first and send the full set.
- **Code nodes:** standard library only, no network, 1 second. Test with `clay workflows code test --file <f> --inputs <json> --output-schema <flat schema>` (a few free tests a day).
- **Find contacts at company** accepts a `limit` of 1 to 10, and returns a different 10 each call. Steer it with title keywords so the 10 are likely buyers.
- **The AI pick settles for the closest match** unless told not to. Say "if nobody fits, return found = false" and give a strict order.
- **first_name is not filled from the full name.** Write it yourself.
- **Free and trial plans may allow 100 runs per workflow, ever.** Tests count. Failed runs don't.

## Campaigns

- **`clay campaigns create` makes a people-type campaign.** A workflow-fed campaign must be made in the app (New sequence, Workflow tab), and the type can't be changed.
- **The enrol step only lists live campaigns.** Launch first, then add the step.
- **A paused campaign rejects enrolments.** Don't leave the workflow live with the campaign paused.
- **`scheduleSettings` is replaced whole.** Read, change, send back.
