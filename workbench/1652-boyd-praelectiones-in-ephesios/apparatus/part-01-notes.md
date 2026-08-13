# Part 01 apparatus

This apparatus belongs to the AI-assisted, unreviewed Part 01 working draft.
It is not a critical apparatus and does not certify the text as human-reviewed.

## Boundary audit

- BSB scan 35 opens with `Prælectio I` in the outer margin and the heading
  `PRÆFATIO IN EPISTOLAM PAULI AD EPHESIOS`.
- The preface runs continuously through scan 42 and closes with `AMEN.`
- BSB scan 43 begins the commentary proper, headed `IN CAPUT PRIMUM`, and its
  outer margin explicitly reads `Prælectio secunda`.
- Part 01 therefore contains the first complete lecture. Its eight pages are
  shorter than the fallback 15–20-page unit, but the complete-lecture boundary
  is structurally preferable and satisfies the requested alternative.

## Witness and image audit

The controlling object is `bsb11059161`, the Regensburg, Staatliche Bibliothek
copy, shelfmark `999/2Script.651`, digitized by the Bayerische Staatsbibliothek.
The IIIF manifest reports 1,298 canvases, London publication by the Stationers'
Company in 1652, extent `[14] Bl., 1236 S., [9] Bl.`, and rights statement
`No Copyright – Non-Commercial Use Only` (`NoC-NC 1.0`). The eight full-size
JPEG hashes in `source-map.tsv` were captured on 2026-08-13 UTC. Images are not
redistributed in this repository.

Stable endpoints:

- Manifest: <https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11059161/manifest>
- Viewer: <https://www.digitale-sammlungen.de/en/view/bsb11059161>
- Image pattern: `https://api.digitale-sammlungen.de/iiif/image/v2/bsb11059161_000NN/full/full/0/default.jpg`
- BSB hOCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11059161/NN`

The source map records first and last words after normalization; split words
are joined in the Latin and the next marker is placed before the complete word
or phrase. Page images govern every reading. BSB hOCR supplied a layout-aware
finding aid only.

## Editorial conventions

- Long `s`, ligatures, line-end divisions, explicit abbreviation marks, and
  typographic `u/v` are normalized.
- Historical spelling, capitalization where semantically useful, Greek,
  section labels, numbered sequences, biblical references, and substantive
  marginal notes are retained.
- Running heads, signatures, catchwords, column letters, ornaments, and bare
  page numbers are omitted from the prose. Scan and printed-page identities
  are retained in exact source markers.
- The first printed preface page has no visible number. Its marker therefore
  reports `Præfatio p. [1], unnumbered`; the visible sequence continues 2–8.
- Marginal matter is linearized after the paragraph or passage it annotates.
  It is translated in the English file and labeled `[Marginalia: ...]` in both.

## Readings requiring human review

The following readings are retained provisionally after image inspection and
should receive special attention in human review:

1. The two Greek poetic quotations on scan 35 are extremely small and worn.
   Their normalized accents and word division have been reconstructed from the
   visible type and parallel searchable text; the wording, especially the
   first quotation, should be collated by a Greek specialist.
2. The marginal identification `D. Beraudus venerandus senex is fuit` on scan
   37 is clear enough in the witness but the intended personal name has not
   been independently identified.
3. The three Christological polemical labels on scan 40 are transcribed as
   `Μετουσίας, Συνουσίας et Πανταχουσίας`; accents and the first
   initial letter should be rechecked against another copy or the 1661 edition.
4. Boyd prints the date of the Council of Ephesus as 450, or 437 according to
   others. The historically standard date is 431; the working text preserves
   the witness rather than silently correcting it.
5. Biblical and patristic marginal citations have been expanded only where the
   referent is clear. The working translation regularizes book names but makes
   no claim to have verified every reference against the cited edition.

No lacuna, illegible replacement character, or intentionally omitted body-text
passage remains in this unit.
