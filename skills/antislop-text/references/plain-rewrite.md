# The plain profile

Derived from seven input/output pairs run through Clever AI Humanizer, a humanizer that
runs a model trained on human-written text. The inputs were typical model-written
paragraphs in six registers: academic history, science explanation, opinion essay,
casual blog, business report, personal statement, plus an academic argument that a
detector had flagged at 100%. The pairs live in `research/clever-samples/`, and
`python3 research/compare_pairs.py` re-measures them whenever more are added.

## What it changes, measured

| Signal | Input mean | Output mean | Pairs that moved this way |
|---|---|---|---|
| Commas per sentence | 1.56 | 0.46 | 7 of 7 (every output at 0.71 or below) |
| Serial commas ("X, Y, and Z") | 1.4 | 0 | 7 of 7 |
| Formal words (moreover, pivotal, facilitated...) | 4.3 | 0 | every pair that had any |
| ", ...ing" clauses | 1.4 | 0.1 | 6 of 7 |
| Average word length | 5.55 | 5.06 | 7 of 7 |
| Words with 3+ syllables | 24% | 16% | 6 of 7 |
| Average sentence length | 21.5 | 17.9 | 5 of 7 |
| Sentence-length variation (CV) | 0.30 | 0.29 | no consistent change |
| Word count | 155 | 149 | about 4% shorter |

## What it does not change

This matters as much as what it does change. Clever does not:

- reorder the paragraph or restructure the argument
- add a voice, opinions, asides, questions or personal detail
- make sentence lengths more varied
- add or remove ideas on purpose (it does lose some, see the meaning lock)

It rewrites **sentence by sentence, in the original order**, mostly one sentence to one
sentence, sometimes splitting one into two. The polish comes out; the content and shape
stay.

## The transformations

Apply in order, one sentence at a time.

### 1. Strip the commas

The strongest signal by far. Target: under 0.8 commas per sentence.

- **Unpack appositives and tucked-in clauses** into plain main clauses or their own sentence.
  - *"chloroplasts, specialized organelles containing the green pigment chlorophyll, which
    absorbs light"* → *"the chloroplast organelles, where there is a green pigment called
    chlorophyll. Chlorophyll absorbs light"*
- **Drop the serial comma.** *"concentration, mood, and academic performance"* →
  *"concentration, mood and overall grades"*
- **Drop optional commas after short opening phrases.** *"When I first moved out on my
  own, I relied"* → *"When I first moved out I would often"*; *"Overall the printing press"*
- Keep commas that prevent a misreading.

### 2. Turn ", ...ing" tails into plain links

| Input | Output |
|---|---|
| ", demonstrating strong operational resilience" | ". This means they had a high level of resiliency." |
| ", making it biologically difficult for them to" | "meaning that they cannot naturally" |
| ", allowing scholars in different countries to work from" | "as scientists across the world were working off" |
| ", indicating areas for improvement" | cut |

### 3. Replace formal and abstract words with everyday ones

Every sample removed every formal connector and most abstract nouns. Real swaps from the
samples:

| Formal | Everyday |
|---|---|
| fundamentally transformed the circulation of knowledge | had a huge impact on the sharing of knowledge |
| This proliferation of printed material | The increase in printed books |
| facilitated the development of modern science | meant that modern science could develop |
| was primarily driven by | was due to |
| inquiries related to invoice formatting | questions about the way the invoicing was laid out |
| temporarily reallocating two agents | temporarily moving 2 agents |
| chronically sleep-deprived | not get enough sleep |
| Critics argue that | Some people say that |
| these logistical concerns, while valid, | despite this being true |
| collaboration, perseverance, and creative problem-solving | teamwork, perseverance and creative thinking |
| I am eager to bring this dedication | I am excited to bring this enthusiasm |
| certain bacteria / specialized organelles | some bacteria / organelles |
| developed by | invented by |
| expensive | costly |

Cut outright: *Moreover, Furthermore, Ultimately, Additionally, consistently,
dramatically, significantly.* Keep *However*. A closing sentence starting with
*Overall* is normal in this profile (3 of 7 samples added one).

