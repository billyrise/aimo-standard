#!/usr/bin/env python3
"""
Update versions/index.md pages with new release information.

This script updates both English and Japanese versions pages:
  - docs/en/standard/versions/index.md
  - docs/ja/standard/versions/index.md

It updates:
  1. The "Current Version" / "現在のバージョン" callout
  2. The Version History table (adds new row at top)
  3. Example version numbers in code blocks

Usage:
  python tooling/release/update_versions_page.py --version 0.1.3 --date 2026-02-01

  # Check mode (no changes, just verify):
  python tooling/release/update_versions_page.py --version 0.1.3 --date 2026-02-01 --check
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

# Ensure we run from repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# File paths
EN_VERSIONS_PATH = REPO_ROOT / "docs/en/standard/versions/index.md"
JA_VERSIONS_PATH = REPO_ROOT / "docs/ja/standard/versions/index.md"

# GitHub repo info
GITHUB_REPO = "billyrise/aimo-standard"
GITHUB_RELEASES_BASE = f"https://github.com/{GITHUB_REPO}/releases"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update versions pages with new release info"
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Version number without 'v' prefix (e.g., 0.1.3)",
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Release date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: verify files would be updated, but don't write",
    )
    return parser.parse_args()


def validate_version(version: str) -> None:
    """Validate version format (X.Y.Z)."""
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        print(f"ERROR: Invalid version format: {version}", file=sys.stderr)
        print("Expected format: X.Y.Z (e.g., 0.1.3)", file=sys.stderr)
        sys.exit(1)


def validate_date(date_str: str) -> None:
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"ERROR: Invalid date format: {date_str}", file=sys.stderr)
        print("Expected format: YYYY-MM-DD (e.g., 2026-02-01)", file=sys.stderr)
        sys.exit(1)


def update_en_versions_page(content: str, version: str, date: str) -> str:
    """Update English versions page content."""
    tag = f"v{version}"
    download_base = f"{GITHUB_RELEASES_BASE}/download/{tag}"

    # 1. Update "Current Version" callout
    current_version_pattern = (
        r'(!!! success "Current Version"\s*\n\s+)\*\*v[\d.]+\*\* \(\d{4}-\d{2}-\d{2}\)'
        r'(.*?\[GitHub Release\]\()https://github\.com/[^/]+/[^/]+/releases/tag/v[\d.]+(\))'
    )
    current_version_replacement = (
        rf'\1**{tag}** ({date})\2{GITHUB_RELEASES_BASE}/tag/{tag}\3'
    )
    content = re.sub(current_version_pattern, current_version_replacement, content)

    # 2. Add new row to Version History table
    # Find the table header and first data row
    table_pattern = (
        r'(\| Version \| Date \| Release Notes \| PDF \(EN\) \| PDF \(JA\) \| Artifacts \| Checksums \|\n'
        r'\| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \|\n)'
    )

    # New row to insert
    changelog_anchor = f"version-{version.replace('.', '')}"
    new_row = (
        f"| **{tag}** | {date} | "
        f"[Changelog](../current/08-changelog.md#{changelog_anchor}) | "
        f"[trust_package.pdf]({download_base}/trust_package.pdf) | "
        f"[trust_package.ja.pdf]({download_base}/trust_package.ja.pdf) | "
        f"[ZIP]({download_base}/aimo-standard-artifacts.zip) | "
        f"[SHA256]({download_base}/SHA256SUMS.txt) |\n"
    )

    # Check if version already exists in table
    if f"| **{tag}**" in content:
        print(f"  Version {tag} already exists in EN table, skipping row insert")
    else:
        content = re.sub(table_pattern, rf"\1{new_row}", content)

    # 3. Update example VERSION in code blocks
    content = re.sub(
        r'VERSION=v[\d.]+',
        f'VERSION={tag}',
        content
    )

    return content


def update_ja_versions_page(content: str, version: str, date: str) -> str:
    """Update Japanese versions page content."""
    tag = f"v{version}"
    download_base = f"{GITHUB_RELEASES_BASE}/download/{tag}"

    # 1. Update "現在のバージョン" callout
    current_version_pattern = (
        r'(!!! success "現在のバージョン"\s*\n\s+)\*\*v[\d.]+\*\* \(\d{4}-\d{2}-\d{2}\)'
        r'(.*?\[GitHub Release\]\()https://github\.com/[^/]+/[^/]+/releases/tag/v[\d.]+(\))'
    )
    current_version_replacement = (
        rf'\1**{tag}** ({date})\2{GITHUB_RELEASES_BASE}/tag/{tag}\3'
    )
    content = re.sub(current_version_pattern, current_version_replacement, content)

    # 2. Add new row to Version History table (Japanese)
    table_pattern = (
        r'(\| バージョン \| 日付 \| リリースノート \| PDF \(EN\) \| PDF \(JA\) \| アーティファクト \| チェックサム \|\n'
        r'\| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \| :[-]+ \|\n)'
    )

    # New row to insert
    changelog_anchor = f"version-{version.replace('.', '')}"
    new_row = (
        f"| **{tag}** | {date} | "
        f"[Changelog](../current/08-changelog.md#{changelog_anchor}) | "
        f"[trust_package.pdf]({download_base}/trust_package.pdf) | "
        f"[trust_package.ja.pdf]({download_base}/trust_package.ja.pdf) | "
        f"[ZIP]({download_base}/aimo-standard-artifacts.zip) | "
        f"[SHA256]({download_base}/SHA256SUMS.txt) |\n"
    )

    # Check if version already exists in table
    if f"| **{tag}**" in content:
        print(f"  Version {tag} already exists in JA table, skipping row insert")
    else:
        content = re.sub(table_pattern, rf"\1{new_row}", content)

    # 3. Update example VERSION in code blocks
    content = re.sub(
        r'VERSION=v[\d.]+',
        f'VERSION={tag}',
        content
    )

    return content


def main() -> None:
    args = parse_args()
    version = args.version
    date = args.date
    check_mode = args.check

    # Validate inputs
    validate_version(version)
    validate_date(date)

    print(f"Updating versions pages for v{version} ({date})")
    if check_mode:
        print("  (check mode - no files will be modified)")

    updated_files = []

    # Update English page
    if EN_VERSIONS_PATH.exists():
        print(f"\nProcessing: {EN_VERSIONS_PATH.relative_to(REPO_ROOT)}")
        original = EN_VERSIONS_PATH.read_text(encoding="utf-8")
        updated = update_en_versions_page(original, version, date)
        if original != updated:
            if not check_mode:
                EN_VERSIONS_PATH.write_text(updated, encoding="utf-8")
            updated_files.append(EN_VERSIONS_PATH)
            print("  ✓ Updated")
        else:
            print("  ○ No changes needed")
    else:
        print(f"WARNING: EN versions page not found: {EN_VERSIONS_PATH}")

    # Update Japanese page
    if JA_VERSIONS_PATH.exists():
        print(f"\nProcessing: {JA_VERSIONS_PATH.relative_to(REPO_ROOT)}")
        original = JA_VERSIONS_PATH.read_text(encoding="utf-8")
        updated = update_ja_versions_page(original, version, date)
        if original != updated:
            if not check_mode:
                JA_VERSIONS_PATH.write_text(updated, encoding="utf-8")
            updated_files.append(JA_VERSIONS_PATH)
            print("  ✓ Updated")
        else:
            print("  ○ No changes needed")
    else:
        print(f"WARNING: JA versions page not found: {JA_VERSIONS_PATH}")

    # Summary
    print(f"\n{'='*50}")
    if updated_files:
        action = "Would update" if check_mode else "Updated"
        print(f"{action} {len(updated_files)} file(s):")
        for f in updated_files:
            print(f"  - {f.relative_to(REPO_ROOT)}")
    else:
        print("No files needed updating.")

    if check_mode and updated_files:
        print("\nRe-run without --check to apply changes.")


if __name__ == "__main__":
    main()
