#!/usr/bin/env python3
"""
Build taxonomy artifacts from SSOT (canonical.yaml + i18n/*.yaml).

This is the main build script for taxonomy distribution files. It reads the
SSOT in data/taxonomy/ and generates:

1. artifacts/taxonomy/{version}/{lang}/taxonomy_dictionary.csv
   - Single-language CSV for distribution
   - Stable column structure (no language suffix columns)

2. source_pack/03_taxonomy/legacy/taxonomy_dictionary_v0.1.csv
   - Legacy EN/JA mixed CSV (21 columns)
   - Maintained for backward compatibility

3. source_pack/03_taxonomy/ derived files
   - taxonomy_en.yaml, taxonomy_ja.yaml
   - code_system.csv, dimensions_en_ja.md
   - taxonomy_dictionary.json

Usage:
    python tooling/taxonomy/build_artifacts.py --version current --langs en ja
    python tooling/taxonomy/build_artifacts.py --version 0.1.0 --langs en ja es
    python tooling/taxonomy/build_artifacts.py --check

Exit codes:
    0 - Success
    1 - Error
"""

import argparse
import csv
import hashlib
import json
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("WARNING: PyYAML not installed. Using simple YAML parser.")

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = REPO_ROOT / "data" / "taxonomy"
CANONICAL_PATH = DATA_DIR / "canonical.yaml"
I18N_DIR = DATA_DIR / "i18n"
ARTIFACTS_DIR = REPO_ROOT / "artifacts" / "taxonomy"
SOURCE_PACK_DIR = REPO_ROOT / "source_pack" / "03_taxonomy"
LEGACY_DIR = SOURCE_PACK_DIR / "legacy"

# Required languages (must have translations for all codes)
REQUIRED_LANGS = ["en"]  # ja is currently required but can be made optional

# Allowed legacy CSV columns (frozen)
LEGACY_ALLOWED_COLUMNS = [
    "standard_id", "standard_version", "dimension_id",
    "dimension_name_en", "dimension_name_ja",
    "code", "label_en", "label_ja", "definition_en", "definition_ja",
    "scope_notes", "examples", "status", "introduced_in",
    "deprecated_in", "removed_in", "replaced_by", "backward_compatible",
    "references", "owner", "last_reviewed_date",
]


def simple_yaml_parse(content: str) -> dict:
    """Simple YAML parser for basic structures (fallback)."""
    # This is a minimal parser; prefer PyYAML
    raise NotImplementedError("PyYAML is required. Install with: pip install pyyaml")


def load_yaml(path: Path) -> dict:
    """Load YAML file."""
    content = path.read_text(encoding="utf-8")
    if HAS_YAML:
        return yaml.safe_load(content)
    return simple_yaml_parse(content)


def load_canonical() -> dict:
    """Load canonical.yaml."""
    if not CANONICAL_PATH.exists():
        raise FileNotFoundError(f"Canonical SSOT not found: {CANONICAL_PATH}")
    return load_yaml(CANONICAL_PATH)


def load_i18n(lang: str) -> Optional[dict]:
    """Load i18n pack for a language."""
    path = I18N_DIR / f"{lang}.yaml"
    if not path.exists():
        return None
    return load_yaml(path)


def get_available_langs() -> list[str]:
    """Get list of available language packs."""
    langs = []
    for path in I18N_DIR.glob("*.yaml"):
        langs.append(path.stem)
    return sorted(langs)


def build_code_index(canonical: dict) -> dict[str, dict]:
    """Build index of codes from canonical data."""
    index = {}
    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        for code_data in dim.get("codes", []):
            code = code_data["code"]
            index[code] = {
                "dimension_id": dim_id,
                **code_data,
            }
    return index


def build_dimension_index(canonical: dict, i18n: dict) -> dict[str, dict]:
    """Build dimension index with translated names."""
    index = {}
    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        dim_i18n = i18n.get("dimensions", {}).get(dim_id, {})
        index[dim_id] = {
            "id": dim_id,
            "name": dim_i18n.get("name", dim_id),
        }
    return index


