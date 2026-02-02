#!/usr/bin/env python3
"""
Lint check for source_pack/00_manifest.md.

Ensures the manifest exists and contains required sections as SSOT for content coverage.

Usage:
    python tooling/checks/lint_manifest.py

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
"""

import sys
from pathlib import Path

# Ensure we run from repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST_PATH = REPO_ROOT / "source_pack" / "00_manifest.md"

# Required content markers
REQUIRED_MARKERS = [
    ("SSOT", "Manifest must declare itself as Single Source of Truth"),
    ("How to use this manifest", "Manifest must contain usage instructions"),
    ("Trust Package PDF Contents", "Manifest must document PDF contents"),
]

# Key hub pages that should be referenced
KEY_HUB_PAGES = [
    ("trust-package", "governance/trust-package"),
    ("evidence-bundle", "artifacts/evidence-bundle"),
    ("minimum-evidence", "artifacts/minimum-evidence"),
    ("methodology", "coverage-map/methodology"),
    ("releases", "releases/index"),
]


def main() -> int:
    errors = []

    # Check 1: Manifest file exists
    if not MANIFEST_PATH.exists():
        print(f"ERROR: {MANIFEST_PATH.relative_to(REPO_ROOT)} does not exist")
        print("  Create source_pack/00_manifest.md as the SSOT for content coverage.")
        return 1

    content = MANIFEST_PATH.read_text(encoding="utf-8")

    # Check 2: Required markers
    for marker, description in REQUIRED_MARKERS:
        if marker not in content:
            errors.append(f"Missing required marker: '{marker}'")
            errors.append(f"  -> {description}")

    # Check 3: Key hub page references (warning only, not error)
    warnings = []
    for name, path_fragment in KEY_HUB_PAGES:
        if path_fragment not in content and name not in content.lower():
            warnings.append(f"  - {name} ({path_fragment})")

    # Report results
    if errors:
        print("ERROR: source_pack/00_manifest.md failed validation:")
        for err in errors:
            print(f"  {err}")
        return 1

    if warnings:
        print("WARNING: Manifest may be missing references to key hub pages:")
        for warn in warnings:
            print(warn)
        print("  (This is a warning, not a failure)")

    print("manifest lint OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
