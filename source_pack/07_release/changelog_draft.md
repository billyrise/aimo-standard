# Changelog Draft Template (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document provides the template for drafting changelogs. It is aligned with `VERSIONING.md` and `docs/standard/current/08-changelog.md`.

---

## Changelog Entry Template

```markdown
## [vX.Y.Z] - YYYY-MM-DD

### Breaking Changes (MAJOR)

- [Breaking] Description of breaking change
  - Migration: How to migrate from previous version
  - Affected: Schemas, templates, validator rules affected

### Features (MINOR)

- [Feature] Description of new feature
  - Details: Additional context if needed

### Fixes (PATCH)

- [Fix] Description of bug fix or clarification
  - Issue: Reference to issue if applicable

### Documentation

- [Docs] Description of documentation changes
  - Pages: Affected documentation pages

### Internal

- [Internal] Description of internal changes (CI, tooling, etc.)
```

---

## Version Categories

| Category | Version impact | Description |
| --- | --- | --- |
| **Breaking** | MAJOR (X.0.0) | Changes that break backward compatibility |
| **Feature** | MINOR (0.X.0) | New functionality, backward-compatible |
| **Fix** | PATCH (0.0.X) | Bug fixes, clarifications, non-breaking |
| **Docs** | None | Documentation-only changes |
| **Internal** | None | CI, tooling, internal processes |

---

## Migration Guidance Format

For breaking changes, include migration guidance:

```markdown
### Migration from vX.Y.Z to vX+1.0.0

#### Schema changes

| Change | Old | New | Action |
| --- | --- | --- | --- |
| Field renamed | `old_field` | `new_field` | Update all references |
| Field removed | `deprecated_field` | — | Remove from payloads |
| Type changed | `string` | `object` | Restructure data |

#### Validator changes

| Change | Description | Action |
| --- | --- | --- |
| New rule | `new_check` added | Ensure compliance |
| Rule removed | `old_check` deprecated | No action needed |

#### Template changes

| Change | Description | Action |
| --- | --- | --- |
| Field added | `new_optional_field` | Consider populating |
| Format changed | Date format updated | Update generators |
```

---

## Example Changelog Entry

```markdown
## [v0.2.0] - 2026-02-15

### Breaking Changes

- [Breaking] `additionalProperties: false` now enforced on all schemas
  - Migration: Remove any custom fields not defined in schema
  - Affected: `aimo-ev.schema.json`, `aimo-dictionary.schema.json`

### Features

- [Feature] Added `renewal` lifecycle object to root schema
  - Details: Supports re-evaluation tracking per Minimum Evidence Requirements

### Fixes

- [Fix] Corrected timestamp description to specify ISO-8601 format
  - Issue: #42

### Documentation

- [Docs] Added Trust Package PDF generation guide
  - Pages: `docs/governance/trust-package.md`

### Internal

- [Internal] Added `lint_manifest.py` CI check
```

---

## Release Checklist

Before releasing:

- [ ] All changes documented in changelog
- [ ] Version number follows SemVer rules
- [ ] Breaking changes have migration guidance
- [ ] Date is release date (not draft date)
- [ ] English changelog complete
- [ ] Japanese changelog updated (if applicable)

---

## Authoring Notes

- This template is the authoring source for changelog entries.
- User-facing changelog is at `docs/standard/current/08-changelog.md`.
- Breaking changes require special attention and migration documentation.
