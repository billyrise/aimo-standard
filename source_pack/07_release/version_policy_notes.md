# Version Policy Notes (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document summarizes the versioning policy from `VERSIONING.md`. It is a reference for authoring, not a replacement for the official policy.

---

## Source Document

The official versioning policy is defined in `VERSIONING.md` at the repository root.

---

## SemVer Rules Summary

The AIMO Standard follows Semantic Versioning (SemVer):

| Version component | When to increment | Examples |
| --- | --- | --- |
| **MAJOR** (X.0.0) | Breaking changes to schemas, codes, or normative requirements | Schema field removed, required field added, code semantics changed |
| **MINOR** (0.X.0) | Backward-compatible additions | New optional field, new code value, new optional schema |
| **PATCH** (0.0.X) | Backward-compatible fixes and clarifications | Typo fix, validator bug fix, documentation clarification |

---

## Scope

This policy applies to:
- Normative specification (`docs/standard/current/`)
- Machine-readable artifacts:
  - Schemas (`schemas/jsonschema/`)
  - Templates (`templates/ev/`)
  - Validator rules (`validator/rules/`)

---

## English Canonical

From `VERSIONING.md`:
> English documentation is canonical. Japanese translations follow and may lag.

---

## Release Requirements

Each official release (`vX.Y.Z` tag) must include:

| Artifact | Description |
| --- | --- |
| Versioned spec site snapshot | MkDocs build frozen via mike |
| PDF | `AIMO-Standard_vX.Y.Z.pdf` under `dist/` |
| Packaged artifacts | Zip with schemas, templates, examples, validator |
| Checksums | SHA-256 checksums for all assets |
| Changelog snapshot | Changelog entry for this version |

---

## Errata / Documentation-Only Revisions

From `VERSIONING.md`:
> If a post-release clarification is needed without changing normative meaning:
> - Publish an errata note under the same version, and
> - Prefer documenting in `docs/standard/current/08-changelog.md` and linking from `versions/`.

---

## Breaking Change Guidelines

Breaking changes (MAJOR version bump) include:

| Change type | Example | Why breaking |
| --- | --- | --- |
| Schema field removed | `tags` field removed from EV | Existing payloads become invalid |
| Required field added | `category` now required | Existing payloads missing field |
| Type changed | `timestamp` from string to object | Existing payloads have wrong type |
| Validation rule tightened | New cross-reference validation | Previously valid bundles may fail |
| Code semantics changed | `approved` now means conditional | Existing interpretations wrong |

---

## Non-Breaking Change Guidelines

Non-breaking changes include:

| Change type | Example | Why non-breaking |
| --- | --- | --- |
| Optional field added | `metadata` field added | Existing payloads still valid |
| Optional code added | New lifecycle code | Existing codes still valid |
| Documentation clarified | Description improved | No schema/behavior change |
| Validator relaxed | Rule made optional | Existing bundles still pass |
| Bug fixed | Validator edge case fixed | Correct behavior now, was wrong before |

---

## Version Alignment

When creating evidence bundles, adopters should:

1. Note which AIMO Standard version they align with (e.g., `v0.1.0`)
2. Use schemas and templates from that specific release
3. Document version in bundle metadata (`version` field in root.json)

---

## Authoring Notes

- This document summarizes `VERSIONING.md`; it does not replace it.
- For authoritative policy, refer to `VERSIONING.md`.
- Version policy changes require careful consideration and documentation.
