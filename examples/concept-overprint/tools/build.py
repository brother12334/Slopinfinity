"""Build index.html by inlining the calendar page designs from sheets.py."""
import calendar
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import sheets  # noqa: E402

grid = "\n".join(f'      <figure><div class="sheet">{sheets.sheet(m, uid=f"g{m}")}</div></figure>' for m in range(1, 13))
html = (ROOT / "tools" / "page.html").read_text()
html = (html.replace("{{COVER}}", sheets.cover(uid="hc")).replace("{{JAN}}", sheets.sheet(1, uid="h1"))
        .replace("{{JUL}}", sheets.sheet(7, uid="h7")).replace("{{GRID}}", grid))
(ROOT / "index.html").write_text(html)
print("wrote index.html")
