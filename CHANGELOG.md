# Changelog

## 2026-09-22
- First build: one-page static site from the flyer and logo. Sections: hero, what we believe,
  what we ask of partners, launch grant, what you get, run by Cru and Trellis, footer.
- Design plan in `DESIGN.md`; handoff list for Ainsley in `HANDOFF.md`.
- CTAs speak as the organization ("Email us") instead of naming Ainsley.
- Full sun in the hero instead of a clipped one; matches the logo.
- Share tags: Open Graph, Twitter card, canonical, theme color, apple touch icon, and a
  1200x630 `assets/og.png`. Site URL in the tags is a placeholder until the domain is set.
- Hero sun redrawn to match the logo: half sun clipped along the swoosh, six tapered rays at
  the logo's angles, blue swoosh ending at the sun. SVG now scales by aspect ratio so no
  width crops it (the previous version lost its rays on wide monitors).
- `tools/gen_sun.py` generates the sun SVG; `tools/og-template.html` is the share-image source.
