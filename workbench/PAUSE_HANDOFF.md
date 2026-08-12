# Reformed Latin translation project — pause handoff

**Paused:** 12 August 2026; updated after completion of Examen Part 05
**State:** all translation agents stopped; no background agent remains active  
**Bottom line:** the research inventory is complete enough to guide the project,
but the user's request to translate every non-Calvin target is **not complete**.
Several substantial works now have complete working drafts; the remaining queue
is still very large.

## Original scope

The request was to:

1. identify influential Reformed theologians, especially Calvin, Beza, and the
   English and Scottish Presbyterian traditions;
2. identify Latin works of theirs for which no public-domain English
   translation could be located;
3. record the findings in a local Markdown document; and
4. translate every identified target except Calvin.

Calvin is included in the bibliographic findings but excluded from all new
translation work, exactly as requested. George Gillespie produced no usable
Latin translation target in the audit and therefore has no translation row.

## Primary project documents

- [`../research/untranslated-latin-treatises.md`](../research/untranslated-latin-treatises.md)
  is the 495-line research inventory. It records candidates, exclusions,
  public-domain witnesses, source boundaries, links, translation-status
  caveats, and the reason Calvin is excluded.
- [`TRANSLATION_STATUS.md`](TRANSLATION_STATUS.md) is the work-by-work ledger.
- [`README.md`](README.md) explains the distinction between a workbench draft
  and a reviewed/published edition.
- Each work directory has its own `README.md` with the controlling witness,
  exact boundaries, editorial method, and local completion state.

The non-Calvin queue is approximately **21,000 source pages or scan frames**.
Consequently, the completed material below is meaningful but does not amount
to completion of the original full-corpus request.

## Complete paired working drafts

These have complete Latin transcriptions and complete independent English
working translations for the documented work boundary. They are AI-assisted
and unreviewed; “complete” here does not mean publication-ready.

| Author | Work | Completed boundary |
|---|---|---|
| Theodore Beza | *De haereticis a civili magistratu puniendis* | All 85 pages, 1582 pp. 85–169; terminal sentence verified although the witness prints no literal `FINIS`. |
| Theodore Beza | *Ad Sebastiani Castellionis calumnias* | All 88 pages, 1582 pp. 337–424; next-work catchword excluded. |
| Theodore Beza | *De pace Christianarum ecclesiarum constituenda* | Complete through `FINIS`; adjacent *Defensio* excluded. |
| Theodore Beza | *De hypostatica duarum in Christo naturarum unione* | Complete 1582 pp. 625–645; following Luther extract excluded. |
| Theodore Beza | *De praedestinationis doctrina et vero usu* | Complete 1582 pp. 402–447, including the address and appended Luther excerpts through `FINIS`; volume errata excluded. |
| Theodore Beza | *De coena Domini* | Complete 1582 pp. 211–258; next-work catchword excluded. |
| Theodore Beza | *De vera excommunicatione et christiano presbyterio* | Complete three-part draft from the surviving opening through `FINIS`; documented overlap between parts. |
| Robert Rollock | *Quaestiones de foedere Dei* | Complete through `FINIS`, with 167 matched question/answer pairs. |
| Robert Howie | *De reconciliatione hominis cum Deo* | Both dedications, main treatise, *De communione*, and *De iustificatione* through `FINIS`; 156 matched markers. |
| Franciscus Junius | *De theologia vera* | Complete 62-page authorial unit: title, dedication, synopsis, eighteen chapters, and concluding prayer. |
| Samuel Rutherford | *Disputatio scholastica de divina providentia* | Complete core-text draft: preliminaries, all thirty chapters, metaphysical disquisitions, additions, terminal `FINIS`, and all 32 printed errata. There are 59 paired parts / 118 files. The printed indexes are deliberately excluded as navigational apparatus. |

Every item above still requires independent Latin and translation review before
quotation or publication.

## Incomplete translations and exact restart points

### Beza, *Ad acta colloquii Montisbelgardensis responsio*

- Directory: [`1588-beza-ad-acta-montisbelgardensis/`](1588-beza-ad-acta-montisbelgardensis/)
- Part I is complete through its true `FINIS` and full work-specific errata:
  196 synchronized markers. The defective 1588 copy's missing printed p. 177 is
  supplied transparently from the public-domain 1587 witness.
- Part II is complete only through PDF 102 / logical scan 101 / printed p. 100:
  100 synchronized markers.
- Exact next text on shared p. 100:
  `Quid igitur? audi patienter quid hic sentiam, Christiane lector & diiudica.`
- Part II ultimately runs through PDF 257 / printed p. 255, including `FINIS`
  and errata. Thus roughly 155 printed pages remain.

### Cartwright, *Commentarii in Proverbia Salomonis*

- Directory: [`1632-cartwright-commentary-proverbs/`](1632-cartwright-commentary-proverbs/)
- Source fully mapped: PDF 5 title; PDFs 7–12 Polyander preface; PDFs 13–672
  commentary, printed columns 1–1333; PDFs 673–684 index; PDFs 685–690
  commandment tables ending at `FINIS`.
- Part 00, title and Polyander's preface, is complete as a paired draft.
- Part 01 reaches the correct Chapter I endpoint on PDF 24, immediately before
  `CAPUT II`, but the final audit was interrupted. The Latin has 12 PDF markers
  for PDFs 13–24; the English has only 9 and lacks explicit markers for PDFs
  14, 20, and 23. Do **not** assume these are marker-only omissions: compare
  the English content for those pages against the Latin and facsimile before
  calling Chapter I complete.
- After that audit, Chapter II begins on the lower part of PDF 24 and ends
  before `CAPUT III` on PDF 30.

### Rutherford, *Exercitationes apologeticae pro divina gratia*

