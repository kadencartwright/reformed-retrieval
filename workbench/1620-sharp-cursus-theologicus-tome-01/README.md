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

## Completed continuation and current boundary

The paired continuation now runs without a content gap from the opening of
the tome through the opening portion of Question IV of `DE DEO`. It
includes the complete opening tract `DE SACRA SCRIPTURA`, with the meanings of
tradition, state of the final controversy, positive arguments, testimonies of
the Fathers, and all twenty-eight printed objections with their responses. It
then continues through the existence, unity, and essence of God, the opening
taxonomy and rules of the divine attributes, the complete treatments of
divine simplicity and infinity, including eternity, immutability, and
immensity, and the opening rule for communicable attributes with the complete
treatments of divine life, divine wisdom or knowledge, the divine will, and
divine truth. The continuation embedded below then completes the sequence of
names given to the divine will: goodness, love, hatred, justice, mercy, anger,
and chastity.
Units that share a numbered column meet at the printed internal heading or
section boundary in that column; neither pair duplicates matter across the
join.

| Part | Complete authorial unit | Fixed-edition columns | BSB frames |
|---:|---|---:|---:|
| 02 | `DE SACRA SCRIPTURA`, Controversy I: canon | 8–25 | 00018–00027 |
| 03 | Controversy II: authentic edition | 25–35 | 00027–00032 |
| 04 | Controversy III: vernacular translations | 35–41 | 00032–00035 |
| 05 | Controversy IV: reading Scripture | 41–48 | 00035–00038 |
| 06 | Controversy V: public sacred rites | 48–53 | 00038–00041 |
| 07 | Controversy VI: authority | 54–69 | 00041–00049 |
| 08 | Controversy VII: clarity | 69–82 | 00049–00055 |
| 09 | Controversy VIII: interpretation | 82–120 | 00055–00074 |
| 10 | Question IX: necessity | 121–125 | 00075–00077 |
| 11 | Controversy IX: perfection, positive case and patristic testimonies | 125–136 | 00077–00082 |
| 12 | Controversy IX: perfection, objections 1–5 | 136–151 | 00082–00090 |
| 13 | Controversy IX: perfection, objections 6–28 | 151–170 | 00090–00099 |
| 14 | `DE DEO`: introduction and Questions I–III | 170–180 | 00099–00104 |
| 15 | Question IV: attributes and divine simplicity | 180–188 | 00104–00106, 00109–00110 |
| 16 | Question IV: divine infinity, eternity, immutability, and immensity | 188–192 | 00110–00112 |
| 17 | Question IV: communicable attributes and divine life | 192–193 | 00112–00113 |
| 18 | Question IV: divine wisdom or knowledge | 194–196 | 00113–00114 |
| 19 | Question IV: divine will | 197–200 | 00115–00116 |
| 20 | Question IV: divine truth | 200 | 00116 |
| 21 (below) | Question IV: divine goodness through divine chastity | 200–205 | 00116–00119 |

For rows 02–20 the normal pair is stored under `parts/` as a normalized Latin
transcription (`-latin.txt`) and a fresh English translation (`-english.md`)
with the same part number and descriptive stem. Part 21 is the explicitly
marked exception: its synchronized pair is embedded below in this README.

**Part-13/Part-14 join:** Part 13 ends in column 170 at BSB frame 00099 with
the response to Objection 28, `in quo & a nobis imitandi sunt.` Part 14 begins
later in the same column at the ornamental heading `DE DEO`; no matter between
the sentence and heading is omitted or duplicated.

**Part-14/Part-15 join:** Part 14 ends in column 180 at BSB frame 00104 with
the final sentence on the name *Elohim*, `De hoc nomine pluribus ubi de
Trinitate.` Part 15 begins immediately afterward in the same column at
`QUAESTIO IV. Qualis sit Deus: ubi de attributis Divinis agitur.` No text is
omitted or duplicated at the join.

