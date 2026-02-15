#!/usr/bin/env python3
"""
Add hidden translation_status marker to all doc pages.
Marker: <!-- aimo:translation_status=source|translated|untranslated -->
Placed immediately after frontmatter (after closing ---) for machine-detectable status.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
EN_DIR = DOCS / "en"

LANGUAGES = ["ja", "zh", "zh-TW", "ko", "de", "es", "fr", "pt", "it"]

MARKER_SOURCE = "<!-- aimo:translation_status=source -->"
MARKER_TRANSLATED = "<!-- aimo:translation_status=translated -->"
MARKER_UNTRANSLATED = "<!-- aimo:translation_status=untranslated -->"
MARKER_RE = re.compile(r"<!--\s*aimo:translation_status=(?:source|translated|untranslated)\s*-->")

def get_body_and_frontmatter(content: str):
    """Return (frontmatter_block, body) or (None, content)."""
    match = re.match(r"^(---\r?\n.*?\r?\n---\r?\n)(.*)$", content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def first_content_line(body: str) -> str:
    """First non-empty line of body (often # Title)."""
    for line in body.splitlines():
        s = line.strip()
        if s:
            return s
    return ""

def is_likely_english(text: str) -> bool:
    """Heuristic: if most of the first line is ASCII/Latin, treat as English."""
    if not text:
        return True
    ascii_count = sum(1 for c in text if ord(c) < 128)
    return ascii_count >= 0.7 * len(text)

def body_looks_same_as_en(lang_body: str, en_body: str, strict: bool = False, full_body: bool = False) -> bool:
    """True if content looks like untranslated copy of EN.
    Default: first content line identical.
    strict=True: first 400 chars of body (after stripping marker) identical.
    full_body=True: entire body (after stripping marker) identical."""
    lang_clean = MARKER_RE.sub("", lang_body).strip()
    en_clean = en_body.strip()
    if full_body:
        return lang_clean == en_clean and len(en_clean) >= 20
    if strict:
        return lang_clean[:400] == en_clean[:400] and len(en_clean) >= 50
    lang_first = first_content_line(lang_clean)
    en_first = first_content_line(en_clean)
    if not en_first:
        return False
    return lang_first == en_first

def ensure_marker_after_frontmatter(content: str, marker: str) -> str:
    """Ensure exactly one marker right after frontmatter; return new content."""
    fm, body = get_body_and_frontmatter(content)
    # Remove any existing marker from body
    body_clean = MARKER_RE.sub("", body).lstrip("\n")
    if fm:
        return fm + marker + "\n\n" + body_clean
    return marker + "\n\n" + body_clean

def main():
    import argparse as _argparse
    p = _argparse.ArgumentParser(description="Add aimo:translation_status markers and list untranslated")
    p.add_argument("--strict", action="store_true", help="Use strict comparison (first 400 chars) to detect untranslated")
    p.add_argument("--full-body", action="store_true", help="Treat as untranslated only when entire body equals EN (exact copy)")
    args = p.parse_args()
    strict = getattr(args, "strict", False)
    full_body = getattr(args, "full_body", False)

    en_files = sorted(EN_DIR.rglob("*.md"))
    rel_paths = [f.relative_to(EN_DIR) for f in en_files]

    # 1) Add source marker to all EN files
    for f in en_files:
        content = f.read_text(encoding="utf-8")
        if MARKER_SOURCE not in content and not MARKER_RE.search(content):
            new_content = ensure_marker_after_frontmatter(content, MARKER_SOURCE)
            f.write_text(new_content, encoding="utf-8")
            print(f"EN: {f.relative_to(ROOT)} -> source")

    # 2) For each language, add translated/untranslated marker and list untranslated
    untranslated_list = []
    for lang in LANGUAGES:
        lang_dir = DOCS / lang
        if not lang_dir.exists():
            continue
        for rel in rel_paths:
            en_path = EN_DIR / rel
            lang_path = lang_dir / rel
            if not lang_path.exists():
                continue
            en_content = en_path.read_text(encoding="utf-8")
            lang_content = lang_path.read_text(encoding="utf-8")
            _, en_body = get_body_and_frontmatter(en_content)
            _, lang_body = get_body_and_frontmatter(lang_content)

            if body_looks_same_as_en(lang_body, en_body, strict=strict, full_body=full_body):
                marker = MARKER_UNTRANSLATED
                untranslated_list.append((lang, str(rel)))
            else:
                marker = MARKER_TRANSLATED

            # Always ensure correct marker (so --strict re-run can fix translated -> untranslated)
            new_content = ensure_marker_after_frontmatter(lang_content, marker)
            if new_content != lang_content:
                lang_path.write_text(new_content, encoding="utf-8")
            status = "untranslated" if marker == MARKER_UNTRANSLATED else "translated"
            if marker == MARKER_UNTRANSLATED:
                print(f"{lang}: {rel} -> {status}")

    # Output untranslated list for follow-up translation
    out_file = ROOT / "tooling" / "i18n" / "untranslated_pages.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        for lang, rel in sorted(untranslated_list):
            f.write(f"{lang}\t{rel}\n")
    print(f"\nWrote {len(untranslated_list)} untranslated (lang, path) to {out_file}")

if __name__ == "__main__":
    main()
