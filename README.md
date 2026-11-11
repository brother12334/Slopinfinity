# Slopinfinity

A single Claude skill for building frontends that don't look AI-generated.

`antislop-design` takes seven design skills (unslop-ui, unslop-text, unslop-code,
impeccable, web-design-guidelines, pick-ui-library and transitions-dev) and runs them as
one pipeline. You get one trigger and one set of commands, and the phases run in the
right order.

## What it does

AI-built sites get spotted for specific reasons: an untouched shadcn theme, an indigo
primary, gradient headline text, emoji icons, the centered hero above three identical
feature cards. The fix most people reach for has become a tell too: a cream background,
a Fraunces or Instrument Serif headline and a sage green accent.

The skill doesn't push a house style. It finds the defaults (both the old ones and the
newer "tasteful" ones) and makes you replace each with a choice the project made and can
explain. When the brief really does call for purple or serif, the skill keeps it.

## The workflow

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

## Commands

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

## Install

Copy the skill folder into your skills directory.

```bash
# per project
mkdir -p .claude/skills && cp -r skills/antislop-design .claude/skills/

# or for every project
mkdir -p ~/.claude/skills && cp -r skills/antislop-design ~/.claude/skills/
```

On claude.ai, zip `skills/antislop-design` and upload it under Settings > Capabilities > Skills.

## The scanners in CI

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

## Layout

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

## Credits

See [NOTICE.md](NOTICE.md) for sources and licenses. Not everything is bundled.
transitions.dev forbids republishing its collection, so this repo carries only the
motion principles, written fresh. Install transitions.dev on its own if you want the
drop-in CSS recipes.