**BSB imaging sequence in Part 15:** Frame 00107 is a defective exposure of
columns 185–186, with the leaf folded and other columns intruding into the
image. Frame 00108 repeats columns 183–184, and frame 00109 supplies the clear
retake of columns 185–186. The transcription therefore maps columns 185–186
to frame 00109 and does not use the obscured exposure to fill readings.

**Part-15/Part-16 join:** Part 15 ends in column 188 at BSB frame 00110 with
the fourth use of the doctrine of simplicity, `nempe Deo similes sine ulla
mixtura peccati.` Part 16 begins immediately afterward in the same column at
`De Infinitate Dei.` No text is omitted or duplicated at the join.

**Part-16/Part-17 join:** Part 16 ends in column 192 at BSB frame 00112 with
the sixth use of the doctrine of immensity, `Ergo non est necesse ut Angelos
invocemus.` Part 17 begins immediately afterward in the same column at `De
attributis κοινωνητοῖς.` No text is omitted or duplicated at the join.

**Part-17/Part-18 join:** Part 17 ends at the foot of column 193 at BSB frame
00113 with the third use of the doctrine of divine life, `Ergo in aeternum
vivemus.` Part 18 begins at the top of column 194 on the same frame at `De
Sapientia seu Scientia Dei.` No text is omitted or duplicated at the join.
Part 17 spans portions of two numbered columns; the word `comprehendere`
crosses their boundary and is represented by a synchronized split in both
files.

**Part-18/Part-19 join:** Part 18 ends at the foot of column 196 at BSB frame
00114 with the fifth use of the doctrine of divine wisdom, `quia Deo inscio
nobis non accidunt.` Part 19 begins at the top of column 197 on BSB frame
00115 with `De Voluntate Dei.` No text is omitted or duplicated at the join.
In Part 18 the Greek word `βλεπομένων` and the Latin word `cogitationis` cross
numbered-column boundaries and are represented by synchronized splits in both
files.

**Part-19/Part-20 join:** Part 19 ends in column 200 at BSB frame 00116 with
the list of names given to the one divine will, `castitas, &c.` Part 20 begins
immediately afterward in the same column at `De Veritate Dei.` No text is
omitted or duplicated at the join. In Part 19 the Latin words `beneplaciti`
and `Malum` cross numbered-column boundaries and are represented by
synchronized splits in both files.

**Part-20/README-continuation join:** Part 20 ends in column 200 at BSB frame
00116 with
the fourth use of the doctrine of divine truth, `licèt nobis quae promisit
impossibilia esse videantur.` The paired continuation below begins immediately
afterward in the same column at `De Bonitate Dei.` No text is omitted or
duplicated at the join. It is embedded here, rather than placed under `parts/`,
to keep this continuation confined to the requested target README.

**Exact resume boundary:** The continuation ends in column 205 at BSB frame
00119 with the use of the doctrine of divine chastity, `sicut pater noster
perfectus est. Matth. 5. ult. vers.` The heading `De Potentia Dei.` begins
immediately afterward in the same column and is excluded. The treatment of
divine power is the next untranscribed text.

## Part 21: Latin source—divine goodness through divine chastity

> **Working-edition notice:** This normalized diplomatic transcription was
> made from the BSB images of the 1620 Geneva edition. Long *s*, ligatures,
> line-end divisions, and typographic `u/v` and `i/j` are normalized; wording,
> Greek, numbers, marginal references, and printed anomalies are retained. It
> begins at the heading `De Bonitate Dei` in column 200 and ends immediately
> before `De Potentia Dei` in column 205.

[1620 Tome I | col. 200 | BSB frame 00116]

### De Bonitate Dei.

Bonitas est voluntas Dei, qua alijs bene vult, & ad benefaciendum est
propensus, Ps. 37.1. Matth. 19.17. estque aeterna & immutabilis, Ps. 117.2.
Ier. 33.11.

Bonitas autem Dei bifariam consideratur.

1. Ut est in se simpliciter, & hoc modo Deus est infinite, & perfectissimè
bonus, immò ipsa bonitas.

2. Respectivè quatenus hanc suam bonitatem alijs communicat: bonitas enim in
Deo non est otiosa, sed ut omne

