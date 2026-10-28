# Brand

Both files (PDF and deck) use one small set of colours and one font. Start from your own brand when you have it, and fall back to the neutral default below.

## Step 1: find your brand

Use the first that exists:

1. **Your context.** A brand or design section in your GTM context, `COMPANY-PROFILE.md`, or a brand file in the project (colours as hex codes, a logo file, a font name).
2. **Your website.** If you give a URL, open the homepage and read the main colours from the page styles (buttons, links, header background), the logo image and the heading font. Pick one accent colour and one dark colour. Show them to you before using them.
3. **Neither.** Use the neutral default. Don't ask twice in the same run.

Offer to save what you found to `COMPANY-PROFILE.md` under a "Brand" heading, so other skills reuse it.

Only use your own brand. Never put a client's or a prospect's logo or colours on the brief.

## Step 2: map it to the template

| Token | Default | Use |
|---|---|---|
| Accent (`primary`) | `#2F6FEB` | Section markers, stat figures, pills, bullets. Use sparingly. |
| Dark (`dark`) | `#111827` | Header band, headings, the deck title slide |
| Ink | `#374151` | Body text |
| Muted | `#6B7280` | Captions, labels, footer |
| Soft | `#F5F6F8` | Card and callout backgrounds |
| White | `#FFFFFF` | Page, cards, text on dark |

Font default: Inter, falling back to Helvetica Neue and Arial. If your brand font isn't installed, use the fallback rather than an odd substitute.

Contrast check: the accent must read clearly on white and on the dark band. If your brand colour is very light (pastel yellow, light grey), use your darker brand colour as the accent instead and say so.

## Layout patterns (already built into the script and template)

- Dark header band with your logo or company name, the company you are meeting in large type, and a pill with the call type.
- Big stat figures with a small label underneath, for deal value, headcount, days since last touch.
- White cards with soft corners for people. A soft callout box for open commitments.
- Lots of white space. If the content runs past 4 pages, cut content. Don't shrink type below 9pt.
- Footer on every PDF page: your company name (if known), the date, "Confidential".

## Deck

Start from `assets/slides-template.html`. Set the colours in the `:root` block at the top, put your logo or name in the title slide, and replace the placeholders. Keep the navigation script. Type stays large (the deck is glanced at during a live call): body 20px or more, headlines 40px or more. Dark title slide, light content slides, one idea per slide.
