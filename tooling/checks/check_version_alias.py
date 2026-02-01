#!/usr/bin/env python3
"""
Check Version Alias Policy

Static verification that versioning configuration follows the immutability policy:
1. mkdocs.yml must have alias_type=redirect (not copy)
2. Workflows must not deploy latest on main branch
3. Release workflow must include proper mike commands
4. Versions docs must explain latest/dev semantics

This is run as part of CI to prevent regression to the old (buggy) behavior.

Usage:
    python tooling/checks/check_version_alias.py          # Check and report
    python tooling/checks/check_version_alias.py --check  # Exit 1 if errors found
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MKDOCS_YML = ROOT / "mkdocs.yml"
VERSIONING_MD = ROOT / "VERSIONING.md"
DEPLOY_DEV_YML = ROOT / ".github" / "workflows" / "deploy-dev.yml"
RELEASE_YML = ROOT / ".github" / "workflows" / "release.yml"
DOCS_CURRENT_YML = ROOT / ".github" / "workflows" / "docs_current.yml"  # Should not exist
VERSIONS_EN = ROOT / "docs" / "en" / "standard" / "versions" / "index.md"


class CheckResult:
    def __init__(self, name: str, passed: bool, message: str):
        self.name = name
        self.passed = passed
        self.message = message


def check_mkdocs_alias_type() -> CheckResult:
    """Verify mkdocs.yml has alias_type: redirect (not copy)."""
    if not MKDOCS_YML.exists():
        return CheckResult(
            "mkdocs.yml alias_type",
            False,
            "mkdocs.yml not found"
        )
    
    content = MKDOCS_YML.read_text(encoding="utf-8")
    
    # Check for mike plugin with alias_type
    if "alias_type: redirect" in content:
        return CheckResult(
            "mkdocs.yml alias_type",
            True,
            "alias_type: redirect is configured"
        )
    elif "alias_type: copy" in content:
        return CheckResult(
            "mkdocs.yml alias_type",
            False,
            "alias_type: copy found - this causes content drift! Use alias_type: redirect"
        )
    elif "alias_type:" not in content and "- mike:" in content:
        return CheckResult(
            "mkdocs.yml alias_type",
            False,
            "mike plugin found but alias_type not set - defaults to copy! Add alias_type: redirect"
        )
    else:
        return CheckResult(
            "mkdocs.yml alias_type",
            False,
            "mike plugin not configured with alias_type"
        )


def check_no_latest_on_main() -> CheckResult:
    """Verify deploy-dev.yml does NOT update latest."""
    if not DEPLOY_DEV_YML.exists():
        return CheckResult(
            "deploy-dev.yml latest check",
            False,
            "deploy-dev.yml not found"
        )
    
    content = DEPLOY_DEV_YML.read_text(encoding="utf-8")
    
    # Check for patterns that would update latest
    bad_patterns = [
        r'mike deploy[^#\n]*latest',  # mike deploy ... latest
        r'--update-aliases[^#\n]*latest',  # --update-aliases ... latest
    ]
    
    for pattern in bad_patterns:
        if re.search(pattern, content):
            return CheckResult(
                "deploy-dev.yml latest check",
                False,
                f"deploy-dev.yml updates latest! Pattern found: {pattern}"
            )
    
    # Verify it only deploys to dev
    if 'mike deploy' in content and 'dev' in content:
        return CheckResult(
            "deploy-dev.yml latest check",
            True,
            "deploy-dev.yml only deploys to dev (does not touch latest)"
        )
    
    return CheckResult(
        "deploy-dev.yml latest check",
        False,
        "Could not verify deploy-dev.yml behavior"
    )


def check_old_workflow_removed() -> CheckResult:
    """Verify docs_current.yml (old workflow) does not exist."""
    if DOCS_CURRENT_YML.exists():
        return CheckResult(
            "Old workflow removed",
            False,
            "docs_current.yml still exists! This workflow updates latest on main push. Remove it."
        )
    
    return CheckResult(
        "Old workflow removed",
        True,
        "docs_current.yml removed (replaced by deploy-dev.yml)"
    )


def check_release_workflow() -> CheckResult:
    """Verify release.yml has proper mike commands."""
    if not RELEASE_YML.exists():
        return CheckResult(
            "release.yml configuration",
            False,
            "release.yml not found"
        )
    
    content = RELEASE_YML.read_text(encoding="utf-8")
    
    required_patterns = [
        (r'mike deploy[^#\n]*--update-aliases[^#\n]*latest', 
         "mike deploy --update-aliases ... latest"),
        (r'mike set-default[^#\n]*latest',
         "mike set-default latest"),
    ]
    
    missing = []
    for pattern, description in required_patterns:
        if not re.search(pattern, content):
            missing.append(description)
    
    if missing:
        return CheckResult(
            "release.yml configuration",
            False,
            f"release.yml missing required commands: {', '.join(missing)}"
        )
    
    # Check for version existence check
    if 'already exist' not in content.lower() and 'does not exist' not in content.lower():
        return CheckResult(
            "release.yml configuration",
            False,
            "release.yml should check that version doesn't already exist (immutability)"
        )
    
    return CheckResult(
        "release.yml configuration",
        True,
        "release.yml has proper mike commands and version check"
    )


def check_versioning_docs() -> CheckResult:
    """Verify VERSIONING.md explains latest/dev semantics."""
    if not VERSIONING_MD.exists():
        return CheckResult(
            "VERSIONING.md content",
            False,
            "VERSIONING.md not found"
        )
    
    content = VERSIONING_MD.read_text(encoding="utf-8")
    
    required_terms = [
        ("latest", "alias"),
        ("dev", "preview"),
        ("immutable", "frozen"),
        ("redirect", "alias_type"),
    ]
    
    content_lower = content.lower()
    missing = []
    for term1, term2 in required_terms:
        if term1 not in content_lower and term2 not in content_lower:
            missing.append(f"{term1}/{term2}")
    
    if missing:
        return CheckResult(
            "VERSIONING.md content",
            False,
            f"VERSIONING.md should explain: {', '.join(missing)}"
        )
    
    return CheckResult(
        "VERSIONING.md content",
        True,
        "VERSIONING.md explains latest/dev semantics"
    )


def check_versions_page() -> CheckResult:
    """Verify versions docs page explains URL semantics."""
    if not VERSIONS_EN.exists():
        return CheckResult(
            "Versions page content",
            False,
            "docs/en/standard/versions/index.md not found"
        )
    
    content = VERSIONS_EN.read_text(encoding="utf-8")
    content_lower = content.lower()
    
    # Check for key concepts
    required_concepts = [
        "latest",
        "dev",
        "/x.y.z/",  # Or similar versioned URL reference
    ]
    
    # Check if page explains the difference
    if "alias" in content_lower and "redirect" in content_lower:
        return CheckResult(
            "Versions page content",
            True,
            "Versions page explains URL semantics"
        )
    
    # Also accept if it explains latest vs dev
    if "latest" in content_lower and "dev" in content_lower and "preview" in content_lower:
        return CheckResult(
            "Versions page content",
            True,
            "Versions page explains latest/dev distinction"
        )
    
    return CheckResult(
        "Versions page content",
        False,
        "Versions page should explain latest/dev semantics"
    )


def main():
    parser = argparse.ArgumentParser(description="Check version alias policy")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with error code if any check fails",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("AIMO Standard - Version Alias Policy Check")
    print("=" * 60)
    print()

    checks = [
        check_mkdocs_alias_type(),
        check_no_latest_on_main(),
        check_old_workflow_removed(),
        check_release_workflow(),
        check_versioning_docs(),
        check_versions_page(),
    ]

    passed = 0
    failed = 0

    for check in checks:
        status = "✓ PASS" if check.passed else "✗ FAIL"
        print(f"{status}: {check.name}")
        print(f"       {check.message}")
        print()

        if check.passed:
            passed += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"Summary: {passed} passed, {failed} failed")
    print("=" * 60)

    if failed > 0:
        print()
        print("Some checks failed. These must be fixed to prevent:")
        print("- /latest/ diverging from the most recent release")
        print("- Content drift between /latest/ and /X.Y.Z/")
        print("- Auditors citing unstable URLs")
        print()
        print("See VERSIONING.md for the correct policy.")
        
        if args.check:
            sys.exit(1)
    else:
        print()
        print("All checks passed. Versioning policy is correctly configured.")

    sys.exit(0)


if __name__ == "__main__":
    main()