[1620 Tome I | col. 201 | BSB frame 00117]

bonum est appetibile, pulchrum & sui communicativum: ita & Dei bonitas quae in
creaturis omnibus, praecipuè verò in Ecclesia relucet, adeò ut bonitatis omnis
causa efficiens, exemplaris & finalis sit.

*Usus doctrinae.* 1. Solus ergo Deus per se & essentia sua perfectè bonus est:
res verò omnes tantum communicatione. Iac. 1.17. ac proinde non est peccatis
offendendus.

2. Ergo est illi fidendum.

3. Ergo in necessitatibus ad illum est confugiendum.

4. Ergo in adversis non debemus de eo conqueri cùm ab eo nihil mali proficisci
possit.

5. Cùm Dei bonitas se ad omnes etiam impios extendat, discamus & nos benefici
esse.

6. Cùm Dei bonitas praecipuè sit erga membra Ecclesiae, ergo & nos domesticos
fidei praecipuè beneficijs prosequamur.

### De Amore Dei.

Amor est voluntas qua Deus vult id est approbat quod bonum est & in eo
acquiescit. Matth. 3.17. Psal. 45.8. immò Deus est ipse amor, nec in Deo
significat passionem ut in nobis sed haec tria.

1. Dei voluntatem seu propositum benefaciendi ab aeterno, ut Rom. 9.13.

2. Effecta huius amoris temporalia & aeterna 1. Ioan. 3.1.

3. Complacentiam & oblectationem Psal. 44.25. & his modis omnibus amor de Deo
dicitur. Deus autem se amat & omnia à se condita, ita tamen ut pro gradu
bonitatis in creaturis meliora plus amet: quia quibus plus bonitatis
communicavit ipsi similiora sunt. Denique amor Dei aeternus, immensus &
constantissimus est.

*Usus doctrinae.* 1. Hoc servit nostrae consolationi cùm sciamus Deum esse

[1620 Tome I | col. 202 | BSB frame 00117]

ipsum amorem.

2. Ergo Deus est fons omnis amoris in nobis, & qui Deum & proximum non amat,
privatur hac communione amoris cum Deo qui amorem proximi continuò ex se
gignit.

3. Deus amat omnia, ergo creaturis pro libidine nostra non est abutendum, sed
erga illas aequitate & moderatione utendum est.

4. Cùm Deus praecipuè amet fideles, ergo illi magis quàm alij à nobis diligendi
sunt, & pro salute illorum & bono procurando nec nobis nec bonis nostris est
parcendum.

5. Deus meliores magis amat: ergo studendum est pietati & sanctitati 1. Thess.
4.3.

6. Cùm Dei amor sit gratuitus, simus humiles, denique & certi de salute.

### De Odio Dei.

Odium est voluntas Dei qua non vult, id est non approbat sed improbat malum &
aversatur. Psal. 48.85. 1. Cor. 10.5. Mala verò odit simpliciter: at malos
secundum quid quatenus peccato sunt vitiati. Odium cum Deo tribuitur tria habet
significata.

1. Significat negationem benevolentiae quae est ad vitam aeternam: vel
significat propositum non miserendi. Rom. 9.13.

2. Significat decretum puniendi, ipsamque punitionem iustam. Psalm. 5.6. Iob.
30.21.

3. Significat displicentiam & detestationem mali Psal. 45.8. & his modis
omnibus rectè Deo tribuitur.

*Usus.* 1. Ergo maxima est virtus odisse omnem impietatem & impios quatenus
impij sunt. 2. Ergo consortia impiorum sunt fugienda, nec cum hostibus amicitia
est colenda, 2. Thess. 2.6.

### De Iustitia Dei.

Iustitia est voluntas Dei qua iustè Deus vult, vel qua ad suum cuique
tribuendum est propensus, bonis praemia, malis poenas decernens.

[1620 Tome I | col. 203 | BSB frame 00118]

Deut. 22.25. Psal. 11.7. & 119.13. & Psalm. 145.17.

