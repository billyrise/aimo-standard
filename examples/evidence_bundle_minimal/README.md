# Evidence Bundle (minimal example)

This folder contains a minimal Evidence Bundle example that conforms to the [Evidence Bundle](https://standard.aimoaas.com/artifacts/evidence-bundle/) structure and [Minimum Evidence Requirements](https://standard.aimoaas.com/artifacts/minimum-evidence/).

## Bundle structure

- **root.json**: Root package (version, dictionary, evidence; optional request, review, change_log). Valid against `aimo-standard.schema.json`.
- **dictionary.json**: Standalone dictionary for reference; the root file embeds the dictionary inline.

## How to run the validator

From the repository root:

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

Expected output: `OK`

## Schema and docs

- Schemas: `schemas/jsonschema/` (aimo-standard.schema.json, aimo-ev.schema.json, aimo-dictionary.schema.json).
- Evidence Bundle and Minimum Evidence: docs under Artifacts (evidence-bundle.md, minimum-evidence.md).
