#!/usr/bin/env python3
"""Check generated site for broken internal links (no index.md, no missing targets)."""
import os
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site"))
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ("href", "src") and v and "{{" not in v:
                self.links.append(v)


def resolve(page_path, href):
    u = urlparse(href)
    if u.scheme in SKIP_SCHEMES or href.startswith("#") or href.startswith("//"):
        return None
    path = u.path or href
    if "index.md" in path:
        return ("INDEX_MD", None)
    page_abs = os.path.abspath(page_path)
    base = os.path.dirname(page_abs)
    if path.startswith("/"):
        # Skip theme-generated locale switcher links (default locale may be at root, not /en/)
        first = path.strip("/").split("/")[0]
        if first in ("en", "ja", "zh", "zh-TW", "de", "es", "fr", "pt", "it", "ko"):
            cand = os.path.join(SITE_DIR, path.lstrip("/"))
            if not os.path.exists(cand) and not os.path.exists(os.path.join(cand, "index.html")):
                return None  # treat as optional locale link
        target = os.path.join(SITE_DIR, path.lstrip("/"))
    else:
        # Resolve relative to page directory so normpath does not escape SITE_DIR
        target = os.path.normpath(os.path.join(base, path))
    if not target.startswith(SITE_DIR):
        return None
    if target.endswith("/"):
        target = os.path.join(target, "index.html")
    else:
        if not os.path.splitext(target)[1]:
            cand = os.path.join(target, "index.html")
            if os.path.exists(cand):
                target = cand
    return ("OK", target)


def main():
    if not os.path.isdir(SITE_DIR):
        print("[FATAL] site/ not found. Run mkdocs build first.", file=sys.stderr)
        sys.exit(2)
    broken = []
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            page = os.path.join(root, fn)
            try:
                with open(page, "r", encoding="utf-8", errors="ignore") as f:
                    html = f.read()
                p = LinkParser()
                p.feed(html)
                for href in p.links:
                    result = resolve(page, href)
                    if result is None:
                        continue
                    status, tgt = result
                    if status == "INDEX_MD":
                        broken.append((page, href, "contains index.md"))
                        continue
                    if not os.path.exists(tgt):
                        broken.append((page, href, f"missing -> {tgt}"))
            except Exception:
                pass
    if broken:
        print("[BROKEN LINKS FOUND]")
        for page, href, why in broken[:250]:
            print(f"  {page}: {href} ({why})")
        if len(broken) > 250:
            print(f"  ... and {len(broken) - 250} more")
        sys.exit(1)
    print("[OK] No broken internal links detected in site/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
