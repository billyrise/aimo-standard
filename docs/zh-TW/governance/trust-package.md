---
description: AIMO Trust Package - Auditor-ready materials bundle. Minimum documentation for auditors, legal, and IT security to assess AI governance adoption readiness.
---

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

- **Conformance**: how to claim compliance and what levels mean — [Conformance](../../conformance/)
- **Coverage Map**: mapping to external standards — [Coverage Map index](../../coverage-map/), [Coverage Map methodology](../../coverage-map/methodology/)
- **Standard**: normative requirements and definitions — [Standard (Current)](../../standard/current/)
- **Taxonomy**: 8-dimension classification system for AI governance — [Taxonomy](../../standard/current/03-taxonomy/), [Codes](../../standard/current/04-codes/), [Dictionary](../../standard/current/05-dictionary/)
- **Evidence Bundle**: structure, TOC, traceability — [Evidence Bundle](../../artifacts/evidence-bundle/)
- **Minimum Evidence Requirements**: MUST-level checklist by lifecycle — [Minimum Evidence Requirements](../../artifacts/minimum-evidence/)
- **ISO/IEC 42001 Certification Readiness Toolkit**: fastest path to audit-ready evidence aligned to ISO 42001 — [ISO 42001 Certification Readiness Toolkit](../../artifacts/iso-42001-certification-readiness-toolkit/). The toolkit supports preparation only; certification decisions are made by accredited certification bodies.
- **Validator**: rules and reference checks — [Validator](../../validator/)
- **Examples**: audit-ready sample bundles — [Examples](../../examples/)
- **Releases**: change history and distribution — [Releases](../../releases/)
- **Governance**: policies, security, licensing — [Governance](../../governance/)

## Minimum set for audit-readiness

| Item | Where to find it | Outcome / what it proves |
| --- | --- | --- |
| Conformance levels | [Conformance](../../conformance/) | How to claim compliance and the scope of evidence required |
| Coverage mapping | [Coverage Map index](../../coverage-map/), [Coverage Map methodology](../../coverage-map/methodology/) | Explainability against external regulations and standards |
| Taxonomy & Dictionary | [Taxonomy](../../standard/current/03-taxonomy/), [Codes](../../standard/current/04-codes/), [Dictionary](../../standard/current/05-dictionary/) | Classification system for AI systems (8 dimensions, 91 codes) |
| Evidence artifacts | [Evidence Bundle](../../artifacts/evidence-bundle/), [Minimum Evidence](../../artifacts/minimum-evidence/), [EV Template](../../standard/current/06-ev-template/) | What data must exist to support traceability |
| Validator checks | [Validator](../../validator/) | How to verify internal consistency and completeness |
| Example bundle | [Examples](../../examples/) | What an audit-ready package looks like in practice |
| Change control | [Releases](../../releases/), [Governance](../../governance/) | How updates are managed and communicated |
| Security / License / Trademarks | [Governance](../../governance/) | Legal and security posture for adoption decisions |

## How to cite

Use the repository README for citation guidance and context; governance links to the authoritative policies.
See [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) and [Governance](../../governance/).

## Artifacts zip contents

The `aimo-standard-artifacts.zip` includes:

- **Taxonomy (SSOT)**: `source_pack/03_taxonomy/` — Dictionary CSV (91 codes), YAML, code system
- **JSON Schemas**: `schemas/jsonschema/` — Machine-readable validation schemas
- **Templates**: `templates/ev/` — Evidence record templates (JSON + Markdown)
- **Examples**: `examples/` — Minimal sample bundles for quick adoption
- **Coverage Map**: `coverage_map/coverage_map.yaml` — Mapping to external standards
- **Validator Rules**: `validator/rules/` — Validation rule definitions
- **Governance docs**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Responsibility boundary

The AIMO Standard provides a structured evidence format and explainability framework. It does **not** provide legal advice, compliance certification, risk assessment, or audit execution.

For the full scope definition, assumptions, and adopter responsibilities, see [Responsibility Boundary](../responsibility-boundary/).

## How to prepare a submission package

Follow these steps to prepare an audit-ready submission:

1. **Generate Evidence Bundle**: Create EV records, Dictionary, Summary, and Change Log per [Evidence Bundle](../../artifacts/evidence-bundle/) and [Minimum Evidence Requirements](../../artifacts/minimum-evidence/). For ISO 42001–oriented readiness, see the [ISO 42001 Certification Readiness Toolkit](../../artifacts/iso-42001-certification-readiness-toolkit/).
2. **Run Validator**: Execute `python validator/src/validate.py bundle/root.json` to check structural consistency. Fix any errors before proceeding.
3. **Create Checksums**: Generate SHA-256 checksums for all submission files:

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **Package Artifacts**: Create a zip archive of your evidence bundle:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Reference Release Version**: Note which AIMO Standard version (e.g., `v1.0.0`) your bundle aligns with.
6. **Deliver**: Provide the zip, checksums, and version reference to your auditor or compliance function.

