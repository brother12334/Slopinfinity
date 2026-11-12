# Handoff

- **Visitor's job:** understand how the tool helps with a handoff.
- **Content used:** the three things the tool shows (work waiting for review, work blocked by
  someone else, the next owner of each task). No customers, metrics or pricing.
- **Real sites studied:** Linear (the product interface beside a concise claim, so visitors
  judge the tool), Stripe Docs (try it out: a working example), Duolingo (one clear first
  action).
- **Concept:** the product page is the product. A claim, then a working board where you can
  approve a task waiting on your review and watch it pass to its named next owner. The three
  states are then explained in rows that use the board's own state labels, instead of an
  icon grid.
- **Visual material:** the interface, built in HTML. Sample tasks and people are labeled
  "DEMO DATA" in the board header, the viewer is "Mara (sample person)", and the footer says
  so again.
- **Color:** neutral UI; one brand color (relay orange) for actions; three state colors
  (review amber, blocked red, next-owner teal), each contrast-checked on its tint.
- **Type (chosen last):** Schibsted Grotesk; JetBrains Mono for task IDs and the demo label.

## Problems found after rendering, and revisions

1. "Approve and hand off" wrapped to two lines on desktop. Action column widened.
2. State labels in the explanation stretched full width on mobile. Aligned to start.
3. Reset demo was a 33px target. Padding increased.

## Actions

- Approve and hand off works in the demo: state, owner, count and any task it was blocking
  update. Reset demo restores the board.
- Try a handoff scrolls to and focuses the first actionable task.
- Request access says it isn't connected.

## Review pass (five-site-review.pdf)

Claim shortened to 'Know who has it next.' so the board rises (first task and its action are on the first mobile screen). Each task now shows its relay path, previous holder, current holder (lit) and next owner, and the light moves on handoff. Request access carries a demo tag before it is clicked.
