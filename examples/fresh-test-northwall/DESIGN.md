# Northwall Bouldering: fresh test of the revised skill

A test brief used after the Juniper Counter concepts, to check whether the revised concept
stage (identity and usability judged together) gives a strong page on a different site
type, without borrowing Juniper's look.

## Brief

Claude wrote this test brief itself. Only a one-line summary was shown to the user:
an indoor climbing gym; hours; day pass $22; shoe hire $5; a 15-minute safety briefing with
no booking; passes sold only at the desk. Claude's notes also held an address
(3 Foundry Lane), a $190 10-visit pass and "briefing included in the price". Those were
never shown to the user, so they count as invented and have been removed (see Fact audit).

Hours used: Monday to Friday 7 am to 10 pm, Saturday and Sunday 9 am to 8 pm.
Visitor's decision: can I go today, what will it cost, what happens the first time?
Primary action: plan a first visit.

## Essentials (Step 1)

Today's hours, the day pass price with shoe hire, "no booking needed" with the briefing,
and (originally) the address, which was later removed as unsupplied. Primary action label: "Plan your first visit".

## Concepts, judged on both axes (Step 2)

Measured with `node scripts/first_screen.js <page> "7 am" "$22" "briefing" "Foundry Lane" "Plan your first visit"`.
Board: `screenshots/northwall-concepts.png` (re-rendered after the fact audit, so the
address and $190 no longer appear). The table records the original judgment. In hindsight
it overrated concept 2's identity: all three concepts share one typeface, palette and wall
illustration, so they are arrangements of one art direction, not three concepts.

| Concept | Usability | Identity | Verdict |
|---|---|---|---|
| 1, full wall with a card (`n1-full-wall.html`) | Passes: all essentials in the first screen at both sizes, 17px on a solid card | Weak: the usual info card on a hero image; with the logo covered it could be any gym | Not chosen |
| 2, front-desk board (`n2-front-desk.html`) | Passes best: hours and price at 63px desktop, 35px mobile; action in the first screen on mobile | Strong: reads like the price board above a gym's desk | **Chosen** |
| 3, split layout (`n3-split-route.html`) | Passes, but on desktop the facts sit at 16.8px under a 72px headline that repeats the address, with dead space above | Middling | Not chosen |

Fixes carried into the build from concept 2: "7 am–10 pm" no longer wraps mid-time; weekend
hours on their own line; the big figure in the first-visit panel is "No booking" (the fact
that decides it), not "15 min"; a working Copy address action (later removed with the unsupplied address).

## Build and revisions

`index.html`. Final measurements: every essential in the first screen at both sizes;
hours, price and "No booking" at 56px (desktop) and 34px (mobile); contrast 16.6:1 and
7.1:1 (cobalt); primary action ends at 336px desktop, 609px mobile. No horizontal overflow,
no targets under 40px, scanners clean.

Revisions after rendering the full page:

1. The lower half repeated the board as four identical label-and-content rows (first
   visit, prices, hours, find us), so hours, prices and "No booking" each appeared twice
   and the page read as a spec sheet. Removed the Prices and Hours sections and moved the
   10-visit price onto the board (later removed as unsupplied).
2. The wall illustration was a decorative strip between sections. Moved it beside the
   first-visit points, where it shows a first-timer the kind of wall they'll meet.
3. The first-visit points were numbered 1–3, which claims an order (pay, then briefing)
   the brief doesn't state. An unordered list with verb headings still read as steps, so
   they are now independent facts: "No booking needed", "Passes sold at the front desk",
   "15-minute safety briefing".

## Assets

Original illustration (`tools/wall.py`, `art/*.svg`): plywood panels, a T-nut grid and
shaded resin holds with chalk. It is labelled "Illustration, not a picture of this gym's
wall" on the image and in the footer. No photos used; Wikimedia Commons was rate-limited
throughout this session, so no attempt was made here. Fonts are Unbounded and Manrope,
self-hosted from @fontsource.

## Fact audit

| Displayed | Source | Status |
|---|---|---|
| Indoor bouldering | "indoor climbing gym" | Kept |
| Hours, "open every day" | Hours in the brief cover all seven days | Kept |
| Day pass $22, shoe hire $5 | Brief | Kept |
| No booking needed, 15-minute briefing on the first visit | Brief | Kept |
| Passes sold at the front desk, no online sale | "passes sold only at the desk" | Kept |
| 3 Foundry Lane, Copy address | Not shown to the user | Removed; Find us says "Address to come" |
| 10-visit pass $190 | Not shown to the user | Removed |
| Briefing "included in the price" | Not shown to the user | Removed |
| "Independent" (meta description) | Not supplied | Removed |
| "Come any time during opening hours", "Everyone starts with a briefing" | Inferences beyond the brief | Removed |
| "Walk in / Pay at the desk / Safety briefing" as headings | Read as a sequence the brief doesn't give | Replaced with independent facts |

## Verdict on the visual test: not passed

The page is clear but looks generated: a generic vector climbing wall beside oversized
numbers and repeated ruled panels. It reads as a price sheet that any climbing gym could
use. The three concepts rearranged the same type, palette and wall artwork, so the
concept stage never compared art directions. The rule that every essential sat in the
first screen also pushed mobile towards an information sheet. These failures produced
the skill changes in that commit (art direction per concept, the "could this belong to
any business of this type" gate question, promise/action/deciding facts instead of every
essential, and the fact audit). The page was deliberately not redesigned to pass.

A real pass would need art direction from this gym's own material: photographs of its
walls, setters, desk and the people who climb there, or a visual idea drawn from
something specific to it. None of that was supplied.

## Distinct from Juniper?

In surface style, yes. That is not enough: it avoided Juniper's look by switching to
another category default, not by finding an idea specific to this gym.

## What works, what's still weak

- Works: the first screen answers the visitor's three questions at both sizes.
- Weak: generic illustrated wall; numbers and ruled panels standing in for a visual idea;
  the page could belong to any bouldering gym.

## What the page can and cannot do

- Can: show hours, prices and the first-visit facts as given; jump to the first-visit
  section.
- Cannot: sell passes (there's no online sale, so there's no buy button); say whether the
  gym is open right now (no time zone given, and the device clock isn't used).

## Unresolved content needs

- The address.
- Photos of the real walls, desk and briefing area.
- What the briefing covers, what to wear, age rules, and whether pay comes before or after
  the briefing.
- A map or directions, and transport or parking.
- Whether the shoe hire price is per visit.
