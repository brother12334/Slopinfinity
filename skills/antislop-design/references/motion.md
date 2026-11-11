# Motion

Motion is the fastest way to make a site look generated: a fade-up on every section, a
bounce on every button, a glow pulse nobody asked for. Treat each animation as a decision
you can justify.

## Principles

- **One authored moment per view.** Pick the single place where motion carries meaning
  (the product reveal, the state change the user waits for) and spend effort there. Do not
  give every section the same entrance.
- **Motion explains a change.** Something opened, moved, loaded, failed, succeeded. If you
  cannot name the state change, cut the animation.
- **Start visible.** Animate from an already-readable default so content never depends on
  JavaScript or a finished animation to be seen.
- **Faster out than in.** Opening can take a beat; closing should feel immediate.
- **Ease out for arrivals.** An exponential or strong ease-out curve for things entering
  and moving. Linear only for loops (shimmer, spinners, skeleton pulse). Bounce only where
  the moment is playful, never by default.
- **Small distances, small scales.** Elements travel a few pixels and scale from just under
  1, not from 0. Large travel reads as a template.
- **Reach past transform and opacity** when it stays smooth: blur, clip-path, mask,
  backdrop-filter and shadow are all available.
- **Always guard `prefers-reduced-motion`.** Replace movement with an instant change or a
  plain fade.

## Tokenize

Hardcoded `300ms ease` scattered across files is a tell of its own. Define a small shared
scale once and reference it everywhere:

- a handful of durations, named by use (stagger, micro, quick, fast, medium, slow), roughly
  40ms at the bottom to 500ms at the top
- three or four easings: a smooth ease-out, ease-in-out for swaps, linear for loops, an
  optional bounce
- a short distance scale in px and a short scale scale just below 1

When tokenizing existing code, map each value by **what the motion does**, not by the
number. A 300ms modal close belongs on the "close" token even if that token is 150ms. If
a value matches no token's purpose, leave it alone and say so.

## Picking the right transition

Match the visible element first, then the verb:

| Element | Transition |
|---|---|
| Surface grows from a trigger, anchored | origin-aware dropdown |
| Surface appears centered, no anchor | modal scale-in, softer scale-out |
| Region slides into the page | panel reveal |
| Two screens, list and detail | side-by-side page slide |
| Container changes size | animated width/height |
| Label changes and shares letters (Copy to Copied) | text morph |
| Label changes, shares nothing (Processing to Done) | text swap |
| Two icons in one slot | icon cross-fade with slight blur and scale |
| Number updates often and should stay quiet | subtle digit cross-fade |
| Number change is an event | rolling counter |
| Validation error | short shake plus message |
| Placeholder then real content | skeleton, then cross-fade |
| Segmented control | sliding active pill |
| Hover hint | delayed tooltip in, instant out |
| Collapsible section | grid-rows accordion |

When two fit, choose the lighter one (dropdown over modal, resize over panel).

## Recipes

For production CSS for each of these, install the transitions.dev skill
(https://transitions.dev). Its license allows using the transitions in your projects but
not republishing the collection, so its snippets are not bundled here. With it installed,
its `transitions review`, `transitions apply` and `transitions refine` commands slot into
Phase 4 of this workflow.

For springs, layout animation, exit animation or gestures, use motion (motion.dev). A hover
or fade needs only CSS.
