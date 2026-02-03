#!/usr/bin/env python3
"""
Release Consistency Checker

Ensures that documentation references (Versions page, Cite page, CITATION.cff)
match the release version before deployment.

Usage:
    RELEASE_TAG=v0.1.x python tooling/checks/check_release_consistency.py

Exit codes:
    0 - All checks passed
    1 - One or more checks failed
    2 - Configuration/environment error
"""

import os
import re
import sys
from glob import glob
from pathlib import Path


def get_release_tag() -> str:
    """Get RELEASE_TAG from environment, exit if not set."""
    tag = os.environ.get("RELEASE_TAG", "").strip()
    if not tag:
        print("[ERROR] RELEASE_TAG environment variable not set")
        print("Usage: RELEASE_TAG=v0.1.x python check_release_consistency.py")
        sys.exit(2)
    return tag


def tag_to_version(tag: str) -> str:
    """Convert tag (v0.1.x) to version (0.1.x)."""
    return tag.lstrip("v")


def find_files(patterns: list[str], base_dir: str = ".") -> list[Path]:
    """Find files matching any of the glob patterns."""
    files = []
    for pattern in patterns:
        files.extend(Path(base_dir).glob(pattern))
    return sorted(set(files))


def read_file(path: Path) -> str:
    """Read file contents."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[WARN] Could not read {path}: {e}")
        return ""


class ConsistencyChecker:
    def __init__(self, tag: str):
        self.tag = tag
        self.ver = tag_to_version(tag)
        self.errors: list[str] = []
        self.successes: list[str] = []

    def check_versions_page(self, lang: str, path: Path) -> None:
        """Check that Versions page shows correct Current Version."""
        content = read_file(path)
        if not content:
            self.errors.append(f"[FAIL] {lang.upper()} versions: Could not read {path}")
            return

        # Check for Current Version marker and correct version
        # Look for v{ver} near "Current Version" text (within 500 chars)
        current_pattern = re.compile(
            r"(Current Version|現在のバージョン|最新リリース).{0,500}" + re.escape(f"v{self.ver}"),
            re.IGNORECASE | re.DOTALL
        )
        
        if current_pattern.search(content):
            self.successes.append(f"[OK] {lang.upper()} versions: Current Version is v{self.ver}")
        else:
            # Try to find what version IS shown
            version_match = re.search(
                r"(Current Version|現在のバージョン|最新リリース).{0,200}(v\d+\.\d+\.\d+)",
                content,
                re.IGNORECASE | re.DOTALL
            )
            found = version_match.group(2) if version_match else "unknown"
            self.errors.append(
                f"[FAIL] {lang.upper()} versions: Current Version does not match. "
                f"Expected v{self.ver}, found {found}, file={path}"
            )

    def check_cite_page(self, lang: str, path: Path) -> None:
        """Check that Cite page has correct version references."""
        content = read_file(path)
        if not content:
            self.errors.append(f"[FAIL] {lang.upper()} cite: Could not read {path}")
            return

        errors_found = []
        
        # Check BibTeX version
        bibtex_pattern = re.compile(r"version\s*=\s*\{" + re.escape(self.ver) + r"\}")
        if bibtex_pattern.search(content):
            self.successes.append(f"[OK] {lang.upper()} cite: BibTeX version is {self.ver}")
        else:
            # Find what version is shown
            bibtex_match = re.search(r"version\s*=\s*\{(\d+\.\d+\.\d+)\}", content)
            found = bibtex_match.group(1) if bibtex_match else "not found"
            errors_found.append(f"BibTeX version={found}")

        # Check URL example (e.g., /0.1.x/)
        url_pattern = re.compile(r"/" + re.escape(self.ver) + r"/")
        if url_pattern.search(content):
            self.successes.append(f"[OK] {lang.upper()} cite: URL example contains /{self.ver}/")
        else:
            # Find what version URLs are shown
            url_match = re.search(r"/(\d+\.\d+\.\d+)/", content)
            found = url_match.group(1) if url_match else "not found"
            errors_found.append(f"URL example=/{found}/")

        # Check Version X.Y.Z text
        version_text_pattern = re.compile(r"Version\s+" + re.escape(self.ver), re.IGNORECASE)
        if version_text_pattern.search(content):
            self.successes.append(f"[OK] {lang.upper()} cite: Version text is {self.ver}")
        else:
            version_text_match = re.search(r"Version\s+(\d+\.\d+\.\d+)", content, re.IGNORECASE)
            found = version_text_match.group(1) if version_text_match else "not found"
            errors_found.append(f"Version text={found}")

        if errors_found:
            self.errors.append(
                f"[FAIL] {lang.upper()} cite: Version mismatch. Expected {self.ver}, "
                f"found: {', '.join(errors_found)}, file={path}"
            )

    def check_citation_cff(self, path: Path) -> None:
        """Check that CITATION.cff has correct version."""
        content = read_file(path)
        if not content:
            self.errors.append(f"[FAIL] CITATION.cff: Could not read {path}")
            return

        # Check version field in YAML (version: X.Y.Z)
        version_pattern = re.compile(r"^version:\s*['\"]?" + re.escape(self.ver) + r"['\"]?\s*$", re.MULTILINE)
        
        if version_pattern.search(content):
            self.successes.append(f"[OK] CITATION.cff: version is {self.ver}")
        else:
            # Find what version is shown
            version_match = re.search(r"^version:\s*['\"]?(\d+\.\d+\.\d+)['\"]?\s*$", content, re.MULTILINE)
            found = version_match.group(1) if version_match else "not found"
            self.errors.append(
                f"[FAIL] CITATION.cff: version does not match. "
                f"Expected {self.ver}, found {found}, file={path}"
            )

    def run(self) -> bool:
        """Run all consistency checks. Returns True if all pass."""
        print(f"=== Release Consistency Check ===")
        print(f"RELEASE_TAG: {self.tag}")
        print(f"Version: {self.ver}")
        print()

        # Find and check Versions pages
        versions_patterns = [
            "docs/en/**/versions*.md",
            "docs/en/**/versions/index.md",
            "docs/en/**/versions/**/index.md",
        ]
        en_versions = find_files(versions_patterns)
        if not en_versions:
            self.errors.append("[FAIL] EN versions: No versions page found")
        else:
            for path in en_versions:
                content = read_file(path)
                if "Current Version" in content or "Latest Release" in content:
                    self.check_versions_page("en", path)
                    break
            else:
                self.errors.append("[FAIL] EN versions: No page with 'Current Version' found")

        ja_versions_patterns = [p.replace("docs/en", "docs/ja") for p in versions_patterns]
        ja_versions = find_files(ja_versions_patterns)
        if not ja_versions:
            self.errors.append("[FAIL] JA versions: No versions page found")
        else:
            for path in ja_versions:
                content = read_file(path)
                if "現在のバージョン" in content or "最新リリース" in content:
                    self.check_versions_page("ja", path)
                    break
            else:
                self.errors.append("[FAIL] JA versions: No page with '現在のバージョン' found")

        # Find and check Cite pages
        cite_patterns = [
            "docs/en/**/cite*.md",
            "docs/en/**/cite/index.md",
        ]
        en_cites = find_files(cite_patterns)
        if not en_cites:
            print("[WARN] EN cite: No cite page found (skipping)")
        else:
            for path in en_cites:
                content = read_file(path)
                if "How to Cite" in content or "Citation" in content or "BibTeX" in content:
                    self.check_cite_page("en", path)
                    break

        ja_cite_patterns = [p.replace("docs/en", "docs/ja") for p in cite_patterns]
        ja_cites = find_files(ja_cite_patterns)
        if not ja_cites:
            print("[WARN] JA cite: No cite page found (skipping)")
        else:
            for path in ja_cites:
                content = read_file(path)
                if "引用" in content or "Cite" in content or "BibTeX" in content:
                    self.check_cite_page("ja", path)
                    break

        # Check CITATION.cff
        citation_cff = Path("CITATION.cff")
        if citation_cff.exists():
            self.check_citation_cff(citation_cff)
        else:
            print("[WARN] CITATION.cff not found (skipping)")

        # Print results
        print()
        print("=== Results ===")
        for msg in self.successes:
            print(msg)
        for msg in self.errors:
            print(msg)
        
        print()
        if self.errors:
            print(f"FAILED: {len(self.errors)} error(s), {len(self.successes)} passed")
            return False
        else:
            print(f"PASSED: All {len(self.successes)} checks passed")
            return True


def main():
    tag = get_release_tag()
    checker = ConsistencyChecker(tag)
    success = checker.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
