---
name: antislop-text
description: Three-pass workflow that makes any writing read as written by a person. Pass 1 does the task normally and gets the substance right. Pass 2 runs a humanizer rewrite (pin a voice, cut the known AI tells, fix rhythm, add real specifics). Pass 3 checks the result for detail, wording, grammar and context, scans it, and fixes what is wrong before delivering. Use whenever writing or rewriting prose a person will read (essays, posts, emails, messages, cover letters, bios, product copy, READMEs, replies), and whenever the user says it sounds like AI or ChatGPT, is too polished, robotic or generic, asks to humanize it, make it sound like them, or make it pass an AI detector. Trigger even if they never say "AI".
argument-hint: "[write <task> | humanize <text or file> | check <text or file>]"
---

# antislop-text

Every piece goes through three passes before it reaches the user. Do not skip a pass and
do not show the intermediate drafts unless asked.

| Command | Runs |
|---|---|
| `write <task>` (default) | Pass 1, 2, 3 |
| `humanize <text or file>` | Pass 2, 3 on text the user supplies |
| `check <text or file>` | Pass 3 only, report without rewriting |

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

Rewrite the Pass 1 draft with [references/humanize-pass.md](references/humanize-pass.md).
In order:

1. Restructure so the order follows the point, not intro, three even bodies, conclusion.
   Cut the summary ending and the warm-up opening.
2. Remove the surface tells in [references/tells.md](references/tells.md) Part A: em dashes,
   "it's not just X, it's Y", delve/tapestry/leverage diction, bolded lead-in labels,
   hollow openers, trailing offers, emoji bullets, needless bullet lists.
3. Fix the structural tells in Part B: uneven the rhythm on purpose, commit instead of
   hedging, drop the reflexive rule of three, use contractions where the register allows,
   cut sycophancy, delete any sentence that says nothing.
4. Add real texture: concrete specifics in place of generalities, an actual opinion where
   the speaker would have one, the plain word over the impressive one.

Do not over-correct into the "trying not to sound like AI" voice: all-short fragments,
forced lowercase, bolted-on slang, a "look," or "honestly," cold open, ellipses where
dashes were. That is a newer default and reads as fake just as fast.

## Pass 3. Check and fix

Run both scanners on the Pass 2 text (write it to a scratch file first if needed):

```bash
python3 scripts/unslop_text_scan.py <file>   # word-level tells; exit code = high-severity count
python3 scripts/rhythm_check.py <file>       # sentence rhythm, openers, repetition; exit code = flags
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

Fix every problem found, then rerun both scanners. Stop when the high-severity count is 0,
the rhythm checker has no high flags, and the checklist passes. Two fix rounds is normally
enough. If a flag is a deliberate choice (the user loves em dashes, a legal brief is
formal on purpose), keep it and mark the line `unslop-ignore`.

## Delivering

Give the user the final text only. Add at most one line after it, and only when it
matters: an assumption you made about voice, or a fact they should confirm. Do not
narrate the passes, list what you changed, or offer more versions unless asked.

## About AI detectors

Detectors mostly measure predictability: very common word choices, even sentence lengths,
uniform structure. This workflow targets the same properties, because they are also what
make readers say "this sounds like AI". It cannot promise any detector's verdict.
Detectors disagree with each other, change often and misflag plenty of human writing.

Do not use tricks aimed only at detectors: invisible or zero-width characters, look-alike
Unicode letters, deliberate typos, random synonym swaps. They corrupt the text, readers
notice them, and detectors now look for them specifically. Better writing is the method
that holds up.
