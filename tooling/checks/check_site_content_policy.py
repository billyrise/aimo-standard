#!/usr/bin/env python3
"""
Site content policy check for AIMO Standard.

Enforces that built site HTML does not regress to "EV as taxonomy dimension":
- Forbidden: EV-001..EV-999 (taxonomy codes); "EV Evidence Type" (en 03/04 only).
- Allowed: EV-YYYYMMDD-NNN (Evidence artifact IDs).
- On 04b-id-policy-namespace only: the single "Previously, the taxonomy used EV-001 … EV-015"
  history block is masked before the EV-\\d{3} check (so that block is allowed).
- Required: LG dimension/codes on taxonomy/codes/dictionary pages; 04b must exist with ID Policy/Namespace.

Run after mkdocs build (site/ must exist). Used in CI to block deploy of old EV taxonomy text.

Usage:
    python tooling/checks/check_site_content_policy.py --site-dir site
    python tooling/checks/check_site_content_policy.py --site-dir site --locales en ja

Exit codes:
    0 - All checks passed (site content policy: OK)
    1 - Forbidden pattern found or required pattern missing
"""

import argparse
import re
import sys
from pathlib import Path

# Pages we inspect (under standard/current/)
CRITICAL_PAGES = [
    "03-taxonomy",
    "04-codes",
    "05-dictionary",
    "06-ev-template",
    "04b-id-policy-namespace",
]

# Forbidden: taxonomy dimension EV (EV-001..EV-999). We allow EV-YYYYMMDD-NNN (artifact ID); mask those first.
ARTIFACT_ID_PATTERN = re.compile(r"EV-\d{8}-\d{3}")
FORBIDDEN_EV_TAXONOMY_CODE = re.compile(r"EV-\d{3}")

# Forbidden in en only: "EV Evidence Type" (dimension name in tables/headings)
FORBIDDEN_EV_EVIDENCE_TYPE = re.compile(r"EV\s+(?:Evidence\s+Type|\|\s*Evidence\s+Type)", re.IGNORECASE)

# Required: LG dimension/codes on 03, 04, 05
REQUIRED_LG_PATTERN = re.compile(r"LG-\d{3}")

# Required on 04b: page must mention Namespace or ID Policy (or anchor id-policy-namespace)
REQUIRED_04B_PATTERN = re.compile(r"Namespace|ID\s+Policy|id-policy-namespace", re.IGNORECASE)

# 04b history block: lines containing "Previously" (en) or "従来" (ja) and EV-001/EV-015 — mask EV-\\d{3} only in that block
HISTORY_START = re.compile(r"Previously|従来|used\s+\*\*EV-001\*\*", re.IGNORECASE)
HISTORY_CONTAINS_EV = re.compile(r"EV-\d{3}")


def discover_locales(site_dir: Path) -> list[str]:
    """Find locale dirs under site/ that contain standard/current/."""
    if not site_dir.is_dir():
        return []
    locales = []
    for d in site_dir.iterdir():
        if d.is_dir() and (d / "standard" / "current").exists():
            locales.append(d.name)
    return sorted(locales)


def find_index(site_dir: Path, locale: str, page: str) -> Path | None:
    """Return path to index.html for (locale, page), or None if missing."""
    p = site_dir / locale / "standard" / "current" / page / "index.html"
    return p if p.exists() else None


def mask_artifact_ids(text: str) -> str:
    """Replace EV-YYYYMMDD-NNN with placeholder so we don't flag them."""
    return ARTIFACT_ID_PATTERN.sub("EV-ARTIFACT-ID", text)


