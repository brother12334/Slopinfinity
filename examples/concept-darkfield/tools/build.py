"""Build index.html: inlines the moon calendars and writes the session list from moons.py."""
import datetime as dt
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import almanac  # noqa: E402
import moons  # noqa: E402


def fmt(d):
    return d.strftime("%A %-d %B %Y")


rows = []
for s in moons.sessions():
    d = dt.date.fromisoformat(s["session"])
    nm = dt.datetime.strptime(s["new_moon_utc"], "%Y-%m-%d %H:%M")
    rows.append(f'<tr><th scope="row"><time datetime="{d.isoformat()}">{fmt(d)}</time></th>'
                f'<td>{nm.strftime("%-d %b %Y, %H:%M")} UTC</td></tr>')

wide = almanac.month_svg(2026, 12, [12], uid="w")
compact = almanac.month_svg(2026, 12, [12], uid="c", compact=True)
strip = almanac.strip_svg(dt.date(2026, 12, 9), 30, uid="s")

html = (ROOT / "tools" / "page.html").read_text()
html = html.replace("{{CAL_WIDE}}", wide).replace("{{CAL_COMPACT}}", compact).replace("{{STRIP}}", strip)
html = html.replace("{{ROWS}}", "\n".join(rows))
(ROOT / "index.html").write_text(html)
print("wrote index.html", len(rows), "sessions")
