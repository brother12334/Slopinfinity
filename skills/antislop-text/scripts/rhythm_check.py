#!/usr/bin/env python3
"""
rhythm_check.py - measure the structural tells in prose that a keyword scanner misses.

Readers and AI detectors both key on evenness: sentences of the same length, paragraphs of
the same size, the same opener over and over, the same phrase repeated. This script measures
those things. It does not judge word choice; unslop_text_scan.py does that.

Standard library only.

Usage:
    python3 rhythm_check.py <file>            # report
    python3 rhythm_check.py <file> --json     # machine-readable
    python3 rhythm_check.py -                 # read from stdin

Exit code is the number of flags raised (0 = rhythm looks varied).
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter

ABBREV = r"(?:e\.g|i\.e|etc|vs|Mr|Mrs|Ms|Dr|Prof|Inc|Ltd|Jr|Sr|St|approx|No|Fig)\."
SENT_END = re.compile(r"(?<!\b[A-Z]\.)(?<=[.!?])[\"')\]]*\s+(?=[\"'(\[]?[A-Z0-9])")
WORD = re.compile(r"[A-Za-z0-9']+")


def prose_paragraphs(text):
    """Yield paragraphs of running prose, skipping code, headings, quotes, tables and lists."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    paras, cur = [], []
    for line in text.splitlines():
        s = line.strip()
        skip = (not s or s.startswith(("#", ">", "|", "-", "*", "+")) or re.match(r"\d+[.)]\s", s))
        if skip:
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue
        cur.append(s)
    if cur:
        paras.append(" ".join(cur))
    return paras


def split_sentences(para):
    protected = re.sub(ABBREV, lambda m: m.group(0).replace(".", "․"), para)
    parts = [p.replace("․", ".").strip() for p in SENT_END.split(protected)]
    return [p for p in parts if WORD.search(p)]


def cv(values):
    if len(values) < 2:
        return None
    mean = statistics.mean(values)
    return statistics.pstdev(values) / mean if mean else None


def analyze(text):
    paras = prose_paragraphs(text)
    sents = [s for p in paras for s in split_sentences(p)]
    lengths = [len(WORD.findall(s)) for s in sents]
    flags = []
    out = {"paragraphs": len(paras), "sentences": len(sents), "flags": flags}
    if len(sents) < 5:
        out["note"] = "Too little running prose to judge rhythm (need 5+ sentences)."
        return out

    out["mean_sentence_words"] = round(statistics.mean(lengths), 1)
    out["sentence_length_cv"] = round(cv(lengths), 2)
    out["shortest"], out["longest"] = min(lengths), max(lengths)

    # 1. Overall evenness. Human prose in most registers lands well above 0.45.
    c = cv(lengths)
    if c < 0.35:
        flags.append({"id": "uniform-length", "sev": "high",
                      "msg": f"Sentence lengths are very even (CV {c:.2f}). Let some run long and cut others short."})
    elif c < 0.45:
        flags.append({"id": "flat-length", "sev": "medium",
                      "msg": f"Sentence lengths are fairly even (CV {c:.2f}). Add a few deliberately short or long ones."})

    # 2. Runs of similar-length sentences.
    run_start, runs = 0, []
    for i in range(1, len(lengths) + 1):
        if i == len(lengths) or abs(lengths[i] - lengths[i - 1]) > 4:
            if i - run_start >= 4:
                runs.append((run_start, i - 1))
            run_start = i
    for a, b in runs:
        flags.append({"id": "even-run", "sev": "medium",
                      "msg": f"Sentences {a + 1}-{b + 1} are all about the same length ({lengths[a]}-{lengths[b]} words): \"{sents[a][:60]}...\""})

    # 3. No short sentences at all, or no long ones.
    if min(lengths) > 8 and len(sents) >= 8:
        flags.append({"id": "no-short", "sev": "medium",
                      "msg": "No sentence under 9 words. A short one now and then is how people land a point."})
    if max(lengths) < 22 and len(sents) >= 8:
        flags.append({"id": "no-long", "sev": "low",
                      "msg": "No sentence over 21 words. All-short prose is the over-corrected register."})

    # 4. Repeated openers.
    openers = [WORD.findall(s)[0].lower() for s in sents]
    common = Counter(openers).most_common(1)[0]
    if common[1] >= 3 and common[1] / len(sents) > 0.2 and common[0] not in {"i"}:
        flags.append({"id": "repeated-opener", "sev": "medium",
                      "msg": f"{common[1]} of {len(sents)} sentences start with \"{common[0]}\"."})
    for i in range(len(openers) - 2):
        if openers[i] == openers[i + 1] == openers[i + 2]:
            flags.append({"id": "opener-streak", "sev": "medium",
                          "msg": f"Three sentences in a row start with \"{openers[i]}\" (from sentence {i + 1})."})
            break

    # 5. Paragraph uniformity.
    psizes = [len(split_sentences(p)) for p in paras if split_sentences(p)]
    if len(psizes) >= 4:
        pc = cv(psizes)
        out["paragraph_size_cv"] = round(pc, 2)
        if pc < 0.2:
            flags.append({"id": "uniform-paragraphs", "sev": "medium",
                          "msg": f"Paragraphs are nearly all {round(statistics.mean(psizes))} sentences. Vary them by what each one has to say."})

    # 6. Repeated three-word phrases.
    words = [w.lower() for w in WORD.findall(" ".join(sents))]
    stop = {"of the", "in the", "to the", "and the", "on the", "it is", "is a", "for the"}
    tri = Counter(" ".join(words[i:i + 3]) for i in range(len(words) - 2))
    reps = [(t, n) for t, n in tri.most_common(10) if n >= 3 and " ".join(t.split()[:2]) not in stop]
    for t, n in reps[:3]:
        flags.append({"id": "repeated-phrase", "sev": "low", "msg": f"\"{t}\" appears {n} times."})

    # 7. Three-item lists everywhere ("X, Y, and Z").
    triads = len(re.findall(r"\b\w+(?: \w+)?, \w+(?: \w+)?,? and \w+", " ".join(sents)))
    if triads >= 3 and triads / len(sents) > 0.15:
        flags.append({"id": "rule-of-three", "sev": "medium",
                      "msg": f"{triads} three-item lists in {len(sents)} sentences. Use the number of items you actually have."})

    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    res = analyze(text)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(f"\n  rhythm check: {args.path}")
        print(f"  paragraphs: {res['paragraphs']}   sentences: {res['sentences']}")
        if "note" in res:
            print(f"  {res['note']}\n")
        else:
            print(f"  mean sentence: {res['mean_sentence_words']} words   range: {res['shortest']}-{res['longest']}"
                  f"   length CV: {res['sentence_length_cv']}" +
                  (f"   paragraph CV: {res['paragraph_size_cv']}" if "paragraph_size_cv" in res else ""))
            if not res["flags"]:
                print("  verdict: rhythm looks varied\n")
            for f in res["flags"]:
                print(f"  [{f['sev'].upper()}] {f['msg']}")
            print("  Numbers are a prompt to reread, not a verdict. Read it aloud.\n")
    sys.exit(min(len(res["flags"]), 255))


if __name__ == "__main__":
    main()
