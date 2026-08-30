#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structural invariants of Boyd, Ephesians, Part 33."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATIN = ROOT / "parts/part-33-praelection-33-resumption-faith-and-charity-latin.txt"
ENGLISH = ROOT / "parts/part-33-praelection-33-resumption-faith-and-charity-english.md"
README = ROOT / "README.md"
MARKER = re.compile(
    r"\[BSB bsb11059161 \| scan (179|180|181|182|183|184) \| "
    r"(De Prædestinatione p\. 135 \(from Prælectio XXXIII opening\)|"
    r"Caput I p\. (?:136|137|138|139|140 \(through Lecture XXXIII close\)))\]"
)
EXPECTED = [
    ("179", "De Prædestinatione p. 135 (from Prælectio XXXIII opening)"),
    ("180", "Caput I p. 136"),
    ("181", "Caput I p. 137"),
    ("182", "Caput I p. 138"),
    ("183", "Caput I p. 139"),
    ("184", "Caput I p. 140 (through Lecture XXXIII close)"),
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

    expected_marginal_distribution = [2, 7, 6, 10, 7, 0]
    for label, text in (("Latin", latin), ("English", english)):
        positions = [match.start() for match in MARKER.finditer(text)] + [len(text)]
        distribution = [
            text[start:end].count("[Marginalia:")
            for start, end in zip(positions, positions[1:])
        ]
        if distribution != expected_marginal_distribution:
            error(
                f"{label} per-scan marginal distribution is {distribution!r}, "
                f"expected {expected_marginal_distribution!r}"
            )
            errors += 1

    for label, text, disclosure, close, next_boundary in (
        (
            "Latin",
            latin,
            ("ope instrumentorum AI", "nondum ab homine recognita"),
            "fascem perferendum ac sustinendum",
            "Hinc jam secundo loco perpendendum venit Charitatis objectum",
        ),
        (
            "English",
            english,
            ("AI-assisted", "unreviewed"),
            "to carry and sustain the burden",
            "Here now in the second place the object of love must be considered",
        ),
    ):
        normalized = " ".join(text.split())
        if any(phrase not in normalized for phrase in disclosure):
            error(f"{label} file lacks AI-assisted/unreviewed disclosure")
            errors += 1
        if text.count("[Marginalia:") != 32:
            error(f"{label} file does not contain exactly 32 marginal blocks")
            errors += 1
        if close not in normalized:
            error(f"{label} file lacks the audited Lecture XXXIII close")
            errors += 1
        if next_boundary not in normalized or "excluded" not in text:
            error(f"{label} file lacks the explicit next-lecture exclusion")
            errors += 1
        if re.search(r"\b(?:TODO|TBD|TRANSLATION PENDING)\b", text, re.I):
            error(f"{label} file contains an unfinished marker")
            errors += 1

    joins = (
        (
            "Latin",
            latin,
            (
                "in Evangelio sibi oblatam, &\n\n[BSB bsb11059161 | scan 180",
                "ipsis Ephesiis eo\n\n[BSB bsb11059161 | scan 181",
                "Christianæ currus,\n\n[BSB bsb11059161 | scan 182",
                "ipsâ fide, quâ de\n\n[BSB bsb11059161 | scan 183",
                "apprehendas, jam\n\n[Marginalia: Corollarium. Prioris illius similis illustratio.]\n\n[BSB bsb11059161 | scan 184",
            ),
        ),
        (
            "English",
            english,
            (
                "in the gospel and\n\n[BSB bsb11059161 | scan 180",
                "how much more\n\n[BSB bsb11059161 | scan 181",
                "continually drawn,\n\n[BSB bsb11059161 | scan 182",
                "faith about which we are\n\n[BSB bsb11059161 | scan 183",
                "have the\n\n[Marginalia: Corollary. An illustration of the former comparison.]\n\n[BSB bsb11059161 | scan 184",
            ),
        ),
    )
    for label, text, expected_joins in joins:
        for join in expected_joins:
            if join not in text:
                error(f"{label} file lacks an audited cross-page join: {join!r}")
                errors += 1

    latin_tokens = len(re.findall(r"\b[\wÀ-ɏ]+\b", latin))
    english_tokens = len(re.findall(r"\b[\w'-]+\b", english))
    if latin and latin_tokens < 4000:
        error("Latin transcription is implausibly short for Lecture XXXIII")
        errors += 1
    if english and english_tokens < 5500:
        error("English translation is implausibly short for Lecture XXXIII")
        errors += 1

    for needle in (
        "| 33 | XXXIII | 179–184 | 135–140 |",
        "part-33-praelection-33-resumption-faith-and-charity-latin.txt",
        "part-33-praelection-33-resumption-faith-and-charity-english.md",
        "validate_part33.py",
    ):
        if needle not in readme:
            error(f"README lacks required Part 33 entry: {needle}")
            errors += 1

    if errors:
        print(f"Part 33 validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(
        "Validated Boyd Ephesians Part 33: 6 paired markers, "
        f"32 paired marginal blocks, {latin_tokens} Latin tokens, "
        f"{english_tokens} English tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
