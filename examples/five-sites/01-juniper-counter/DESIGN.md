# Juniper Counter

- **Visitor's job:** decide whether to visit today.
- **Content used:** Wed–Sun 8 am–3 pm; espresso, cardamom buns, egg sandwiches; 24 Willow Street.
- **Real sites studied:** La Cabra (hours and location within easy reach), Ottolenghi
  (make the food tangible), NYC311 ("today" information first, borrowed across categories).
- **Concept:** the counter seen from the door. An illustrated counter with the three things
  on it, beside an egg-yolk panel that answers "when and where": a Monday-to-Sunday strip
  (closed days dashed) and the address with Copy address. No live open/closed status: no
  time zone is given, so the visitor reads today off the strip.
- **Visual material:** an original flat illustration drawn for this page. A licensed
  Commons photo (CC0) was chosen but could not be downloaded (rate limited); the download
  was cancelled at your request.
- **Palette:** egg yolk `#f6d365`, juniper-berry blue `#22305a`, cardamom green `#4f6b25`.
- **Type (chosen last):** Bricolage Grotesque 800 / Nunito Sans.

## Problems found after rendering, and revisions

1. Photo column forced to the image's intrinsic width: text column overflowed by 33px.
   Columns set to `minmax(0, 1fr)`.
2. Mobile: photo first pushed hours and address to y=932. Text first; illustration after.
3. "On the counter" repeated the headline's three items as an icon row. Removed.
4. Sandwich floated on the counter front; scene left empty tiles. Sandwich moved onto the
   counter, scene anchored to the panel bottom (a `slice` crop tried first cut the food off,
   so it was reverted to `meet`).

## Actions

- Copy address works (clipboard), with a fallback message.
- No booking, ordering or live status on this page.
