#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structural invariants of Boyd, Ephesians, Part 01."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATIN = ROOT / "parts/part-01-praelection-01-preface-latin.txt"
ENGLISH = ROOT / "parts/part-01-praelection-01-preface-english.md"
SOURCE_MAP = ROOT / "apparatus/source-map.tsv"
MARKER = re.compile(
    r"\[BSB bsb11059161 \| scan (\d+) \| "
    r"Pr(?:æ|ae)fatio p\. (\[1\], unnumbered|\d+)\]"
)
EXPECTED = [(str(35), "[1], unnumbered"), *[(str(n + 34), str(n)) for n in range(2, 9)]]


def error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    texts: dict[Path, str] = {}
    for path in (LATIN, ENGLISH, SOURCE_MAP, ROOT / "README.md", ROOT / "apparatus/part-01-notes.md"):
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
            error(f"{path.relative_to(ROOT)} contains a forbidden control/replacement character")
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
    for label, text in (("Latin", latin), ("English", english)):
        if "AI-assisted" not in text or "unreviewed" not in text:
            error(f"{label} file lacks AI-assisted/unreviewed disclosure")
            errors += 1
        if text.count("[Marginalia:") < 20:
            error(f"{label} file has implausibly few marginal blocks")
            errors += 1
        if "AMEN." not in text:
            error(f"{label} file does not reach the lecture's explicit close")
            errors += 1
        if re.search(r"\b(?:TODO|TBD|TRANSLATION PENDING)\b", text, re.I):
            error(f"{label} file contains an unfinished marker")
            errors += 1

    latin_tokens = len(re.findall(r"\b[\wÀ-ɏ]+\b", latin))
    english_tokens = len(re.findall(r"\b[\w'-]+\b", english))
    if latin and latin_tokens < 7500:
        error("Latin transcription is implausibly short for eight folio pages")
        errors += 1
    if english and english_tokens < 9000:
        error("English translation is implausibly short for the complete lecture")
        errors += 1

    if SOURCE_MAP in texts:
        rows = list(csv.DictReader(texts[SOURCE_MAP].splitlines(), delimiter="\t"))
        if [row.get("bsb_scan") for row in rows] != [str(n) for n in range(35, 43)]:
            error("source-map.tsv does not map scans 35 through 42 exactly once")
            errors += 1
        hashes = [row.get("full_image_sha256", "") for row in rows]
        if any(not re.fullmatch(r"[0-9a-f]{64}", digest) for digest in hashes):
            error("source-map.tsv contains an invalid image SHA-256")
            errors += 1

    if errors:
        print(f"Part 01 validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(
        "Validated Boyd Ephesians Part 01: 8 paired markers, "
        f"{latin_tokens} Latin tokens, {english_tokens} English tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
