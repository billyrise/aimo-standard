#!/usr/bin/env python3
"""
Lint check for legacy taxonomy CSV files.

Ensures that legacy CSV files do not contain new language columns
(e.g., label_es, definition_de, dimension_name_ko).

This check prevents "column explosion" when adding new languages.
New languages should use per-language artifacts in artifacts/taxonomy/.

Usage:
    python tooling/checks/lint_legacy_csv.py

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
"""

import csv
import re
import sys
from pathlib import Path
from typing import List

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LEGACY_DIR = REPO_ROOT / "source_pack" / "03_taxonomy" / "legacy"

# Allowed columns in legacy CSV (frozen at 21 columns)
ALLOWED_COLUMNS = {
    "standard_id",
    "standard_version",
    "dimension_id",
    "dimension_name_en",
    "dimension_name_ja",
    "code",
    "label_en",
    "label_ja",
    "definition_en",
    "definition_ja",
    "scope_notes",
    "examples",
    "status",
    "introduced_in",
    "deprecated_in",
    "removed_in",
    "replaced_by",
    "backward_compatible",
    "references",
    "owner",
    "last_reviewed_date",
}

# Allowed language suffixes (frozen at en, ja)
ALLOWED_LANG_SUFFIXES = {"en", "ja"}

# Pattern to detect language-specific columns
LANG_COLUMN_PATTERN = re.compile(
    r"^(dimension_name|label|definition)_([a-z]{2,}(?:-[A-Za-z]+)?)$"
)


def check_csv_columns(path: Path, errors: List[str]) -> None:
    """Check CSV file for forbidden columns."""
    if not path.exists():
        # Skip if file doesn't exist (might be OK if not yet generated)
        return

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            errors.append(f"{path.name}: Empty CSV file")
            return

    forbidden = []
    for col in headers:
        # Check if column is in allowed list
        if col in ALLOWED_COLUMNS:
            continue

        # Check if it's a language-specific column
        match = LANG_COLUMN_PATTERN.match(col)
        if match:
            lang_suffix = match.group(2)
            if lang_suffix not in ALLOWED_LANG_SUFFIXES:
                forbidden.append(col)
        else:
            # Unknown column - might be OK, just warn
            pass

    if forbidden:
        errors.append(
            f"{path.name}: Found forbidden language columns: {', '.join(sorted(forbidden))}\n"
            f"    Legacy CSV is frozen at en/ja columns only.\n"
            f"    For new languages, use: artifacts/taxonomy/{{version}}/{{lang}}/taxonomy_dictionary.csv"
        )


def main() -> int:
    errors: List[str] = []

    # Check legacy directory exists
    if not LEGACY_DIR.exists():
        print(f"WARNING: Legacy directory not found: {LEGACY_DIR.relative_to(REPO_ROOT)}")
        print("legacy CSV lint skipped (no legacy files)")
        return 0

    # Check all CSV files in legacy directory
    csv_files = list(LEGACY_DIR.glob("*.csv"))
    if not csv_files:
        print("legacy CSV lint skipped (no CSV files in legacy/)")
        return 0

    for csv_path in csv_files:
        check_csv_columns(csv_path, errors)

    if errors:
        print("ERROR: legacy CSV lint failed:")
        for err in errors:
            print(f"  {err}")
        return 1

    print(f"legacy CSV lint OK ({len(csv_files)} files checked, columns frozen at en/ja)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
