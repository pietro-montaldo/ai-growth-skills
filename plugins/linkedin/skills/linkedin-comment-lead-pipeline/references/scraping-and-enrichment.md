# Getting engagers and enriching them

## A. With Apify

Apify actors change. Before every run, read the actor's details and input schema, and fetch 2 or 3 items to check the real field names before pulling the rest.

### One post, commenters only (default)

A good starting actor is `apimaestro/linkedin-post-comments-replies-engagements-scraper-no-cookies`: no cookies needed, and it returns comment text, author name, headline and profile URL. Typical input:

```json
{"postIds": ["<post url>"], "page_number": 1, "sortOrder": "most recent", "limit": 100}
```

- Each item is a top-level comment with its replies nested inside. The post author's replies are usually in the replies: tag them `Author`.
- More than 100 comments: page with `page_number`.
- The total count in the run's metadata can be off by one. Trust the items you actually get.
- If it fails, search the Apify store for another LinkedIn post comments actor (for example `harvestapi/linkedin-post-comments`).

### Several posts, or reactors too

When you want more than one post, or reactors as well as commenters:
- Use an actor that takes a list of post URLs, or a profile URL plus a number of recent posts, and has options to include comments and reactions. Search the Apify store for "LinkedIn profile posts" and check the input schema for those options.
- Results often mix posts, comments and reactions in one dataset. Split them by item type and link each comment or reaction to its post.
- Before going further, report what was captured: "3 posts. Post 1: 'first 60 characters...' (120 reactions, 34 comments)." Wait for an OK. A post that came back with no engagers usually means a wrong URL.
- Reactor lists are often capped or partial on LinkedIn's side. Say so if the counts look low.
- Reactors mean many more rows and more credits. Give the expected item count before the run.

### Pulling the data

The first call usually returns a preview, and long runs keep going in the background. Check the run status until it's finished, then fetch the dataset in chunks (about 15 to 50 items at a time), asking only for the fields you need. Save the rows to `raw.json` as soon as you have them.

## B. Without Apify: paste or export

Any of these works:
- **Paste.** Open the post on LinkedIn, expand all comments, select the comments section and paste it into the chat. Each comment block usually shows name, headline, time and text. Profile URLs don't come through a paste: leave them blank and say the DMs will need you to find each profile.
- **Export.** If you use a LinkedIn tool that exports post engagers (many scheduling and analytics tools do), put the CSV in the working folder.
- **A list you typed.** Name, headline and what they said is enough.

Parse it into the same rows as the Apify path. Reactors are hard to copy by hand: suggest commenters only on this path.

## C. Enrichment (optional)

Use an enrichment tool like Clay or Apollo, if connected. Only after the yes in Step 5 of SKILL.md.

### What to collect, and nothing else

- Current role (title).
- Current company and its website domain.
- Location.
- Work email, and whether it is verified.

Never collect mobile or personal phone numbers. Don't run extras like work history summaries, funding, headcount or tech stack unless you ask for them, because they spend more credits.

### How to match

1. **Match by LinkedIn URL first.** It works even when the headline has no company, and it returns the current employer and domain.
2. **Then find the work email** from the person's name plus the company domain from step 1. Clean the name first: drop credentials and emojis (", PhD", "🚀").
3. People with no current company: skip the email step. `match_note`: "no current employer found, no email".
4. **Wait until every lookup is finished** before scoring or writing anything. Never report an email as missing while lookups are still running. If it's slow, say how many are done and keep waiting.

### Tool notes

- **Clay:** functions differ per workspace. List the workspace's functions first and pick one that enriches a person from a LinkedIn URL and one that finds a work email. Avoid any function that also finds phone numbers. Results come back in input order with the inputs echoed: map back by LinkedIn URL. Large results may be saved to a file: pull only the fields above with a short script, don't print whole profiles.
- **Apollo:** bulk match takes up to 10 people per call, by LinkedIn URL plus name. It shows the credit cost before the call: tell you and wait for a yes. Unmatched people are left out of the response, so map back by name or URL, never by position.
- People one tool didn't match: give the count and offer to try the other tool for just those, on a yes.

### Checking matches

- Set `enriched_via` to the tool name.
- If the returned name or role clearly differs from the engager, set `match_note` to "verify".
- If the current employer differs from the headline, note it. A URL match is usually right (headlines go stale).

## leads.json schema

```json
{
  "meta": {"post_urls": [""], "post_topic": "", "offer": "", "offer_url": "", "slug": "YYYY-MM-DD-short-name"},
  "leads": [
    {"name": "", "type": "Person|Company|Author", "headline": "", "profile_url": "",
     "engagement": "comment|reaction|comment + reaction", "posts_engaged": 1, "comment": "",
     "enriched_via": "", "enriched_name": "", "title": "", "company": "", "location": "",
     "email": "", "email_status": "", "match_note": "", "fit": 0, "rationale": "", "dm": ""}
  ]
}
```

`dm` is only needed for leads with `fit` 4 or 5, and those leads need `profile_url` so you can open the profile and send the DM.
