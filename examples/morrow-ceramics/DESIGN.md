# Morrow Ceramics: design record

Built with the `antislop-design` skill and `references/real-sites.pdf`.

## Step 1. Product and audience

- **Site type:** a small maker's studio that teaches: part home-goods maker (Areaware,
  teenage engineering), part place you visit on a schedule (La Cabra, Cooper Hewitt).
- **Visual material:** none supplied. No logo, photographs, colors or style. No
  permission to source licensed photos. The page has to stand on type, structure and
  drawn material, and must not imply photos of a real studio.
- **Audience:** people curious about trying clay, most likely with no experience.
- **Key task:** Explore workshops. Then request a place.
- **Facts available:** Beginner hand-building workshop, Saturdays 10 am–noon.
  Introduction to the wheel, Sundays 2–4 pm. Small-batch cups and bowls are made in the
  studio. Places are requested through a form; no live booking or payment.
- **Not available, not invented:** reviews, attendance, prices, dates, address, class
  size, teacher names, what each session covers beyond its name.
- **Five-second sentence:** Morrow Ceramics is a small studio that makes cups and bowls
  and runs two weekend workshops; look at the workshops and request a place.

### Questions the skill would ask (answered by assumption, since the brief asked to build)

| Question | Assumption used |
|---|---|
| Imagery: real photos, or may I source licensed images? | Neither. Use authored line drawings, clearly drawings. |
| Brand: fixed colors, fonts, references? | None. Derive from clay and glaze. |
| Content and proof: what is real? | Only the four facts above. |
| Task: what happens after "Request a place"? | A request form that is visibly not connected on this demo page. |

## Step 2. Real sites studied

| Site | Principle borrowed | Not copied |
|---|---|---|
| Areaware (home goods) | A plain statement beside the object; the object's form shapes the page. | Their split-screen color block, photography |
| teenage engineering (physical product) | Precise small labels next to the object; the object is the hero. | Black space, their nav system |
| La Cabra (cafe) | Mood from the made thing; practical info (when, where) within easy reach. | Photography, product-scene hero |
| Cooper Hewitt (museum) | Dates and times kept next to the thing you would come for. | Masthead, image carousel |
| GOV.UK (government portal) | A plain form with clear labels and a predictable confirmation. | Visual identity |

## Step 2. Design concept

1. **Concept:** the potter's profile drawing. Potters and archaeologists draw a vessel as
   a half section: one side shows the outside line, the other side the cut wall, with a
   center axis. That drawing is honest (it is visibly a drawing, not a photo of an object
   we do not have) and it belongs to this craft.
2. **Palette with roles:**
   | Color | Role | Source |
   |---|---|---|
   | Clay `#d8cfc2` | page ground | raw stoneware clay |
   | Shino `#f4efe8` | raised surfaces, form fields | a white shino glaze |
   | Iron `#2a211c` | text, drawing lines | iron-oxide brushwork |
   | Iron light `#5a4a40` | secondary text (5.5:1 on clay) | thinned iron oxide |
   | Iron red `#9b3a1c` | the one action color, section cuts in drawings | an iron-red glaze |
3. **Type system:** Young Serif for display (heavy, soft-edged, reads like a stamped
   mark); Source Sans 3 400/600 for body; DM Mono for times and drawing labels (times are
   data, labels are annotation).
4. **Imagery and shape:** profile drawings with a red section cut; thin rules; a round
   stamp-like wordmark like a potter's chop mark; 2px radius on controls only.
5. **Page hierarchy:**
   - Hero: statement and Explore workshops, beside a large profile drawing of a cup.
   - Workshops: the two workshops side by side. They are genuine peers a visitor chooses
     between, so two panels are the right structure. Day and time lead each panel.
   - The studio: one sentence about the cups and bowls, with a row of profile drawings.
   - Request a place: a plain form with the workshop choice first.
   - Footer: name, times, address placeholder, demo note.
6. **Effects budget:** none. No gradients, shadows, glass or motion.

## Step 4. Visual gate

### First render: failed

| Question | Answer |
|---|---|
| Feels like this kind of place? | Partly. Palette and drawings fit, but one huge outline cup read as a technical diagram. |
| Enough authentic material? | No photos (none supplied). Drawings carry it honestly, but the workshop panels used drawings that implied what each workshop makes, which is not in the brief. |
| Balanced across the page? | No. A dominant single drawing in the hero; a thin "Made here" section with one sentence and labels too small to read on mobile. |
| Good at real sizes? | No. Horizontal overflow of 1846px (unsized SVGs), and on mobile the drawing sat above the headline, pushing Explore workshops to y=889. |

### Composition redesign

1. The hero now holds a shelf of three pots on a baseline, which shows the studio's
   cups and bowls where the studio is introduced. The separate "Made here" section,
   which only repeated one sentence, is gone.
2. Drawings removed from the workshop panels so the page does not imply what each
   workshop produces.
3. Mobile order is text, actions, then the shelf. Explore workshops at y=511.
4. Drawing labels moved from SVG text to HTML so they stay readable at any size.
5. Desktop hero rebalanced: the shelf sits on the same baseline as the buttons; the
   headline uses a non-breaking hyphen so "Hand-building" never splits.

### Second render: passed

All four questions answered yes, with one caveat: real photographs of the studio and
its work would make the page much stronger than drawings can.

## Step 5. Pattern audit

| Pattern | Status |
|---|---|
| 1 Palette as personality | Not generic: clay, shino white, iron and iron-red glaze, each with a role. |
| 2 Interchangeable hero | Passes. The headline is the studio's actual weekly offer. |
| 3 Cards for everything | Two workshop panels, kept: the workshops are genuine peers a visitor chooses between. |
| 4 Glass | Not present. |
| 5 Bland type | Display, body and utility voices defined. |
| 6 Meaningless metrics | Not present. No reviews, numbers or prices. |
| 7 Icon grid | Not present. |
| 8 Glow | Not present. |

Step 6: no further generic decisions to revise after the redesign.

## Step 7. Checks

- No horizontal scroll at 1440px or 390px.
- Contrast: iron on clay 10.2:1, iron-light on clay 5.5:1, shino on iron-red 6.1:1,
  iron-red on clay 4.5:1 (used only for focus rings and large shapes).
- Every visible control at least 44px tall; body text 18px.
- States: buttons have hover, active and focus. Workshop choices show selected and
  focus states. "Request a place" on a workshop pre-selects it in the form. The form
  validates on submit, shows errors, moves focus to the first problem, and on success
  shows that the request was not sent.
- Scanners: style and copy clean; one low code finding is the deliberate
  `name@example.com` hint in an error message.
