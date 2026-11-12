---
name: antislop-design
description: An end-to-end workflow for frontend design that does not look like an AI template. It starts from the product and audience, commits to a stated design concept, builds the page, audits it against eight generic patterns (palette as personality, the interchangeable hero, cards for everything, glass without a reason, bland type hierarchy, meaningless metrics, the endless icon grid, glow competing with content), then revises the three most generic decisions before delivery. Gradients, cards, glass and glow are allowed only with a stated reason. Demands specific copy, credible proof, varied layouts and a visual identity built for the project, plus checks for mobile layout, readability, contrast and interaction states. Use whenever building, redesigning, styling, reviewing, auditing, animating or polishing a website, landing page, web app, dashboard or component, or when the user says it looks AI-made, generic, templated or vibe-coded. Trigger even if they never say "slop".
argument-hint: "[build | audit | polish | motion | libs | copy] [target]"
---

# antislop-design

The visual reference for this skill is [references/visual-reference.pdf](references/visual-reference.pdf)
("Beyond the AI website template"), written out in
[references/generic-patterns.md](references/generic-patterns.md). **When any other file in
this skill conflicts with the PDF, the PDF wins.**

## The rule everything else serves

Design from the product, the audience and the content outward. Every visible decision
(palette, type, layout, imagery, effects, copy, proof) needs a reason you can say in one
sentence in terms of this product. A recognizable pattern is a prompt to inspect, not an
automatic ban. A pattern with a real reason stays; a pattern that is there because it is
what websites usually look like goes.

The brief always wins. If the user asks for a purple gradient or a glass navbar, build it
well and note the reason as "requested".

The PDF's illustrations use one palette and type style. That is the PDF's own look, not a
template. Each project gets an identity drawn from its own subject.

## Commands

| Command | What it runs | Steps |
|---|---|---|
| `build [feature]` (default for new work) | Full workflow | 0 to 8 |
| `audit [target]` | Pattern audit, scans and quality checks on existing UI, no edits | 0, 5, 6, 7, report |
| `polish [target]` | Audit, then revise and fix | 0, 5 to 8 |
| `motion [target]` | Motion review and tokenizing | motion reference only |
| `libs [task]` | Library lookup | library reference only |
| `copy [target]` | Copy and proof pass | step 3 copy rules plus the copy scan |

No argument and no obvious intent: ask which one, in one short question.

## Step 0. Triage

1. **Refine or replace.** Refinement keeps the existing identity, copy and behavior and
   changes only what is in scope. A redesign keeps product truth and function and treats
   the old look as evidence of what not to repeat.
2. **Surface mode.** *Persuade* (landing, pricing, marketing): a strong point of view.
   *Operate* (app UI, dashboards, settings): scanability and consistency first. *Read*
   (docs, articles): comprehension first. *Experience* (portfolios, galleries): the work
   leads.
3. **Existing truth.** Read `PRODUCT.md`, `DESIGN.md`, theme files, tokens,
   `tailwind.config`, `components.json` and `package.json` before choosing anything.

## Step 1. Understand the product and audience

Write these down before any visual decision. Ask the user for what you cannot find; if
they want you to proceed anyway, state your assumptions and mark them.

- **Audience.** Who visits, what they already know, what situation they are in.
- **Key task.** The one thing a visitor should understand or do. This becomes the single
  primary action per view.
- **Problem and outcome.** The user's problem in their own words, and the concrete result
  the product gives them.
- **Proof on hand.** Real metrics (with measure, population, period, baseline, source),
  real customers, real screenshots or product states. List what exists and what does not.
- **Content inventory.** The sections the page actually needs, ranked by importance.

Five-second target: a visitor should be able to tell who it serves, what it does and the
next action. Write that sentence now; the hero has to deliver it.

## Step 2. Choose a design concept

State, in writing, before coding:

