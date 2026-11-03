# Pick buyer prompt (agent node "Pick buyer")

Fill the `<...>` parts from the user's ICP card: who signs, in the order the user would want to email them. Show it to the user, then paste it as the node's `agentPrompt`. Inputs: `company_name`, `domain`, `icp_card`, `job_title`, `people` (the whole result of "Find signers"). Outputs: `found` (boolean), `full_name`, `title`, `linkedin_url`, `reason`.

Test it twice: once with the real list, and once with the top group removed, to check it falls back to the next group and not to the closest match.

```text
Pick ONE person at {{company_name}} ({{domain}}) who can SIGN a deal for <the offer>. Use only the people in the list below. Do not search the web and do not invent anyone.

Company ICP card: {{icp_card}}
Why we are reaching out: {{job_title}}

People found at the company:
{{people}}

Who counts as a signer, in this order of preference (pick from the highest group that has someone):
1. <for example: Founder, Co-founder, CEO, Managing Partner, Managing Director, Owner. Any founder counts.>
2. <the leader of the function the offer serves, for example: Chief People Officer, VP of HR, Head of L&D, Head of Enablement>
3. <the next best, for example: COO, VP or Head of Operations>
4. <optional fourth group>
Never pick <the leaders who don't buy this, for example: finance, sales, engineering, product, customer success>, unless they are also a founder. If nobody fits the groups above, return found = false.
The ICP card is a hint only: the order above applies to every company.

Hard rules:
- The title must be at Director level or higher (Founder, Owner, C-suite, Partner, VP, Head of, Director). A "Lead", "Manager", "Specialist", "Senior", "Associate" or any individual contributor title is NOT a signer, even if their work is close to the offer.
- The person must currently work at {{company_name}}; skip anyone whose title shows a past role or another employer.
- Never pick a freelancer, advisor, board member, reseller or partner, a recruiter, or an intern.
- When several people fit the same group, pick the most senior.
- If nobody in the list is a signer, return found = false and leave the person fields empty. Ending with nobody is the correct outcome when the list has no signer: do not settle for the closest match.

Return found, full_name, title, linkedin_url (the person's LinkedIn profile URL, linkedin.com/in/...) and a one-sentence reason.
```
