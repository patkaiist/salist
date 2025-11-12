# SALIST

The _Sal Area Lexical Inventory for Sino-Tibetan_ (SALIST, "Sal-list") is an multi-stage concept list designed for lexical data collection and comparison in the Patkai range and surrounding areas, specifically for languages which may be included within the the proposed Sal subfamily within Sino-Tibetan (Burling 1983). 

## Goals

The SALIST has two goals:

1. Provide a regionally appropriate multi-stage concept list for lexical elicitation
2. Create an easily extensible set of unique internal concept identifiers, cross-linked to standard concept lists where possible

The list is meant to serve as both a tool to those undertaking documentation work in the region, as well as for phylogenetic analysis of Sal and neighbouring varieties in order to better categories relatedness within the cluster. Concepts are ranked into stages based on pecieved usefulness for historical reconstruction, phylogenetic analyses, and investigations into semantic shifts in the history of the langauges of the region.

Additionally, the concepts aim to track fine-grained semantic distinctions where other concept lists may lack specificity. For this reason, the SALIST is constantly expanding. Versions are tracked in this repository, and, when citing the concept list, the appropriate version should be considered. By having such narrow-grained distinctions in the concepts listed here, we hope that the concept IDs may also prove useful as internal concept identifiers for lexicographical work documenting the languages of the region. For example, while `carry` may occur in a general sense, the SALIST also contains unique concepts for any verb which may be translated as "carry" in English, in order to maintain the maximal number of distinctions. This helps in assessing semantic drift across the region, as well as in establishing etymological origins of the terms used.

| slno | concept_id              | name                     | gloss |
|------|-------------------------|--------------------------|-------|
| 868  | carry..child.on.back:to | to carry (child on back) | carry |
| 869  | carry..general:to       | to carry (general)       | carry |
| 870  | carry..in.arms:to       | to carry (in arms)       | carry |
| 871  | carry..in.bag:to        | to carry (in bag)        | carry |
| 872  | carry..in.hand:to       | to carry (in hand)       | carry |
| 873  | carry..in.pocket:to     | to carry (in pocket)     | carry |
| 874  | carry..on.back:to       | to carry (on back)       | carry |
| 875  | carry..on.head:to       | to carry (on head)       | carry |
| 876  | carry..on.pole:to       | to carry (on pole)       | carry |
| 877  | carry..on.shoulder:to   | to carry (on shoulder)   | carry |
| 878  | carry..under.arm:to     | to carry (under arm)     | carry |

