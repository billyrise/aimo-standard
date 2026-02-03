---
description: AIMO Standard examples - End-to-end and minimal sample bundles showing how to assemble evidence artifacts for AI governance audits.
---

# Examples

This section points to end-to-end and minimal examples that show how artifacts are assembled.

- **Minimal bundle**: `examples/minimal/` in the repository (e.g., `sample_ev.json`, `sample_dictionary.json`).
- **Evidence Bundle (minimal)**: `examples/evidence_bundle_v01_minimal/` — normative minimal Bundle (manifest, object_index, payload_index, hash_chain, signing); see [Evidence Bundle](../artifacts/evidence-bundle.md) and [Minimum Evidence](../artifacts/minimum-evidence.md).
- **Evidence Bundle (EU AI Act Annex IV sample)**: `examples/evidence_bundle_v01_annex_iv_sample/` — official sample aligned with EU AI Act Annex IV technical documentation for high-risk AI; same structure as minimal, with root payload content oriented to Annex IV (general description, development, monitoring, risk management, conformity, post-market monitoring). See [EU AI Act mapping](../coverage-map/eu-ai-act.md) and profile `coverage_map/profiles/eu_ai_act_annex_iv.json`.
- **Schema alignment**: validate against `schemas/jsonschema/` and [Standard](../standard/current/index.md).
- **Audit-ready packaging**: see the [Trust Package](../governance/trust-package.md).

Detailed scenario coverage is added in later change units.
