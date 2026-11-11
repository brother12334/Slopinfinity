# Slopinfinity

Claude skills that keep AI output from looking or sounding AI-generated.

| Skill | For | Folder |
|---|---|---|
| `antislop-design` | Websites, app UI, dashboards, components | [skills/antislop-design](skills/antislop-design) |
| `antislop-text` | Anything a person reads: posts, emails, essays, copy, replies | [skills/antislop-text](skills/antislop-text) |

Both work the same way. They catch the specific defaults people spot as AI, swap in
choices made on purpose, and check the result with scanners before you see it.

# antislop-design

`antislop-design` takes seven design skills (unslop-ui, unslop-text, unslop-code,
impeccable, web-design-guidelines, pick-ui-library and transitions-dev) and runs them as
one pipeline. You get one trigger and one set of commands, and the phases run in the
right order.

### What it does

AI-built sites get spotted for specific reasons: an untouched shadcn theme, an indigo
primary, gradient headline text, emoji icons, the centered hero above three identical
feature cards. The fix most people reach for has become a tell too: a cream background,
a Fraunces or Instrument Serif headline and a sage green accent.

The skill doesn't push a house style. It finds the defaults (both the old ones and the
newer "tasteful" ones) and makes you replace each with a choice the project made and can
explain. When the brief really does call for purple or serif, the skill keeps it.

### The workflow

| Phase | What happens | From |
|---|---|---|
| 0. Triage | Refine or redesign, surface mode, read existing tokens and docs | impeccable |
| 1. Brief | Reference, color, type, layout intent, light or dark from the use scene | unslop-ui |
| 2. Libraries | One curated pick per task, after checking what is installed | pick-ui-library |
| 3. Build | Craft floor plus the catalog of visual tells to avoid | impeccable, unslop-ui |
| 4. Motion | One authored moment, shared tokens, reduced-motion guards | transitions-dev (principles) |
| 5. Scan | Three deterministic scanners: styles, copy, code | unslop-ui, unslop-text, unslop-code |
| 6. Review | Eye check, Vercel Web Interface Guidelines, scored audit out of 20 | web-design-guidelines, impeccable |
| 7. Polish | Fix by priority without swapping in a new default, rescan | all |

### Commands

```
/antislop-design build [feature]   full pipeline for new work
/antislop-design audit [target]    scan and review, no edits
/antislop-design polish [target]   audit, then fix in priority order
/antislop-design motion [target]   motion review and tokenizing
/antislop-design libs [task]       library lookup
/antislop-design copy [target]     UI copy pass
```

It also triggers on its own whenever you build, style or review frontend work, or say
something "looks AI-made" or "vibe-coded".

### The scanners in CI

Each scanner uses only the Python standard library. Its exit code is the number of
high-severity findings, so a CI job can fail on any of them.

```bash
sh skills/antislop-design/scripts/antislop_scan.sh src/                 # all three
sh skills/antislop-design/scripts/antislop_scan.sh src/ --severity high
python3 skills/antislop-design/scripts/devibe_scan.py src/ --json       # just styles
```

Add `unslop-ignore` to any line holding a value you chose on purpose and the scanners will
skip it.

A clean scan only means the surface tells are gone. The scanners can't judge layout
rhythm, overflow, sentence rhythm or code that ignores the rest of the repo, so Phase 6
puts a person (or Claude, looking at the render) on those.

### Layout

```
skills/antislop-design/
  SKILL.md                         the workflow
  references/
    choosing-a-look.md             how to pick color, type and layout without a default
    ui-tells.md                    catalog of visual tells, ranked by complaint data
    craft-floor.md                 quality floor and refusals for every UI edit
    motion.md                      motion principles, tokens, element-to-transition map
    libraries.md                   curated library picks
    copy-tells.md                  prose and UI copy tells
    code-tells.md                  frontend code tells
    fitting-the-codebase.md        matching the existing repo
    audit.md                       five-dimension scored audit
  scripts/
    antislop_scan.sh               runs all three scanners
    devibe_scan.py                 styles and markup
    unslop_text_scan.py            prose and copy
    unslop_code_scan.py            code
```

# antislop-text

Every piece of writing goes through three passes before you see it.

1. **Write it normally.** Claude does the task the usual way and puts all its effort into
   getting the content right: facts, coverage, order. It also notes the register (casual,
   work, essay, formal), who is speaking and what the main point is.
2. **Humanize it.** Claude rewrites the draft. The point goes first and the recap
   ending is cut. Next come the word-level tells (em dashes, "it's not just X, it's Y",
   overused chatbot words, bold lead-in labels), then the sentence rhythm gets uneven on
   purpose, hedges get committed to, and vague claims become concrete details.
3. **Check it and fix it.** Two scanners run on the rewrite. Then the whole piece gets
   read for detail (no fact lost, nothing invented), wording, grammar and context (does it
   answer the request, in one consistent voice). Claude fixes what it finds and checks
   again, usually one or two rounds.

You get the final text without a list of every change.

### Commands

```
/antislop-text write <task>          all three passes (default)
/antislop-text humanize <text|file>  passes 2 and 3 on your own text
/antislop-text check <text|file>     pass 3 only, a report with no rewrite
```

It also kicks in automatically for any writing a person will read, and when you say
something sounds like ChatGPT, is too polished, or needs humanizing.

### The scanners

```bash
python3 skills/antislop-text/scripts/unslop_text_scan.py draft.md   # word-level tells
python3 skills/antislop-text/scripts/rhythm_check.py draft.md       # sentence rhythm
```

`rhythm_check.py` is new in this repo. It measures how much sentence length varies,
flags runs of same-length sentences, repeated openers, same-size paragraphs, repeated
phrases and three-item lists everywhere. On a typical AI paragraph it reports a length
variation of 0.13. A human-written paragraph of the same size scored 0.65.

### On AI detectors

Detectors mostly score how predictable and even the text is, and humans notice the same
things, so this workflow addresses both. No tool can promise a detector result, though:
detectors disagree with each other and misflag human writing all the time. The skill
won't use tricks aimed only at detectors (invisible characters, look-alike letters,
planted typos). They damage the text and detectors now look for them.

### Layout

```
skills/antislop-text/
  SKILL.md                     the three-pass workflow
  references/
    humanize-pass.md           the pass 2 rewrite, step by step
    review-checklist.md        the pass 3 checklist
    tells.md                   catalog of writing tells, ranked by how often readers cite them
    writing-with-intent.md     picking a register, speaker and claim
  scripts/
    unslop_text_scan.py        word-level scanner
    rhythm_check.py            rhythm and structure checker
```

# Install

Copy either skill folder (or both) into your skills directory.

```bash
# per project
mkdir -p .claude/skills && cp -r skills/antislop-design skills/antislop-text .claude/skills/

# or for every project
mkdir -p ~/.claude/skills && cp -r skills/antislop-design skills/antislop-text ~/.claude/skills/
```

On claude.ai, zip each skill folder and upload it under Settings > Capabilities > Skills.

# Credits

See [NOTICE.md](NOTICE.md) for sources and licenses. Not everything is bundled.
transitions.dev forbids republishing its collection, so this repo carries only the
motion principles, written fresh. Install transitions.dev on its own if you want the
drop-in CSS recipes.
