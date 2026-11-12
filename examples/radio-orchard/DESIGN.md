# Radio Orchard: design record

Built with the `antislop-design` skill. Steps 1 and 2, written before coding.

## Step 1. Product and audience

- **Audience:** people looking for something interesting to listen to tonight. They
  arrive in the evening, often on a phone, and want to know quickly whether something
  is on and what it is.
- **Key task:** Listen live. One primary action per view.
- **Secondary tasks:** find a show (scan the schedule), submit a song.
- **Problem and outcome:** "Is there something worth putting on tonight?" → four hours
  of community-run radio on Thursdays, with a clear idea of what plays when.
- **Proof on hand:** none. No audience numbers, testimonials, sponsors or past success.
  The schedule is the only content, so the schedule does the persuading.
- **Content inventory, by importance:** Listen live and when it's on; the three shows
  in order; submit a song; footer.
- **Five-second sentence:** Radio Orchard is community-run late-night radio, live every
  Thursday from 8 pm to midnight. Press Listen live.

## Step 2. Design concept

1. **Concept:** the evening seen on a radio dial. The four broadcast hours are drawn as
   a tuning band from 8 to 12, and the shows sit on it where they air. Brown-black
   bark and dial-lamp amber stand in for a wooden radio set; "orchard" comes through in
   the warm wood and fruit tones rather than in leaf illustrations.
2. **Palette with roles:**
   | Color | Role | Source |
   |---|---|---|
   | Bark `#17130f` / `#211b16` | page and raised surfaces | a wooden radio cabinet at night |
   | Paper `#f1e7d6` | primary text | dial-card paper, 15:1 on bark |
   | Dim `#b9ab96` | secondary text | 8.2:1 on bark |
   | Amber `#f2a33a` | the one action color: Listen live, on-air lamp, focus ring | a dial lamp |
   | Violet `#6d4fc2` → `#3a2a73` → `#16122b` | **only** the schedule band | the night sky through the evening |
3. **Type system:**
   - Display: Big Shoulders Display 700/800, condensed signage. Station name, headline,
     show names.
   - Body: Atkinson Hyperlegible 400/700, chosen for reading on a dim phone at night.
   - Utility: IBM Plex Mono 400/500 for times and the dial numerals (times are data).
4. **Imagery and shape:** no photography or illustration (none supplied, none
   invented). Shape language is the dial: thin rules, tick marks, square corners, a
   small 4px radius only on buttons and inputs.
5. **Page hierarchy:**
   - Hero: headline, one-line description, Listen live, "Live every Thursday" line.
   - Tonight's schedule: the dial band (time ruler) with each show's details aligned
     under its slot. A timeline, not cards, because the shows are a sequence.
   - Submit a song: short copy beside a form.
   - Footer: name, schedule line, demo note.
6. **Effects budget:**
   - **One violet gradient**, on the schedule band. Reason: the user asked for one
     violet gradient to evoke a radio signal at night; placing it on the time band lets
     it also encode the night getting later from 8 pm to midnight, so it carries
     meaning instead of decorating a background.
   - On-air lamp: a small amber dot that pulses slowly while the player is on. Turned
     off under `prefers-reduced-motion`.
   - No glow, no glass, no shadows beyond focus rings.

## Step 5. Audit (on the rendered page)

| Pattern | Status |
|---|---|
| 1 Palette as personality | One violet gradient, on the schedule band only, kept with a reason (requested; shows the night darkening across the broadcast hours). Rest of the palette is drawn from the radio-cabinet concept. |
| 2 Interchangeable hero | Passes. The headline names the actual offer: community radio, Thursday, four hours. |
| 3 Cards for everything | Not present. The schedule is a timeline. |
| 4 Glass | Not present. |
| 5 Bland type | Three voices defined. First render: the headline was so large it buried the action (fixed, see step 6). |
| 6 Meaningless metrics | Not present. No numbers, testimonials or logos; none were supplied. |
| 7 Icon grid | Not present. |
| 8 Glow | Not present. |

Final test (cover the wordmark): the dial band, bark-and-amber palette and condensed
signage type still read as this station.

## Step 6. Revisions after the first render

1. **Hero hierarchy.** The headline wrapped to six lines at desktop and pushed Listen
   live to y=876 on a 900px screen, with the schedule a full screen below. Headline
   reduced and widened; Listen live now sits at about y=520 and the schedule band and
   ruler are inside the first desktop viewport. Tradeoff: a less dramatic headline.
2. **Mobile schedule.** Time ranges wrapped mid-range ("9–10:30 / pm") and the band lost
   its labels, leaving bare colored blocks. Time column widened with no wrapping; band
   labels kept at a smaller size. Tradeoff: a wider time column.
3. **Misleading on-air lamp.** A static amber dot beside "Live Thursdays" read as "on air
   now", which the page cannot know. The lamp now appears only while the player is
   playing. Tradeoff: no at-a-glance live indicator until a real schedule check exists.

Smaller fixes: footer items aligned on a baseline; nav and wordmark links padded to
at least 44px tall.

## Step 7. Checks

- No horizontal scroll at 1440px or 390px; no clipped text.
- Contrast: paper on bark 15.1:1, dim on bark 8.2:1, dark text on amber 8.9:1, paper on
  the lightest violet 4.8:1.
- Every visible link, button and input at least 44px tall.
- Body text 17px.
- States: Listen live has hover, active, focus and pressed (playing); with no stream it
  shows an error message. The form validates on submit, shows field errors, moves focus
  to the first bad field, and confirms on success.
- The compact header Listen live button appears once the main one scrolls out of view.
- `prefers-reduced-motion` turns off the lamp pulse and transitions.
- No console errors.
