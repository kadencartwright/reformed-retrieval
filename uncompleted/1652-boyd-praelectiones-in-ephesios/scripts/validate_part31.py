#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structural invariants of Boyd, Ephesians, Part 31."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATIN = ROOT / "parts/part-31-praelection-31-errors-against-predestination-latin.txt"
ENGLISH = ROOT / "parts/part-31-praelection-31-errors-against-predestination-english.md"
README = ROOT / "README.md"
MARKER = re.compile(
    r"\[BSB bsb11059161 \| scan (171|172|173|174|175) \| "
    r"De Prædestinatione p\. (127 \(from Prælectio XXXI opening\)|"
    r"128|129|130|131 \(through Prælectio XXXI close\))\]"
)
EXPECTED = [
    ("171", "127 (from Prælectio XXXI opening)"),
    ("172", "128"),
    ("173", "129"),
    ("174", "130"),
    ("175", "131 (through Prælectio XXXI close)"),
]


def error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    texts: dict[Path, str] = {}
    for path in (LATIN, ENGLISH, README):
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
    readme = texts.get(README, "")
    latin_markers = MARKER.findall(latin)
    english_markers = MARKER.findall(english)
    if latin_markers != EXPECTED:
        error(f"Latin marker sequence is {latin_markers!r}, expected {EXPECTED!r}")
        errors += 1
    if english_markers != latin_markers:
        error("English marker sequence does not exactly match Latin")
        errors += 1

    expected_marginal_distribution = [3, 9, 9, 7, 6]
    for label, text in (("Latin", latin), ("English", english)):
        marker_positions = [match.start() for match in MARKER.finditer(text)]
        marker_positions.append(len(text))
        distribution = [
            text[start:end].count("[Marginalia:")
            for start, end in zip(marker_positions, marker_positions[1:])
        ]
        if distribution != expected_marginal_distribution:
            error(
                f"{label} per-scan marginal distribution is {distribution!r}, "
                f"expected {expected_marginal_distribution!r}"
            )
            errors += 1

    for label, text, next_lecture, disclosure in (
        (
            "Latin",
            latin,
            "Prælectio XXXII",
            ("ope instrumentorum AI", "nondum ab homine recognita"),
        ),
        ("English", english, "Lecture XXXII", ("AI-assisted", "unreviewed")),
    ):
        normalized = " ".join(text.split())
        if any(phrase not in normalized for phrase in disclosure):
            error(f"{label} file lacks AI-assisted/unreviewed disclosure")
            errors += 1
        if text.count("[Marginalia:") != 34:
            error(f"{label} file does not contain exactly 34 marginal blocks")
            errors += 1
        if next_lecture not in text or "excluded" not in text:
            error(f"{label} file lacks the explicit next-lecture exclusion")
            errors += 1
        if re.search(r"\b(?:TODO|TBD|TRANSLATION PENDING)\b", text, re.I):
            error(f"{label} file contains an unfinished marker")
            errors += 1

    latin_joins = [
        "ab omni\n\n[BSB bsb11059161 | scan 172",
        "conditionis artificem\n\n[Marginalia: Error 3. 1.]\n\n[BSB bsb11059161 | scan 173",
        "alii divinam\nprovidentiam\n\n[Marginalia: Membrum posterius.]\n\n[BSB bsb11059161 | scan 174",
        "opinio incidit in\n\n[Marginalia: Error 6.]\n\n[BSB bsb11059161 | scan 175",
    ]
    english_joins = [
        "every stain of\n\n[BSB bsb11059161 | scan 172",
        "make it the artisan\n\n[Marginalia: Error 3. 1.]\n\n[BSB bsb11059161 | scan 173",
        "others divine\n\n[Marginalia: The latter part.]\n\n[BSB bsb11059161 | scan 174",
        "same opinion falls into\n\n[Marginalia: Error 6.]\n\n[BSB bsb11059161 | scan 175",
    ]
    for label, text, joins in (
        ("Latin", latin, latin_joins),
        ("English", english, english_joins),
    ):
        for join in joins:
            if join not in text:
                error(f"{label} file lacks an audited cross-page join: {join!r}")
                errors += 1

    latin_tokens = len(re.findall(r"\b[\wÀ-ɏ]+\b", latin))
    english_tokens = len(re.findall(r"\b[\w'-]+\b", english))
    if latin and latin_tokens < 4000:
        error("Latin transcription is implausibly short for Lecture XXXI")
        errors += 1
    if english and english_tokens < 5200:
        error("English translation is implausibly short for Lecture XXXI")
        errors += 1

    for needle in (
        "| 31 | XXXI | 171–175 | 127–131 |",
        "part-31-praelection-31-errors-against-predestination-latin.txt",
        "part-31-praelection-31-errors-against-predestination-english.md",
        "validate_part31.py",
    ):
        if needle not in readme:
            error(f"README lacks required Part 31 entry: {needle}")
            errors += 1

    if errors:
        print(f"Part 31 validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(
        "Validated Boyd Ephesians Part 31: 5 paired markers, "
        f"34 paired marginal blocks, {latin_tokens} Latin tokens, "
        f"{english_tokens} English tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