Not every swap is shorter or simpler ("sluggish" became "lethargic"). The direction is
toward the word an ordinary writer reaches for, not the shortest one.

### 4. Put a person or a thing, not an abstraction, in the subject

- *"Learning to cook has been one of the most rewarding experiences of my adult life"*
  → *"One of the most rewarding things I have learnt as an adult is cooking"*
- *"My passion for environmental engineering began during"* → *"I became interested in
  environmental engineering when I"*
- *"The printing press, developed by Johannes Gutenberg around 1440, fundamentally
  transformed"* → *"The printing press was invented by Johannes Gutenberg in around 1440
  which had a huge impact"*

### 5. Plain intensifiers and evaluations

Outputs used everyday emphasis the inputs avoided: *huge, extremely, really, very, quite,
actually, definitely, much quicker, a lot*. One or two per paragraph, never stacked.

### 6. Split only where a sentence carries two ideas

Average length dropped in 5 of 7 pairs, but one stayed flat and one got longer when two
short sentences merged. Length is not the target; commas and formality are. Do not chop
everything into short sentences, and do not try to vary length on purpose.

### 7. Everyday conventions

- Numbers as numerals: *fifty years* → *50 years*, *two agents* → *2 agents*.
- Common abbreviations: *in the third quarter* → *during Q3*; *11 p.m.* → *11pm*.
- One spelling convention throughout. Clever defaulted to UK English (learnt,
  civilisation, flavouring, takeaways); match the writer's own convention instead.
- Simple sentence openers repeat freely: *The ... The ...*, *This ... This ...*, the topic
  word twice. Do not vary openers for the sake of it.

## Meaning lock: what not to copy

Clever lost or bent something in 6 of 7 samples. The plain profile keeps the
simplification and refuses the damage:

| Sample | What Clever did | Rule |
|---|---|---|
| History | dropped "an estimated" (20 million became a hard fact); dropped literacy being confined to clergy and the elite | keep hedges that carry real uncertainty; keep every fact |
| Science | "Making it one of the most important processes." as a fragment; "earth" lowercase | no fragments in academic register; keep proper nouns |
| Opinion | "8:30 or later" became "8.30am"; "reported improvements" became "have seen"; "because, research"; "students concentration" | keep ranges and attributions exact; no punctuation errors |
| Blog | none found | |
| Business | "the team experienced an increase in ticket volume" became "Customer Support increased ticket volume" (the team did not cause it); dropped "slightly" | keep who did what; keep qualifiers that change the meaning |
| Personal statement | dropped "make a meaningful impact in my community"; "highschool"; "how important teamwork ... is" | keep every point the writer makes; spelling and agreement correct |
| Bezos | dropped "executive chair"; "knew" for "a calculated bet"; "doctrine" became "laws"; unclear "their" | keep terms of art; every pronoun needs a clear referent |

After the rewrite, check every fact, number, range, qualifier, attribution, technical
term and pronoun against the input. Optional commas may go; real errors may not.

## Checker targets

`python3 scripts/rhythm_check.py <file> --profile plain` flags, from the sample data:

| Check | Target | Severity |
|---|---|---|
| Commas per sentence | 0.8 or less | MEDIUM over 0.8, HIGH over 1.3 |
| Serial commas | 0 | MEDIUM |
| Formal words | 0 | MEDIUM, HIGH at 3+ |
| ", ...ing" clauses | 0 | LOW for 1, MEDIUM for 2+ |
| Semicolons | 0 | MEDIUM |
| Sentences over 35 words | none | MEDIUM |
| Literary moves (Nor was, as far as it goes...) | none | MEDIUM |
| Words with 3+ syllables | 24% or less | LOW |

On the seven samples, every input gets at least two HIGH or MEDIUM flags and every Clever
output gets none. The thresholds were tuned on those same samples, so treat new pairs as
the real test and re-run `research/compare_pairs.py` as they come in.

The voice-profile checks (sentence-length variety, sentence shapes, repeated openers,
contractions) are switched off in this profile, because the samples show Clever does not
do any of them.
