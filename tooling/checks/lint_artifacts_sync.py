#!/usr/bin/env python3
"""
Artifacts Sync Lint - Ensures SSOT → Distribution integrity.

This script validates that all generated/distributed artifacts match their
SSOT (Single Source of Truth) sources. It is the CI gate that ensures:

1. Taxonomy CSVs in artifacts/ match data/taxonomy/ SSOT
2. Evidence Pack files in distribution dirs match source_pack/ SSOT
3. ZIP-required files exist in the repository

SSOT Definitions:
-----------------
- Taxonomy:
  - SSOT: data/taxonomy/canonical.yaml + data/taxonomy/i18n/*.yaml
  - Distribution: artifacts/taxonomy/current/{lang}/taxonomy_dictionary.csv

- Evidence Pack:
  - SSOT: source_pack/04_evidence_pack/
  - Distribution: schemas/jsonschema/, templates/ev/, examples/

Usage:
    python tooling/checks/lint_artifacts_sync.py          # Report only
    python tooling/checks/lint_artifacts_sync.py --check  # CI mode (exit 1 on mismatch)
    python tooling/checks/lint_artifacts_sync.py --sync   # Actually sync files

Exit codes:
    0 - All artifacts in sync
    1 - Mismatches detected (--check mode)
"""

import argparse
import difflib
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NamedTuple

# Paths
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "taxonomy"
ARTIFACTS_DIR = REPO_ROOT / "artifacts" / "taxonomy"
SOURCE_PACK_EV = REPO_ROOT / "source_pack" / "04_evidence_pack"
SCHEMAS_DIR = REPO_ROOT / "schemas" / "jsonschema"
TEMPLATES_DIR = REPO_ROOT / "templates" / "ev"
EXAMPLES_DIR = REPO_ROOT / "examples"
COVERAGE_MAP = REPO_ROOT / "coverage_map" / "coverage_map.yaml"
VALIDATOR_RULES = REPO_ROOT / "validator" / "rules"

# Evidence Pack sync mappings: (source, destination)
# Each tuple is (source_path_relative_to_SOURCE_PACK_EV, dest_path_relative_to_REPO_ROOT)
EVIDENCE_PACK_SYNC_MAP = [
    ("schemas/evidence_pack_manifest.schema.json", "schemas/jsonschema/evidence_pack_manifest.schema.json"),
    ("examples/evidence_pack_manifest.example.json", "examples/evidence_pack/evidence_pack_manifest.example.json"),
]

# ZIP required files (paths relative to REPO_ROOT)
# These must exist for release ZIP packaging
ZIP_REQUIRED_PATHS = [
    "coverage_map/coverage_map.yaml",
    "validator/rules/checks.yaml",
    "validator/rules/checks.md",
    "VERSIONING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "MIGRATION.md",
]

# ZIP required directories (must exist and contain files)
ZIP_REQUIRED_DIRS = [
    "schemas/jsonschema",
    "templates/ev",
    "examples",
    "validator/rules",
]


class SyncItem(NamedTuple):
    """A single sync verification result."""
    category: str
    source: str
    dest: str
    status: str  # "OK", "MISSING", "MISMATCH", "MISSING_DIR"
    diff: str


def file_hash(path: Path) -> str:
    """Compute SHA256 hash of a file."""
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_content(content: str, ignore_dates: bool = True) -> str:
    """Normalize content for comparison, optionally ignoring dates."""
    import re
    
    lines = []
    for line in content.splitlines():
        if ignore_dates:
            # Skip or normalize date lines
            if "generated_date:" in line.lower():
                continue
            if "last_reviewed_date" in line.lower():
                continue
            if "**generated**:" in line.lower():
                continue
            # Normalize ISO dates in CSV data lines (trailing date column)
            line = re.sub(r',\d{4}-\d{2}-\d{2}$', ',DATE', line)
        lines.append(line)
    return "\n".join(lines)