def generate_single_lang_csv(
    canonical: dict,
    i18n: dict,
    lang: str,
    fallback_i18n: Optional[dict] = None,
) -> str:
    """Generate single-language taxonomy dictionary CSV."""
    lines = []
    header = [
        "code", "dimension", "dimension_name", "label", "definition",
        "status", "introduced_in", "scope_notes", "examples",
    ]
    lines.append(",".join(header))

    code_index = build_code_index(canonical)
    dim_index = build_dimension_index(canonical, i18n)

    for code in sorted(code_index.keys()):
        code_data = code_index[code]
        dim_id = code_data["dimension_id"]
        dim_name = dim_index.get(dim_id, {}).get("name", dim_id)

        # Get translated label/definition
        dim_i18n = i18n.get("dimensions", {}).get(dim_id, {}).get("codes", {})
        code_i18n = dim_i18n.get(code, {})

        label = code_i18n.get("label", "")
        definition = code_i18n.get("definition", "")

        # Fallback to English if translation missing
        if fallback_i18n and (not label or not definition):
            fallback_dim = fallback_i18n.get("dimensions", {}).get(dim_id, {}).get("codes", {})
            fallback_code = fallback_dim.get(code, {})
            if not label:
                label = fallback_code.get("label", "")
            if not definition:
                definition = fallback_code.get("definition", "")

        # Format examples
        examples = code_data.get("examples", [])
        examples_str = "|".join(examples) if isinstance(examples, list) else str(examples)

        row = [
            code,
            dim_id,
            escape_csv(dim_name),
            escape_csv(label),
            escape_csv(definition),
            code_data.get("status", "active"),
            code_data.get("introduced_in", ""),
            escape_csv(code_data.get("scope_notes", "")),
            escape_csv(examples_str),
        ]
        lines.append(",".join(row))

    return "\n".join(lines) + "\n"


def escape_csv(value: str) -> str:
    """Escape CSV value."""
    if not value:
        return ""
    if "," in value or '"' in value or "\n" in value:
        return '"' + value.replace('"', '""') + '"'
    return value


def generate_legacy_csv(canonical: dict, en_i18n: dict, ja_i18n: dict) -> str:
    """Generate legacy EN/JA mixed CSV (21 columns)."""
    lines = []
    lines.append(",".join(LEGACY_ALLOWED_COLUMNS))

    code_index = build_code_index(canonical)
    en_dims = en_i18n.get("dimensions", {})
    ja_dims = ja_i18n.get("dimensions", {})

    for code in sorted(code_index.keys()):
        code_data = code_index[code]
        dim_id = code_data["dimension_id"]

        en_dim = en_dims.get(dim_id, {})
        ja_dim = ja_dims.get(dim_id, {})
        en_code = en_dim.get("codes", {}).get(code, {})
        ja_code = ja_dim.get("codes", {}).get(code, {})

        examples = code_data.get("examples", [])
        examples_str = "|".join(examples) if isinstance(examples, list) else str(examples)

        row = [
            "AIMO-STD",  # standard_id
            canonical.get("version", "0.1.0"),  # standard_version
            dim_id,  # dimension_id
            escape_csv(en_dim.get("name", "")),  # dimension_name_en
            escape_csv(ja_dim.get("name", "")),  # dimension_name_ja
            code,  # code
            escape_csv(en_code.get("label", "")),  # label_en
            escape_csv(ja_code.get("label", "")),  # label_ja
            escape_csv(en_code.get("definition", "")),  # definition_en
            escape_csv(ja_code.get("definition", "")),  # definition_ja
            escape_csv(code_data.get("scope_notes", "")),  # scope_notes
            escape_csv(examples_str),  # examples
            code_data.get("status", "active"),  # status
            code_data.get("introduced_in", ""),  # introduced_in
            code_data.get("deprecated_in", ""),  # deprecated_in
            code_data.get("removed_in", ""),  # removed_in
            code_data.get("replaced_by", ""),  # replaced_by
            str(code_data.get("backward_compatible", True)).lower(),  # backward_compatible
            "",  # references
            "AIMO WG",  # owner
            date.today().isoformat(),  # last_reviewed_date
        ]
        lines.append(",".join(row))

    return "\n".join(lines) + "\n"


