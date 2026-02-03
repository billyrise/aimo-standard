#!/usr/bin/env python3
"""
Translation synchronization tool for AIMO Standard multilingual documentation.

This tool implements "Translation Freshness Tracking" to maintain consistency
between English (source) and translated content.

Features:
- Check translation freshness (compare EN hash vs recorded source_hash)
- Initialize new language folders
- Update translation metadata
- Generate translation reports

Usage:
    python tooling/i18n/sync_translations.py --check           # Check all translations
    python tooling/i18n/sync_translations.py --check --lang ja # Check specific language
    python tooling/i18n/sync_translations.py --report          # Generate coverage report
    python tooling/i18n/sync_translations.py --init-lang es    # Initialize new language
    python tooling/i18n/sync_translations.py --update-meta FILE # Update file metadata
"""

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
EN_DIR = DOCS / "en"

# All supported languages (excluding EN which is source)
SUPPORTED_LANGUAGES = {
    "ja": "日本語",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "pt": "Português",
    "it": "Italiano",
    "zh": "简体中文",
    "zh-TW": "繁體中文",
    "ko": "한국어",
}

# Translation priority tiers
TIER1_CRITICAL = [
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
    "standard/current/08-changelog.md",
    "governance/index.md",
    "releases/index.md",
]

TIER2_HIGH = [
    "coverage-map/index.md",
    "coverage-map/methodology.md",
    "artifacts/index.md",
    "artifacts/evidence-bundle.md",
    "artifacts/minimum-evidence.md",
    "validator/index.md",
    "conformance/index.md",
]

# Regex for extracting frontmatter
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SOURCE_HASH_RE = re.compile(r"^source_hash:\s*(.+)$", re.MULTILINE)
TRANSLATION_STATUS_RE = re.compile(r"^translation_status:\s*(.+)$", re.MULTILINE)


@dataclass
class TranslationStatus:
    """Status of a single translated file."""
    file_path: Path
    lang: str
    relative_path: str
    exists: bool
    has_metadata: bool
    source_hash_recorded: str | None
    source_hash_current: str | None
    is_fresh: bool
    translation_status: str


def compute_content_hash(content: str) -> str:
    """Compute SHA256 hash of content (excluding frontmatter for comparison)."""
    # Remove frontmatter for hashing
    match = FRONTMATTER_RE.match(content)
    if match:
        content_body = content[match.end():]
    else:
        content_body = content
    return hashlib.sha256(content_body.strip().encode("utf-8")).hexdigest()[:16]


