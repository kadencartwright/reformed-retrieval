# Part 02 apparatus

This apparatus belongs to the AI-assisted, unreviewed Part 02 working draft.
It is not a critical apparatus and does not certify the Latin or English as
human-reviewed.

## Boundary audit

- BSB scan 43, printed main-text page 1, opens the commentary proper with `IN
  CAPUT PRIMUM`, `DE SALUTATIONE`, and the outer marginal label `Prælectio
  secunda`.
- Lecture II expounds Ephesians 1:1–2: the person greeting, the persons
  greeted, and the grace and peace for which Paul prays.
- The lecture continues through all of printed pages 1–3. At the top of scan
  46, printed page 4, its last nine lines conclude the inference about the
  condition of the faithful and end `Jam ad ipsum Epistolæ corpus explicandum
  transeamus.`
- The next centered heading, `In versum tertium & sequentes`, and the outer
  marginal label `Prælectio tertia` begin Lecture III on that same page. They
  are recorded only to prove the boundary and are excluded from both Part 02
  texts.
- Part 01 established the priority of an exact complete-lecture boundary over
  the fallback 15–20-page range. Part 02 follows that same rule: the next
  complete lecture occupies three full folio pages plus ten lines of a fourth.
  No portion of Lecture III has been appended merely to enlarge the unit.

## Witness and image audit

The controlling object remains BSB `bsb11059161`, the Regensburg, Staatliche
Bibliothek copy, shelfmark `999/2Script.651`. Full-size JPEGs for scans 43–46
were captured from the BSB IIIF image service on 2026-08-13 UTC. Their SHA-256
digests and normalized first and last included text are recorded in
`part-02-source-map.tsv`; images are not redistributed in the repository.

Stable endpoints:

- Manifest: <https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11059161/manifest>
- Viewer: <https://www.digitale-sammlungen.de/en/view/bsb11059161>
- Image pattern: `https://api.digitale-sammlungen.de/iiif/image/v2/bsb11059161_000NN/full/full/0/default.jpg`
- BSB hOCR pattern: `https://api.digitale-sammlungen.de/ocr/bsb11059161/NN`

Page images govern every reading. BSB hOCR was used only to locate and collate
words after the column order had been checked against each image. Scan 46 is
hashed in full even though Part 02 includes only the upper nine lines of its
left column; `included_region` makes that limitation explicit.

## Editorial conventions

- Long `s`, ligatures, explicit abbreviations, line-end word divisions, and
  typographic `u/v` are normalized.
- Historical spelling, capitalization where semantically useful, Greek,
  Hebrew transliteration, numbered structures, biblical references, and
  substantive marginal notes are retained.
- Running heads, ornaments, signatures, catchwords, column letters, and bare
  printed page numbers are omitted.
- Source markers have exact parity in Latin and English. The scan 46 marker
  explicitly states that it ends at the close of Lecture II.
- Marginal matter is moved after the passage it annotates and labeled
  `[Marginalia: ...]`; purely navigational column letters are not reproduced.
- The English is a fresh, full close translation of the paired Latin, not a
  summary. Greek technical terms are translated in context while remaining
  visible in the Latin file.

## Completed local collation repairs

- On scan 43, image collation corrected hOCR-derived `consentientibus` to the
  witness's `censentibus`; the existing English sense, “some hold,” already
  represented the corrected reading.
- On scan 44, image collation restored printed `adque` where the draft had
  silently read `adeóque`; the paired English coordination was corrected with
  it.
- On scan 45, `velut` below the final body line is the catchword repeated as
  the first word on scan 46. It is omitted at the foot of scan 45 and
  transcribed once after the scan 46 marker. The source map's final-text field
  now excludes that catchword.
- Direct image counting established that Lecture II occupies the first nine
  body lines of scan 46. The earlier provisional count of ten was corrected in
  the boundary note, source map, and validator.

## Readings requiring human review

1. The paired Greek marginal note concerning the forms *Saul* and *Paul* on
   scan 43 is very small. It is provisionally read `κατ᾽ ἄρσιν καὶ θέσιν`.
2. The Greek adjective describing apostolic doctrine and the adjective for
   inspired writings on scan 44 are normalized as `αὐτόπιστος` and
   `θεόπνευστα`; accents and the final letters should be collated against a
   second copy.
3. The compressed phrase surrounding `ἀναμαρτησίας testimonio` on scan 44 is
   syntactically difficult but visually supports the retained text.
4. The Greek adverbs criticizing unexamined use of patristic writings on scan
   45 are provisionally normalized `ἀβασανίστως καὶ ἀνεξετάστως`.
5. The printed Greek in the catalogue of pagan greetings and in the
   explanations of grace and peace is small and worn. The readings
   `εὐπραθεῖν`, `χρηστότητι`, and `ἐκ πληροφορίᾳ` should receive specialist
   review; the last construction is preserved rather than silently repaired.
6. Boyd's references and quotations have been normalized where their referent
   is clear but have not all been independently collated against biblical or
   patristic editions.

No lacuna, replacement character, intentionally omitted body-text passage, or
unfinished translation remains within the stated Lecture II boundary.
