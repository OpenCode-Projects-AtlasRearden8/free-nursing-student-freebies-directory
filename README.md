# Free Nursing-Student Freebies Directory

A curated, hand-checked directory of **free resources for nursing students**:
flashcards, NCLEX-style practice questions, open-access journals, scholarships,
drug references, and simulation-lab-style learning. Built as plain static HTML
with no dependencies, no accounts, and no tracking.

**By Asdale Dynamics, LLC** - Dylan Asdale, RN. Plain English, step by step,
never condescending. Learn more at dylanasdale.github.io.

## What's inside

- `site/index.html` - the directory. Every entry lists:
  - **What it is** - a one-to-two-sentence plain-English description
  - **Cost** - what's actually free (and what isn't)
  - **Requirements** - account? email? software? enrollment?
  - **Link** - direct URL
  - **Verified** - date the entry was last hand-checked
- `docs/README.md` - maintainer guide: how entries are structured, how to add
  one, how to re-verify
- `tools/check_site.py` - lightweight checker (no dependencies) that validates
  the HTML structure and entry fields
- `LICENSE` - MIT, Copyright (c) 2026 Asdale Dynamics, LLC

## Categories

1. **Flashcards** - Anki, Quizlet, Brainscape, Cram
2. **NCLEX Practice** - question banks and prep that cost $0
3. **Journals** - open-access articles and searchable databases
4. **Scholarships** - real programs, no pay-to-apply sites
5. **Drug References** - NIH and other free clinical references
6. **Sim Labs** - free simulation and scenario-based learning

## Run it

```bash
# any of these works; no packages required
python3 -m http.server 8000 --directory site
# then open http://localhost:8000
```

Or just open `site/index.html` directly in a browser - the page has no
server-side requirements.

## Verify it

```bash
python3 tools/check_site.py
```

## Ground rules

- **Education only.** Never medical advice. Nothing here is for clinical
  decision-making; always follow your instructor, your facility's policy, and a
  licensed pharmacist or provider for real patients.
- **No ads.** We don't accept paid placements, affiliate links, or nursing
  program advertising. Discoverability is the only benefit listed resources get.
- **No secrets, no personal data.** The repo contains none, and asks you to
  contribute none.
- **Local-first.** Static files, runs offline from disk, no tracking.

## Contributing

PRs welcome. Read `docs/README.md` first - entries must include cost,
requirements, link, and a verified date, and may not include paywalled "free
trial" offers or nursing-program ads.

## License

MIT - see `LICENSE`. Copyright (c) 2026 Asdale Dynamics, LLC.