Iustitia quatuor significata habet.

1. Significat bonitatem absolutam seu omnum virtutum collectionem. 1. Tim.
1.9. & haec soli Deo competit.

2. Significat integritatem & sinceritatem, non simpliciter sed secundum
personam & statum quem aliquis gerit Lucae 1.6.

3. Significat iustitiam particularem distributivam vel collectivam quae partim
est in honoris, pecuniae, &c. partim iuris citra προσωποληψίαν
distributione.

4. Significat ipsam fidem seu veritatem in dictis & promissis servandis. 1.
Ioan. 1.9. & in his duobus ultimis significatis propriè etiam Deo convenit: &
ita licèt unica simplicissima sit Dei iustitia quae est ipsa Dei essentia,
tamen propter hos diversos respectus multiplex dicitur.

*Usus doctrina.* 1. Cùm Deus sit ipsa iustitia, in operibus nec verbo nec
cogitatione ullius iniustitiae est accusandus.

2. Ergo cùm constat de voluntate Dei non est disputandum utrum bona sit an
mala, iusta an iniusta, sed quidquid vult à nobis est praestandum.

3. Cùm Deus sit iustus iudex caveamus à peccato & excecutiamus securitatem
carnalem.

4. Cùm Deus sit iudex cùm nos castigat aequum est ut nos illi humiliter
subiiciamus culpam agnoscentes & veniam petentes quia nos corrigit in salutem.
Rom. 5.3.

### De Misericordia Dei.

Misericordia est voluntas Dei qua ad succurrendum miseris est propensus. Psal.
86.5. & 106.1. 118.1. Ier. 3.11. Eph. 2.4. idque aeternè & immutabiliter.
Misericordia autem in Deo non est ut à Philosophis definitur, id est quod sit
aegritudo animi ex miseria alterius concepta: sed misericordia in Deo duo
significat.

[1620 Tome I | col. 204 | BSB frame 00118]

1. Affectum Dei propensum ad miserendum.

2. Eius affectus effectum, ipsam nempe opitulationem, & in Deo duplex esse
dicitur.

1. Generalis erga omnes creaturas Luc. 6.36.

2. Specialis qua electorum miseretur ad vitam aeternam.

*Usus doctrinae.* 1. Hinc discimus nostram miseriam, quia misericordia Dei
egemus.

2. In afflictionibus non esse desperandum à quocunque nobis iniuriae inferantur,
quia Deus nobiscum quasi compatitur, ideóque suo tempore succurret.

3. Etsi labamur in gravia scelera non esse desperandum de salute, quia Deus
est summè misericors qui nos gratis in Christo amavit cùm essemus eius inimici:
Ergo multò magis cùm iam simus reconciliati Rom. 5.10.

### De Ira Dei.

Ira est voluntas Dei qua ad puniendum peccatores est propensus, quae in Deo
non est passio sed ipsa simplicissima Dei essentia: & ut Deo tribuitur in
Scriptura tria significat.

1. Certam & iustissimam Dei voluntatem atque decretum ulciscendi peccatum
Ioan. 3.36. Rom. 1.18.

2. Significat comminationes poenarum Psalm. 6.1. Oseae 11.9.

3. Effecta seu poenas ipsas. Rom. 2.5. Eph. 5.6. Matt. 3.7. dicitur autem ira
Dei mutari non ratione affectus in Deo sed effectus & ratione sensus nostri.

*Usus doctrinae.* 1. Ira ergo non est simpliciter res mala, sed quatenus animi
nostri vitia coniuncta habet: quia Deus, Christus, & Apostoli irasci dicuntur,
vitia autem irae cavenda sunt.

1. Ne temerè. 2. Ne propter privatas causas & non propter vitia, quà vitia
sunt. 3. Ne relicto vitio contra personam irascamur.

[1620 Tome I | col. 205 | BSB frame 00119]

2. Cùm Deus peccatis irascatur securitas carnalis & peccata fugienda sunt nec
differenda est poenitentia.

### De Castitate Dei.

