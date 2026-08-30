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

## Completed lecture boundaries

The authorial lecture labels, rather than an arbitrary page count, control the
part boundaries. Several lectures begin or end within a printed page, so the
same scan can legitimately close one part and open the next:

| Part | Lecture | BSB scans | Printed pages | Boundary |
|---:|---:|---:|---:|---|
| 01 | I | 35–42 | preface [1]–8 | `PRÆFATIO` through `AMEN.` |
| 02 | II | 43–46 | 1–4 | `Prælectio secunda` through the transition to the epistle body |
| 03 | III | 46–48 | 4–6 | `Prælectio tertia` through the close of the doxology exposition |
| 04 | IV | 48–52 | 6–10 | `Prælectio IV` through its concluding doxology and `Amen` |
| 05 | V | 52–56 | 10–14 | `Prælectio quinta` through the exposition of `In Charitate` |
| 06 | VI | 56–60 | 14–18 | `Prælectio sexta` through `laudaretur ac celebraretur in omne ævum` |
| 07 | VII | 60–63 | 18–21 | `Prælectio septima` through its concluding `Amen` |
| 08 | VIII | 63–68 | 21–26 | `Prælectio octava` through its concluding `Amen` |
| 09 | IX | 69–71 | 27–29 | `In versum 8, &c.` through `dicta sunto` before Lecture X |
| 10 | X | 71–75 | 29–33 | `Sequitur jam versu proximo, pars ejusdem secunda` through `de ipsâ recollectione dicta sunto` |
| 11 | XI | 75–80 | 33–38 | `Quod ad secundum membrum attinet` through its concluding `Amen` |
| 12 | XII | 80–85 | 38–43 | `In Versum 11. ac 12.` and `Dictum nobis suprà suo loco` through `quam cum discrimine veritatis aliquo judicare` before Lecture XIII |
| 13 | XIII | 85–88 | 43–46 | `Jam ad quartum hujus loci membrum pergamus` through its concluding `Amen` before `In Versum 13. ac 14.` and Lecture XIV |

Part 01's page-level first and last text and captured full-image SHA-256 values
are recorded in [`apparatus/source-map.tsv`](apparatus/source-map.tsv), with
detailed notes in [`apparatus/part-01-notes.md`](apparatus/part-01-notes.md).
Part 02 has its separate
[`apparatus/part-02-source-map.tsv`](apparatus/part-02-source-map.tsv) and
[`apparatus/part-02-notes.md`](apparatus/part-02-notes.md). The later parts use
the same controlling witness and exact in-file source-marker convention.

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

## Completed parts

Each completed unit has a normalized Latin transcription and a fresh, full
English translation:

| Part | Subject | Latin | English |
|---:|---|---|---|
| 01 | Preface | [`part-01-praelection-01-preface-latin.txt`](parts/part-01-praelection-01-preface-latin.txt) | [`part-01-praelection-01-preface-english.md`](parts/part-01-praelection-01-preface-english.md) |
| 02 | Salutation | [`part-02-praelection-02-salutation-latin.txt`](parts/part-02-praelection-02-salutation-latin.txt) | [`part-02-praelection-02-salutation-english.md`](parts/part-02-praelection-02-salutation-english.md) |
| 03 | Method and doxology | [`part-03-praelection-03-method-and-doxology-latin.txt`](parts/part-03-praelection-03-method-and-doxology-latin.txt) | [`part-03-praelection-03-method-and-doxology-english.md`](parts/part-03-praelection-03-method-and-doxology-english.md) |
| 04 | Spiritual blessings | [`part-04-praelection-04-spiritual-blessings-latin.txt`](parts/part-04-praelection-04-spiritual-blessings-latin.txt) | [`part-04-praelection-04-spiritual-blessings-english.md`](parts/part-04-praelection-04-spiritual-blessings-english.md) |
| 05 | Election in Christ | [`part-05-praelection-05-election-in-christ-latin.txt`](parts/part-05-praelection-05-election-in-christ-latin.txt) | [`part-05-praelection-05-election-in-christ-english.md`](parts/part-05-praelection-05-election-in-christ-english.md) |
| 06 | Predestination and adoption | [`part-06-praelection-06-predestination-and-adoption-latin.txt`](parts/part-06-praelection-06-predestination-and-adoption-latin.txt) | [`part-06-praelection-06-predestination-and-adoption-english.md`](parts/part-06-praelection-06-predestination-and-adoption-english.md) |
| 07 | Observations on election | [`part-07-praelection-07-observations-on-election-latin.txt`](parts/part-07-praelection-07-observations-on-election-latin.txt) | [`part-07-praelection-07-observations-on-election-english.md`](parts/part-07-praelection-07-observations-on-election-english.md) |
| 08 | Redemption in Christ | [`part-08-praelection-08-redemption-in-christ-latin.txt`](parts/part-08-praelection-08-redemption-in-christ-latin.txt) | [`part-08-praelection-08-redemption-in-christ-english.md`](parts/part-08-praelection-08-redemption-in-christ-english.md) |
| 09 | Effectual calling and spiritual wisdom | [`part-09-praelection-09-effectual-calling-latin.txt`](parts/part-09-praelection-09-effectual-calling-latin.txt) | [`part-09-praelection-09-effectual-calling-english.md`](parts/part-09-praelection-09-effectual-calling-english.md) |
| 10 | The mystery of God’s will and recapitulation in Christ | [`part-10-praelection-10-mystery-and-recapitulation-latin.txt`](parts/part-10-praelection-10-mystery-and-recapitulation-latin.txt) | [`part-10-praelection-10-mystery-and-recapitulation-english.md`](parts/part-10-praelection-10-mystery-and-recapitulation-english.md) |
| 11 | The scope and time of recapitulation | [`part-11-praelection-11-scope-and-time-of-recapitulation-latin.txt`](parts/part-11-praelection-11-scope-and-time-of-recapitulation-latin.txt) | [`part-11-praelection-11-scope-and-time-of-recapitulation-english.md`](parts/part-11-praelection-11-scope-and-time-of-recapitulation-english.md) |
| 12 | Inheritance in Christ and the counsel of God’s will | [`part-12-praelection-12-inheritance-and-divine-purpose-latin.txt`](parts/part-12-praelection-12-inheritance-and-divine-purpose-latin.txt) | [`part-12-praelection-12-inheritance-and-divine-purpose-english.md`](parts/part-12-praelection-12-inheritance-and-divine-purpose-english.md) |
| 13 | The praise of God’s glory and the priority of Jewish hope | [`part-13-praelection-13-praise-and-priority-latin.txt`](parts/part-13-praelection-13-praise-and-priority-latin.txt) | [`part-13-praelection-13-praise-and-priority-english.md`](parts/part-13-praelection-13-praise-and-priority-english.md) |

