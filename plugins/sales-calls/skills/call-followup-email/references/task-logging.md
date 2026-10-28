# Task logging

Optional. Only when you say yes. The goal: nothing you promised on the call gets lost, and you remember to chase what they promised.

## Where tasks go

Use the first that applies:

1. **Your task tool, if connected** (Notion database, Asana, ClickUp, Todoist, Trello, Linear or similar). Ask which list, project or database the first time, and offer to save the answer to `COMPANY-PROFILE.md` under "Call tasks". Fetch its fields before writing, so you use the right names and options.
2. **Your CRM's task feature,** if that is where you track work.
3. **A markdown list** in your working folder: `outputs/call-tasks.md`. Create it if it doesn't exist and add new tasks at the top.

## What becomes a task

- **One task per thing you committed to.** Title: `<Company or first name>: <action>`, for example "Acme: send proposal with both options".
- **Their commitments become one chase task for you:** `<Company>: chase decision on <topic>`, with their to-dos listed in the notes. Don't create tasks as if they belong to the prospect.
- **Conditional tasks say so** in the title: "Acme: book kickoff (if they pick the full migration)".

## Fields

| Field | Value |
|---|---|
| Title | As above |
| Status | To do (or your tool's first status) |
| Due | Only when a date was committed on the call. "By end of day" means the call date. Otherwise empty. Never invent a date. |
| Notes | The details needed to do the task, plus the call link if there is one |

Map these to whatever your tool calls them. If it has an owner field, set it to you.

## Before creating

1. Search the task tool or the markdown list for existing tasks with the same company, to avoid duplicates. Update instead of duplicating.
2. Show the task list in chat and wait for a yes.

## Markdown list format

```markdown
## Acme · call 2026-06-10

- [ ] Acme: send proposal with both options · due 2026-06-13
- [ ] Acme: chase decision on option and go-live date
  - Their to-dos: confirm option, share rough record count
```

## If writing fails

Still show the full task list in chat, so nothing is lost, and say which tool failed.
