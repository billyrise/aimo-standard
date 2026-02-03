# Editing Policy

## Development: English Only
- **During development**, update **English docs only** (`docs/en/`).
- Do not update other locales (ja, es, fr, de, pt, it, zh, zh-TW, ko) in day-to-day edits.
- This keeps a single source of truth and avoids drift until release.

## Normative language (shall / should / may)
- In **normative** standard text, use **shall** for mandatory requirements (MUST), **should** for recommended practice (RECOMMENDED), and **may** for optional (MAY). Do not use "must" or "can" where the standard uses RFC 2119-style language; keep normative and informative clearly separated.
- See `source_pack/00_manifest.md` for which content is Normative vs Informative.

## English Canonical
- English `.md` files under `docs/en/` are canonical.
- Other locales live under `docs/<locale>/` (folder structure; see mkdocs i18n).

## Translation at Release
- **When creating a new version** (bumping version number, adding tag `vX.Y.Z`), run **full translation to all other languages** so the release ships with all locales in sync.
- See [02-release-process.md](02-release-process.md) for when and how to run translation as part of release.

## i18n Sync
- At release time, all built locales must be present and pass lint.
- Heading levels must match across locales (enforced by `tooling/checks/lint_i18n.py`).

## Generated Outputs
- `site/` and `dist/` are generated; never commit them.

## PR Checklist (Required)
- [ ] Updated docs (EN only during development)
- [ ] Translation: only at release (see 02-release-process); PRs for main may leave other locales as-is
- [ ] Updated schemas/templates/examples if applicable
- [ ] Updated changelog
- [ ] Validator tests pass
- [ ] i18n lint and schema lint pass (at release, all locales must pass)
