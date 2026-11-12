---
name: antislop-design
description: An end-to-end workflow for frontend design that does not look like an AI template. It starts from the product and audience, commits to a stated design concept, builds the page, audits it against eight generic patterns (palette as personality, the interchangeable hero, cards for everything, glass without a reason, bland type hierarchy, meaningless metrics, the endless icon grid, glow competing with content), then revises up to three decisions that are still generic, and none when the design is already specific. It asks at most four high-impact questions up front, studies real sites of the same kind for task order and composition, makes the rendered visual result a real gate (a scanner pass is not a visual pass), and requires honest primary actions with no invented photos or proof. Gradients, cards, glass and glow are allowed when the design concept or audit records a reason. Demands specific copy, credible proof, varied layouts and a visual identity built for the project, plus checks for mobile layout, readability, contrast and interaction states. Use whenever building, redesigning, styling, reviewing, auditing, animating or polishing a website, landing page, web app, dashboard or component, or when the user says it looks AI-made, generic, templated or vibe-coded. Trigger even if they never say "slop".
argument-hint: "[build | audit | polish | motion | libs | copy] [target]"
---

# antislop-design

Two visual references drive this skill:

- [references/visual-reference.pdf](references/visual-reference.pdf) ("Beyond the AI website
  template"), written out in [references/generic-patterns.md](references/generic-patterns.md):
  the eight generic patterns and the anti-template audit.
- [references/real-sites.pdf](references/real-sites.pdf) ("24 real websites, 24 different
  design jobs"), written out in [references/real-sites.md](references/real-sites.md): real
  sites by type, what to borrow, what to ask, and the visual-judgment gate.
- [references/five-site-review.pdf](references/five-site-review.pdf) ("Clearer. Still not
  finished."), a review of five test builds. Its lessons are in steps 1, 3, 4 and 8 and in
  [references/assets.md](references/assets.md).

**When any other file in this skill conflicts with these PDFs, the PDFs win.** Study
them for principles; never recreate a screenshot.

## The rule everything else serves

The central test: **does this design communicate this product clearly and feel specific
to its audience?** Every other rule in this skill serves that question. When the answer
is already yes, do not change things to satisfy a checklist.

Design from the product, the audience and the content outward. Every visible decision
(palette, type, layout, imagery, effects, copy, proof) needs a reason you can say in one
sentence in terms of this product. A recognizable pattern is a prompt to inspect, not an
automatic ban. A pattern with a real reason stays; a pattern that is there because it is
what websites usually look like goes.

The brief always wins. If the user asks for a purple gradient or a glass navbar, build it
well and note the reason as "requested".

The first PDF's illustrations use one palette and type style. That is the PDF's own look,
not a template. Each project gets an identity drawn from its own subject.

Three more rules hold everywhere:

- **A scanner pass is not a visual pass.** The rendered page has to look right to a
  person at the sizes it ships at (step 4). Clean scans never overrule a failed look, and
  a clean screenshot is not the same as a finished design.
- **Primary actions are honest.** A missing stream, checkout or form must not appear to
  work. Never invent photos, proof, customers or performance numbers.
- **Honesty supports the design; it does not overwhelm it.** Disclose a limitation once,
  at the action it affects, with verbs that say what actually happens. Repeated warnings
  in every section become part of the brand.

## Commands

| Command | What it runs | Steps |
|---|---|---|
| `build [feature]` (default for new work) | Full workflow | 0 to 8 |
| `audit [target]` | Visual gate, pattern audit, scans and quality checks on existing UI, no edits | 0, 4 to 7, report |
| `polish [target]` | Audit, then revise and fix | 0, 4 to 8 |
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

Write these down before any visual decision:

- **Site type.** Which of the jobs in [references/real-sites.md](references/real-sites.md)
  this is closest to (cafe, radio, store, publication, civic service, software product,
  portfolio...). It decides what the visitor expects to find first.
- **Visual material.** What real imagery exists: photographs of the place, product,
  people or work; product screens; artwork; footage; data for charts. List what exists
  and what does not. A design without authentic material has to be carried by type,
  structure and the task, and that changes the concept.
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

**Essentials.** From the key task, list the two to four facts or actions the visitor's
decision depends on. They differ by site type: for a café, opening hours, address and
what's served; for a shop, the product, its price and how to choose; for a service, the
price, the area and the request action; for a magazine, a headline worth opening; for a
tool, what it does and a way to try it. Every concept and every render is checked against
this list, but the list is not a quota for the first screen (see step 2).

**Fact sources.** Every fact the page displays (prices, addresses, hours, inclusions,
policies, sequences) must trace to what the user supplied. When you write a test brief
yourself, show the user the full brief before building; a fact that appears only in your
notes counts as invented. Before delivery, list each displayed fact beside its source in
`DESIGN.md` and remove or label anything without one.

### Check the content can carry the task

Before any visual decision, check whether the available content and assets let the
visitor complete the main task. A magazine whose stories cannot be read, a shop with no
way to judge the products, or a café page with nothing to show of the food promises a
task it cannot deliver, and no styling fixes that.

- If content is missing that would change the result (story text, product photos or
  dimensions, real imagery), ask for it (below).
- For a fictional demo, representative content may be authored only when it is clearly
  labeled as sample and, where it stands in for something substantial (an article, a
  product description), only with the user's approval. Never imply sample facts, people
  or imagery are real.
- Decide the asset strategy now with the ladder in [references/assets.md](references/assets.md):
  user-provided real material, then verified licensed imagery, then original
  illustration or a labeled concept render, then an intentional text-led design. Choose
  per project; do not carry one project's choice into the next.

### Ask only what changes the design

If the brief or the project lacks decisive information, ask **at most four** focused
questions, **together in one message**, chosen from:

1. **Imagery.** Do you have real photos, product images, artwork or footage? May I source
   licensed images online if needed?
2. **Brand.** Are any colors, fonts, logo rules or visual references fixed? What should
   this definitely not feel like?
3. **Content and proof.** Which facts, product states, prices, dates, metrics and proof
   are real and approved?
4. **Task.** What should the visitor do first, and what happens after they click? (A
   radio player, booking flow, checkout or form needs an honest working or demo state.)

Rules:
- Do not ask about anything the brief or the project already answers. Use those answers.
- Make a recommendation with each question, so the user can just say yes.
- If the user wants progress immediately, state reasonable assumptions and build.
- A preferred color or font is a constraint to design with, not something to override
  because a pattern checker dislikes it.
- Never silently substitute generic stock imagery for real material.

## Step 2. Study real sites, then choose a design concept

**Study first.** Pick at least three entries from
[references/real-sites.md](references/real-sites.md): the closest match to the site type,
plus one or two from other categories in a different style whose task order or
composition solves a similar problem. When a browser is available, open the live sites to
see behavior and the mobile layout. Write down, for each, the principle you are borrowing
(task order, how the primary action stays in sight, how imagery or type carries the
mood) and what you will not copy (brand, photographs, exact layout).

**Then the concept.** State, in writing, before coding:

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
7. **Art direction and material plan.** The visual idea that makes this business, not its
   category, recognizable; the real site that informed it and what it borrows; the
   authentic material it depends on (whose photos, of what, shot how) and how that will
   be obtained; what stands in until then, labeled as a stand-in. When visitors judge a
   physical place, product or person, say plainly that a stand-in cannot do that job and
   record the missing material as an unresolved content need.
   When the brief supplies no distinguishing brand or visual material, the identity is
   yours: call it a **proposed identity** in the concept and delivery, and justify it
   from the subject and audience. Do not invent facts about the business (history,
   materials, people, neighbourhood, methods) to make the proposal sound grounded.
   A photograph of another real business cannot carry the identity of the business
   you are designing, even with a caption saying it is somewhere else. Judge the
   impression the page makes before anyone reads the caption: if the borrowed photo is
   the hero, the page reads as that place. Use such photos as research, or as clearly
   secondary illustration, never as the dominant evidence for this business.

When the user has no reference and no preference, offer two or three distinct concepts, or
pick one and say why. **Concepts must differ in art direction, not arrangement**: in the
visual idea, the kind of material and how it is treated (documentary photography, a
specific illustration hand, signage or wayfinding, found material, a typographic system
drawn from the place). Three layouts of the same typeface, palette and artwork are one
concept. Test: swap the layouts between two concepts; if they still look like the same
brand, they are arrangements. Record the chosen concept in `DESIGN.md` so later work stays
consistent.

**Judge each concept as an identity and as a website.** Render every concept at desktop
and mobile before comparing them, and score both:

- *Identity:* is it specific to this business, memorable, and still recognizable with the
  logo covered? Could it belong to any business of this type? Polished type and a tidy
  grid around generic artwork is not identity.
- *Usability:* at both sizes, are the **main promise**, the **next action** and the
  **one or two facts that decide whether to continue** easy to find and read (primary or
  secondary text, not caption-sized labels, not dependent on what's behind them)? Is
  there a clear path to the rest: a visible action, or the next section starting in view?

The first screen does not have to hold every essential. Cramming all of them in, above
all on mobile, turns the page into an information sheet and squeezes out the visual
idea. Put the deciding facts up front and the rest one clear step away. A striking
poster, attractive illustration or new palette does not make up for a decisive fact that
is buried, tiny or unreadable. Only recommend a concept that passes usability; identity
decides between the ones that pass. If a favorite fails usability, revise it before
recommending it. Don't discard a direction with an idea of its own because its first
execution is weak: give it a deliberate revision of its typography, composition and
mobile treatment, then compare it with the other options. If it still fails after that
revision, reject it and say why. The revision is craft only; it adds no business facts.
Where the task is exploratory (a portfolio, a magazine, a gallery), the deciding element can be a clear entry point into the work rather than facts.
`scripts/first_screen.js` reports where each fact lands; read a "below fold" result as a
question (is there a clear path to it?), not an automatic failure:

```bash
node scripts/first_screen.js page.html "8 am" "Willow Street" "Copy address"
```

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
- Structure follows content (see step 2). Vary structures where the content differs;
  repeat one in adjacent sections when the repetition helps the reader compare or
  follow along (two parallel case studies, consecutive steps).
- One clear primary action per view.

**Identity.**
- Theme the framework fully (tokens, radius, neutrals, spacing). Untouched shadcn or
  Tailwind defaults are an unmade decision.
- Real icons from one set or authored SVG, one stroke weight, used only where they help
  recognition. No emoji as icons.
- Theme browser surfaces: selection, caret, scrollbars, focus rings, underline offset,
  tabular numerals.

**Effects.** Gradients, cards, glass, glow, blur and heavy shadows are allowed when their
reason from step 2 still holds in the built page. The reason lives in the concept's
effects budget (and in `DESIGN.md`); an effect with no recorded reason goes. An inline
code comment is optional: add one only when a future maintainer would otherwise be
tempted to remove the effect, for example
`/* unslop-ignore: gradient maps cold-to-warm across the forecast range */`. The scanners
skip lines carrying `unslop-ignore`.

**Honest actions and material.**
- A primary action that is not connected (no stream, no checkout, no form endpoint)
  shows that before anyone clicks: a visible offline, demo or "coming soon" state on or
  beside the control, not a button that looks live and fails afterwards.
- Disclose each limitation **once, at the relevant action**, with one concise note beside the
  sample list, one at the form. Do not repeat the same warning on every card or section.
- Use verbs that describe what actually happens. A form that only validates says "Check
  request" or "Preview request", not "Send"; its result says "checked", not "sent". A
  disabled purchase becomes a working "Add to demo bag" or a "Preview" with a label that
  says what it does, rather than a dead end.
- Don't imply a sequence the brief doesn't state. Numbers, arrows, and a row of verb
  headings ("Walk in / Pay / Briefing") all read as steps. If the order isn't known,
  present independent facts ("No booking needed", "Passes sold at the front desk").
- Imagery follows [references/assets.md](references/assets.md). Never invent photographs,
  people, customers or results. Never leave an empty image slot.
- Original illustration or a concept render must have the same conviction, scale and
  detail as a strong photo-led design: composed at hero scale, with texture and real
  detail of the subject. A small diagram-like drawing at the edge of the layout reads as
  a placeholder.

**States.** Design the states each control actually has. Every interactive element
needs a visible keyboard focus state. Beyond that, a link needs hover; a button needs
hover, active and disabled if it can be disabled, and loading if it triggers slow work; a
form field needs error and disabled where those can happen; a list or data view needs an
empty and a loading state. Skip states a control cannot enter.

**Codebase fit.** Follow the project's naming, file layout and patterns
([references/fitting-the-codebase.md](references/fitting-the-codebase.md)). Motion follows
[references/motion.md](references/motion.md): one authored moment per view, shared tokens,
a `prefers-reduced-motion` guard.

## Step 4. Render and judge (the visual gate)

Render the page at desktop (about 1440px) and mobile (about 390px) widths with real copy,
take screenshots and look at them. Batch your looking: note everything wrong in one pass.

Then judge the actual visual result:

1. Does it feel like this particular place or product, not only its category? Compare it
   with the real sites you studied in step 2. **Could this page belong to any business of
   this type? Does it rely on generic generated artwork, repeated blocks, or typography
   used in place of a real visual idea?** Illustration, bold type and simple layouts are
   all fine when they carry an idea specific to this business; they fail when they are
   the default filling for its category.
2. Is there enough authentic visual material, or is the page leaning on decoration to
   fill the space? Does the material have a deliberate role?
3. Inspect the full composition: is there a clear **focal point**? Is the **whitespace**
   intentional, or are there large empty fields? Do **hierarchy** and the **first task**
   read in that order? Are scale, rhythm, imagery and type balanced across the whole page?
   Once the essentials lead the first screen, does the rest of the page add something
   (the next decision, detail, evidence), or does it restate each essential as its own
   identical section until the page reads like a spec sheet?
4. Does it look good at the real viewport sizes, including what is visible before
   scrolling? On mobile, are the promise, next action and deciding facts easy to find,
   with a clear path to the rest, without the first screen collapsing into a fact sheet?
   Are those facts set as readable text rather than small decorative labels?
5. **Does the first screen feel finished?** If the result only passes the checklist but
   still feels unfinished (a layout awaiting a photo, a schematic standing in for a
   product, warnings louder than content), it fails.
6. Can the visitor actually **complete the promised task**, or is it accurately labeled
   as a demo at the point of action?

**If any answer is no, redesign the composition**, then render and judge again. Do not
patch a failing composition with small tweaks, and do not move on because the scanners
are clean. Steps 5 to 7 run on a page that has passed this gate.

**Across projects.** When several sites are built in one session, compare the finished
first screens side by side. Look for a shared skeleton, a shared illustration hand or a
shared warning voice, and revise whichever site carries it least deliberately. Do not
force expressive decoration onto public-service or operating interfaces that benefit
from restraint.

### Content and imagery pass

After the page passes the gate, look at it from the visitor's side and list what they
still cannot **see, assess, read or complete**. Fix the most important gap first; one gap
fixed well beats several touched lightly. These are prompts to check, not rules every
design must satisfy:

- **What decision does this visual support, what does it actually show, and what
  remains unknown?** Answer all three for each image, drawing or sample. Record what
  remains unknown as an unresolved content need instead of implying the visual settles it.
- **Can they assess what's offered?** A single view rarely lets someone judge an object
  they might buy. Real photos are best; several labeled concept views can help a visitor
  picture the object, but they remain views. Never imply a scale you don't know: ask
  for dimensions.
- **Can they read what's promised?** When reading is the task, at least one complete
  piece should be readable: real content, or sample content the user approved and that
  is labeled as sample.
- **Does every instruction match the real action?** Read the lede, steps, headings,
  buttons and result messages together. If the action only checks or previews, none of
  them should say send, book or buy.
- **Does rendered text survive real data?** Read the actual text in every state, not
  the template. Edits and string joins leave artifacts like stray spaces before commas.
- **Does a visual that works once still work when repeated?** A diagram that explains
  one desktop row can clutter a stack of mobile cards. Compress it or show it once.
- **Does every large region have a job?** Give empty space a role that serves the task
  (showing the product up close, for instance) or crop it.
- **Did image sourcing respect the source?** Honor rate limits and Retry-After headers;
  one attempt per source, then move down the asset ladder.

## Step 5. Compare against the eight patterns

Go through [references/generic-patterns.md](references/generic-patterns.md) section by
section against the rendered page, the whole page and not just the hero:

1. For each of the eight patterns, mark *not present*, *present with a reason* (state it)
   or *present without a reason*.
2. Run the eight-question anti-template audit.
3. Run the final test: cover the logo. Does it still feel like this brand?

## Step 6. Revise up to three generic decisions

Rank the decisions by how easily each could appear unchanged on an unrelated product.
Identify up to three that are genuinely generic: a decision qualifies only when it fails
the central test or a pattern's reason test from step 5. For each one, write the
decision, the pattern it matches, the specific replacement and the tradeoff, then make
the change, render again and re-run step 5 on the changed sections.

If fewer than three qualify, revise only those. If none do, say so and explain briefly
why the design already passes. Do not manufacture revisions to fill the count; a change
that makes a specific design less clear is a regression.

## Step 7. Quality checks

Two kinds of check. **Hard requirements** must pass. **Defaults** are starting points to
check in context: departing from one is fine when the context justifies it, and the
delivery note says why.

Hard requirements:

- **No broken mobile layout.** At about 390px: no horizontal page scroll, no overflowing
  or clipped text, the primary action reachable, layouts recomposed for the narrow screen
  rather than squeezed.
- **Contrast.** WCAG AA: 4.5:1 for body text and placeholders, 3:1 for large text, icons
  and control boundaries, including text over images, gradients or glass.
- **Keyboard and focus.** Every control reachable in a sensible order with a visible
  focus state. Motion respects `prefers-reduced-motion`.
- **The states each control can enter** are designed (see step 3).

Defaults to check in context:

| Default | When departing is fine |
|---|---|
| Body text about 16px | Dense data tables, captions, legal text, a typeface that reads large at a smaller size |
| Tap targets about 44px | Inline text links, dense desktop-only tools; keep enough spacing to avoid mis-taps |
| Line length about 45 to 75 characters | Short UI strings, captions, wide data, display headlines |
| Body line height about 1.4 to 1.6 | Headlines, labels, tight UI text |

Then run the scanners from the project root (paths relative to this skill folder):

```bash
sh scripts/antislop_scan.sh <path>                       # styles, copy and code together
python3 scripts/devibe_scan.py <path> [--severity high]  # styles and markup only
```

A clean scan does not pass the step 4 gate. A scanner finding is a prompt to inspect, like the patterns. If the reason is already
recorded in the concept or audit, leave it. If it has no reason, fix it. Add an
`unslop-ignore` comment only when it helps future maintainers or keeps CI quiet. For a fuller review, also apply the Vercel
Web Interface Guidelines
(`https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`)
and score the five dimensions in [references/audit.md](references/audit.md).

## Step 8. Deliver

Give the user, briefly:

1. **The concept** in one sentence, and the palette, type and layout reasons.
2. **First questions** asked (or the assumptions used instead), and the **asset decision**, meaning
   sources with license and credit, or which rung of the asset ladder was used and why.
3. **Sites studied** in step 2 and the principle borrowed from each.
4. **The visual gate** from step 4: the answer to each question, and any composition
   redesign it caused.
5. **The revisions** from step 6 (up to three): before, after and the tradeoff of each,
   or a short note that none were needed and why.
6. **Effects kept**, each with its reason.
7. **Demo states, placeholders and unresolved content needs.** Every action that is not
   connected, and every piece of real proof, content or imagery the user must supply,
   with the visitor decision each one blocks.
8. **Defaults departed from** in step 7, with the reason.
9. **Anything not checked** (no browser, no real device, no network), stated plainly
   rather than implied as passing.
10. **Assumptions and unresolved needs** from the fact audit. The full fact-by-fact
    audit stays in `DESIGN.md`; the delivery names only what was assumed, labeled or
    removed, and what the user still needs to supply.

For `audit` without edits, report instead: the verdict on the central test, the visual
gate answers, the eight-pattern table, up to three generic decisions with suggested replacements (or none), quality-check failures with
`file:line`, and the scanner results.
