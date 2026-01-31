#!/usr/bin/env python3
"""
Build language-neutral canonical taxonomy and i18n packs from SSOT CSV.

This script generates:
- data/taxonomy/canonical.yaml: Language-neutral structure (codes, status, lifecycle)
- data/taxonomy/i18n/en.yaml: English labels and definitions
- data/taxonomy/i18n/ja.yaml: Japanese labels and definitions
- data/taxonomy/i18n/{lang}.yaml: Template for additional languages

The canonical.yaml is the SSOT for structure; i18n packs provide translations.

Usage:
    python tooling/taxonomy/build_i18n_taxonomy.py          # Generate files
    python tooling/taxonomy/build_i18n_taxonomy.py --check  # Check if up to date
    python tooling/taxonomy/build_i18n_taxonomy.py --add-lang es  # Add empty language pack
"""

import argparse
import csv
import hashlib
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path
from typing import Any

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
# Note: CSV has been moved to legacy/ directory as part of SSOT migration
# This script is deprecated for generation - use build_artifacts.py instead
# Kept for --add-lang functionality only
SOURCE_CSV = REPO_ROOT / "source_pack" / "03_taxonomy" / "legacy" / "taxonomy_dictionary_v0.1.csv"
DATA_DIR = REPO_ROOT / "data" / "taxonomy"
I18N_DIR = DATA_DIR / "i18n"

# Output files
CANONICAL_PATH = DATA_DIR / "canonical.yaml"


