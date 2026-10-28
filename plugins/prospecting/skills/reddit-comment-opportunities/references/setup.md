# Setup and cost

## The two-skill workflow

1. Put your company context where Claude can see it: GTM context from the GTM Context Kit, a `COMPANY-PROFILE.md`, or just paste it in.
2. Run `reddit-subreddit-finder` once. It builds a spreadsheet of the communities you picked, with their posted rules. No connectors needed.
3. Spend fifteen minutes actually opening those communities. This decides whether the whole thing works.
4. Run this skill weekly against that spreadsheet. Pick your mention mode when asked.
5. Read the briefs, edit the drafts, post them yourself. Work the Leads sheet separately.

Already know your communities? Build the spreadsheet by hand with a subreddit column and a rules column and skip step 2. A list you researched yourself beats one a search produced.

## Reading Reddit: three ways

| Route | Speed | Cost | What you need |
|---|---|---|---|
| **Apify** (recommended) | A few minutes for 10 communities | A few cents per run | The Apify connector |
| **Browser** | About 2 to 3 minutes per community | Free | A browser tool (Claude in Chrome or the built-in browser) |
| **Paste** | As fast as you can copy | Free | Nothing |

**Apify** is a marketplace of small scraper programs. This skill uses the Reddit Scraper Lite actor. To connect it in the Claude app: Customize, then Connectors, then Browse, search for Apify, install it and log in once. In Claude Code you can add Apify's official MCP server (`https://mcp.apify.com`) with an API token from your Apify account settings. Apify's free tier gives a small monthly credit that covers many weekly runs. Results bill at a fraction of a cent each, and the default sweep is 20 posts per community, so ten communities is about 200 results.

**Browser and paste** are in `browser-sweep.md`. They are slower and work best with five communities or fewer per run.

## The community list

Any of these work:

- **A local `.xlsx` or `.csv`** in your working folder. Nothing to install.
- **A Google Sheet**, read through your Google Drive connector. The connector only sees files your connected account can open. If it can't find the sheet, share it with that account, or export it as CSV into your folder.
- **A Sheet the connector can't reach**, read through the browser tool.

## Not needed

No Reddit account or Reddit API access is needed to run this skill. You only need an account to post the comments, which you do yourself. Nothing in this skill posts to Reddit or sends a message.
