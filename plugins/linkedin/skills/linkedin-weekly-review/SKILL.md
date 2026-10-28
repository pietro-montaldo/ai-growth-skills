---
name: linkedin-weekly-review
description: "Review how your LinkedIn posts did this week. Collects impressions, reactions, comments, reposts, saves, sends, profile views and new followers for each of your posts (from your own analytics in the browser, an analytics export, or stats you paste), then builds a visual report that ranks posts by impressions and explains why each one performed the way it did. Use for \"how did my posts do this week\", \"LinkedIn weekly review\", \"LinkedIn recap\", \"post performance\", \"which posts did best\", \"Friday review\", or questions about impressions, saves or engagement on your own posts. Not for analysing other people's posts or scraping anyone's profile."
metadata:
  version: "0.1.0"
---

# LinkedIn weekly review

You collect the numbers for your own LinkedIn posts from the last week, rank them by impressions, and explain why each one did well or badly. Impressions are the north star. Saves, sends, comments, reactions and reposts explain how each post got there.

**What this skill does and doesn't do.** It only reads your own post analytics, the same pages you can open yourself. It is read-only: it never likes, comments, posts, edits or messages. When it uses the browser, it moves at a human pace (a few seconds between pages, one post at a time) and stops if LinkedIn shows a warning or a check.

**Works best with:** Claude in Chrome (it uses your signed-in LinkedIn) or the built-in browser. Without a browser, use an analytics export or paste the stats.

## Reference files

- `references/collect-analytics.md`: how to collect the numbers in the browser, from an export, or from pasted stats, and how to handle missing data.
- `references/output-spec.md`: the visual report, the written insights, and the data file this skill saves.

## Before starting

1. **Your profile URL.** Look for it in `COMPANY-PROFILE.md` or `about-me.md`. If it isn't there, ask: "What's your LinkedIn profile URL? (It looks like linkedin.com/in/your-name)". Offer to save it to `COMPANY-PROFILE.md` so the next run doesn't ask.
2. **Audience.** To judge topic fit, read who the posts are for: the ICP page linked in `gtm-hub.md`, or `gtm/icp.md` if the project has `gtm/README.md`, or `COMPANY-PROFILE.md`. If none exist, skip it and judge on the numbers alone.
3. **Date range.** Default is Monday to Friday of the current week, using today's date. When run by hand, ask if you want a different range. When run on a schedule, use the default and don't ask.
4. **Data source.** Ask which way you want to go, and recommend the first one available:
   - **Browser:** Claude in Chrome or the built-in browser. You need to be signed in to LinkedIn yourself. This skill never enters your password.
   - **Export:** on LinkedIn, open Analytics, pick the date range and click Export. Put the file in the working folder.
   - **Paste:** paste each post's first lines and its numbers.

## Steps

### 1. Find this week's posts

Follow `references/collect-analytics.md` for the source you chose. List every original post in the date range with its first line and date. Skip reposts (items marked "<your name> reposted this") and comments.

Say the count: "Found 4 posts from Monday to Friday." If a date is unclear, say so and include the post.

### 2. Collect the numbers for each post

For every post, collect: hook (first 2 to 3 lines), date and weekday, impressions, reactions, comments, reposts, saves, sends, profile viewers from the post, followers gained. Note link clicks if shown.

Flag any post published less than 2 hours ago: its numbers are still climbing, so the analysis for it stays light.

Mark missing metrics as N/A. A post with no impressions goes to the bottom of the ranking.

### 3. Pause: confirm the data

Show the table of posts and numbers (on a scheduled run, skip this pause, see `references/output-spec.md`). Ask: "Does this match what you see? Anything missing?" Fix what you point out. Don't build the report on numbers you haven't seen.

### 4. Build the report

Follow `references/output-spec.md`:
- A React report saved as `outputs/YYYY-MM-DD-linkedin-weekly-review.jsx` in the working folder.
- The week's data saved as `outputs/YYYY-MM-DD-linkedin-weekly-review.csv`, so other skills (like session-to-linkedin-post) can learn from it later.

### 5. Written insights

In the conversation, add a short summary:
1. **Top performer:** which post won and the single biggest reason.
2. **Underperformer:** which post had the most room to improve, and one specific fix.
3. **Save and send standout:** the highest save or send rate, and what it says about what your audience keeps vs shares.
4. **Engagement driver:** which metric moved most with impressions this week. Data-grounded, and honest about the small sample.
5. **Pattern:** one trend across the week.
6. **One action for next week.**

Every point uses this week's real numbers. No generic advice.

## Rules

- Only your own posts and your own analytics. Never browse or collect other people's profiles or posts.
- Read-only. Never click like, comment, repost, follow, connect, message or edit.
- Human pace in the browser: one page at a time, a few seconds between pages. If LinkedIn shows a warning, a captcha or a sign-in page, stop and ask you to handle it.
- Never type a password or sign in for you.
- Never invent a number. N/A is better than a guess.
- Save files only to the working folder's `outputs/`. Nothing is posted or shared.
