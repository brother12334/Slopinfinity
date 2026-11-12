#!/usr/bin/env python3
"""
compare_pairs.py - measure what a humanizer changed, across input/output pairs.

Reads every NN-name.input.md / NN-name.output.md pair in a folder (default:
research/clever-samples) and prints per-pair metrics, the averages, and the word-level
swaps that recur across pairs. Standard library only.

Usage:
    python3 research/compare_pairs.py [folder]
"""
import glob
import os
import re
import statistics as st
import sys
from collections import Counter

WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
STOP = set("""a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those there their they them he she his her we our you your i my me
not no so than then very more most can could would should will may might has have had do does did
which who whom what when where while also into over under about after before up out off all any
some such each one two""".split())
FORMAL = ["moreover", "furthermore", "ultimately", "additionally", "consequently", "thus",
          "pivotal", "significant", "significantly", "fundamentally", "facilitate", "facilitated",
          "demonstrating", "demonstrate", "primarily", "consistently", "dramatically",
          "proliferation", "circulation", "utilize", "landscape", "foundation", "essential",
          "resilience", "reallocating", "inquiries", "chronically", "logistical", "eager",
          "meaningful", "firsthand", "sought", "deepen", "certain", "specialized"]
PLAIN = ["overall", "however", "really", "very", "quite", "extremely", "actually", "definitely",
         "huge", "much", "lot", "big", "meaning", "because", "so"]


def sentences(text):
    t = re.sub(r"\b([A-Z])\.", r"\1", text.strip())
    t = re.sub(r"\b(a\.m|p\.m|e\.g|i\.e)\.", lambda m: m.group(0).replace(".", ""), t)
    return [s for s in re.split(r"(?<=[.!?])\s+", t) if WORD.search(s)]


def syllables(w):
    w = w.lower().strip("'’")
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and n > 1 and not w.endswith("le"):
        n -= 1
    return max(n, 1)


def metrics(text):
    ss = sentences(text)
    lens = [len(WORD.findall(s)) for s in ss]
    words = WORD.findall(text)
    lw = [w.lower() for w in words]
    m = {
        "words": len(words),
        "sentences": len(ss),
        "mean_len": st.mean(lens),
        "len_cv": st.pstdev(lens) / st.mean(lens),
        "max_len": max(lens),
        "commas_per_sent": text.count(",") / len(ss),
        "semicolons": text.count(";"),
        "serial_commas": len(re.findall(r", (?:and|or) ", text)),
        "polysyllabic_pct": 100 * sum(syllables(w) >= 3 for w in words) / len(words),
        "avg_word_len": st.mean(len(w) for w in words),
        "digits": len(re.findall(r"\b\d+\b", text)),
        "formal_words": sum(lw.count(f) for f in FORMAL),
        "plain_words": sum(lw.count(p) for p in PLAIN),
        "ing_tails": len(re.findall(r", \w+ing\b", text)),
        "fragments": sum(1 for s in ss if re.match(r"(Making|Being|Showing|Meaning|Which)\b", s)),
        "openers": [WORD.findall(s)[0] for s in ss],
    }
    return m, lw


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "clever-samples")
    pairs = sorted(glob.glob(os.path.join(folder, "*.input.md")))
    keys = ["words", "sentences", "mean_len", "len_cv", "max_len", "commas_per_sent", "semicolons",
            "serial_commas", "polysyllabic_pct", "avg_word_len", "digits", "formal_words",
            "plain_words", "ing_tails", "fragments"]
    rows, removed, added = [], Counter(), Counter()
    for inp in pairs:
        out = inp.replace(".input.md", ".output.md")
        if not os.path.exists(out):
            continue
        name = os.path.basename(inp).replace(".input.md", "")
        mi, wi = metrics(open(inp, encoding="utf-8").read())
        mo, wo = metrics(open(out, encoding="utf-8").read())
        rows.append((name, mi, mo))
        ci = {w for w in wi if w not in STOP}
        co = {w for w in wo if w not in STOP}
        removed.update(ci - co)
        added.update(co - ci)

    print(f"\n{len(rows)} pairs\n")
    print(f"{'metric':<18}" + "".join(f"{r[0][:10]:>12}" for r in rows) + f"{'mean':>12}")
    for k in keys:
        cells, deltas = [], []
        for _, mi, mo in rows:
            a, b = mi[k], mo[k]
            fmt = "{:.2f}" if isinstance(a, float) else "{}"
            cells.append(f"{fmt.format(a)}>{fmt.format(b)}")
            deltas.append(b - a)
        mean_in = st.mean(r[1][k] for r in rows)
        mean_out = st.mean(r[2][k] for r in rows)
        print(f"{k:<18}" + "".join(f"{c:>12}" for c in cells) + f"{mean_in:>6.2f}>{mean_out:<5.2f}")
    print("\nopeners (output):")
    for name, _, mo in rows:
        print(f"  {name}: {' '.join(mo['openers'])}")
    print("\nwords dropped in 2+ pairs:", ", ".join(w for w, n in removed.most_common() if n >= 2))
    print("words added in 2+ pairs:  ", ", ".join(w for w, n in added.most_common() if n >= 2))


if __name__ == "__main__":
    main()
