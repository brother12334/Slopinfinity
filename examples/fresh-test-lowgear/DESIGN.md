# Lowgear Bike Repair: test of the revised skill

## Brief (shown to the user in full before building)

Lowgear Bike Repair, an independent bicycle repair workshop. Repairs only, no bike sales.

- Address: 41 Canal Row
- Hours: Tuesday to Saturday 9 am–6 pm. Closed Sunday and Monday.
- Prices: Safety check $25 · Puncture repair $15, plus $8 if a new inner tube is needed ·
  Standard service $75 · Full service $140
- Turnaround: most repairs are ready within 2 working days.
- Drop-off: no booking needed; bring the bike in during opening hours. Pay when you collect.
- Phone: 555-0142
- Supplied: no photos, logo, colours or style. No reviews, customer numbers, years in
  business, staff names or certifications.
- Visitor's decision: what will my repair cost, how long will it take, and how do I get my
  bike in? Primary action: call, or come by with the bike.

## Visual material

Wikimedia Commons' API was rate-limited, but its category and file pages loaded, and
original files on upload.wikimedia.org could be fetched one at a time. Two usable photos
came through before the rate limit closed in (see `img/CREDITS.md`); a further shortlist of
15 waited out repeated 10-minute Retry-After responses and was stopped.

Both photos show **Bicycle Kitchen, a real workshop in Los Angeles**, not Lowgear. Every
use is captioned as a different workshop with author and licence (CC BY-SA 4.0). A third
photo (a retailer's e-bike showroom) was rejected because Lowgear sells no bikes.

## Directions (art direction, not arrangement)

All identities are **proposed**: the brief supplied no brand material.

| Direction | Material and treatment | Reference | Result |
|---|---|---|---|
| A, Workbench (`a-workbench.html`) | Documentary workshop photography, plain grotesk, a workshop rate card | Rapha (07): equipment in real use; La Cabra (01): hours and location within reach | **Chosen.** Looks like a real place. Mobile first screen was a text sheet with the photo at the bottom; fixed in the build by moving the photo up |
| B, Repair tag (`b-repair-tag.html`) | Paper job ticket and parcel tag: carbon-blue print, stamp, kraft | SXSW (13): a distinctive graphic system with logistics still legible | Distinct and honest as a proposal, weak in execution: all-Courier text reads as costume, empty kraft field on desktop, headline orphan "IN." |
| C, Shadow board (`c-shadow-board.html`) | Illustrated painted tool board, signwriter slab type | teenage engineering (08): hardware as hero | **Fails.** The tools read as flat clip art, crash into the name and crop at the edges: generic generated artwork |

A service-manual parts diagram was considered and dropped: mapping services to bike parts
would invent what each service includes.

## Judgment of the finished page

- **Works:** the first screen reads as a real workshop at both sizes. Promise ("no booking
  needed"), next action (call), prices and turnaround are all easy to find, and the photo
  carries mood the earlier tests lacked.
- **Fails, plainly:** the specificity is borrowed. The page's character comes almost
  entirely from a photo of someone else's workshop. Take the photo away and the layout is
  a familiar split hero with a bold grotesk headline and a price list: competent, not
  specific to Lowgear. The type and colour add little identity of their own.
- **Weaker below the fold:** the drop-off band is good, but "Find us" is an address, a
  button and a plain hours table; the turnaround and hours are each stated three times
  down the page.
- **Mobile:** the photo now opens the page, but at 230px tall with a two-line credit over
  it, the credit covers a fair part of the image.

## Status: failed visual test

This page remains a failed visual test. Two skill changes came from it afterwards:
another real business's photo cannot be the hero evidence for this one (the caption is
read after the impression is made), and a distinctive direction is refined before being
compared with a polished one. Neither change alters this page. Here the borrowed photo is
still the hero, and the repair-tag direction (B) was set aside after one rough execution
without that refinement.

## Fact audit

| Displayed | Source in the brief |
|---|---|
| Lowgear Bike Repair; repairs only, no bike sales | Name; "Repairs only, no bike sales" |
| 41 Canal Row; 555-0142 | Address; phone |
| Tuesday to Saturday 9 am–6 pm; Sunday and Monday closed | Hours |
| $25, $15 + $8 tube, $75, $140 | Prices |
| Most repairs ready within 2 working days | Turnaround |
| No booking needed; bring the bike in during opening hours; pay when you collect | Drop-off |
| Photo captions | `img/CREDITS.md` (Commons file pages) |

Removed during the build: "Nothing to pay at drop-off" and "That's the usual time for
most repairs", both inferences beyond the brief.

## Assumptions and unresolved needs

- Proposed identity throughout; no brand material was supplied.
- Photos of Lowgear's own bench, tool wall and stand are needed; the page currently
  depends on another workshop's photos.
- What each service includes, whether puncture repairs can be done while you wait, how
  collection is arranged, and payment methods.
- The page has no working actions beyond `tel:` links and in-page anchors.
