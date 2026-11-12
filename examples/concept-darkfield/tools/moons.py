"""New-moon times (Meeus, Astronomical Algorithms, ch. 49) and the Saturday nearest each.

    python3 tools/moons.py            # prints the session table as JSON
"""
import datetime as dt
import json
import math


def jde_new_moon(k):
    T = k / 1236.85
    jde = (2451550.09766 + 29.530588861 * k + 0.00015437 * T**2
           - 0.000000150 * T**3 + 0.00000000073 * T**4)
    E = 1 - 0.002516 * T - 0.0000074 * T**2
    r = math.radians
    M = r(2.5534 + 29.10535670 * k - 0.0000014 * T**2 - 0.00000011 * T**3)
    Mp = r(201.5643 + 385.81693528 * k + 0.0107582 * T**2 + 0.00001238 * T**3 - 0.000000058 * T**4)
    F = r(160.7108 + 390.67050284 * k - 0.0016118 * T**2 - 0.00000227 * T**3 + 0.000000011 * T**4)
    O = r(124.7746 - 1.56375588 * k + 0.0020672 * T**2 + 0.00000215 * T**3)
    s = math.sin
    corr = (-0.40720 * s(Mp) + 0.17241 * E * s(M) + 0.01608 * s(2 * Mp) + 0.01039 * s(2 * F)
            + 0.00739 * E * s(Mp - M) - 0.00514 * E * s(Mp + M) + 0.00208 * E * E * s(2 * M)
            - 0.00111 * s(Mp - 2 * F) - 0.00057 * s(Mp + 2 * F) + 0.00056 * E * s(2 * Mp + M)
            - 0.00042 * s(3 * Mp) + 0.00042 * E * s(M + 2 * F) + 0.00038 * E * s(M - 2 * F)
            - 0.00024 * E * s(2 * Mp - M) - 0.00017 * s(O) - 0.00007 * s(Mp + 2 * M)
            + 0.00004 * s(2 * Mp - 2 * F) + 0.00004 * s(3 * M) + 0.00003 * s(Mp + M - 2 * F)
            + 0.00003 * s(2 * Mp + 2 * F) - 0.00003 * s(Mp + M + 2 * F) + 0.00003 * s(Mp - M + 2 * F)
            - 0.00002 * s(Mp - M - 2 * F) - 0.00002 * s(3 * Mp + M) + 0.00002 * s(4 * Mp))
    return jde + corr


def jd_to_utc(jd):
    # JDE is Terrestrial Time; TT - UTC is about 69 s in this period, negligible for dates.
    return dt.datetime(2000, 1, 1, 12, tzinfo=dt.timezone.utc) + dt.timedelta(days=jd - 2451545.0)


def nearest_saturday(d):
    # Saturday is weekday 5; choose the closest (ties cannot occur: max distance is 3 days)
    diff = (5 - d.weekday()) % 7
    return d + dt.timedelta(days=diff) if diff <= 3 else d - dt.timedelta(days=7 - diff)


def sessions(start=dt.date(2026, 12, 1), end=dt.date(2027, 11, 30)):
    k0 = math.floor((2026.9 - 2000) * 12.3685)
    out = []
    for k in range(k0 - 2, k0 + 16):
        t = jd_to_utc(jde_new_moon(k))
        if start <= t.date() <= end:
            out.append({"new_moon_utc": t.strftime("%Y-%m-%d %H:%M"),
                        "session": nearest_saturday(t.date()).isoformat()})
    return out


if __name__ == "__main__":
    print(json.dumps(sessions(), indent=1))
