"""Search Wikimedia Commons and download a file with its license metadata.

    python3 commons.py search "query"
    python3 commons.py get "File:Name.jpg" out.jpg [width]

Uses a generic user agent. Prints title, size, license, author and source page.
"""
import json, re, sys, time, urllib.error, urllib.parse, urllib.request

UA = {"User-Agent": "design-demo-builder/1.0 (image credit lookup)"}
API = "https://commons.wikimedia.org/w/api.php?"


def fetch(url, tries=5):
    """GET with backoff on 429/5xx, as the Wikimedia API asks."""
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503) or i == tries - 1:
                raise
            time.sleep(int(e.headers.get("Retry-After") or 0) or 5 * 2 ** i)


def call(params):
    return json.loads(fetch(API + urllib.parse.urlencode(params)))


def clean(v):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", v or "")).strip()


def info(pages):
    for p in pages:
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        yield {
            "title": p["title"], "w": ii["width"], "h": ii["height"],
            "license": clean(m.get("LicenseShortName", {}).get("value")),
            "license_url": clean(m.get("LicenseUrl", {}).get("value")),
            "artist": clean(m.get("Artist", {}).get("value"))[:80],
            "page": ii.get("descriptionurl"), "thumb": ii.get("thumburl"), "original": ii.get("url"),
        }


def search(q, n=10):
    d = call({"action": "query", "generator": "search", "gsrsearch": q, "gsrnamespace": 6, "gsrlimit": n,
              "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": 1600, "format": "json"})
    return list(info(d.get("query", {}).get("pages", {}).values()))


def get(title, out, width=1600):
    d = call({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|extmetadata|size",
              "iiurlwidth": width, "format": "json"})
    meta = next(info(d["query"]["pages"].values()))
    # Originals come from upload.wikimedia.org; resize locally to the requested width.
    import io
    from PIL import Image
    im = Image.open(io.BytesIO(fetch(meta["original"]))).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return meta


def original_url(title):
    """Commons stores originals at a path derived from the MD5 of the file name."""
    import hashlib
    name = title.removeprefix("File:").replace(" ", "_")
    h = hashlib.md5(name.encode()).hexdigest()
    return f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{urllib.parse.quote(name)}"


def download(title, out, width=1600):
    """Fetch the original straight from upload.wikimedia.org (no API call) and resize."""
    import io
    from PIL import Image
    im = Image.open(io.BytesIO(fetch(original_url(title)))).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return im.size


if __name__ == "__main__":
    if sys.argv[1] == "download":
        print(download(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 1600))
    elif sys.argv[1] == "search":
        for r in search(sys.argv[2]):
            print(f'{r["title"][:72]} | {r["w"]}x{r["h"]} | {r["license"]} | {r["artist"][:40]}')
    else:
        print(json.dumps(get(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 1600), indent=1))
