"""Procedural illustrations for the three Juniper Counter concepts.

Each function returns an SVG string. Nothing here depicts a real café; these are drawn
stand-ins for food photography until real photos are supplied.
"""
import math
import random

R = random.Random(7)


def spiral(cx, cy, turns=2.1, r0=10, gap=15, w0=22, w1=34, steps=220):
    """Centerline and width of a bun's dough spiral."""
    pts = []
    tmax = turns * 2 * math.pi
    for i in range(steps + 1):
        t = tmax * i / steps
        r = r0 + gap * t / (2 * math.pi) * 1.0 + 2.2 * t
        w = w0 + (w1 - w0) * i / steps
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t) * 0.92, w, t))
    return pts


def ribbon(pts, side=1.0, scale=0.5):
    """Offset polygon around a centerline."""
    left, right = [], []
    for i, (x, y, w, _) in enumerate(pts):
        a = pts[max(i - 1, 0)]; b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy) or 1
        nx, ny = -dy / n, dx / n
        left.append((x + nx * w * scale, y + ny * w * scale))
        right.append((x - nx * w * scale, y - ny * w * scale))
    poly = left + right[::-1]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in poly) + " Z"


def line(pts, off=0.0):
    out = []
    for i, (x, y, w, _) in enumerate(pts):
        a = pts[max(i - 1, 0)]; b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy) or 1
        out.append((x + (-dy / n) * w * off, y + (dx / n) * w * off))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in out)


def pearls(cx, cy, rad, n, seed):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi); d = rad * math.sqrt(rnd.uniform(0.05, 1))
        x, y = cx + d * math.cos(a), cy + d * math.sin(a) * 0.9
        s = rnd.uniform(3.2, 6.2)
        k = rnd.randint(5, 7)
        poly = " ".join(f"{x + s * math.cos(2 * math.pi * j / k + rnd.uniform(-.3, .3)) * rnd.uniform(.75, 1.15):.1f},{y + s * math.sin(2 * math.pi * j / k) * rnd.uniform(.75, 1.15):.1f}" for j in range(k))
        out.append((x, y, s, poly))
    return out


def flecks(cx, cy, rad, n, seed):
    rnd = random.Random(seed)
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi); d = rad * math.sqrt(rnd.uniform(0, 1))
        yield cx + d * math.cos(a), cy + d * math.sin(a) * 0.9, rnd.uniform(0, 180), rnd.uniform(1.4, 2.6)


# ---------------------------------------------------------------- A: painterly still life

