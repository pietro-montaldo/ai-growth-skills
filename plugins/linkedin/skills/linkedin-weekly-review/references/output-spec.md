# Output spec

Two files go into `outputs/` in the working folder, named with today's date:
- `YYYY-MM-DD-linkedin-weekly-review.jsx`: the visual report.
- `YYYY-MM-DD-linkedin-weekly-review.csv`: the raw numbers.

## The data file (CSV)

One row per post. Header exactly:

```
Date,Weekday,Hook,Post URL,Impressions,Reactions,Comments,Reposts,Saves,Sends,Profile viewers,Followers gained,Early snapshot,Captured on
```

- Dates as `YYYY-MM-DD`. N/A for missing numbers. `Early snapshot` is `yes` or `no`.
- `Captured on` is today's date. Posts keep growing after the week ends, so numbers captured on different days are not directly comparable. Other skills read this column to know that.
- Write it with Python's `csv` module so commas and quotes in hooks stay valid.

## The visual report (React)

A single self-contained `.jsx` component with all data embedded. No external fetches.

### Summary stats at the top

Eight stat cards in a grid:
- Total impressions
- Total comments
- Total reactions
- Average impressions per post
- Total saves
- Total sends
- Profile views from posts
- New followers from posts

### Horizontal bar chart

- Posts ranked from most to least impressions.
- Each bar labelled with the hook cut to about 40 characters.
- Top performer in a strong blue (#2563eb), the others in neutral grays.
- Tooltips with the full hook and the impression count.
- Use Recharts: `import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from "recharts"`.

### Engagement rate table

Each rate is a percentage of impressions, per post:
- Save rate = saves / impressions x 100
- Send rate = sends / impressions x 100
- Comment rate = comments / impressions x 100
- Reaction rate = reactions / impressions x 100
- Repost rate = reposts / impressions x 100

Highlight in blue any value above the week's average, so you can spot posts that punch above their weight on one type of engagement.

### Engagement and impressions insight box

A blue box with a short paragraph: which engagement metrics went with higher impressions this week. Be specific and grounded in the numbers. Say the sample is small, but still draw a directional conclusion.

### Post detail cards

One card per post, best to worst by impressions:
- A badge on the #1 post.
- Date and weekday.
- The hook in quotes.
- Six metric boxes: impressions, reactions, comments, reposts, saves (with rate %), sends (with rate %).
- Save and send boxes in blue when above the week's average.
- An "early snapshot" tag on posts under 2 hours old.
- A 2 to 4 sentence analysis of **why** the post performed the way it did.

The analysis considers: hook strength, format (text, image, carousel, video), topic fit with your audience, the CTA, save and send signals, and the posting day and time. Specific, not generic.

### Design

- Tailwind utility classes for layout and styling.
- Clean, minimal, easy to scan. White background, subtle gray borders on cards.
- A footer with the date the data was collected, which source was used (browser, export or pasted), and which metrics were N/A.

## Scheduled runs

The skill can run on a schedule (for example every Friday afternoon). On a scheduled run:
- Use the profile URL saved in `COMPANY-PROFILE.md` and the default Monday to Friday range. Don't ask questions.
- The browser path needs you to be signed in to LinkedIn already. If you're not, stop and leave a note saying so, instead of trying to sign in.
- Skip the data confirmation pause, but list in the footer anything that looked odd.

The output is the same full report however the skill is started.
