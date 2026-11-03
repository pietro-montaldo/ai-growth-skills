# Qualify prompt (agent node "Qualify signal")

Fill the `<...>` parts from the user's ICP card, show the result to the user, then paste it as the node's `agentPrompt`. Keep the `{{...}}` variables: they are the node's inputs, wired from "Read company and signal". Outputs: `qualified` (boolean) and `reason` (string). Start with the smallest model and move up only if the answers are wrong.

```text
You decide whether one company signal is a real reason to offer <the offer, in a few words> to {{company_name}} ({{domain}}).

Signal type: {{signal_type}}

If the signal type is job_post:
- Job title: {{job_title}}
- Posting URL: {{job_url}}
Open the posting URL and read the job description. If the page cannot be read, search the web for this exact job title at {{company_name}} and read the posting there.
Qualified only if BOTH are true:
1. <what the posting must show, for example: "<tool>" means the software tool, not a person's name>.
2. <what rules it out, from the ICP disqualifiers, for example: the posting names a competing tool as the company's standard>.

If the signal type is new_hire:
- Person: {{hire_name}}
- Title: {{hire_title}}
- LinkedIn: {{hire_linkedin}}
Qualified only if the role <owns the problem the offer solves, for example: owns training and enablement for the company's own staff>. Not qualified if the person <the look-alike roles to exclude, for example: is a freelancer, a reseller, a recruiter hiring for the role, or the title only matches because of what the company sells>. Judge from the title first; open the LinkedIn profile only if the title is ambiguous.

If the signal type is news:
- Headline and link: {{signal_detail}}
Qualified only if the news <the trigger from the ICP card, for example: is a funding round, a new leader in the buyer's function, or a new program the offer supports>.

Do not research anything else. If you cannot find enough evidence, answer not qualified.
Return qualified (true or false) and a one-sentence reason quoting the evidence.
```