def mask_04b_history_block(content: str) -> str:
    """
    In 04b page content, mask EV-\\d{3} only inside the single "Previously, the taxonomy used EV-001 … EV-015"
    history block (so that block is allowed; any other EV-\\d{3} on 04b still fails).
    """
    lines = content.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if HISTORY_START.search(line):
            # Find end of block: next lines that contain EV-001/EV-015/EV-999 (up to ~15 lines)
            end = i
            for k in range(i, min(i + 15, len(lines))):
                if HISTORY_CONTAINS_EV.search(lines[k]):
                    end = k
            # Mask EV-\\d{3} in lines [i, end+1]
            for k in range(i, min(end + 2, len(lines))):
                masked = mask_artifact_ids(lines[k])
                masked = FORBIDDEN_EV_TAXONOMY_CODE.sub("EV-MASKED", masked)
                out.append(masked)
            i = min(end + 2, len(lines))
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def check_forbidden_ev_codes(content: str, locale: str, page: str, path: Path, is_04b: bool) -> list[str]:
    """Flag EV-001..EV-999 (taxonomy) but not EV-YYYYMMDD-NNN. On 04b, mask history block first."""
    if is_04b:
        content = mask_04b_history_block(content)
    content = mask_artifact_ids(content)
    errors = []
    for m in FORBIDDEN_EV_TAXONOMY_CODE.finditer(content):
        line_no = content[: m.start()].count("\n") + 1
        line_start = content.rfind("\n", 0, m.start()) + 1
        line_end = content.find("\n", m.end())
        if line_end == -1:
            line_end = len(content)
        line = content[line_start:line_end].strip()
        if len(line) > 120:
            line = line[:117] + "..."
        errors.append(f"[{locale}] {page}: forbidden taxonomy code EV-NNN at line ~{line_no}: {line!r}")
    return errors


def check_forbidden_ev_evidence_type(content: str, locale: str, page: str) -> list[str]:
    """Flag 'EV Evidence Type' in en 03-taxonomy / 04-codes only."""
    if locale != "en" or page not in ("03-taxonomy", "04-codes"):
        return []
    errors = []
    for m in FORBIDDEN_EV_EVIDENCE_TYPE.finditer(content):
        line_no = content[: m.start()].count("\n") + 1
        line_start = content.rfind("\n", 0, m.start()) + 1
        line_end = content.find("\n", m.end())
        if line_end == -1:
            line_end = len(content)
        line = content[line_start:line_end].strip()
        if len(line) > 120:
            line = line[:117] + "..."
        errors.append(f"[{locale}] {page}: forbidden 'EV Evidence Type' at line ~{line_no}: {line!r}")
    return errors


def check_required_lg(content: str, locale: str, page: str) -> list[str]:
    """Require at least one LG-NNN on 03-taxonomy, 04-codes, 05-dictionary."""
    if page not in ("03-taxonomy", "04-codes", "05-dictionary"):
        return []
    if not REQUIRED_LG_PATTERN.search(content):
        return [f"[{locale}] {page}: required LG dimension/codes (e.g. LG-001) not found"]
    return []


def check_required_04b(content: str, locale: str, path: Path) -> list[str]:
    """04b must contain Namespace or ID Policy (or id-policy-namespace)."""
    if not REQUIRED_04B_PATTERN.search(content):
        return [f"[{locale}] 04b-id-policy-namespace: required 'Namespace' or 'ID Policy' not found in {path}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check built site HTML for EV/LG content policy (no EV taxonomy regression)."
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=Path("site"),
        help="Path to mkdocs build output (default: site)",
    )
    parser.add_argument(
        "--locales",
        nargs="*",
        default=None,
        help="Locales to check (default: auto-detect from site dir)",
    )
    args = parser.parse_args()
    site_dir = args.site_dir.resolve()

    if not site_dir.is_dir():
        print(f"ERROR: site dir not found: {site_dir}")
        print("Run after: python -m mkdocs build --strict")
        return 1

    locales = args.locales or discover_locales(site_dir)
    if not locales:
        print("ERROR: no locales found under site dir (no standard/current/ subdirs)")
        return 1

    all_errors: list[str] = []

    for locale in locales:
        for page in CRITICAL_PAGES:
            path = find_index(site_dir, locale, page)
            if path is None:
                if page == "04b-id-policy-namespace":
                    all_errors.append(f"[{locale}] 04b-id-policy-namespace: index.html missing")
                continue
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                all_errors.append(f"[{locale}] {page}: failed to read {path}: {e}")
                continue

            is_04b = page == "04b-id-policy-namespace"
            # Forbidden: EV taxonomy codes (all locales, all critical pages; on 04b history block is masked)
            all_errors.extend(check_forbidden_ev_codes(content, locale, page, path, is_04b))
            # Forbidden: "EV Evidence Type" (en 03/04 only)
            all_errors.extend(check_forbidden_ev_evidence_type(content, locale, page))
            # Required: LG on 03, 04, 05
            all_errors.extend(check_required_lg(content, locale, page))
            # Required: 04b has Namespace/ID Policy
            if is_04b:
                all_errors.extend(check_required_04b(content, locale, path))

    if all_errors:
        print("ERROR: site content policy check failed")
        print("(EV is reserved for Evidence artifact IDs only; taxonomy dimension is LG.)")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("site content policy: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
