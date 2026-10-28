# AI Growth Skills

Claude skills for the commercial side of a business: LinkedIn, newsletters, sales calls and prospecting. Plus two tools for building better skills of your own.

Each skill was built and used on a real business first, then cleaned up so it works for yours. Nothing in them is about one company: every skill reads **your** context (what you sell, who buys, how you sound) before it does anything.

Built for students of the [AI Growth Systems Bootcamp](https://maven.com/pietro-montaldo/ai-growth-system-bootcamp-claude). Free for anyone to use.

## Start with your GTM context

These skills work best once Claude knows your business. Build that first with the **[GTM Context Kit](https://github.com/pietro-montaldo/AI-Growth-System-Bootcamp)**: product, ICP, competitors, customer language, objections and shareable customers, in Notion or in your own repo.

No GTM context yet? Every skill still works. It asks a few questions the first time and offers to save the answers to a `COMPANY-PROFILE.md` file, so the next skill doesn't ask again.

## What's inside

| Plugin | Skills | What you get |
|---|---|---|
| **linkedin** | `linkedin-hook-generator`, `linkedin-post-reviewer`, `linkedin-weekly-review`, `session-to-linkedin-post`, `linkedin-comment-lead-pipeline` | Hooks and posts in your voice, a scored review before you publish, a weekly read on what worked, posts drafted from your calls, and a ranked lead list from the people who commented on a post |
| **newsletter** | `newsletter-writer` | A full edition from your raw notes and links, with subject lines |
| **sales-calls** | `pre-call-brief`, `sales-call-coach`, `call-followup-email`, `proposal-from-call`, `webinar-followup-email`, `inbound-triage` | A brief before the call, coaching after it, the follow-up email and the proposal, webinar follow-ups for attendees and no-shows, and a weekly review of who reached out |
| **prospecting** | `reddit-subreddit-finder`, `reddit-comment-opportunities`, `icp-lead-ranker`, `respondent-persona` | The communities where your buyers are and the threads worth answering, a lead list ranked against your ICP, and a buyer persona from your sign-ups |
| **skill-building** | `skill-auditor`, `skill-model5-upgrade` | An audit of any skill against best practices, and an upgrade for skills written for older Claude models |

## Install

In Claude Code, add the marketplace once:

```
/plugin marketplace add pietro-montaldo/ai-growth-skills
```

Then install the plugins you want:

```
/plugin install linkedin@ai-growth-skills
/plugin install newsletter@ai-growth-skills
/plugin install sales-calls@ai-growth-skills
/plugin install prospecting@ai-growth-skills
/plugin install skill-building@ai-growth-skills
```

In the Claude app (Cowork or chat), download a skill's folder as a zip and upload it under Customize, then Skills.

Then just ask in plain words, for example "prep me for my call with Acme tomorrow" or "write hooks for a post about onboarding". Each skill's description lists the phrases that start it.

## What to connect

Nothing is required. Every step that uses a tool also works if you paste the data in or upload an export. Connectors just make it faster:

| Connector | Used by |
|---|---|
| Email (Gmail, Outlook) | follow-ups, pre-call brief, inbound triage |
| Call recorder (Fathom, Granola, Gong, Zoom) | call coaching, follow-ups, proposals, session-to-post |
| Calendar | pre-call brief, call coaching |
| CRM (HubSpot or similar) | pre-call brief, inbound triage |
| Browser (Claude in Chrome) | LinkedIn weekly review, Reddit finder |
| Apify | LinkedIn comment pipeline, Reddit comment opportunities |
| Enrichment (Clay, Apollo) | lead ranking and the comment pipeline, optional |

Skills that spend credits (Apify, enrichment) tell you how many runs they need and ask first.

## The rules every skill keeps

- **It drafts, you send.** No skill sends an email, posts a comment, publishes or schedules anything.
- **You approve before anything is saved.** Every write has a pause.
- **Honest in public.** Comments and posts that mention your own product say you're behind it.
- **Your data stays yours.** Skills describe people by role and company type, never by name, in anything they save.

See [CONVENTIONS.md](CONVENTIONS.md) for the full set, if you want to change a skill or add your own.

## License

MIT. Made by [NotLinear](https://www.notlinear.ai).