Castitas est voluntas Dei qua munditiem vult & probat cum ordine à se sancito
congruentem: & immunditiem omnem cum hoc ordine pugnantem improbat. 1. Thess.
4.3.

*Usus doctrinae.* Cùm nos templa Spiritus sancti simus, studendum est ut ab
omni immunditie nos purgemus ut simus perfecti sicut pater noster perfectus
est. Matth. 5. ult. vers.

[End of Part 21. `De Potentia Dei` begins later in column 205 and is excluded.]

## Part 21: English translation—divine goodness through divine chastity

> **Working-edition notice:** This is a complete AI-assisted, unreviewed
> translation made independently from the Latin transcription above. It
> follows the same six source markers and includes every marginal reference.
> Printed anomalies are translated according to the apparent sense only where
> a note says so.

[1620 Tome I | col. 200 | BSB frame 00116]

### On the Goodness of God

Goodness is the will of God by which he wills good to others and is inclined
to do good, Psalm 37:1,[^p21-1] Matthew 19:17; and it is eternal and immutable,
Psalm 117:2 and Jeremiah 33:11.

God's goodness, however, is considered in two ways:

1. As it is in him absolutely; and in this way God is infinitely and most
perfectly good—indeed, goodness itself.

2. Relatively, insofar as he communicates this goodness of his to others. For
goodness in God is not idle, but, just as every

[1620 Tome I | col. 201 | BSB frame 00117]

good thing is desirable, beautiful, and communicative of itself, so too God's
goodness shines forth in all creatures, but especially in the Church, to such
a degree that he is the efficient, exemplary, and final cause of all goodness.

*Uses of the doctrine.* 1. God alone, therefore, is perfectly good of himself
and by his own essence; all other things are good only by communication, James
1:17. Consequently, he must not be offended by sins.

2. Therefore we must trust him.

3. Therefore in our needs we must flee to him for refuge.

4. Therefore in adversities we ought not complain about him, since nothing
evil can proceed from him.

5. Since God's goodness extends to everyone, even to the ungodly, let us also
learn to be beneficent.

6. Since God's goodness is especially directed toward the members of the
Church, let us also bestow kindness especially upon the household of faith.

### On the Love of God

Love is the will by which God wills—that is, approves—what is good and rests
satisfied in it, Matthew 3:17 and Psalm 45:8. Indeed, God is love itself; and
in God love does not signify a passion, as it does in us, but these three
things:

1. God's will or purpose to do good from eternity, as in Romans 9:13.

2. The temporal and eternal effects of this love, 1 John 3:1.

3. Satisfaction and delight, Psalm 44:25. In all these ways love is spoken of
in relation to God. Now God loves himself and everything created by himself,
yet in such a way that he loves the better things among creatures more,
according to their degree of goodness; for those to which he has communicated
more goodness are more like him. Finally, God's love is eternal, immense, and
most constant.

*Uses of the doctrine.* 1. This serves for our consolation, since we know God
to be

[1620 Tome I | col. 202 | BSB frame 00117]

love itself.

2. Therefore God is the fountain of all love in us; and whoever does not love
God and his neighbor is deprived of this communion of love with God, who
continually gives rise from himself to love of neighbor.

3. God loves all things. Therefore creatures must not be abused according to
our whim, but must be treated with equity and moderation.

4. Since God especially loves the faithful, they must therefore be loved by
us more than others; and in pursuing their salvation and good, we must spare
neither ourselves nor our possessions.

5. God loves the better more. We must therefore devote ourselves to piety and
holiness, 1 Thessalonians 4:3.

6. Since God's love is gratuitous, let us be humble and, finally, certain of
salvation.

### On the Hatred of God

Hatred is the will of God by which he does not will—that is, does not approve,
but disapproves of evil and turns away from it, Psalm 48.85,[^p21-2] 1
Corinthians 10:5. He hates evils absolutely, but evil persons relatively,
insofar as they have been corrupted by sin. When hatred is attributed to God,
it has three meanings:

1. It signifies the denial of the benevolence that leads to eternal life, or
it signifies the purpose not to show mercy, Romans 9:13.

