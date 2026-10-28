# Proposal structure

## Style rules (hard)

- **No intro paragraph after a heading, ever.** A section opens with bullets, a table, or the content itself.
- **Facts and asks never mixed.** "Where you are" lists what they have and do today. "What you asked for" lists what they want. Then one boxed sentence: the goal, stated as what the work does for them. No internal role names in the goal.
- **Only lines that carry logic or core data survive.** Cut anything decorative, any restated context, any "we are passionate about".
- **No extra pages, no dead space.** Merge sections. Use two-column bullet lists when a page would otherwise be half empty.
- Plain language. No em dashes or double dashes. Ranges with "to".

## Proposal (3 to 5 pages)

1. **Cover:** your logo or company name, a title that names the client ("Sales onboarding proposal for Acme"), a one-line subtitle, then Prepared for (role and company), Prepared by, Date.
2. **The situation:**
   - Where you are (bullets)
   - What you asked for (bullets)
   - The goal (boxed, one sentence)
   - How the work works (bullets): who delivers it, how practical or hands-on it is, what is customised, delivery mode, what support is included, what you need from them (and what you don't)
   - Proof box, only with cleared items: client names, results, a public rating or review link the user confirmed
3. **Options:**
   - Summary table first: option, what's included, time or sessions, support, price (and second currency if used)
   - Then one compact block per option, one bullet each where possible
   - Mark the recommended option if you want to recommend one
4. **Add-ons and next steps:**
   - Add-ons with their logic in two or three bullets
   - Next steps: pick an option, then format and dates are proposed; any limits (session length, timeline window, availability)
   - If customisation is on offer, a box at the end: "If you choose a customised option, I'll need:" with the list

No separate "format and dates" section. Fold it into next steps: dates are proposed after they pick an option.

## Detailed scope (optional, held back)

For work that needs a detailed plan (session by session, phase by phase, deliverable by deliverable):

- Build it as a separate document and save it. Don't attach it to the first email.
- The proposal says the detailed plan follows once they pick a direction. It never refers to "the accompanying document".
- Page 1: a table of what each option includes (modules or phases against options, with hours and support), then a customisation box. Then each module or phase, two columns where needed.
- Content comes from your standard material in context (your methodology, standard modules, past plans in the folder). The call sets the size and the boundaries. Custom modules only when sold.

## Option patterns

- **Two axes.** Most service ladders vary on how much (scope, hours, modules, deliverables) and how tailored (standard, customised, customised per team or per unit). Three options usually sit on these axes: a lighter standard option, a fuller option, and a tailored option.
- **Per-team or per-unit options** come as a symmetric pair when used (core per team, full per team): same logic, same structure, a cap stated ("the price covers up to 3 teams").
- **Per-team logic** to state in both the proposal and the email: a shared first part for everyone, then separate tracks, deeper for the teams they choose and lighter for the rest. Fewer tracks than teams is deliberate: the best result at a friendlier price than full separation.
- **Add-ons:** state the honest difference. A responsive add-on (extra support hours, office hours, reviews) needs no preparation, so it costs less than a prepared one. Say when an add-on pairs with a shared option as the lower-priced alternative to a per-team option.
- **Support** scales with the size of the option: more Q&A or check-in time for bigger options. Teaching or delivery time and support time are listed separately.

## Design

Use `assets/proposal-template.html`: your brand colours and fonts in the `:root` block (or the neutral default), your company name and page number in the footer. A4. Filenames `YYYY-MM-DD-<client>-proposal.*` and `YYYY-MM-DD-<client>-scope.*`.
