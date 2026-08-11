# Translation and transcription policy

## Aim

The project supplies readable English without hiding the Latin evidence. It
distinguishes the historical work, the nineteenth-century edition, the
normalized transcription, and the new translation.

## Latin normalization

The normalized Latin:

1. follows the identified *Calvini Opera* witness;
2. removes line wrapping and joins words divided only by printer line endings;
3. normalizes long `s`, ligatures, and unambiguous OCR errors;
4. preserves edition spelling such as `quum`, `autor`, or `foemina` when it is
   genuinely printed that way;
5. preserves paragraph boundaries where they can be recovered;
6. inserts explicit printed-page markers; and
7. excludes editorial footnotes from the historical text while recording any
   material intervention in the document README or notes.

The transcription is diplomatic-normalized, not a new critical Latin edition.

## English translation

The English is translated afresh from the normalized Latin and checked against
the facsimile. It favors semantic precision over imitation of sixteenth-century
English. Technical and ecclesiological terms are rendered consistently where
possible; meaningful ambiguity is explained in a translator's note rather than
silently resolved.

The translation does not copy or paraphrase a copyrighted modern translation.
Public-domain English discussions may be consulted for bibliography, but the
Latin witness controls the wording.

## Review status

Every document begins as an AI-assisted draft. A document should not be called
“reviewed” until a named reviewer competent in early modern Latin has compared
the complete transcription and translation with the page images. Corrections
should preserve an inspectable Git history.

## Licensing

Only project-authored content in `texts/*/english.md`, including translator's
notes within those files, is dedicated under CC0. The normalized source files,
document READMEs, research, metadata, and this policy are not part of that CC0
dedication. Platform software and supporting configuration are licensed under
MIT. See [`LICENSING.md`](LICENSING.md) for the authoritative path-based scope.
