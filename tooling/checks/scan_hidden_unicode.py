#!/usr/bin/env python3
"""
One-off scanner: list all hidden/bidi Unicode in git-tracked files.
Output: file:line:col U+XXXX name category bidi
Used to identify characters to remove for PR #8.
"""
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Bidi control
BIDI_CODEPOINTS = [
    0x200E, 0x200F,  # LRM, RLM
    *range(0x202A, 0x202F),  # LRE, RLE, PDF, LRO, RLO
    *range(0x2066, 0x206A),   # LRI, RLI, FSI, PDI
]
# Zero-width / invisible
ZERO_WIDTH = [0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF]
ALLOWED_WS = {" ", "\t", "\n", "\r"}


def is_problem(c: str) -> tuple[bool, str]:
    """Return (is_problem, reason)."""
    cp = ord(c)
    if cp in BIDI_CODEPOINTS or cp in ZERO_WIDTH:
        return True, "bidi/zw"
    try:
        cat = unicodedata.category(c)
    except Exception:
        return False, ""
    if cat == "Cf":
        return True, "Cf"
    if c.isspace() and c not in ALLOWED_WS:
        return True, "non-ASCII-whitespace"
    return False, ""


def scan_content(content: str) -> list[tuple[int, int, str, str]]:
    """Yield (line_1based, col_0based, char, reason)."""
    for line_num, line in enumerate(content.splitlines(), start=1):
        for col, c in enumerate(line):
            ok, reason = is_problem(c)
            if ok:
                yield (line_num, col, c, reason)


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=False,
    )
    if result.returncode != 0:
        print("git ls-files failed", file=sys.stderr)
        return 1
    paths = [Path(ROOT) / p for p in result.stdout.decode("utf-8").strip("\0").split("\0") if p]
    skip_dirs = {".venv", "venv", "site", ".git", "node_modules", "__pycache__", ".mypy_cache"}
    exts = {".md", ".yml", ".yaml", ".json", ".py", ".txt", ".html", ".cff", ".sh"}
    hits = []
    for path in paths:
        if not path.is_file():
            continue
        if any(part in skip_dirs for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix not in exts:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_num, col, c, reason in scan_content(content):
            rel = path.relative_to(ROOT)
            try:
                name = unicodedata.name(c)
            except ValueError:
                name = "?"
            cat = unicodedata.category(c)
            try:
                bidi = unicodedata.bidirectional(c)
            except Exception:
                bidi = "?"
            hits.append((str(rel), line_num, col + 1, c, reason, name, cat, bidi))
    for rel, line, col, c, reason, name, cat, bidi in hits:
        print(f"{rel}:{line}:{col} U+{ord(c):04X} {name} {cat} {bidi} [{reason}]")
    return 0 if not hits else 1


if __name__ == "__main__":
    sys.exit(main())
