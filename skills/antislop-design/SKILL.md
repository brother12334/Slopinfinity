---
name: antislop-design
description: One end-to-end workflow for frontend design that does not read as AI-generated. Covers the brief, library picks, building to a craft floor, motion, UI copy, a deterministic scan of styles, copy and code, a guidelines and accessibility review, and a final polish. Removes the known tells (untouched shadcn/Tailwind defaults, AI purple, gradient text, unprompted glow, emoji icons, the hero plus three feature cards, AND the newer cream plus serif plus sage "tasteful default") without imposing a house look. Use whenever building, redesigning, styling, reviewing, auditing, animating or polishing a website, landing page, web app, dashboard or component, or when the user says it looks AI-made, generic, vibe-coded, templated, or asks to de-slop it. Trigger even if they never say "slop".
argument-hint: "[build | audit | polish | motion | libs | copy] [target]"
---

# antislop-design

This skill merges seven separate design skills into one pipeline: unslop-ui, unslop-text,
unslop-code, impeccable, web-design-guidelines, pick-ui-library and transitions-dev. Each
phase below says which part it came from, so you can trace a rule back to its source.

## The one rule everything else serves

**Never replace one default with another.** The 2024 tell was a purple-to-blue gradient on
a dark hero. The 2026 tell is cream background, Instrument Serif or Fraunces, sage green
accent. Swapping the first for the second is not a fix. This skill never prescribes a
palette, typeface or layout. It detects defaults and demands that every major choice be
one the project made on purpose and can explain.

A tell is an *unspecified default*, not a banned value. If the brief asks for purple, neon,
a serif or cream, honor it, and mark the line `unslop-ignore` so the scanners leave it
alone. The brief always wins over this skill's preferences.

## Commands

| Command | What it runs | Phases |
|---|---|---|
| `build [feature]` (default for new work) | Full pipeline | 0 to 7 |
| `audit [target]` | Scan and review existing UI, no edits | 0, 5, 6, report |
| `polish [target]` | Audit, then fix in priority order | 0, 5, 6, 7 |
| `motion [target]` | Motion review and tokenizing | 4 only |
| `libs [task]` | Library lookup | 2 only |
| `copy [target]` | UI copy pass | 5a only |

No argument and no obvious intent: ask which one, in one short question. Do not auto-run.

## Phase 0. Triage

Decide three things before touching anything.

1. **Refine or replace.** Refinement keeps the existing identity, copy and behavior and
   changes only what is in scope. Redesign keeps product truth and function but treats the
   old look as an anti-reference. Never split the difference by polishing a look you were
   asked to discard.
2. **Surface mode.** Pick from the surface, not the product:
   - *Persuade* (landing, pricing, marketing): full commitment, a point of view.
   - *Operate* (app UI, dashboards, settings): scanability and consistency beat expression.
   - *Read* (docs, articles, changelogs): structure for comprehension.
   - *Experience* (portfolios, galleries): the work leads, the interface recedes.
3. **Existing truth.** Read `PRODUCT.md`, `DESIGN.md`, theme files, tokens, `tailwind.config`,
   `components.json`, `package.json`. A missing DESIGN.md does not mean greenfield.

## Phase 1. The brief (most of the battle)

"Looks AI" is mostly a specification problem. An unspecified prompt returns the median of
the training data, and everyone's median is the same. Settle these concretely, from the
user or from the project. If the user just says "build it", state your choices and the
reason for each, then proceed. Never fall back silently.

- **Reference.** One real site, brand, product or screenshot to anchor to. This does more
  than every other rule combined. No reference? Commit to a *named* direction (dense
  utilitarian, editorial, warm consumer, stark technical, brand-loud), never "modern and clean".
- **Color.** A real brand color, or one sampled from something concrete. Not the framework
  default, not cream/sage.
- **Type.** A specific face or pairing with a reason. Inter and Geist (the no-choice picks)
  and Instrument Serif, Fraunces, Playfair (the tasteful picks) are overexposed; use them
  only as a real decision.
- **Layout intent.** What the page is for and the first thing the visitor should do. The
  structure follows from that, which is how you avoid hero plus three cards.
- **Light or dark** from the use scene (who, where, what light), not the category.

When there is no brief at all, offer two or three genuinely distinct directions instead of
one median result. Record the settled choices in `DESIGN.md` so later work stays consistent.

Method: [references/choosing-a-look.md](references/choosing-a-look.md).

## Phase 2. Libraries

Check `package.json` first and use what is installed. For gaps, use the curated picks in
[references/libraries.md](references/libraries.md): recommend one library, say what it is
for in a sentence, and say so plainly if you leave the list. Do not churn an existing
dependency unasked.

## Phase 3. Build to the craft floor

