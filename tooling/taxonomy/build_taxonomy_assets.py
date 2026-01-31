#!/usr/bin/env python3
"""
Build taxonomy assets from the SSOT CSV.

Generates the following derived files from taxonomy_dictionary_v0.1.csv:
- taxonomy_en.yaml: English taxonomy with codes by dimension
- taxonomy_ja.yaml: Japanese taxonomy with codes by dimension
- code_system.csv: Dimension namespaces and prefixes
- dimensions_en_ja.md: Dimension mapping table (EN/JA)
- taxonomy_dictionary.json: Machine-readable dictionary (aimo-dictionary.schema.json)

Usage:
    python tooling/taxonomy/build_taxonomy_assets.py          # Generate files
    python tooling/taxonomy/build_taxonomy_assets.py --check  # Check if regeneration needed

Exit codes:
    0 - Success (or no changes needed in --check mode)
    1 - Error or changes detected in --check mode
"""

import argparse
import csv
import hashlib
import json
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path
from typing import Any

# Try to import yaml, fallback to simple output if not available
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TAXONOMY_DIR = REPO_ROOT / "source_pack" / "03_taxonomy"
# Note: CSV has been moved to legacy/ directory as part of SSOT migration
# This script is deprecated - use build_artifacts.py instead
DICTIONARY_PATH = TAXONOMY_DIR / "legacy" / "taxonomy_dictionary_v0.1.csv"

# Output paths
OUTPUT_FILES = {
    "taxonomy_en": TAXONOMY_DIR / "taxonomy_en.yaml",
    "taxonomy_ja": TAXONOMY_DIR / "taxonomy_ja.yaml",
    "code_system": TAXONOMY_DIR / "code_system.csv",
    "dimensions_en_ja": TAXONOMY_DIR / "dimensions_en_ja.md",
    "taxonomy_dictionary": TAXONOMY_DIR / "taxonomy_dictionary.json",
}


