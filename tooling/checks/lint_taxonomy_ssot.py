#!/usr/bin/env python3
"""
Lint check for taxonomy SSOT (canonical.yaml + i18n/*.yaml).

Validates:
1. i18n packs only reference codes that exist in canonical.yaml
2. Required languages (en, optionally ja) have translations for all codes
3. BCP47 language code format for i18n file names
4. Canonical structure integrity (code format, dimension IDs, etc.)

Usage:
    python tooling/checks/lint_taxonomy_ssot.py
    python tooling/checks/lint_taxonomy_ssot.py --required-langs en ja

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Set

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = REPO_ROOT / "data" / "taxonomy"
CANONICAL_PATH = DATA_DIR / "canonical.yaml"
I18N_DIR = DATA_DIR / "i18n"

# Valid dimension IDs (LG = Log/Event Type; EV reserved for Evidence artifact IDs only)
VALID_DIMENSIONS = {"FS", "UC", "DT", "CH", "IM", "RS", "OB", "LG"}

# Code pattern: <DIM>-<NNN>
CODE_PATTERN = re.compile(r"^([A-Z]{2})-(\d{3})$")

# BCP47 language code pattern (simplified)
# Matches: en, ja, es, de, ko, zh-Hans, zh-Hant, pt-BR, etc.
LANG_CODE_PATTERN = re.compile(r"^[a-z]{2,3}(-[A-Za-z]{2,4})?$")


def load_yaml(path: Path) -> dict:
    """Load YAML file."""
    content = path.read_text(encoding="utf-8")
    return yaml.safe_load(content)


def extract_canonical_codes(canonical: dict) -> tuple[Set[str], dict[str, str]]:
    """Extract all codes from canonical.yaml.
    
    Returns:
        codes: Set of all code IDs
        code_to_dim: Mapping of code ID to dimension ID
    """
    codes = set()
    code_to_dim = {}
    
    for dim in canonical.get("dimensions", []):
        dim_id = dim.get("id", "")
        for code_data in dim.get("codes", []):
            code = code_data.get("code", "")
            if code:
                codes.add(code)
                code_to_dim[code] = dim_id
    
    return codes, code_to_dim


def extract_i18n_codes(i18n: dict) -> Set[str]:
    """Extract all codes referenced in i18n pack."""
    codes = set()
    
    for dim_id, dim_data in i18n.get("dimensions", {}).items():
        for code in dim_data.get("codes", {}).keys():
            codes.add(code)
    
    return codes


def check_canonical(canonical: dict, errors: List[str]) -> Set[str]:
    """Validate canonical.yaml structure. Returns set of valid codes."""
    codes = set()
    seen_codes = {}
    
    for dim_idx, dim in enumerate(canonical.get("dimensions", [])):
        dim_id = dim.get("id", "")
        
        # Check dimension ID
        if not dim_id:
            errors.append(f"canonical.yaml: dimensions[{dim_idx}] missing 'id'")
            continue
        
        if dim_id not in VALID_DIMENSIONS:
            errors.append(
                f"canonical.yaml: Invalid dimension_id '{dim_id}'. "
                f"Valid values: {sorted(VALID_DIMENSIONS)}"
            )
        
        for code_idx, code_data in enumerate(dim.get("codes", [])):
            code = code_data.get("code", "")
            
            if not code:
                errors.append(
                    f"canonical.yaml: dimensions[{dim_idx}].codes[{code_idx}] missing 'code'"
                )
                continue
            
            # Check code format
            match = CODE_PATTERN.match(code)
            if not match:
                errors.append(
                    f"canonical.yaml: Invalid code format '{code}'. "
                    f"Expected pattern: <DIM>-<NNN>"
                )
            else:
                code_dim = match.group(1)
                if code_dim != dim_id:
                    errors.append(
                        f"canonical.yaml: Code '{code}' prefix doesn't match dimension '{dim_id}'"
                    )
            
            # Check uniqueness
            if code in seen_codes:
                errors.append(
                    f"canonical.yaml: Duplicate code '{code}' "
                    f"(in dimensions {seen_codes[code]} and {dim_id})"
                )
            else:
                seen_codes[code] = dim_id
                codes.add(code)
            
            # Check required fields
            if "status" not in code_data:
                errors.append(f"canonical.yaml: Code '{code}' missing 'status'")
            if "introduced_in" not in code_data:
                errors.append(f"canonical.yaml: Code '{code}' missing 'introduced_in'")
    
    return codes


def check_i18n_pack(
    path: Path,
    canonical_codes: Set[str],
    required: bool,
    errors: List[str],
    warnings: List[str],
) -> None:
    """Validate an i18n pack."""
    lang = path.stem
    
    # Check BCP47 format
    if not LANG_CODE_PATTERN.match(lang):
        errors.append(
            f"i18n/{lang}.yaml: Invalid language code '{lang}'. "
            f"Use BCP47 format (e.g., en, ja, zh-Hans)"
        )
    
    try:
        i18n = load_yaml(path)
    except Exception as e:
        errors.append(f"i18n/{lang}.yaml: Failed to parse YAML: {e}")
        return
    
    i18n_codes = extract_i18n_codes(i18n)
    
    # Check for orphan codes (in i18n but not in canonical)
    orphan_codes = i18n_codes - canonical_codes
    if orphan_codes:
        errors.append(
            f"i18n/{lang}.yaml: References codes not in canonical.yaml: "
            f"{', '.join(sorted(orphan_codes))}"
        )
    
    # Check for missing codes (in canonical but not in i18n)
    missing_codes = canonical_codes - i18n_codes
    if missing_codes:
        if required:
            errors.append(
                f"i18n/{lang}.yaml: Missing translations for codes: "
                f"{', '.join(sorted(missing_codes))}"
            )
        else:
            warnings.append(
                f"i18n/{lang}.yaml: Missing translations for {len(missing_codes)} codes "
                f"(will fallback to English)"
            )
    
    # Check for empty translations in required language
    if required:
        for dim_id, dim_data in i18n.get("dimensions", {}).items():
            dim_name = dim_data.get("name", "")
            if not dim_name:
                errors.append(
                    f"i18n/{lang}.yaml: Dimension '{dim_id}' has empty 'name'"
                )
            
            for code, code_data in dim_data.get("codes", {}).items():
                if not code_data.get("label"):
                    errors.append(
                        f"i18n/{lang}.yaml: Code '{code}' has empty 'label'"
                    )
                if not code_data.get("definition"):
                    errors.append(
                        f"i18n/{lang}.yaml: Code '{code}' has empty 'definition'"
                    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint taxonomy SSOT (canonical.yaml + i18n/*.yaml)"
    )
    parser.add_argument(
        "--required-langs",
        nargs="+",
        default=["en"],
        help="Languages that must have complete translations (default: en)",
    )
    args = parser.parse_args()
    
    errors: List[str] = []
    warnings: List[str] = []
    
    # Check canonical.yaml exists
    if not CANONICAL_PATH.exists():
        print(f"ERROR: Canonical SSOT not found: {CANONICAL_PATH.relative_to(REPO_ROOT)}")
        return 1
    
    # Load and validate canonical
    print(f"Checking: {CANONICAL_PATH.relative_to(REPO_ROOT)}")
    try:
        canonical = load_yaml(CANONICAL_PATH)
    except Exception as e:
        print(f"ERROR: Failed to parse canonical.yaml: {e}")
        return 1
    
    canonical_codes = check_canonical(canonical, errors)
    print(f"  Found {len(canonical_codes)} codes in canonical.yaml")
    
    # Check i18n packs
    if not I18N_DIR.exists():
        errors.append(f"i18n directory not found: {I18N_DIR.relative_to(REPO_ROOT)}")
    else:
        i18n_files = list(I18N_DIR.glob("*.yaml"))
        print(f"Checking: {len(i18n_files)} i18n packs")
        
        required_set = set(args.required_langs)
        found_required = set()
        
        for i18n_path in i18n_files:
            lang = i18n_path.stem
            is_required = lang in required_set
            if is_required:
                found_required.add(lang)
            
            check_i18n_pack(
                i18n_path,
                canonical_codes,
                required=is_required,
                errors=errors,
                warnings=warnings,
            )
        
        # Check all required languages exist
        missing_required = required_set - found_required
        if missing_required:
            errors.append(
                f"Missing required language packs: {', '.join(sorted(missing_required))}"
            )
    
    # Report results
    if warnings:
        print("\nWARNINGS:")
        for warn in warnings:
            print(f"  {warn}")
    
    if errors:
        print("\nERROR: taxonomy SSOT lint failed:")
        for err in errors:
            print(f"  {err}")
        return 1
    
    print(f"\ntaxonomy SSOT lint OK ({len(canonical_codes)} codes validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
