#!/usr/bin/env python3
"""
Lint for hidden / bidirectional Unicode (GitHub warning parity and hardening).

Detects characters that trigger GitHub "hidden or bidirectional Unicode text" warnings
and additional problematic characters for audit/security:

- Bidirectional control: U+200E, U+200F, U+202A–U+202E, U+2066–U+2069
- Zero-width / invisible: U+200B, U+200C, U+200D, U+2060, U+FEFF (BOM)
- Unicode category Cf (Format)
- Unicode category Cc (Control), except \\t \\n \\r
- Non-ASCII whitespace: isspace() but not in [' ', '\\t', '\\n', '\\r']
- Variation selectors: U+FE00–U+FE0F

Exit codes:
- 0: No hidden/bidi characters found
- 1: One or more found; prints file:line:col U+XXXX and exits 1
"""

import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Bidi control codepoints
BIDI = {0x200E, 0x200F, *range(0x202A, 0x202F), *range(0x2066, 0x206A)}
# Zero-width / invisible
ZERO_WIDTH = {0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF}
# Variation selectors
VARIATION = set(range(0xFE00, 0xFE10))
ALLOWED_WS = {" ", "\t", "\n", "\r"}

SKIP_DIRS = {".venv", "venv", "site", ".git", "node_modules", "__pycache__", ".mypy_cache"}
SCAN_EXTENSIONS = {".md", ".yml", ".yaml", ".json", ".py", ".txt", ".html", ".cff", ".sh"}


def is_problem(c: str) -> tuple[bool, str]:
    """Return (is_problem, reason)."""
    cp = ord(c)
    if cp in BIDI:
        return True, "bidi"
    if cp in ZERO_WIDTH:
        return True, "zero-width/invisible"
    if cp in VARIATION:
        return True, "variation-selector"
    try:
        cat = unicodedata.category(c)
    except Exception:
        return False, ""
    if cat == "Cf":
        return True, "Cf"
    if cat == "Cc":
        return True, "Cc"
    if c.isspace() and c not in ALLOWED_WS:
        return True, "non-ASCII-whitespace"
    return False, ""


def scan_file(filepath: Path, content: str) -> list[tuple[int, int, str, str, str]]:
    """Return list of (line_1based, col_1based, char, reason, name)."""
    hits = []
    for line_num, line in enumerate(content.splitlines(), start=1):
        for col, c in enumerate(line):
            ok, reason = is_problem(c)
            if ok:
                try:
                    name = unicodedata.name(c)
                except ValueError:
                    name = "?"
                hits.append((line_num, col + 1, c, reason, name))
    return hits


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=False,
    )
    if result.returncode != 0:
        print("lint_hidden_unicode: git ls-files failed", file=sys.stderr)
        return 1
    paths = [
        ROOT / p
        for p in result.stdout.decode("utf-8").strip("\0").split("\0")
        if p
    ]
    errors = []
    for path in paths:
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix not in SCAN_EXTENSIONS:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_num, col, c, reason, name in scan_file(path, content):
            rel = path.relative_to(ROOT)
            errors.append(
                f"{rel}:{line_num}:{col} U+{ord(c):04X} {name} [{reason}]"
            )
    if errors:
        print(
            "lint_hidden_unicode: Hidden or bidirectional Unicode found (GitHub warning parity):",
            file=sys.stderr,
        )
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print("lint_hidden_unicode: OK (no hidden/bidi Unicode)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
