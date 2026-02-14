#!/usr/bin/env python3
"""
Baseline Audit Script for AIMO Standard Repository.

Generates a comprehensive audit report for public release preparation.

Audit Items:
1. Broken link detection in docs/ (relative links, mkdocs nav references)
2. English canonical vs JA translation correspondence (missing translations)
3. Reference integrity for schemas/templates/examples/validator
4. Unreferenced files (orphan pages in docs/)
5. Release requirements verification (trust_package*.pdf, artifacts.zip, SHA256SUMS.txt)

Output: REPORTS/baseline_audit.md

Usage:
    python tooling/audit/baseline_audit.py          # Generate audit report
    python tooling/audit/baseline_audit.py --check  # Exit with error if NG found
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import NamedTuple, Optional

import yaml

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    Draft202012Validator = None
    ValidationError = None

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
EN_DIR = DOCS / "en"
JA_DIR = DOCS / "ja"
SCHEMAS_DIR = ROOT / "schemas" / "jsonschema"
TEMPLATES_DIR = ROOT / "templates"
EXAMPLES_DIR = ROOT / "examples"
VALIDATOR_DIR = ROOT / "validator"
REPORTS_DIR = ROOT / "REPORTS"
MKDOCS_YML = ROOT / "mkdocs.yml"
RELEASE_WORKFLOW = ROOT / ".github" / "workflows" / "release.yml"
DEPLOY_DEV_WORKFLOW = ROOT / ".github" / "workflows" / "deploy-dev.yml"
DOCS_CURRENT_WORKFLOW = ROOT / ".github" / "workflows" / "docs_current.yml"  # Should not exist


class AuditItem(NamedTuple):
    """Single audit finding."""
    category: str
    status: str  # "OK", "NG", "WARN"
    file_path: str
    message: str
    recommendation: str


def load_mkdocs_nav() -> list[str]:
    """Extract all nav file references from mkdocs.yml."""
    if not MKDOCS_YML.exists():
        return []

    with MKDOCS_YML.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    nav_files = []

    def extract_nav_files(nav_item):
        if isinstance(nav_item, str):
            nav_files.append(nav_item)
        elif isinstance(nav_item, dict):
            for value in nav_item.values():
                extract_nav_files(value)
        elif isinstance(nav_item, list):
            for item in nav_item:
                extract_nav_files(item)

    nav = config.get("nav", [])
    extract_nav_files(nav)
    return nav_files


def resolve_link_url_style(current_path_under_docs: Path, link_target: str, docs_root: Path) -> Optional[Path]:
    """
    Resolve a relative link the same way the built site does (URL path segments).
    current_path_under_docs: e.g. Path('ja/artifacts/evidence-bundle-coverage-map.md')
    link_target: e.g. '../minimum-evidence/' -> target is docs/ja/artifacts/minimum-evidence
    """
    # Current page path as segments (URL has no .md; last part is stem)
    parts = list(current_path_under_docs.parts)
    if not parts:
        return None
    if parts[-1].endswith(".md"):
        parts[-1] = Path(parts[-1]).stem
    # Normalize link into segments
    raw = link_target.rstrip("/").split("#")[0]
    if not raw:
        return None
    link_segments = [p for p in raw.split("/") if p and p != "."]
    for seg in link_segments:
        if seg == "..":
            if len(parts) <= 1:
                return None
            parts.pop()
        else:
            parts.append(seg)
    if not parts:
        return None
    candidate = docs_root.joinpath(*parts)
    if candidate.is_dir():
        candidate = candidate / "index.md"
    if not candidate.exists():
        # Try .md: with_suffix works only when name has no other dots (e.g. 10-roadmap-v0.2)
        with_md = candidate.parent / (candidate.name + ".md")
        if with_md.exists():
            return with_md
        if not candidate.suffix:
            with_md = candidate.with_suffix(".md")
            if with_md.exists():
                return with_md
    return candidate if candidate.exists() else None


def extract_markdown_links(content: str) -> list[tuple[int, str, str]]:
    """
    Extract all markdown links from content.
    Returns list of (line_num, link_text, link_target).
    """
    links = []
    lines = content.splitlines()

    # Pattern for [text](link)
    link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')

    for i, line in enumerate(lines):
        for match in link_pattern.finditer(line):
            link_text = match.group(1)
            link_target = match.group(2)
            # Skip external links and anchors
            if not link_target.startswith(('http://', 'https://', 'mailto:', '#')):
                links.append((i + 1, link_text, link_target))

    return links


def check_broken_links() -> list[AuditItem]:
    """
    Check for broken links in docs/.
    Checks relative links and mkdocs nav references.
    """
    items = []

    # Check nav references
    nav_files = load_mkdocs_nav()
    for nav_file in nav_files:
        # nav references are relative to docs/en/ (default lang)
        en_path = EN_DIR / nav_file
        ja_path = JA_DIR / nav_file

        if not en_path.exists() and not ja_path.exists():
            items.append(AuditItem(
                category="Broken Links",
                status="NG",
                file_path=f"mkdocs.yml (nav: {nav_file})",
                message=f"Nav reference not found in docs/en/ or docs/ja/",
                recommendation=f"Create docs/en/{nav_file} or remove from nav"
            ))
        elif not en_path.exists():
            items.append(AuditItem(
                category="Broken Links",
                status="WARN",
                file_path=f"mkdocs.yml (nav: {nav_file})",
                message=f"Nav reference missing in EN (exists in JA only)",
                recommendation=f"Create docs/en/{nav_file} as canonical source"
            ))

    # Check relative links in all markdown files
    for md_file in DOCS.rglob("*.md"):
        if "overrides" in str(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        links = extract_markdown_links(content)

        for line_num, link_text, link_target in links:
            # Remove anchor from link
            target_path = link_target.split('#')[0]
            if not target_path:
                continue

            # Resolve relative path
            if target_path.startswith('/'):
                # Absolute from docs root
                resolved = DOCS / target_path.lstrip('/').rstrip('/')
            else:
                # Relative from current file (normalize trailing slash for pretty-URL links)
                resolved = (md_file.parent / target_path.rstrip('/')).resolve()

            # Handle directory links (should have index.md)
            if resolved.is_dir():
                resolved = resolved / "index.md"

            # Add .md extension if needed (pretty-URL links use path/ which points to path.md in source)
            if not resolved.suffix and not resolved.exists():
                resolved_with_md = resolved.with_suffix(".md")
                if not resolved_with_md.exists():
                    resolved_with_md = resolved.parent / (resolved.name + ".md")
                if resolved_with_md.exists():
                    resolved = resolved_with_md

            # Fallback: links to releases/ may use ../../../releases/ (for built site URL)
            # but in source tree the file is docs/<locale>/releases/index.md
            if not resolved.exists() and target_path.rstrip("/").endswith("releases"):
                try:
                    rel_parts = md_file.relative_to(DOCS).parts
                    if len(rel_parts) >= 1:
                        locale = rel_parts[0]
                        alt = DOCS / locale / "releases" / "index.md"
                        if alt.exists():
                            resolved = alt
                except ValueError:
                    pass

            # Fallback: relative links are written for built URL (e.g. /ja/0.1.2/artifacts/);
            # ../../standard/... from there means /ja/0.1.2/standard/... but in source
            # file-relative ../../ goes to docs/, so resolve to docs/<locale>/standard/...
            if not resolved.exists() and not target_path.startswith("/"):
                try:
                    rel_parts = md_file.relative_to(DOCS).parts
                    if len(rel_parts) >= 1:
                        locale = rel_parts[0]
                        # resolved is e.g. .../docs/standard/current/03-taxonomy
                        try:
                            under_docs = resolved.relative_to(DOCS)
                        except ValueError:
                            under_docs = None
                        if under_docs is not None and under_docs.parts and under_docs.parts[0] not in ("en", "ja", "es", "fr", "de", "pt", "it", "zh", "zh-TW", "ko"):
                            # path has no locale; try under current file's locale
                            alt = DOCS / locale / under_docs
                            if alt.is_dir():
                                alt = alt / "index.md"
                            if not alt.exists():
                                alt_md = alt.parent / (alt.name + ".md")
                                if alt_md.exists():
                                    alt = alt_md
                                elif not alt.suffix:
                                    alt_md = alt.with_suffix(".md")
                                    if alt_md.exists():
                                        alt = alt_md
                            if alt.exists():
                                resolved = alt
                except (ValueError, IndexError):
                    pass

            # Fallback: resolve relative links using URL-path rules (built site behavior)
            if not resolved.exists() and not target_path.startswith("/"):
                try:
                    current_under_docs = md_file.relative_to(DOCS)
                    url_resolved = resolve_link_url_style(current_under_docs, target_path, DOCS)
                    if url_resolved is not None:
                        resolved = url_resolved
                except ValueError:
                    pass

            if not resolved.exists():
                rel_file = md_file.relative_to(ROOT)
                items.append(AuditItem(
                    category="Broken Links",
                    status="NG",
                    file_path=f"{rel_file}:{line_num}",
                    message=f"Link target not found: {link_target}",
                    recommendation=f"Fix link or create missing file"
                ))

    if not items:
        items.append(AuditItem(
            category="Broken Links",
            status="OK",
            file_path="docs/",
            message="All links resolved successfully",
            recommendation=""
        ))

    return items


def check_translation_coverage() -> list[AuditItem]:
    """
    Check EN canonical vs JA translation correspondence.
    List untranslated files.
    """
    items = []
    untranslated = []

    # Get all EN files
    en_files = sorted(EN_DIR.rglob("*.md"))

    for en_file in en_files:
        rel_path = en_file.relative_to(EN_DIR)
        ja_file = JA_DIR / rel_path

        if not ja_file.exists():
            untranslated.append(str(rel_path))

    if untranslated:
        for rel_path in untranslated:
            items.append(AuditItem(
                category="Translation Coverage",
                status="WARN",
                file_path=f"docs/en/{rel_path}",
                message=f"No JA translation exists",
                recommendation=f"Create docs/ja/{rel_path} or confirm EN fallback is acceptable"
            ))
    else:
        items.append(AuditItem(
            category="Translation Coverage",
            status="OK",
            file_path="docs/",
            message="All EN files have JA translations",
            recommendation=""
        ))

    # Check for orphan JA files (JA without EN)
    ja_files = sorted(JA_DIR.rglob("*.md"))
    for ja_file in ja_files:
        rel_path = ja_file.relative_to(JA_DIR)
        en_file = EN_DIR / rel_path

        if not en_file.exists():
            items.append(AuditItem(
                category="Translation Coverage",
                status="WARN",
                file_path=f"docs/ja/{rel_path}",
                message=f"Orphan JA file (no EN canonical source)",
                recommendation=f"Create docs/en/{rel_path} as canonical or remove orphan"
            ))

    return items


def check_reference_integrity() -> list[AuditItem]:
    """
    Check that files mentioned in docs actually exist.
    Check that examples conform to schemas.
    """
    items = []

    # Patterns for file references in docs
    # Matches: `schemas/jsonschema/xxx`, `examples/xxx`, `templates/xxx`, `validator/xxx`
    file_ref_patterns = [
        (re.compile(r'`(schemas/jsonschema/[^`]+)`'), "schemas"),
        (re.compile(r'`(examples/[^`]+)`'), "examples"),
        (re.compile(r'`(templates/[^`]+)`'), "templates"),
        (re.compile(r'`(validator/[^`]+)`'), "validator"),
    ]

    # Also match repository path references
    repo_ref_pattern = re.compile(r'(?:repository|repo)[^`]*`([^`]+/[^`]+)`')

    # Check all docs for file references
    for md_file in DOCS.rglob("*.md"):
        if "overrides" in str(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        rel_md = md_file.relative_to(ROOT)

        for pattern, category in file_ref_patterns:
            for match in pattern.finditer(content):
                ref_path = match.group(1)
                full_path = ROOT / ref_path

                # Handle wildcard references
                if '*' in ref_path:
                    continue

                # Handle directory references
                if full_path.is_dir():
                    continue

                if not full_path.exists():
                    items.append(AuditItem(
                        category="Reference Integrity",
                        status="NG",
                        file_path=str(rel_md),
                        message=f"Referenced file not found: {ref_path}",
                        recommendation=f"Create {ref_path} or update reference"
                    ))

    # Validate examples against schemas
    if Draft202012Validator:
        schema_map = {
            "aimo-dictionary.schema.json": ["sample_dictionary.json", "dictionary.json"],
            "aimo-ev.schema.json": ["sample_ev.json"],
        }

        for schema_name, example_patterns in schema_map.items():
            schema_path = SCHEMAS_DIR / schema_name
            if not schema_path.exists():
                items.append(AuditItem(
                    category="Reference Integrity",
                    status="WARN",
                    file_path=str(schema_path.relative_to(ROOT)),
                    message=f"Schema file not found",
                    recommendation=f"Create {schema_name} schema"
                ))
                continue

            try:
                schema = json.loads(schema_path.read_text(encoding="utf-8"))
                validator = Draft202012Validator(schema)
            except Exception as e:
                items.append(AuditItem(
                    category="Reference Integrity",
                    status="NG",
                    file_path=str(schema_path.relative_to(ROOT)),
                    message=f"Invalid schema: {e}",
                    recommendation=f"Fix schema syntax"
                ))
                continue

            # Find and validate matching example files
            for example_pattern in example_patterns:
                for example_file in EXAMPLES_DIR.rglob(example_pattern):
                    try:
                        example_data = json.loads(example_file.read_text(encoding="utf-8"))
                        validator.validate(example_data)
                    except json.JSONDecodeError as e:
                        items.append(AuditItem(
                            category="Reference Integrity",
                            status="NG",
                            file_path=str(example_file.relative_to(ROOT)),
                            message=f"Invalid JSON: {e}",
                            recommendation=f"Fix JSON syntax"
                        ))
                    except ValidationError as e:
                        items.append(AuditItem(
                            category="Reference Integrity",
                            status="NG",
                            file_path=str(example_file.relative_to(ROOT)),
                            message=f"Schema validation failed: {e.message}",
                            recommendation=f"Update example to match schema {schema_name}"
                        ))

    if not any(i.status == "NG" for i in items if i.category == "Reference Integrity"):
        items.append(AuditItem(
            category="Reference Integrity",
            status="OK",
            file_path="schemas/, examples/",
            message="All references valid and examples conform to schemas",
            recommendation=""
        ))

    return items


def check_unreferenced_files() -> list[AuditItem]:
    """
    Find unreferenced files in docs/ that are not linked from anywhere.
    """
    items = []

    # Get all nav files
    nav_files = set(load_mkdocs_nav())

    # Get all markdown files in docs/en and docs/ja
    all_docs = set()
    for lang in ["en", "ja"]:
        lang_dir = DOCS / lang
        for md_file in lang_dir.rglob("*.md"):
            rel_path = md_file.relative_to(lang_dir)
            all_docs.add(str(rel_path))

    # Collect all internal link targets from docs
    linked_files = set()

    for md_file in DOCS.rglob("*.md"):
        if "overrides" in str(md_file):
            continue

        content = md_file.read_text(encoding="utf-8")
        links = extract_markdown_links(content)

        for _, _, link_target in links:
            # Normalize link target
            target = link_target.split('#')[0]
            if not target:
                continue

            # Handle relative paths
            if not target.startswith('/'):
                # Relative from current file's directory
                current_dir = md_file.parent
                if md_file.is_relative_to(EN_DIR):
                    rel_to_lang = md_file.parent.relative_to(EN_DIR)
                elif md_file.is_relative_to(JA_DIR):
                    rel_to_lang = md_file.parent.relative_to(JA_DIR)
                else:
                    continue

                resolved = (rel_to_lang / target).as_posix()
                # Normalize path
                parts = []
                for part in resolved.split('/'):
                    if part == '..':
                        if parts:
                            parts.pop()
                    elif part != '.':
                        parts.append(part)
                resolved = '/'.join(parts)

                if resolved.endswith('/'):
                    resolved += 'index.md'
                if not resolved.endswith('.md'):
                    resolved += '.md'

                linked_files.add(resolved)

    # Add nav files as referenced
    for nav_file in nav_files:
        linked_files.add(nav_file)

    # Find unreferenced files (not in nav and not linked)
    for doc_file in all_docs:
        if doc_file not in nav_files and doc_file not in linked_files:
            # Check if it's an index file in a linked directory
            parent_dir = str(Path(doc_file).parent)
            if doc_file.endswith("index.md"):
                dir_path = parent_dir + "/"
                if any(lf.startswith(dir_path) for lf in linked_files):
                    continue
                if any(nf.startswith(parent_dir + "/") for nf in nav_files):
                    continue

            items.append(AuditItem(
                category="Unreferenced Files",
                status="WARN",
                file_path=f"docs/en/{doc_file} (or ja/)",
                message=f"Not referenced in nav or any link",
                recommendation=f"Add to nav or link from another page, or remove if obsolete"
            ))

    if not items:
        items.append(AuditItem(
            category="Unreferenced Files",
            status="OK",
            file_path="docs/",
            message="All docs files are referenced in nav or linked",
            recommendation=""
        ))

    return items


def check_redirect_targets() -> list[AuditItem]:
    """
    Check that all redirect targets in build_redirects.py exist in docs/.
    Ensures redirects point to valid source documents.
    """
    items = []

    # Import REDIRECT_MAPS from build_redirects.py
    build_redirects_path = ROOT / "tooling" / "release" / "build_redirects.py"
    if not build_redirects_path.exists():
        items.append(AuditItem(
            category="Redirect Targets",
            status="WARN",
            file_path="tooling/release/build_redirects.py",
            message="Redirect generator script not found",
            recommendation="Create build_redirects.py for legacy URL support"
        ))
        return items

    # Parse REDIRECT_MAPS from the script
    redirect_maps = {}
    try:
        content = build_redirects_path.read_text(encoding="utf-8")
        # Extract REDIRECT_MAPS dictionary using regex
        import ast
        # Find the REDIRECT_MAPS = { ... } block
        match = re.search(r'REDIRECT_MAPS\s*=\s*\{([^}]+)\}', content, re.DOTALL)
        if match:
            # Parse each line like: "source": "target",
            for line in match.group(1).strip().split('\n'):
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                # Match "key": "value",
                kv_match = re.match(r'"([^"]+)":\s*"([^"]+)"', line)
                if kv_match:
                    redirect_maps[kv_match.group(1)] = kv_match.group(2)
    except Exception as e:
        items.append(AuditItem(
            category="Redirect Targets",
            status="WARN",
            file_path="tooling/release/build_redirects.py",
            message=f"Could not parse REDIRECT_MAPS: {e}",
            recommendation="Check build_redirects.py syntax"
        ))
        return items

    if not redirect_maps:
        items.append(AuditItem(
            category="Redirect Targets",
            status="OK",
            file_path="tooling/release/build_redirects.py",
            message="No redirect mappings configured",
            recommendation=""
        ))
        return items

    # Check each redirect target exists in docs/en/
    invalid_targets = []
    for source, target in redirect_maps.items():
        # Target path is like "standard/versions/" - convert to doc path
        # URLs ending with / map to either index.md or <name>.md
        target_doc = target.rstrip('/')

        # First try: target as a directory with index.md
        target_path_index = EN_DIR / target_doc / "index.md"
        # Second try: target as a file with .md extension
        target_path_file = EN_DIR / (target_doc + ".md")

        target_exists = target_path_index.exists() or target_path_file.exists()

        if not target_exists:
            invalid_targets.append((source, target))
            items.append(AuditItem(
                category="Redirect Targets",
                status="NG",
                file_path=f"build_redirects.py ({source})",
                message=f"Redirect target not found: {target}",
                recommendation=f"Create docs/en/{target_doc}/index.md or docs/en/{target_doc}.md"
            ))

    if not invalid_targets:
        items.append(AuditItem(
            category="Redirect Targets",
            status="OK",
            file_path="tooling/release/build_redirects.py",
            message=f"All {len(redirect_maps)} redirect targets exist",
            recommendation=""
        ))

    return items


def check_versioning_policy() -> list[AuditItem]:
    """
    Check that versioning configuration follows immutability policy.
    - alias_type must be redirect (not copy)
    - deploy-dev.yml must exist and not touch latest
    - docs_current.yml must not exist (old workflow)
    """
    items = []

    # Check mkdocs.yml for alias_type
    if MKDOCS_YML.exists():
        content = MKDOCS_YML.read_text(encoding="utf-8")
        
        if "alias_type: redirect" in content:
            items.append(AuditItem(
                category="Versioning Policy",
                status="OK",
                file_path="mkdocs.yml",
                message="alias_type: redirect is configured",
                recommendation=""
            ))
        elif "alias_type: copy" in content:
            items.append(AuditItem(
                category="Versioning Policy",
                status="NG",
                file_path="mkdocs.yml",
                message="alias_type: copy causes content drift",
                recommendation="Change to alias_type: redirect"
            ))
        elif "- mike:" in content:
            items.append(AuditItem(
                category="Versioning Policy",
                status="NG",
                file_path="mkdocs.yml",
                message="mike plugin found but alias_type not set (defaults to copy)",
                recommendation="Add alias_type: redirect to mike plugin config"
            ))

    # Check that deploy-dev.yml exists
    if DEPLOY_DEV_WORKFLOW.exists():
        content = DEPLOY_DEV_WORKFLOW.read_text(encoding="utf-8")
        
        # Check it doesn't update latest
        if re.search(r'mike deploy[^#\n]*latest', content):
            items.append(AuditItem(
                category="Versioning Policy",
                status="NG",
                file_path="deploy-dev.yml",
                message="deploy-dev.yml updates latest on main branch",
                recommendation="Remove latest from mike deploy command"
            ))
        else:
            items.append(AuditItem(
                category="Versioning Policy",
                status="OK",
                file_path="deploy-dev.yml",
                message="deploy-dev.yml correctly deploys only to dev",
                recommendation=""
            ))
    else:
        items.append(AuditItem(
            category="Versioning Policy",
            status="NG",
            file_path="deploy-dev.yml",
            message="deploy-dev.yml not found",
            recommendation="Create deploy-dev.yml for main branch deployments"
        ))

    # Check that old docs_current.yml is removed
    if DOCS_CURRENT_WORKFLOW.exists():
        items.append(AuditItem(
            category="Versioning Policy",
            status="NG",
            file_path="docs_current.yml",
            message="Old workflow still exists - updates latest on main push",
            recommendation="Delete docs_current.yml (replaced by deploy-dev.yml)"
        ))
    else:
        items.append(AuditItem(
            category="Versioning Policy",
            status="OK",
            file_path="docs_current.yml",
            message="Old workflow removed",
            recommendation=""
        ))

    return items


def check_release_requirements() -> list[AuditItem]:
    """
    Check that release requirements are met.
    Required assets: trust_package.pdf, trust_package.ja.pdf, artifacts.zip, SHA256SUMS.txt
    """
    items = []

    # Check release workflow exists
    if not RELEASE_WORKFLOW.exists():
        items.append(AuditItem(
            category="Release Requirements",
            status="NG",
            file_path=".github/workflows/release.yml",
            message="Release workflow not found",
            recommendation="Create release workflow"
        ))
        return items

    workflow_content = RELEASE_WORKFLOW.read_text(encoding="utf-8")

    # Check for required assets in workflow
    required_assets = [
        ("trust_package.pdf", "English Trust Package PDF"),
        ("trust_package.ja.pdf", "Japanese Trust Package PDF"),
        ("aimo-standard-artifacts.zip", "Artifacts ZIP"),
        ("SHA256SUMS.txt", "Checksums file"),
    ]

    for asset_name, description in required_assets:
        if asset_name not in workflow_content:
            items.append(AuditItem(
                category="Release Requirements",
                status="NG",
                file_path=".github/workflows/release.yml",
                message=f"Missing reference to {asset_name} ({description})",
                recommendation=f"Add {asset_name} to release workflow"
            ))

    # Check build_assets.py exists
    build_assets_path = ROOT / "tooling" / "release" / "build_assets.py"
    if not build_assets_path.exists():
        items.append(AuditItem(
            category="Release Requirements",
            status="NG",
            file_path="tooling/release/build_assets.py",
            message="Build assets script not found",
            recommendation="Create build_assets.py to generate release assets"
        ))

    # Check PDF generation deps in tooling/requirements.txt
    tooling_reqs = ROOT / "tooling" / "requirements.txt"
    if tooling_reqs.exists():
        reqs_content = tooling_reqs.read_text(encoding="utf-8").lower()
        if "weasyprint" not in reqs_content:
            items.append(AuditItem(
                category="Release Requirements",
                status="WARN",
                file_path="tooling/requirements.txt",
                message="WeasyPrint not in requirements (needed for PDF generation)",
                recommendation="Add weasyprint to tooling/requirements.txt"
            ))

    # Check that schemas exist for artifact packaging
    artifact_dirs = [
        ("schemas/jsonschema", "JSON Schemas"),
        ("templates", "Templates"),
        ("examples", "Examples"),
        ("validator/rules", "Validator Rules"),
    ]

    for dir_path, description in artifact_dirs:
        full_path = ROOT / dir_path
        if not full_path.exists() or not any(full_path.iterdir()):
            items.append(AuditItem(
                category="Release Requirements",
                status="WARN",
                file_path=dir_path,
                message=f"{description} directory empty or missing",
                recommendation=f"Populate {dir_path} with required artifacts"
            ))

    if not any(i.status == "NG" for i in items if i.category == "Release Requirements"):
        items.append(AuditItem(
            category="Release Requirements",
            status="OK",
            file_path=".github/workflows/release.yml",
            message="Release workflow properly configured for required assets",
            recommendation=""
        ))

    return items


def generate_report(items: list[AuditItem]) -> str:
    """Generate markdown report from audit items."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Baseline Audit Report",
        "",
        f"**Generated:** {now}",
        "",
        "## Summary",
        "",
    ]

    # Count by status and category
    categories = {}
    for item in items:
        if item.category not in categories:
            categories[item.category] = {"OK": 0, "NG": 0, "WARN": 0}
        categories[item.category][item.status] += 1

    lines.append("| Category | OK | NG | WARN |")
    lines.append("|----------|----|----|------|")
    for cat, counts in categories.items():
        lines.append(f"| {cat} | {counts['OK']} | {counts['NG']} | {counts['WARN']} |")

    lines.append("")

    total_ng = sum(c["NG"] for c in categories.values())
    total_warn = sum(c["WARN"] for c in categories.values())

    if total_ng == 0 and total_warn == 0:
        lines.append("**Status: ALL CHECKS PASSED** ✓")
    elif total_ng == 0:
        lines.append(f"**Status: {total_warn} WARNING(S)** (review recommended)")
    else:
        lines.append(f"**Status: {total_ng} NG / {total_warn} WARN** — action required")

    lines.append("")

    # Detailed findings by category
    lines.append("## Detailed Findings")
    lines.append("")

    for category in categories.keys():
        lines.append(f"### {category}")
        lines.append("")

        cat_items = [i for i in items if i.category == category]

        # Show NG first, then WARN, then OK
        for status in ["NG", "WARN", "OK"]:
            status_items = [i for i in cat_items if i.status == status]
            if not status_items:
                continue

            lines.append(f"#### {status}")
            lines.append("")
            lines.append("| File | Message | Recommendation |")
            lines.append("|------|---------|----------------|")

            for item in status_items:
                msg = item.message.replace("|", "\\|")
                rec = item.recommendation.replace("|", "\\|") if item.recommendation else "-"
                lines.append(f"| `{item.file_path}` | {msg} | {rec} |")

            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Baseline audit for AIMO Standard")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with error code if NG items found",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("AIMO Standard Baseline Audit")
    print("=" * 60)
    print()

    all_items: list[AuditItem] = []

    # Run all checks
    print("Checking broken links...")
    all_items.extend(check_broken_links())

    print("Checking translation coverage...")
    all_items.extend(check_translation_coverage())

    print("Checking reference integrity...")
    all_items.extend(check_reference_integrity())

    print("Checking unreferenced files...")
    all_items.extend(check_unreferenced_files())

    print("Checking redirect targets...")
    all_items.extend(check_redirect_targets())

    print("Checking release requirements...")
    all_items.extend(check_release_requirements())

    print("Checking versioning policy...")
    all_items.extend(check_versioning_policy())

    print()

    # Generate report
    report = generate_report(all_items)

    # Ensure REPORTS directory exists
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Write report
    report_path = REPORTS_DIR / "baseline_audit.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report written to: {report_path.relative_to(ROOT)}")

    # Print summary
    ng_count = sum(1 for i in all_items if i.status == "NG")
    warn_count = sum(1 for i in all_items if i.status == "WARN")
    ok_count = sum(1 for i in all_items if i.status == "OK")

    print()
    print("=" * 60)
    print(f"Summary: {ok_count} OK, {ng_count} NG, {warn_count} WARN")
    print("=" * 60)

    if ng_count > 0:
        print("\nNG items require attention before release.")
        if args.check:
            sys.exit(1)

    if warn_count > 0:
        print("\nWARN items should be reviewed.")

    if ng_count == 0:
        print("\nBaseline audit completed successfully.")

    sys.exit(0)


if __name__ == "__main__":
    main()
