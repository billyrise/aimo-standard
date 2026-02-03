#!/usr/bin/env python3
"""
Public /latest/ drift check.

Compares the version that the public site /latest/ redirects to against the
latest Git tag (v*). Used by monitor-latest-drift.yml to fail when they diverge.

Usage:
    python tooling/checks/check_public_latest_drift.py [--base-url URL]

Exit codes:
    0 - Public /latest/ points to the same version as the latest tag
    1 - Drift: /latest/ points to a different version (or fetch/parse failed)
    2 - Configuration / environment error
"""

import argparse
import re
import subprocess
import sys
import urllib.request
from typing import Optional

DEFAULT_BASE_URL = "https://standard.aimoaas.com"


def fetch_latest_redirect_version(base_url: str) -> Optional[str]:
    """Fetch /latest/ HTML and extract the version it redirects to (e.g. 0.0.3)."""
    url = f"{base_url.rstrip('/')}/latest/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "aimo-standard-drift-check/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}", file=sys.stderr)
        return None

    # Redirect target: url=../0.0.3/ or href="../0.0.3/" or "0.0.3/"
    patterns = [
        r'url=(?:\.\./)*(\d+\.\d+\.\d+)/',
        r'href=["\']?(?:\.\./)*(?:\.\./)*(\d+\.\d+\.\d+)/',
        r'["\']/(\d+\.\d+\.\d+)/["\']',
    ]
    for pat in patterns:
        m = re.search(pat, html)
        if m:
            return m.group(1)
    print("[ERROR] Could not extract version from /latest/ HTML", file=sys.stderr)
    return None


def get_latest_tag_version(remote: str = "origin") -> Optional[str]:
    """Return the latest semver version from remote tags v* (e.g. 0.1.0)."""
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--tags", remote, "refs/tags/v*"],
            capture_output=True,
            text=True,
            timeout=10,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"[ERROR] git ls-remote failed: {e}", file=sys.stderr)
        return None

    # refs/tags/v0.0.1, refs/tags/v0.1.0, etc. — no dereferenced (^{})
    tags = []
    for line in out.stdout.strip().splitlines():
        ref = line.split("\t")[-1]
        m = re.match(r"refs/tags/v(\d+\.\d+\.\d+)$", ref)
        if m and not ref.endswith("^{}"):
            tags.append(m.group(1))

    if not tags:
        print("[ERROR] No v* tags found on remote", file=sys.stderr)
        return None

    def semver_key(v: str) -> tuple:
        parts = v.split(".")
        return (int(parts[0]), int(parts[1]), int(parts[2])) if len(parts) == 3 else (0, 0, 0)

    latest = max(tags, key=semver_key)
    return latest


def main() -> int:
    parser = argparse.ArgumentParser(description="Check public /latest/ matches latest tag")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Site base URL (default: {DEFAULT_BASE_URL})",
    )
    args = parser.parse_args()

    public_ver = fetch_latest_redirect_version(args.base_url)
    if public_ver is None:
        return 1

    tag_ver = get_latest_tag_version()
    if tag_ver is None:
        return 2

    print(f"Public /latest/ -> {public_ver}")
    print(f"Latest tag (v*)  -> {tag_ver}")

    if public_ver != tag_ver:
        print("", file=sys.stderr)
        print("[FAIL] Drift: /latest/ does not point to latest release.", file=sys.stderr)
        print(f"       Public: {public_ver}  Expected: {tag_ver}", file=sys.stderr)
        print("       Fix by pushing a release tag (v*) so release workflow runs.", file=sys.stderr)
        return 1

    print("OK: /latest/ matches latest tag.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
