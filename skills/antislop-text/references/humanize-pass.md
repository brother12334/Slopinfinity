# The humanize pass

A rewrite of the Pass 1 draft in seven stages. The order matters: structure changes
make line edits moot, and the predictability stage only works on a draft that already
has a speaker.

Why drafts get caught: detectors score how predictable each word is given what came
before, and how even the text is overall. Readers feel the same two things as "smooth"
and "flat". A draft can be free of every listed tell and still be flagged when each
sentence is the most likely next sentence. Stages 3 to 5 are aimed at that.

Keep every fact from Pass 1. Change how it is said, never what is true.

## 1. Speaker card

Write this down before touching the draft (in your head, not in the output):

- **Register:** A casual, B work, C expository, D formal.
- **Who:** a specific person with a reason to write this. "A tech blogger who finds Bezos
  more interesting than likable", not "an informative writer".
- **To whom:** one reader. A friend, a class, a hiring manager, a forum.
- **Stance:** what the speaker thinks about the subject. Most human writing has one, even
  in reports. Neutral summary nobody asked for is the strongest flag there is.
- **Habits:** if the user gave a sample, take five concrete habits from it (average
  sentence length, how it opens, punctuation it likes, words it repeats, how blunt it
  is). Copy them. A real sample beats every other stage in this file combined; when the
  result has to read as one specific person's, ask for one.

## 2. Structure

- **Break the timeline.** Encyclopedia order (born, studied, founded, expanded, retired)
  is the most predictable shape there is. Open on the most interesting fact or the
  speaker's angle, then circle back for the background.
- **Point first.** The first sentence does work. No warm-up, no "X is one of the most".
- **Uneven paragraphs.** One long, one short. Equal blocks read as generated.
- **No recap ending.** Close on a detail, an opinion or the last real point, not on a
  summary of the legacy, the impact or the journey.
- **Bullets only for real lists.** Arguments go in paragraphs.

## 3. Surface tells (mechanical, always fix)

| Tell | Fix |
|---|---|
| Em dash | Comma, period, parentheses or colon, whichever the speaker would use |
| "not just X but Y", "it's not X, it's Y" | State Y |
| delve, tapestry, testament, leverage, seamless, robust, elevate, unlock, landscape, realm, foster, pivotal, cornerstone, transformative, multifaceted | The plain word |
| "one of the most influential", "left an indelible mark", "a complex legacy" | A specific claim, or cut |
| "In today's fast-paced world", "In an era of" | Cut |
| "Ultimately", "In conclusion", "Overall" wrap-ups | Cut the recap |
| ", signaling / highlighting / underscoring / reflecting ..." tails | Its own sentence, or cut |
| "while also", "on one hand ... on the other" | Pick a side or say what it depends on |
| "Moreover", "Furthermore", "Additionally" openers | Nothing, or and/but/so/also |
| **Bold label:** sentence, emoji bullets, Title Case Headings | Plain sentences, sentence case |
| "Great question", "I hope this helps", "Let me know if" | Cut |

Never swap a tell for its sibling (delve to dive, dash to ellipsis).

## 4. Predictability (the stage that beats detectors)

Go sentence by sentence. For each one ask: *if I covered this sentence and guessed it
from the one before, would I guess it?* If yes, change it, using whichever of these fits:

- **Second-choice phrasing.** Write the phrase that came to mind first, then use a
  different one that is just as natural and more specific. "Expanded into many markets"
  becomes "started selling groceries, of all things". Not a thesaurus swap: a rarer word
  that is wrong or stiff is worse than the common one.
- **Concrete over abstract.** Name the actual thing. "Cloud computing" becomes "renting
  out the servers it had built for itself". "Criticism over working conditions" becomes
  what the criticism actually is.
- **Collocation breaks.** Stock pairs (rapid growth, significant impact, key role, wide
  range, stable job) are the most predictable two-word units in English. Replace the pair
  or drop the adjective.
- **Speaker reactions.** Where the speaker would react, let them: "which for him was small
  change", "of all things", "oddly enough". One or two per paragraph, not every sentence.
- **Idiom and register-native phrasing.** "kicked himself upstairs", "not bad for", "the
  guy" in register A to C. These are low-probability for a model and normal for people.
- **Unexpected-but-true connections.** Link two facts the draft kept apart ("he flew to
  space two weeks after leaving the CEO job").
- **Information-density changes.** Models put one fact in every clause. People slow
  down on what they find interesting and race through the rest in one line.

## 5. Sentence shape

Text of only plain declaratives is flagged even when the lengths vary. Use the shapes the
speaker would actually use, and for register A to C use at least three of these in any
piece over about eight sentences:

- a question (rhetorical or real)
- an aside in parentheses
- a colon or semicolon
- a sentence starting with And, But or So
- a fragment that lands a point ("Not bad for a bookstore.")
- a sentence that ends on a preposition, or uses "who" where a grammar book says "whom"
- a long sentence that strings clauses with "and" the way speech does

Also vary openers (not subject-first every time, never three in a row with the same
word), and mix lengths: something under 6 words and something over 30 in any piece
over 150 words.

## 6. Grammar the way people use it

Correct, but not textbook-stiff. Contractions in A to C. "Who" for "whom" in casual and
work registers. Starting with "But" or "And" is fine. A split infinitive is fine. These
are real usage, not errors. Never add actual mistakes: misspellings, wrong words, broken
agreement. Readers notice them and detectors look for planted ones.

## 7. Over-correction check

The rewrite should not land in the "trying not to sound like AI" voice:

- not every sentence short, not every sentence quirky
- no forced lowercase or dropped capitals outside register A
- no "look,", "here's the thing", "real talk", "honestly," cold opens
- no slang or swearing the speaker would not use
- reactions and idioms are seasoning: a couple per paragraph at most
- no invented anecdotes, quotes, numbers or first-person experiences. Opinions are
  fine; made-up memories presented as real are not. When a personal detail would help
  and the user hasn't given one, leave it out or ask.