def generate_taxonomy_yaml(canonical: dict, i18n: dict, lang: str) -> str:
    """Generate taxonomy_*.yaml for a language."""
    lines = [
        f"# AIMO Taxonomy ({i18n.get('language_name', lang)})",
        f"# Generated from: data/taxonomy/canonical.yaml + i18n/{lang}.yaml",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_artifacts.py",
        "",
        f'version: "{canonical.get("version", "0.1.0")}"',
        f'generated_date: "{date.today().isoformat()}"',
        "",
        "dimensions:",
    ]

    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        dim_i18n = i18n.get("dimensions", {}).get(dim_id, {})
        dim_name = dim_i18n.get("name", dim_id)

        lines.append(f"  - id: {dim_id}")
        lines.append(f'    name: "{escape_yaml(dim_name)}"')
        lines.append("    codes:")

        for code_data in dim.get("codes", []):
            code = code_data["code"]
            code_i18n = dim_i18n.get("codes", {}).get(code, {})

            label = code_i18n.get("label", "")
            definition = code_i18n.get("definition", "")

            lines.append(f"      - code: {code}")
            lines.append(f'        label: "{escape_yaml(label)}"')
            lines.append(f'        definition: "{escape_yaml(definition)}"')
            lines.append(f'        status: {code_data.get("status", "active")}')
            lines.append(f'        introduced_in: "{code_data.get("introduced_in", "")}"')

            if code_data.get("deprecated_in"):
                lines.append(f'        deprecated_in: "{code_data["deprecated_in"]}"')
            if code_data.get("removed_in"):
                lines.append(f'        removed_in: "{code_data["removed_in"]}"')
            if code_data.get("replaced_by"):
                lines.append(f'        replaced_by: "{code_data["replaced_by"]}"')

    lines.append("")
    return "\n".join(lines)


def escape_yaml(value: str) -> str:
    """Escape YAML string value."""
    if not value:
        return ""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def generate_code_system_csv(canonical: dict, en_i18n: dict, ja_i18n: dict) -> str:
    """Generate code_system.csv."""
    lines = [
        "# Code System Namespaces",
        "# Generated from: data/taxonomy/canonical.yaml",
        "# DO NOT EDIT MANUALLY - regenerate with: python tooling/taxonomy/build_artifacts.py",
        "dimension_id,dimension_name_en,dimension_name_ja,namespace_prefix,code_count,notes",
    ]

    en_dims = en_i18n.get("dimensions", {})
    ja_dims = ja_i18n.get("dimensions", {})

    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        name_en = en_dims.get(dim_id, {}).get("name", "")
        name_ja = ja_dims.get(dim_id, {}).get("name", "")
        prefix = f"{dim_id}-"
        code_count = len(dim.get("codes", []))
        notes = f"{code_count} codes defined"
        lines.append(f'{dim_id},"{name_en}","{name_ja}",{prefix},{code_count},"{notes}"')

    lines.append("")
    return "\n".join(lines)


