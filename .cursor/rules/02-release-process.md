# Release Process

## Tagging
- Releases are created from tags `vX.Y.Z`.

## What CI must do on tag
- Build site
- Freeze version snapshot via mike
- Build PDF: `AIMO-Standard_vX.Y.Z.pdf` (under `dist/`)
- Create checksums (sha256)
- Publish GitHub Release assets
- Add build attestation when available

## Post-release
- Update versions index pages if needed (prefer automation).
