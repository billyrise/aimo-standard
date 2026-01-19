# PDF Generation

Goal:
- Generate official PDF per release: `AIMO-Standard_vX.Y.Z.pdf`
- Store outputs under `dist/` (not committed)

Initial approach:
- A dedicated PDF build step will be implemented in CI.
- The PDF must include: version, release date, tag/commit, license, trademark notice.

Implementation notes:
- For now, PDF generation can be introduced later once site pipeline is stable.
- Keep this directory as the authoritative place for PDF build instructions.
