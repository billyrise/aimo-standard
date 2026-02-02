---
description: AIMO Validator hub - Validation tooling quickstart. Install, run, and interpret results in 30 seconds. Evidence pack validation and compliance checks.
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/validator/index.md
source_hash: cd550ba293855924
translation_date: 2026-02-02
translator: pending
translation_status: needs_translation
---

# Validator

This page is a hub for validation tooling and rules. The normative specification for the validator and its rules is in the Standard.

## Quickstart (30 seconds)

**1. Prerequisites**

```bash
pip install jsonschema   # if not already installed
```

**2. Run validation against a sample bundle**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Read the report and fix errors/warnings**

Example output (success):

```
OK
```

Example output (failure):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Exit codes: `0` = success, `1` = validation errors, `2` = usage error.

---

## What it checks

- **Schema validation**: root object, dictionary, and evidence conform to JSON Schema
- **Dictionary consistency**: all codes exist in taxonomy dictionary
- **Code status**: warns for deprecated codes, errors for removed codes

## What it does NOT check

- **Content accuracy**: validator checks structure, not meaning
- **Compliance guarantee**: passing validation does not guarantee regulatory compliance
- **Human judgment**: context-dependent decisions require human review (see [Human Oversight Protocol](../governance/human-oversight-protocol.md))
- **Automatic log collection**: validator validates submitted evidence; it does not collect logs

---

## Resources

- **Specification**: [Standard > Current > Validator](../standard/current/07-validator.md) — rules, reference checks, and how validation relates to evidence.
- **Rules and implementation**: repository `validator/rules/` (checks), `validator/src/` (reference implementation). Run and CI usage are described in the spec.
- **Interpretation**: what a validation "fail" means for auditors (explained in the spec).

For conformance and artifact usage, see [Conformance](../conformance/index.md) and [Artifacts](../artifacts/index.md).