Read [references/craft-floor.md](references/craft-floor.md) immediately before the first UI
edit, then build without reciting it. While building, steer clear of everything in
[references/ui-tells.md](references/ui-tells.md). The short version:

- Theme the framework. Stock shadcn/Tailwind tokens are the tell, not the framework.
- Solid color on text; emphasis from weight and size, never gradient fill.
- Real icons from one library or authored SVG, one stroke weight. No emoji as icons.
- A small, intentional radius scale, not one value on everything.
- Shadows with an offset and soft blur; no zero-offset colored halos, no unprompted glow.
- No eyebrow labels over headings. No 01/02/03 section numbers unless the order matters.
- No same-size icon-heading-text cards as the page skeleton. No nested cards.
- Show the real product (true screenshots, real data) over abstract icon cards.
- Theme the browser surfaces: selection, caret, scrollbars, focus rings, underline offset,
  tabular numerals. Models skip these most often, and they are the cheapest signal of craft.
- Every state: hover, focus, disabled, loading, error, empty.
- Match the codebase. New components follow the project's existing naming, file layout
  and patterns ([references/fitting-the-codebase.md](references/fitting-the-codebase.md)).

## Phase 4. Motion

Follow [references/motion.md](references/motion.md). One authored moment per view, not an
entrance on every section. Every animation communicates a state change, uses shared duration
and easing tokens, and has a `prefers-reduced-motion` guard. For drop-in recipes, the user
can install transitions.dev alongside this skill; the reference explains how to map a UI
element to the right transition.

## Phase 5. Scan

Run the combined scanner from the project root (paths are relative to this skill folder):

```bash
sh scripts/antislop_scan.sh <path>              # all three scanners
sh scripts/antislop_scan.sh <path> --severity high
```

Or each one on its own:

```bash
python3 scripts/devibe_scan.py <path> [--severity high] [--json]       # styles and markup
python3 scripts/unslop_text_scan.py <path> [--severity high] [--json]  # prose and UI copy
python3 scripts/unslop_code_scan.py <path> [--severity high] [--json]  # frontend code
```

Each exits with its high-severity count, so CI can gate on it. All three honor
`unslop-ignore` on a line. Standard library Python only, no install.

**A clean scan is not a verdict.** The scanners catch surface tells. They cannot see layout
coherence, spacing rhythm, overflowing text, uniform sentence rhythm or code that ignores
its surroundings. Phase 6 covers those.

### 5a. Copy pass

UI copy reads as AI as fast as UI does. Check headlines, buttons, empty states, errors and
microcopy against [references/copy-tells.md](references/copy-tells.md). Most fixes are
mechanical: the em dash becomes a comma or period, "delve into" becomes "look at", the
"it's not just X, it's Y" cadence becomes a plain claim, the rule-of-three list loses its
filler item. Controls name their action. Errors name the problem and the way out. Do not
over-correct into choppy fragments or fake casualness; that is a second default.

### 5b. Code pass

Check the frontend code against [references/code-tells.md](references/code-tells.md):
narrating comments, placeholder names, swallowed errors, hallucinated APIs, tutorial-shaped
boilerplate, over-engineering.

## Phase 6. Review

Render it and look, at the sizes it ships at. Batch checks: fix everything one look shows
before looking again.

1. Look at it: layout coherence, spacing rhythm (more space above a heading than below),
   alignment, text overflow with real copy at every breakpoint, measure 65 to 75ch.
2. Fetch the Web Interface Guidelines and apply the current rules to the changed files,
   reporting in terse `file:line` form:
   `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
   If the fetch fails, clone `github.com/vercel-labs/web-interface-guidelines` and read
   `command.md`. Skip this step with a note if there is no network.
3. Score the five dimensions in [references/audit.md](references/audit.md)
   (accessibility, performance, theming, responsive, implementation integrity).

## Phase 7. Fix and polish

Fix in priority order: P0, P1, then the highest-impact P2s. Fix well:

- Do not fix `bg-purple-600` with `bg-emerald-700`. That is a different default. Apply the
  project's actual color or ask what it should be.
- Do not fix "delve" with "dive". Use the plain verb.
- A fix that introduces a new unspecified default is not a fix.

Re-run Phase 5 after fixes and confirm the high-severity count dropped.

## Reporting

Lead with the verdict and the single highest-impact change. Then findings by priority with
`file:line` and the fix. Close with the scanner scores, the audit score out of 20, and the
next three changes. Plain and specific. Note anything you could not check (no browser, no
network) instead of implying it passed.

## What this deliberately does not flag

Mesh, aurora and blob backgrounds barely register in the complaint data. Bento grids and
glassmorphism are low and contested. Dark mode is fine; unprompted glow is the tell.
shadcn and Tailwind are fine; untouched defaults are the tell. Over-flagging trains people
to ignore the tool, so keep findings narrow and real.
