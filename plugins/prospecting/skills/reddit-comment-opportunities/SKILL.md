---
name: reddit-comment-opportunities
description: "Find the Reddit posts worth commenting on this week, work out how each one turns into business, and draft the comments. Takes your list of subreddits (Excel, CSV or Google Sheet), sweeps each community's newest and top-of-week posts (with Apify, or a browser if you don't have it), scores them against what you sell, and returns an Excel workbook with up to 3 posts per community, a read on what each community is talking about, a brief and a draft comment for each, and a leads sheet for people worth a direct message. Use for \"find Reddit posts to comment on\", \"Reddit comment opportunities\", \"rank Reddit posts by fit\", \"weekly Reddit outreach\", \"which threads should I reply to\", or when you hand over a sheet of subreddits and want comment drafts. Not for finding which subreddits to be in (use reddit-subreddit-finder first) and not for posting or sending anything."
metadata:
  version: "0.2.0"
---

# Reddit Comment Opportunities

Turn a list of subreddits into a weekly shortlist of posts worth replying to, with a commercial reason attached to every one. Each pick gets one of four angles (mention, lead, visibility, or dropped), a brief you could write from yourself, a draft in that community's own voice, and a DM draft when the poster is a prospect. The skill drafts. You post.

**Works best with:** the Apify connector (fast, a few cents a run). Without it, a browser tool or pasted posts work too, just slower. A Google Drive connector helps if your list is a Google Sheet.

## Reference files

- `references/principles.md`: why the skill works this way. Read it before changing any rule.
- `references/setup.md`: the two-skill workflow, connecting Apify, cost, and where the list can live.
- `references/company-profile.md`: the profile fields, and how they map from GTM context.
- `references/apify-sweep.md`: the Apify sweep: feeds, sizing, input traps, filters.
- `references/browser-sweep.md`: the sweep without Apify, in a browser or by pasting.
- `references/community-voice.md`: how to read a community's register and pick a comment shape.
- `references/scoring-rubric.md`: the 30-point rubric, risk deductions, thresholds.
- `references/comment-playbook.md`: what a comment must deliver, the anti-slop filter, search and local angles, mention modes, DMs, honesty rules.
- `scripts/build_workbook.py`: JSON to formatted Excel workbook. Needs `openpyxl`.

## Before starting

Read your context. Use the first that exists, and combine where it helps:

1. **GTM context.** A `gtm-hub.md` file means Notion: fetch the Product & offer, ICP, Messaging and Competitors pages it links. A `gtm/README.md` file means the repo: read `gtm/product.md`, `gtm/icp.md`, `gtm/messaging.md` and `gtm/competitors.md`. Never read the CSV banks whole.
2. **A company profile file**, such as `COMPANY-PROFILE.md` (a previous run of this skill or `reddit-subreddit-finder` leaves one), `BUSINESS-PROFILE.md` or `about-me.md`.
3. **Ask once, in one batch**, only for the fields in `references/company-profile.md` that are still missing. GTM context never holds the Reddit-specific ones (geography, guardrails, your relationship to the company, DMs, default mention mode), so ask for those if the profile file doesn't have them.

If you gave a website, fetch it once for real product vocabulary and proof points. Use that language, not invented language.

**Voice:** the community's register leads (step 4). If a `<name>-voice` skill is installed, use it so the drafts also sound like you. Otherwise, optionally ask for 3 to 5 Reddit comments you've written.

## Steps

### 1. Pause: profile and mention mode

Show what you found and what you still need in one message. If you built or changed the profile, show the draft and save it to `COMPANY-PROFILE.md` in your working folder only after you approve. Never write it inside this skill folder.

**Confirm your relationship to the company** if the profile doesn't say: founder, owner, employee, contractor, affiliate, agency, or a genuine customer with no stake in it.

Then ask the mention mode, every run, with any saved default pre-selected. Offer only what the relationship allows:

- **Disclosed:** names the company and says your connection in one clause ("I run X", "I work on X"). The default for anyone connected to the company.
- **Neutral:** names the company flatly among real alternatives. Still carries a short disclosure clause if you are connected to it.
- **Customer voice:** first person, as someone who uses it. **Only if you confirm, in this run, that you are a genuine customer and not the seller.** Founders, staff, contractors, affiliates and paid partners never get this mode, even if they use the product themselves.

`references/comment-playbook.md` has how each mode is written. Record the mode for Run Info.

**Scheduled runs with nobody to ask:** use the saved profile and the default sweep size. Use disclosed mode unless the profile records you as a genuine customer. State these assumptions in one line at the top of the output.

### 2. Read the subreddit list

This skill doesn't find communities. If there's no list, point to `reddit-subreddit-finder` and stop.

- **A reddit-subreddit-finder spreadsheet** is the ideal input. Use `Subreddit` and `URL`, and treat `Rules` as the most valuable column. Check the date in `Rules source` and flag rules older than about three months. A community you added yourself gets the benefit of the doubt. Read the selection summary next to it for your own reasoning per community.
- **A local `.xlsx` or `.csv`:** read it from the working folder.
- **A Google Sheet:** find it by name with your Google Drive connector and read it. If the connector can't see it, don't guess: ask you to share it or export a CSV, or read it in the browser.
- **Nothing given:** ask once for the file or link.

