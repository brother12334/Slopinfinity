# Legible: colour contrast checker (concept)

**Brief (fictional, written for this test):** a free colour contrast checker. Checks a text
colour against a background colour using the WCAG thresholds (AA 4.5:1 normal text, 3:1
large text; AAA 7:1 and 4.5:1; 3:1 for interface parts). Runs in the browser; nothing is
uploaded; no account. Primary action: check two colours.

**Idea:** the page takes on the colours being checked. The result panel is painted in the
user's pair, with the ratio as a huge number and sample text at each size, while the
controls stay in fixed, readable colours. The visual is the working tool.

**Checked:** the ratio math (WCAG 2 relative luminance), rounding down so a pair never
shows as passing when it falls just short (#777 on white: 4.48, shown 4.4, AA normal
fails), invalid hex input with an error message, and the swap button.

**Verdict:** the strongest of the three on usability, and the idea is honest and specific
to the tool. Visually it's the plainest: outside the coloured panel it's a clean utility
page with one typeface. Not yet built: saved pairs, colour-blindness previews, sharing a
link to a result.
