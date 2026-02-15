---
description: AIMO Validator hub - Validation tooling quickstart. Install, run, and interpret results in 30 seconds. Evidence pack validation and compliance checks.
---
<!-- aimo:translation_status=source -->

# Validator

This page is a hub for validation tooling and rules. The normative specification for the validator and its rules is in the Standard.

## Quickstart (30 seconds)

**1. Prerequisites**

```bash
pip install jsonschema   # if not already installed
```

**2. Run validation against a sample bundle**

```bash
# Single root JSON file
python validator/src/validate.py examples/evidence_bundle_minimal/root.json

# Evidence Bundle directory (v0.1 minimal: validates manifest, object_index, payload_index, signing, hash_chain)
python validator/src/validate.py examples/evidence_bundle_v01_minimal
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

**Exit codes**: `0` = success, `1` = validation errors, `2` = usage error (e.g. missing path or options).

---

## Output formats (--format) and CI usage

| Option | Use case | Output |
|--------|----------|--------|
| `default` (omit) | Local inspection | Human-readable message (OK / error list) |
| `--format json` | CI and scripts | Machine-readable JSON (`valid`, `errors`, `warnings`, `path`, `profiles_valid`) |
| `--format sarif` | GitHub Code Scanning | SARIF 2.1.0 (ruleId, level, location, message). Use when feeding results into Code Scanning as a pre-submission gate. |
| `--format audit-json` | Audit attachment (machine-readable) | Validation report with metadata (validator version, AIMO standard version, bundle info, summary, results). Use with `--output <path>` to write to a file. |
| `--format audit-html` | Audit attachment (human-readable) | Same content as HTML for review or printing. You can export to PDF via the browser’s print dialog. Use with `--output <path>` to write to a file. |

**Example: validating the Evidence Bundle v0.1 minimal sample**

```bash
# Local success check
python validator/src/validate.py examples/evidence_bundle_v01_minimal

# Get result as JSON (for CI parsing)
python validator/src/validate.py examples/evidence_bundle_v01_minimal --validate-profiles --format json

# Write SARIF to a file (for Code Scanning upload)
python validator/src/validate.py examples/evidence_bundle_v01_minimal --validate-profiles --format sarif > dist/validator.sarif
```

### Audit report output

For audit attachment, use **audit-json** (machine-readable) or **audit-html** (human-readable, printable). These outputs summarize evidence readiness and integrity checks (bundle manifest, hash chain, signatures, schema validation). They do **not** constitute legal or compliance advice.

- **`--format audit-json`** — JSON report with `report_version`, `generated_at`, `validator`, `aimo_standard`, `bundle`, `summary`, and `results`. Suitable for tooling and archiving.
- **`--format audit-html`** — HTML report with the same information; you can print or save as PDF from your browser.

Use **`--output <path>`** to write the report to a file; if omitted, output is written to stdout.

```bash
# Audit report (JSON) to file
aimo validate <path-to-bundle> --format audit-json --output aimo_validation_report.json

# Audit report (HTML) to file
aimo validate <path-to-bundle> --format audit-html --output aimo_validation_report.html
```

If you run the validator as a script:

```bash
python validator/src/validate.py examples/evidence_bundle_v01_minimal --format audit-json --output aimo_validation_report.json
python validator/src/validate.py examples/evidence_bundle_v01_minimal --format audit-html --output aimo_validation_report.html
```

HTML reports can be converted to PDF using the browser’s print function (e.g. “Save as PDF”). This feature is for evidence readiness and integrity reporting only; it does not provide assurance or legal advice.

**How it appears on GitHub**: The Quality Gate workflow runs the validator with `--format sarif` and uploads the result via `upload-sarif`. When validation fails on a PR, the Security tab (Code Scanning) shows results for `aimo-standard/validation` so you can see which path and which error failed.

---

## What it checks

- **Schema validation**: root object, dictionary, and evidence conform to JSON Schema
- **Dictionary consistency**: all codes exist in taxonomy dictionary
- **Code status**: warns for deprecated codes, errors for removed codes

## What it does NOT check

- **Content accuracy**: validator checks structure, not meaning
- **Compliance guarantee**: passing validation does not guarantee regulatory compliance
- **Human judgment**: context-dependent decisions require human review (see [Human Oversight Protocol](../governance/human-oversight-protocol/))
- **Automatic log collection**: validator validates submitted evidence; it does not collect logs

---

## Resources

- **Specification**: [Standard > Current > Validator](../standard/current/07-validator/) — rules, reference checks, and how validation relates to evidence.
- **Rules and implementation**: repository `validator/rules/` (checks), `validator/src/` (reference implementation). Run and CI usage are described in the spec.
- **Interpretation**: what a validation "fail" means for auditors (explained in the spec).

For conformance and artifact usage, see [Conformance](../conformance/) and [Artifacts](../artifacts/).