Match columns loosely: `subreddit` / `community` / `url` (required; normalise `r/name`, `name` or a full URL to `https://www.reddit.com/r/<name>/`), `rules`, `priority`, `notes` / `why`, `entry strategy`, `members`. Drop blank rows, dedupe, and report how many communities loaded.

Before spending anything, check the rules for three things: **promotion banned** (still sweep, but the angle becomes visibility or lead, no mention), **AI-generated content removable** (the anti-slop filter becomes a removal risk), and **karma or account-age gates** (flag them, since no draft helps if the account can't post).

### 3. Pause: sweep the communities

**With Apify:** follow `references/apify-sweep.md`. Default 20 posts per community, 10 from `/new/` and 10 from `/top/?t=week`. Before sweeping, say the size and the cost and ask once:

> Sweeping N communities at 20 posts each, about N x 20 results, a few cents of Apify credit. Go ahead, or go deeper on any of them?

**Without Apify:** follow `references/browser-sweep.md`. Open each community's `/new` and `/top?t=week` in the browser and read the posts, or have you paste post URLs and text. Say up front that this is slower, about 2 to 3 minutes per community, and suggest five communities or fewer.

A community that keeps returning nothing at 20 posts is usually the wrong community, not an undersampled one. Say so.

### 4. Read the community pulse

Before scoring, read the whole sweep per community and write five short fields:

- **What they're talking about:** the two to four themes this week, in the community's words.
- **Questions that keep coming up:** the evergreen ones worth answering well. These are the search surface.
- **How they write:** the voice note from `references/community-voice.md` (length, bullets or prose, formatting, opening move, register, insider words, what gets downvoted).
- **Culture and vendor tolerance:** how the room treats a recommendation.
- **Where this business fits:** one honest line, including "nobody here has this problem".

Say it plainly when a community isn't working.

### 5. Score and select

Follow `references/scoring-rubric.md`: problem fit 0 to 10, audience fit 0 to 5, comment opening 0 to 5, commercial path 0 to 5, traction 0 to 5, then risk deductions. Comment opening and commercial path are gates: fail either and the post is dropped. With Apify, score traction after the shortlist enrichment. With the browser, it's visible in the listing.

Take up to 3 per community. Fewer is fine. Never pad and never invent a post.

### 6. Decide the commercial angle

For every pick, before writing anything, assign one angle and a one-line `business_case`:

- **mention:** the company is genuinely one of the right answers. Name the buying signal.
- **lead:** a live prospect in the wrong venue (rules, culture, audience). Clean comment plus a DM draft. Usually comment first, DM after.
- **visibility:** no honest mention, no single prospect, but a query people search. Name the query. Most picks in a healthy week land here.
- **none:** drop it.

If a community produces only `none`, say so. Never force a mention.

### 7. Write the brief, the draft and the DM

Read `references/comment-playbook.md` first. Write to the community's voice note, not a house style: no bullets where the room doesn't use them, no closing question where the room ends on statements.

For each pick write **the brief** (register and shape, the angle nobody has taken, the anchor fact, what to avoid, post now or wait), **the draft** (complete, editable in three sentences), and for leads **the DM** (shorter, references the thread, says who you are, ends on a question). Run every draft through the anti-slop filter and the "does it belong beside three real comments" test. Vary the shape across the batch.

### 8. Pause: review, then build the workbook

Show the shortlist in the chat first: per community, the post titles, scores and angles, and any rules overrides. Ask before building.

Write the picks to JSON in the shape documented at the top of `scripts/build_workbook.py`, then run it from this skill's folder:

```bash
python3 <this skill folder>/scripts/build_workbook.py posts.json outputs/YYYY-MM-DD-reddit-comment-opportunities.xlsx
```

Sheets: Top Posts, Leads, Community Pulse, Summary, Run Info. Save to `outputs/` in your working folder and give the path.

In the chat, lead with the commercial read: "Nine posts across four communities: two mentions, three leads worth a DM, four visibility plays, and r/x produced nothing two weeks running."

If you learned something worth keeping (a recurring keyword, a community that bans promotion), show the change to `COMPANY-PROFILE.md` and save it only if you approve.

## Rules

- Nothing is posted, commented or messaged by this skill. You read and send every one.
- Never pretend you are a customer when you are the seller. Whenever your own company is named by its owner or staff, the draft says so. Customer voice only for a confirmed genuine customer.
- No invented results, savings, timelines, metrics, rules or customer stories, in any mode.
- A subreddit whose rules require disclosure gets disclosed mode, and the workbook notes the override.
- Mention in roughly one comment in five. Never run the same mention across several threads in one week.
- Usernames appear only on the Leads sheet, for posters you might DM. No real names, emails or profiles beyond that.
- Apify spends credits: say the number of results and ask before every sweep.
