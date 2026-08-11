# Reformed Retrieval

[![Validate texts](https://github.com/kadencartwright/reformed-retrieval/actions/workflows/validate.yml/badge.svg)](https://github.com/kadencartwright/reformed-retrieval/actions/workflows/validate.yml)

Open, source-linked transcriptions and English translations of difficult-to-find
Reformed primary texts.

The repository currently presents **67 source-linked document editions**. The
collection includes 21 independent works, prefaces, and letters, plus a
complete edition set for the **46-item *consilia* corpus** printed at CO X/1
153–266: 32 Latin-form witnesses and 14 French-form witnesses. One incoming
letter from Laelius Socinus is supplied as context; collaborative,
represented-author, translated, contextual, and doubtfully attributed
witnesses are identified as such rather than silently treated as ordinary
sole-authored Calvin texts.

The independent works, prefaces, and correspondence are:

| Date | Author(s) | Document | Latin edition |
|---|---|---|---|
| 1531-03-06 | John Calvin | [Preface to Duchemin's *Antapologia*](texts/1531-preface-duchemin-antapologia/) | CO IX, 785–786 |
| 1537 | Farel, Calvin, and Viret; four endorsers | [*Confessio de Trinitate* concerning Caroli](texts/1537-confession-trinity-caroli/) | CO IX, 703–710 |
| 1537 | Farel, Calvin, Viret; endorsed by Bucer and Capito | [*Confessio fidei de Eucharistia*](texts/1537-confession-faith-eucharist/) | CO IX, 711–712 |
| 1541-01-01 | John Calvin | [*Epinicion Christo cantatum*](texts/1541-01-01-epinicion-christo-cantatum/) | CO V, 421–428 |
| c. 1544 | John Calvin | [Fragment of an apologetic preface for the *Institutes*](texts/1544-fragment-apologetic-preface-institutes/) | CO IX, 841–846 |
| 1547-10-01 | John Calvin | [Preface to Bucer's second Regensburg proceedings](texts/1547-preface-bucer-acta-ratisbonensia/) | CO IX, 851–854 |
| 1549-06-26 | John Calvin | [Letter 1211 to Heinrich Bullinger](texts/1549-06-26-calvin-to-bullinger/) | CO XIII, 305–307 |
| 1549-06-26 | John Calvin | [Letter 1212 to Laelius Socinus](texts/1549-06-26-calvin-to-socinus/) | CO XIII, 307–311 |
| 1549-07-25 | Laelius Socinus | [Letter 1231 to John Calvin (context)](texts/1549-07-25-socinus-to-calvin-context/) | CO XIII, 337–340 |
| 1549-12-07 | John Calvin | [Letter 1323 to Laelius Socinus](texts/1549-12-07-calvin-to-socinus/) | CO XIII, 484–487 |
| 1549-12-07 | John Calvin | [Letter 1324 to Heinrich Bullinger](texts/1549-12-07-calvin-to-bullinger/) | CO XIII, 488–490 |
| late 1555 | John Calvin | [Letter 2372 to Andrzej Trzecieski](texts/1555-12-calvin-to-trzecieski/) | CO XV, 910–912 |
| late 1555 | John Calvin | [Letter 2373 to Spytek Jordan](texts/1555-12-calvin-to-spytek-jordan/) | CO XV, 912–913 |
| late 1555 | John Calvin | [Letter 2373 bis to Francis Lismanino](texts/1555-12-calvin-to-lismanino/) | CO XV, 913–914 |
| 1558 | John Calvin | [*Ad quaestiones Georgii Blandratae responsum*](texts/1558-response-to-biandrata/) | CO IX, 325–332 |
| 1560-06-09 | Calvin for the Genevan pastors and teachers | [First response concerning Stancaro and Christ's mediation](texts/1560-response-stancaro-christ-mediator/) | CO IX, 337–342 |
| 1561 | Calvin and the Genevan ministers | [Second response concerning Stancaro and Christ's mediation](texts/1561-ministers-response-stancaro-mediation/) | CO IX, 349–358 |
| 1562 | John Calvin | [*Responsio ad Balduini convicia*](texts/1562-response-to-baudouin-invectives/) | CO IX, 565–580 |
| 1563 | John Calvin | [*Brevis admonitio ad fratres Polonos*](texts/1563-brevis-admonitio-polish-brethren/) | CO IX, 633–638 |
| 1563-04-30 | John Calvin | [Letter confirming the Polish admonition](texts/1563-epistola-confirming-polish-admonition/) | CO IX, 645–650 |
| 1563 | John Calvin | [Preface to Beza's book against Baudouin](texts/1563-preface-beza-against-balduin/) | CO IX, 859–862 |

The exhaustive [46-row *consilia* table](research/calvin-no-public-domain-english.md#the-consilia-or-ecclesiastical-advice)
links every completed edition and records whether the printed source is
authorial Latin or French, a historical translation from French, corporate or
represented speech, contextual material by another author, or of doubtful
attribution.

These documents were selected after a bibliographic audit did not locate a
complete, reusable public-domain English translation. That is a report of the
search result, not proof that no translation has ever circulated. The
consolidated, source-linked [Calvin translation-gap
inventory](research/calvin-no-public-domain-english.md) records the much larger
queue, modern copyrighted coverage, public-domain false positives, attribution
issues, and corpus-level work still required. The 1549 Socinus letter is
included as indispensable context for Calvin's replies; it is not attributed
to Calvin. The two 1537 confessions and the 1560–61 corporate responses are
likewise identified by their actual collective settings.

Each document directory contains:

- `latin.txt` or `french.txt` — one normalized source-language transcription
  with printed-page markers;
- `english.md` — a new English translation made directly from that source
  witness; and
- `README.md` — work identity, witness, editorial policy, and known limits.

## Status

These are AI-assisted working editions checked against page images. They are
designed to make the sources inspectable and reusable, but they have not yet
received independent specialist review. Quote the source edition when wording
is decisive, and report suspected errors through an issue or pull request.

No wording from a copyrighted modern translation was used in producing these
translations. In particular, no text from Mary D. Beaty and Benjamin Wirt
Farley's 1991 *Calvin's Ecclesiastical Advice* was used.

Run `make check` to verify document completeness, UTF-8 cleanliness, and the
expected printed-page marker sequence. The same check runs in GitHub Actions.
Run `sha256sum -c MANIFEST.sha256` to verify the canonical Latin, French, and
English files byte for byte.

## Source witnesses

The Latin and French source transcriptions are taken from *Ioannis Calvini
opera quae supersunt omnia*, edited by Wilhelm Baum, Eduard Cunitz, and Eduard
Reuss, in the *Corpus Reformatorum*.
The University of Geneva provides public scans through its
[complete Calvin collection](https://archive-ouverte.unige.ch/unige:650).
Exact volume links and page locators appear in each document directory and in
[`sources/README.md`](sources/README.md).

## Editorial conventions

- Printer line-end hyphenation and page-driven line wrapping are removed.
- Long `s` and obvious OCR artifacts are normalized.
- The nineteenth-century edition's Latin or historical French spelling and
  punctuation are otherwise retained unless a documented correction is
  necessary.
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
