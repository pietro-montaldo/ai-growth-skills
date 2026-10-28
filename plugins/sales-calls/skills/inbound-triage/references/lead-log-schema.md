# Lead log schema

Use this when you have no CRM, or when you want a simple log in your working folder. One row per person. Same columns for CSV and markdown.

## Columns

| Column | What goes in it |
|---|---|
| Name | The person's name as they gave it. Company name only when no person is known. |
| Company | Company or brand |
| Email | Their work email, if they gave it |
| LinkedIn | Clean profile URL, if known |
| Channel | Where they first came from: Email, LinkedIn, Booking, Form, Referral, Other |
| Offer | Which of your offers this is about (your categories from setup) |
| Stage | Lead, In conversation, Call booked, Proposal sent, Negotiation, Waiting, Won, Lost |
| Interest | High, Medium, Low |
| Value | Deal value as they said it, with currency. Empty if unknown. |
| First contact | ISO date, YYYY-MM-DD |
| Last contact | ISO date of the latest message either way |
| Latest communication | One or two lines: who wrote last and what about |
| Next step | One line, with a date when there is one |
| Notes | Lasting facts (team size, budget timing, who decides). Keep what is already there. |

## CSV

File: `leads.csv` in your working folder. First line is the header row, exactly:

```
Name,Company,Email,LinkedIn,Channel,Offer,Stage,Interest,Value,First contact,Last contact,Latest communication,Next step,Notes
```

Rules:

- Quote any field that contains a comma, quote mark or line break, and double any quote mark inside it.
- To find a lead, search by email, then LinkedIn, then name, then company. Read only the matching rows.
- Update the existing row instead of adding a duplicate.
- Show the exact new or changed rows before writing.

## Markdown

File: `leads.md` in your working folder. One table with the same columns. Easier to read, harder to keep tidy past about 50 leads. Suggest moving to CSV or a CRM when it grows past that.

## CRM

If your CRM is connected, use it instead. Fetch its fields and stage options first and map the columns above to them. Don't create new fields or stages in someone's CRM without asking. Common mapping: Name and Email go on the contact, Company on the company, Stage, Value and Next step on the deal, Latest communication as a note.

## Privacy

This file holds personal details of real people. Keep it out of any public repo or shared folder. If the working folder is a git repo, offer to add `leads.csv` and `leads.md` to `.gitignore`.
