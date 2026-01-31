#!/usr/bin/env python3
"""
Migration script: suffix structure (.ja.md) -> folder structure (en/, ja/)

This script moves:
- docs/*.md (not .ja.md) -> docs/en/*.md
- docs/*.ja.md -> docs/ja/*.md (renamed)

Preserves:
- docs/overrides/ (theme overrides, stays at docs root)
- docs/robots.txt (stays at docs root)
"""

import shutil
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
EN_DIR = DOCS / "en"
JA_DIR = DOCS / "ja"

# Directories/files to keep at docs root (not move)
KEEP_AT_ROOT = {"overrides", "robots.txt"}


def migrate(dry_run: bool = False):
    """Migrate from suffix to folder structure."""
    moved_files = []

    # Ensure target dirs exist
    if not dry_run:
        EN_DIR.mkdir(exist_ok=True)
        JA_DIR.mkdir(exist_ok=True)

    # Collect all .md files
    all_md_files = list(DOCS.rglob("*.md"))

    for md_file in all_md_files:
        # Skip files already in en/ or ja/
        rel = md_file.relative_to(DOCS)
        parts = rel.parts
        if parts[0] in ("en", "ja"):
            continue

        # Skip overrides
        if parts[0] in KEEP_AT_ROOT:
            continue

        if md_file.name.endswith(".ja.md"):
            # Japanese file -> ja/
            new_name = md_file.name.replace(".ja.md", ".md")
            dest = JA_DIR / rel.parent / new_name
        else:
            # English file -> en/
            dest = EN_DIR / rel

        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(md_file), str(dest))

        moved_files.append((md_file.relative_to(ROOT), dest.relative_to(ROOT)))

    return moved_files


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    moved = migrate(dry_run=dry_run)

    print(f"{'Would move' if dry_run else 'Moved'} {len(moved)} files:\n")

    # Group by type
    en_files = [(s, d) for s, d in moved if "ja" not in str(d).split("/")[1]]
    ja_files = [(s, d) for s, d in moved if "ja" in str(d).split("/")[1]]

    print(f"English files ({len(en_files)}):")
    for src, dst in sorted(en_files):
        print(f"  {src} -> {dst}")

    print(f"\nJapanese files ({len(ja_files)}):")
    for src, dst in sorted(ja_files):
        print(f"  {src} -> {dst}")

    if not dry_run:
        print("\n✓ Migration complete!")
        print("\nNext steps:")
        print("1. Update mkdocs.yml: docs_structure: folder")
        print("2. Fix internal links in all moved files")
        print("3. Run: mkdocs build --strict")


if __name__ == "__main__":
    main()
