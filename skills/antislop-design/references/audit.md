# Scored audit

Adapted from the impeccable skill's audit (Apache License 2.0, see NOTICE.md). Verify every
finding in context before reporting it. Keep scanner findings separate from visual judgment,
and call out false positives.

## Dimensions (score each 0 to 4)

0 = systemic drift, 1 = major repeated failures, 2 = several verified issues,
3 = minor isolated issues, 4 = coherent and intentional.

1. **Accessibility.** Contrast (body and placeholder at least 4.5:1, large text 3:1),
   visible keyboard focus, semantic elements over clickable divs, labels on inputs, alt
   text, ARIA only where native semantics fall short, touch targets at least 44px,
   reduced-motion respected.
2. **Performance.** Image sizes and formats, font loading (subset, `font-display`), layout
   shift, animation on compositor-friendly properties, bundle weight of UI libraries,
   long lists virtualized.
3. **Theming.** Colors, radius, spacing and motion come from tokens, not hardcoded values.
   Light and dark both designed if both ship. Browser surfaces themed.
4. **Responsive.** Real copy at every breakpoint, no overflow or orphaned controls, layouts
   recomposed for small screens rather than squeezed.
5. **Implementation integrity.** Does the code express one coherent, product-specific
   system, or is it interchangeable with an unrelated product? Repeated shortcuts,
   design-system drift, decorative or fake content, the scanner's high-severity tells.

## Report

Start with the integrity verdict (pass or fail, with evidence). Then:

| # | Dimension | Score | Key finding |
|---|---|---|---|
| 1 | Accessibility | ? | |
| 2 | Performance | ? | |
| 3 | Theming | ? | |
| 4 | Responsive | ? | |
| 5 | Implementation integrity | ? | |
| | **Total** | **?/20** | |

Bands: 18 to 20 excellent, 14 to 17 good, 10 to 13 acceptable, 6 to 9 poor, 0 to 5 critical.

Tag each issue by severity:

| Tag | Meaning | When to fix |
|---|---|---|
| P0 | Stops a task | Now |
| P1 | Real difficulty, or a WCAG AA failure | Before release |
| P2 | Annoyance with a workaround | Next pass |
| P3 | No real user impact | If time allows. Keep these few, or they bury the rest |

For each: location (`file:line`), category, impact on the user, the standard it breaks if
any, and the specific fix. Then list systemic patterns ("hardcoded colors in 15
components") and what is working well, so it gets kept.
