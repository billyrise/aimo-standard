#!/usr/bin/env python3
"""Generate llms-full.txt for each language by concatenating all Markdown documentation pages.

The output files are placed in the docs language directories so MkDocs includes them
in the build (e.g., docs/llms-full.txt for English, docs/ja/llms-full.txt for Japanese).
The CI pipeline then copies them to the gh-pages root alongside robots.txt and sitemap.xml.

Usage:
    # Generate English full-text only (default)
    python tooling/build_llms_txt.py

    # Generate all language full-text files
    python tooling/build_llms_txt.py --all-langs

    # Generate a specific language
    python tooling/build_llms_txt.py --lang ja

    # Custom output path
    python tooling/build_llms_txt.py --lang en --output docs/llms-full.txt
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

LANGUAGES = {
    "en": {
        "source_dir": REPO_ROOT / "docs" / "en",
        "output": REPO_ROOT / "docs" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/",
        "label": "English",
    },
    "ja": {
        "source_dir": REPO_ROOT / "docs" / "ja",
        "output": REPO_ROOT / "docs" / "ja" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/ja/",
        "label": "Japanese / 日本語",
    },
    "es": {
        "source_dir": REPO_ROOT / "docs" / "es",
        "output": REPO_ROOT / "docs" / "es" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/es/",
        "label": "Spanish / Español",
    },
    "fr": {
        "source_dir": REPO_ROOT / "docs" / "fr",
        "output": REPO_ROOT / "docs" / "fr" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/fr/",
        "label": "French / Français",
    },
    "de": {
        "source_dir": REPO_ROOT / "docs" / "de",
        "output": REPO_ROOT / "docs" / "de" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/de/",
        "label": "German / Deutsch",
    },
    "pt": {
        "source_dir": REPO_ROOT / "docs" / "pt",
        "output": REPO_ROOT / "docs" / "pt" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/pt/",
        "label": "Portuguese / Português",
    },
    "it": {
        "source_dir": REPO_ROOT / "docs" / "it",
        "output": REPO_ROOT / "docs" / "it" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/it/",
        "label": "Italian / Italiano",
    },
    "zh": {
        "source_dir": REPO_ROOT / "docs" / "zh",
        "output": REPO_ROOT / "docs" / "zh" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/zh/",
        "label": "Simplified Chinese / 简体中文",
    },
    "zh-TW": {
        "source_dir": REPO_ROOT / "docs" / "zh-TW",
        "output": REPO_ROOT / "docs" / "zh-TW" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/zh-TW/",
        "label": "Traditional Chinese / 繁體中文",
    },
    "ko": {
        "source_dir": REPO_ROOT / "docs" / "ko",
        "output": REPO_ROOT / "docs" / "ko" / "llms-full.txt",
        "site_prefix": "https://standard.aimoaas.com/latest/ko/",
        "label": "Korean / 한국어",
    },
}

# Pages to skip — metadata or generated files that add noise but no semantic value
SKIP_PATTERNS = [
    r"^llms",          # avoid including the llms.txt / llms-full.txt themselves
    r"^versions/",     # auto-generated versions page
]

# Preferred page order: place these first when they exist
PAGE_ORDER_PREFIXES = [
    "index",
    "standard/index",
    "standard/current/index",
    "standard/current/01",
    "standard/current/02",
    "standard/current/03",
    "standard/current/04",
    "standard/current/05",
    "standard/current/06",
    "standard/current/07",
    "standard/current/08",
    "standard/current/09",
    "standard/current/10",
    "artifacts/",
    "coverage-map/",
    "conformance/",
    "validator/",
    "examples/",
    "governance/",
    "releases/",
]


def strip_front_matter(text: str) -> str:
    """Remove YAML front matter delimited by --- from the top of a Markdown file."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def strip_html_comments(text: str) -> str:
    """Remove HTML comments (including translation status markers)."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def clean_markdown(text: str) -> str:
    """Normalise whitespace: collapse 3+ blank lines into 2."""
    text = strip_front_matter(text)
    text = strip_html_comments(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def md_path_to_url_path(md_path: Path, source_dir: Path) -> str:
    """Convert a .md file path relative to source_dir into a URL path segment."""
    rel = md_path.relative_to(source_dir)
    parts = list(rel.parts)
    # Replace index.md with the directory path
    if parts[-1] == "index.md":
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1].removesuffix(".md") + "/"
    return "/".join(parts) + ("/" if parts and not parts[-1].endswith("/") else "")


def should_skip(rel_path: str) -> bool:
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, rel_path):
            return True
    return False


def sort_key(md_path: Path, source_dir: Path) -> tuple:
    rel = str(md_path.relative_to(source_dir)).replace("\\", "/")
    for i, prefix in enumerate(PAGE_ORDER_PREFIXES):
        if rel.startswith(prefix):
            return (i, rel)
    return (len(PAGE_ORDER_PREFIXES), rel)


def collect_markdown_files(source_dir: Path) -> list[Path]:
    if not source_dir.exists():
        return []
    files = [
        f for f in source_dir.rglob("*.md")
        if not should_skip(str(f.relative_to(source_dir)).replace("\\", "/"))
    ]
    return sorted(files, key=lambda f: sort_key(f, source_dir))


def build_llms_full(lang: str, output_override: Path | None = None) -> Path:
    cfg = LANGUAGES[lang]
    source_dir: Path = cfg["source_dir"]
    output: Path = output_override or cfg["output"]
    site_prefix: str = cfg["site_prefix"]
    label: str = cfg["label"]

    md_files = collect_markdown_files(source_dir)
    if not md_files:
        print(f"  WARNING: No Markdown files found in {source_dir}", file=sys.stderr)

    sections: list[str] = []

    header = (
        f"# AIMO Standard — Full Documentation ({label})\n"
        f"# Source: {site_prefix}\n"
        f"# License: Apache-2.0\n"
        f"# Generated: see tooling/build_llms_txt.py\n"
        f"# This file contains the complete text of all documentation pages for LLM ingestion.\n"
    )
    sections.append(header)

    for md_path in md_files:
        raw = md_path.read_text(encoding="utf-8")
        content = clean_markdown(raw)
        if not content:
            continue

        url_path = md_path_to_url_path(md_path, source_dir)
        page_url = site_prefix + url_path

        separator = f"\n\n---\n<!-- page: {page_url} -->\n\n"
        sections.append(separator + content)

    full_text = "\n".join(sections) + "\n"

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(full_text, encoding="utf-8")

    size_kb = output.stat().st_size / 1024
    print(f"  [{lang}] {len(md_files)} pages → {output} ({size_kb:.1f} KB)")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate llms-full.txt files from AIMO Standard Markdown documentation."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--all-langs",
        action="store_true",
        help="Generate llms-full.txt for all 10 supported languages.",
    )
    group.add_argument(
        "--lang",
        choices=list(LANGUAGES.keys()),
        default="en",
        help="Language code to generate (default: en).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Override output file path (only valid with --lang, not --all-langs).",
    )
    args = parser.parse_args()

    if args.all_langs:
        print("Generating llms-full.txt for all languages...")
        for lang in LANGUAGES:
            build_llms_full(lang)
    else:
        lang = args.lang
        print(f"Generating llms-full.txt for language: {lang}")
        build_llms_full(lang, output_override=args.output)

    print("Done.")


if __name__ == "__main__":
    main()
