---
name: antislop-text
description: Three-pass workflow that makes any writing read as written by a person. Pass 1 does the task normally and gets the substance right. Pass 2 runs a humanizer rewrite (pin a voice, cut the known AI tells, fix rhythm, add real specifics). Pass 3 checks the result for detail, wording, grammar and context, scans it, and fixes what is wrong before delivering. Use whenever writing or rewriting prose a person will read (essays, posts, emails, messages, cover letters, bios, product copy, READMEs, replies), and whenever the user says it sounds like AI or ChatGPT, is too polished, robotic or generic, asks to humanize it, make it sound like them, or make it pass an AI detector. Trigger even if they never say "AI".
argument-hint: "[write <task> | humanize <text or file> | check <text or file> | finish <text or file>] [--style normal|structured|academic]"
---

# antislop-text

Every piece goes through three passes before it reaches the user. Do not skip a pass and
do not show the intermediate drafts unless asked.

| Command | Runs |
|---|---|
| `write <task>` (default) | Pass 1, 2, 3 |
| `humanize <text or file>` | Pass 2, 3 on text the user supplies |
| `check <text or file>` | Pass 3 only, report without rewriting |
| `finish <text or file>` | Minimal-edit Pass 3 on text from an external humanizer (see below) |

## Styles

Pick one from the request, or ask when it is unclear. It sets the register for Pass 2.

| Style | For | Register | Scanner flag |
|---|---|---|---|
| `normal` (default) | Blog posts, social posts, emails, product copy | A or B/C, friendly and plain | none |
| `structured` | Reports, summaries, documentation, work updates | B/C, clean structure over vocabulary, short paragraphs, headings when long | none |
| `academic` | Essays, papers, literature reviews | D, no contractions, a clear argument, real hedges ("arguably"), real citations only | `--formal` |

## Pass 1. Do the task normally

Write the piece the way you would without this skill. All attention goes to substance:
answer what was asked, get the facts right, cover what the reader needs, in a sensible
order. Do not worry about style yet. A humanizer cannot rescue a draft that says nothing
or gets things wrong, so this pass is where correctness lives.

Before writing, note four things (silently, unless the user needs to weigh in):

- **Register.** A casual (texts, DMs), B conversational-professional (work email, Slack),
  C expository (essays, posts, articles), D formal (papers, briefs, specs). This decides
  what "natural" means for the rest of the workflow.
- **Speaker.** Who is talking, to whom, why they care. If the user gave a writing sample,
  that is the voice. Anchor to it closely: sentence length, vocabulary, how blunt they are.
- **Claim.** The one thing the piece asserts or achieves, in a sentence.
- **Facts.** Everything the piece must contain. Pass 3 checks these survived.

## Pass 2. Humanize

Rewrite the Pass 1 draft through the seven stages in
[references/humanize-pass.md](references/humanize-pass.md):

1. **Speaker card.** Register, who is talking, to whom, their stance, their habits. A
   writing sample from the user beats everything else; ask for one when the text has to
   pass as a specific person's.
2. **Structure.** Break encyclopedia order, put the point first, make paragraphs uneven,
   cut the recap ending.
3. **Surface tells.** The mechanical fixes from [references/tells.md](references/tells.md)
   Part A: em dashes, "not just X but Y", the diction memes, ", signaling..." tails,
   "while also" balance, wrap-ups.
4. **Predictability.** Sentence by sentence: if you could guess it from the sentence
   before, change it. Second-choice phrasing, concrete nouns, broken stock pairs, speaker
   reactions, register-native idiom, uneven information density.
5. **Sentence shape.** Questions, asides in parentheses, colons, And/But/So openers,
   fragments, long run-on-style sentences, varied openers and lengths.
6. **Grammar the way people use it.** Contractions, who for whom, conjunction starts.
   Never real errors.
7. **Over-correction check.** No costume casualness, no invented anecdotes or quotes.

## Pass 3. Check and fix