def generate_dimensions_md(canonical: dict, en_i18n: dict, ja_i18n: dict) -> str:
    """Generate dimensions_en_ja.md."""
    lines = [
        "# Dimension Names EN/JA Mapping",
        "",
        "**Status**: Generated from data/taxonomy/",
        "**DO NOT EDIT MANUALLY** - regenerate with: `python tooling/taxonomy/build_artifacts.py`",
        "",
        "---",
        "",
        "## Dimension Definitions",
        "",
        "| ID | Name (EN) | Name (JA) | Code Count | Prefix |",
        "| --- | --- | --- | --- | --- |",
    ]

    en_dims = en_i18n.get("dimensions", {})
    ja_dims = ja_i18n.get("dimensions", {})

    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        name_en = en_dims.get(dim_id, {}).get("name", "")
        name_ja = ja_dims.get(dim_id, {}).get("name", "")
        code_count = len(dim.get("codes", []))
        prefix = f"`{dim_id}-`"
        lines.append(f"| **{dim_id}** | {name_en} | {name_ja} | {code_count} | {prefix} |")

    lines.extend([
        "",
        "---",
        "",
        "## Code Summary by Dimension",
        "",
    ])

    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        en_dim = en_dims.get(dim_id, {})
        ja_dim = ja_dims.get(dim_id, {})

        lines.append(f"### {dim_id}: {en_dim.get('name', '')} / {ja_dim.get('name', '')}")
        lines.append("")
        lines.append("| Code | Label (EN) | Label (JA) | Status |")
        lines.append("| --- | --- | --- | --- |")

        for code_data in dim.get("codes", []):
            code = code_data["code"]
            en_code = en_dim.get("codes", {}).get(code, {})
            ja_code = ja_dim.get("codes", {}).get(code, {})
            status = code_data.get("status", "active")
            lines.append(f"| {code} | {en_code.get('label', '')} | {ja_code.get('label', '')} | {status} |")

        lines.append("")

    total_codes = sum(len(dim.get("codes", [])) for dim in canonical.get("dimensions", []))
    lines.extend([
        "---",
        "",
        "## Generation Info",
        "",
        f"- **Source**: `data/taxonomy/canonical.yaml` + `i18n/*.yaml`",
        f"- **Generated**: {date.today().isoformat()}",
        f"- **Total Codes**: {total_codes}",
        "",
    ])

    return "\n".join(lines)


def generate_taxonomy_json(canonical: dict, en_i18n: dict, ja_i18n: dict) -> str:
    """Generate taxonomy_dictionary.json."""
    entries = []

    en_dims = en_i18n.get("dimensions", {})
    ja_dims = ja_i18n.get("dimensions", {})

    for dim in canonical.get("dimensions", []):
        dim_id = dim["id"]
        en_dim = en_dims.get(dim_id, {})
        ja_dim = ja_dims.get(dim_id, {})

        for code_data in dim.get("codes", []):
            code = code_data["code"]
            en_code = en_dim.get("codes", {}).get(code, {})
            ja_code = ja_dim.get("codes", {}).get(code, {})

            entry: dict[str, Any] = {
                "dimension_id": dim_id,
                "code": code,
                "label_en": en_code.get("label", ""),
                "label_ja": ja_code.get("label", ""),
                "definition_en": en_code.get("definition", ""),
                "definition_ja": ja_code.get("definition", ""),
                "status": code_data.get("status", "active"),
                "introduced_in": code_data.get("introduced_in", ""),
                "backward_compatible": code_data.get("backward_compatible", True),
            }

            if code_data.get("deprecated_in"):
                entry["deprecated_in"] = code_data["deprecated_in"]
            if code_data.get("replaced_by"):
                entry["replaced_by"] = code_data["replaced_by"]

            entries.append(entry)

    dictionary = {
        "taxonomy_version": canonical.get("version", "0.1.0"),
        "entries": entries,
    }

    return json.dumps(dictionary, ensure_ascii=False, indent=2) + "\n"


