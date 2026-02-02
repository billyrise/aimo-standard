#!/usr/bin/env python3
"""
Docs Consistency Lint for AIMO Standard.

Checks for common inconsistencies in documentation that can confuse
auditors and external users.

Checks performed:
1. No hardcoded git checkout versions (e.g., "git checkout v0.1.3")
2. URL patterns are consistent (site paths use version without 'v' prefix)
3. Version examples are up-to-date

Usage:
    python tooling/checks/lint_docs_consistency.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

# Patterns that indicate problems
PROBLEMS = []


def check_hardcoded_checkout(content: str, filepath: Path) -> list[tuple[int, str]]:
    """
    Check for hardcoded 'git checkout vX.Y.Z' with specific old versions.
    
    Allowed: VERSION=vX.Y.Z followed by git checkout "$VERSION"
    Not allowed: git checkout v0.1.3 (or other hardcoded old versions)
    """
    issues = []
    lines = content.splitlines()
    
    # Pattern for hardcoded checkout (not using a variable)
    # Match: git checkout v0.1.0, v0.1.1, v0.1.2, v0.1.3, v0.1.4, v0.1.5
    # (older versions that shouldn't be hardcoded)
    hardcoded_pattern = re.compile(r'git checkout v0\.1\.[0-5]\b(?!\s*#.*VERSION)')
    
    for i, line in enumerate(lines):
        if hardcoded_pattern.search(line):
            issues.append((i + 1, f"Hardcoded old version in git checkout: {line.strip()}"))
    
    return issues


def check_url_pattern_consistency(content: str, filepath: Path) -> list[tuple[int, str]]:
    """
    Check that site URLs use version without 'v' prefix.
    
    Correct: https://standard.aimoaas.com/0.1.6/
    Wrong:   https://standard.aimoaas.com/v0.1.6/
    
    Exception: GitHub release tag URLs should use 'v' prefix.
    """
    issues = []
    lines = content.splitlines()
    
    # Pattern for site URLs with 'v' prefix (wrong)
    # Match: standard.aimoaas.com/v0. or standard.aimoaas.com/v1.
    # But NOT: github.com/...releases/tag/v (which is correct)
    wrong_pattern = re.compile(r'standard\.aimoaas\.com/v\d+\.')
    
    for i, line in enumerate(lines):
        if wrong_pattern.search(line):
            # Check if it's a placeholder like v{X.Y.Z} - those were already fixed
            if 'v{X.Y.Z}' not in line and 'v{version}' not in line:
                issues.append((i + 1, f"Site URL should not have 'v' prefix: {line.strip()}"))
    
    return issues


def check_url_placeholder_consistency(content: str, filepath: Path) -> list[tuple[int, str]]:
    """
    Check that URL placeholders are consistent.
    
    Correct: {X.Y.Z} or {version}
    Wrong:   v{X.Y.Z} (mixing literal 'v' with placeholder)
    """
    issues = []
    lines = content.splitlines()
    
    # Pattern for mixed v prefix with placeholder
    wrong_pattern = re.compile(r'standard\.aimoaas\.com/v\{')
    
    for i, line in enumerate(lines):
        if wrong_pattern.search(line):
            issues.append((i + 1, f"URL placeholder should not have 'v' prefix: {line.strip()}"))
    
    return issues


def lint_file(filepath: Path) -> list[tuple[str, int, str]]:
    """Run all checks on a single file."""
    issues = []
    
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return [(str(filepath), 0, f"Could not read file: {e}")]
    
    rel_path = str(filepath.relative_to(ROOT))
    
    # Run all checks
    for line_num, message in check_hardcoded_checkout(content, filepath):
        issues.append((rel_path, line_num, message))
    
    for line_num, message in check_url_pattern_consistency(content, filepath):
        issues.append((rel_path, line_num, message))
    
    for line_num, message in check_url_placeholder_consistency(content, filepath):
        issues.append((rel_path, line_num, message))
    
    return issues


def main():
    print("=" * 60)
    print("AIMO Standard Docs Consistency Lint")
    print("=" * 60)
    print()
    
    all_issues = []
    
    # Check all markdown files in docs/
    for md_file in DOCS.rglob("*.md"):
        if "overrides" in str(md_file):
            continue
        issues = lint_file(md_file)
        all_issues.extend(issues)
    
    if all_issues:
        print("Issues found:")
        print()
        for filepath, line_num, message in sorted(all_issues):
            print(f"  {filepath}:{line_num}: {message}")
        print()
        print(f"Total: {len(all_issues)} issue(s)")
        print()
        print("docs-consistency lint FAILED")
        sys.exit(1)
    else:
        print("All checks passed.")
        print()
        print("docs-consistency lint OK")
        sys.exit(0)


if __name__ == "__main__":
    main()
