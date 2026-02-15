---
description: AIMO Standard examples - End-to-end and minimal sample bundles showing how to assemble evidence artifacts for AI governance audits.
---
<!-- aimo:translation_status=source -->

# Examples

This section points to end-to-end and minimal examples that show how artifacts are assembled.

- **Minimal bundle**: `examples/minimal/` in the repository (e.g., `sample_ev.json`, `sample_dictionary.json`).
- **Evidence Bundle (minimal)**: `examples/evidence_bundle_v01_minimal/` — normative minimal Bundle (manifest, object_index, payload_index, hash_chain, signing); see [Evidence Bundle](../artifacts/evidence-bundle/) and [Minimum Evidence](../artifacts/minimum-evidence/).
- **Evidence Bundle (EU AI Act Annex IV sample)**: `examples/evidence_bundle_v01_annex_iv_sample/` — official sample aligned with EU AI Act Annex IV technical documentation for high-risk AI; same structure as minimal, with root payload and an Annex IV technical documentation payload (`payloads/ANNEXIV_technical_documentation.md`). The bundle includes `signatures/` and `hashes/` and satisfies normative Evidence Bundle v0.1 path and coverage requirements. See [EU AI Act mapping](../coverage-map/eu-ai-act/) and profile `coverage_map/profiles/eu_ai_act_annex_iv.json`.
- **Schema alignment**: validate against `schemas/jsonschema/` and [Standard](../standard/current/).
- **Audit-ready packaging**: see the [Trust Package](../governance/trust-package/).

### GPAI CoP evidence bundle outline

For **EU GPAI Code of Practice** alignment, attach the **Model Documentation Form** (or equivalent) as an external form:

1. Add the form file (e.g. PDF or DOC) under `payloads/` and assign a stable `logical_id` (e.g. `GPAI_MODEL_DOC_FORM`) in the bundle `manifest.json` `payload_index`.
2. Record the file path, `sha256`, `mime`, and `size` in the payload_index so the bundle remains integrity-verifiable.
3. Reference the form in your coverage map or handoff index so auditors can trace between the GPAI form and AIMO taxonomy/bundle objects.

Profile: `coverage_map/profiles/eu_gp_ai_cop.json`. See [EV Template — External Forms](../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) and [Procurement & Disclosure Overlays](../coverage-map/procurement-and-disclosure/) for UK/Japan overlays.

Detailed scenario coverage is added in later change units.
