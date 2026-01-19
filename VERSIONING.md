# Versioning Policy (SemVer)

## Scope
This policy applies to the normative specification and machine-readable artifacts (schemas, templates, validator rules).

## English Canonical
English documentation is canonical. Japanese translations follow and may lag.

## SemVer Rules
- MAJOR: breaking changes to schemas, codes, or normative requirements
- MINOR: backward-compatible additions (new fields with defaults, new optional codes)
- PATCH: backward-compatible fixes and clarifications (including validator bug fixes)

## Releases
- Official releases are tagged as `vX.Y.Z`.
- Each release must include:
  - Versioned spec site snapshot
  - PDF: `AIMO-Standard_vX.Y.Z.pdf`
  - Packaged artifacts (zip) and checksums
  - Changelog snapshot

## Errata / Documentation-Only Revisions
If a post-release clarification is needed without changing normative meaning:
- Publish an errata note under the same version, and
- Prefer documenting in `docs/standard/current/08-changelog.md` and linking from `versions/`.
