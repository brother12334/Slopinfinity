# The eight generic patterns

Source: [visual-reference.pdf](visual-reference.pdf), "Beyond the AI website template".
This file is the authority for the skill. Where another reference disagrees with it,
this one wins.

A recognizable pattern is **a prompt to inspect, not an automatic ban**. Each of the
eight is allowed when you can state, in one sentence tied to this product's content or
audience, the job it does. "It looks modern" and "it adds depth" are not reasons.

The PDF's own illustrations share one palette (paper, deep green, a rust accent, a serif
display face). That is the PDF's identity, not a recommended look. Build each project's
identity from its own subject.

---

## 1. Color: a palette as the personality

**Generic default.** A purple or violet gradient haze (or any stock palette) that would
fit almost any product.

**Why it fails.** It signals a category without saying what the brand believes or does.

**Better move.** Pick colors from the subject, the audience and the tone, and give each
color a role. The PDF's farm-journal example: paper, foliage, soil, and one clear action
color.

**Reason test.** For each color in the palette, can you name its role and where it came
from? A gradient passes when it encodes something (a temperature scale, a time of day, a
material) or is part of a documented brand; it fails when it only fills a background.

## 2. Message: the interchangeable hero

**Generic default.** "Unlock your potential with intelligent solutions." "Streamline,
optimize and scale." A decorative dashboard placeholder below.

**Why it fails.** Abstract promises make visitors work out the product, the user and the
outcome for themselves. A decorative dashboard does not resolve that.

**Better move.** Name the user's problem, the concrete result and the evidence. Put a
real task or a representative interface beside the claim ("Know which invoices will be
paid late" next to an at-risk list with real-looking names and amounts).

**Reason test.** Swap in a competitor's name. If the page still works, rewrite it.

## 3. Layout: cards for everything

**Generic default.** Six identical rounded boxes, each an icon circle, a one-word title
and a filler line.

**Why it fails.** Identical boxes give unequal ideas equal weight. Repeated icons, radii
and filler make the section feel assembled from components.

**Better move.** Match the structure to the meaning: one lead idea, an ordered process,
a comparison table, a plain list. Use cards when the items are genuine peers that a
person would scan and pick between (plans, products, articles).

**Reason test.** Are these items peers, of similar importance, that the visitor compares
or chooses among? If not, they are not cards.

## 4. Surface: glass without a reason

**Generic default.** Translucent, blurred panels stacked over a colored background.

**Why it fails.** Blur and transparency reduce text contrast, make stacking ambiguous,
and use decoration to suggest complexity.

**Better move.** Opaque surfaces, visible grouping and a clear reading order. Add depth
only when it explains overlap or focus.

**Reason test.** Glass passes when something real sits behind it that the user benefits
from seeing (a map under a floating panel, a video under its controls) and the text on it
still meets contrast. Otherwise use an opaque surface.

## 5. Typography: bland type, bland hierarchy

**Generic default.** One neutral voice: a centered headline, a centered subhead, similar
line lengths, predictable weights.

**Why it fails.** No editorial rhythm. Nothing tells the eye where to go.

**Better move.** A deliberate type system matters more than the font choice. Define
three voices:
- **Display:** headlines, with character.
- **Body:** readable at length.
- **Utility:** small labels, metadata, navigation, data (a small caps, mono or condensed
  style is fine here when it carries real information like an issue number or a date).

Vary scale, alignment and line length to guide attention.

**Reason test.** Can you name the three voices and where each is used? Is the headline
left-aligned or centered for a reason?

## 6. Proof: meaningless metrics

**Generic default.** "10K+ users. 99.9% uptime. 5x faster." "Trusted by teams worldwide."

**Why it fails.** A number with no unit, period, baseline or source is decoration, and
the claim may be impossible to evaluate.

**Better move.** Use a metric tied to a user outcome, and label it: the measure, the
population, the period, the baseline and the source ("Late payments fell 18% for 34
pilot customers over 90 days. Source: pilot invoice records vs. the prior 90 days."). If
the proof is weak, show the product instead.

**Reason test.** Could a skeptical reader check this number? Never invent metrics,
customer names, logos or testimonials. When real proof is missing, use clearly labeled
placeholders and list them for the user to replace.

## 7. Features: the endless icon grid

**Generic default.** Eight icon circles labeled Smart, Secure, Flexible, Fast, Sync,
Share, Track, Scale.

**Why it fails.** Repeated symbols make different features feel interchangeable.
Labels like "Smart" and "Fast" say nothing about a workflow.

**Better move.** Group features around real tasks. Show the sequence, the decisions
and a representative screen ("Capture a request, check the details, approve with
context" beside a request card showing "Poster print, budget $240, approved"). Let the
interface carry the explanation.

**Reason test.** Does each feature name a thing a user does, with an object? "Approve
with context" passes; "Smart" fails.

## 8. Effects: glow competing with content

**Generic default.** Several luminous blurred spots behind a dark hero.

**Why it fails.** The glows compete with the heading and the action. Brightness stands
in for hierarchy and can hurt readability.

**Better move.** Reserve effects for one meaningful focal point. Start with spacing,
contrast and useful content. Add restrained light only if it clarifies emphasis.

**Reason test.** Is there at most one effect per view, and does it point at the thing
the visitor should look at or do?

Record each effect's reason in the design concept or the audit. An inline code comment
is optional and only worth adding when it helps future maintainers.

---

## The anti-template audit

Run it on the full page, not just the hero. Answer each with yes or no and the evidence.

| # | Check | Question |
|---|---|---|
| 1 | Message | Can a visitor tell who it serves, what it does and the next action within five seconds? |
| 2 | Specificity | Could this headline, image or metric belong to a competitor? Replace what is interchangeable. |
| 3 | Hierarchy | Is there one clear lead idea per section, with secondary ideas visibly secondary? |
| 4 | Structure | Does each layout fit its content, or is every section a row of rounded cards? |
| 5 | Proof | Do numbers have units, dates, context and a source? Unsupported claims removed? |
| 6 | Visual identity | Can you explain the palette, type, imagery and shapes in terms of the brand? |
| 7 | Effects | Do gradients, blur, glass and glow serve the content? Anything that only fills space removed? |
| 8 | Accessibility | Text contrast, focus states, motion, responsive layout, readable type sizes. |

**Final test.** Remove the logo. Would the page still feel like the same brand?

## Revising up to three generic decisions

After the audit, rank the decisions on the page (each section's structure, the hero
claim, the palette, the type system, each effect, each proof element) by how easily each
could appear unchanged on an unrelated product. Take up to three that genuinely fail a
reason test or the central test (does this communicate the product clearly and feel
specific to its audience?). For each write:

1. **The decision**, as built ("six-card feature grid with icon circles").
2. **The pattern** it matches (from the eight above).
3. **The replacement**, specific to this product ("three-step approval flow beside a
   real request card").
4. **The tradeoff** the replacement accepts (more content to write, less scannable, a
   placeholder the user must fill).

Make the changes, re-run the audit, and report them at delivery. If fewer than three
qualify, change only those; if none do, say so. Never manufacture a revision to fill the
count.
