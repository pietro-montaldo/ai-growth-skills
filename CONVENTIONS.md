# Conventions

Every skill in this repo follows these rules. Read them before adding or changing a skill.

## Who it is for

Students of the AI Growth Systems Bootcamp: founders, consultants, marketers and sales or growth operators. Most are not technical. They run B2B services, agencies, courses, SaaS, or B2C offers. A skill must work for all of them, not just for the business it was first built for.

## Context comes from the user, never from the skill

No skill describes a specific company, offer, price, ICP or voice. Each one reads the user's context at the start, in this order, and uses the first that exists:

1. **GTM context from the GTM Context Kit** (https://github.com/pietro-montaldo/AI-Growth-System-Bootcamp). A `gtm-hub.md` file in the project means the context lives in Notion: fetch the pages it links. A `gtm/README.md` file means it lives in the repo: read the pages it links.
2. **A company profile file** in the project, such as `COMPANY-PROFILE.md` or `about-me.md`.
3. **Ask once, in one batch**, only for what this skill needs (for example: what you sell, who buys, price range). Offer to save the answers to `COMPANY-PROFILE.md` so the next skill doesn't ask again.

Voice works the same way: use the user's `<name>-voice` skill if one is installed, otherwise ask for 3 to 5 things they wrote (posts, emails) and match them. Never ship someone else's voice.

## Anonymous by default

Nothing in a skill can point to a real person, company or account:

- No real names, emails, phone numbers, LinkedIn URLs or handles. Use roles ("the founder", "a Head of Sales at a 50-person agency").
- No client or customer names, logos, quotes or deal details.
- No Notion page or data source IDs, Google Sheet or Drive IDs, calendar IDs, course URLs, promo codes or prices.
- No hardcoded MCP tool IDs (`mcp__1a2b3c...`). Name the tool by what it does: "your call recorder (Fathom, Granola, Gong or similar)", "your CRM", "your email".
- Examples use made-up companies (Acme, Brightlane, Kito) and made-up people with first names only.
- No local paths from anyone's machine. Save outputs to the user's working folder, or an `outputs/` folder in it.

## Works without the fancy tools

Every step that uses a connector has a fallback a student can do by hand: paste the transcript, upload a CSV export, paste the email thread, paste the LinkedIn post text. Say which connectors make it faster in a short "Works best with" line, and never block on one.

When a step spends credits (Apify, Clay, Apollo, enrichment), say how many lookups or runs it will be and ask first.

## Human in the loop

- Show a draft before anything is written, saved or logged. Don't write on silence.
- Nothing is ever sent, posted, published, scheduled or connected by a skill. It drafts; the user sends.
- Comments or posts in communities never pretend the user is a customer when they are the founder or seller. Disclose the relationship when the user's own product is mentioned.

## Shape of a skill

- `SKILL.md` under about 150 lines. Detail goes in `references/`. Scripts go in `scripts/` and are standard-library Python where possible.
- Frontmatter `description` is one quoted string: what the skill does, quoted trigger phrases, then "Not for X".
- Frontmatter `metadata.version` is set.
- Sections in this order: one-paragraph purpose, Reference files, Before starting (context), Steps (with numbered pauses), Rules.
- Every file the skill mentions exists in the skill folder. No `__pycache__`, no `.pyc`.

## Writing style

Plain language, short sentences. No em dashes or double dashes. No jargon a non-technical founder wouldn't use. Say "you" to the user.
