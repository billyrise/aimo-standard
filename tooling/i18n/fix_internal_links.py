#!/usr/bin/env python3
"""
Fix internal links in Japanese files after folder structure migration.

Changes:
- Links like `governance/trust-package.ja.md` -> `governance/trust-package.md`
- Links like `standard/current/03-taxonomy.ja.md` -> `standard/current/03-taxonomy.md`

This is needed because in folder structure, Japanese files are in ja/ folder
and no longer use .ja.md suffix.
"""

import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
JA_DIR = ROOT / "docs" / "ja"

# Pattern to match .ja.md in markdown links
# Matches: [text](path/to/file.ja.md) or [text](path/to/file.ja.md#anchor)
LINK_PATTERN = re.compile(r'(\[[^\]]*\]\([^)]*?)\.ja\.md([#)])')


def fix_links_in_file(filepath: Path, dry_run: bool = False) -> list[tuple[str, str]]:
    """Fix .ja.md links in a file. Returns list of (before, after) changes."""
    content = filepath.read_text(encoding="utf-8")
    changes = []

    def replacer(match):
        before = match.group(0)
        after = f"{match.group(1)}.md{match.group(2)}"
        changes.append((before, after))
        return after

    new_content = LINK_PATTERN.sub(replacer, content)

    if changes and not dry_run:
        filepath.write_text(new_content, encoding="utf-8")

    return changes


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    all_changes = []

    for md_file in JA_DIR.rglob("*.md"):
        changes = fix_links_in_file(md_file, dry_run=dry_run)
        if changes:
            all_changes.append((md_file.relative_to(ROOT), changes))

    if all_changes:
        print(f"{'Would fix' if dry_run else 'Fixed'} links in {len(all_changes)} files:\n")
        for filepath, changes in all_changes:
            print(f"{filepath}:")
            for before, after in changes:
                print(f"  - {before}")
                print(f"  + {after}")
            print()
    else:
        print("No .ja.md links found to fix.")

    if not dry_run and all_changes:
        print("✓ Link fixes complete!")


if __name__ == "__main__":
    main()