def bun_painted(cx, cy, s=1.0, seed=1, uid="a"):
    pts = spiral(cx, cy, turns=2.05, r0=8 * s, gap=16 * s, w0=24 * s, w1=36 * s)
    body_r = pts[-1][3] and math.hypot(pts[-1][0] - cx, pts[-1][1] - cy) + 18 * s
    g = [f'<g filter="url(#rough-{uid})">']
    g.append(f'<ellipse cx="{cx + 10*s:.1f}" cy="{cy + 22*s:.1f}" rx="{body_r*1.05:.1f}" ry="{body_r*0.86:.1f}" fill="#000" opacity=".35" filter="url(#soft-{uid})"/>')
    g.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{body_r:.1f}" ry="{body_r*0.92:.1f}" fill="url(#crumb-{uid})"/>')
    g.append(f'<path d="{ribbon(pts)}" fill="url(#dough-{uid})"/>')
    g.append(f'<path d="{line(pts, -0.36)}" fill="none" stroke="#5a2e0c" stroke-width="{7*s:.1f}" stroke-linecap="round" opacity=".55"/>')
    g.append(f'<path d="{line(pts, 0.22)}" fill="none" stroke="#ffd79a" stroke-width="{6*s:.1f}" stroke-linecap="round" opacity=".55" filter="url(#soft-{uid})"/>')
    g.append(f'<ellipse cx="{cx - body_r*0.3:.1f}" cy="{cy - body_r*0.35:.1f}" rx="{body_r*0.55:.1f}" ry="{body_r*0.3:.1f}" fill="#fff" opacity=".18" filter="url(#soft-{uid})"/>')
    for x, y, rot, l in flecks(cx, cy, body_r * 0.85, int(26 * s), seed):
        g.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{l:.1f}" ry="{l*0.55:.1f}" transform="rotate({rot:.0f} {x:.1f} {y:.1f})" fill="#2b3a14" opacity=".85"/>')
    for x, y, sz, poly in pearls(cx, cy, body_r * 0.82, int(34 * s), seed + 10):
        g.append(f'<polygon points="{poly}" fill="#f5f1e8"/><polygon points="{poly}" fill="#9a8f7c" opacity=".35" transform="translate(0.9 1.4)"/>'
                 f'<circle cx="{x - sz*0.3:.1f}" cy="{y - sz*0.35:.1f}" r="{sz*0.28:.1f}" fill="#fff"/>')
    g.append("</g>")
    return "".join(g)


def painted_defs(uid="a"):
    return f'''<defs>
  <radialGradient id="dough-{uid}" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#f2b866"/><stop offset=".55" stop-color="#d48a35"/><stop offset="1" stop-color="#8f4f17"/></radialGradient>
  <radialGradient id="crumb-{uid}" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#c9822f"/><stop offset=".7" stop-color="#a5601f"/><stop offset="1" stop-color="#6e3a10"/></radialGradient>
  <radialGradient id="crema-{uid}" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#e6b77d"/><stop offset=".6" stop-color="#b9783f"/><stop offset="1" stop-color="#6f3d17"/></radialGradient>
  <radialGradient id="light-{uid}" cx="22%" cy="12%" r="95%"><stop offset="0" stop-color="#fff3dc" stop-opacity=".55"/><stop offset=".55" stop-color="#fff3dc" stop-opacity="0"/></radialGradient>
  <radialGradient id="vig-{uid}" cx="50%" cy="50%" r="75%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
  <pattern id="linen-{uid}" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#efe8da"/><path d="M0 1.5h6M0 4.5h6" stroke="#e1d8c6" stroke-width="1"/><path d="M1.5 0v6M4.5 0v6" stroke="#e7dfcf" stroke-width=".8"/></pattern>
  <filter id="soft-{uid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>
  <filter id="rough-{uid}"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="6"/></filter>
  <filter id="grain-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
  <filter id="tiger-{uid}"><feTurbulence type="fractalNoise" baseFrequency=".045 .045" numOctaves="3" seed="9"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .18  0 0 0 0 .06  0 0 0 -1.6 1.0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
</defs>'''


def still_life_a(w=1600, h=1000):
    uid = "a"
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Illustration: cardamom buns, an espresso and a halved egg sandwich on a linen cloth">', painted_defs(uid)]
    s.append(f'<rect width="{w}" height="{h}" fill="#2b211b"/>')
    s.append(f'<g transform="rotate(-6 {w*0.55} {h*0.55})"><rect x="{w*0.18}" y="{h*0.06}" width="{w*0.95}" height="{h*1.1}" fill="url(#linen-{uid})"/>'
             f'<rect x="{w*0.18}" y="{h*0.06}" width="{w*0.95}" height="{h*1.1}" fill="url(#light-{uid})"/>'
             f'<path d="M{w*0.18} {h*0.06}v{h*1.1}" stroke="#d3c7b1" stroke-width="10" stroke-dasharray="2 6"/></g>')
    # espresso, top view (cropped by the top edge)
    ex, ey = w * 0.80, h * 0.16
    s.append(f'<ellipse cx="{ex+18}" cy="{ey+30}" rx="250" ry="236" fill="#000" opacity=".28" filter="url(#soft-{uid})"/>')
    s.append(f'<circle cx="{ex}" cy="{ey}" r="236" fill="#f4f0e8"/><circle cx="{ex}" cy="{ey}" r="236" fill="none" stroke="#d9d1c1" stroke-width="4"/>')
    s.append(f'<circle cx="{ex}" cy="{ey}" r="176" fill="#e8e1d3"/>')
    s.append(f'<path d="M{ex-200} {ey+40}a50 50 0 0 1 0 -90h26v90z" fill="#f4f0e8"/>')
    s.append(f'<circle cx="{ex}" cy="{ey}" r="148" fill="#fbf8f2"/><circle cx="{ex}" cy="{ey}" r="124" fill="url(#crema-{uid})"/>')
    s.append(f'<circle cx="{ex}" cy="{ey}" r="124" fill="#000" filter="url(#tiger-{uid})"/>')
    s.append(f'<ellipse cx="{ex-40}" cy="{ey-50}" rx="60" ry="22" fill="#fff" opacity=".25" filter="url(#soft-{uid})"/>')
    # sandwich half
    sx, sy = w * 0.86, h * 0.80
    s.append(f'<g transform="rotate(-18 {sx} {sy}) scale(1.35) translate({-sx*0.26} {-sy*0.26})">'
             f'<ellipse cx="{sx+18}" cy="{sy+30}" rx="190" ry="90" fill="#000" opacity=".25" filter="url(#soft-{uid})"/>'
             f'<path d="M{sx-180} {sy+40} L{sx-60} {sy-150} Q{sx-40} {sy-172} {sx-14} {sy-150} L{sx+170} {sy+40} Z" fill="#e9c98f"/>'
             f'<path d="M{sx-160} {sy+40} L{sx-56} {sy-122} L{sx+150} {sy+40} Z" fill="#f6ead2"/>'
             f'<path d="M{sx-170} {sy+40} h340 v26 h-340z" fill="#d9a85c"/>'
             f'<path d="M{sx-176} {sy+66} h352 v34 h-352z" fill="#fff6e0"/>'
             f'<ellipse cx="{sx-60}" cy="{sy+83}" rx="44" ry="14" fill="#f2a516"/><ellipse cx="{sx+56}" cy="{sy+83}" rx="40" ry="13" fill="#f0a012"/>'
             f'<path d="M{sx-178} {sy+100} q20 -12 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" fill="#6f9a3a" stroke="#4f7a22" stroke-width="3"/>'
             f'<path d="M{sx-180} {sy+108} h360 v30 h-360z" fill="#e3bd7c"/></g>')
    # buns, large and cropped
    s.append(bun_painted(w * 0.57, h * 0.50, 3.4, seed=3, uid=uid))
    s.append(bun_painted(w * 0.13, h * 0.20, 2.6, seed=5, uid=uid))
    s.append(bun_painted(w * 0.62, h * 0.98, 2.7, seed=8, uid=uid))
    s.append(f'<rect width="{w}" height="{h}" fill="url(#vig-{uid})"/><rect width="{w}" height="{h}" fill="#fff" filter="url(#grain-{uid})"/>')
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- B: two-ink riso print

def riso_defs(uid="b"):
    return f'''<defs>
  <pattern id="dotG-{uid}" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(15)"><circle cx="4.5" cy="4.5" r="2.6" fill="#1f6b4a"/></pattern>
  <pattern id="dotGs-{uid}" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(15)"><circle cx="4.5" cy="4.5" r="1.5" fill="#1f6b4a"/></pattern>
  <pattern id="dotY-{uid}" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><circle cx="4" cy="4" r="3.4" fill="#ff8a3d"/></pattern>
  <filter id="ink-{uid}"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="1" seed="4" result="n"/><feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.75" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>
  <filter id="paper-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".6" numOctaves="3"/><feColorMatrix values="0 0 0 0 .55  0 0 0 0 .45  0 0 0 0 .3  0 0 0 .12 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
</defs>'''


def bun_riso(cx, cy, s, uid="b"):
    pts = spiral(cx, cy, turns=2.05, r0=8 * s, gap=16 * s, w0=24 * s, w1=36 * s)
    body = math.hypot(pts[-1][0] - cx, pts[-1][1] - cy) + 18 * s
    g = [f'<g filter="url(#ink-{uid})">']
    # orange ink: the bun, solid + dots
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{body}" ry="{body*0.92}" fill="#ff8a3d" style="mix-blend-mode:multiply"/>')
    # green ink: shadows in the spiral gaps, offset for misregistration
    g.append(f'<g transform="translate(5 -4)" style="mix-blend-mode:multiply"><path d="{line(pts, -0.42)}" fill="none" stroke="#1f6b4a" stroke-width="{9*s}" stroke-linecap="round"/>'
             f'<ellipse cx="{cx+body*0.25}" cy="{cy+body*0.3}" rx="{body*0.85}" ry="{body*0.7}" fill="url(#dotGs-{uid})" opacity=".9"/></g>')
    for x, y, sz, poly in pearls(cx, cy, body * 0.8, int(30 * s), 21):
        g.append(f'<polygon points="{poly}" fill="#f4ecd9"/>')
    g.append("</g>")
    return "".join(g)


def poster_b(w=1600, h=1100):
    uid = "b"
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Two-colour print illustration of a cardamom bun">', riso_defs(uid)]
    s.append(bun_riso(w * 0.52, h * 0.55, 6.2, uid))
    s.append("</svg>")
    return "".join(s)


def small_riso(kind, uid):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" role="img" aria-label="Two-colour print illustration: {kind}">', riso_defs(uid), '<rect width="400" height="300" fill="#f4ecd9"/>']
    if kind == "espresso":
        s.append(f'<g filter="url(#ink-{uid})"><circle cx="200" cy="150" r="118" fill="url(#dotY-{uid})"/><circle cx="200" cy="150" r="78" fill="#1f6b4a" style="mix-blend-mode:multiply"/>'
                 f'<circle cx="196" cy="146" r="56" fill="#ff8a3d" style="mix-blend-mode:multiply"/><path d="M300 136h30a20 20 0 0 1 0 40h-30" fill="none" stroke="#1f6b4a" stroke-width="14"/></g>')
    elif kind == "sandwich":
        s.append(f'<g filter="url(#ink-{uid})">'
                 f'<path d="M50 150 L180 40 L350 150 Z" fill="#ff8a3d"/><path d="M76 142 L180 56 L322 142 Z" fill="url(#dotY-{uid})"/>'
                 f'<path d="M46 150 h308 v16 h-308z" fill="#ff8a3d"/>'
                 f'<path d="M44 166 h312 v34 h-312z" fill="#f4ecd9" stroke="#1f6b4a" stroke-width="3"/>'
                 f'<ellipse cx="120" cy="183" rx="34" ry="12" fill="#ff8a3d" style="mix-blend-mode:multiply"/><ellipse cx="200" cy="183" rx="32" ry="12" fill="#ff8a3d" style="mix-blend-mode:multiply"/><ellipse cx="280" cy="183" rx="34" ry="12" fill="#ff8a3d" style="mix-blend-mode:multiply"/>'
                 f'<path d="M44 204 q12 -10 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0" fill="none" stroke="#1f6b4a" stroke-width="7" style="mix-blend-mode:multiply"/>'
                 f'<path d="M46 212 h308 v20 h-308z" fill="url(#dotY-{uid})"/><path d="M46 232 h308 v8 h-308z" fill="#ff8a3d"/></g>')
    else:
        s.append(bun_riso(200, 150, 2.6, uid))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- C: ink engraving plates

def engraving_defs(uid="c"):
    return f'''<defs>
  <pattern id="hatch-{uid}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><path d="M0 2.5h5" stroke="#1d1a16" stroke-width="1.1"/></pattern>
  <pattern id="hatch2-{uid}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><path d="M0 2.5h5" stroke="#1d1a16" stroke-width="1"/></pattern>
  <pattern id="fine-{uid}" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><path d="M0 2h4" stroke="#1d1a16" stroke-width=".6"/></pattern>
  <filter id="pen-{uid}"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="2"/><feDisplacementMap in="SourceGraphic" scale="2.5"/></filter>
</defs>'''


def plate(kind, uid):
    vb = "70 40 260 250" if kind == "bun" else "0 0 400 320"
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="Ink engraving: {kind}">', engraving_defs(uid)]
    s.append(f'<g filter="url(#pen-{uid})" fill="none" stroke="#1d1a16" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">')
    if kind == "bun":
        pts = spiral(200, 156, turns=2.05, r0=8, gap=19, w0=26, w1=40)
        body = math.hypot(pts[-1][0] - 200, pts[-1][1] - 156) + 16
        s.append(f'<ellipse cx="208" cy="{160+body*0.88}" rx="{body*0.95}" ry="14" fill="url(#hatch-{uid})" stroke="none"/>')
        s.append(f'<ellipse cx="200" cy="156" rx="{body}" ry="{body*0.92}" fill="#f6efe0"/>')
        s.append(f'<path d="{ribbon(pts)}" fill="#f6efe0"/>')
        s.append(f'<path d="{line(pts, -0.42)}" stroke="#1d1a16" stroke-width="7" opacity=".9"/>')
        s.append(f'<path d="{ribbon([(x, y, w * 0.5, t) for x, y, w, t in pts], scale=0.5)}" fill="url(#fine-{uid})" stroke="none" transform="translate(4 4)" opacity=".7"/>')
        for x, y, sz, poly in pearls(200, 156, body * 0.8, 34, 33):
            s.append(f'<polygon points="{poly}" fill="#f6efe0" stroke-width="1.3"/>')
    elif kind == "espresso":
        s.append(f'<ellipse cx="200" cy="250" rx="150" ry="34" fill="url(#hatch2-{uid})" stroke="none"/>')
        s.append('<ellipse cx="200" cy="232" rx="150" ry="34" fill="#f6efe0"/><ellipse cx="200" cy="232" rx="104" ry="20"/>')
        s.append(f'<path d="M120 110 L130 214 Q200 246 270 214 L280 110" fill="#f6efe0"/><path d="M196 120 L204 214 Q240 226 268 212 L276 120" fill="url(#hatch-{uid})" stroke="none"/>')
        s.append('<ellipse cx="200" cy="110" rx="80" ry="18" fill="#f6efe0"/>')
        s.append(f'<ellipse cx="200" cy="112" rx="66" ry="12" fill="url(#hatch2-{uid})"/>')
        s.append('<path d="M280 132 q46 4 40 40 q-6 30 -46 30"/>')
        s.append('<path d="M180 92 q-10 -24 6 -40 M214 92 q-10 -24 6 -40" stroke-width="1.6"/>')
    else:
        s.append(f'<path d="M60 250 L190 70 L340 250 Z" fill="#f6efe0"/>')
        s.append(f'<path d="M84 232 L190 92 L314 232 Z" fill="url(#fine-{uid})" opacity=".55"/>')
        s.append('<path d="M60 250 h280 v22 h-280z" fill="#f6efe0"/><path d="M60 272 h280 v18 h-280z" fill="#f6efe0"/>')
        s.append('<ellipse cx="150" cy="281" rx="34" ry="6" fill="#1d1a16"/><ellipse cx="248" cy="281" rx="30" ry="6" fill="#1d1a16"/>')
        s.append('<path d="M58 292 q14 -10 28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0" stroke-width="1.6"/>')
        s.append(f'<path d="M60 296 h280 v16 h-280z" fill="url(#hatch-{uid})"/>')
    s.append("</g></svg>")
    return "".join(s)