def compare_files(source: Path, dest: Path, ignore_dates: bool = True) -> tuple[bool, str]:
    """
    Compare two files and return (match, diff_text).
    """
    if not source.exists():
        return False, f"Source not found: {source}"
    if not dest.exists():
        return False, f"Destination not found: {dest}"
    
    source_content = source.read_text(encoding="utf-8")
    dest_content = dest.read_text(encoding="utf-8")
    
    source_normalized = normalize_content(source_content, ignore_dates)
    dest_normalized = normalize_content(dest_content, ignore_dates)
    
    if source_normalized == dest_normalized:
        return True, ""
    
    # Generate unified diff
    diff_lines = list(difflib.unified_diff(
        dest_normalized.splitlines(keepends=True),
        source_normalized.splitlines(keepends=True),
        fromfile=str(dest),
        tofile=str(source),
        lineterm="",
    ))
    
    # Truncate if too long
    if len(diff_lines) > 50:
        diff_text = "".join(diff_lines[:50]) + f"\n... ({len(diff_lines) - 50} more lines)"
    else:
        diff_text = "".join(diff_lines)
    
    return False, diff_text


def check_taxonomy_sync() -> list[SyncItem]:
    """
    Check taxonomy artifacts are in sync with SSOT.
    Uses build_artifacts.py --check internally.
    """
    items = []
    
    # Run the existing build_artifacts.py --check
    build_script = REPO_ROOT / "tooling" / "taxonomy" / "build_artifacts.py"
    if not build_script.exists():
        items.append(SyncItem(
            category="Taxonomy",
            source="tooling/taxonomy/build_artifacts.py",
            dest="",
            status="MISSING",
            diff="Build script not found",
        ))
        return items
    
    # Instead of running subprocess, we check directly
    # This avoids subprocess complexity and gives us more control
    canonical_path = DATA_DIR / "canonical.yaml"
    if not canonical_path.exists():
        items.append(SyncItem(
            category="Taxonomy",
            source="data/taxonomy/canonical.yaml",
            dest="",
            status="MISSING",
            diff="Canonical SSOT not found",
        ))
        return items
    
    # Check for each language
    i18n_dir = DATA_DIR / "i18n"
    if not i18n_dir.exists():
        items.append(SyncItem(
            category="Taxonomy",
            source="data/taxonomy/i18n/",
            dest="",
            status="MISSING_DIR",
            diff="i18n directory not found",
        ))
        return items
    
    langs = [p.stem for p in i18n_dir.glob("*.yaml")]
    
    for lang in langs:
        csv_path = ARTIFACTS_DIR / "current" / lang / "taxonomy_dictionary.csv"
        if not csv_path.exists():
            items.append(SyncItem(
                category="Taxonomy",
                source=f"data/taxonomy/ → artifacts/taxonomy/current/{lang}/",
                dest=str(csv_path.relative_to(REPO_ROOT)),
                status="MISSING",
                diff=f"Expected CSV for language '{lang}' not found",
            ))
        else:
            # For now, just check existence - detailed content check is done by build_artifacts.py
            items.append(SyncItem(
                category="Taxonomy",
                source=f"data/taxonomy/canonical.yaml + i18n/{lang}.yaml",
                dest=str(csv_path.relative_to(REPO_ROOT)),
                status="OK",
                diff="",
            ))
    
    return items