def get_git_commit_hash(file_path: Path) -> str | None:
    """Get the latest Git commit hash for a file."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%h", "--", str(file_path)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def extract_frontmatter_value(content: str, pattern: re.Pattern) -> str | None:
    """Extract a value from frontmatter using a regex pattern."""
    match = FRONTMATTER_RE.match(content)
    if match:
        frontmatter = match.group(1)
        value_match = pattern.search(frontmatter)
        if value_match:
            return value_match.group(1).strip()
    return None


def check_translation_freshness(
    en_file: Path, translated_file: Path, lang: str
) -> TranslationStatus:
    """Check if a translation is up-to-date with its English source."""
    relative_path = str(en_file.relative_to(EN_DIR))
    
    # Check if translation exists
    if not translated_file.exists():
        return TranslationStatus(
            file_path=translated_file,
            lang=lang,
            relative_path=relative_path,
            exists=False,
            has_metadata=False,
            source_hash_recorded=None,
            source_hash_current=None,
            is_fresh=False,
            translation_status="missing",
        )
    
    # Read files
    en_content = en_file.read_text(encoding="utf-8")
    trans_content = translated_file.read_text(encoding="utf-8")
    
    # Compute current EN hash
    current_hash = compute_content_hash(en_content)
    
    # Extract recorded hash from translation
    recorded_hash = extract_frontmatter_value(trans_content, SOURCE_HASH_RE)
    trans_status = extract_frontmatter_value(trans_content, TRANSLATION_STATUS_RE)
    
    has_metadata = recorded_hash is not None
    is_fresh = recorded_hash == current_hash if recorded_hash else False
    
    return TranslationStatus(
        file_path=translated_file,
        lang=lang,
        relative_path=relative_path,
        exists=True,
        has_metadata=has_metadata,
        source_hash_recorded=recorded_hash,
        source_hash_current=current_hash,
        is_fresh=is_fresh,
        translation_status=trans_status or "unknown",
    )


def check_all_translations(lang: str | None = None) -> dict[str, list[TranslationStatus]]:
    """Check translation freshness for all languages or a specific one."""
    results: dict[str, list[TranslationStatus]] = {}
    
    languages = [lang] if lang else list(SUPPORTED_LANGUAGES.keys())
    
    for check_lang in languages:
        lang_dir = DOCS / check_lang
        if not lang_dir.exists():
            print(f"Warning: Language directory not found: {lang_dir}")
            continue
        
        results[check_lang] = []
        
        # Check all EN files
        for en_file in sorted(EN_DIR.rglob("*.md")):
            relative_path = en_file.relative_to(EN_DIR)
            translated_file = lang_dir / relative_path
            
            status = check_translation_freshness(en_file, translated_file, check_lang)
            results[check_lang].append(status)
    
    return results


def generate_report(results: dict[str, list[TranslationStatus]]) -> str:
    """Generate a translation coverage report."""
    lines = [
        "# Translation Coverage Report",
        f"Generated: {date.today().isoformat()}",
        "",
    ]
    
    for lang, statuses in results.items():
        lang_name = SUPPORTED_LANGUAGES.get(lang, lang)
        
        total = len(statuses)
        exists = sum(1 for s in statuses if s.exists)
        fresh = sum(1 for s in statuses if s.is_fresh)
        outdated = sum(1 for s in statuses if s.exists and not s.is_fresh)
        missing = total - exists
        
        lines.append(f"## {lang_name} ({lang})")
        lines.append("")
        lines.append(f"| Metric | Count | Percentage |")
        lines.append(f"|--------|-------|------------|")
        lines.append(f"| Total files | {total} | 100% |")
        lines.append(f"| Translated | {exists} | {exists*100//total}% |")
        lines.append(f"| Fresh | {fresh} | {fresh*100//total}% |")
        lines.append(f"| Outdated | {outdated} | {outdated*100//total}% |")
        lines.append(f"| Missing | {missing} | {missing*100//total}% |")
        lines.append("")
        
        # List Tier 1 status
        lines.append("### Tier 1 (Critical) Status")
        lines.append("")
        lines.append("| File | Status |")
        lines.append("|------|--------|")
        
        for page in TIER1_CRITICAL:
            status = next((s for s in statuses if s.relative_path == page), None)
            if status:
                if not status.exists:
                    icon = "❌ Missing"
                elif status.is_fresh:
                    icon = "✅ Fresh"
                else:
                    icon = "⚠ Outdated"
                lines.append(f"| `{page}` | {icon} |")
        
        lines.append("")
        
        # List outdated files
        outdated_files = [s for s in statuses if s.exists and not s.is_fresh]
        if outdated_files:
            lines.append("### Outdated Translations")
            lines.append("")
            for s in outdated_files[:20]:  # Limit to 20
                lines.append(f"- `{s.relative_path}`")
            if len(outdated_files) > 20:
                lines.append(f"- ... and {len(outdated_files) - 20} more")
            lines.append("")
    
    return "\n".join(lines)


def init_language(lang: str) -> int:
    """Initialize a new language by copying EN files."""
    lang_name = SUPPORTED_LANGUAGES.get(lang, lang)
    lang_dir = DOCS / lang
    
    if lang_dir.exists():
        print(f"Error: Language directory already exists: {lang_dir}")
        return 1
    
    print(f"Initializing {lang_name} ({lang})...")
    
    # Copy EN directory
    shutil.copytree(EN_DIR, lang_dir)
    
    # Add translation metadata to each file
    files_updated = 0
    for md_file in lang_dir.rglob("*.md"):
        relative_path = md_file.relative_to(lang_dir)
        en_file = EN_DIR / relative_path
        
        if not en_file.exists():
            continue
        
        en_content = en_file.read_text(encoding="utf-8")
        content_hash = compute_content_hash(en_content)
        
        # Read current content
        content = md_file.read_text(encoding="utf-8")
        
        # Check if has frontmatter
        match = FRONTMATTER_RE.match(content)
        
        translation_metadata = f"""# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/{relative_path}
