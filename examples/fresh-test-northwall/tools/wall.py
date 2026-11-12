"""Illustrated bouldering wall: plywood panels, T-nut grid, shaded resin holds with chalk.

Drawn for the Northwall demo; it shows the kind of wall, not this gym's actual routes.
"""
import math
import random

HOLD_COLORS = [("#1f9e98", "#147570", "#5cc7c1"), ("#e2557d", "#b13459", "#f08aa7"),
               ("#2f5bd3", "#1f3f99", "#6d8ff0"), ("#97c93d", "#6e9a22", "#c2e47a"),
               ("#f08a24", "#c0650d", "#f7b46d"), ("#232323", "#0c0c0c", "#575757")]


def blob(cx, cy, r, rnd, k=8, wobble=0.35):
    pts = []
    for i in range(k):
        a = 2 * math.pi * i / k + rnd.uniform(-0.2, 0.2)
        rr = r * rnd.uniform(1 - wobble, 1 + wobble * 0.6)
        pts.append((cx + rr * math.cos(a), cy + rr * 0.8 * math.sin(a)))
    d = ""
    n = len(pts)
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        if i == 0:
            d += f"M{p1[0]:.1f},{p1[1]:.1f}"
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d + "Z"


def hold(cx, cy, r, color, rnd, uid):
    base, dark, light = color
    shape = blob(cx, cy, r, rnd, k=rnd.choice([6, 7, 8, 9]))
    g = [f'<g>',
         f'<path d="{shape}" fill="#000" opacity=".28" transform="translate({r*0.18:.1f} {r*0.26:.1f})" filter="url(#hs-{uid})"/>',
         f'<path d="{shape}" fill="{dark}"/>',
         f'<path d="{shape}" fill="{base}" transform="translate({-r*0.06:.1f} {-r*0.08:.1f}) scale(.94)" transform-origin="{cx:.1f} {cy:.1f}"/>',
         f'<ellipse cx="{cx - r*0.28:.1f}" cy="{cy - r*0.3:.1f}" rx="{r*0.38:.1f}" ry="{r*0.2:.1f}" fill="{light}" opacity=".75" transform="rotate(-20 {cx:.1f} {cy:.1f})"/>']
    # chalk on the top edge
    for _ in range(rnd.randint(4, 9)):
        a = rnd.uniform(math.pi * 1.05, math.pi * 1.95); d = r * rnd.uniform(0.3, 0.85)
        g.append(f'<circle cx="{cx + d*math.cos(a):.1f}" cy="{cy + d*0.8*math.sin(a):.1f}" r="{rnd.uniform(1.5, r*0.12):.1f}" fill="#fff" opacity="{rnd.uniform(.35,.7):.2f}"/>')
    # bolt
    g.append(f'<circle cx="{cx + r*0.05:.1f}" cy="{cy + r*0.02:.1f}" r="{max(3, r*0.11):.1f}" fill="{dark}"/><circle cx="{cx + r*0.05:.1f}" cy="{cy + r*0.02:.1f}" r="{max(2, r*0.07):.1f}" fill="#c9c9c9"/>')
    g.append('</g>')
    return "".join(g)


def wall(w=1600, h=1000, seed=4, uid="w", density=1.0, angle=0):
    rnd = random.Random(seed)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Illustration of a bouldering wall with coloured holds">',
         f'''<defs>
  <linearGradient id="ply-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3c79c"/><stop offset="1" stop-color="#c9a776"/></linearGradient>
  <filter id="hs-{uid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="grain-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".012 .3" numOctaves="3" seed="2"/><feColorMatrix values="0 0 0 0 .45  0 0 0 0 .3  0 0 0 0 .15  0 0 0 .22 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
  <filter id="dust-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".004" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .5 -.12"/><feComposite in2="SourceGraphic" operator="in"/></filter>
</defs>''']
    s.append(f'<g transform="rotate({angle} {w/2} {h/2})">')
    s.append(f'<rect x="-200" y="-200" width="{w+400}" height="{h+400}" fill="url(#ply-{uid})"/>')
    s.append(f'<rect x="-200" y="-200" width="{w+400}" height="{h+400}" fill="#000" filter="url(#grain-{uid})"/>')
    # panel seams
    for x in range(-200, w + 200, 400):
        s.append(f'<path d="M{x} -200V{h+200}" stroke="#a78456" stroke-width="3"/>')
    for y in range(-200, h + 200, 400):
        s.append(f'<path d="M-200 {y}H{w+200}" stroke="#a78456" stroke-width="3"/>')
    # T-nut grid
    for x in range(-180, w + 200, 50):
        for y in range(-180, h + 200, 50):
            s.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#6e5434"/>')
    # holds along a few rising lines (routes), colour-grouped
    for route in range(int(6 * density)):
        col = HOLD_COLORS[route % len(HOLD_COLORS)]
        x = rnd.uniform(0, w); y = h + 60
        for _ in range(rnd.randint(5, 8)):
            x += rnd.uniform(-130, 130); y -= rnd.uniform(110, 190)
            s.append(hold(x, y, rnd.uniform(18, 44), col, rnd, uid))
    # a few big volumes
    for _ in range(int(2 * density)):
        col = HOLD_COLORS[rnd.randint(0, 3)]
        s.append(hold(rnd.uniform(0, w), rnd.uniform(0, h), rnd.uniform(70, 110), col, rnd, uid))
    s.append(f'<rect x="-200" y="-200" width="{w+400}" height="{h+400}" fill="#fff" filter="url(#dust-{uid})"/>')
    s.append('</g></svg>')
    return "".join(s)


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w").write(wall(seed=int(sys.argv[2]) if len(sys.argv) > 2 else 4))