def read_dictionary() -> list[dict[str, str]]:
    """Read the taxonomy dictionary CSV."""
    with open(DICTIONARY_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def extract_dimensions(rows: list[dict[str, str]]) -> OrderedDict[str, dict[str, Any]]:
    """Extract unique dimensions with their metadata and codes."""
    dimensions: OrderedDict[str, dict[str, Any]] = OrderedDict()

    for row in rows:
        dim_id = row["dimension_id"]
        if dim_id not in dimensions:
            dimensions[dim_id] = {
                "dimension_id": dim_id,
                "name_en": row["dimension_name_en"],
                "name_ja": row["dimension_name_ja"],
                "codes": [],
            }

        # Add code to dimension
        code_entry = {
            "code": row["code"],
            "label_en": row["label_en"],
            "label_ja": row["label_ja"],
            "definition_en": row["definition_en"],
            "definition_ja": row["definition_ja"],
            "status": row["status"],
            "introduced_in": row["introduced_in"],
            "deprecated_in": row.get("deprecated_in", ""),
            "removed_in": row.get("removed_in", ""),
            "replaced_by": row.get("replaced_by", ""),
        }
        dimensions[dim_id]["codes"].append(code_entry)

    return dimensions


def generate_taxonomy_yaml_en(dimensions: OrderedDict[str, dict[str, Any]]) -> str:
    """Generate English taxonomy YAML content."""
    lines = [
        "# AIMO Taxonomy (English)",
        "# Generated from: taxonomy_dictionary_v0.1.csv",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_taxonomy_assets.py",
        "",
        f'version: "0.1.0"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim_id, dim_data in dimensions.items():
        lines.append(f"  - id: {dim_id}")
        lines.append(f'    name: "{dim_data["name_en"]}"')
        lines.append("    codes:")

        for code in dim_data["codes"]:
            lines.append(f"      - code: {code['code']}")
            # Escape quotes in label and definition
            label = code["label_en"].replace('"', '\\"')
            definition = code["definition_en"].replace('"', '\\"')
            lines.append(f'        label: "{label}"')
            lines.append(f'        definition: "{definition}"')
            lines.append(f'        status: {code["status"]}')
            lines.append(f'        introduced_in: "{code["introduced_in"]}"')
            if code["deprecated_in"]:
                lines.append(f'        deprecated_in: "{code["deprecated_in"]}"')
            if code["removed_in"]:
                lines.append(f'        removed_in: "{code["removed_in"]}"')
            if code["replaced_by"]:
                lines.append(f'        replaced_by: "{code["replaced_by"]}"')

    lines.append("")
    return "\n".join(lines)


def generate_taxonomy_yaml_ja(dimensions: OrderedDict[str, dict[str, Any]]) -> str:
    """Generate Japanese taxonomy YAML content."""
    lines = [
        "# AIMO Taxonomy (日本語)",
        "# Generated from: taxonomy_dictionary_v0.1.csv",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_taxonomy_assets.py",
        "",
        f'version: "0.1.0"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim_id, dim_data in dimensions.items():
        lines.append(f"  - id: {dim_id}")
        lines.append(f'    name: "{dim_data["name_ja"]}"')
        lines.append("    codes:")

        for code in dim_data["codes"]:
            lines.append(f"      - code: {code['code']}")
            # Escape quotes in label and definition
            label = code["label_ja"].replace('"', '\\"')
            definition = code["definition_ja"].replace('"', '\\"')
            lines.append(f'        label: "{label}"')
            lines.append(f'        definition: "{definition}"')
            lines.append(f'        status: {code["status"]}')
            lines.append(f'        introduced_in: "{code["introduced_in"]}"')
            if code["deprecated_in"]:
                lines.append(f'        deprecated_in: "{code["deprecated_in"]}"')
            if code["removed_in"]:
                lines.append(f'        removed_in: "{code["removed_in"]}"')
            if code["replaced_by"]:
                lines.append(f'        replaced_by: "{code["replaced_by"]}"')

    lines.append("")
    return "\n".join(lines)


def generate_code_system_csv(dimensions: OrderedDict[str, dict[str, Any]]) -> str:
    """Generate code_system.csv content."""
    lines = [
        "# Code System Namespaces",
        "# Generated from: taxonomy_dictionary_v0.1.csv",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_taxonomy_assets.py",
        "dimension_id,dimension_name_en,dimension_name_ja,namespace_prefix,code_count,notes",
    ]

    for dim_id, dim_data in dimensions.items():
        name_en = dim_data["name_en"]
        name_ja = dim_data["name_ja"]
        prefix = f"{dim_id}-"
        code_count = len(dim_data["codes"])
        notes = f"{code_count} codes defined"
        lines.append(f'{dim_id},"{name_en}","{name_ja}",{prefix},{code_count},"{notes}"')

    lines.append("")
    return "\n".join(lines)


def generate_dimensions_md(dimensions: OrderedDict[str, dict[str, Any]]) -> str:
    """Generate dimensions_en_ja.md content."""
    lines = [
        "# Dimension Names EN/JA Mapping",
        "",
        "**Status**: Generated from taxonomy_dictionary_v0.1.csv",
        "**DO NOT EDIT MANUALLY** - regenerate with: `python tooling/taxonomy/build_taxonomy_assets.py`",
        "",
        "---",
        "",
        "## Dimension Definitions",
        "",
        "| ID | Name (EN) | Name (JA) | Code Count | Prefix |",
        "| --- | --- | --- | --- | --- |",
    ]

    for dim_id, dim_data in dimensions.items():
        name_en = dim_data["name_en"]
        name_ja = dim_data["name_ja"]
        code_count = len(dim_data["codes"])
        prefix = f"`{dim_id}-`"
        lines.append(f"| **{dim_id}** | {name_en} | {name_ja} | {code_count} | {prefix} |")

    lines.extend([
        "",
        "---",
        "",
        "## Code Summary by Dimension",
        "",
    ])

    for dim_id, dim_data in dimensions.items():
        lines.append(f"### {dim_id}: {dim_data['name_en']} / {dim_data['name_ja']}")
        lines.append("")
        lines.append("| Code | Label (EN) | Label (JA) | Status |")
        lines.append("| --- | --- | --- | --- |")

        for code in dim_data["codes"]:
            code_id = code["code"]
            label_en = code["label_en"]
            label_ja = code["label_ja"]
            status = code["status"]
            lines.append(f"| {code_id} | {label_en} | {label_ja} | {status} |")

        lines.append("")

    lines.extend([
        "---",
        "",
        "## Generation Info",
        "",
        f"- **Source**: `source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv`",
        f"- **Generated**: {date.today().isoformat()}",
        f"- **Total Codes**: {sum(len(d['codes']) for d in dimensions.values())}",
        "",
    ])

    return "\n".join(lines)


def generate_taxonomy_dictionary_json(rows: list[dict[str, str]]) -> str:
    """Generate taxonomy_dictionary.json content conforming to aimo-dictionary.schema.json."""
    entries = []

    for row in rows:
        entry: dict[str, Any] = {
            "dimension_id": row["dimension_id"],
            "code": row["code"],
            "label_en": row["label_en"],
            "label_ja": row["label_ja"],
            "definition_en": row["definition_en"],
            "definition_ja": row["definition_ja"],
            "status": row["status"],
            "introduced_in": row["introduced_in"],
            "backward_compatible": row.get("backward_compatible", "").lower() == "true",
        }

        # Only include optional fields if they have values
        if row.get("deprecated_in"):
            entry["deprecated_in"] = row["deprecated_in"]
        if row.get("replaced_by"):
            entry["replaced_by"] = row["replaced_by"]

        entries.append(entry)

    dictionary = {
        "taxonomy_version": "0.1.0",
        "entries": entries,
    }

    return json.dumps(dictionary, ensure_ascii=False, indent=2) + "\n"


def compute_content_hash(content: str) -> str:
    """Compute SHA-256 hash of content (excluding date lines for comparison)."""
    # Remove generated_date and Generated lines for stable comparison
    lines = []
    for line in content.splitlines():
        if "generated_date:" in line.lower():
            continue
        if "**generated**:" in line.lower():
            continue
        if "- **generated**:" in line.lower():
            continue
        lines.append(line)
    stable_content = "\n".join(lines)
    return hashlib.sha256(stable_content.encode("utf-8")).hexdigest()


def files_match(new_content: str, existing_path: Path) -> bool:
    """Check if new content matches existing file (ignoring date changes)."""
    if not existing_path.exists():
        return False

    existing_content = existing_path.read_text(encoding="utf-8")
    return compute_content_hash(new_content) == compute_content_hash(existing_content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build taxonomy assets from SSOT CSV")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if regeneration is needed (no file writes)",
    )
    args = parser.parse_args()

    # Verify source exists
    if not DICTIONARY_PATH.exists():
        print(f"ERROR: Dictionary not found: {DICTIONARY_PATH.relative_to(REPO_ROOT)}")
        return 1

    # Read and process dictionary
    print(f"Reading: {DICTIONARY_PATH.relative_to(REPO_ROOT)}")
    rows = read_dictionary()
    dimensions = extract_dimensions(rows)

    print(f"Found {len(dimensions)} dimensions with {len(rows)} total codes")

    # Generate content
    generated = {
        "taxonomy_en": generate_taxonomy_yaml_en(dimensions),
        "taxonomy_ja": generate_taxonomy_yaml_ja(dimensions),
        "code_system": generate_code_system_csv(dimensions),
        "dimensions_en_ja": generate_dimensions_md(dimensions),
        "taxonomy_dictionary": generate_taxonomy_dictionary_json(rows),
    }

    if args.check:
        # Check mode: verify files match
        mismatches = []
        for key, content in generated.items():
            path = OUTPUT_FILES[key]
            if not files_match(content, path):
                mismatches.append(path.name)

        if mismatches:
            print("ERROR: Taxonomy assets need regeneration:")
            for name in mismatches:
                print(f"  - {name}")
            print("\nRun: python tooling/taxonomy/build_taxonomy_assets.py")
            return 1
        else:
            print("taxonomy assets check OK (all files up to date)")
            return 0

    # Write mode: generate files
    for key, content in generated.items():
        path = OUTPUT_FILES[key]
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path.relative_to(REPO_ROOT)}")

    print(f"\nTaxonomy assets generated successfully ({len(generated)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
