# North Library

- **Visitor's job:** find a suitable room and understand how to request it.
- **Content used:** open Monday to Saturday, 9 am to 6 pm (Sunday shown as closed). No real
  room list, no booking system.
- **Real sites studied:** GOV.UK (plain language, task first, accessible form with clear
  errors and predictable confirmation), NYC311 (organize by what the visitor wants to do),
  Stripe Docs (fast routes into the task).
- **Concept:** a task-first civic page, no hero. A room finder (group size and needs filter a
  list) with opening hours and the request rules beside it, then the request form. The form
  checks the request against the stated hours: Sundays and times running past 6 pm are
  caught with plain error messages.
- **Visual material:** none. The task is the page.
- **Sample data:** Rooms A to D are labeled "Sample" on every row, in the room select, in a
  notice above the list, and in the footer. No live availability is shown.
- **Type (chosen last):** Public Sans.

## Problems found after rendering, and revisions

1. The page heading touched the header bar: the shared `.wrap` padding overrode the main
   area's top padding. Fixed.
2. Mobile: hours and request rules came first and pushed the rooms to y=1855. The header
   strip already carries the hours, so the panels now follow the room list; the filters
   start on the first mobile screen.

## Actions

- Filters work, with a live count and a no-match message.
- "Request this room" fills the form with that room and moves to it.
- The form validates and, when valid, shows "Request checked, not sent". A notice above the
  form says the page can't send requests.

## Review pass (five-site-review.pdf)

Two long notices replaced by one short note at the room list and one at the form. Per-row Sample badges removed. 'Check and send request' became 'Check request', and the result says 'Your request is ready ... On this demo page it stops here.'
