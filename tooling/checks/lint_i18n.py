import sys
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")

def extract_headings(p: Path):
    headings = []
    for line in p.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line.strip())
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headings.append((level, text))
    return headings

def main():
    errors = []
    en_files = sorted([p for p in DOCS.rglob("*.md") if not p.name.endswith(".ja.md")])

    for en in en_files:
        ja = en.with_name(en.stem + ".ja.md")
        if not ja.exists():
            errors.append(f"Missing JA file: {ja.relative_to(ROOT)} (for {en.relative_to(ROOT)})")
            continue

        en_h = extract_headings(en)
        ja_h = extract_headings(ja)

        en_levels = [lv for (lv, _) in en_h]
        ja_levels = [lv for (lv, _) in ja_h]

        if en_levels != ja_levels:
            errors.append(
                "Heading level mismatch:\n"
                f"  EN: {en.relative_to(ROOT)}\n"
                f"  JA: {ja.relative_to(ROOT)}\n"
                f"  EN levels: {en_levels}\n"
                f"  JA levels: {ja_levels}\n"
            )

    if errors:
        print("i18n lint failed:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)

    print("i18n lint OK")
    sys.exit(0)

if __name__ == "__main__":
    main()
