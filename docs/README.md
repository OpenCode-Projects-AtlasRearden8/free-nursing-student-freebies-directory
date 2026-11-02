# Maintainer Guide: Free Nursing-Student Freebies Directory

Everything you need to add, edit, and re-verify entries in `site/index.html`.
Written for people maintaining this by hand - no frameworks, no packages.

## Entry format

Every entry is an `<article class="entry">` inside the `<div class="grid">` of
its category section. These fields are **required** for every entry:

| Field | Where | Rule |
|---|---|---|
| What it is | `<li><b>What:</b> ...</li>` | 1 sentence, plain English, no jargon |
| Cost | `<li><b>Cost:</b> ...</li>` | Say exactly what is free and what isn't. If the free part is a tier, put "Free tier" and name the paid boundary |
| Requirements | `<li><b>Requirements:</b> ...</li>` | Account? email? download? enrollment? Say it |
| Link | `<a href="...">` in the `<h3>` and in the fields list | Direct URL to the resource, not a landing page with pop-ups |
| Verified | `<div class="verified">` header | Date of the most recent hand-check, month + year |

Optional extras:

- `data-tags="..."` attribute on the article - lowercase keywords used by the
  in-page search. Include aliases people actually search for.
- `.badge` inside the `<h3>` link - short label like "Free tier", "Open
  source", "NIH".
- A caveat in the verified line (e.g. "has ads", "deadline closes early in the
  year").

## Categories

Six fixed sections, each `<section id="..." data-category="...">`:

`flashcards`, `nclex`, `journals`, `scholarships`, `drugs`, `sims`

To add a new category you must update:

1. The `<section>` with a matching `data-category`
2. A filter `<button data-filter="...">` in the `.controls` nav
3. This guide's list above

## Ground rules for entries (non-negotiable)

1. **Genuinely free.** No "free trials", paywalled teases, or paid-only tools.
   A free tier is fine if studying is actually usable without paying.
2. **Education only, never medical advice.** No entries framed as guidance for
   real clinical decision-making; the disclaimer stays in place.
3. **No program ads, affiliate links, or sponsored placements.** If a site
   sells its own paid course, note it in the verified line - that's fine -
   but we never take payment for listing.
4. **No secrets or personal data.** Nothing in edits, issue links, or notes.
5. **Link checks by hand.** Open the link, confirm it lands where you say it
   does, and update the verified date even if nothing else changed.

## Re-verification routine (quarterly or each semester)

1. Open every link; fix or remove dead ones (note the removal in the commit
   message).
2. Re-read each Cost field - free tiers quietly shrink.
3. Update the `Verified:` line with the new month/year only for entries you
   actually checked.
4. Run the checker (below) and commit.

## Checker

```bash
python3 tools/check_site.py
```

Dependency-free Python that validates the page structure: required fields per
entry, matching `data-filter` buttons for every section, the disclaimer text,
and basic HTML tag balance. It does **not** fetch the web (by design - the
repo verifies offline); treat live link checking as the manual step above.

## Serving locally

```bash
python3 -m http.server 8000 --directory site
# open http://localhost:8000
```

The page also works opened directly as a file; the server is just nicer.
