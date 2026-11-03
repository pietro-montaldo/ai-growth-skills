# The watchlist

One company field decides who is watched. One segment shows every watched company in one place. One small workflow adds companies, now and later. Keeping the watch tag separate from where a company came from (lookalike, website visitor, CRM) means you can always add or remove a company without touching anything else.

Show the user this list and wait for a yes before creating anything.

## 1. The watch field

```bash
clay audiences fields list --entity-type companies
clay audiences fields create --entity-type companies --name "Signals: watch"
```

Reuse the field if it already exists. Its value is a short watchlist name, such as `team-training` or `agencies`. One field can then hold several watchlists, each with its own value.

## 2. The segment

Create a company segment named "Signals watchlist · <short offer name>" whose filter is: Signals: watch equals `<value>`. Read `clay audiences create --help` for the filter shape, and copy the `dataPath` pattern from an existing segment (`clay audiences get <id>`).

If the user already has a live segment that should always be watched (for example website visitors that fit the ICP), add it with an `Or` group, so new members join on their own. Ask first.

## 3. The add-to-watchlist workflow

Create a workflow named "Signals: add to watchlist" with:

- **A manual trigger** whose inputs are `domain` (required), `company_name` and `watch` (required).
- **One tool node**, "Add company to watchlist": the Audiences action "Create or update Audiences record" (`upsert-audiences-record`), entity type ACCOUNT, looked up by domain. It writes `domain`, `org_name` from `company_name`, and the watch field from `watch`.

Record fields must be mapped from an input, not typed in as a fixed value: Clay's check rejects a fixed value there. That is why `watch` is a trigger input.

Validate it with `clay workflows graph validate`. It does not need publishing: manual test runs use the draft.

## 4. Add the companies

Test one company first and read it back:

```bash
echo '{"domain":"acme.com","company_name":"Acme","watch":"team-training"}' | clay workflows runs test <workflowId> --inputs -
clay workflows runs get <runId> --wait 60
```

Then check the company record shows the watch value. After that, add the rest of the CSV, one run per company, and wait for each run. For more than about 100 companies, use a CSV upload trigger instead (see the Clay `workflows` skill, `csv-triggers.md`).

Finish with `clay audiences records search-count --audience-id <segmentId> --entity-type companies` and compare it with the CSV. Clay's index lags a few seconds: if it is short, wait and count again before looking for who is missing.

New companies are created with only a domain and a name. Clay fills in the rest over time. Signals only need the domain.

## Adding and removing later

- **Add:** the user says "add acme.com to my signals watchlist". Run the workflow for each domain.
- **Remove:** clear the company's watch field in the Clay app (Companies, open the company). Sending an empty `watch` through the workflow may not clear it, because the save step skips empty values.
- **See it:** Companies, Segments, the watchlist segment. Suggested columns: watch, industry, size, the source fields, and "Signals: last added" once the workflow exists.

## Without the CLI

Create the field and the segment in the Clay app (Companies, Data hub, Fields, then Segments). Import the CSV into Companies with the watch column mapped to the field.