def read_dictionary() -> list[dict[str, str]]:
    """Read the taxonomy dictionary CSV."""
    with open(SOURCE_CSV, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def extract_canonical_data(rows: list[dict[str, str]]) -> OrderedDict[str, dict[str, Any]]:
    """Extract language-neutral dimension and code data."""
    dimensions: OrderedDict[str, dict[str, Any]] = OrderedDict()

    for row in rows:
        dim_id = row["dimension_id"]
        if dim_id not in dimensions:
            dimensions[dim_id] = {
                "id": dim_id,
                "codes": [],
            }

        code_entry = {
            "code": row["code"],
            "status": row["status"],
            "introduced_in": row["introduced_in"],
        }

        # Optional fields
        if row.get("deprecated_in"):
            code_entry["deprecated_in"] = row["deprecated_in"]
        if row.get("removed_in"):
            code_entry["removed_in"] = row["removed_in"]
        if row.get("replaced_by"):
            code_entry["replaced_by"] = row["replaced_by"]
        if row.get("backward_compatible"):
            code_entry["backward_compatible"] = row["backward_compatible"].lower() == "true"
        if row.get("scope_notes"):
            code_entry["scope_notes"] = row["scope_notes"]
        if row.get("examples"):
            code_entry["examples"] = row["examples"].split("|")

        dimensions[dim_id]["codes"].append(code_entry)

    return dimensions


def extract_i18n_data(rows: list[dict[str, str]], lang: str) -> dict[str, Any]:
    """Extract labels and definitions for a specific language."""
    name_key = f"dimension_name_{lang}"
    label_key = f"label_{lang}"
    definition_key = f"definition_{lang}"

    dimensions: dict[str, Any] = {}

    for row in rows:
        dim_id = row["dimension_id"]
        if dim_id not in dimensions:
            dimensions[dim_id] = {
                "name": row.get(name_key, ""),
                "codes": {},
            }

        code = row["code"]
        dimensions[dim_id]["codes"][code] = {
            "label": row.get(label_key, ""),
            "definition": row.get(definition_key, ""),
        }

    return dimensions


def generate_canonical_yaml(dimensions: OrderedDict[str, dict[str, Any]]) -> str:
    """Generate canonical.yaml content."""
    lines = [
        "# AIMO Taxonomy - Canonical Structure (Language-neutral)",
        "# Generated from: source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_i18n_taxonomy.py",
        "#",
        "# This file is the SSOT for taxonomy structure (codes, status, lifecycle).",
        "# Labels and definitions are in data/taxonomy/i18n/*.yaml",
        "",
        'version: "0.1.0"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim_id, dim_data in dimensions.items():
        lines.append(f"  - id: {dim_id}")
        lines.append("    codes:")

        for code in dim_data["codes"]:
            lines.append(f"      - code: {code['code']}")
            lines.append(f"        status: {code['status']}")
            lines.append(f'        introduced_in: "{code["introduced_in"]}"')

            if code.get("deprecated_in"):
                lines.append(f'        deprecated_in: "{code["deprecated_in"]}"')
            if code.get("removed_in"):
                lines.append(f'        removed_in: "{code["removed_in"]}"')
            if code.get("replaced_by"):
                lines.append(f'        replaced_by: "{code["replaced_by"]}"')
            if "backward_compatible" in code:
                lines.append(f"        backward_compatible: {str(code['backward_compatible']).lower()}")
            if code.get("scope_notes"):
                notes = code["scope_notes"].replace('"', '\\"')
                lines.append(f'        scope_notes: "{notes}"')
            if code.get("examples"):
                lines.append("        examples:")
                for ex in code["examples"]:
                    lines.append(f'          - "{ex}"')

    lines.append("")
    return "\n".join(lines)


def generate_i18n_yaml(dimensions: dict[str, Any], lang: str, lang_name: str) -> str:
    """Generate i18n YAML content for a language."""
    lines = [
        f"# AIMO Taxonomy - {lang_name} Labels and Definitions",
        "# Generated from: source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_i18n_taxonomy.py",
        "#",
        "# This file provides translations for the canonical taxonomy structure.",
        "# Structure is defined in data/taxonomy/canonical.yaml",
        "",
        f'language: "{lang}"',
        f'language_name: "{lang_name}"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim_id, dim_data in dimensions.items():
        name = dim_data["name"].replace('"', '\\"') if dim_data["name"] else ""
        lines.append(f"  {dim_id}:")
        lines.append(f'    name: "{name}"')
        lines.append("    codes:")

        for code, code_data in dim_data["codes"].items():
            label = code_data["label"].replace('"', '\\"') if code_data["label"] else ""
            definition = code_data["definition"].replace('"', '\\"') if code_data["definition"] else ""
            lines.append(f"      {code}:")
            lines.append(f'        label: "{label}"')
            lines.append(f'        definition: "{definition}"')

    lines.append("")
    return "\n".join(lines)


def generate_empty_i18n_yaml(lang: str, lang_name: str, template_dims: dict[str, Any]) -> str:
    """Generate empty i18n YAML template for a new language."""
    lines = [
        f"# AIMO Taxonomy - {lang_name} Labels and Definitions",
        f"# Template generated for: {lang}",
        "#",
        "# Fill in the translations below. For untranslated items, leave empty",
        "# and the system will fall back to English.",
        "",
        f'language: "{lang}"',
        f'language_name: "{lang_name}"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim_id, dim_data in template_dims.items():
        lines.append(f"  {dim_id}:")
        lines.append(f'    name: ""  # English: {dim_data["name"]}')
        lines.append("    codes:")

        for code, code_data in dim_data["codes"].items():
            en_label = code_data["label"]
            lines.append(f"      {code}:")
            lines.append(f'        label: ""  # English: {en_label}')
            lines.append(f'        definition: ""')

    lines.append("")
    return "\n".join(lines)


def compute_content_hash(content: str) -> str:
    """Compute hash of content (excluding date lines)."""
    lines = [line for line in content.splitlines() if "generated_date:" not in line.lower()]
    stable_content = "\n".join(lines)
    return hashlib.sha256(stable_content.encode("utf-8")).hexdigest()


def files_match(new_content: str, existing_path: Path) -> bool:
    """Check if new content matches existing file."""
    if not existing_path.exists():
        return False
    existing_content = existing_path.read_text(encoding="utf-8")
    return compute_content_hash(new_content) == compute_content_hash(existing_content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build language-neutral taxonomy and i18n packs")
    parser.add_argument("--check", action="store_true", help="Check if regeneration is needed")
    parser.add_argument("--add-lang", metavar="LANG", help="Add empty language pack (e.g., es, de, ko)")
    parser.add_argument("--lang-name", metavar="NAME", help="Language name for --add-lang (e.g., Español)")
    args = parser.parse_args()

    # Verify source exists
    if not SOURCE_CSV.exists():
        print(f"ERROR: Source CSV not found: {SOURCE_CSV.relative_to(REPO_ROOT)}")
        return 1

    # Ensure directories exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    I18N_DIR.mkdir(parents=True, exist_ok=True)

    # Read and process dictionary
    print(f"Reading: {SOURCE_CSV.relative_to(REPO_ROOT)}")
    rows = read_dictionary()
    canonical = extract_canonical_data(rows)
    en_data = extract_i18n_data(rows, "en")
    ja_data = extract_i18n_data(rows, "ja")

    print(f"Found {len(canonical)} dimensions with {len(rows)} total codes")

    # Generate content
    canonical_content = generate_canonical_yaml(canonical)
    en_content = generate_i18n_yaml(en_data, "en", "English")
    ja_content = generate_i18n_yaml(ja_data, "ja", "日本語")

    generated = {
        CANONICAL_PATH: canonical_content,
        I18N_DIR / "en.yaml": en_content,
        I18N_DIR / "ja.yaml": ja_content,
    }

    # Handle --add-lang
    if args.add_lang:
        lang = args.add_lang
        lang_name = args.lang_name or lang.upper()
        lang_path = I18N_DIR / f"{lang}.yaml"

        if lang_path.exists():
            print(f"Language pack already exists: {lang_path.relative_to(REPO_ROOT)}")
            return 1

        empty_content = generate_empty_i18n_yaml(lang, lang_name, en_data)
        lang_path.write_text(empty_content, encoding="utf-8")
        print(f"Created empty language pack: {lang_path.relative_to(REPO_ROOT)}")
        return 0

    if args.check:
        # Check mode
        mismatches = []
        for path, content in generated.items():
            if not files_match(content, path):
                mismatches.append(path.name)

        if mismatches:
            print("ERROR: i18n taxonomy assets need regeneration:")
            for name in mismatches:
                print(f"  - {name}")
            print("\nRun: python tooling/taxonomy/build_i18n_taxonomy.py")
            return 1
        else:
            print("i18n taxonomy assets check OK (all files up to date)")
            return 0

    # Write mode
    for path, content in generated.items():
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path.relative_to(REPO_ROOT)}")

    print(f"\ni18n taxonomy assets generated successfully ({len(generated)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