2. It signifies the decree to punish and the just punishment itself, Psalm
5:6 and Job 30:21.

3. It signifies displeasure at and detestation of evil, Psalm 45:8. In all
these ways it is rightly attributed to God.

*Uses.* 1. Therefore it is the greatest virtue to hate all ungodliness and
ungodly people insofar as they are ungodly. 2. Therefore the company of the
ungodly must be avoided, and friendship with enemies must not be cultivated,
2 Thessalonians 2:6.[^p21-3]

### On the Justice of God

Justice is the will of God by which God wills justly, or by which he is
inclined to give each his due, decreeing rewards for the good and punishments
for the evil.

[1620 Tome I | col. 203 | BSB frame 00118]

Deuteronomy 22:25, Psalms 11:7 and 119:13, and Psalm 145:17.

Justice has four meanings:

1. It signifies absolute goodness, or the collection of all virtues,[^p21-4]
1 Timothy 1:9; and this belongs to God alone.

2. It signifies integrity and sincerity, not absolutely but in accordance
with the person and station someone bears, Luke 1:6.

3. It signifies particular distributive or collective justice, which lies
partly in the distribution of honor, money, and so forth, and partly of right,
without partiality.[^p21-5]

4. It signifies faithfulness itself, or truth observed in sayings and
promises, 1 John 1:9. In these last two meanings it also properly belongs to
God. Thus, although God's justice is one and most simple, being God's very
essence, it is nevertheless called manifold because of these different
relations.

*Uses of the doctrine.* 1. Since God is justice itself, he must not be accused
of any injustice in his works, by word, or in thought.

2. Therefore, when God's will is known, we must not dispute whether it is good
or evil, just or unjust; rather, whatever he wills must be performed by us.

3. Since God is a just judge, let us beware of sin and shake off carnal
security.[^p21-6]

4. Since God is judge when he chastises us, it is right for us to submit
humbly to him, acknowledging our fault and seeking pardon, because he corrects
us unto salvation, Romans 5:3.

### On the Mercy of God

Mercy is the will of God by which he is inclined to aid the miserable, Psalms
86:5, 106:1, and 118:1, Jeremiah 3:11, and Ephesians 2:4; and it is eternal and
immutable. Mercy in God, however, is not what the philosophers define it to
be, namely, distress of mind conceived from another's misery. Rather, mercy in
God signifies two things:

[1620 Tome I | col. 204 | BSB frame 00118]

1. God's affection inclined toward showing mercy.

2. The effect of this affection, namely aid itself; and in God this is said to
be twofold:

1. General, toward all creatures, Luke 6:36.

2. Special, by which he has mercy upon the elect unto eternal life.

*Uses of the doctrine.* 1. From this we learn our misery, because we need
God's mercy.

2. In afflictions we must not despair, no matter who inflicts injuries upon
us, because God as it were suffers with us and therefore will come to our aid
in his own time.

3. Even if we fall into grave crimes, we must not despair of salvation,
because God is supremely merciful: he freely loved us in Christ when we were
his enemies. Therefore he will do so much more now that we have been
reconciled, Romans 5:10.

### On the Anger of God

Anger is the will of God by which he is inclined to punish sinners. In God it
is not a passion, but God's own most simple essence; and as it is attributed
to God in Scripture, it signifies three things:

1. God's certain and most just will and decree to avenge sin, John 3:36 and
Romans 1:18.

2. It signifies threats of punishments, Psalm 6:1 and Hosea 11:9.

3. The effects, or the punishments themselves, Romans 2:5, Ephesians 5:6, and
Matthew 3:7. God's anger is said to change not by reason of an affection in
God, but by reason of its effect and of our perception.

*Uses of the doctrine.* 1. Anger, therefore, is not simply an evil thing, but
only insofar as the faults of our minds are joined to it; for God, Christ, and
the apostles are said to grow angry. The faults of anger, however, must be
avoided:

1. We must not grow angry rashly. 2. We must not do so for private causes
rather than for vices considered as vices. 3. We must not leave the vice aside
and direct our anger against the person.

