# Emailing the buyers

Only when the user asks to switch on emailing. Until then the workflow stays in list mode.

## 1. The copy

Start from the user's own words: a cold email they sent that got replies, a template they use, or their voice skill. Keep their sentences. Only fill in the facts. No praise, no reactions, no clever lines: that reads as automated.

The shape that worked:

1. **Opener**: the signal, as a plain fact. From the "Signals: opener" field, for example "Saw your <job title> job post mentions <tool>." or "Saw you recently joined <company> as <title>." Never mention topic intent or website visits.
2. **What you do**, in one sentence in the buyer's words from the GTM messaging page.
3. **One line of credibility**, such as a rating or a number the user may share.
4. **The ask**: offer to send a short case. "If this could be useful, I can send over <proof>." The "Signals: proof" field holds the case. It can differ by company type (for example one case for agencies, another for everyone else). Use only customers who gave permission in the GTM context.
5. **Follow-up** 3 days later, as a reply in the same thread: a two-line bump that offers a short call.

Subject: short and plain, for example "<company> + <topic>".

Show 2 versions, each filled in for a real person from the buyer list, and recommend one. Wait for the user's pick.

**Spintax.** Vary 2 or 3 small phrases so every email isn't identical, for example `{{spintax:Hey|Hi}}` and `{{spintax:useful|interesting}}`. Never vary the facts or the ask. Every variant must be something the user would write.

## 2. The campaign: a workflow type, made in the Clay app

Clay campaigns come in two types, and the type can't be changed later:

- **People**: leads come from a segment. `clay campaigns create` makes this type, and it can't launch without a lead list.
- **Workflow**: leads are added by a workflow's "Enroll in campaign" step. No lead list needed.

So the user creates it in the Clay app: **Campaigns, New sequence, Workflow tab, Create workflow sequence**. Then the skill sets it up with the CLI (draft campaigns accept every edit):

- Name: "Signals · <watchlist>" (`clay campaigns update <id> --input '{"name": ...}'`).
- Copy: `clay campaigns sequence edit` with two `addStep` ops: the first as `NEW_EMAIL_THREAD` with a subject and `delayDays` 0, the follow-up as `REPLY_TO_THREAD` with `delayDays` 3. Use lead tokens `{{lead:<fieldId>|<label>}}` for first name and the "Signals" fields, and `{{sender.senderFirstName}}` for the signature. Field ids come from `clay audiences fields list --entity-type people`.
- Inboxes: the ones the user picks, from `clay campaigns options sender-accounts`, in `settings.senderAccountIds`.
- Schedule: weekdays in office hours in the buyers' main time zone. `settings.scheduleSettings` is replaced whole, so read it, change it, send it back.
- `settings.autoPauseDomainLeadsOnReply: true`, so a reply from anyone at a company pauses everyone there.
- Leave open and click tracking off.
- The goal in `claygentContext.campaignIntent`, in one sentence.

Make one change per command and read the campaign back after each. Then run `clay campaigns sequence spam-check <id> --variant-id <id>`, and fix anything it flags with the user.

## 3. Do-not-contact blocklist

If the user has the do-not-contact list, run check-do-not-contact's "make a blocklist" and ask the user to upload the file in the Clay app: **Campaigns, Blocklist**. That stops emails to blocked people and domains even though the workflow doesn't check the list. If there is no list, say plainly that nothing stops an email to a customer or an open deal, and get a clear OK.

## 4. The order for going live

1. **The user launches the campaign** in Clay. With no leads, nothing sends.
2. **Check Clay can see it:** `clay workflows actions dynamic-fields b1ab3d5d-b0db-4b30-9251-3f32d8b103c1 enroll-lead-in-sequence campaignId --type select`. The enrol step only accepts a campaign that is live and of the workflow type. If the list is empty, the campaign isn't live yet.
3. **Add the enrol step to the draft workflow**, between Save buyer and Mark company: tool node "Enroll in campaign" (`enroll-lead-in-sequence`), `campaignId` as a static value from the list above, `entityId` from Save buyer's `$.result.entityId`. Rewire Mark company to come after it. Validate.
4. **The user presses Publish** in Clay. From then on, every qualified hit is emailed.

**Keep the campaign running while the workflow is live.** A paused campaign rejects every enrolment, so each hit would spend credits on the lookups and then fail at the last step. Those failed runs can be restarted later from the failed step (`clay workflows runs rerun <id> <runId> --dry-run` first, then with the user's OK).

If an enrolment fails with `provider_result_indeterminate` or `enrollment_persistence_unavailable`, the person may already be enrolled. Never retry those: ask the user to check the campaign.

## 5. Moving people already on the list

People added in list mode are not enrolled by switching on emailing, and their companies are stamped for 90 days. If the user wants them emailed too, enrol them from the buyer list with their OK, one batch, after the campaign is live.
