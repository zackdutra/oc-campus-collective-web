# The OC Campus Collective — website

One-page site for The OC Campus Collective, a network of churches and ministries reaching
Orange County college and high school campuses, run by Cru in partnership with Trellis.

Plain HTML and CSS. No build step, no framework, no dependencies. Edit `index.html` in any
text editor and push; Vercel redeploys from GitHub.

- `index.html` — the whole page
- `styles.css` — all styling; brand tokens at the top
- `assets/` — logo and favicon
- `sources/` — the flyer and logo the site was built from
- `DESIGN.md` — the design plan and the rules that keep it from looking templated
- `HANDOFF.md` — what Ainsley needs to confirm or supply, and where each item lives in the page

## Editing rules
- Nothing on the page is time-bound on purpose. Do not add events, dates, or "upcoming" anything.
- Applying for anything means emailing the Collective (Ainsley's address, worded as "us"). Keep it that way; there is no form to maintain.
- Colors and type come from the flyer. See `DESIGN.md` before changing them.

## Preview locally
```
python3 -m http.server 8765
```
then open http://localhost:8765/.