[1620 Tome I | col. 205 | BSB frame 00119]

2. Since God is angry at sins, carnal security and sins must be fled, and
repentance must not be deferred.

### On the Chastity of God

Chastity is the will of God by which he wills and approves purity consonant
with the order established by himself, and disapproves all impurity that
conflicts with this order, 1 Thessalonians 4:3.

*Use of the doctrine.* Since we are temples of the Holy Spirit, we must strive
to cleanse ourselves from every impurity, so that we may be perfect as our
Father is perfect, Matthew 5, last verse.

[End of Part 21. *On the Power of God* begins later in column 205 and is
excluded.]

[^p21-1]: The witness prints `Ps. 37.1.`; Psalm 73:1 appears to be intended.
[^p21-2]: The witness prints the malformed locator `Psal. 48.85.`; it is
    retained without conjectural correction.
[^p21-3]: The witness prints `2. Thess. 2.6.`; 2 Thessalonians 3:6 appears to
    be intended.
[^p21-4]: The witness prints `omnum`; the translation gives the apparent sense,
    `omnium` ("of all").
[^p21-5]: The witness prints `collectivam`, although the standard pairing here
    is distributive and commutative justice. The translation retains
    "collective" and renders the printed Greek `προσωποληψίαν` as "partiality."
[^p21-6]: The witness prints `excecutiamus`; the translation gives the
    apparent sense, `excutiamus` ("let us shake off").

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

## Printed anomalies in Part 12

- In Objection 1, column 136 prints `non posterius` twice. Both the Latin and
  English retain the duplicated “not the latter”; the apparent correction
  `non prius` / “not the former” is not silently introduced.
- The objection between Objections 2 and 4 is numbered `Obiect. 6` in column
  140, and another Objection 6 begins in column 151. The first apparent error
  for Objection 3 is retained in both paired files.
- Within the objection apparently intended as Objection 3, the printed
  instance sequence proceeds from 10 to 12 and then returns to 11. The order
  is retained.
- Column 148 prints the locators `Ioh. 21.1. & 26. 1. ad Cor. 26.2.`. They are
  retained, while the English notes that John 20:1, 26 and 1 Corinthians 16:2
  may have been intended.

## Printed anomalies in Part 13

- Column 153 prints `Matth. 28.9.10. & 29.` even though Matthew 28 has no verse
  29. The locator is retained and noted in the English.
- Column 157 prints Augustine, *City of God* `20.10`; the quoted statement is
  found in chapter 19. The printed chapter number is retained and noted in the
  English.
- Column 160 prints a second `Obiect. 12` and then proceeds to Objection 14.
  The sequence is retained rather than silently changing the second number to
  13.
- In the response to Objection 23, column 164 prints that the Council of
  Nicaea's condemnation of Arius “from Scripture” is false, although the
  surrounding argument appears to require “not from Scripture.” Both files
  retain the printed wording, and the English notes the anomaly.

## Printed anomalies in Part 14

- In Question I, column 172 prints `Isa. 57.24.`, although Isaiah 57 has no
  verse 24. The locator is retained and noted in the English.
- In Question II, column 174 prints `Deus` in the Tertullian quotation where
  the grammar and argument appear to require `Deos`. The Latin retains the
  reading, and the English notes its rendering of the apparent sense.
- In Question III, column 176 prints `Galat. 1.` for the occurrence of
  `φύσις`; Galatians 4:8 appears to be intended. The printed locator is
  retained and noted in the English.
- Column 177 prints `Exod. 13.15.` in the discussion of the divine name;
  Exodus 3:15 appears to be intended. The printed locator is retained and
  noted in the English.
- The Hebrew and small Greek types in columns 174–180 have been normalized to
  Unicode directly from the page images but should receive specialist
  collation before publication.

## Printed anomalies in Part 15

- In the first argument for divine simplicity, column 185 prints `Exodi 3.6.`
  for God’s calling himself *EST* without a predicate; Exodus 3:14 appears to
  be intended. The printed locator is retained and noted in the English.
