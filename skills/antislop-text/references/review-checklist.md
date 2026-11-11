# Pass 3 checklist

Read the full piece once from top to bottom, out loud in your head, before checking items.
Anything that made you slow down or wince is a problem even if no item below names it.

## Detail

- [ ] Every fact, name, number, date and requirement from Pass 1 is present.
- [ ] Nothing changed meaning in the rewrite (a hedge removed where the claim really was
      uncertain, a number rounded wrongly, a qualifier lost).
- [ ] Nothing was made up: no invented anecdote, quote, statistic, source or credential.
- [ ] Specifics are specific. Any "various", "many", "a range of", "numerous" either
      becomes concrete or goes.
- [ ] Names, product terms and jargon are spelled and capitalized the way their owners do.

## Wording

- [ ] `unslop_text_scan.py` reports 0 high-severity findings (or each is marked as deliberate).
- [ ] No sibling replacements (dive for delve, ellipsis for dash, "all in all" for "in conclusion").
- [ ] No word or phrase repeated close together unless on purpose. `rhythm_check.py` lists
      repeated three-word phrases.
- [ ] Each word is one this speaker would actually use in this register.
- [ ] No filler intensifiers: really, truly, incredibly, extremely, absolutely, deeply.
- [ ] Transitions are plain and only where needed.

## Grammar and mechanics

- [ ] Spelling, subject-verb agreement, tense consistency, pronoun reference.
- [ ] Punctuation: commas around non-restrictive clauses, no comma splices unless the
      register is A and it is clearly voice, apostrophes right, quotes closed.
- [ ] Fragments are deliberate and native to the register.
- [ ] One spelling convention throughout (US or UK), matching the user.
- [ ] Formatting fits the medium: no markdown in an email or text message, headings only
      in documents long enough to need them.

## Rhythm

- [ ] `rhythm_check.py` shows no HIGH flag. Sentence-length CV is about 0.45 or higher for
      registers A to C (formal D can sit a bit lower).
- [ ] At least one short sentence and one long one in any piece over about 8 sentences.
- [ ] No streak of three sentences with the same opener.
- [ ] Paragraphs vary in size.

## Context

- [ ] It does what the user asked, all of it, and nothing they did not ask for.
- [ ] Length fits the medium (a text is short, a cover letter fits on a page, a reply
      answers first).
- [ ] One register throughout. No formal sentence stranded in a casual message or the reverse.
- [ ] It sounds like the speaker, and like the user's sample if there was one.
- [ ] The reader would know what to do or think after reading it.
- [ ] The opening and closing lines both do work.

## If something fails

Fix it in place, then rerun both scripts. If a fix breaks something else (a rhythm fix
drops a fact), the fact wins. Stop after the checklist passes, normally within two rounds.
