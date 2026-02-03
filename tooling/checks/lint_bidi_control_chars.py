#!/usr/bin/env python3
"""
Lint for Unicode Bidirectional (Bidi) control characters (Trojan Source hardening).

Detects characters that can be used to alter visual rendering and hide malicious code:
- U+202A–202E: LRE, RLE, PDF, LRO, RLO
- U+2066–2069: LRI, RLI, FSI, PDI
- U+200E, U+200F: LRM, RLM

Exit Codes:
- 0: No bidi control chars found
- 1: Bidi control char(s) found; prints file:line and exits 1

Usage:
    python tooling/checks/lint_bidi_control_chars.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Bidi control character ranges (Trojan Source)
# 202A-202E: LRE, RLE, PDF, LRO, RLO
# 2066-2069: LRI, RLI, FSI, PDI
# 200E, 200F: LRM, RLM
BIDI_RE = re.compile(r"[\u200E\u200F\u202A-\u202E\u2066-\u2069]")

# Directories to skip
SKIP_DIRS = {".venv", "venv", "site", ".git", "node_modules", "__pycache__", ".mypy_cache"}

# Extensions to scan (text assets)
SCAN_EXTENSIONS = {".md", ".yml", ".yaml", ".json", ".py", ".txt", ".html", ".cff", ".sh"}


def should_skip(path: Path) -> bool:
    if not path.is_file():
        return True
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    if path.suffix not in SCAN_EXTENSIONS:
        return True
    return False


def scan_file(filepath: Path) -> list[tuple[int, str]]:
    """Return list of (line_num, line_content) where bidi control char was found."""
    issues = []
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return issues
    for i, line in enumerate(content.splitlines(), start=1):
        if BIDI_RE.search(line):
            issues.append((i, line.strip()))
    return issues


def main() -> int:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if should_skip(path):
            continue
        rel = path.relative_to(ROOT)
        for line_num, line in scan_file(path):
            preview = (line[:72] + "...") if len(line) > 72 else line
            errors.append(f"{rel}:{line_num}: {preview}")

    if errors:
        print("lint_bidi_control_chars: Bidi control characters found (Trojan Source risk):", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print("lint_bidi_control_chars: OK (no bidi control characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
