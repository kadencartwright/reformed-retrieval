#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run lightweight structural checks over the published text set."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (
    "1549-06-26-calvin-to-socinus",
    "1549-07-25-socinus-to-calvin-context",
    "1549-12-07-calvin-to-socinus",
    "1555-06-05-response-to-socinus",
    "1561-11-13-baptism-improperly-administered",
)
REQUIRED = ("README.md", "latin.txt", "english.md")
EXPECTED_PAGES = {
    "1549-06-26-calvin-to-socinus": ("XIII", 307, 311),
    "1549-07-25-socinus-to-calvin-context": ("XIII", 337, 340),
    "1549-12-07-calvin-to-socinus": ("XIII", 484, 487),
    "1555-06-05-response-to-socinus": ("X/1", 160, 165),
    "1561-11-13-baptism-improperly-administered": ("X/1", 214, 215),
}
PAGE_MARKER = re.compile(r"\[CO (X/1|XIII), p\. (\d+)\]")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
LICENSE_CHECKS = {
    "LICENSE": ("MIT License", "Permission is hereby granted"),
    "LICENSES/CC0-1.0.txt": ("CC0 1.0 Universal", "Public License Fallback"),
    "LICENSING.md": (
        "`texts/*/english.md`",
        "No other repository file is covered by that CC0 dedication",
    ),
}
MIT_SPDX_PATHS = (
    "Makefile",
    "scripts/validate.py",
    ".github/workflows/validate.yml",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0

    for relative, required_phrases in LICENSE_CHECKS.items():
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing licensing file {relative}")
            errors += 1
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in text:
                fail(f"{relative} is missing required licensing phrase {phrase!r}")
                errors += 1

    for relative in MIT_SPDX_PATHS:
        path = ROOT / relative
        if not path.is_file() or "SPDX-License-Identifier: MIT" not in path.read_text(
            encoding="utf-8"
        ):
            fail(f"{relative} lacks an MIT SPDX identifier")
            errors += 1

    for slug in DOCUMENTS:
        directory = ROOT / "texts" / slug
        for name in REQUIRED:
            path = directory / name
            if not path.is_file():
                fail(f"missing {path.relative_to(ROOT)}")
                errors += 1
                continue

            raw = path.read_bytes()
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")
                errors += 1
                continue

            if not text.strip():
                fail(f"{path.relative_to(ROOT)} is empty")
                errors += 1
            if "\r" in text:
                fail(f"{path.relative_to(ROOT)} contains CR line endings")
                errors += 1
            if "\f" in text:
                fail(f"{path.relative_to(ROOT)} contains form-feed characters")
                errors += 1
            if "\ufffd" in text:
                fail(f"{path.relative_to(ROOT)} contains a Unicode replacement character")
                errors += 1
            if any(line.rstrip() != line for line in text.splitlines()):
                fail(f"{path.relative_to(ROOT)} contains trailing whitespace")
                errors += 1
            if raw and not raw.endswith(b"\n"):
                fail(f"{path.relative_to(ROOT)} has no final newline")
                errors += 1
            if re.search(r"\b(?:TODO|TBD|TRANSLATION PENDING)\b", text, re.I):
                fail(f"{path.relative_to(ROOT)} contains an unfinished marker")
                errors += 1

        latin = directory / "latin.txt"
        if latin.is_file():
            text = latin.read_text(encoding="utf-8")
            volume, first_page, last_page = EXPECTED_PAGES[slug]
            markers = [(match.group(1), int(match.group(2))) for match in PAGE_MARKER.finditer(text)]
            expected = [(volume, page) for page in range(first_page, last_page + 1)]
            if markers != expected:
                fail(
                    f"{latin.relative_to(ROOT)} has page markers {markers!r}; "
                    f"expected {expected!r}"
                )
                errors += 1
            if len(text.strip()) < 500:
                fail(f"{latin.relative_to(ROOT)} is implausibly short")
                errors += 1

        english = directory / "english.md"
        if english.is_file():
            text = english.read_text(encoding="utf-8")
            if not text.startswith("# "):
                fail(f"{english.relative_to(ROOT)} needs a title")
                errors += 1
            if len(text.strip()) < 500:
                fail(f"{english.relative_to(ROOT)} is implausibly short")
                errors += 1
            volume, first_page, last_page = EXPECTED_PAGES[slug]
            markers = [(match.group(1), int(match.group(2))) for match in PAGE_MARKER.finditer(text)]
            expected = [(volume, page) for page in range(first_page, last_page + 1)]
            if markers != expected:
                fail(
                    f"{english.relative_to(ROOT)} has page markers {markers!r}; "
                    f"expected {expected!r}"
                )
                errors += 1

        readme = directory / "README.md"
        if readme.is_file():
            readme_text = readme.read_text(encoding="utf-8")
            if "AI-assisted" not in readme_text:
                fail(f"{readme.relative_to(ROOT)} does not disclose AI-assisted status")
                errors += 1
            if "../../LICENSES/CC0-1.0.txt" not in readme_text:
                fail(f"{readme.relative_to(ROOT)} does not link the scoped CC0 text")
                errors += 1
            if "../../LICENSING.md" not in readme_text:
                fail(f"{readme.relative_to(ROOT)} does not link the licensing scope")
                errors += 1
            if "No CC0 dedication is" not in readme_text:
                fail(f"{readme.relative_to(ROOT)} does not exclude non-English files from CC0")
                errors += 1

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            linked = (markdown.parent / target).resolve()
            if not linked.exists():
                fail(
                    f"{markdown.relative_to(ROOT)} links to missing local target "
                    f"{raw_target!r}"
                )
                errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(DOCUMENTS)} document directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