For release assets and verification, see [Releases](../../releases/).

## Non-overclaim statement

!!! warning "Important: No certification, no assurance, no legal compliance claim"
    - AIMO Standard defines an **evidence packaging and validation format**. It does not certify compliance with laws or standards.
    - Audit/assurance opinions remain the responsibility of independent auditors and the adopting organization.
    - **Appropriate claim:** "An Evidence Bundle was produced according to AIMO Standard v0.1.2 and structurally validated by the AIMO Validator."
    - **Inappropriate claim:** <!-- UNACCEPTABLE_CLAIMS_EXAMPLES --> "EU AI Act compliant", "ISO 42001 certified", "government approved". <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

See [Responsibility Boundary](../responsibility-boundary/) for details on scope, assumptions, and adopter responsibilities.

## For auditors: Verification procedure

When receiving an evidence submission, auditors should verify integrity and structure using the following steps:

!!! success "Build Provenance Available"
    All release assets include cryptographically signed build attestations. See [Verification Procedure](../../standard/versions/#4-verify-build-provenance-attestation) for attestation verification steps.

### Step 1: Verify checksums (SHA-256)

=== "Linux"

    ```bash
    # Download or receive SHA256SUMS.txt with the submission
    # Verify all files match their recorded checksums
    sha256sum -c SHA256SUMS.txt

    # Or verify individual files manually:
    sha256sum evidence_bundle.zip
    # Compare output against the value in SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Verify all files match their recorded checksums
    shasum -a 256 -c SHA256SUMS.txt

    # Or verify individual files manually:
    shasum -a 256 evidence_bundle.zip
    # Compare output against the value in SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verify individual files
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Compare the Hash output with SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

If any checksum fails, the submission should be rejected or re-requested.

### Step 2: Verify bundle structure (Validator)

**Prerequisites** (one-time setup):

```bash
# Clone the official AIMO Standard release
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# IMPORTANT: Use the exact version stated in the submission
# Replace VERSION with the submitter's declared version (e.g., v0.0.1)
VERSION=v0.0.1  # ← Match the version in the submission
git checkout "$VERSION"

# Set up Python environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Version Matching"
    Always use the exact AIMO Standard version stated in the submission. Using a different version may cause validation mismatches due to schema or rule changes between versions.

**Run validation**:

```bash
# Extract the submitted bundle
unzip evidence_bundle.zip -d bundle/

# Run validator against the bundle's root.json
python validator/src/validate.py bundle/root.json

# Expected output: "validation OK" or list of errors
```

**Example** (using built-in sample):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

The validator checks:

- Required files exist (EV records, Dictionary)
- JSON files conform to schema
- Cross-references (request_id, review_id, etc.) are valid
- Timestamps are present and properly formatted

### Step 3: Verify version alignment

Check that the submission references an official AIMO Standard release:

1. Confirm the stated version (e.g., `v0.0.1`) exists at [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. Compare submitted schemas against the release artifacts
3. Note any deviations from the official release

### What to look for

| Check | Pass Criteria | Fail Action |
| --- | --- | --- |
| Checksums match | All `sha256sum -c` checks pass | Reject or re-request |
| Validator passes | No errors from `validate.py` | Request fixes before acceptance |
| Version exists | Release tag exists on GitHub | Clarify version alignment |
| Required fields present | EV records have id, timestamp, source, summary | Request completion |
| Traceability intact | Cross-references resolve correctly | Request linkage fixes |

!!! info "Auditor independence"
    Auditors should obtain the validator and schemas directly from the official AIMO Standard release, not from the submitting party, to ensure verification independence.

## Audit journey

From this page, the recommended audit journey is:

1. **Classification system**: [Taxonomy](../../standard/current/03-taxonomy/) + [Dictionary](../../standard/current/05-dictionary/) — understand the 8-dimension code system
2. **Evidence structure**: [Evidence Bundle](../../artifacts/evidence-bundle/) — understand bundle TOC and traceability
3. **Required evidence**: [Minimum Evidence Requirements](../../artifacts/minimum-evidence/) — MUST-level checklist by lifecycle
4. **Framework alignment**: [Coverage Map](../../coverage-map/) + [Methodology](../../coverage-map/methodology/) — see how AIMO maps to external frameworks
5. **Validation**: [Validator](../../validator/) — run structural consistency checks
6. **Download**: [Releases](../../releases/) — get release assets and verify checksums
