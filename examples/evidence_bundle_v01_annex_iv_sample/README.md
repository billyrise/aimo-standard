# Evidence Bundle v0.1 — EU AI Act Annex IV sample

This directory is an **official sample** Evidence Bundle that illustrates how AIMO evidence maps to **EU AI Act Annex IV** technical documentation for high-risk AI systems. It is one of the "10-minute value" minimal packages referenced in the v0.1.1 update plan.

## Purpose

- **EU AI Act**: From August 2026, high-risk AI systems (Annex III) require technical documentation under Article 11(1) and Annex IV (general description, development process, monitoring/control, risk management, conformity, post-market monitoring).
- This sample shows a minimal Evidence Bundle whose root payload contains request, review, evidence, and change_log aligned with Annex IV documentation elements. Use it as a starting point for building conformity packages.

## Structure

Same as the [normative minimal bundle](../evidence_bundle_v01_minimal/README.md):

- **manifest.json** — Bundle manifest (bundle_id, object_index, payload_index, hash_chain, signing).
- **objects/index.json** — Index object.
- **payloads/root.json** — Root payload with dictionary, evidence, request, review, change_log (Annex IV–oriented content).
- **hashes/chain.sha256** — Hash chain; `hash_chain.covers` includes `manifest.json` and `objects/index.json`.
- **signatures/manifest.sig** — Signature file (v0.1: existence only).

## Validation

From repo root:

```bash
python validator/src/validate.py examples/evidence_bundle_v01_annex_iv_sample
```

Must print `OK` and exit 0.

## Profile mapping

The [EU AI Act Annex IV profile](../../coverage_map/profiles/eu_ai_act_annex_iv.json) maps AIMO objects (Summary, dictionary, evidence) to Annex IV fields. See that profile and [evidence-bundle-coverage-map](../../docs/en/artifacts/evidence-bundle-coverage-map.md) for audit questions and mapping details.

## References

- [09-evidence-bundle-structure](../../docs/en/standard/current/09-evidence-bundle-structure.md)
- [Minimum Evidence Requirements](../../docs/en/artifacts/minimum-evidence.md)
- [REPORTS/v0.1.1_update_plan.md](../../REPORTS/v0.1.1_update_plan.md) — EU applicability and Annex IV pull-forward scope
