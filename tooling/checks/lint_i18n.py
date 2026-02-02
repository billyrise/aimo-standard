#!/usr/bin/env python3
"""
i18n lint for folder-based structure (docs/en/, docs/ja/).

Quality Gates:
1. Language Purity: No CJK characters in EN files (excludes code blocks)
2. Required Pages: Critical pages must exist in all active languages
3. Heading Consistency: Heading levels match between translations
4. Orphan Detection: Warn about JA files without EN counterpart
5. Language-specific Column Detection: Detect _ja/_en suffixed columns in wrong language docs

Exit Codes:
- 0: All checks pass
- 1: Critical errors found (CI should fail)

Usage:
    python tooling/checks/lint_i18n.py          # Run all checks
    python tooling/checks/lint_i18n.py --strict # Treat warnings as errors
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
EN_DIR = DOCS / "en"
JA_DIR = DOCS / "ja"

# Active languages (languages that should be fully validated)
ACTIVE_LANGUAGES = ["en", "ja"]

# Required pages that MUST exist in all active languages
# These are critical for the documentation to be functional
REQUIRED_PAGES = [
    "index.md",
    "standard/index.md",
    "standard/current/index.md",
    "standard/current/01-overview.md",
    "standard/current/02-scope.md",
    "standard/current/03-taxonomy.md",
    "standard/current/04-codes.md",
    "standard/current/05-dictionary.md",
    "standard/current/06-ev-template.md",
    "standard/current/07-validator.md",
    "governance/index.md",
    "releases/index.md",
]

# Pages that are recommended but not critical (warn if missing)
RECOMMENDED_PAGES = [
    "coverage-map/index.md",
    "coverage-map/methodology.md",
    "artifacts/index.md",
    "contributing/localization.md",
]

# Pages allowed to have mixed-language content (e.g., translation mapping docs)
# Use relative path from language directory (e.g., "contributing/localization.md")
MIXED_LANGUAGE_ALLOWLIST = [
    "contributing/localization.md",  # Localization guide may reference both languages
]

# Regex patterns
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
# CJK character ranges:
# - Hiragana: U+3040-U+309F
# - Katakana: U+30A0-U+30FF
# - CJK Unified Ideographs: U+4E00-U+9FFF
# - CJK Extension A: U+3400-U+4DBF
# - Full-width forms: U+FF00-U+FFEF
# Note: CJK Extension B (U+20000+) requires special handling and is omitted
CJK_RE = re.compile(r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3400-\u4DBF\uFF00-\uFFEF]")
# Code block detection
CODE_FENCE_RE = re.compile(r"^```")

# Language-specific column patterns that indicate wrong language content
# In EN pages: should not have _ja suffix columns documented
# In JA pages: should not have _en suffix columns documented
LANG_COLUMN_PATTERNS = {
    "en": [
        re.compile(r"`[a-z_]+_ja`"),  # _ja suffix columns like `label_ja`
        re.compile(r"\|\s*`?dimension_name_ja`?\s*\|"),  # Table cells with _ja columns
        re.compile(r"\|\s*`?label_ja`?\s*\|"),
        re.compile(r"\|\s*`?definition_ja`?\s*\|"),
        re.compile(r"Japanese\s+(dimension\s+name|label|definition)", re.IGNORECASE),
    ],
    "ja": [
        # JA pages should use Japanese terminology, not EN-specific references
        # This is a softer check - we mainly care about _ja columns in EN pages
    ],
}

# Deprecated SSOT phrases that should not appear in documentation
# These indicate outdated references to the old CSV-as-SSOT model
DEPRECATED_SSOT_PHRASES = [
    # English patterns
    re.compile(r"SSOT\s+is\s+(the\s+)?CSV", re.IGNORECASE),
    re.compile(r"taxonomy_dictionary_v0\.1\.csv.*(?:is|as)\s+the\s+(?:authoritative|SSOT|single\s+source)", re.IGNORECASE),
    re.compile(r"(?:serves?\s+as|is)\s+(?:the\s+)?(?:Single\s+Source\s+of\s+Truth|SSOT).*CSV", re.IGNORECASE),
    re.compile(r"CSV\s+file\s+(?:that\s+)?serves?\s+as\s+(?:the\s+)?(?:Single\s+Source|SSOT)", re.IGNORECASE),
    # Japanese patterns
    re.compile(r"CSV.*(?:が|は).*(?:正式|正本|SSOT)", re.IGNORECASE),
    re.compile(r"辞書CSV.*が正式なソース", re.IGNORECASE),
]

# Files that may contain legacy references for historical/migration documentation
DEPRECATED_PHRASE_ALLOWLIST = [
    "contributing/localization.md",  # May explain migration
    "releases/index.md",  # May reference old versions
]


def is_in_code_block(lines: list[str], line_idx: int) -> bool:
    """Check if the given line is inside a fenced code block."""
    fence_count = 0
    for i in range(line_idx):
        if CODE_FENCE_RE.match(lines[i].strip()):
            fence_count += 1
    # If odd number of fences before this line, we're inside a code block
    return fence_count % 2 == 1


def check_language_purity(filepath: Path) -> list[tuple[int, str]]:
    """
    Check for CJK characters in an English file.
    Excludes content inside fenced code blocks.
    Returns list of (line_num, line_content).
    """
    issues = []
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()

    for i, line in enumerate(lines):
        # Skip if inside code block
        if is_in_code_block(lines, i):
            continue
        # Skip inline code (backticks)
        # Remove inline code spans before checking
        line_without_code = re.sub(r"`[^`]+`", "", line)
        if CJK_RE.search(line_without_code):
            issues.append((i + 1, line.strip()))

    return issues


def check_language_column_patterns(filepath: Path, lang: str) -> list[tuple[int, str, str]]:
    """
    Check for language-specific column patterns in the wrong language file.
    For example, _ja suffix columns should not be documented in EN pages.
    
    Returns list of (line_num, line_content, pattern_description).
    """
    issues = []
    patterns = LANG_COLUMN_PATTERNS.get(lang, [])
    if not patterns:
        return issues

    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()

    for i, line in enumerate(lines):
        # Skip if inside code block (code examples may legitimately reference columns)
        if is_in_code_block(lines, i):
            continue

        for pattern in patterns:
            if pattern.search(line):
                issues.append((i + 1, line.strip(), pattern.pattern))
                break  # Only report first match per line

    return issues


def check_deprecated_ssot_phrases(filepath: Path) -> list[tuple[int, str, str]]:
    """
    Check for deprecated SSOT phrases that incorrectly state CSV is the SSOT.
    The correct SSOT is canonical.yaml + i18n/*.yaml.
    
    Returns list of (line_num, line_content, pattern_description).
    """
    issues = []
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()

    for i, line in enumerate(lines):
        # Skip if inside code block
        if is_in_code_block(lines, i):
            continue

        for pattern in DEPRECATED_SSOT_PHRASES:
            if pattern.search(line):
                issues.append((i + 1, line.strip(), pattern.pattern))
                break  # Only report first match per line

    return issues


def extract_headings(filepath: Path) -> list[tuple[int, str]]:
    """Extract heading levels and text from a markdown file."""
    headings = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line.strip())
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headings.append((level, text))
    return headings


def check_required_pages(lang_dir: Path, lang: str) -> tuple[list[str], list[str]]:
    """
    Check for required and recommended pages.
    Returns (missing_required, missing_recommended).
    """
    missing_required = []
    missing_recommended = []

    for page in REQUIRED_PAGES:
        if not (lang_dir / page).exists():
            missing_required.append(f"docs/{lang}/{page}")

    for page in RECOMMENDED_PAGES:
        if not (lang_dir / page).exists():
            missing_recommended.append(f"docs/{lang}/{page}")

    return missing_required, missing_recommended


def main():
    parser = argparse.ArgumentParser(description="i18n lint for AIMO documentation")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    # Verify base directories exist
    if not EN_DIR.exists():
        errors.append(f"EN directory not found: {EN_DIR.relative_to(ROOT)}")
        print("i18n lint FAILED:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)

    if not JA_DIR.exists():
        errors.append(f"JA directory not found: {JA_DIR.relative_to(ROOT)}")
        print("i18n lint FAILED:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)

    # === Check 1: Required Pages ===
    print("Checking required pages...")
    for lang in ACTIVE_LANGUAGES:
        lang_dir = DOCS / lang
        missing_req, missing_rec = check_required_pages(lang_dir, lang)

        for page in missing_req:
            errors.append(f"[CRITICAL] Missing required page: {page}")

        for page in missing_rec:
            warnings.append(f"[WARN] Missing recommended page: {page}")

    # === Check 2: Language Purity (CJK in EN files) ===
    print("Checking language purity (EN files)...")
    en_files = sorted(EN_DIR.rglob("*.md"))

    for en_file in en_files:
        rel_path = en_file.relative_to(EN_DIR)
        rel_path_str = str(rel_path).replace("\\", "/")

        # Skip files in allowlist
        if rel_path_str in MIXED_LANGUAGE_ALLOWLIST:
            continue

        cjk_issues = check_language_purity(en_file)

        for line_num, line in cjk_issues:
            errors.append(
                f"[CRITICAL] CJK characters in EN file: docs/en/{rel_path}:{line_num}\n"
                f"           {line[:80]}{'...' if len(line) > 80 else ''}"
            )

    # === Check 2b: Language-specific Column Patterns (e.g., _ja in EN files) ===
    print("Checking for wrong-language column patterns...")
    for en_file in en_files:
        rel_path = en_file.relative_to(EN_DIR)
        rel_path_str = str(rel_path).replace("\\", "/")

        # Skip files in allowlist
        if rel_path_str in MIXED_LANGUAGE_ALLOWLIST:
            continue

        column_issues = check_language_column_patterns(en_file, "en")

        for line_num, line, pattern in column_issues:
            errors.append(
                f"[CRITICAL] Language-specific content in EN file: docs/en/{rel_path}:{line_num}\n"
                f"           Pattern: {pattern}\n"
                f"           {line[:80]}{'...' if len(line) > 80 else ''}"
            )

    # === Check 2c: Deprecated SSOT Phrases (CSV is not the SSOT) ===
    print("Checking for deprecated SSOT phrases...")
    all_docs = list(EN_DIR.rglob("*.md")) + list(JA_DIR.rglob("*.md"))
    for doc_file in all_docs:
        # Determine relative path for allowlist check
        if doc_file.is_relative_to(EN_DIR):
            rel_path = doc_file.relative_to(EN_DIR)
            lang_prefix = "en"
        else:
            rel_path = doc_file.relative_to(JA_DIR)
            lang_prefix = "ja"
        rel_path_str = str(rel_path).replace("\\", "/")

        # Skip files in allowlist
        if rel_path_str in DEPRECATED_PHRASE_ALLOWLIST:
            continue

        ssot_issues = check_deprecated_ssot_phrases(doc_file)

        for line_num, line, pattern in ssot_issues:
            errors.append(
                f"[CRITICAL] Deprecated SSOT phrase in docs/{lang_prefix}/{rel_path}:{line_num}\n"
                f"           Pattern: {pattern}\n"
                f"           {line[:80]}{'...' if len(line) > 80 else ''}\n"
                f"           FIX: SSOT is canonical.yaml + i18n/*.yaml, not CSV"
            )

    # === Check 3: Translation Coverage & Heading Consistency ===
    print("Checking translation coverage...")
    for en_file in en_files:
        rel_path = en_file.relative_to(EN_DIR)
        ja_file = JA_DIR / rel_path

        if not ja_file.exists():
            # Missing translation - warn only (fallback to EN is acceptable)
            warnings.append(f"[WARN] No JA translation: docs/ja/{rel_path} (fallback to EN)")
            continue

        # Heading level consistency
        en_headings = extract_headings(en_file)
        ja_headings = extract_headings(ja_file)

        en_levels = [lv for (lv, _) in en_headings]
        ja_levels = [lv for (lv, _) in ja_headings]

        if en_levels != ja_levels:
            warnings.append(
                f"[WARN] Heading level mismatch: docs/en/{rel_path} vs docs/ja/{rel_path}\n"
                f"       EN: {en_levels}\n"
                f"       JA: {ja_levels}"
            )

    # === Check 4: Orphan JA Files ===
    print("Checking for orphan JA files...")
    ja_files = sorted(JA_DIR.rglob("*.md"))
    for ja_file in ja_files:
        rel_path = ja_file.relative_to(JA_DIR)
        en_file = EN_DIR / rel_path
        if not en_file.exists():
            warnings.append(f"[WARN] Orphan JA file (no EN source): docs/ja/{rel_path}")

    # === Report Results ===
    print()

    if warnings:
        print("=" * 60)
        print("WARNINGS:")
        print("=" * 60)
        for w in warnings:
            print(f"  {w}")
        print()

    if errors:
        print("=" * 60)
        print("ERRORS (CI will fail):")
        print("=" * 60)
        for e in errors:
            print(f"  {e}")
        print()

    # Summary
    print("=" * 60)
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")
    print("=" * 60)

    # Exit code
    if errors:
        print("\ni18n lint FAILED")
        sys.exit(1)

    if args.strict and warnings:
        print("\ni18n lint FAILED (--strict mode)")
        sys.exit(1)

    print("\ni18n lint OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
