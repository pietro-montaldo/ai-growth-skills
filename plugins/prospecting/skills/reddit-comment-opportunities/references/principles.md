# Why this skill works the way it does

Most tools for this problem search Reddit for keyword matches and hand back threads to go and mention yourself in. The output looks like work. It performs badly, and it tends to end with an account nobody reads any more. Every rule in this skill follows from one of the ideas below. Read this before changing any of them.

## 1. Finding communities and working them are different jobs

Community research happens rarely, benefits from breadth and ends in a human judgement call. Thread selection happens weekly, benefits from depth and ends in something you can post. So `reddit-subreddit-finder` runs once per market, and this skill runs every week against the list it produced. This skill never re-researches communities.

## 2. You judge a community better than any tool

Two minutes in a subreddit tells you whether the regulars are buyers or competitors, whether the mods are strict in practice, and whether the place is alive. A list you built yourself beats an automated one. Automated discovery is the fallback for people without a list, not the default.

## 3. A community's rules are data

The subreddit list carries each community's real posted rules, and this skill uses them. A ban on promotion scores drafts down and removes the mention. A rule against AI-generated content turns the anti-slop filter into a removal risk. A karma or account-age gate gets flagged before anything is spent. Without the rules column, every one of those is a guess.

## 4. Both feeds, or you see half the board

Newest and top-of-week surface different posts. The top feed gives reach: threads already pulling traffic. The new feed gives the question nobody has answered yet, where you are the first reply. A three-hour-old post with two upvotes often beats the week's top post, because being first is worth more than being loud. A post in both feeds gets a bonus.

## 5. Sweep shallow, enrich narrow

Twenty posts per community is enough to find three worth answering in a community that fits. A community that returns nothing at twenty posts two weeks running is the wrong community, not an undersampled one. Problem fit, audience fit, comment opening and commercial path carry 25 of the 30 points and need only the post text. Only the shortlist gets the slower engagement check.

## 6. Every pick needs a commercial reason, named out loud

The quiet failure is nice comments that earn nothing. So every selected post gets one of four angles before a word is drafted:

- **mention**: the company is honestly one of the right answers, and the buying signal can be named
- **lead**: the poster is a live prospect but the thread is the wrong venue, so the comment stays clean and a DM is drafted separately
- **visibility**: no honest mention and no individual prospect, but the thread is a query people search, and a strong answer earns standing
- **none**: not in the workbook at all

Visibility is a real outcome, and most picks in a healthy week land there. It's also what lets the mentions survive: an account that only ever mentions one brand gets filtered. A forced mention never fills a column. "This community produced nothing worth answering, two weeks running" is worth more than three polite drafts.

## 7. What a community talks about is an output

The sweep already pulls every recent post, so summarising the week's themes costs nothing and answers the question the shortlist can't: is this list still right? The recurring questions are the search surface. The honest "where this business fits" line is what gets a dead community dropped.

## 8. A comment must be worth reading without the mention

If the only honest thing to say is "use our product", the post is dropped however good the topic fit looks. Comments with nothing in them get downvoted, and downvoted brand mentions are exactly what gets a name into an automod filter. Fewer than three posts for a community is a correct result. Padding is what makes this kind of tool useless after two weeks.

## 9. AI-sounding text is a removal risk

More subreddits name AI-generated content as removable, and readers spot it in seconds. So drafting carries a real filter: banned words and structures, contractions required, varied sentence length, varied shape across the batch, and a 30 percent cut. The filter is necessary but not enough.

## 10. Every community has a voice, and the comment has to be in it

A comment is judged against the comments around it. What gives an outsider away is the shape: more formatted, longer, politer, more hedged than anything nearby, using the category's marketing words instead of the room's own word. So each community gets a voice note built from the sweep, and the last check on every draft is "does it belong beside three real comments from this room". Most drafts end up with no bullets, because most communities don't use them.

## 11. Two ways to use the output

Some people want the thread and the angle, then write it themselves. Others want a draft to edit. Every pick gets both: a brief that makes the thread writeable on its own, and a full draft. Leads get a DM draft too.

## 12. Honesty is not a setting

How the company appears in a comment is your call: named with your connection, listed flatly among alternatives, or left out. Whether you are honest about who you are is not. If you own, work for or earn from the company, any comment that names it says so. Customer voice is only for real customers who are not the seller. No invented results, savings, timelines or stories in any mode. Reddit's own rules, most subreddit rules, and endorsement rules in the US, UK and EU all require disclosing a material connection, and moderators act on it quickly. A subreddit that requires disclosure gets disclosed mode whatever you picked.

## 13. The account is the asset

One comment rarely causes a problem. A pattern does: the same brand, the same enthusiasm, across threads, from an account with no other history. So mention in roughly one comment in five, never run the same mention across several threads in one week, and skip the mention whenever you aren't genuinely one of the right answers. An account in an automod filter doesn't come back.

## What the skill never does

- Post anything to Reddit or send any DM. A human reads and sends every message
- Find new communities (that's `reddit-subreddit-finder`)
- Invent subreddit rules, results, savings or customer stories
- Pad a shortlist, or force a company mention to fill a column
- Write every comment in the same voice, imitate a specific user, or claim a trade you aren't in
