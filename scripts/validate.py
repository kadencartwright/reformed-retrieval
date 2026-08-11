#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run lightweight structural checks over the published text set."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXTS = ROOT / "texts"
DOCUMENTS = tuple(
    sorted(path.name for path in TEXTS.iterdir() if path.is_dir() and not path.name.startswith("."))
)
REQUIRED_COMMON = ("README.md", "english.md")
SOURCE_NAMES = ("latin.txt", "french.txt")
PAGE_MARKER = re.compile(r"\[CO ([IVXLCDM]+(?:/\d+)?), p\. (\d+)\]")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MANIFEST_LINE = re.compile(
    r"^[0-9a-f]{64}  (texts/[^/]+/(?:latin\.txt|french\.txt|english\.md))$"
)
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
        source_files = [directory / name for name in SOURCE_NAMES if (directory / name).is_file()]
        if len(source_files) != 1:
            found = [path.name for path in source_files]
            fail(
                f"{directory.relative_to(ROOT)} must contain exactly one normalized "
                f"source file ({', '.join(SOURCE_NAMES)}); found {found!r}"
            )
            errors += 1

        required = (*REQUIRED_COMMON, *(path.name for path in source_files))
        for name in required:
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

        source_markers: list[tuple[str, int]] = []
        if len(source_files) == 1:
            source = source_files[0]
            text = source.read_text(encoding="utf-8")
            source_markers = [
                (match.group(1), int(match.group(2))) for match in PAGE_MARKER.finditer(text)
            ]
            if not source_markers:
                fail(f"{source.relative_to(ROOT)} has no CO page markers")
                errors += 1
            elif len({volume for volume, _ in source_markers}) != 1:
                fail(f"{source.relative_to(ROOT)} mixes CO volumes in its page markers")
                errors += 1
            elif [page for _, page in source_markers] != list(
                range(source_markers[0][1], source_markers[-1][1] + 1)
            ):
                fail(f"{source.relative_to(ROOT)} has non-consecutive CO page markers")
                errors += 1
            if len(text.strip()) < 500:
                fail(f"{source.relative_to(ROOT)} is implausibly short")
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
            markers = [(match.group(1), int(match.group(2))) for match in PAGE_MARKER.finditer(text)]
            if markers != source_markers:
                fail(
                    f"{english.relative_to(ROOT)} has page markers {markers!r}; "
                    f"expected the source sequence {source_markers!r}"
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

    manifest = ROOT / "MANIFEST.sha256"
    if manifest.is_file():
        listed = {
            match.group(1)
            for line in manifest.read_text(encoding="utf-8").splitlines()
            if (match := MANIFEST_LINE.match(line))
        }
        expected = {
            str(path.relative_to(ROOT))
            for slug in DOCUMENTS
            for name in (*SOURCE_NAMES, "english.md")
            if (path := TEXTS / slug / name).is_file()
        }
        if listed != expected:
            missing = sorted(expected - listed)
            stale = sorted(listed - expected)
            if missing:
                fail(f"MANIFEST.sha256 is missing canonical files: {missing!r}")
            if stale:
                fail(f"MANIFEST.sha256 lists absent canonical files: {stale!r}")
            errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(DOCUMENTS)} document directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
