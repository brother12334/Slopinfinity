"""Generate potter's half-section profile drawings as inline SVG.

Each form is a list of (x, y) points for the right-hand outside wall, from the rim down
to the foot, in a 0-100 box with the vertical axis at x=0. The left half is drawn as a
section: the cut wall filled, with the inside line offset by the wall thickness.
"""
import math

FORMS = {
    "cup":      {"pts": [(38, 4), (40, 30), (39, 62), (33, 86), (26, 96), (26, 100)], "wall": 4.5},
    "bowl":     {"pts": [(62, 30), (56, 52), (44, 70), (28, 80), (22, 82), (22, 86)], "wall": 4},
    "tall cup": {"pts": [(30, 0), (31, 40), (30, 76), (26, 94), (22, 96), (22, 100)], "wall": 4},
    "wide bowl":{"pts": [(76, 50), (66, 66), (48, 78), (28, 84), (24, 86), (24, 90)], "wall": 3.5},
}


def smooth(pts):
    """Catmull-Rom through pts, as an SVG path fragment starting with M."""
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def inner(pts, wall):
    """Offset the wall inward (toward the axis and up from the base)."""
    out = []
    for i, (x, y) in enumerate(pts[:-2]):
        a = pts[max(i - 1, 0)]; b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy) or 1
        nx, ny = -dy / n, dx / n          # normal pointing toward the axis
        if nx > 0: nx, ny = -nx, -ny
        out.append((x + nx * wall, y + ny * wall))
    base_y = pts[-1][1] - wall * 2.2
    out.append((out[-1][0] * 0.7, base_y))
    out.append((0, base_y))
    return out


def mirror(pts):
    return [(-x, y) for x, y in pts]


def svg(name, label=True, cls="profile"):
    f = FORMS[name]
    pts, wall = f["pts"], f["wall"]
    top = min(y for _, y in pts) - 4
    bottom = max(y for _, y in pts) + 4
    width = max(x for x, _ in pts) + 6
    rim = pts[0]
    ins = inner(pts, wall)
    outside_right = smooth(pts) + f" L0,{pts[-1][1]:.1f}"
    left_out = mirror(pts); left_in = mirror(ins)
    section = smooth(left_out) + f" L0,{pts[-1][1]:.1f} L0,{ins[-1][1]:.1f}"
    rev = list(reversed(left_in))
    section += " " + smooth(rev).replace("M", "L", 1) + " Z"
    h = bottom - top
    lab = (f'<text x="0" y="{bottom + 9:.1f}" text-anchor="middle" class="lab">{name}</text>' if label else "")
    return (
        f'<svg class="{cls}" style="--w:{2 * width:.0f}" viewBox="{-width:.1f} {top:.1f} {2 * width:.1f} {h + (14 if label else 0):.1f}" '
        f'role="img" aria-label="Profile drawing of a {name}">'
        f'<line x1="0" y1="{top:.1f}" x2="0" y2="{bottom - 2:.1f}" class="axis"/>'
        f'<path d="{section}" class="cut"/>'
        f'<path d="{outside_right}" class="line"/>'
        f'<line x1="{-rim[0]:.1f}" y1="{rim[1]:.1f}" x2="{rim[0]:.1f}" y2="{rim[1]:.1f}" class="rim"/>'
        f'{lab}</svg>'
    )


if __name__ == "__main__":
    import sys
    print(svg(sys.argv[1], label=len(sys.argv) < 3))
