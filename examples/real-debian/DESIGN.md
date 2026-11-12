# Debian: unofficial design concept (real-organization test)

Private test of the design process on a real organization. **Not affiliated with or
endorsed by the Debian project.** Debian is a registered trademark owned by Software in the
Public Interest, Inc. The page carries this notice at the top and in the footer.

## Sources and terms (checked 12 November 2026)

| Material | Source | Terms |
|---|---|---|
| Open Use Logo, with and without "debian" (`brand/openlogo-*.svg`) | www.debian.org/logos | © 1999 SPI; LGPL-3.0-or-later or CC BY-SA 3.0. Trademark guidelines: keep proportions; don't use as your own branding; link to debian.org. |
| Brand red #CE0056 | www.debian.org/logos | PANTONE Strong Red C equivalent |
| "Ceratopsian", Debian 13 artwork (`brand/ceratopsian-*.svg`) | wiki.debian.org/DebianArt/Themes/Ceratopsian | © 2024 Elise Couper; CC BY-SA 4.0 or GPL-2.0-or-later. "This is the theme chosen for Trixie." |
| Facts, wording and links | www.debian.org (home, /distrib/, /releases/stable/, /logos/, /trademark, /license) | Debian WWW pages: MIT (Expat) or GPL for material since 2012 |

Not used: the homepage's people photos (no photographer or licence shown, identifiable
people), the Swiss Army knife photo (third-party trademark), and the installer screenshot
(its own source and terms not verified), as agreed.

## Verified facts used

- Debian 13 "trixie"; 13.0 released 9 August 2025; 13.7 released 12 September 2026.
- Full support until 9 August 2028; LTS until 30 June 2030; fewer architectures during LTS.
- Architectures at release: amd64, AArch64, armhf, POWER, riscv64, IBM System z.
- Download options and their descriptions from /distrib/: netinst (small, Internet needed),
  DVD-1 (all desktop environments, no Internet needed), live GNOME/Xfce/KDE with Calamares
  (64-bit PC only), cloud images (OpenStack, QEMU, EC2, Azure), vendors, pre-installed.
- Homepage wording: "Debian is a complete Free Operating System!", "Debian is a Community
  of People!", section names and blurbs; banner slogan "The universal operating system".
- Project news titles and dates from the homepage.

All download links point to the official destinations listed on www.debian.org/distrib/
(cdimage.debian.org, cloud.debian.org) or to www.debian.org pages. The primary button
uses the same netinst ISO as the homepage's own Download button.

## Peers studied

- **Ubuntu** (ubuntu.com/download/desktop): a row per architecture with file size and a
  Download button; the clearest at a glance. Heavy chrome and a cookie banner on arrival.
- **Fedora** (fedoraproject.org): a bold blue field and a large release number; editions
  sit below the fold.
- **Debian today** (debian.org, /distrib/): the homepage already pairs the swirl with a
  Download button; the download page is a dense list of links.

## Directions

| Direction | Material | Result |
|---|---|---|
| 1, Release artwork (`d1-release-art.html`) | Ceratopsian artwork as the hero, red logo on white, Fira Sans | Polished but conventional: hero plus three identical cards; mostly restates Debian's current banner |
| 2, Swirl and manual (`d2-swirl-manual.html`) | The open-use swirl at full scale, Source Serif/Sans, a decision table | **Chosen**: more distinctive and easier to choose from. First draft broke on mobile (swirl over the headline) |

The build (`index.html`) adds a release section on the Ceratopsian artwork with a support
timeline, project news and community links. Fixes after rendering: swirl moved off the
navigation and headline on desktop and above the text on mobile; timeline labels listed
on mobile instead of colliding; horizontal overflow removed.

## Verdict

- **Download usability: better than the current Debian pages, close to Ubuntu.** One
  primary download with its type and the Internet requirement stated beside it; a
  three-row decision table answers "which image do I need?" in plain terms. Weaker than
  Ubuntu on two points: no file sizes (not published on /distrib/, so not shown) and only
  64-bit PC images up front, with other architectures behind "All images".
- **Debian identity: strong and honest.** Every visual element is Debian's own: the logo,
  the red and the release artwork, plus Debian's own wording.
- **Visual quality: good, but not inventive.** The swirl-and-Download hero is Debian's
  existing homepage idea, enlarged and cleaned up rather than a new one. Below the hero
  the page is a well-set documentation layout (table, three text columns, news list):
  clear, but plain.
- **Whole-page polish: mostly there; mobile is the weak spot.** The cropped swirl and the
  notice push the download button to 656px on a 390×844 screen, and the community
  section has no images because no licensed community photos were available.

Overall: a credible, honest improvement for Debian's download task, with real brand
fit. It is not a striking redesign, and the mobile hero needs another pass.

## Missing material

- Licensed community photos (DebConf and others) with photographer credits.
- Image file sizes and per-architecture download links from an official source.
- Translations: debian.org is published in many languages; the concept is English only.
- Search and the full site navigation are not designed.
