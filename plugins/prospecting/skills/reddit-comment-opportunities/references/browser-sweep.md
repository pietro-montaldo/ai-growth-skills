# The sweep without Apify

Use this when Apify isn't connected or you don't want to spend credits. It's free and it works, but it's slower: about 2 to 3 minutes per community in a browser, so say that up front and suggest five communities or fewer per run. Everything after the sweep (pulse, scoring, angles, drafts, workbook) is the same.

## Route A: read the feeds in a browser

For each community, open both feeds with the browser tool (Claude in Chrome or the built-in browser):

- `https://old.reddit.com/r/<name>/new/` for the freshest posts
- `https://old.reddit.com/r/<name>/top/?t=week` for the week's most-read threads

`old.reddit.com` loads faster and blocks less often. If it fails, try `https://www.reddit.com/r/<name>/new/`, then `https://www.reddit.com/r/<name>/new/.rss`. One try each, then move on and note it in Run Info.

From each feed, take the first 10 posts that aren't pinned or moderator announcements. For each, record: title, URL, age, upvotes and comment count (both are visible in the listing), and the author's username only if the post may become a lead.

Then open the posts that look promising from their titles, about 4 to 6 per community, and read the body. Skip the rest. A post in both feeds gets plus 1 on traction, the same as the Apify route.

Because the listing already shows upvotes and comments, there is no separate enrichment stage. Score traction straight away.

Apply the same filters as `apify-sweep.md`: older than 7 days, pinned posts, no body and no question in the title, threads past 50 comments.

## Route B: paste it in

If the browser tool isn't available, or Reddit blocks it, ask the user to do the sweep by hand:

> Open each community's /new and /top (this week) pages. For anything that looks like a fit, paste the post URL, the title and the post text here. About 5 to 10 posts per community is plenty. Add the upvotes and comment count if you can see them.

Score what they paste the same way. Traction is scored only where they gave the numbers, otherwise mark it 3 and say it is unverified.

## What to write in Run Info

Name the route used (browser or paste), how many posts were read per community, and any community that wouldn't load. Put "browser" or "pasted" where the Apify actor and run id would go.
