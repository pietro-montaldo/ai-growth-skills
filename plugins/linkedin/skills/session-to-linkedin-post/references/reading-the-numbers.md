# Reading past post performance

The goal is not a full analysis. It's to find which kinds of posts your audience rewards, so the ideas from the session lean that way.

## Get one row per post

- **Weekly review files** (`outputs/*-linkedin-weekly-review.csv`): the same post can appear in more than one file if it was captured in two weeks. Keep the row with the latest `Captured on` date for each post (match on `Post URL`, or on the hook if the URL is missing).
- **LinkedIn export:** use the post-level sheet. It usually has impressions and engagements, and often no saves.
- **Pasted posts:** use what you gave. Ask for impressions and saves if you know them, but don't block on it.

Rank by total engagement, and look at the top 10 to 20 posts.

## How to read the numbers, and why

- **Weight saves, save rate and followers gained above comments.** Posts with "comment X to get it" mechanics inflate comment counts, so comments there say little about the idea itself.
- **Separate reach from depth.** Reach is impressions. Depth is save rate and engagement rate. Opinion and news posts often get reach with almost no saves. "Here is my setup" posts tend to win on depth. Say which one an idea is likely to win on.
- **Don't compare recent posts with old ones directly.** A post captured 2 days after publishing has had less time to grow than one captured 3 weeks after. Say so when you compare.
- **Old rows without post text** only give you the hook or title. Treat patterns from them as rough.
- **Small samples are directional.** With fewer than about 10 posts, say the patterns are a hunch, not a rule.

## What to pull out

For the top posts, note:
- The topic and the format (text, image, carousel, video).
- The hook pattern (see `ideas-and-drafts.md`).
- Whether it won on reach, on depth, or both.

Use these to explain each idea in Checkpoint 1: "Like your post on [topic] ([X] saves, your best save rate), this is a setup post."

## No data at all

If there is no weekly review, no export and no pasted posts:
- Say so in one line.
- Ground each idea in your audience's pains and words from your GTM context (ICP and Messaging), or in your profile file.
- Use the general hook patterns in `ideas-and-drafts.md` instead of model posts.
- Suggest running `linkedin-weekly-review` for a few weeks so the next run has data.
