# Governance

## Single Source of Truth
This GitHub repository is the single source of truth (SSOT). Generated outputs must not be edited manually.

## Change Process
- All changes must be made via PR (even by maintainers).
- PRs must pass:
  - Build (MkDocs)
  - i18n synchronization lint
  - schema lint
  - validator tests

## Normative vs Non-Normative
- Normative: requirements (MUST/SHALL), schema constraints, code definitions, validator rule definitions
- Non-normative: explanations, examples, rationale

## Release Authority
Releases are created only from tags `vX.Y.Z` and must follow `02-release-process.md`.