The completed sequence now extends through Lecture XIII. Its successive subjects
are the work's exegetical method and preface, Paul's salutation, the form and
matter of the opening doxology, spiritual blessings in the heavenly places,
election in Christ, and the relation of predestination, adoption, Christ's
mediation, divine good pleasure, and the praise of glorious grace. Lecture VII
then derives six observations on assurance, foreseen faith and works, holiness
as the ordained means to salvation, the relation of faith and love, God's sole
causality in election, and the doxological end of the doctrine.
Lecture VIII then expounds redemption through Christ's blood, its price and
twofold liberation, union with Christ, forgiveness as redemption's effect,
the riches of divine grace, the typology of the two goats in Leviticus 16,
and the ethical force of having been bought with so great a price.
Lecture IX opens the application of these benefits through effectual calling,
distinguishes its external and internal aspects, and expounds the abundance of
spiritual wisdom and understanding in Ephesians 1:8. It distinguishes wisdom
from practical prudence by their objects, relates both to saving illumination,
and traces the gift through Christ to the riches of the Father's grace.
Lecture X then expounds the revealed mystery of God's will in Ephesians
1:9–10, the two senses of recapitulation, humanity's twofold dispersion from
God and neighbor, and three ancient readings of the restoration and gathering
of believers under Christ the head. Lecture XI continues with the scope of
the things in heaven and on earth, the debated relation of angels to that
gathering, Christ as its center, and the fullness and dispensation of the
times. Its concluding observations treat effectual calling, faith as a
spiritual gift, the sufficiency and depth of Scripture, wisdom joined to
Christian practice, the unity of the Church militant and triumphant under
Christ alone, and patient hope for the final consummation.
Lecture XII then begins the special application of Ephesians 1:11–12 to
believing Jews. It expounds their being allotted an inheritance in Christ,
the typology of Israel’s allotted land, the relation of inheritance to
adoption, and eternal predestination as the source of effectual calling. It
then examines God as the one who works all things according to the counsel of
his will, distinguishes divine counsel from creaturely deliberation, and
weighs restricted and providential readings of “all things” while denying
that divine providence makes God the author of sin.
Lecture XIII completes the exposition of Ephesians 1:12 by distinguishing the
inherent glory of God from creaturely praise and explaining the passive and
active senses in which believers exist for the praise of that glory. It then
interprets the Jews’ prior hope in Christ as a priority of time rather than
merit, grounds the gospel’s historical priority to Israel in God’s covenant
promises, and draws applications concerning personal appropriation of the
gospel, gratuitous election, submission to providence, and holy living as the
praise of divine glory.

## Validation

Run the existing work-local structural validators from the repository root:

```sh
python3 workbench/1652-boyd-praelectiones-in-ephesios/scripts/validate_part01.py
python3 workbench/1652-boyd-praelectiones-in-ephesios/scripts/validate_part02.py
```

These check UTF-8 and line hygiene, exact marker sequence and parity,
AI/unreviewed disclosures, minimum full-text size, required closes and
marginalia, and the available source-map structure. All later pairs follow the
same marker-parity and hygiene requirements. This workbench sequence does not
modify global ledgers, the publication manifest, or repository checksums.