- The Hebrew and small Greek types in columns 180–186 have been normalized to
  Unicode directly from the page images but should receive specialist
  collation before publication.

## Printed anomalies in Part 16

- In the treatment of eternity, column 189 prints `Gen. 23.33.`, although
  Genesis 23 has no verse 33; Genesis 21:33 appears to be intended. The
  printed locator is retained and noted in the English.
- In the treatment of immutability, column 190 prints `Numer. 33.23.`;
  Numbers 23:19 appears to be intended. The printed locator is retained and
  noted in the English.

## Printed anomalies in Part 18

- In the special knowledge of the elect, column 194 prints `2. Tim. 2.9.`;
  2 Timothy 2:19 appears to be intended. The printed locator is retained and
  noted in the English.
- In the account of God's knowledge of all things outside himself, column 195
  prints `Hebr. 4.31.`, although Hebrews 4 has no verse 31; Hebrews 4:13
  appears to be intended. The printed locator is retained and noted in the
  English.
- Among the proofs that divine wisdom belongs to God alone, column 196 prints
  `1. Reg. 8.29.`; 1 Kings 8:39, parallel to the next citation at 2 Chronicles
  6:30, appears to be intended. The printed locator is retained and noted in
  the English.
- The small Greek types in columns 194–196 have been normalized to Unicode
  directly from the page images but should receive specialist collation before
  publication.

## Printed anomalies in Part 19

- Column 197 prints `Num. 29.19.` in support of the immutability of God’s will;
  Numbers 23:19 appears to be intended. It also prints `Proverb. 29.21.`, where
  Proverbs 19:21 appears to be intended, and `Ezec. 9.28.`, although Ezekiel 9
  has no verse 28. All three locators are retained and noted in the English.
- Column 198 prints Lombard, *Sentences*, `lib. 1. distinctione 145.`; the
  apparent intended reference is book 1, distinction 45. The printed number is
  retained and noted in the English.
- Column 198 prints `1. Cor. 10.32.` for God’s willing his own glory before all
  things; 1 Corinthians 10:31 appears to be intended. The printed locator is
  retained and noted in the English.
- Column 199 prints `Habac. 1.43.`, although Habakkuk 1 has no verse 43;
  Habakkuk 1:13 appears to be intended. The printed locator is retained and
  noted in the English.
- Column 200 prints the anomalous phrase `Haec vnicas Dei voluntas`. The Latin
  retains `unicas` under the edition’s normalized `u/v` convention, while the
  English gives the apparent sense and records the wording in a note.
- The small Greek types in columns 197–198 have been normalized to Unicode
  directly from the page images but should receive specialist collation before
  publication.

## Printed anomalies in Part 20

- Column 200 prints `Iere. 0 10.` in the proofs of divine truth; Jeremiah
  10:10 appears to be intended. The printed locator is retained and noted in
  the English.

## Printed anomalies in Part 21

- Column 200 prints `Ps. 37.1.` for God's goodness toward others; Psalm 73:1
  appears to be intended. The printed locator is retained and noted in the
  English.
- Column 202 prints the malformed locator `Psal. 48.85.` in the definition of
  divine hatred. It is retained in both texts without conjectural correction.
- Column 202 prints `2. Thess. 2.6.` for avoiding the company of the ungodly;
  2 Thessalonians 3:6 appears to be intended. The printed locator is retained
  and noted in the English.
- Column 203 prints `omnum` where the sense calls for `omnium` ("of all"). The
  Latin retains the form and the English records its rendering.
- Column 203 prints `collectivam` in the conventional distinction between
  distributive and commutative justice. The Latin retains the word, while the
  English renders it literally as "collective" and records the likely issue.
- Column 203 prints `excecutiamus` where `excutiamus` ("let us shake off")
  appears to be intended. The Latin retains the form and the English notes its
  sense.
- The small Greek type `προσωποληψίαν` in column 203 has been normalized
  to Unicode directly from the page image but should receive specialist
  collation before publication.
