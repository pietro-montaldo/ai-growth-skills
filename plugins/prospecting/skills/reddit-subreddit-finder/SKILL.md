---
name: reddit-subreddit-finder
description: "Run a fast, browsing-only sweep for the subreddits where your buyers actually gather, hand back a shortlist you open and judge yourself, then build a spreadsheet of your picks with each subreddit's posted rules. Uses web search and a browser only, no connectors and no paid scraping, and is built to finish in about ten minutes. Use for \"find subreddits\", \"where should I be on Reddit\", \"which communities fit my business\", \"Reddit target list\", \"where do my customers hang out on Reddit\", \"help me get started with Reddit\", or when you are setting up Reddit as a channel and don't know where to look yet. Not for finding this week's threads to comment on (use reddit-comment-opportunities)."
metadata:
  version: "0.2.0"
---

# Reddit Subreddit Finder

Give you a shortlist of communities to judge for yourself, fast. This is a quick sweep, not a study. You will find better subreddits than any search, because you know your market and can read a room. The skill saves you the blank page and the first twenty searches, then gets out of the way. **Target about ten minutes of working time.** If a step runs past its budget, ship what you have and say what was skipped.

**Works best with:** a browser tool (Claude in Chrome or the built-in browser) and web search. Nothing else is needed, and nothing here costs credits.

## Reference files

- `references/browsing-reddit.md`: how to skim a feed and read the rules when Reddit blocks a page, and what to look for in the rules.

## Before starting

Read your context before asking anything. Use the first that exists:

1. **GTM context.** A `gtm-hub.md` file means it lives in Notion: fetch the Product, ICP and Messaging pages it links. A `gtm/README.md` file means it lives in the repo: read `gtm/product.md`, `gtm/icp.md` and `gtm/messaging.md`. The ICP page gives the buyer, the messaging page gives the buyer's own words, which are the search vocabulary.
2. **A company profile file**, such as `COMPANY-PROFILE.md`, `BUSINESS-PROFILE.md` or `about-me.md`.
3. **Nothing found:** ask in step 1.

Outputs go to `outputs/reddit-target-list/` in your working folder, named `YYYY-MM-DD-description.ext`.

## Steps

### 1. Interview: one exchange, about two minutes

If context exists, open with it: "I have you down as X selling Y to Z, still right?" Don't make anyone retype what they already wrote down.

Otherwise ask one open question: "Tell me about your business. What do you sell, and who buys it?" Keep their words. Their phrasing is the search vocabulary.

Then one round of at most three questions, only for what is missing:

- **Who has the problem, in job title terms.** "Small businesses" is not searchable. "Salon owners doing their own books" is.
- **Which buyer, when there are several.** Someone paying with their own card and a company with a procurement process sit in different subreddits. Don't average them.
- **Anything to steer away from.** Adjacent topics, competitors' communities, parts of the market you've said no to.

If you gave a website, fetch it once. A homepage names job titles and the problem in your own words. One fetch, not a crawl.

Don't go past two exchanges. If the input is thin, say what you assumed and move on.

### 2. One search sweep, about four minutes

Run one batch of searches covering five angles:

- **Profession:** where the buyer's job title gathers to talk about the work.
- **Problem language:** the symptom in the buyer's words. People post about being overwhelmed, not about product categories.
- **Product category:** the obvious one. Run it, expect it to be the least useful.
- **Adjacent tools:** the software the buyer already uses daily. People post when they hit a wall in a tool.
- **Life situation:** recently promoted, changing careers, taking over a team, going independent.

Two searches per angle is enough. Use `site:reddit.com` queries plus Reddit's own search in the browser. If you can run parallel sub-agents, run the five angles at once and tell them to return candidates, not analysis.

**Don't sample every candidate's feed.** That turns ten minutes into an hour, and you do it better anyway. Open the feeds of the top three or four only, to catch an obviously dead or mismatched community. Label everything else unverified.

Watch for one pattern: communities full of the right people often don't discuss the category at all, and communities discussing the category are often practitioners and competitors, not buyers. Say which one each candidate looks like, because they need different entry strategies.

Aim for 12 to 15 candidates. Stop there.

### 3. Pause: hand over the shortlist, about one minute

Paste the shortlist in the chat, best first, then save it as markdown in the output folder. It's meant to be read with a browser open.

```
### r/name  ->  https://reddit.com/r/name
Roughly N members (unverified)
What it is: one line
Why I picked it: one line
Worth checking: <the specific thing to look at on landing>
```

The "worth checking" line is the useful part. Point at what would confirm or kill it.

Say plainly which ones you opened and which you didn't. Member counts from third-party sites disagree, so give a range and label it unverified.

Then hand the real work over:

> This is a first pass from search, not a verdict. Open each one in a tab and give it two minutes: are the people posting the people you sell to, are they asking questions you could answer well, and what do the sidebar rules say about promotion. Check the sidebar for related subreddits and look at where the regulars post next. That's how you find the ones search never surfaces. Then tell me which ones felt right, including any you found yourself.

### 4. Pause: ask you to choose

Don't infer the choice from enthusiasm in the chat. Ask directly with a multi-select list of the candidates, and make it obvious you can add your own.

Your picks and your additions carry equal weight. A subreddit you've lurked in for a year beats anything a search turned up.

### 5. Rules pass and spreadsheet, about three minutes

Spend the effort only on the chosen ones. One row per subreddit:

| Column | Content |
|---|---|
| Subreddit | r/name |
| URL | full https://reddit.com/r/name link |
| Members | approximate range, or "unverified" |
| Rules | the actual posted rules, condensed, self-promotion rules first |
| Rules source | where they came from, and the date read |
| Selected by | "user pick" or "user addition" |
| Why | one line, yours if you gave a reason |
| Entry strategy | one line on how to get traction there |

Build it as an Excel file (or CSV if Excel isn't available): readable font, wrapped text, frozen header row, a wide rules column. Highlight the surprises: a subreddit that allows promotion under conditions, or one that removes a post for naming a company.

`references/browsing-reddit.md` says how to get the rules. Give each subreddit one attempt down that list and move on. **Never write a rule you didn't read.** Where you couldn't get them, write "could not retrieve, check the sidebar" and say what you tried.

Show the condensed rules per pick in the chat, then save the spreadsheet.

### 6. Pause: two handoff files

**The selection summary**, markdown, next to the spreadsheet: one short section per chosen subreddit with the rules that matter, why it was chosen and the entry strategy. Keep your reasoning in your own words. This is what `reddit-comment-opportunities` reads next.

**`COMPANY-PROFILE.md`**, in your working folder (not the output folder), so the weekly skill doesn't ask the same questions again. If GTM context exists, only add the Reddit-specific parts: the buyer's search vocabulary, the trigger moment, geography and the steer-away list. Otherwise write the whole interview: what you sell, who buys, the trigger, vocabulary, geography, what to avoid.

Show both drafts and save only after you approve. If `COMPANY-PROFILE.md` already exists, show the changes and update it rather than overwriting it.

## Rules

- Web search and a browser only. No connectors, no paid scraping, no Reddit API.
- Never invent a subreddit rule, a member count or a community you didn't find. Label what you didn't verify.
- Nothing is posted, joined or messaged. You do that yourself.
- No personal usernames in the outputs. Describe communities, not people.
- **Refreshing:** re-running is not starting over. Read the existing list, ask what has been working, drop what you've given up on, and spend the sweep on new candidates. Report what changed.
