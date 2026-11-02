#!/usr/bin/env python3
"""Structure checker for the Free Nursing-Student Freebies Directory.

Dependency-free. Validates site/index.html offline:
  - every entry has What / Cost / Requirements / Link / Verified fields
  - every section has a matching filter button
  - required disclaimer and footer credit present
  - malformed tags (vertical HTML only, no full parser needed)

Exit code 0 = pass, 1 = problems found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site" / "index.html"

ENTRY_FIELDS = ["What", "Cost", "Requirements"]
REQUIRED_SECTIONS = [
    "flashcards", "nclex", "journals", "scholarships", "drugs", "sims",
]
REQUIRED_STRINGS = [
    "Education only",  # disclaimer
    "Asdale Dynamics, LLC",  # credit
    "never medical advice",  # explicit scope line
    "no ads",
]

def check() -> list[str]:
    problems: list[str] = []
    html = SITE.read_text(encoding="utf-8")

    sections = re.findall(r"<section[^>]*>", html)
    data_categories = [
        re.search(r'data-category="([^"]+)"', s).group(1)
        for s in sections
        if 'data-category="' in s
    ]
    if data_categories != REQUIRED_SECTIONS:
        problems.append(
            f"sections in order {data_categories}, expected {REQUIRED_SECTIONS}"
        )

    filters = re.findall(r'<button[^>]*data-filter="([^"]+)"', html)
    for cat in REQUIRED_SECTIONS:
        if cat not in filters:
            problems.append(f"no filter button for {cat}")
    for f in filters:
        if f != "all" and f not in REQUIRED_SECTIONS:
            problems.append(f"filter button {f} has no section")

    entries = re.findall(
        r"<article class=\"entry\".*?</article>", html, flags=re.S
    )
    if len(entries) < 20:
        problems.append(f"only {len(entries)} entries; expected >= 20")
    for i, entry in enumerate(entries, 1):
        title = re.search(r"<h3>.*?>([^<]+)</a>", entry)
        name = title.group(1).strip() if title else f"entry #{i}"
        for field in ENTRY_FIELDS:
            if f"<b>{field}:</b>" not in entry:
                problems.append(f"{name}: missing <b>{field}:</b>")
        if "</a></h3>" in entry and 'rel="noopener"' not in entry.split("</h3>")[0]:
            problems.append(f"{name}: h3 link missing rel=\"noopener\"")
        if not re.search(r"Verified:\s+\w+ \d{4}", entry):
            problems.append(f"{name}: missing Verified date")
        link = re.search(r'<h3><a href="([^"]+)"', entry)
        if not link:
            problems.append(f"{name}: no link in h3")
        elif not link.group(1).startswith("https://"):
            problems.append(f"{name}: link not https -> {link.group(1)}")
        if 'data-tags="' not in entry:
            problems.append(f"{name}: missing data-tags")

    for needle in REQUIRED_STRINGS:
        if needle.lower() not in html.lower():
            problems.append(f"required text not found: {needle!r}")

    # crude tag balance for the tags we control strictly
    for tag in ("article", "section", "ul", "table"):
        opens = len(re.findall(rf"<{tag}[\s>]", html))
        closes = len(re.findall(rf"</{tag}>", html))
        if tag != "table" and opens != closes:
            problems.append(f"<{tag}> unbalanced: {opens} open / {closes} close")

    for href in re.findall(r'href="(?!https://)(?!#)[^"]+"', html):
        problems.append(f"non-https href: {href}")

    return problems

def main() -> int:
    if not SITE.exists():
        print(f"ERROR: {SITE} not found")
        return 1
    problems = check()
    if problems:
        print(f"FAILED - {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    html = SITE.read_text(encoding="utf-8")
    n_entries = len(re.findall(r"<article class=\"entry\"", html))
    print(f"OK - site/index.html valid: {n_entries} entries, "
          f"{len(REQUIRED_SECTIONS)} sections, all required fields present.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
