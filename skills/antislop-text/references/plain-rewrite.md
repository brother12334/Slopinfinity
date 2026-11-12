# The plain profile

Derived from comparing one academic paragraph with the output of Clever AI Humanizer
(a humanizer that runs a model trained on human-written text). The input, a polished
argumentative piece, was flagged as 100% AI. The output used the same facts in plain,
student-style explanatory prose. Use this profile when the text is academic or
informational and has to read as an ordinary person's writing rather than a polished
writer's.

This is one sample, so treat the numbers as targets to aim near, not laws.

## What changed, measured

| | Input (flagged) | Output |
|---|---|---|
| Average sentence | 23 words | 17 words |
| Longest sentence | 51 words | 34 words |
| Sentence length variation (CV) | 0.58 | 0.43 |
| Commas per sentence | 1.5 | 0.6 |
| Semicolons | 2 | 0 |
| Same facts, same length | 294 words | 292 words |

Polish and syntactic sophistication were the giveaway, not evenness. The output is
*flatter* than the input.

## The transformations

Apply in this order, sentence by sentence. Keep every fact (see the meaning lock below).

### 1. One idea per sentence

- Split at semicolons. Split two independent clauses joined by "and" or "but" when
  each carries its own fact.
- Long sentences (over about 30 words) become two or three.
- Keep sentence length mostly in the 9 to 25 word band. A couple of longer ones are fine.

> *"Bezos founded Blue Origin in 2000 and bought The Washington Post in 2013 for $250
> million; in July 2021, ... he flew to the edge of space"*
> → *"Bezos started his own aerospace company called Blue Origin in 2000. He also
> purchased The Washington Post in 2013 for $250 million. In July 2021, ..."*

### 2. Unpack embedded clauses

Appositives, participle phrases and clauses tucked between commas become plain main
clauses. Aim for well under one comma per sentence on average.

> *"Bezos, born in Albuquerque in 1964, had trained in ..."*
> → *"Bezos was born in Albuquerque in 1964 and had trained in ..."*

> *"Amazon Web Services, launched in 2006 to rent out computing infrastructure the
> company had first developed for its own use."*
> → what it is, where it came from, when it launched, who used it: four short sentences
> in that order.

### 3. Replace literary moves with plain explanation

Polished rhetorical constructions are what a model produces when asked to write well.
Swap them for the plain statement of what they mean.

| Polished | Plain |
|---|---|
| "accurate as far as it goes, but it obscures more than it explains" | "While this is technically true, it omits key details" |
| "Nor was X the most consequential thing" | "While X was important, arguably the most impactful thing ..." |
| "If X is now better understood as Y, the shift began there" | "This is where X can now be seen as more of a Y" |
| "complicate any single characterization" | cut, or "people have different views of him" |
| "diverge sharply ... divide along lines of" | "There are mixed opinions about" |
| "a question less about X than about Y" | "This is less to do with X and more to do with Y" |
| "not a leap in the dark" | "This was a strategic risk" |

Also drop: inversions ("Nor was", "Rarely has"), "as far as it goes", "in the long run",
"to be sure", antithesis pairs ("less X than Y"), and closing sentences built as aphorisms.

### 4. Everyday vocabulary

Keep the technical terms the subject needs. Replace the abstract, literary ones with the
words a student or professional would use in ordinary writing.

| Literary | Everyday |
|---|---|
| consequential | impactful, important |
| characterization | view, description |
| distinction | difference, credit |
| accumulated | gained, built up |
| complicate | make it harder to |
| documented | highlighted, reported |
| bought, founded | purchased, started (either is fine; match the register) |

Do not swap in rarer synonyms. The direction is toward common words, not unusual ones.

### 5. Explicit links between sentences

Short sentences need visible connections. Use the simple cohesion devices ordinary
writers use:

- "This" or "They" opening a sentence that refers back to the previous one
  (up to about a quarter of sentences is normal in this profile).
- "While", "However", "Also" at the start of a sentence.
- Spelled-out reasons: "as he expected ...", "due to ...", "This is seen as ...".

Make sure every "This" and "They" has a clear referent. Clever's output had two that
did not (see the meaning lock).

### 6. Explain in sequence

When a passage covers a thing, an event or a process, order it the way someone explains
it out loud: what it is, where it came from, when it happened, what came of it.

### 7. Ordinary conventions

These are acceptable variants that polished model prose tends to avoid. Use them where
they fit the register and stay consistent:

- numerals for small numbers ("2 weeks")
- the writer's own spelling convention (UK or US), applied throughout
- no serial comma
- common phrasings like "from a customer perspective", "things cheaper and easier"

Do not add actual errors. Clever's output contained some ("There is mixed opinions",
"high level job", "the Blue Origin New Shepard Capsule"); the `finish` pass corrected
them, and errors can cost marks in graded work.

## Meaning lock: what not to copy

Clever's output also did these, and the plain profile must not:

- **Dropped a fact** (Bezos becoming executive chair).
- **Overstated** a claim ("he knew the web would be growing" for "a calculated bet").
- **Lost attribution** ("This is seen as the trade-off", with no one doing the seeing).
- **Changed a term of art** ("antitrust doctrine" became "anti-trust laws").
- **Left unclear referents** ("rent their computing resources", where "their" pointed to
  the wrong noun).

After the rewrite, check every fact, claim, attribution, technical term and pronoun
against the original.

## Targets for the checker

`python3 scripts/rhythm_check.py <file> --profile plain` checks:

- no semicolons
- commas per sentence at or below about 0.9
- no sentence over 35 words
- none of the literary moves from section 3
- no voice or burstiness flags (this profile skips them on purpose)