- Directory: [`1651-rutherford-exercitationes-apologeticae/`](1651-rutherford-exercitationes-apologeticae/)
- Complete source map: authorial body logical pp. 1–539 / PDFs 19–557;
  two-page index PDFs 558–559; no separate errata; no missing body leaves.
- Parts 01–05 are complete and scan-audited through Exercise I, Chapter III,
  argument 13 on logical p. 85 / PDF 103.
- Exact completed endpoint:
  `Et non possunt non salvandi salvari, & qui damnantur, non damnari, etiam Deo invito.`
- The next unit was mapped but not drafted. It begins on shared logical p. 85
  at argument 14, `Sed quoniam obiter hoc argumentum evertit
  prædestinationem Arminianam ex prævisa fide...`, and runs through the actual
  end of Chapter III on logical p. 103 / PDF 121. Stop before centered
  `CAP. IV` on that shared page.

### Rutherford, *Examen Arminianismi*

- Directory: [`1668-rutherford-examen-arminianismi/`](1668-rutherford-examen-arminianismi/)
- Complete source map: Rutherford's body printed pp. 1–761 / PDFs 54–810,
  surrounded by separately identified editorial preliminaries, errata, and
  three indexes.
- Parts 01–05 are complete and scan-audited through the liberty-of-prophesying
  discussion on printed p. 93 / PDF 144.
- The controlling KBNL/UvA copy genuinely lacks printed pp. 42–43. Those pages
  are already supplied under explicit markers from the public-domain British
  Library witness.
- Part 05 has seventeen synchronized markers, ends with the mapped p. 93
  sentence `...quæ Arminiani controversa non necessaria vocant`, and applies
  and documents the printed correction `potest mortem` to `post mortem`.
- Resume on p. 94 at the allied question, `Huic Quæstioni, affinis est illa. An
  non quilibet in quâlibet Religione salvari queat?`

### Cartwright, *Metaphrasis et homiliae in Ecclesiasten*

- Directory: [`1663-cartwright-metaphrasis-ecclesiastes/`](1663-cartwright-metaphrasis-ecclesiastes/)
- Translation has **not begun**.
- A complete 1663 public-domain Google reader witness was found and mapped:
  six preliminary images plus 230 two-page openings, printed pp. 1–460.
- `PP1` is the title; `PP2` is blank; `PP3`–`PP4` are Cartwright's dedication
  to King James; `PP5`–`PP6` are his address to the reader; `PA1`–`PA459` are
  the complete exposition.
- The final page has a complete terminal sentence and ornamental tailpiece,
  but no literal `FINIS`.
- A temporary cache of all 236 ordinary reader images exists at
  `/tmp/cartwright-ecclesiastes-1663-google-pages`. Temporary paths are not a
  durable repository asset; the work README records stable Google links and
  the full map.

## Source-audited but untranslated queue

Usable witnesses and editorial warnings are in the research inventory for:

- Robert Baillie, *Operis historici et chronologici libri duo*;
- David Calderwood, *Altare Damascenum*;
- John Brown of Wamphray, *De causa Dei* volumes I–II and the two volumes
  against Wolzogen and Velthuysen;
- William Twisse, *Vindiciae gratiae*, *De scientia media*, and the
  *Animadversiones*;
- Robert Parker, *De politeia ecclesiastica*;
- Hugh Sanford and Robert Parker, *De descensu Domini ad inferos*;
- Anthony Tuckney, *Praelectiones theologicae*;
- John Sharp, *De justificatione*, *De misero hominis statu*, and the two-tome
  *Cursus theologicus*;
- Robert Boyd of Trochrig, *Praelectiones in Ephesios*;
- William Ames, *Coronis* and *Bellarminus enervatus*;
- Francis Turretin, *Institutio theologiae elencticae*; and
- Amandus Polanus, *Syntagma theologiae christianae*.

John Sharp's *Symphonia prophetarum et apostolorum* remains blocked because no
openly downloadable scan or OCR was located. Source status is not translation
completion.

## Recommended resume order

1. Audit Cartwright Proverbs Chapter I, especially English PDFs 14, 20, and
   23; only then update its README to say complete.
2. Translate the already-mapped Rutherford *Exercitationes* Chapter III Part B
   (logical pp. 85–103).
3. Resume Beza Montbéliard Part II at printed p. 100 and continue sequentially
   through p. 255 / `FINIS` / errata.
4. Continue Cartwright *Proverbs* chapter by chapter.
5. Begin Cartwright *Ecclesiastes* with the six preliminary reader images,
   keeping the dedication and reader address separately attributed.
6. Work through the remaining source-audited British and Scottish queue in
   bounded textual units.

## Editorial and safety rules for continuation

- Preserve one-to-one Latin/English source-marker parity.
- Translate the full text; do not summarize omitted passages.
- Keep headings, marginalia, biblical references, Greek, Hebrew, tables, and
  documentary quotations. Label separately authored or editorial matter.
- Let facsimile images control; OCR is only a transcription aid.
- Mark source defects and supplied readings explicitly rather than silently
  inventing or emending text.
- Every English file must say **AI-assisted and unreviewed**.
- Do not move workbench files into `texts/` or call them public-domain English
  editions until qualified human review is complete.
- Do not translate the Calvin items.

## Repository state at pause

- `python3 scripts/validate.py` passes: `Validated 67 document directories.`
- `git diff --check` is clean.
- `research/` and `workbench/` are untracked in Git (`??`); no commit was made.
- Workbench inventory at pause: 190 files, including 85 Latin files, 85 English
  files, 19 per-work READMEs, and the status ledger.
- The validator does not detect semantic incompleteness. In particular, it
  does not make the unaudited Cartwright Chapter I complete.