1. **Concept.** One sentence that ties the look to the subject ("a field notebook for
   small farms", "a ledger you can read at a glance"). Drawn from the product's world,
   not from "modern and clean".
2. **Palette with roles.** Each color, where it came from and what it does (surface,
   text, structure, the one action color, status). Contrast-checked.
3. **Type system.** A display voice, a body voice and a utility voice, each with the face,
   size range and where it is used.
4. **Imagery and shape.** What the pictures are (product states, photography, diagrams,
   illustration) and the radius, line and depth language.
5. **Page hierarchy.** Each section from step 1 with the structure that fits its content:
   lead statement, ordered process, comparison table, plain list, representative screen,
   cards only for genuine peers. Vary the structures down the page.
6. **Effects budget.** Every gradient, glass surface, glow, shadow style and animation you
   plan to use, each with its reason. At most one effect as a focal point per view.

When the user has no reference and no preference, offer two or three distinct concepts in
a few lines each and let them pick, or pick one and say why. Record the chosen concept in
`DESIGN.md` so later work stays consistent.

More on choosing: [references/choosing-a-look.md](references/choosing-a-look.md).
Library picks: [references/libraries.md](references/libraries.md) (check `package.json` first).

## Step 3. Build

Read [references/craft-floor.md](references/craft-floor.md) before the first UI edit.
Build against the concept from step 2. Requirements:

**Copy.**
- The headline names the user's problem or outcome in concrete terms, not an abstract
  promise. The competitor-swap test from pattern 2 must fail.
- Features are tasks with objects ("approve a request with its budget attached"), not
  adjectives ("Smart", "Fast").
- Buttons say what happens ("See a sample forecast"), not "Get started" or "Learn more"
  unless that is literally the action.
- Write UI copy to [references/copy-tells.md](references/copy-tells.md): no em dash
  habit, no "not just X, it's Y", no hype words.

**Proof.**
- Every number carries its measure, population, period, baseline and source, or it goes.
- Show representative product states or task examples next to claims.
- Never invent metrics, customers, logos, quotes or testimonials. If real proof is
  missing, use a labeled placeholder (`[PLACEHOLDER: pilot result]`) and list each one
  for the user at delivery.

**Layout.**
- One lead idea per section, secondary ideas visibly secondary.
- Structure follows content (see step 2). No two adjacent sections share the same
  structure unless the content really is the same shape.
- One clear primary action per view.

**Identity.**
- Theme the framework fully (tokens, radius, neutrals, spacing). Untouched shadcn or
  Tailwind defaults are an unmade decision.
- Real icons from one set or authored SVG, one stroke weight, used only where they help
  recognition. No emoji as icons.
- Theme browser surfaces: selection, caret, scrollbars, focus rings, underline offset,
  tabular numerals.

**Effects.** Gradients, cards, glass, glow, blur and heavy shadows are allowed when their
reason from step 2 still holds in the built page. Mark each with a comment on the same
line, which the scanners honor, giving the reason:
`background: linear-gradient(...); /* unslop-ignore: maps cold-to-warm across the forecast range */`.
No reason, no effect.

**States.** Every interactive element has hover, focus-visible, active, disabled and,
where relevant, loading, error and empty states.

**Codebase fit.** Follow the project's naming, file layout and patterns
([references/fitting-the-codebase.md](references/fitting-the-codebase.md)). Motion follows
[references/motion.md](references/motion.md): one authored moment per view, shared tokens,
a `prefers-reduced-motion` guard.

## Step 4. Render and look

Render the page at desktop (about 1440px) and mobile (about 390px) widths with real copy.
Batch your looking: note everything wrong in one pass, fix it, then look again.

## Step 5. Compare against the eight patterns

Go through [references/generic-patterns.md](references/generic-patterns.md) section by
section against the rendered page, the whole page and not just the hero:

1. For each of the eight patterns, mark *not present*, *present with a reason* (state it)
   or *present without a reason*.
2. Run the eight-question anti-template audit.
3. Run the final test: cover the logo. Does it still feel like this brand?

## Step 6. Revise the three most generic decisions

Rank every decision by how easily it could appear unchanged on an unrelated product. Take
the top three, even if the audit mostly passed, and for each write the decision, the
pattern it matches, the specific replacement and the tradeoff. Make the changes, render
again, and re-run step 5 on the changed sections.

## Step 7. Quality checks

All of these must pass before delivery:

- **Mobile layout.** At 390px: no horizontal scroll, no overflowing or clipped text,
  tap targets at least 44px, the primary action visible without hunting, layouts
  recomposed for the narrow screen rather than squeezed, images sized for the viewport.
- **Readability.** Body text at least 16px, line length about 45 to 75 characters,
  line height about 1.4 to 1.6 for body, clear size and weight steps between levels.
- **Contrast.** WCAG AA: 4.5:1 for body text and placeholders, 3:1 for large text, icons
  and control boundaries. Check text on every surface it sits on, including any image,
  gradient or glass.
- **Interaction states.** Hover, focus-visible, active, disabled, loading, error and
  empty all designed. Keyboard: every control reachable in a sensible order with a
  visible focus ring. Motion respects `prefers-reduced-motion`.

Then run the scanners from the project root (paths relative to this skill folder):

```bash
sh scripts/antislop_scan.sh <path>                       # styles, copy and code together
python3 scripts/devibe_scan.py <path> [--severity high]  # styles and markup only
```

A scanner finding is a prompt to inspect, like the patterns. Fix it, or keep it and add
an `unslop-ignore:` comment with the reason. For a fuller review, also apply the Vercel
Web Interface Guidelines
(`https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`)
and score the five dimensions in [references/audit.md](references/audit.md).

## Step 8. Deliver

Give the user, briefly:

1. **The concept** in one sentence, and the palette, type and layout reasons.
2. **The three revisions** from step 6: before, after and the tradeoff of each.
3. **Effects kept**, each with its reason.
4. **Placeholders** the user must fill with real proof or content.
5. **Anything not checked** (no browser, no real device, no network), stated plainly
   rather than implied as passing.

For `audit` without edits, report instead: the verdict, the eight-pattern table, the three
most generic decisions with suggested replacements, quality-check failures with
`file:line`, and the scanner results.
