# Design plan — The OC Campus Collective

One static page. No build step, no CMS, no dates. Anyone can edit `index.html` in a text editor.

## Colors (from the flyer and logo)
| Token | Hex | Use |
|---|---|---|
| navy | #163b5e | headings, body text, dark panels |
| sun | #ffcf67 | the single accent: underline rules, button, sun mark |
| sky | #e9f1f8 | light panel background (flyer card tint) |
| haze | #a9c4e0 | swoosh, hairline borders |
| paper | #ffffff | page background |

Three-color rule: navy carries, sun accents, sky separates. No gradients, no shadows, no purple.

## Type
Montserrat only (flyer's geometric sans). 800 for display, 600 for subheads and buttons, 400 for body.
Scale: 15/17px body, 1.6 line-height, ~65ch measure. Display sizes 40–72px, line-height 1.05, tight tracking (-0.02em).
Sentence case everywhere. No tracked-out caps eyebrows. No single-word color accents in headlines.

## Layout
Left-aligned, asymmetric two-column rhythm on desktop, single column on phone.

```
┌───────────────────────────────────────────────┐
│ [logo]                          Email Ainsley │
├───────────────────────────────────────────────┤
│ Together, reaching every            ╲  ☀     │  hero: headline left,
│ Orange County campus                 ╲___    │  sun-over-horizon mark right
│ with the gospel.                              │
│ one sentence · two CTAs                       │
├───────────────────────────────────────────────┤
│ What we believe          | prose              │  label column / content column
│ ─── (sun rule)           |                    │
├───────────────────────────────────────────────┤
│ What we ask of partners  | 4-item list        │
├─────────────── navy band ─────────────────────┤
│ Up to $1,500 per new campus launch            │  the one loud moment
│ eligibility · approved uses (2-col list)      │
│ How to apply: email Ainsley with …            │
├───────────────────────────────────────────────┤
│ What you get             | 4 definition rows  │
├───────────────────────────────────────────────┤
│ Run by Cru and Trellis   | contacts           │
└───────────────────────────────────────────────┘
```

The memorable thing: the hero's sun rising over the swoosh horizon, drawn as SVG from the logo's own shapes, and the sun-yellow rule that recurs under every section heading. Nothing else decorates.

## Principles
- Real content, in the flyer's own words. No buzzwords.
- Structure encodes meaning: lists for lists, columns for two parallel sets, a band for the one offer.
- No cards. No icons-above-text. No numbered steps. No stat row. No scroll animations.
- Nothing time-bound on the page. Applying means emailing Ainsley.
- CTAs say what happens: "Email Ainsley about joining".

## Self-review against generic defaults
- Generic version of this brief: centered hero over stock photo, three icon cards for "offers", four cards for commitments, $1,500 stat tile, FAQ, footer. Rejected: replaced cards with a label/content two-column list layout; the offer is a band with a sentence, not a tile; no icons, no FAQ.
- Flyer's own habits (tracked caps headings, icon cards, check bullets) kept out; flyer's identity (colors, sun, swoosh, yellow underline, Montserrat) kept in.
