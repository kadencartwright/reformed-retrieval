# Robert Boyd of Trochrig, *Prælectiones in Ephesios* (1652)

> **Working-edition notice:** This directory contains an AI-assisted,
> unreviewed diplomatic-normalized Latin transcription and an independent close
> English translation. Neither file is a reviewed or publication-ready edition.
> A qualified editor must compare both in full with the controlling facsimile.

## Work and edition

- **Author:** Robert Boyd of Trochrig (Robertus Bodius a Trochoregia,
  1578–1627)
- **Title:** *In Epistolam Pauli Apostoli ad Ephesios Prælectiones supra CC*
- **Edition used:** London, at the expense of the Stationers' Company, 1652
- **Form:** more than two hundred lectures on Ephesians, with analysis,
  exposition, doctrinal observations, commonplaces, questions, controversies,
  and four indexes
- **Publication status:** posthumous

## Controlling audited witness

The controlling witness is the Regensburg, Staatliche Bibliothek copy,
shelfmark `999/2Script.651`, digitized by the Bayerische Staatsbibliothek as
[`bsb11059161`](https://www.digitale-sammlungen.de/en/view/bsb11059161).
The [IIIF manifest](https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11059161/manifest)
contains 1,298 canvases and identifies the extent as fourteen preliminary
leaves, 1,236 numbered pages, and nine final leaves. Its persistent URN is
`urn:nbn:de:bvb:12-bsb11059161-3`; its BSB catalog ID is `BV019864617`.

The printed work is public-domain historical text. The supplied BSB digital
object carries the rights statement
[`No Copyright – Non-Commercial Use Only 1.0`](https://rightsstatements.org/vocab/NoC-NC/1.0/).
No page image or OCR derivative is redistributed here. The transcription and
metadata are working research materials; only the repository's path-scoped
English publication files under `texts/*/english.md` receive its CC0
dedication. This workbench English draft is therefore outside that dedication;
see the repository [licensing scope](../../LICENSING.md).

## Source map and first-unit boundary

The work's authorial preface is explicitly the first lecture:

| BSB scans | Printed preface pages | Printed structure | Unit decision |
|---|---:|---|---|
| 35–42 | unnumbered [1], then 2–8 | outer marginal label `Prælectio I`; heading `PRÆFATIO`; closes `AMEN.` | Part 01, complete |
| 43 onward | main-text p. 1 onward | `IN CAPUT PRIMUM`; outer marginal label `Prælectio secunda` | excluded |

The requested priority was the first complete lecture, with a coherent 15–20
page unit as fallback. Lecture I is complete in eight folio pages, so this
exact authorial boundary controls rather than adding an incomplete portion of
Lecture II. The page-level first/last text and captured full-image SHA-256
values are recorded in [`apparatus/source-map.tsv`](apparatus/source-map.tsv).
Detailed boundary, witness, convention, and uncertain-reading notes appear in
[`apparatus/part-01-notes.md`](apparatus/part-01-notes.md).

## Editorial method

Page images govern. BSB's layout-aware hOCR is used only as a finding and
collation aid. The Latin normalizes long `s`, ligatures, explicit
abbreviations, line-end divisions, and typographic `u/v`; it retains
substantive spelling, Greek, headings, numbered structures, citations, and
marginal annotations. Running heads, ornaments, signatures, catchwords,
column letters, and bare printed foliation are omitted from the prose.

Source markers have this exact form:

`[BSB bsb11059161 | scan 39 | Præfatio p. 5]`

The first preface page has no visible number and is marked `Præfatio p. [1],
unnumbered`. At page-crossing word or sentence boundaries the Latin joins
printer divisions and places the new marker before the complete continuation;
the English marker is aligned to the corresponding phrase. Substantive
marginal notes are linearized after the relevant passage in both files.

The English is a fresh, full translation of the paired Latin, not a summary.
No modern English version served as a wording source. Greek quotations are
translated in context while the Greek remains visible in the Latin file.

## Completed Part 01

Part 01 contains all of Lecture I, the preface to Ephesians, from BSB scan 35
through scan 42:

- [`parts/part-01-praelection-01-preface-latin.txt`](parts/part-01-praelection-01-preface-latin.txt)
- [`parts/part-01-praelection-01-preface-english.md`](parts/part-01-praelection-01-preface-english.md)

Its argument moves from the two mutually supporting theological tasks—biblical
exegesis and synthetic commonplaces—through a proposed course of theological
study, the rationale for beginning with Ephesians, the epistle's occasion and
contents, twelve principal theological loci, and the division of Ephesians
into a didactic first half and exhortatory second half. It ends by deriving two
consequences: doctrine precedes the works that are its fruits, and the doctrine
of grace energizes rather than discourages holy living.

## Validation

Run the work-local structural validator from the repository root:

```sh
python3 workbench/1652-boyd-praelectiones-in-ephesios/scripts/validate_part01.py
```

It checks UTF-8 and line hygiene, the exact eight-marker sequence and parity,
AI/unreviewed disclosures, minimum full-text size, marginal-block presence,
the explicit `AMEN.` close, and source-map scan/hash structure. Repository-wide
validation may also be run, but this new workbench unit deliberately does not
modify global ledgers, the publication manifest, or repository checksums.
