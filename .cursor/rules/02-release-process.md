# Release Process

## Policy: Translate at Release
- **Development**: Only English (`docs/en/`) is updated.
- **When creating a new version** (bumping version, tagging `vX.Y.Z`): run **full translation to all other languages** (ja, es, fr, de, pt, it, zh, zh-TW, ko) so the release ships with all locales in sync.
- Translation should happen **before** or **as part of** the release (e.g. in the same PR that bumps version refs, or via a dedicated translation step before tagging).

## Tagging
- Releases are created from tags `vX.Y.Z`.

## Before tagging (release prep)
1. Run translation from English to all locales (e.g. `tooling/i18n/sync_translations.py` or equivalent; see repo tooling).
2. Bump version references (Versions pages, Cite, CITATION.cff) via `prepare-release` workflow or `bump_release_references.py`.
3. Merge release-prep PR, then create and push tag `vX.Y.Z`.

## What CI must do on tag
- Build site
- Freeze version snapshot via mike
- Build PDF: `AIMO-Standard_vX.Y.Z.pdf` (under `dist/`)
- Create checksums (sha256)
- Publish GitHub Release assets
- Add build attestation when available

## Post-release
- Update versions index pages if needed (prefer automation).
