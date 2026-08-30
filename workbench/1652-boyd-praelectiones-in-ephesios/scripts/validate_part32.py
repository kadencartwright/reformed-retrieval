#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structural invariants of Boyd, Ephesians, Part 32."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATIN = ROOT / "parts/part-32-praelection-32-scriptural-objections-and-recapitulation-latin.txt"
ENGLISH = ROOT / "parts/part-32-praelection-32-scriptural-objections-and-recapitulation-english.md"
README = ROOT / "README.md"
MARKER = re.compile(
    r"\[BSB bsb11059161 \| scan (175|176|177|178|179) \| "
    r"De Prædestinatione p\. (131 \(from Prælectio XXXII opening\)|132|133|134|"
    r"135 \(through Prælectio XXXII close\))\]"
)
EXPECTED = [
    ("175", "131 (from Prælectio XXXII opening)"),
    ("176", "132"),
    ("177", "133"),
    ("178", "134"),
    ("179", "135 (through Prælectio XXXII close)"),
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

    expected_marginal_distribution = [5, 8, 9, 9, 3]
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
            "Prælectio XXXIII",
            ("ope instrumentorum AI", "nondum ab homine recognita"),
        ),
        ("English", english, "Lecture XXXIII", ("AI-assisted", "unreviewed")),
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
        "verbi ministerio vocantur,\n\n[Marginalia: Depulsio.]\n\n[BSB bsb11059161 | scan 176",
        "ipse suo Spiritu\n\n[Marginalia: 2. Membrum.]\n\n[BSB bsb11059161 | scan 177",
        "quinque adversantium\n\n[Marginalia: 1. Dictorum omnium",
        "quinque ipsorum objectiones diluimus.\n\n[Marginalia: 10.]\n\n[BSB bsb11059161 | scan 179",
    ]
    english_joins = [
        "called through the ministry of the word is\n\n[Marginalia: Rebuttal.]\n\n[BSB bsb11059161 | scan 176",
        "he himself by his Spirit\n\n[Marginalia: Part 2.]\n\n[BSB bsb11059161 | scan 177",
        "five arguments of the\n\n[Marginalia: 1. Recapitulation of everything said",
        "then five of their\nobjections.\n\n[Marginalia: 10.]\n\n[BSB bsb11059161 | scan 179",
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
    if latin and latin_tokens < 3750:
        error("Latin transcription is implausibly short for Lecture XXXII")
        errors += 1
    if english and english_tokens < 5200:
        error("English translation is implausibly short for Lecture XXXII")
        errors += 1

    for needle in (
        "| 32 | XXXII | 175–179 | 131–135 |",
        "part-32-praelection-32-scriptural-objections-and-recapitulation-latin.txt",
        "part-32-praelection-32-scriptural-objections-and-recapitulation-english.md",
        "validate_part32.py",
    ):
        if needle not in readme:
            error(f"README lacks required Part 32 entry: {needle}")
            errors += 1

    if errors:
        print(f"Part 32 validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(
        "Validated Boyd Ephesians Part 32: 5 paired markers, "
        f"34 paired marginal blocks, {latin_tokens} Latin tokens, "
        f"{english_tokens} English tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
