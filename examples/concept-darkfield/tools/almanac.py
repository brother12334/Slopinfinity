"""Moon-phase calendar for a month: each day shows the Moon as it looks that evening
(21:00 UTC), drawn from the near side's main maria in their approximate positions.

    python3 tools/almanac.py 2026 12 art/december-2026.svg
"""
import calendar
import datetime as dt
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import moons  # noqa: E402

UTC = dt.timezone.utc


def new_moons_around(year, month):
    k0 = math.floor((year + (month - 1) / 12 - 2000) * 12.3685)
    return [moons.jd_to_utc(moons.jde_new_moon(k)) for k in range(k0 - 2, k0 + 3)]


def age_fraction(t, nms):
    prev = max(n for n in nms if n <= t)
    nxt = min(n for n in nms if n > t)
    return (t - prev) / (nxt - prev)


def moon_symbol(uid):
    maria = [(-28, -4, 15, 25, -10), (-14, -24, 13, 12, 0), (8, -19, 8, 8, 0), (15, -3, 11, 9, 20),
             (34, -13, 6, 5, 0), (28, 9, 7, 8, 0), (-8, 18, 9, 7, 0), (-26, 19, 5, 5, 0),
             (-3, -37, 20, 3.5, -4), (6, 4, 5, 6, 0)]
    blobs = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{a}" ry="{b}" transform="rotate({r} {x} {y})"/>' for x, y, a, b, r in maria)
    rays = "".join(f'<path d="M-6 34 L{-6 + 46*math.cos(a):.1f} {34 + 46*math.sin(a):.1f}" />' for a in [i * 0.52 for i in range(12)])
    return f'''<defs>
<radialGradient id="lit-{uid}" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#e9e6dc"/><stop offset=".75" stop-color="#cbc7bb"/><stop offset="1" stop-color="#9d998e"/></radialGradient>
<filter id="soft-{uid}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.6"/></filter>
<filter id="tex-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".09" numOctaves="4" seed="3"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .34  0 0 0 0 .31  0 0 0 .55 -.12"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="edge-{uid}" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation=".9"/></filter>
<clipPath id="disc-{uid}"><circle r="50"/></clipPath>
<g id="moon-{uid}" clip-path="url(#disc-{uid})">
  <circle r="50" fill="url(#lit-{uid})"/>
  <g fill="#878378" opacity=".6" filter="url(#soft-{uid})">{blobs}</g>
  <g stroke="#f4f1e8" stroke-width="1.1" opacity=".09">{rays}</g>
  <circle cx="-6" cy="34" r="2.4" fill="#f7f4ea"/>
  <circle r="50" fill="#000" filter="url(#tex-{uid})"/>
</g>
</defs>'''


def shadow(p, r=50.0):
    """Path for the unlit part at lunation fraction p (0 new, .5 full), Moon seen from the north."""
    x = abs(r * math.cos(2 * math.pi * p))
    if p < 0.5:   # waxing: shadow on the left
        bulge_right = p < 0.25
        return f"M0,{-r} A{r},{r} 0 0 0 0,{r} A{x:.2f},{r} 0 0 {0 if bulge_right else 1} 0,{-r}Z"
    bulge_left = p > 0.75   # waning: shadow on the right
    return f"M0,{-r} A{r},{r} 0 0 1 0,{r} A{x:.2f},{r} 0 0 {1 if bulge_left else 0} 0,{-r}Z"


def moon(p, uid, cx, cy, size):
    s = size / 100
    return (f'<g transform="translate({cx:.1f} {cy:.1f}) scale({s:.3f})">'
            f'<use href="#moon-{uid}"/>'
            f'<path d="{shadow(p)}" fill="#0b0f1a" opacity=".93" filter="url(#edge-{uid})"/>'
            f'<circle r="50" fill="none" stroke="#2b3550" stroke-width="1.2"/></g>')


def month_svg(year, month, session_days, uid="m", compact=False):
    nms = new_moons_around(year, month)
    cal = calendar.Calendar(firstweekday=0)  # Monday first
    weeks = cal.monthdayscalendar(year, month)
    cw, ch, top = (100, 104, 52) if compact else (128, 132, 46)
    fs, ms = (26, 60) if compact else (15, 72)
    w, h = cw * 7, top + ch * len(weeks)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
         f'aria-label="Moon phase each evening in {calendar.month_name[month]} {year}">', moon_symbol(uid),
         f'<style>.d-{uid}{{font:600 {fs}px "Public Sans",sans-serif;fill:#c9d0e0}}.wd-{uid}{{font:600 {fs-2 if compact else 13}px "Public Sans",sans-serif;fill:#8b95ad;letter-spacing:.06em}}'
         f'.s-{uid}{{font:600 {fs}px "Public Sans",sans-serif;fill:#f2d27a}}</style>']
    names = ["M", "T", "W", "T", "F", "S", "S"] if compact else ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    for i, name in enumerate(names):
        o.append(f'<text class="wd-{uid}" x="{i*cw + 10}" y="{30 if compact else 22}">{name}</text>')
    for r, week in enumerate(weeks):
        for c, day in enumerate(week):
            if not day:
                continue
            x, y = c * cw, top + r * ch
            t = dt.datetime(year, month, day, 21, tzinfo=UTC)
            p = age_fraction(t, nms)
            if day in session_days:
                o.append(f'<rect x="{x+3}" y="{y+3}" width="{cw-6}" height="{ch-6}" rx="10" fill="#172038" stroke="#f2d27a" stroke-width="2"/>')

            o.append(f'<text class="{"s" if day in session_days else "d"}-{uid}" x="{x+10}" y="{y + (30 if compact else 26)}">{day}{"" if compact or day not in session_days else " · session"}</text>')
            o.append(moon(p, uid, x + cw / 2, y + (68 if compact else 78), ms))
    o.append("</svg>")
    return "".join(o)


def strip_svg(start, days, uid="s", size=64, gap=14):
    """A row of moons, one per evening, for the hero on wide screens."""
    nms = new_moons_around(start.year, start.month) + new_moons_around((start + dt.timedelta(days=days)).year, (start + dt.timedelta(days=days)).month)
    w = days * (size + gap)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {size + 4}" aria-hidden="true">', moon_symbol(uid)]
    for i in range(days):
        t = dt.datetime.combine(start + dt.timedelta(days=i), dt.time(21), tzinfo=UTC)
        o.append(moon(age_fraction(t, sorted(set(nms))), uid, i * (size + gap) + size / 2, size / 2 + 2, size))
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    y, m, path = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    sessions = [int(a) for a in sys.argv[4:]]
    open(path, "w").write(month_svg(y, m, sessions))
