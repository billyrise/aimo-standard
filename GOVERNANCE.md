# Governance

This document describes the governance structure, decision-making processes, and operational policies for the AIMO Standard project.

## Scope

This governance document covers:

- **Repository management**: How changes are proposed, reviewed, and merged
- **Release process**: How versions are tagged and distributed
- **Content classification**: Normative vs non-normative content
- **Decision authority**: Who approves what types of changes

This document does **not** cover:

- **Legal advice**: Consult qualified legal counsel for regulatory compliance
- **Adopter governance**: How organizations implement AIMO internally
- **Third-party implementations**: Governance of external tools or integrations

## Definitions

| Term | Definition |
| ---- | ---------- |
| **AIMO Standard** | The specification, schemas, templates, and tooling in this repository |
| **SSOT** | Single Source of Truth — this GitHub repository |
| **Normative** | Requirements that MUST/SHALL be followed for conformance |
| **Non-normative** | Explanatory content (examples, rationale, guidance) |
| **Maintainer** | Individual with merge authority for the repository |
| **Contributor** | Anyone submitting changes via pull request |

## Single Source of Truth (SSOT)

This GitHub repository is the **single source of truth** for AIMO Standard.

| Asset | SSOT Location | Generated From |
| ----- | ------------- | -------------- |
| Specification | `docs/en/standard/current/` | — (source) |
| Taxonomy | `data/taxonomy/canonical.yaml` + `i18n/*.yaml` | — (source) |
| Schemas | `schemas/jsonschema/` | — (source) |
| Templates | `templates/` | — (source) |
| Website | `site/` | `docs/` via MkDocs |
| PDFs | GitHub Releases | `docs/` via build scripts |
| Artifacts ZIP | GitHub Releases | `schemas/`, `templates/`, etc. |

**Rule**: Generated outputs (site, PDFs, CSVs) MUST NOT be edited manually. Edit the source, regenerate, and commit.

## Change Process

### Pull Request Requirements

All changes—including those by maintainers—MUST be made via pull request.

| Check | Required | Description |
| ----- | -------- | ----------- |
| MkDocs build | ✅ | `mkdocs build --strict` must pass |
| i18n lint | ✅ | `python tooling/checks/lint_i18n.py` must pass |
| Schema lint | ✅ | `python tooling/checks/lint_schema.py` must pass |
| Baseline audit | ✅ | `python tooling/audit/baseline_audit.py --check` must pass |
| Validator tests | ✅ | Validator test suite must pass |
| Peer review | ✅ | At least one maintainer approval |

### Change Categories

| Category | Examples | Review Requirements |
| -------- | -------- | ------------------- |
| **Normative** | Schema changes, requirement changes, code additions | Maintainer approval + discussion |
| **Non-normative** | Typo fixes, clarifications, examples | Maintainer approval |
| **Tooling** | CI/CD, build scripts, linters | Maintainer approval |
| **i18n** | Translation updates | Maintainer approval + structure match |

### Breaking Changes

Changes that break backward compatibility require:

1. Discussion in an issue before implementation
2. Version bump following [VERSIONING.md](VERSIONING.md)
3. Changelog entry with migration guidance
4. Deprecation period for removed features (when feasible)

## RACI Matrix

| Activity | Maintainers | Contributors | Adopters |
| -------- | :---------: | :----------: | :------: |
| Propose changes | R | R | C |
| Review PRs | R/A | C | — |
| Merge PRs | R/A | — | — |
| Create releases | R/A | — | I |
| Define normative requirements | R/A | C | I |
| Implement in production | — | — | R/A |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

## Normative vs Non-Normative Content

### Normative Content

Normative content defines **requirements** for conformance. Uses RFC 2119 keywords:

- **MUST / SHALL**: Absolute requirement
- **MUST NOT / SHALL NOT**: Absolute prohibition
- **SHOULD / RECOMMENDED**: Strong recommendation with valid exceptions
- **MAY / OPTIONAL**: Truly optional

Normative content includes:

- Requirements in specification chapters
- JSON Schema constraints (`required`, `pattern`, etc.)
- Taxonomy code definitions
- Validator rule definitions

### Non-Normative Content

Non-normative content provides **guidance** without conformance implications:

- Examples and sample bundles
- Explanatory rationale
- Best practices and recommendations
- Coverage map interpretations

## Release Authority

### Release Process

1. Releases are created **only** from tags matching `vX.Y.Z`
2. Tags trigger automated release workflow
3. Release artifacts include:
   - `trust_package.pdf` (English)
   - `trust_package.ja.pdf` (Japanese)
   - `aimo-standard-artifacts.zip`
   - `SHA256SUMS.txt`

### Version Authority

| Version Component | Trigger | Authority |
| ----------------- | ------- | --------- |
| Major (X) | Breaking changes | Maintainer consensus |
| Minor (Y) | New features, non-breaking | Maintainer approval |
| Patch (Z) | Bug fixes, clarifications | Maintainer approval |

See [VERSIONING.md](VERSIONING.md) for detailed versioning policy.

## Decision-Making

### Consensus-Based

Most decisions are made by **lazy consensus**:

1. Proposal is made (issue or PR)
2. Review period (typically 7 days for significant changes)
3. If no objections, proposal is accepted
4. If objections, discussion continues until consensus

### Escalation

For contested decisions:

1. Discussion continues in the issue/PR
2. Maintainers seek to find common ground
3. If unresolved, maintainers vote (majority wins)

## Code of Conduct

All participants must follow the project's [Code of Conduct](CODE_OF_CONDUCT.md).

Violations may result in:

- Warning
- Temporary exclusion
- Permanent exclusion

## Related Resources

- [SECURITY.md](SECURITY.md) — Security policy and vulnerability reporting
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [VERSIONING.md](VERSIONING.md) — Versioning policy
- [TRADEMARKS.md](TRADEMARKS.md) — Trademark usage guidelines
- [Governance (website)](https://standard.aimoaas.com/latest/governance/) — Full governance documentation

## FAQ

**Q: Can I fork and modify AIMO Standard?**
A: Yes, under the Apache-2.0 license terms. See [LICENSE.txt](LICENSE.txt).

**Q: How do I propose a new feature?**
A: Open a GitHub issue describing the feature, use case, and proposed approach.

**Q: Who are the maintainers?**
A: See the repository's contributor list and CODEOWNERS file (if present).

**Q: How often are releases made?**
A: Releases are made as needed, typically after significant changes accumulate.
