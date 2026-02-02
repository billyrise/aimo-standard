# Editing Policy

## English Canonical
- English `.md` files are canonical.
- Japanese translations must exist as `.ja.md` files (same base name).

## i18n Sync
- Missing `.ja.md` is an error.
- Heading levels must match (enforced by `tooling/checks/lint_i18n.py`).

## Generated Outputs
- `site/` and `dist/` are generated; never commit them.

## PR Checklist (Required)
- [ ] Updated docs (EN)
- [ ] Updated translation files (JA) or clearly marked as pending (but files must exist)
- [ ] Updated schemas/templates/examples if applicable
- [ ] Updated changelog
- [ ] Validator tests pass
- [ ] i18n lint and schema lint pass