Where possible, the concepts are cross-linked to those of the [CONCEPTICON](https://concepticon.clld.org/).

## Stages

The concept list is divided into stages, with the shorder lists focused on concepts which may prove most useful for comparative and diagnostic purposes. The stages include 30, 100, 350, 500, and 1000 concepts, with the full list currently containing over 2,650 concepts.

SALIST 30 is specifically developed for the purposes of determining whether or not a given language of the region belongs to the Patkaian branch of Tibeto-Burman. SALIST 100 and above are for more general lexicostatistic comparisons and historical reconstruction.


## Design principles

(This section is still being written)

1. **Specificity is preferred over generality**, but not to the point of projecting it where it is not coded in the data. General terms should be used only in cases where specificity cannot be determined, as in "Greater hornbill" versus "hornbill (general)".
2. **Verb stems take precendence over noun stems** in cases where a concept may occur as both in English. "To be hungry" is considered more basic than "hunger (sensation)". This is based on local typological features, where the latter is almost always derived from the former. However, verbs are always affixed with "to (be)".

## Definitions

Definitions are still being refined for concepts as our understanding of the regions languages improves. For the time being, we try to follow those given in [CONCEPTICON](https://concepticon.clld.org/) for parallel concpts.

## Structure

SALIST concepts are defined in English, with glossing or short definitions definitions also given in in Hindi, Assamese, Mandarin, and Burmese, with Nagamese intended to be added in a future version.

Each concept has a unique numerical identifier, a unique concept, the format of which is described in the following section, a plain-English name based on that form, and a simplified form for interlinear glossing. The numerical identifier is not the primary index, however. It is there for convenience, but is likely to change. Instead, the string ID should be taken as the primary identifier.

### ID format

Concept IDs are not numerical but rather intended to exist as statiut easily-readable strings that include the potential for formatting information and notes, while still being quickly sortable and modifiable as needed.

The purpose of this system is so that I can quickly type out detailed concept IDs to keep things distinct in the database while also having readily formatted versions for both a concept name and a gloss. These dot-formatted IDs are used internally for cross-linguistic databases that I work with for documentation and typological purposes. It is meant to allow like-concepts to be grouped together as part of the unique concept identifierr without cluttering a display name or gloss. Importantly, the system is meant to provide a single string which: conveys the meaning unambiguously at a glance through the inclusion of relevant notes; can be converted quickly via regex to a plain human-readable concept name; can be converted via regex to a simple interlinear glossing form. It is thus meant to allow a single column to represent multiple visual forms of a concept.

For example, `bee` and `bee.:hornet` should reaonsably be connected semantically, but "bee" should not be part of a gloss or simple name for the concept. Likewise `bee::hive` includes a separator that still links it to a semantic "bee" region in the list, and `bee..general` flags the concept as the most general term for bees while not needing to include that as part of a gloss. Use of the double colon should align with morpheme boundaries, thus `bee::s::wax` rather than `bees::wax` or `bee::swax`.

Verb stems are explicitly marked with `:to` in all cases, without exception, reducing ambiguity in the concept naming. Any concept which may be ambiguous, such as `smoke`, can be immediately understood as a noun in the absence of `:to`.

Outside of the formatting itself, but related to the form in which concept IDs exist, all ambiguous concepts require some form of additional information in the ID to prevent confusion. A concept `spicy` may be misinterpreted in elicitation based on one's dialect of English to mean "having a great amount of spices". This is resolved by appending `..of.chilis`. While many such ambiguities should also be clear in the corresponding definitions for each comment, by including such information in the concept ID itself, there is one less possible point of confusion for those conducting the elicitation and data coding.

This also allows for quick assignment or filtering for semantic categories. For example, most RICE nouns will begin with `rice:` or `rice.`. Thus `/rice[\.\:]+/` can be used to filter and assign tags to all such terms. 

An important principle of the system is that ambiguity is always avoided. Verbal concepts should have `:to`, nouns which are homophones in English will not. Concepts such as "to cry" will be clearly disambiguated between crying out in pain `cry.out:to`, to signal someone vocally `call.out:to`, to give a war cry `war.cry:to.give`, and to weep `weep:to`. Similarly, soil, ground and earth in the metaphysical sense are all distinguished, though often may have the same term in the target language.

## Dot notation conventions

```
:       swap order of items in the gloss or name
:.      display only items to the left in the gloss or name
.:      display only items to the right in the gloss or name
::      separator for semantic concept sorting
..      parenthetical in name
:::     Linnean taxonomy formatting
...     separate gloss form to the right of the ellipsis
```

The basic table looks like this, with all **name** and **gloss** values being automatically generated from the concept ID itself:

| concept | name | gloss | conc_id | conc_name |
|--------------------------|------------------------|---------------|--------:|-----------|
| bee::hive | beehive | beehive | 88 | BEEHIVE |
| bee.:hornet | hornet | hornet | 3261 | HORNET |
| bee..general | bee (general) | bee | 665 | BEE |
| big:to.be | to be big | big | 1202 | BIG |
| bitter:to.be | to be bitter | bitter | 887 | BITTER |
| blanket | blanket | blanket | 806 | BLANKET |
| blind:to.be | to be blind | blind | | |
| blood | blood | blood | 946 | BLOOD |
| blunt..of.edge:to.be | to be blunt (of edge) | blunt | 379 | BLUNT |
| blunt..of.point:to.be | to be blunt (of point) | blunt | 379 | BLUNT |
| bone | bone | bone | 1394 | BONE |
| bos.frontalis..mithun::: | _Bos frontalis (mithun)_ | bos.frontalis | – | – |
| bos.gaurus..gaur::: | _Bos gaurus (gaur)_ | bos.gaurus | – | – |

The easiest way to use this right now is in a spreadsheet. In a spreadsheet, the concept value is easily converted to the name with this:

```
=SUBSTITUTE(REGEXREPLACE(REGEXREPLACE(REGEXREPLACE(REGEXREPLACE(REGEXREPLACE(REGEXREPLACE(REGEXREPLACE(IF(RIGHT(A1,3)=":::", UPPER(LEFT(E886,1))&MID(E886,2,LEN(E886)-4), E886),"([a-z]+)\.\.\.([a-zA-Z .]+)","$1"),"([0-9a-z.]+)\:\.([0-9a-z.]+)","$1"),"([0-9a-z.]+)\.\:([0-9a-z.]+)","$2"),"([a-z.]+)\:\:([a-z.]+)","$1$2"),"([a-z.]+)\:([a-z.]+)","$2.$1"),"([0-9a-z.]+)\.\.([0-9a-zA-Z.\/]+)","$1 ($2)"),"([a-z.]+)\:([a-z.]+)","$2.$1"),"."," ")
```

The name can then be converted to the gloss with this:

```
=TRIM(REGEXREPLACE(REGEXREPLACE(LOWER(SUBSTITUTE(SUBSTITUTE(REGEXREPLACE(REGEXREPLACE(A1,"^to be ",""),"^to have ","")," of bird","")," ",".")),"^to ",""), "\.\([^)]*\)", ""))
```

Adjustments will be made to the glossing format, however, in order to simplify string lengths. This is a work in progress.

## References 

- Burling, Robbins (1983), "The Sal Languages" (PDF), Linguistics of the Tibeto-Burman Area, 7 (2): 1–32.