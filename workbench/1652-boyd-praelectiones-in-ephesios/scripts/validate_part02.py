#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structural invariants of Boyd, Ephesians, Part 02."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATIN = ROOT / "parts/part-02-praelection-02-salutation-latin.txt"
ENGLISH = ROOT / "parts/part-02-praelection-02-salutation-english.md"
NOTES = ROOT / "apparatus/part-02-notes.md"
SOURCE_MAP = ROOT / "apparatus/part-02-source-map.tsv"
MARKER = re.compile(
    r"\[BSB bsb11059161 \| scan (\d+) \| Caput I p\. "
    r"(1|2|3|4 \(through Lecture II close\))\]"
)
EXPECTED = [
    ("43", "1"),
    ("44", "2"),
    ("45", "3"),
    ("46", "4 (through Lecture II close)"),
]
EXPECTED_IMAGE_HASHES = [
    "056cf287ccb1d26b65d68904cfc7d485bda7c236a7f75f00480d118df6176473",
    "a87a789c24eb165846b3567149740063d28bcd1d8a4b62fe97e1fd5f39e5124b",
    "83b6d562015f1308634e8fc61ca6c3e1119ca56dc31c4589a2d9d8fa67f9d61b",
    "1cdf4ed9d72d65f6e4f9f9f59ba59f7967118672cb490567b85e2347ee34ccb4",
]


def error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    texts: dict[Path, str] = {}
    for path in (LATIN, ENGLISH, NOTES, SOURCE_MAP):
        if not path.is_file():
            error(f"missing {path.relative_to(ROOT)}")
            errors += 1
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            error(f"{path.relative_to(ROOT)} is not UTF-8: {exc}")
            errors += 1
            continue
        texts[path] = text
        if not text.strip():
            error(f"{path.relative_to(ROOT)} is empty")
            errors += 1
        if "\r" in text or "\f" in text or "\ufffd" in text:
            error(f"{path.relative_to(ROOT)} contains a forbidden character")
            errors += 1
        if any(line.rstrip() != line for line in text.splitlines()):
            error(f"{path.relative_to(ROOT)} contains trailing whitespace")
            errors += 1
        if raw and not raw.endswith(b"\n"):
            error(f"{path.relative_to(ROOT)} lacks a final newline")
            errors += 1

    latin = texts.get(LATIN, "")
    english = texts.get(ENGLISH, "")
    latin_markers = MARKER.findall(latin)
    english_markers = MARKER.findall(english)
    if latin_markers != EXPECTED:
        error(f"Latin marker sequence is {latin_markers!r}, expected {EXPECTED!r}")
        errors += 1
    if english_markers != latin_markers:
        error("English marker sequence does not exactly match Latin")
        errors += 1

    for label, text, next_lecture in (
        ("Latin", latin, "Prælectio III"),
        ("English", english, "Lecture III"),
    ):
        if "AI-assisted" not in text or "unreviewed" not in text:
            error(f"{label} file lacks AI-assisted/unreviewed disclosure")
            errors += 1
        if text.count("[Marginalia:") != 17:
            error(f"{label} file does not contain exactly 17 marginal blocks")
            errors += 1
        if next_lecture not in text or "excluded" not in text:
            error(f"{label} file lacks the explicit next-lecture exclusion")
            errors += 1
        if re.search(r"\b(?:TODO|TBD|TRANSLATION PENDING)\b", text, re.I):
            error(f"{label} file contains an unfinished marker")
            errors += 1

    latin_tokens = len(re.findall(r"\b[\wÀ-ɏ]+\b", latin))
    english_tokens = len(re.findall(r"\b[\w'-]+\b", english))
    # Lecture II occupies three full pages and only the first ten lines of page
    # 4.  These floors are calibrated to that audited authorial boundary, not
    # to four complete folio pages.
    if latin and latin_tokens < 2700:
        error("Latin transcription is implausibly short for Lecture II")
        errors += 1
    if english and english_tokens < 3400:
        error("English translation is implausibly short for Lecture II")
        errors += 1

    if SOURCE_MAP in texts:
        rows = list(csv.DictReader(texts[SOURCE_MAP].splitlines(), delimiter="\t"))
        if [row.get("bsb_scan") for row in rows] != ["43", "44", "45", "46"]:
            error("part-02-source-map.tsv does not map scans 43–46 exactly once")
            errors += 1
        if rows and rows[-1].get("included_region") != "upper left column through line 9":
            error("source map does not state the partial-page scan 46 boundary")
            errors += 1
        hashes = [row.get("full_image_sha256", "") for row in rows]
        if hashes != EXPECTED_IMAGE_HASHES:
            error("part-02-source-map.tsv image hashes do not match the audited sources")
            errors += 1

    if errors:
        print(f"Part 02 validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(
        "Validated Boyd Ephesians Part 02: 4 paired markers, "
        f"{latin_tokens} Latin tokens, {english_tokens} English tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