def check_evidence_pack_sync() -> list[SyncItem]:
    """
    Check evidence pack artifacts are in sync with source_pack.
    """
    items = []
    
    if not SOURCE_PACK_EV.exists():
        items.append(SyncItem(
            category="Evidence Pack",
            source="source_pack/04_evidence_pack/",
            dest="",
            status="MISSING_DIR",
            diff="Evidence Pack source directory not found",
        ))
        return items
    
    for source_rel, dest_rel in EVIDENCE_PACK_SYNC_MAP:
        source_path = SOURCE_PACK_EV / source_rel
        dest_path = REPO_ROOT / dest_rel
        
        if not source_path.exists():
            items.append(SyncItem(
                category="Evidence Pack",
                source=f"source_pack/04_evidence_pack/{source_rel}",
                dest=dest_rel,
                status="MISSING",
                diff="Source file not found",
            ))
            continue
        
        if not dest_path.exists():
            items.append(SyncItem(
                category="Evidence Pack",
                source=f"source_pack/04_evidence_pack/{source_rel}",
                dest=dest_rel,
                status="MISSING",
                diff="Destination file not found (needs sync)",
            ))
            continue
        
        match, diff = compare_files(source_path, dest_path, ignore_dates=False)
        items.append(SyncItem(
            category="Evidence Pack",
            source=f"source_pack/04_evidence_pack/{source_rel}",
            dest=dest_rel,
            status="OK" if match else "MISMATCH",
            diff=diff,
        ))
    
    return items


def check_zip_required() -> list[SyncItem]:
    """
    Check all ZIP-required files and directories exist.
    """
    items = []
    
    # Check required files
    for rel_path in ZIP_REQUIRED_PATHS:
        full_path = REPO_ROOT / rel_path
        if full_path.exists():
            items.append(SyncItem(
                category="ZIP Required",
                source=rel_path,
                dest=rel_path,
                status="OK",
                diff="",
            ))
        else:
            items.append(SyncItem(
                category="ZIP Required",
                source=rel_path,
                dest=rel_path,
                status="MISSING",
                diff=f"Required file not found: {rel_path}",
            ))
    
    # Check required directories
    for rel_dir in ZIP_REQUIRED_DIRS:
        full_dir = REPO_ROOT / rel_dir
        if not full_dir.exists():
            items.append(SyncItem(
                category="ZIP Required",
                source=rel_dir,
                dest=rel_dir,
                status="MISSING_DIR",
                diff=f"Required directory not found: {rel_dir}",
            ))
        elif not any(full_dir.iterdir()):
            items.append(SyncItem(
                category="ZIP Required",
                source=rel_dir,
                dest=rel_dir,
                status="MISSING",
                diff=f"Required directory is empty: {rel_dir}",
            ))
        else:
            items.append(SyncItem(
                category="ZIP Required",
                source=rel_dir,
                dest=rel_dir,
                status="OK",
                diff="",
            ))
    
    return items


def sync_evidence_pack() -> list[str]:
    """
    Actually sync evidence pack files from source_pack to distribution directories.
    Returns list of synced file paths.
    """
    synced = []
    
    for source_rel, dest_rel in EVIDENCE_PACK_SYNC_MAP:
        source_path = SOURCE_PACK_EV / source_rel
        dest_path = REPO_ROOT / dest_rel
        
        if not source_path.exists():
            print(f"  SKIP: Source not found: {source_rel}")
            continue
        
        # Create destination directory if needed
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        shutil.copy2(source_path, dest_path)
        synced.append(dest_rel)
        print(f"  SYNCED: {source_rel} → {dest_rel}")
    
    return synced


