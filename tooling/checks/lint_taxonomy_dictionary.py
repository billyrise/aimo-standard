#!/usr/bin/env python3
"""
Lint check for taxonomy_dictionary_v0.1.csv.

Validates the Taxonomy Dictionary SSOT for structural consistency, required fields,
uniqueness constraints, and semantic validity.

Usage:
    python tooling/checks/lint_taxonomy_dictionary.py

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
"""

import csv
import re
import sys
from pathlib import Path
from typing import List, Tuple

# Ensure we run from repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
# Note: CSV has been moved to legacy/ directory as part of SSOT migration
DICTIONARY_PATH = REPO_ROOT / "source_pack" / "03_taxonomy" / "legacy" / "taxonomy_dictionary_v0.1.csv"

# Expected column count and headers
EXPECTED_COLUMNS = 21
EXPECTED_HEADERS = [
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
]

# Required fields (must not be empty)
REQUIRED_FIELDS = [
    "standard_id",
    "standard_version",
    "dimension_id",
    "code",
    "label_en",
    "label_ja",
    "definition_en",
    "definition_ja",
    "status",
    "introduced_in",
    "backward_compatible",
]

# Valid dimension IDs (LG = Log/Event Type; EV reserved for Evidence artifact IDs only)
VALID_DIMENSIONS = {"FS", "UC", "DT", "CH", "IM", "RS", "OB", "LG"}

# Valid status values
VALID_STATUSES = {"active", "deprecated", "removed"}

# Code pattern: <DIM>-<NNN>
CODE_PATTERN = re.compile(r"^([A-Z]{2})-(\d{3})$")

# SemVer pattern
SEMVER_PATTERN = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse_semver(version: str) -> Tuple[int, int, int]:
    """Parse a SemVer string into a tuple (major, minor, patch)."""
    match = SEMVER_PATTERN.match(version)
    if not match:
        raise ValueError(f"Invalid SemVer: {version}")
    return (int(match.group(1)), int(match.group(2)), int(match.group(3)))


def compare_semver(v1: str, v2: str) -> int:
    """Compare two SemVer strings. Returns -1 if v1 < v2, 0 if equal, 1 if v1 > v2."""
    t1 = parse_semver(v1)
    t2 = parse_semver(v2)
    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    return 0


def main() -> int:
    errors: List[str] = []
    warnings: List[str] = []

    # Check 1: File exists
    if not DICTIONARY_PATH.exists():
        print(f"ERROR: {DICTIONARY_PATH.relative_to(REPO_ROOT)} does not exist")
        return 1

    # Read CSV
    with open(DICTIONARY_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    # Check 2: Column count
    if len(headers) != EXPECTED_COLUMNS:
        errors.append(
            f"Column count mismatch: expected {EXPECTED_COLUMNS}, got {len(headers)}"
        )

    # Check 3: Header names match
    for i, expected in enumerate(EXPECTED_HEADERS):
        if i < len(headers):
            if headers[i] != expected:
                errors.append(
                    f"Header mismatch at column {i+1}: expected '{expected}', got '{headers[i]}'"
                )
        else:
            errors.append(f"Missing header at column {i+1}: expected '{expected}'")

    if errors:
        # Stop early if headers are wrong
        print("ERROR: taxonomy_dictionary lint failed (header issues):")
        for err in errors:
            print(f"  {err}")
        return 1

    # Track uniqueness
    seen_codes: dict[str, int] = {}  # code -> row number
    seen_dim_code_pairs: dict[Tuple[str, str], int] = {}

    # Check each row
    for row_num, row in enumerate(rows, start=2):  # row 1 is header
        # Check 4: Required fields
        for field in REQUIRED_FIELDS:
            value = row.get(field, "").strip()
            if not value:
                errors.append(f"Row {row_num}: Missing required field '{field}'")

        code = row.get("code", "").strip()
        dimension_id = row.get("dimension_id", "").strip()
        status = row.get("status", "").strip()
        standard_version = row.get("standard_version", "").strip()
        introduced_in = row.get("introduced_in", "").strip()
        deprecated_in = row.get("deprecated_in", "").strip()
        removed_in = row.get("removed_in", "").strip()
        backward_compatible = row.get("backward_compatible", "").strip()

        # Check 5: (dimension_id, code) uniqueness
        key = (dimension_id, code)
        if key in seen_dim_code_pairs:
            errors.append(
                f"Row {row_num}: Duplicate (dimension_id, code) pair: {key} "
                f"(first seen at row {seen_dim_code_pairs[key]})"
            )
        else:
            seen_dim_code_pairs[key] = row_num

        # Also check code-only uniqueness
        if code in seen_codes:
            errors.append(
                f"Row {row_num}: Duplicate code '{code}' "
                f"(first seen at row {seen_codes[code]})"
            )
        else:
            seen_codes[code] = row_num

        # Check 6: Valid dimension_id
        if dimension_id and dimension_id not in VALID_DIMENSIONS:
            errors.append(
                f"Row {row_num}: Invalid dimension_id '{dimension_id}'. "
                f"Valid values: {sorted(VALID_DIMENSIONS)}"
            )

        # Check 7: Code format
        if code:
            match = CODE_PATTERN.match(code)
            if not match:
                errors.append(
                    f"Row {row_num}: Invalid code format '{code}'. "
                    f"Expected pattern: <DIM>-<NNN>"
                )
            else:
                code_dim = match.group(1)
                if code_dim != dimension_id:
                    errors.append(
                        f"Row {row_num}: Code prefix '{code_dim}' doesn't match "
                        f"dimension_id '{dimension_id}'"
                    )

        # Check 8: Valid status
        if status and status not in VALID_STATUSES:
            errors.append(
                f"Row {row_num}: Invalid status '{status}'. "
                f"Valid values: {sorted(VALID_STATUSES)}"
            )

        # Check 9: introduced_in <= standard_version (SemVer comparison)
        if introduced_in and standard_version:
            try:
                if compare_semver(introduced_in, standard_version) > 0:
                    errors.append(
                        f"Row {row_num}: introduced_in ({introduced_in}) > "
                        f"standard_version ({standard_version})"
                    )
            except ValueError as e:
                errors.append(f"Row {row_num}: {e}")

        # Check 10: deprecated_in requires status=deprecated
        if deprecated_in and status != "deprecated":
            errors.append(
                f"Row {row_num}: deprecated_in is set but status is '{status}' "
                f"(expected 'deprecated')"
            )

        # Check 11: removed_in requires status=removed
        if removed_in and status != "removed":
            errors.append(
                f"Row {row_num}: removed_in is set but status is '{status}' "
                f"(expected 'removed')"
            )

        # Check 12: backward_compatible is boolean-interpretable
        if backward_compatible:
            bc_lower = backward_compatible.lower()
            if bc_lower not in {"true", "false", "1", "0", "yes", "no"}:
                errors.append(
                    f"Row {row_num}: backward_compatible '{backward_compatible}' "
                    f"is not a valid boolean (expected true/false)"
                )

    # Report results
    if errors:
        print("ERROR: taxonomy_dictionary lint failed:")
        for err in errors:
            print(f"  {err}")
        return 1

    if warnings:
        print("WARNING:")
        for warn in warnings:
            print(f"  {warn}")

    print(f"taxonomy_dictionary lint OK ({len(rows)} codes validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