def write_file(path: Path, content: str) -> None:
    """Write file, creating directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build taxonomy artifacts from SSOT",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python tooling/taxonomy/build_artifacts.py --version current --langs en ja
    python tooling/taxonomy/build_artifacts.py --version 0.1.0 --langs en ja es
    python tooling/taxonomy/build_artifacts.py --check
        """,
    )
    parser.add_argument(
        "--version",
        default="current",
        help="Version directory name (default: current)",
    )
    parser.add_argument(
        "--langs",
        nargs="+",
        default=["en", "ja"],
        help="Languages to generate (default: en ja)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if regeneration is needed (no file writes)",
    )
    args = parser.parse_args()

    # Load SSOT
    print(f"Loading SSOT from: {DATA_DIR.relative_to(REPO_ROOT)}")

    try:
        canonical = load_canonical()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1

    print(f"  canonical.yaml: {len(canonical.get('dimensions', []))} dimensions")

    # Load i18n packs
    i18n_packs = {}
    available = get_available_langs()
    print(f"  Available languages: {', '.join(available)}")

    for lang in args.langs:
        i18n = load_i18n(lang)
        if i18n is None:
            print(f"ERROR: Language pack not found: {I18N_DIR / f'{lang}.yaml'}")
            return 1
        i18n_packs[lang] = i18n
        print(f"  {lang}.yaml: loaded")

    # Ensure required languages are present
    for req_lang in REQUIRED_LANGS:
        if req_lang not in i18n_packs:
            print(f"ERROR: Required language '{req_lang}' not in --langs")
            return 1

    # Get English as fallback
    en_i18n = i18n_packs.get("en")
    ja_i18n = i18n_packs.get("ja", en_i18n)  # Fallback to en if ja not present

    generated_files: dict[Path, str] = {}

    # Generate per-language artifacts
    print(f"\nGenerating artifacts for version: {args.version}")
    for lang in args.langs:
        csv_path = ARTIFACTS_DIR / args.version / lang / "taxonomy_dictionary.csv"
        csv_content = generate_single_lang_csv(
            canonical, i18n_packs[lang], lang,
            fallback_i18n=en_i18n if lang != "en" else None,
        )
        generated_files[csv_path] = csv_content

    # Generate legacy CSV (EN/JA only)
    if en_i18n and ja_i18n:
        legacy_path = LEGACY_DIR / "taxonomy_dictionary_v0.1.csv"
        legacy_content = generate_legacy_csv(canonical, en_i18n, ja_i18n)
        generated_files[legacy_path] = legacy_content

        # Also create dictionary_seed.csv as alias
        seed_path = LEGACY_DIR / "dictionary_seed.csv"
        generated_files[seed_path] = legacy_content

    # Generate source_pack derived files
    for lang in ["en", "ja"]:
        if lang in i18n_packs:
            yaml_path = SOURCE_PACK_DIR / f"taxonomy_{lang}.yaml"
            yaml_content = generate_taxonomy_yaml(canonical, i18n_packs[lang], lang)
            generated_files[yaml_path] = yaml_content

    if en_i18n and ja_i18n:
        generated_files[SOURCE_PACK_DIR / "code_system.csv"] = generate_code_system_csv(
            canonical, en_i18n, ja_i18n
        )
        generated_files[SOURCE_PACK_DIR / "dimensions_en_ja.md"] = generate_dimensions_md(
            canonical, en_i18n, ja_i18n
        )
        generated_files[SOURCE_PACK_DIR / "taxonomy_dictionary.json"] = generate_taxonomy_json(
            canonical, en_i18n, ja_i18n
        )

    if args.check:
        # Check mode: verify files are up to date
        mismatches = []
        for path, content in generated_files.items():
            if not path.exists():
                mismatches.append(f"  Missing: {path.relative_to(REPO_ROOT)}")
            else:
                existing = path.read_text(encoding="utf-8")
                # Ignore date differences for comparison
                if normalize_for_compare(content) != normalize_for_compare(existing):
                    mismatches.append(f"  Outdated: {path.relative_to(REPO_ROOT)}")

        if mismatches:
            print("\nERROR: Taxonomy artifacts need regeneration:")
            for m in mismatches:
                print(m)
            print("\nRun: python tooling/taxonomy/build_artifacts.py --version current --langs en ja")
            return 1

        print("\ntaxonomy artifacts check OK (all files up to date)")
        return 0

    # Write mode
    for path, content in generated_files.items():
        write_file(path, content)
        print(f"  Generated: {path.relative_to(REPO_ROOT)}")

    print(f"\nTaxonomy artifacts generated successfully ({len(generated_files)} files)")
    return 0


def normalize_for_compare(content: str) -> str:
    """Normalize content for comparison (ignore dates)."""
    import re
    # Pattern to match ISO dates (YYYY-MM-DD) at end of CSV lines
    date_pattern = re.compile(r',\d{4}-\d{2}-\d{2}$')
    
    lines = []
    for line in content.splitlines():
        # Skip lines that contain generated dates (YAML/MD)
        if "generated_date:" in line.lower():
            continue
        if "**generated**:" in line.lower():
            continue
        if "- **generated**:" in line.lower():
            continue
        # Skip CSV header containing last_reviewed_date
        if "last_reviewed_date" in line.lower():
            continue
        # Normalize CSV data lines: remove trailing date column
        normalized_line = date_pattern.sub(',DATE', line)
        lines.append(normalized_line)
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
