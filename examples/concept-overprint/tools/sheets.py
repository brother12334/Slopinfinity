"""Page designs for the Overprint Studio 2027 calendar: two riso inks (fluorescent pink and
medium blue) on off-white paper, A3 portrait (297 x 420). Pink is drawn with multiply so the
overlap prints purple, offset slightly as riso registration is.
"""
import calendar
import math

PAPER, PINK, BLUE = "#f3efe6", "#ff4fa8", "#2f56a6"
FONT = "'Bricolage Grotesque', sans-serif"


def defs(uid):
    return f'''<defs>
<filter id="grain-{uid}" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed="{len(uid) * 7}" result="n"/>
  <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.75" result="mask"/>
  <feComposite in="SourceGraphic" in2="mask" operator="in"/>
</filter>
<filter id="paper-{uid}" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="5"/>
  <feColorMatrix values="0 0 0 0 .45  0 0 0 0 .4  0 0 0 0 .3  0 0 0 .08 0"/>
  <feComposite in2="SourceGraphic" operator="in"/>
</filter>
</defs>'''


def shape(kind, rnd_seed):
    """Pink shapes; all in the 297 x 420 sheet, upper area."""
    s = {
        "sun": '<circle cx="190" cy="150" r="92"/>',
        "half": '<path d="M40 240 A110 110 0 0 1 260 240 Z"/>',
        "arch": '<path d="M70 268 V160 A80 80 0 0 1 230 160 V268 Z"/>',
        "quarter": '<path d="M297 40 V250 A210 210 0 0 1 87 40 Z"/>',
        "twins": '<circle cx="110" cy="140" r="62"/><circle cx="200" cy="200" r="62"/>',
        "stripes": "".join(f'<rect x="30" y="{60 + i*44}" width="237" height="22"/>' for i in range(5)),
        "ring": '<path fill-rule="evenodd" d="M148 56 a95 95 0 1 0 .1 0Z M148 106 a45 45 0 1 0 .1 0Z"/>',
        "diamond": '<path d="M148 36 L258 150 L148 264 L38 150 Z"/>',
        "waves": "".join(f'<path d="M20 {70+i*40} q32 -26 64 0 t64 0 t64 0 t64 0 v18 q-32 -26 -64 0 t-64 0 t-64 0 t-64 0 Z"/>' for i in range(5)),
        "drop": '<path d="M150 36 C200 116 232 158 232 192 A82 82 0 0 1 68 192 C68 158 100 116 150 36 Z"/>',
        "steps": '<path d="M30 268 V214 H90 V160 H150 V106 H210 V52 H267 V268 Z"/>',
        "moon": '<path fill-rule="evenodd" d="M150 50 a100 100 0 1 0 .1 0Z M200 30 a95 95 0 1 0 .1 0Z"/>',
    }
    return s[kind]


MONTH_SHAPES = ["sun", "stripes", "arch", "twins", "diamond", "half", "waves", "quarter", "ring", "drop", "steps", "moon"]
NUM_POS = [(20, 238), (30, 250), (24, 250), (40, 232), (28, 244), (36, 250), (22, 250), (24, 236), (40, 250), (24, 250), (36, 246), (24, 250)]


def date_grid(year, month, uid, x0=24, y0=298, w=249):
    cw = w / 7
    out = [f'<text x="{x0}" y="{y0}" font-family="{FONT}" font-weight="800" font-size="15" fill="{BLUE}" filter="url(#grain-{uid})">{calendar.month_name[month]}</text>']
    for i, d in enumerate("MTWTFSS"):
        out.append(f'<text x="{x0 + i*cw + cw/2:.1f}" y="{y0+20}" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="6.5" fill="{PINK if i > 4 else BLUE}">{d}</text>')
    for r, week in enumerate(calendar.Calendar(0).monthdayscalendar(year, month)):
        for c, day in enumerate(week):
            if day:
                out.append(f'<text x="{x0 + c*cw + cw/2:.1f}" y="{y0 + 34 + r*12.5:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="600" font-size="8.5" fill="{PINK if c > 4 else BLUE}">{day}</text>')
    return "".join(out)


def sheet(month, year=2027, uid=None):
    uid = uid or f"m{month}"
    nx, ny = NUM_POS[month - 1]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 297 420" role="img" '
            f'aria-label="{calendar.month_name[month]} {year} page: a large blue {month:02d} overprinted with a pink shape, and the month\'s dates">'
            f'{defs(uid)}<rect width="297" height="420" fill="{PAPER}"/><rect width="297" height="420" fill="#000" filter="url(#paper-{uid})"/>'
            f'<g fill="{BLUE}" filter="url(#grain-{uid})"><text x="{nx}" y="{ny}" font-family="{FONT}" font-weight="800" font-size="178" letter-spacing="-8">{month:02d}</text></g>'
            f'<g fill="{PINK}" style="mix-blend-mode:multiply" transform="translate(1.4 -.9)" filter="url(#grain-{uid})">{shape(MONTH_SHAPES[month-1], month)}</g>'
            f'{date_grid(year, month, uid)}'
            f'<text x="273" y="406" text-anchor="end" font-family="{FONT}" font-weight="600" font-size="6.5" fill="{BLUE}">Overprint Studio · {year}</text>'
            f'</svg>')


def cover(year=2027, uid="cover"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 297 420" role="img" aria-label="Cover: 2027 in large blue numerals under a pink circle">'
            f'{defs(uid)}<rect width="297" height="420" fill="{PAPER}"/><rect width="297" height="420" fill="#000" filter="url(#paper-{uid})"/>'
            f'<g fill="{BLUE}" filter="url(#grain-{uid})"><text x="18" y="250" font-family="{FONT}" font-weight="800" font-size="104" letter-spacing="-5">20</text>'
            f'<text x="18" y="346" font-family="{FONT}" font-weight="800" font-size="104" letter-spacing="-5">27</text></g>'
            f'<g fill="{PINK}" style="mix-blend-mode:multiply" transform="translate(1.4 -.9)" filter="url(#grain-{uid})"><circle cx="196" cy="168" r="84"/></g>'
            f'<g fill="{BLUE}" font-family="{FONT}"><text x="24" y="44" font-weight="800" font-size="13">Overprint Studio</text>'
            f'<text x="24" y="60" font-weight="600" font-size="8.5">A calendar in two inks</text>'
            f'<text x="24" y="398" font-weight="600" font-size="8.5" fill="{PINK}">Fluorescent pink + medium blue</text></g></svg>')
