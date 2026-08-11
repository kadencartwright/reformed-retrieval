# Reformed Retrieval

[![Validate texts](https://github.com/kadencartwright/reformed-retrieval/actions/workflows/validate.yml/badge.svg)](https://github.com/kadencartwright/reformed-retrieval/actions/workflows/validate.yml)

Open, source-linked transcriptions and English translations of difficult-to-find
Reformed primary texts.

The first release presents five documents surrounding John Calvin's exchanges
with Laelius Socinus and Calvin's judgments about baptism:

| Date | Author | Document | Latin edition |
|---|---|---|---|
| 1549-06-26 | John Calvin | [Letter 1212 to Laelius Socinus](texts/1549-06-26-calvin-to-socinus/) | CO XIII, 307–311 |
| 1549-07-25 | Laelius Socinus | [Letter 1231 to John Calvin (context)](texts/1549-07-25-socinus-to-calvin-context/) | CO XIII, 337–340 |
| 1549-12-07 | John Calvin | [Letter 1323 to Laelius Socinus](texts/1549-12-07-calvin-to-socinus/) | CO XIII, 484–487 |
| 1555-06-05 | John Calvin | [*Responsio ad aliquot Laelii Socini Senensis quaestiones*](texts/1555-06-05-response-to-socinus/) | CO X/1, 160–165 |
| 1561-11-13 | John Calvin | [*Ad baptismum minus legitime administratum*](texts/1561-11-13-baptism-improperly-administered/) | CO X/1, 214–215 |

These documents were selected after a bibliographic audit did not locate a
complete, reusable public-domain English translation. That is a report of the
search result, not proof that no translation has ever circulated. The 1549
Socinus letter is included as the indispensable context for Calvin's replies;
it is not attributed to Calvin.

Each document directory contains:

- `latin.txt` — a normalized transcription with printed-page markers;
- `english.md` — a new English translation made directly from the Latin; and
- `README.md` — work identity, witness, editorial policy, and known limits.

## Status

These are AI-assisted working editions checked against page images. They are
designed to make the sources inspectable and reusable, but they have not yet
received independent specialist review. Quote the Latin edition when wording is
decisive, and report suspected errors through an issue or pull request.

No text from Mary D. Beaty and Benjamin Wirt Farley's copyrighted 1991
translation, *Calvin's Ecclesiastical Advice*, was used in producing these
translations.

Run `make check` to verify document completeness, UTF-8 cleanliness, and the
expected printed-page marker sequence. The same check runs in GitHub Actions.
Run `sha256sum -c MANIFEST.sha256` to verify the ten canonical Latin and
English files byte for byte.

## Source witnesses

The Latin is taken from *Ioannis Calvini opera quae supersunt omnia*, edited by
Wilhelm Baum, Eduard Cunitz, and Eduard Reuss, in the *Corpus Reformatorum*.
The University of Geneva provides public scans through its
[complete Calvin collection](https://archive-ouverte.unige.ch/unige:650).
Exact volume links and page locators appear in each document directory and in
[`sources/README.md`](sources/README.md).

## Editorial conventions

- Printer line-end hyphenation and page-driven line wrapping are removed.
- Long `s` and obvious OCR artifacts are normalized.
- The nineteenth-century edition's Latin spelling and punctuation are otherwise
  retained unless a documented correction is necessary.
- `[CO …, p. …]` marks the beginning of each printed page.
- Editorial headings and apparatus are identified rather than silently treated
  as Calvin's or Socinus's words.
- Words supplied for intelligible English appear in brackets only when the
  addition affects interpretation.

See [`TRANSLATION_POLICY.md`](TRANSLATION_POLICY.md) for the full policy.

## Licensing

This is a mixed-license repository:

- the platform software and supporting configuration are licensed under the
  [MIT License](LICENSE);
- only project-authored content in `texts/*/english.md` is dedicated under
  [CC0 1.0 Universal](LICENSES/CC0-1.0.txt); and
- the underlying historical works and nineteenth-century editions are public
  domain independently of these repository licenses.

Normalized source transcriptions, document READMEs, research notes, metadata,
manifests, and editorial policies are not included in the CC0 dedication. See
the authoritative path-based [licensing statement](LICENSING.md) for the exact
scope.

Scholarly citation is strongly encouraged so readers can inspect the source
witness and revision history.
