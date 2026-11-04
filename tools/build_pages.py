"""Build the separate pages (about.html, work.html, ...) from index.html.

index.html is the only file to edit. After changing it, run:

    python3 tools/build_pages.py

Each generated page is a copy of index.html that shows only its own
sections (see the body[data-page] rules in the stylesheet), with its own
title, address and highlighted menu link.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://vanessa-banini.netlify.app/"
PAGES = {
    "about": "About",
    "work": "Work",
    "talks": "Talks",
    "press": "Press",
    "contact": "Contact",
}

src = (ROOT / "index.html").read_text(encoding="utf-8")


def swap(text, old, new):
    if old not in text:
        raise SystemExit(f"build_pages: expected text not found in index.html: {old!r}")
    return text.replace(old, new, 1)


for slug, label in PAGES.items():
    html = src
    html = swap(html, "<title>Vanessa Woenam Banini</title>", f"<title>{label} · Vanessa Woenam Banini</title>")
    html = swap(html, f'<link rel="canonical" href="{SITE}">', f'<link rel="canonical" href="{SITE}{slug}.html">')
    html = swap(html, f'<meta property="og:url" content="{SITE}">', f'<meta property="og:url" content="{SITE}{slug}.html">')
    html = swap(html, "<body>", f'<body data-page="{slug}">')
    html = swap(html, '<a class="plate" href="#top" id="plate">', '<a class="plate" href="./" id="plate">')
    html = swap(html, '<a class="skip" href="#about">', '<a class="skip" href="#main">')
    html = swap(html, "<main>", '<main id="main">')
    html = swap(html, f'<a href="{slug}.html">{label}</a>', f'<a href="{slug}.html" aria-current="page">{label}</a>')
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"wrote {slug}.html")
