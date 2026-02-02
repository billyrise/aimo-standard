#!/usr/bin/env python3
"""
Internal link checker for AIMO Standard documentation.

Verifies that:
1. All nav targets in mkdocs.yml exist under docs/<locale>/ for each built locale.
2. No required page is missing (avoids 404s after deploy).

Run as part of CI (quality-gate, release) so that 404s fail the build.

Usage:
    python tooling/checks/check_internal_links.py
    python tooling/checks/check_internal_links.py --check   # Exit 1 if any missing

Exit codes:
    0 - All nav targets exist for all locales
    1 - One or more nav targets missing
    2 - Config error (e.g. mkdocs.yml not found)
"""

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MKDOCS_YML = ROOT / "mkdocs.yml"
DOCS_DIR = ROOT / "docs"


def collect_nav_paths(nav) -> set[str]:
    """Recursively collect all .md paths from mkdocs nav structure."""
    paths = set()
    for item in nav:
        if isinstance(item, dict):
            for _key, value in item.items():
                if isinstance(value, list):
                    paths.update(collect_nav_paths(value))
                elif isinstance(value, str) and value.endswith(".md"):
                    paths.add(value)
        elif isinstance(item, str) and item.endswith(".md"):
            paths.add(item)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check that all nav targets exist under docs/<locale>/"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with code 1 if any target is missing",
    )
    args = parser.parse_args()

    if not MKDOCS_YML.exists():
        print(f"ERROR: {MKDOCS_YML} not found")
        return 2

    config = yaml.safe_load(MKDOCS_YML.read_text(encoding="utf-8"))
    nav = config.get("nav") or []
    required_paths = collect_nav_paths(nav)

    # Locales that are built (from i18n plugin or default en)
    # mkdocs.yml has i18n with folder structure; docs are in docs/en, docs/ja, etc.
    locales = ["en"]
    if "plugins" in config:
        for p in config["plugins"]:
            if isinstance(p, dict) and "i18n" in p:
                locales = [
                    c.get("locale", "en")
                    for c in p["i18n"].get("languages", [])
                    if c.get("build", True)
                ]
                break

    # Ensure en is always checked
    if "en" not in locales:
        locales = ["en"] + list(locales)

    missing: list[tuple[str, str]] = []  # (locale, path)
    for locale in locales:
        base = DOCS_DIR / locale
        if not base.is_dir():
            missing.append((locale, f"<docs dir missing: {base}>"))
            continue
        for path in sorted(required_paths):
            # Nav paths use forward slashes; resolve to locale doc root
            full = base / path
            if not full.exists():
                # Allow index.md for directory (e.g. standard/current/ -> standard/current/index.md)
                alt = base / path.replace(".md", "") / "index.md"
                if not alt.exists():
                    missing.append((locale, path))

    if missing:
        print("ERROR: The following nav targets are missing (would cause 404):")
        for locale, path in sorted(missing):
            print(f"  [{locale}] {path}")
        print()
        print("Fix: Create the missing file under docs/<locale>/ or fix nav in mkdocs.yml")
        if args.check:
            return 1
    else:
        print("OK: All nav targets exist for all built locales.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