source_hash: {content_hash}
translation_date: {date.today().isoformat()}
translator: pending
translation_status: needs_translation"""
        
        if match:
            # Insert after existing frontmatter description
            existing_fm = match.group(1)
            new_fm = existing_fm + "\n" + translation_metadata
            new_content = f"---\n{new_fm}\n---\n" + content[match.end():]
        else:
            # Add new frontmatter
            new_content = f"---\n{translation_metadata}\n---\n\n" + content
        
        md_file.write_text(new_content, encoding="utf-8")
        files_updated += 1
    
    print(f"✓ Created {lang_dir.relative_to(ROOT)}")
    print(f"✓ Added translation metadata to {files_updated} files")
    print(f"\nNext steps:")
    print(f"1. Update mkdocs.yml to add '{lang}' locale")
    print(f"2. Translate files in docs/{lang}/")
    print(f"3. Run: python tooling/i18n/sync_translations.py --check --lang {lang}")
    
    return 0


def update_metadata(file_path: Path) -> int:
    """Update translation metadata for a file."""
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return 1
    
    # Determine language from path
    rel_to_docs = file_path.relative_to(DOCS)
    lang = rel_to_docs.parts[0]
    
    if lang == "en":
        print("Error: Cannot update metadata for English source files")
        return 1
    
    if lang not in SUPPORTED_LANGUAGES and lang not in ["zh-Hans", "zh-Hant"]:
        print(f"Error: Unknown language: {lang}")
        return 1
    
    # Find corresponding EN file
    relative_path = Path(*rel_to_docs.parts[1:])
    en_file = EN_DIR / relative_path
    
    if not en_file.exists():
        print(f"Error: English source not found: {en_file}")
        return 1
    
    # Compute EN hash
    en_content = en_file.read_text(encoding="utf-8")
    content_hash = compute_content_hash(en_content)
    git_hash = get_git_commit_hash(en_file) or "unknown"
    
    # Update translation file
    content = file_path.read_text(encoding="utf-8")
    
    # Update or add metadata
    new_metadata = {
        "source_hash": content_hash,
        "source_commit": git_hash,
        "translation_date": date.today().isoformat(),
        "translation_status": "current",
    }
    
    match = FRONTMATTER_RE.match(content)
    if match:
        fm = match.group(1)
        for key, value in new_metadata.items():
            pattern = re.compile(rf"^{key}:\s*.*$", re.MULTILINE)
            if pattern.search(fm):
                fm = pattern.sub(f"{key}: {value}", fm)
            else:
                fm += f"\n{key}: {value}"
        new_content = f"---\n{fm}\n---\n" + content[match.end():]
    else:
        fm_lines = [f"{k}: {v}" for k, v in new_metadata.items()]
        new_content = "---\n" + "\n".join(fm_lines) + "\n---\n\n" + content
    
    file_path.write_text(new_content, encoding="utf-8")
    print(f"✓ Updated metadata: {file_path.relative_to(ROOT)}")
    print(f"  source_hash: {content_hash}")
    print(f"  translation_status: current")
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Translation synchronization tool for AIMO Standard"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check translation freshness",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate translation coverage report",
    )
    parser.add_argument(
        "--init-lang",
        metavar="LANG",
        help="Initialize new language folder (e.g., es, fr, de)",
    )
    parser.add_argument(
        "--update-meta",
        metavar="FILE",
        type=Path,
        help="Update translation metadata for a file",
    )
    parser.add_argument(
        "--lang",
        metavar="LANG",
        help="Specific language to check (used with --check)",
    )
    args = parser.parse_args()
    
    if args.init_lang:
        return init_language(args.init_lang)
    
    if args.update_meta:
        return update_metadata(args.update_meta)
    
    if args.check or args.report:
        results = check_all_translations(args.lang)
        
        if not results:
            print("No languages to check")
            return 1
        
        if args.report:
            report = generate_report(results)
            print(report)
            return 0
        
        # Check mode - print summary
        total_outdated = 0
        total_missing = 0
        
        print("=" * 60)
        print("Translation Freshness Check")
        print("=" * 60)
        
        for lang, statuses in results.items():
            lang_name = SUPPORTED_LANGUAGES.get(lang, lang)
            outdated = [s for s in statuses if s.exists and not s.is_fresh]
            missing = [s for s in statuses if not s.exists]
            
            print(f"\n{lang_name} ({lang}):")
            print(f"  Total files: {len(statuses)}")
            print(f"  Fresh: {sum(1 for s in statuses if s.is_fresh)}")
            print(f"  Outdated: {len(outdated)}")
            print(f"  Missing: {len(missing)}")
            
            total_outdated += len(outdated)
            total_missing += len(missing)
            
            # Show first few outdated
            if outdated:
                print("  Outdated files (first 5):")
                for s in outdated[:5]:
                    print(f"    - {s.relative_path}")
        
        print("\n" + "=" * 60)
        print(f"Summary: {total_outdated} outdated, {total_missing} missing")
        print("=" * 60)
        
        # Return non-zero if there are critical issues (missing Tier 1)
        for lang, statuses in results.items():
            for page in TIER1_CRITICAL:
                status = next((s for s in statuses if s.relative_path == page), None)
                if status and not status.exists:
                    print(f"\nWarning: Critical page missing: {lang}/{page}")
        
        return 0
    
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
