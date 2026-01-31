#!/usr/bin/env python3
"""
Build release assets for AIMO Standard.

Produces:
  - dist/trust_package.pdf (EN)
  - dist/trust_package.ja.pdf (JA, optional)
  - dist/aimo-standard-artifacts.zip
  - dist/SHA256SUMS.txt

Usage:
  python tooling/release/build_assets.py [--version X.Y.Z] [--ja]

Requirements:
  - weasyprint (pip install weasyprint)
  - markdown (pip install markdown)
  - jinja2 (pip install jinja2)
  - System: pango, cairo, gdk-pixbuf (for weasyprint)
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

# Ensure we run from repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(REPO_ROOT)

DIST_DIR = REPO_ROOT / "dist"

# Files to include in the artifacts zip
# Taxonomy/Dictionary SSOT files (for internal checksum generation)
TAXONOMY_SSOT_PATHS = [
    "source_pack/03_taxonomy/taxonomy_dictionary_v0.1.csv",
    "source_pack/03_taxonomy/taxonomy_dictionary.json",
    "source_pack/03_taxonomy/dictionary_seed.csv",
    "source_pack/03_taxonomy/taxonomy_en.yaml",
    "source_pack/03_taxonomy/taxonomy_ja.yaml",
    "source_pack/03_taxonomy/code_system.csv",
    "source_pack/03_taxonomy/dimensions_en_ja.md",
    "source_pack/03_taxonomy/taxonomy_pack_v0.1.json",
    "source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json",
]

ARTIFACT_PATHS = [
    # Schemas
    "schemas/jsonschema/aimo-dictionary.schema.json",
    "schemas/jsonschema/aimo-ev.schema.json",
    "schemas/jsonschema/aimo-standard.schema.json",
    # Taxonomy (SSOT and derived) - referenced from TAXONOMY_SSOT_PATHS
    *TAXONOMY_SSOT_PATHS,
    # Templates
    "templates/ev/ev_template.json",
    "templates/ev/ev_template.md",
    # Examples
    "examples/minimal/sample_dictionary.json",
    "examples/minimal/sample_ev.json",
    "examples/evidence_bundle_minimal/dictionary.json",
    "examples/evidence_bundle_minimal/root.json",
    "examples/evidence_bundle_minimal/README.md",
    # Coverage map
    "coverage_map/coverage_map.yaml",
    # Validator
    "validator/rules/checks.yaml",
    "validator/rules/checks.md",
    # Governance
    "VERSIONING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "LICENSE.txt",
    "NOTICE.txt",
    "TRADEMARKS.md",
]

# Trust Package pages to include in PDF (in order)
TRUST_PACKAGE_PAGES_EN = [
    "docs/governance/trust-package.md",
    "docs/governance/responsibility-boundary.md",
    "docs/artifacts/evidence-bundle.md",
    "docs/artifacts/minimum-evidence.md",
    "docs/coverage-map/methodology.md",
    "docs/coverage-map/iso-42001.md",
    "docs/coverage-map/nist-ai-rmf.md",
    "docs/coverage-map/eu-ai-act.md",
    "docs/coverage-map/isms.md",
    "docs/releases/index.md",
]

TRUST_PACKAGE_PAGES_JA = [
    "docs/governance/trust-package.ja.md",
    "docs/governance/responsibility-boundary.ja.md",
    "docs/artifacts/evidence-bundle.ja.md",
    "docs/artifacts/minimum-evidence.ja.md",
    "docs/coverage-map/methodology.ja.md",
    "docs/coverage-map/iso-42001.ja.md",
    "docs/coverage-map/nist-ai-rmf.ja.md",
    "docs/coverage-map/eu-ai-act.ja.md",
    "docs/coverage-map/isms.ja.md",
    "docs/releases/index.ja.md",
]

PDF_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>AIMO Standard - Trust Package{lang_suffix}</title>
  <style>
    @page {{
      size: A4;
      margin: 2cm;
      @top-center {{
        content: "AIMO Standard - Trust Package";
        font-size: 10pt;
        color: #666;
      }}
      @bottom-center {{
        content: "Page " counter(page) " of " counter(pages);
        font-size: 10pt;
        color: #666;
      }}
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 11pt;
      line-height: 1.6;
      color: #333;
      max-width: 100%;
    }}
    h1 {{
      font-size: 24pt;
      color: #1a1a2e;
      border-bottom: 2px solid #4361ee;
      padding-bottom: 0.5em;
      page-break-after: avoid;
    }}
    h2 {{
      font-size: 18pt;
      color: #1a1a2e;
      margin-top: 1.5em;
      page-break-after: avoid;
    }}
    h3 {{
      font-size: 14pt;
      color: #333;
      page-break-after: avoid;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 1em 0;
      font-size: 10pt;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }}
    th {{
      background-color: #f5f5f5;
      font-weight: bold;
    }}
    tr:nth-child(even) {{
      background-color: #fafafa;
    }}
    code {{
      background-color: #f5f5f5;
      padding: 2px 6px;
      border-radius: 3px;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 10pt;
    }}
    pre {{
      background-color: #f5f5f5;
      padding: 1em;
      border-radius: 5px;
      overflow-x: auto;
      font-size: 9pt;
    }}
    pre code {{
      padding: 0;
      background: none;
    }}
    a {{
      color: #4361ee;
      text-decoration: none;
    }}
    blockquote {{
      border-left: 4px solid #4361ee;
      margin: 1em 0;
      padding-left: 1em;
      color: #666;
    }}
    .cover-page {{
      text-align: center;
      padding-top: 30%;
    }}
    .cover-page h1 {{
      font-size: 36pt;
      border: none;
    }}
    .cover-page .version {{
      font-size: 18pt;
      color: #666;
      margin-top: 2em;
    }}
    .cover-page .date {{
      font-size: 14pt;
      color: #888;
      margin-top: 1em;
    }}
    .section-break {{
      page-break-before: always;
    }}
    hr {{
      border: none;
      border-top: 1px solid #ddd;
      margin: 2em 0;
    }}
  </style>
</head>
<body>
  <div class="cover-page">
    <h1>AIMO Standard</h1>
    <p style="font-size: 24pt; color: #4361ee;">Trust Package</p>
    <p class="version">Version: {version}</p>
    <p class="date">Generated: {date}</p>
    <p style="margin-top: 3em; font-size: 12pt; color: #888;">
      Auditor-Ready Assurance Materials
    </p>
  </div>
  <div class="section-break"></div>
  {content}
</body>
</html>
"""


