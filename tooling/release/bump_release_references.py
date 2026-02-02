#!/usr/bin/env python3
"""
Release References Bumper

Automatically updates version references in documentation files for a new release.
Updates: Versions pages, Cite pages, and CITATION.cff.

Usage:
    python tooling/release/bump_release_references.py --version 0.1.8

Exit codes:
    0 - All updates completed successfully
    1 - No changes made (exploration failed) or validation failed
    2 - Invalid arguments
"""

import argparse
import re
import sys
from glob import glob
from pathlib import Path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Update version references in documentation for a new release"
    )
    parser.add_argument(
        "--version",
        required=True,
        help="New version number (e.g., 0.1.8). Do not include 'v' prefix."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without actually modifying files"
    )
    args = parser.parse_args()
    
    # Validate version format
    if not re.match(r"^\d+\.\d+\.\d+$", args.version):
        print(f"[ERROR] Invalid version format: {args.version}")
        print("Expected format: X.Y.Z (e.g., 0.1.8)")
        sys.exit(2)
    
    return args


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


def write_file(path: Path, content: str, dry_run: bool = False) -> None:
    """Write file contents."""
    if dry_run:
        print(f"[DRY-RUN] Would write to {path}")
        return
    path.write_text(content, encoding="utf-8")


class VersionBumper:
    def __init__(self, new_version: str, dry_run: bool = False):
        self.new_version = new_version
        self.dry_run = dry_run
        self.changes: list[dict] = []
        self.errors: list[str] = []

    def _detect_old_versions(self, content: str) -> set[str]:
        """Detect version strings in content that are NOT the new version."""
        # Find all version patterns
        version_pattern = re.compile(r"\d+\.\d+\.\d+")
        found_versions = set(version_pattern.findall(content))
        # Remove the new version from the set
        found_versions.discard(self.new_version)
        return found_versions

    def _update_version_references(self, content: str, file_path: Path) -> tuple[str, int]:
        """
        Update version references in content.
        Returns (new_content, change_count).
        """
        original_content = content
        change_count = 0
        
        # Detect old versions first
        old_versions = self._detect_old_versions(content)
        
        for old_ver in old_versions:
            # Pattern 1: v0.1.7 -> v{new_version}
            v_pattern = re.compile(r"\bv" + re.escape(old_ver) + r"\b")
            new_content, n = v_pattern.subn(f"v{self.new_version}", content)
            if n > 0:
                change_count += n
                content = new_content

            # Pattern 2: /0.1.7/ -> /{new_version}/
            url_pattern = re.compile(r"/" + re.escape(old_ver) + r"/")
            new_content, n = url_pattern.subn(f"/{self.new_version}/", content)
            if n > 0:
                change_count += n
                content = new_content

            # Pattern 3: version = {0.1.7} (BibTeX) -> version = {new_version}
            bibtex_pattern = re.compile(
                r"(version\s*=\s*\{)" + re.escape(old_ver) + r"(\})"
            )
            new_content, n = bibtex_pattern.subn(rf"\g<1>{self.new_version}\2", content)
            if n > 0:
                change_count += n
                content = new_content

            # Pattern 4: Version 0.1.7 (APA style) -> Version {new_version}
            apa_pattern = re.compile(
                r"(Version\s+)" + re.escape(old_ver) + r"\b",
                re.IGNORECASE
            )
            new_content, n = apa_pattern.subn(rf"\g<1>{self.new_version}", content)
            if n > 0:
                change_count += n
                content = new_content

            # Pattern 5: version: 0.1.7 (YAML) -> version: {new_version}
            yaml_pattern = re.compile(
                r"(^version:\s*['\"]?)" + re.escape(old_ver) + r"(['\"]?\s*$)",
                re.MULTILINE
            )
            new_content, n = yaml_pattern.subn(rf"\g<1>{self.new_version}\2", content)
            if n > 0:
                change_count += n
                content = new_content

        return content, change_count

    def _verify_no_old_versions_remain(self, content: str, file_path: Path) -> bool:
        """
        Verify that no old version references remain in critical sections.
        Returns True if clean, False if old versions found.
        """
        # Find version patterns that are NOT the new version
        remaining_old = self._detect_old_versions(content)
        
        # These old versions might be legitimate historical references
        # We only flag them if they appear in "current" contexts
        suspicious_patterns = []
        
        for old_ver in remaining_old:
            # Check for "Current Version: vX.Y.Z" with old version
            if re.search(
                r"Current Version[:\s]+v?" + re.escape(old_ver),
                content,
                re.IGNORECASE
            ):
                suspicious_patterns.append(f"Current Version with {old_ver}")
            
            # Check for active URL examples (not historical)
            # Look for patterns like "use /X.Y.Z/" or "https://...com/X.Y.Z/"
            if re.search(
                r"(use|visit|access|https?://[^/]+)/" + re.escape(old_ver) + r"/",
                content,
                re.IGNORECASE
            ):
                suspicious_patterns.append(f"Active URL with /{old_ver}/")

        if suspicious_patterns:
            for pattern in suspicious_patterns:
                self.errors.append(
                    f"[WARN] Potential old version in active context: {pattern} in {file_path}"
                )
        
        return len(suspicious_patterns) == 0

    def update_versions_pages(self) -> int:
        """Update EN and JA Versions pages."""
        total_changes = 0
        
        # EN Versions
        en_patterns = [
            "docs/en/**/versions*.md",
            "docs/en/**/versions/index.md",
            "docs/en/**/versions/**/index.md",
        ]
        en_files = find_files(en_patterns)
        for path in en_files:
            content = read_file(path)
            if not content or "Current Version" not in content:
                continue
            
            new_content, count = self._update_version_references(content, path)
            if count > 0:
                write_file(path, new_content, self.dry_run)
                self.changes.append({
                    "file": str(path),
                    "type": "EN Versions",
                    "changes": count
                })
                total_changes += count
                self._verify_no_old_versions_remain(new_content, path)
        
        # JA Versions
        ja_patterns = [p.replace("docs/en", "docs/ja") for p in en_patterns]
        ja_files = find_files(ja_patterns)
        for path in ja_files:
            content = read_file(path)
            if not content:
                continue
            # Check for Japanese version markers
            if "現在のバージョン" not in content and "最新リリース" not in content:
                continue
            
            new_content, count = self._update_version_references(content, path)
            if count > 0:
                write_file(path, new_content, self.dry_run)
                self.changes.append({
                    "file": str(path),
                    "type": "JA Versions",
                    "changes": count
                })
                total_changes += count
                self._verify_no_old_versions_remain(new_content, path)
        
        return total_changes

    def update_cite_pages(self) -> int:
        """Update EN and JA Cite pages."""
        total_changes = 0
        
        # EN Cite
        en_patterns = [
            "docs/en/**/cite*.md",
            "docs/en/**/cite/index.md",
        ]
        en_files = find_files(en_patterns)
        for path in en_files:
            content = read_file(path)
            if not content:
                continue
            # Check for cite markers
            if not any(marker in content for marker in ["How to Cite", "Citation", "BibTeX"]):
                continue
            
            new_content, count = self._update_version_references(content, path)
            if count > 0:
                write_file(path, new_content, self.dry_run)
                self.changes.append({
                    "file": str(path),
                    "type": "EN Cite",
                    "changes": count
                })
                total_changes += count
                self._verify_no_old_versions_remain(new_content, path)
        
        # JA Cite
        ja_patterns = [p.replace("docs/en", "docs/ja") for p in en_patterns]
        ja_files = find_files(ja_patterns)
        for path in ja_files:
            content = read_file(path)
            if not content:
                continue
            # Check for Japanese cite markers
            if not any(marker in content for marker in ["引用", "Cite", "BibTeX", "推奨"]):
                continue
            
            new_content, count = self._update_version_references(content, path)
            if count > 0:
                write_file(path, new_content, self.dry_run)
                self.changes.append({
                    "file": str(path),
                    "type": "JA Cite",
                    "changes": count
                })
                total_changes += count
                self._verify_no_old_versions_remain(new_content, path)
        
        return total_changes

    def update_citation_cff(self) -> int:
        """Update CITATION.cff."""
        citation_path = Path("CITATION.cff")
        if not citation_path.exists():
            print("[INFO] CITATION.cff not found, skipping")
            return 0
        
        content = read_file(citation_path)
        if not content:
            return 0
        
        new_content, count = self._update_version_references(content, citation_path)
        
        # Also update date-released if present
        today = __import__("datetime").date.today().isoformat()
        date_pattern = re.compile(
            r"(^date-released:\s*['\"]?)\d{4}-\d{2}-\d{2}(['\"]?\s*$)",
            re.MULTILINE
        )
        new_content, n = date_pattern.subn(rf"\g<1>{today}\2", new_content)
        if n > 0:
            count += n
        
        if count > 0:
            write_file(citation_path, new_content, self.dry_run)
            self.changes.append({
                "file": str(citation_path),
                "type": "CITATION.cff",
                "changes": count
            })
        
        return count

    def run(self) -> bool:
        """Run all version bumps. Returns True if successful."""
        print(f"=== Version References Bumper ===")
        print(f"Target version: {self.new_version}")
        print(f"Dry run: {self.dry_run}")
        print()

        # Run updates
        versions_changes = self.update_versions_pages()
        cite_changes = self.update_cite_pages()
        citation_cff_changes = self.update_citation_cff()
        
        total_changes = versions_changes + cite_changes + citation_cff_changes

        # Print summary
        print()
        print("=== Changes Summary ===")
        if self.changes:
            for change in self.changes:
                print(f"  {change['type']}: {change['file']} ({change['changes']} replacements)")
        else:
            print("  No changes made")
        
        print()
        print(f"Total replacements: {total_changes}")
        
        # Print warnings
        if self.errors:
            print()
            print("=== Warnings ===")
            for error in self.errors:
                print(error)

        # Validate
        if total_changes == 0:
            print()
            print("[ERROR] No changes were made. Either:")
            print("  - Files are already at the target version, or")
            print("  - File exploration failed (check glob patterns)")
            return False
        
        print()
        if self.dry_run:
            print(f"[DRY-RUN] Would update {len(self.changes)} files with {total_changes} replacements")
        else:
            print(f"[SUCCESS] Updated {len(self.changes)} files with {total_changes} replacements")
        
        return True


def main():
    args = parse_args()
    bumper = VersionBumper(args.version, dry_run=args.dry_run)
    success = bumper.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
