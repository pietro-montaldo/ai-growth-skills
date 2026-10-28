# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`ai-growth-skills` is a public Claude Code plugin marketplace of commercial skills for students of the AI Growth Systems Bootcamp. One plugin per topic: `linkedin`, `newsletter`, `sales-calls`, `prospecting`, `skill-building`. The skills are content (SKILL.md, references, small standard-library Python scripts). There is no build step and no test suite.

GTM context (product, ICP, competitors, messaging, objections, customers) is built by the separate GTM Context Kit repo. This repo only links to it and never copies its skills.

## Commands

```bash
claude plugin validate .                       # marketplace manifest
claude plugin validate plugins/<plugin>        # one plugin
```

To try locally: `/plugin marketplace add ./` then `/plugin install <plugin>@ai-growth-skills`.

## Rules

[CONVENTIONS.md](CONVENTIONS.md) is the source of truth. The ones that matter most when editing:

- Skills read the user's context (GTM kit, then `COMPANY-PROFILE.md`, then ask). Never describe a specific company, offer, price, ICP or voice inside a skill.
- No real names, emails, URLs, IDs, prices, promo codes or client details. No hardcoded MCP tool IDs. Before committing, run:
  `grep -rniE "pietro|montaldo|notlinear|maven\.com|nforce\.ai|collection://|mcp__[0-9a-f]{6}|/Users/" plugins/*/skills`
  It should find nothing. (The NotLinear credit and course link in each `plugin.json` are intended.)
- Every connector step has a paste or export fallback. Steps that spend credits ask first.
- Skills draft; they never send, post or publish. Every write has an approval pause.
- New skills go in the plugin for their topic and get a row in the README table.

## Writing style

Students are non-technical. Plain language, short sentences, no em dashes or double dashes. Frontmatter `description` is one quoted string: what it does, quoted trigger phrases, then "Not for X". Keep SKILL.md under about 150 lines and push detail into `references/`.