def sha256_file(filepath: Path) -> str:
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def render_markdown_to_html(md_files: list[Path], lang: str = "en") -> str:
    """Render multiple markdown files to HTML content."""
    import markdown
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.toc import TocExtension

    md = markdown.Markdown(
        extensions=[
            TableExtension(),
            FencedCodeExtension(),
            TocExtension(permalink=False),
            "md_in_html",
        ]
    )

    html_parts = []
    for i, md_file in enumerate(md_files):
        if not md_file.exists():
            print(f"Warning: {md_file} not found, skipping", file=sys.stderr)
            continue

        content = md_file.read_text(encoding="utf-8")

        # Convert relative links to text (they won't work in PDF)
        # Keep the link text but remove the link
        import re

        content = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", content)

        html = md.convert(content)
        md.reset()

        if i > 0:
            html = f'<div class="section-break"></div>\n{html}'

        html_parts.append(html)

    return "\n".join(html_parts)


def build_pdf(version: str, lang: str = "en") -> Path:
    """Build Trust Package PDF."""
    from weasyprint import HTML

    pages = TRUST_PACKAGE_PAGES_EN if lang == "en" else TRUST_PACKAGE_PAGES_JA
    md_files = [REPO_ROOT / p for p in pages]

    content = render_markdown_to_html(md_files, lang)

    lang_suffix = " (日本語)" if lang == "ja" else ""
    html_content = PDF_HTML_TEMPLATE.format(
        lang=lang,
        lang_suffix=lang_suffix,
        version=version,
        date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        content=content,
    )

    suffix = ".ja" if lang == "ja" else ""
    pdf_path = DIST_DIR / f"trust_package{suffix}.pdf"

    HTML(string=html_content).write_pdf(pdf_path)
    print(f"  Created: {pdf_path.relative_to(REPO_ROOT)}")

    return pdf_path


