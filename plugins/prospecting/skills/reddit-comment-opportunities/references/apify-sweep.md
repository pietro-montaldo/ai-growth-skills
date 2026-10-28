# The Apify sweep

Everything about pulling posts. Read this at step 3.

Actor: `trudax/reddit-scraper-lite` (Reddit Scraper Lite, pay per result). Use the Apify connector. If you don't have Apify, use `browser-sweep.md` instead.

## Two feeds per community, always

Newest and best-of-week surface different posts, and the overlap is smaller than you expect. A post can be the week's top thread and never appear in a `/new/` window. A three-hour-old question with two upvotes is invisible to `/top/` and is often the best comment slot on the board, because nobody has answered it yet.

For every community, build two start URLs:

- `https://www.reddit.com/r/<name>/new/` for the freshest posts, where first-comment advantage lives
- `https://www.reddit.com/r/<name>/top/?t=week` for the week's most-read threads, where reach lives

Deduplicate by post id after the run. A post appearing in both feeds is a signal rather than a problem: it is fresh and already pulling traffic. Give it plus 1 on traction.

## Sizing: 20 posts per community by default

`maxPostCount` is per start URL, so **10** with two feeds gives 20 posts per community. That is the default, and it is small on purpose.

Twenty recent posts is enough to find three worth answering in a community that genuinely fits. Sweeping 120 per feed to find the same three posts costs twelve times the credit and turns a three minute run into a long one. If 20 posts produce nothing two weeks running, the community is the problem, not the sample size, and that belongs in the pulse row rather than in a bigger sweep.

Ask once before sweeping whether to go deeper, and raise it only when the user asks or when catching up across several weeks.

`maxItems` must cover `maxPostCount` multiplied by the number of start URLs or results truncate silently. At the default, ten communities across two feeds each needs 200, not 100.

## Stage one: the wide pass

Cheap and fast. Do not use `includeMediaLinks` here.

```json
{
  "startUrls": [
    { "url": "https://www.reddit.com/r/smallbusiness/new/" },
    { "url": "https://www.reddit.com/r/smallbusiness/top/?t=week" },
    { "url": "https://www.reddit.com/r/dentistry/new/" },
    { "url": "https://www.reddit.com/r/dentistry/top/?t=week" }
  ],
  "skipComments": true,
  "skipUserPosts": true,
  "maxPostCount": 10,
  "maxItems": 200
}
```

This returns title, body, author, url and createdAt for everything, which is all that problem fit, audience fit, comment opening and commercial path need. Those four dimensions carry 25 of the 30 points, and they are also everything the community pulse needs.

## Stage two: enrich the shortlist

`includeMediaLinks: true` is the only way to get `upVotes`, `upVoteRatio` and `numberOfComments`, and it costs 10 to 15 seconds per post because it visits each post page. Never run it across the whole sweep.

Run it on the shortlist. After stage one scoring, take the top 5 or 6 candidates per community and re-fetch just those by post URL:

```json
{
  "startUrls": [
    { "url": "https://www.reddit.com/r/smallbusiness/comments/abc123/some_post/" }
  ],
  "skipComments": true,
  "skipUserPosts": true,
  "includeMediaLinks": true,
  "maxItems": 40
}
```

Then apply the traction score and the risk deductions and cut to the final three. Posts dropped for weak problem fit or no commercial path never cost an enrichment.

## Input traps, verified the hard way

- **Do not pass `sort`, `time`, `maxComments`, `skipCommunity` or a `proxy` override alongside `startUrls`.** The actor fails with "Invalid input" and exit code 2, and burns a run doing it. Those fields belong to the `searches` mode only. Control ordering through the URL path instead, which is why the feeds above end in `/new/` and `/top/?t=week`
- Batch communities 20 to 25 at a time, so 40 to 50 start URLs, so one failure does not lose the whole sweep
- Read results with the Apify connector's "get dataset items" tool, paginating past the default limit of 20. Keep only items where `dataType` is a post

## Filter before scoring

- Posts older than 7 days. `/top/?t=week` can return an older post that is still ranking, so check `createdAt` on every row rather than trusting the feed
- Stickied and moderator announcement posts
- Posts with no body and no question in the title, unless the title alone states a problem
- Threads past 50 comments, where a new comment will not be read

Keep the filtered-out posts in view for step 4. They still tell you what the community is talking about even when they are not commentable.

## Cost

Results bill at roughly 0.004 USD each. Ten communities at the default 20 posts is 200 results, so under a dollar and usually a few cents against the free tier. Say the number before spending it.
