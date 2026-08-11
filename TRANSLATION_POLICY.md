# Translation and transcription policy

## Aim

The project supplies readable English without hiding the source-language
evidence. It
distinguishes the historical work, the nineteenth-century edition, the
normalized transcription, and the new translation.

## Source transcription and normalization

Each document has one canonical normalized source file: `latin.txt` for a
Latin-form witness or `french.txt` for a French-form witness. The normalized
source transcription:

1. follows the identified *Calvini Opera* witness;
2. removes line wrapping and joins words divided only by printer line endings;
3. normalizes long `s`, ligatures, and unambiguous OCR errors;
4. preserves edition spelling and historical forms—Latin *quum*, *autor*, or
   *foemina*, and corresponding early modern French orthography—when genuinely
   printed that way;
5. preserves paragraph boundaries where they can be recovered;
6. inserts explicit printed-page markers;
7. when a printer divides one word across a page boundary, joins the word and
   places the new-page marker before the complete word; and
8. excludes editorial footnotes from the historical text while recording any
   material intervention in the document README or notes.

The transcription is diplomatic-normalized, not a new critical edition. A
historical translation is never silently relabeled as an original-language
witness; its direction and status are recorded in the document README.

## English translation

The English is translated afresh from the normalized source-language text and
checked against the facsimile. It favors semantic precision over imitation of
sixteenth-century English. Technical and ecclesiological terms are rendered
consistently where possible; meaningful ambiguity is explained in a
translator's note rather than silently resolved.

English page markers reproduce the source marker sequence. At a split-word
boundary, the English marker is placed before the translated word or phrase
that corresponds to the joined source word, even when ordinary English word
order would permit a smoother break elsewhere.

The translation does not copy or paraphrase a copyrighted modern translation.
Public-domain English discussions may be consulted for bibliography, but the
source witness controls the wording.

## Review status

Every document begins as an AI-assisted draft. A document should not be called
“reviewed” until a named reviewer competent in the source language has compared
the complete transcription and translation with the page images. Corrections
should preserve an inspectable Git history.

## Licensing

Only project-authored content in `texts/*/english.md`, including translator's
notes within those files, is dedicated under CC0. The normalized source files,
document READMEs, research, metadata, and this policy are not part of that CC0
dedication. Platform software and supporting configuration are licensed under
MIT. See [`LICENSING.md`](LICENSING.md) for the authoritative path-based scope.
