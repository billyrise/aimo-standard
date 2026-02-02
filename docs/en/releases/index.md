---
description: AIMO Standard releases - Download versioned PDFs, artifacts, and checksums. Changelog, migration guides, and build provenance attestations.
---

# Releases

This section is a hub for versioned releases, changelog, migration, and distribution artifacts.

## Download Latest Release

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)**

## Release Assets

Each official release (`vX.Y.Z` tag) includes:

| Asset | Description |
| --- | --- |
| `trust_package.pdf` | English Trust Package — auditor-ready assurance materials |
| `trust_package.ja.pdf` | Japanese Trust Package |
| `aimo-standard-artifacts.zip` | Schemas, templates, examples, validator rules |
| `SHA256SUMS.txt` | SHA-256 checksums for all assets |

### Verifying Downloads

After downloading, verify file integrity using checksums:

=== "Linux"

    ```bash
    # Download the checksums file
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verify a specific file
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # Or verify manually:
    sha256sum trust_package.pdf
    # Compare output with SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Download the checksums file
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verify a specific file
    shasum -a 256 -c SHA256SUMS.txt

    # Or verify manually:
    shasum -a 256 trust_package.pdf
    # Compare output with SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Download the checksums file
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Verify a specific file
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Compare the Hash output with SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

## Artifacts Zip Contents

The `aimo-standard-artifacts.zip` contains:

- `schemas/jsonschema/*` — JSON Schemas for validation
- `templates/ev/*` — Evidence templates (JSON + Markdown)
- `examples/*` — Sample evidence bundles
- `coverage_map/coverage_map.yaml` — External standards mapping
- `validator/rules/*` — Validation rule definitions
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.

## Resources

- **Version History Table**: [Standard > Versions](../standard/versions/index.md) — version table with direct links to all release assets (PDF, ZIP, SHA256)
- **Changelog (spec)**: [Standard > Current > Changelog](../standard/current/08-changelog.md) — normative and non-normative change history.
- **Release process**: tagging `vX.Y.Z`, CI build, PDF under `dist/`, checksums, GitHub Release assets. See [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) and [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) in the repository.
- **Migration guide**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — upgrade paths for breaking changes.

For governance and versioning policy, see [Governance](../governance/index.md).

## Preparing your submission package

When preparing evidence for audit submission:

1. **Create your Evidence Bundle**: Follow [Evidence Bundle](../artifacts/evidence-bundle.md) and [Minimum Evidence Requirements](../artifacts/minimum-evidence.md) to create EV records, Dictionary, Summary, and Change Log.
2. **Run the Validator**: Execute `python validator/src/validate.py bundle/root.json` to check structural consistency. Fix all errors before proceeding.
3. **Generate Checksums**: Create SHA-256 checksums for verification:

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
4. **Package**: Create a zip archive of your bundle directory.
5. **Document version alignment**: Note which AIMO Standard release (e.g., `v1.0.0`) your evidence aligns with.
6. **Deliver**: Provide the package, checksums, and version reference to your auditor.

For the complete preparation guide, see [Trust Package](../governance/trust-package.md).

## For auditors: Verification procedure

Auditors receiving evidence submissions should verify integrity and structure:

1. **Verify checksums**: Run checksum verification (Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`) to confirm file integrity
2. **Run validator**: Execute `python validator/src/validate.py bundle/root.json` to check structure
3. **Confirm version**: Verify the stated AIMO Standard version exists at [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "Obtain tools independently"
    Auditors should download the validator and schemas directly from the official AIMO Standard release, not from the submitting party.

For the full verification procedure, see [Trust Package](../governance/trust-package.md).

## Non-overclaim statement

!!! warning "Important"
    The AIMO Standard supports **explainability and evidence readiness**. It does **not** provide legal advice, guarantee compliance, or certify conformity to any regulation or framework. Adopters must verify claims against authoritative texts and obtain professional advice as appropriate.

See [Responsibility Boundary](../governance/responsibility-boundary.md) for scope, assumptions, and adopter responsibilities.