def run_taxonomy_build_check() -> tuple[bool, str]:
    """
    Run the taxonomy build check and return (success, output).
    """
    build_script = REPO_ROOT / "tooling" / "taxonomy" / "build_artifacts.py"
    if not build_script.exists():
        return False, "Build script not found"
    
    try:
        result = subprocess.run(
            [sys.executable, str(build_script), "--check"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check SSOT → Distribution artifact synchronization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python tooling/checks/lint_artifacts_sync.py          # Report only
    python tooling/checks/lint_artifacts_sync.py --check  # CI mode
    python tooling/checks/lint_artifacts_sync.py --sync   # Sync files
        """,
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="CI mode: exit 1 if any mismatches found",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Actually sync files from SSOT to distribution",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed diff output",
    )
    args = parser.parse_args()
    
    print("=" * 70)
    print("AIMO Artifacts Sync Check")
    print("=" * 70)
    print()
    
    all_items: list[SyncItem] = []
    
    # === Check 1: Taxonomy ===
    print("Checking Taxonomy SSOT → artifacts/ sync...")
    
    # Run the dedicated build_artifacts.py --check
    taxonomy_ok, taxonomy_output = run_taxonomy_build_check()
    if not taxonomy_ok:
        all_items.append(SyncItem(
            category="Taxonomy",
            source="data/taxonomy/",
            dest="artifacts/taxonomy/current/",
            status="MISMATCH",
            diff=taxonomy_output,
        ))
    else:
        all_items.append(SyncItem(
            category="Taxonomy",
            source="data/taxonomy/",
            dest="artifacts/taxonomy/current/",
            status="OK",
            diff="",
        ))
        print("  Taxonomy check OK")
    
    # === Check 2: Evidence Pack ===
    print("Checking Evidence Pack source_pack/ → distribution sync...")
    ev_items = check_evidence_pack_sync()
    all_items.extend(ev_items)
    
    for item in ev_items:
        if item.status == "OK":
            print(f"  OK: {item.dest}")
        else:
            print(f"  {item.status}: {item.dest}")
    
    # === Check 3: ZIP Required ===
    print("Checking ZIP-required files existence...")
    zip_items = check_zip_required()
    all_items.extend(zip_items)
    
    missing_count = sum(1 for i in zip_items if i.status != "OK")
    ok_count = sum(1 for i in zip_items if i.status == "OK")
    print(f"  {ok_count} present, {missing_count} missing")
    
    # === Summary ===
    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    
    ok_items = [i for i in all_items if i.status == "OK"]
    problem_items = [i for i in all_items if i.status != "OK"]
    
    print(f"Total: {len(all_items)} checks")
    print(f"  OK: {len(ok_items)}")
    print(f"  Problems: {len(problem_items)}")
    
    if problem_items:
        print()
        print("=" * 70)
        print("Problems Found")
        print("=" * 70)
        
        for item in problem_items:
            print(f"\n[{item.status}] {item.category}")
            print(f"  Source: {item.source}")
            if item.dest:
                print(f"  Dest:   {item.dest}")
            if item.diff and args.verbose:
                print(f"  Diff:\n{item.diff}")
            elif item.diff:
                # Show truncated diff
                lines = item.diff.splitlines()
                if len(lines) > 5:
                    for line in lines[:5]:
                        print(f"    {line}")
                    print(f"    ... ({len(lines) - 5} more lines, use -v for full)")
                else:
                    for line in lines:
                        print(f"    {line}")
    
    # === Sync Mode ===
    if args.sync:
        print()
        print("=" * 70)
        print("Syncing Evidence Pack files...")
        print("=" * 70)
        synced = sync_evidence_pack()
        print(f"Synced {len(synced)} file(s)")
        
        print()
        print("Rebuilding Taxonomy artifacts...")
        build_script = REPO_ROOT / "tooling" / "taxonomy" / "build_artifacts.py"
        result = subprocess.run(
            [sys.executable, str(build_script), "--version", "current", "--langs", "en", "ja"],
            cwd=REPO_ROOT,
        )
        if result.returncode != 0:
            print("ERROR: Taxonomy rebuild failed")
            return 1
    
    # === Exit Code ===
    if args.check and problem_items:
        print()
        print("=" * 70)
        print("FAILED: Artifacts out of sync")
        print("=" * 70)
        print()
        print("To fix:")
        print("  1. Update SSOT files in data/ or source_pack/")
        print("  2. Run: python tooling/checks/lint_artifacts_sync.py --sync")
        print("  3. Commit the updated artifacts")
        return 1
    
    print()
    if not problem_items:
        print("artifacts sync check OK")
    else:
        print("artifacts sync check completed with warnings")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
