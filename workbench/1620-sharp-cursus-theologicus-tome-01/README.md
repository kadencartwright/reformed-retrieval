# John Sharp, *Cursus theologicus*, Tome I (1620)

> **Working-edition notice:** This directory begins an AI-assisted,
> independently unreviewed transcription and English translation. It is not a
> publication-ready critical edition. The page images, not OCR, control the
> text.

## Work and fixed edition

- **Author:** John Sharp (Johannes Scharpius; 1572?–1648?)
- **Title:** *Cursus theologicus, in quo controversiae omnes de fidei
  dogmatibus, hoc seculo exagitatae, nominatim inter nos & Pontificios,
  pertractantur; et ad Bellarmini argumenta respondetur*
- **Fixed edition:** Geneva, apud Petrum & Jacobum Chouët, 1620, Tome I
- **Edition relation:** the 1620 setting is the second edition, following the
  Geneva 1618 first edition. Pagination from the two settings must not be mixed.
- **Tome-I extent in the fixed edition:** four preliminary leaves and 1,574
  numbered columns

This workbench fixes the 1620 edition. The earlier 1618 e-rara copy (BGE Cxa
3171 / BGE Bc 793; DOI
[10.3931/e-rara-73428](https://doi.org/10.3931/e-rara-73428)) documents the first
edition but is not silently used to fill or renumber the 1620 text.

## Controlling witness and companion record

The textual witness is Bayerische Staatsbibliothek `bsb10175567`, call number
Dogm. 1237 b-1/2:

- [BSB catalog record](https://www.digitale-sammlungen.de/en/details/bsb10175567)
- [IIIF manifest](https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10175567/manifest)
- frame image pattern:
  `https://api.digitale-sammlungen.de/iiif/image/v2/bsb10175567_00015/full/full/0/default.jpg`
- hOCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb10175567/15`

The BSB manifest identifies the edition as Geneva, Chouët, 1620, with `[4]
Bl., 1574 Sp.` and 792 digital frames. BSB images govern this transcription;
hOCR is only a navigation and first-pass aid.

The same 1620 two-tome edition also has a Public Domain Mark e-rara record at
[e-rara 19548480](https://www.e-rara.ch/zuz/content/titleinfo/19548480),
Bibliothèque de Genève BGE Ctf 6160 / BGE Te 8345. The repository's prior
source audit records its extent as Tome I `[8], 1574 columns, [2 blank] pages`
and Tome II `570 columns, [11] pages`. That same-edition record confirms the
two-tome architecture and prevents the 1,574-column first tome from being
mistaken for the whole work. Part 01 was transcribed and checked directly
against the BSB images; no claim of a page-by-page collation with the e-rara
copy is made here.

## Exact boundaries and column mapping

The 1620 body begins at BSB frame 00015. Every physical page bears two numbered
columns:

| BSB frame | Fixed-edition columns | Content in Part 01 |
|---|---:|---|
| 00015 | 1–2 | opening heading and treatment of natural and communicated theology |
| 00016 | 3–4 | fallen natural theology; definition and genus of supernatural theology |
| 00017 | 5–6 | wisdom, subject, form, and efficient/instrumental causes |
| 00018 | 7–8 | enunciative speech, ends, and first principles of theology |

**Part 01 is the complete opening authorial topic, `DE THEOLOGIA`.** It begins
with `Locos Theologiae, quos Communes vocant, tractaturi` in column 1 and ends
in column 8 with `de sacra Scriptura primo loco agemus.` On the same physical
page, below that sentence, the ornamental heading `DE SACRA SCRIPTURA` opens
the next topic and its first controversy; all of that later matter is excluded.
The paired files contain eight synchronized column markers and the full text
between those exact boundaries:

- `parts/part-01-de-theologia-latin.txt`
- `parts/part-01-de-theologia-english.md`

This complete topic occupies four physical pages (eight numbered columns). It
is used as the request's first complete disputation/lecture-sized authorial
unit rather than padding Part 01 with an incomplete portion of the much longer
topic on Scripture.

## Editorial method and status

Long *s*, ligatures, line-end divisions, and typographic `u/v` and `i/j` are
normalized.
Substantive spelling, wording, numbering, Greek expressions, and printed
biblical locators are retained. Running heads, signatures, catchwords, and
ornaments are omitted. A word divided at a column boundary is shown with an em
dash on both sides of the synchronized marker. Uncertain or anomalous readings
are recorded instead of silently emended.

The English is a complete, independent translation of the accompanying Latin,
not a summary. No modern English translation was used as a wording source.
Both files are AI-assisted and unreviewed.

## Printed anomalies in Part 01

- Column 3 prints `Iacob. 3.11` beside `δαιμονιώδης`; the matching language is
  at James 3:15. The Latin retains `3.11`; the English retains it and notes the
  likely intended verse.
- Column 4 prints `1. ad Cor. 12.6. & 7` as a citation for theology as wisdom.
  The same claim in column 1 cites 1 Corinthians 2:6–7, which is the evident
  intended passage. The printed `12.6. & 7` remains in both paired files.
- Column 6 prints `2. Petr. 1.22`, although 2 Peter 1 ends at verse 21. The
  Latin and English retain the printed locator; the English notes the apparent
  intended verse.
- The small Greek types are legible but should receive specialist collation
  before publication. They have been normalized to standard Unicode accents
  without changing the words represented by the witness.
