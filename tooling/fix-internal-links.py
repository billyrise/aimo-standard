#!/usr/bin/env python3
"""
Fix internal markdown links in docs/ for MkDocs pretty URLs.
- .../index.md -> .../  (and index.md#anchor -> /#anchor)
- .../foo.md -> .../foo/  (and foo.md#anchor -> foo/#anchor)
Skips links that are http(s), mailto, tel, or point to GitHub.
"""
import os
import re

DOCS = "docs"
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")

def fix_link(match: re.Match) -> str:
    full = match.group(0)
    pre, path_anchor = full[:-1].split("](", 1)  # ](path)
    if any(path_anchor.startswith(p) for p in SKIP_PREFIXES):
        return full
    path = path_anchor
    anchor = ""
    if "#" in path:
        path, anchor = path.split("#", 1)
        anchor = "#" + anchor
    if not path or path.endswith("/"):
        return full
    # index.md -> directory
    if path.endswith("/index.md"):
        base = path.replace("/index.md", "").rstrip("/") or "."
        return f"{pre}]({base}/{anchor})" if base != "." else f"{pre}](./{anchor})"
    if path.strip() == "index.md":
        return f"{pre}](../{anchor})"  # same-dir index: parent dir in URL tree
    # other .md -> pretty URL (trailing slash)
    if path.endswith(".md"):
        base = path[:-3].rstrip("/")
        return f"{pre}]({base}/{anchor})"
    return full

def fix_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    # Match ](something) where something may contain .md or index.md
    pattern = re.compile(r"\]\(([^)]+)\)")
    new_text = pattern.sub(fix_link, text)
    if new_text != text:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new_text)
        return True
    return False

def main():
    changed = 0
    for root, _, files in os.walk(DOCS):
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            if fix_file(path):
                changed += 1
                print(path)
    print(f"Changed {changed} files.")

if __name__ == "__main__":
    main()
