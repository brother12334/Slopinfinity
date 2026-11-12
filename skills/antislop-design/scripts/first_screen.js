#!/usr/bin/env node
/*
 * first_screen.js - where do the visitor's essentials land, at desktop and mobile?
 *
 *   node first_screen.js <page.html|url> "<essential 1>" "<essential 2>" ...
 *
 * For each essential (a piece of text such as "8 am", "Willow Street", "$22", or the label
 * of the primary action), reports at 1440x900 and 390x844:
 *   - whether it is visible in the first screen
 *   - its top position, font size and weight
 *   - its contrast against what is painted behind it (an image, SVG or gradient behind the
 *     text is reported as "over image" because contrast can't be computed reliably; a solid
 *     panel sitting on top of an image counts as solid)
 * It also reports how much of the first screen is taken by images, SVG or canvas.
 *
 * Needs Playwright (preinstalled in Claude Code cloud sessions). Exit code is the number
 * of essentials missing from the first screen at either size.
 */
const { chromium } = require("playwright");

function lum([r, g, b]) {
  const c = [r, g, b].map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
}
function ratio(a, b) { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); }

(async () => {
  const [target, ...needles] = process.argv.slice(2);
  if (!target || !needles.length) { console.error('usage: node first_screen.js <page> "<text>" ...'); process.exit(2); }
  const url = /^https?:|^file:/.test(target) ? target : "file://" + require("path").resolve(target);
  const browser = await chromium.launch();
  let missing = 0;
  for (const [name, w, h] of [["desktop", 1440, 900], ["mobile", 390, 844]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    await page.goto(url); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(200);
    const res = await page.evaluate(({ needles, h }) => {
      const parse = s => (s.match(/[\d.]+/g) || []).slice(0, 4).map(Number);
      // Walk down the paint stack at the text's centre: the first opaque background wins;
      // an image, SVG, canvas, video or CSS background image first means "over image".
      function behind(el) {
        const r = el.getBoundingClientRect();
        const x = Math.min(Math.max(r.left + r.width / 2, 0), innerWidth - 1), y = r.top + r.height / 2;
        const stack = y >= 0 && y < innerHeight ? document.elementsFromPoint(x, y) : [];
        for (const e of stack) {
          if (/^(IMG|CANVAS|VIDEO)$/.test(e.tagName) || e.closest("svg")) return null;
          const cs = getComputedStyle(e);
          if (cs.backgroundImage && cs.backgroundImage !== "none" && !cs.backgroundImage.startsWith("url(\"data:image/svg")) return null;
          const c = parse(cs.backgroundColor);
          if (c.length >= 3 && (c.length < 4 || c[3] > 0.9)) {
            // an image inside this box paints over its background (pseudo-element overlays
            // also report as this box), so the colour isn't what's behind the text
            const covered = [...e.querySelectorAll("img, svg, canvas, video")].some(m => {
              const q = m.getBoundingClientRect(); return !m.contains(el) && q.left <= x && q.right >= x && q.top <= y && q.bottom >= y;
            });
            return covered ? null : c.slice(0, 3);
          }
        }
        for (let e = el; e; e = e.parentElement) {  // below the fold: fall back to ancestors
          const c = parse(getComputedStyle(e).backgroundColor);
          if (c.length >= 3 && (c.length < 4 || c[3] > 0.9)) return c.slice(0, 3);
        }
        return [255, 255, 255];
      }
      const out = needles.map(n => {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let best = null;
        while (walker.nextNode()) {
          const t = walker.currentNode;
          if (!t.textContent.toLowerCase().includes(n.toLowerCase())) continue;
          const el = t.parentElement; const r = el.getBoundingClientRect();
          if (!r.width || getComputedStyle(el).visibility === "hidden") continue;
          if (!best || r.top < best.top) {
            const cs = getComputedStyle(el); const fg = parse(cs.color).slice(0, 3);
            best = { top: Math.round(r.top + scrollY), size: parseFloat(cs.fontSize), weight: cs.fontWeight, fg, bg: behind(el) };
          }
        }
        return { n, best };
      });
      const media = [...document.querySelectorAll("img, svg, canvas, video")].filter(m => !m.closest("svg svg") && m.getBoundingClientRect().width > 200).reduce((a, m) => {
        const r = m.getBoundingClientRect(); const top = Math.max(r.top, 0), bot = Math.min(r.bottom, h), left = Math.max(r.left, 0), right = Math.min(r.right, innerWidth);
        return a + Math.max(0, bot - top) * Math.max(0, right - left);
      }, 0) / (innerWidth * h);
      return { out, media: Math.min(1, media) };
    }, { needles, h });
    console.log(`\n${name} ${w}x${h}  imagery in first screen: ${Math.round(res.media * 100)}%`);
    for (const { n, best } of res.out) {
      if (!best) { console.log(`  MISSING  "${n}" not found`); missing++; continue; }
      const inFirst = best.top < h;
      if (!inFirst) missing++;
      const c = best.bg ? ratio(best.fg, best.bg).toFixed(1) + ":1" : "over image";
      console.log(`  ${inFirst ? "first screen" : "below fold  "}  "${n}"  top ${best.top}px  ${best.size}px/${best.weight}  contrast ${c}`);
    }
    await page.close();
  }
  await browser.close();
  process.exit(Math.min(missing, 255));
})();
