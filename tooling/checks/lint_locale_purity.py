#!/usr/bin/env python3
"""
EN locale purity lint: ensure docs/en/**/*.md contain no CJK outside code blocks.

Quality Gate:
- Target: docs/en/**/*.md
- Rule: CJK characters (Hiragana, Katakana, CJK Unified Ideographs, Hangul) are errors
- Exclusions: Content inside fenced code blocks (``` ... ```) is skipped
- Optional: File-level or line-level allowlist for documented exceptions

Exit Codes:
- 0: No CJK in EN docs (or only in code blocks / allowlisted)
- 1: CJK detected; prints file:line and exits 1

Usage:
    python tooling/checks/lint_locale_purity.py
    python tooling/checks/lint_locale_purity.py --allowlist docs/en/contributing/localization.md  # (example; prefer fixing content)
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EN_DOCS = ROOT / "docs" / "en"

# CJK character ranges (same as lint_i18n for consistency)
# Hiragana U+3040-U+309F, Katakana U+30A0-U+30FF, CJK Unified U+4E00-U+9FFF, Hangul U+AC00-U+D7AF
CJK_RE = re.compile(r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]")
CODE_FENCE_RE = re.compile(r"^```")


def is_in_code_block(lines: list[str], line_idx: int) -> bool:
    """True if line at line_idx is inside a fenced code block."""
    fence_count = 0
    for i in range(line_idx):
        if CODE_FENCE_RE.match(lines[i].strip()):
            fence_count += 1
    return fence_count % 2 == 1


def scan_file(filepath: Path, allowlist_files: set[Path]) -> list[tuple[int, str]]:
    """
    Scan a single file for CJK outside code blocks.
    Returns list of (line_num, line_content) where CJK was found.
    """
    if allowlist_files and filepath.resolve() in allowlist_files:
        return []
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError:
        return []
    lines = content.splitlines()
    issues = []
    for i, line in enumerate(lines):
        if is_in_code_block(lines, i):
            continue
        # Strip inline code (backticks) before checking, so `Japanese (日本語)` in docs is still reported
        line_without_inline_code = re.sub(r"`[^`]*`", "", line)
        if CJK_RE.search(line_without_inline_code):
            issues.append((i + 1, line.strip()))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint docs/en for CJK; EN pages must be English-only (code blocks excluded)."
    )
    parser.add_argument(
        "--allowlist",
        action="append",
        default=[],
        metavar="FILE",
        help="File path (relative to repo root) to allowlist; can be repeated.",
    )
    parser.add_argument(
        "--list-files",
        action="store_true",
        help="List scanned files and exit.",
    )
    args = parser.parse_args()

    allowlist_set: set[Path] = set()
    for raw in args.allowlist:
        p = (ROOT / raw).resolve()
        if p.exists():
            allowlist_set.add(p)

    md_files = sorted(EN_DOCS.rglob("*.md"))
    if args.list_files:
        for f in md_files:
            print(f.relative_to(ROOT))
        return 0

    errors: list[str] = []
    for f in md_files:
        rel = f.relative_to(ROOT)
        for line_num, line in scan_file(f, allowlist_set):
            preview = (line[:72] + "...") if len(line) > 72 else line
            errors.append(f"{rel}:{line_num}: {preview}")

    if errors:
        print("lint_locale_purity: CJK found in docs/en (EN must be English-only):", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print("lint_locale_purity: OK (no CJK in docs/en outside code blocks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
