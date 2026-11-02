# STATUS

## What was built

A curated, maintainable directory of free nursing-student resources, shipped as
a fully static site plus maintainer docs and an offline checker.

- `site/index.html` - the directory. 6 categories (flashcards, NCLEX-style
  practice, journals & articles, scholarships, drug references, sim labs),
  22 entries. Every entry carries the required fields: what it is, cost
  (including free-tier boundaries), requirements (account/download/etc.),
  https link, and a hand-verified date (Nov 2026). Filter buttons by category,
  live text/tag search, disclaimer banner, no external assets, no tracking.
- `docs/README.md` - maintainer guide: entry format, ground rules (genuinely
  free, education-only, no program ads/affiliates, no secrets or personal
  data), re-verification routine.
- `tools/check_site.py` - dependency-free Python checker validating entry
  fields, section/filter consistency, https links, verified dates, disclaimer
  and credit text, and tag balance.
- `README.md` - project README, credits Asdale Dynamics, LLC, ground rules
  stated up front, run + verify instructions.
- `LICENSE` - MIT, copyright line exactly:
  `Copyright (c) 2026 Asdale Dynamics, LLC`

## How to run it

```bash
python3 -m http.server 8000 --directory site
# open http://localhost:8000
```

Or open `site/index.html` directly in any browser - no server, packages, or
accounts needed.

## Verification results

- `python3 tools/check_site.py` -> OK: 22 entries, 6 sections, all required
  fields present (exit 0).
- Served with `python3 -m http.server 8137 --directory site` -> HTTP 200,
  29,315 bytes, 22 entry cards confirmed served.
- Inline JavaScript extracted and validated with `node --check` -> OK.
- Secret/personal-data scan across repo (api keys, tokens, passwords,
  private-key blocks) -> clean.
- No nursing-program ads, affiliate links, or sponsored placements anywhere.

## Known gaps

- Link checking (`tools/check_site.py`) is offline by design; live URL
  verification is a manual step (see docs/README.md routine).
- 22 entries is a solid start, not exhaustive; scholarships in particular
  should be re-verified every application season - deadlines shift and free
  tiers shrink.
- Free-tier terms for Quizlet/Drugs.com/Medscape can change without notice;
  the checker cannot detect that - flag it via issue if you spot drift.
- No screenshots or deep-linking into subpages of resources; entries link to
  category homepages.

## License & credit

MIT - see `LICENSE`. By Asdale Dynamics, LLC (Dylan Asdale, RN). Education
only - never medical advice; no ads, no affiliate links, no paid placements.