def generate_taxonomy_checksums() -> str:
    """Generate SHA256 checksums for taxonomy/dictionary SSOT files."""
    lines = []
    for rel_path in TAXONOMY_SSOT_PATHS:
        full_path = REPO_ROOT / rel_path
        if full_path.exists():
            h = sha256_file(full_path)
            lines.append(f"{h}  {rel_path}")
    return "\n".join(lines) + "\n"


def build_artifacts_zip(version: str) -> Path:
    """Build artifacts zip file."""
    zip_path = DIST_DIR / "aimo-standard-artifacts.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel_path in ARTIFACT_PATHS:
            full_path = REPO_ROOT / rel_path
            if full_path.exists():
                zf.write(full_path, rel_path)
                print(f"  Added: {rel_path}")
            else:
                print(f"  Warning: {rel_path} not found, skipping", file=sys.stderr)

        # Generate and add TAXONOMY_SHA256SUMS.txt inside the zip
        taxonomy_checksums = generate_taxonomy_checksums()
        zf.writestr("TAXONOMY_SHA256SUMS.txt", taxonomy_checksums)
        print(f"  Added: TAXONOMY_SHA256SUMS.txt (internal checksum for SSOT files)")

    print(f"  Created: {zip_path.relative_to(REPO_ROOT)}")
    return zip_path


def build_checksums(files: list[Path]) -> Path:
    """Generate SHA256SUMS.txt for given files."""
    checksums_path = DIST_DIR / "SHA256SUMS.txt"

    lines = []
    for f in files:
        if f.exists():
            h = sha256_file(f)
            lines.append(f"{h}  {f.name}")
            print(f"  {h}  {f.name}")

    checksums_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Created: {checksums_path.relative_to(REPO_ROOT)}")

    return checksums_path


def get_version_from_git() -> str:
    """Try to get version from git tag or commit."""
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--exact-match"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return tag.lstrip("v")
    except subprocess.CalledProcessError:
        pass

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return f"dev-{commit}"
    except subprocess.CalledProcessError:
        return "dev"


def main():
    parser = argparse.ArgumentParser(
        description="Build AIMO Standard release assets"
    )
    parser.add_argument(
        "--version",
        help="Version string (default: from git tag or commit)",
    )
    parser.add_argument(
        "--ja",
        action="store_true",
        help="Also build Japanese PDF",
    )
    parser.add_argument(
        "--pdf-only",
        action="store_true",
        help="Only build PDFs (skip zip)",
    )
    parser.add_argument(
        "--zip-only",
        action="store_true",
        help="Only build zip (skip PDFs)",
    )
    args = parser.parse_args()

    version = args.version or get_version_from_git()
    print(f"Building release assets for version: {version}")

    # Clean and create dist directory
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    assets = []

    # Build PDFs
    if not args.zip_only:
        print("\n[1/3] Building Trust Package PDF (EN)...")
        pdf_en = build_pdf(version, "en")
        assets.append(pdf_en)

        if args.ja:
            print("\n[2/3] Building Trust Package PDF (JA)...")
            pdf_ja = build_pdf(version, "ja")
            assets.append(pdf_ja)
        else:
            print("\n[2/3] Skipping Japanese PDF (use --ja to include)")

    # Build artifacts zip
    if not args.pdf_only:
        print("\n[3/3] Building artifacts zip...")
        zip_path = build_artifacts_zip(version)
        assets.append(zip_path)

    # Generate checksums
    if assets:
        print("\nGenerating checksums...")
        build_checksums(assets)

    print("\n✓ Build complete!")
    print(f"  Output directory: {DIST_DIR.relative_to(REPO_ROOT)}/")

    return 0


if __name__ == "__main__":
    sys.exit(main())