Run both scanners on the Pass 2 text (write it to a scratch file first if needed):

```bash
python3 scripts/unslop_text_scan.py <file>   # word-level tells; exit code = high-severity count
python3 scripts/rhythm_check.py <file>       # rhythm, sentence shapes, voice, predictable structure; exit code = flags
python3 scripts/rhythm_check.py <file> --formal   # register D: skips the voice checks
```

Then read the whole piece against [references/review-checklist.md](references/review-checklist.md),
through four lenses:

- **Detail.** Every fact from Pass 1 is still there and still true. Nothing was invented
  in Pass 2 (no fake anecdotes, quotes, numbers or sources presented as real). Specifics
  are specific.
- **Wording.** No tells left, no new ones introduced, no word repeated awkwardly, every
  word one the speaker would say.
- **Grammar.** Correct spelling, agreement, tense and punctuation. Fragments only where the
  register allows them and they are clearly on purpose. Clean grammar is not a tell; errors
  are just errors.
- **Context.** It answers the actual request, fits the medium and length, holds one
  register throughout, and means the same thing the Pass 1 draft meant.

Fix every problem found, then rerun both scanners. Stop when the word scanner shows 0
high-severity findings, the rhythm checker shows no HIGH flag and at most one MEDIUM, and
the checklist passes. Allow up to three rounds.

Then do one last predictability read: go through the final text and, for each sentence,
ask whether a model would have written exactly that next. Rewrite any that it would. The
scripts can't measure word-level predictability, so this read is what covers it. If a flag is a deliberate choice (the user loves em dashes, a legal brief is
formal on purpose), keep it and mark the line `unslop-ignore`.

## Finishing external humanizer output

Some humanizers run a model trained on human writing, which a written workflow cannot
match. When the user runs a draft through one and brings the result back, use
`finish`. The goal is to repair, not restyle: rewriting the output in your own words
puts model phrasing back in.

1. **Meaning lock.** Compare against the Pass 1 draft (or the user's original) and list
   every fact, number, name, citation and claim. Restore anything lost or changed.
2. **Real errors only.** Fix grammar mistakes, wrong words, broken sentences, mangled
   terms of art, and wrongly swapped synonyms ("cardinal" for "key", "pecuniary" for
   "financial").
3. **Leave the rest.** Keep their sentence structure and word choice even where yours
   would differ. Do not "improve" anything that is correct.
4. **Report the edits.** List each change in one line (original, then fixed, then the
   reason) so the user can undo any of them.

Run `unslop_text_scan.py` only for em dashes and assistant boilerplate. Skip the rhythm
checker, because rhythm is the humanizer's job here.

## Delivering

Give the user the final text only. Add at most one line after it, and only when it
matters: an assumption you made about voice, or a fact they should confirm. Do not
narrate the passes, list what you changed, or offer more versions unless asked.

## About AI detectors

Detectors mostly measure predictability: how expected each word is, how even the
sentences are, how uniform the structure is. Stages 4 and 5 target exactly that, and so
do the voice and shape checks in `rhythm_check.py`. No workflow can promise any detector's
verdict, though. Detectors disagree with each other, change often and misflag plenty of
human writing. Three things make a flag more likely whatever you do:

- **Short texts.** Under about 250 words, detectors are unreliable either way.
- **Encyclopedic topics.** A factual bio or definition reads like reference text even
  when a person wrote it, so it needs a stronger speaker and stance.
- **No real voice.** Without a sample from the user, the speaker is still one the model
  invented. A paragraph or two of the user's own writing to copy is the best upgrade.

When the user reports a flag, ask which detector it was and rerun Pass 2 from stage 1
with a stronger stance, rather than tweaking words.

Do not use tricks aimed only at detectors: invisible or zero-width characters, look-alike
Unicode letters, deliberate typos, random synonym swaps. They corrupt the text, readers
notice them, and detectors now look for them specifically. Better writing is the method
that holds up.
