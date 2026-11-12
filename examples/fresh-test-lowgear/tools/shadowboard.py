"""Shadow board: a painted tool board with outlines for each tool, some tools hanging,
some out. Proposed identity for the Lowgear demo; it is not a picture of a real board.

    python3 tools/shadowboard.py art/board-wide.svg 1600 900
"""
import math
import random
import sys

PAINT = "#f1ead8"     # outline paint
METAL = ("#8f969c", "#5d646a", "#c9cfd3")  # body, shade, highlight
HANDLE = ("#d4462f", "#9c2c1c", "#ef7a63")


def rr(x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    return (f"M{x+r:.1f},{y:.1f}H{x+w-r:.1f}A{r:.1f},{r:.1f} 0 0 1 {x+w:.1f},{y+r:.1f}"
            f"V{y+h-r:.1f}A{r:.1f},{r:.1f} 0 0 1 {x+w-r:.1f},{y+h:.1f}H{x+r:.1f}"
            f"A{r:.1f},{r:.1f} 0 0 1 {x:.1f},{y+h-r:.1f}V{y+r:.1f}A{r:.1f},{r:.1f} 0 0 1 {x+r:.1f},{y:.1f}Z")


def circ(cx, cy, r):
    return f"M{cx-r:.1f},{cy:.1f}a{r:.1f},{r:.1f} 0 1 0 {2*r:.1f},0a{r:.1f},{r:.1f} 0 1 0 {-2*r:.1f},0Z"


def hexagon(cx, cy, r, rot=0):
    pts = [(cx + r * math.cos(rot + i * math.pi / 3), cy + r * math.sin(rot + i * math.pi / 3)) for i in range(6)]
    return "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"


# Each tool is drawn pointing down from a hook at (0, 0), in local units.
# Returns (outline path, list of (path, role)) where role picks a colour.
def spanner(L=300):
    w = 26
    body = rr(-w / 2, 40, w, L - 80, 10)
    ring = circ(0, 28, 34)
    jaw = circ(0, L - 26, 38)
    hole = hexagon(0, 28, 18, math.pi / 6)
    mouth = f"M-15,{L-26}L-15,{L+20}L15,{L+20}L15,{L-26}Z"
    outline = body + ring + jaw
    return outline, [(body + ring + jaw, "metal"), (hole + mouth, "cut")]


def tyre_lever(L=170):
    body = rr(-17, 0, 34, L, 17)
    hook = f"M-17,{L-30}Q-30,{L+6} 0,{L+10}Q14,{L+10} 17,{L-8}Z"
    slot = rr(-6, 12, 12, 26, 6)
    return body + hook, [(body + hook, "handle"), (slot, "cut")]


def screwdriver(L=280):
    handle = rr(-24, 10, 48, 120, 20)
    shaft = rr(-6, 128, 12, L - 140, 3)
    tip = f"M-6,{L-14}L6,{L-14}L3,{L}L-3,{L}Z"
    return handle + shaft + tip, [(shaft + tip, "metal"), (handle, "handle")]


def hex_key(L=200):
    p = f"M-9,0H9V{L-30}Q9,{L-9} 30,{L-9}H90V{L+9}H30Q-9,{L+9} -9,{L-30}Z"
    return p, [(p, "metal")]


def spoke_key(r=46):
    outer = hexagon(0, r + 10, r, 0)
    notches = "".join(rr(r * math.cos(a) - 6, r + 10 + r * math.sin(a) - 6, 12, 12, 3)
                      for a in [math.pi / 6 + i * math.pi / 3 for i in range(6)])
    hole = circ(0, r + 10, 12)
    return outer, [(outer, "metal"), (notches + hole, "cut")]


def pump(L=420):
    barrel = rr(-22, 60, 44, L - 60, 12)
    rod = rr(-5, 18, 10, 50, 3)
    t = rr(-60, 0, 120, 24, 12)
    foot = rr(-14, L - 4, 28, 26, 6)
    return barrel + rod + t + foot, [(rod, "metal"), (barrel + foot, "dark"), (t, "handle")]


def pliers(L=260):
    a = f"M-8,0Q-40,{L*0.35} -14,{L*0.6}L-4,{L}L6,{L}L4,{L*0.6}Q-6,{L*0.35} 8,0Z"
    b = f"M8,0Q40,{L*0.35} 14,{L*0.6}L4,{L}L-6,{L}L-4,{L*0.6}Q6,{L*0.35} -8,0Z"
    grips = f"M-12,{L*0.0}Q-44,{L*0.3} -20,{L*0.52}L-10,{L*0.52}Q-28,{L*0.3} 0,{L*0.02}Z" \
            f"M12,{L*0.0}Q44,{L*0.3} 20,{L*0.52}L10,{L*0.52}Q28,{L*0.3} 0,{L*0.02}Z"
    pivot = circ(0, L * 0.62, 7)
    return a + b, [(a + b, "metal"), (grips, "handle"), (pivot, "dark")]


def chain_whip(L=330):
    handle = rr(-14, 0, 28, L * 0.62, 10)
    links = "".join(rr(-8 + 10 * math.sin(i * 0.5), L * 0.6 + i * 15, 16, 18, 7) for i in range(9))
    return handle + links, [(handle, "handle"), (links, "dark")]


TOOLS = [spanner, tyre_lever, screwdriver, hex_key, spoke_key, pump, pliers, chain_whip]


def board(w=1600, h=900, seed=3, uid="b", base="#21473b", missing=(2, 5), scale=1.0, label=None):
    rnd = random.Random(seed)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" '
         f'aria-label="Illustration of a painted tool board with tool outlines">',
         f'''<defs>
<filter id="paint-{uid}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="3.2"/></filter>
<filter id="wood-{uid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9 .02" numOctaves="3" seed="9"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .16 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="drop-{uid}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur in="SourceAlpha" stdDeviation="5"/><feOffset dx="6" dy="9"/><feComponentTransfer><feFuncA type="linear" slope=".45"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="metal-{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{METAL[1]}"/><stop offset=".45" stop-color="{METAL[2]}"/><stop offset="1" stop-color="{METAL[0]}"/></linearGradient>
<pattern id="peg-{uid}" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="4.2" fill="#0e211b"/><circle cx="20.8" cy="19.2" r="4.2" fill="none" stroke="#000" stroke-opacity=".25"/></pattern>
</defs>''',
         f'<rect width="{w}" height="{h}" fill="{base}"/>',
         f'<rect width="{w}" height="{h}" fill="#000" filter="url(#wood-{uid})"/>',
         f'<rect width="{w}" height="{h}" fill="url(#peg-{uid})"/>']
    # lay tools out in a row with varied hook heights
    n = len(TOOLS)
    xs = [w * (0.07 + 0.86 * i / (n - 1)) for i in range(n)]
    for i, (tool, x) in enumerate(zip(TOOLS, xs)):
        y = 70 + rnd.uniform(0, 70)
        ang = rnd.uniform(-4, 4)
        outline, parts = tool()
        tr = f'translate({x:.0f} {y:.0f}) rotate({ang:.1f}) scale({scale})'
        o.append(f'<g transform="{tr}">')
        # painted outline: a thick stroke around the tool shape, slightly rough
        o.append(f'<path d="{outline}" fill="{PAINT}" stroke="{PAINT}" stroke-width="14" stroke-linejoin="round" filter="url(#paint-{uid})"/>')
        o.append(f'<path d="{outline}" fill="{base}" opacity=".0"/>')
        if i not in missing:
            o.append(f'<g filter="url(#drop-{uid})">')
            for d, role in parts:
                col = {"metal": f"url(#metal-{uid})", "handle": HANDLE[0], "dark": "#2a2d30", "cut": base}[role]
                o.append(f'<path d="{d}" fill="{col}" fill-rule="evenodd"/>')
            o.append('</g>')
        else:
            # empty slot: the outline shows the board colour inside
            o.append(f'<path d="{outline}" fill="{base}" fill-rule="nonzero" transform="translate(0 0)"/>')
        # hook
        o.append(f'<circle cx="0" cy="-6" r="7" fill="#c9cfd3" stroke="#3a3f43" stroke-width="2"/>')
        o.append('</g>')
    if label:
        o.append(label)
    o.append('</svg>')
    return "".join(o)


if __name__ == "__main__":
    path, w, h = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    open(path, "w").write(board(w, h))
