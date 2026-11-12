# Research

Input/output pairs used to build the `plain` profile of `antislop-text`.

`clever-samples/` holds paragraphs written by Claude (`NN-name.input.md`) and the same
paragraphs after a run through Clever AI Humanizer (`NN-name.output.md`).

To add a pair, save both files with the next number and rerun:

```bash
python3 research/compare_pairs.py
```

It prints each metric per pair (input > output), the averages, how sentences open, and
the words dropped or added in two or more pairs. Then check the plain profile still
separates them:

```bash
for f in research/clever-samples/*.md; do
  python3 skills/antislop-text/scripts/rhythm_check.py "$f" --profile plain | grep -c "\[HIGH\|\[MEDIUM"
done
```

Inputs should get flags and outputs should get none. When a new pair breaks that,
update `skills/antislop-text/references/plain-rewrite.md` and the plain checks in
`rhythm_check.py`.

Useful to record with each pair, when available: the Clever style used and detector
scores for both versions. None of the current pairs have scores.
