# From one seed company to a lookalike list

Clay's own search guide is the authority on query syntax. If the Clay plugin's `searches` skill is installed, follow it. Otherwise save the reference and read it in parts:

```bash
clay searches query-mode reference | jq -r '.reference' > outputs/clay-search-reference.md
```

## 1. Read the seed company

Ask for the seed's website. Pull just that one company to see how Clay describes it:

```bash
clay searches query-mode create --query 'select from companies where clay.include_company_identifiers(("acme.com"))'
clay searches query-mode run <searchId> --limit 1
```

Note its industry, size bucket, headquarters country and description. Say back in two lines what makes it a good customer, using the GTM context (why it bought, what it bought). That is what the lookalikes must share.

## 2. Draft the search

Combine the seed and the ICP card. Show the user the filters in plain words before running anything:

| Filter | Where it comes from |
|---|---|
| `industry in (...)` | The seed's industry plus 1 to 3 close ones the ICP card names |
| `company_size in (...)` | The ICP card's headcount range, as Clay's size buckets |
| `locations.any(is_headquarters = true and ...)` | The ICP card's geography. If geography is only a preference, start with the preferred regions |
| `products_and_services is_similar_to (...)` | 2 or 3 short phrases for what the seed sells, in the buyer's words |
| `people.exists(...)` (optional) | A buyer title the ICP card requires, such as a founder or a Head of L&D |
| `clay.exclude_company_identifiers((...))` | Customers, open deals, competitors, do-not-contact companies (step 4 below) |

Use `industry` for verticals, not description keywords. Keep it to what the ICP actually requires: every extra filter shrinks the list.

**Careful with "uses our category" filters**, for example "an employee mentions the tool you train on". They tend to return companies that build or sell that tool, not companies that buy help with it. Prefer the ICP's firmographics, and let the signals find the buying moment.

## 3. Sample, then adjust

Create the search and pull 10. Show them as a short table: name, website, industry, size, country, one line on fit. Ask what's off. Typical fixes: too many of the user's competitors (exclude their industry or add a `not products_and_services is_similar_to`), too big or small (size buckets), wrong country.

Repeat until the user says the sample looks right. Each sample pull counts against the search quota.

## 4. Exclusions

Collect the domains that must never be on the list:

- **Customers** from the GTM context. A company client blocks its whole domain. A person who bought on their own blocks only themselves, not their employer.
- **Open and recent deals** in the CRM, if the user has one: anyone at a stage past first contact, plus lost deals.
- **Competitors** from the GTM context.
- **Do-not-contact**: if the user has the list, run check-do-not-contact on the final CSV instead (step 6).

Put company domains into one `clay.exclude_company_identifiers((...))` call (up to 1,000). Rows with a company name but no domain are matched by name after the pull.

## 5. Pull the list

About half of the search results survive a fit check. To end with N companies, pull about N × 1.5. Pull in pages of up to 50 (`run <searchId> --limit 50`, repeat while `hasMore`). Watch `periodQuota` after each page.

## 6. Fit check and save

Go through every company and drop clear misfits against the ICP card's disqualifiers: competitors, companies that sell what the user sells, subsidiaries of big groups when the ICP wants founder-led firms, nonprofits or schools when the ICP is commercial, and so on. Keep borderline ones and flag them.

Save `outputs/<YYYY-MM-DD>-signals-watchlist.csv` with columns: `domain, company_name, linkedin_url, industry, size, country, why_fit, source`. Use `lookalike: <seed name>` as the source.

If the do-not-contact list exists, run check-do-not-contact on the CSV and keep only its keep file.

Show: how many were pulled, dropped (with reasons) and kept, and the top 10. Wait for an OK before step 3.

## Without the CLI

In the Clay app: Find leads, Companies. Set the same filters by hand, export the results as CSV, and give the file to the skill for the fit check.
