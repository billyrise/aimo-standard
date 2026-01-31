# Trust Package (Assurance Package)

This page bundles the minimum materials auditors, legal, and IT security need to assess adoption readiness.
It is a hub only; detailed Evidence TOC and Coverage tables are maintained in their respective sections.

## Download

**[Download Trust Package PDF (Latest Release)](https://github.com/billyrise/aimo-standard/releases/latest)**

The Trust Package PDF consolidates auditor-ready materials into a single document. Each GitHub Release includes:

- `trust_package.pdf` — English Trust Package
- `trust_package.ja.pdf` — Japanese Trust Package
- `aimo-standard-artifacts.zip` — Schemas, templates, examples, validator rules
- `SHA256SUMS.txt` — Checksums for verification

## What you get

- **Conformance**: how to claim compliance and what levels mean — [Conformance](../conformance/index.md)
- **Coverage Map**: mapping to external standards — [Coverage Map index](../coverage-map/index.md), [Coverage Map methodology](../coverage-map/methodology.md)
- **Standard**: normative requirements and definitions — [Standard (Current)](../standard/current/index.md)
- **Evidence Bundle**: structure, TOC, traceability — [Evidence Bundle](../artifacts/evidence-bundle.md)
- **Minimum Evidence Requirements**: MUST-level checklist by lifecycle — [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- **Validator**: rules and reference checks — [Validator](../validator/index.md)
- **Examples**: audit-ready sample bundles — [Examples](../examples/index.md)
- **Releases**: change history and distribution — [Releases](../releases/index.md)
- **Governance**: policies, security, licensing — [Governance](../governance/index.md)

## Minimum set for audit-readiness

| Item | Where to find it | Outcome / what it proves |
| --- | --- | --- |
| Conformance levels | [Conformance](../conformance/index.md) | How to claim compliance and the scope of evidence required |
| Coverage mapping | [Coverage Map index](../coverage-map/index.md), [Coverage Map methodology](../coverage-map/methodology.md) | Explainability against external regulations and standards |
| Evidence artifacts | [Evidence Bundle](../artifacts/evidence-bundle.md), [Minimum Evidence](../artifacts/minimum-evidence.md), [EV Template](../standard/current/06-ev-template.md) | What data must exist to support traceability |
| Validator checks | [Validator](../validator/index.md) | How to verify internal consistency and completeness |
| Example bundle | [Examples](../examples/index.md) | What an audit-ready package looks like in practice |
| Change control | [Releases](../releases/index.md), [Governance](../governance/index.md) | How updates are managed and communicated |
| Security / License / Trademarks | [Governance](../governance/index.md) | Legal and security posture for adoption decisions |

## How to cite

Use the repository README for citation guidance and context; governance links to the authoritative policies.
See [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) and [Governance](../governance/index.md).

## Artifacts zip contents

The `aimo-standard-artifacts.zip` includes:

- **JSON Schemas**: `schemas/jsonschema/` — Machine-readable validation schemas
- **Templates**: `templates/ev/` — Evidence record templates (JSON + Markdown)
- **Examples**: `examples/` — Minimal sample bundles for quick adoption
- **Coverage Map**: `coverage_map/coverage_map.yaml` — Mapping to external standards
- **Validator Rules**: `validator/rules/` — Validation rule definitions
- **Governance docs**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Important note

This package supports explainability and evidence readiness; it does not itself provide legal advice or guarantee compliance.
