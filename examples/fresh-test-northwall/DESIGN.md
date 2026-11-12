# Northwall Bouldering: fresh test of the revised skill

A test brief used after the Juniper Counter concepts, to check whether the revised concept
stage (identity and usability judged together) gives a strong page on a different site
type, without borrowing Juniper's look.

## Brief

Northwall Bouldering, an independent indoor bouldering gym at 3 Foundry Lane.

- Open Monday to Friday 7 am to 10 pm, Saturday and Sunday 9 am to 8 pm.
- Day pass $22, shoe hire $5, 10-visit pass $190.
- First visit: a 15-minute safety briefing, included, no booking needed.
- Passes are bought at the front desk; there's no online sale.
- No photos, logo, colours or style supplied. No reviews, member counts or route grades.

Visitor's decision: can I go today, what will it cost, what happens the first time?
Primary action: plan a first visit.

## Essentials (Step 1)

Today's hours, the day pass price with shoe hire, "no booking needed" with the briefing,
and the address. Primary action label: "Plan your first visit".

## Concepts, judged on both axes (Step 2)

Measured with `node scripts/first_screen.js <page> "7 am" "$22" "briefing" "Foundry Lane" "Plan your first visit"`.
Board: `screenshots/northwall-concepts.png`.

| Concept | Usability | Identity | Verdict |
|---|---|---|---|
| 1, full wall with a card (`n1-full-wall.html`) | Passes: all essentials in the first screen at both sizes, 17px on a solid card | Weak: the usual info card on a hero image; with the logo covered it could be any gym | Not chosen |
| 2, front-desk board (`n2-front-desk.html`) | Passes best: hours and price at 63px desktop, 35px mobile; action in the first screen on mobile | Strong: reads like the price board above a gym's desk | **Chosen** |
| 3, split layout (`n3-split-route.html`) | Passes, but on desktop the facts sit at 16.8px under a 72px headline that repeats the address, with dead space above | Middling | Not chosen |

Fixes carried into the build from concept 2: "7 am–10 pm" no longer wraps mid-time; weekend
hours on their own line; the big figure in the first-visit panel is "No booking" (the fact
that decides it), not "15 min"; a working Copy address action.

## Build and revisions

`index.html`. Final measurements: every essential in the first screen at both sizes;
hours, price and "No booking" at 56px (desktop) and 34px (mobile); contrast 16.6:1 and
7.1:1 (cobalt); primary action ends at 336px desktop, 609px mobile. No horizontal overflow,
no targets under 40px, scanners clean.

Revisions after rendering the full page:

1. The lower half repeated the board as four identical label-and-content rows (first
   visit, prices, hours, find us), so hours, prices and "No booking" each appeared twice
   and the page read as a spec sheet. Removed the Prices and Hours sections and moved the
   10-visit price onto the board.
2. The wall illustration was a decorative strip between sections. Moved it beside the
   first-visit points, where it shows a first-timer the kind of wall they'll meet.
3. The first-visit points were numbered 1–3, which claims an order (pay, then briefing)
   the brief doesn't state. Now an unordered list.

## Assets

Original illustration (`tools/wall.py`, `art/*.svg`): plywood panels, a T-nut grid and
shaded resin holds with chalk. It is labelled "Illustration, not a picture of this gym's
wall" on the image and in the footer. No photos used; Wikimedia Commons was rate-limited
throughout this session, so no attempt was made here. Fonts are Unbounded and Manrope,
self-hosted from @fontsource.

## Distinct from Juniper?

Yes. Juniper's concepts used cream paper, serif type (Bodoni, Caslon), riso, engraving
and painterly food still lifes. Northwall uses a heavy wide grotesque, thick black rules,
numbers as the largest elements and a cobalt accent, with the art in its own section, not
behind the text.

## What works, what's still weak

- Works: the first screen answers all three questions at both sizes, and the board makes
  that answer the identity rather than a strip under a poster.
- Weak: on mobile the first screen has no imagery, so identity rests on type and rules
  alone. The Find us row on desktop leaves its left half mostly empty. The wall is a
  convincing generic wall, not this gym, so it can't help a visitor judge the gym itself.

## What the page can and cannot do

- Can: show hours, prices and the first-visit facts as given; jump to the first-visit
  section; copy the address to the clipboard.
- Cannot: sell passes (there's no online sale, so there's no buy button); say whether the
  gym is open right now (no time zone given, and the device clock isn't used).

## Unresolved content needs

- Photos of the real walls, desk and briefing area.
- What the briefing covers, what to wear, age rules, and whether pay comes before or after
  the briefing.
- A map or directions, and transport or parking.
- Whether the shoe hire price is per visit.
