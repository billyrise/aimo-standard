---
description: AIMO Standard version history. Official frozen releases with auditor-ready PDFs, machine-readable artifacts, checksums, and build provenance attestations.
---

# Versions

Official releases are frozen snapshots published with auditor-ready PDFs and machine-readable artifacts.

## Latest Release

!!! success "Current Version"
    **v0.1.1** (2026-02-04) — [View Documentation](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.1.1)

## Version History

| Version | Date | Release Notes | PDF (EN) | PDF (JA) | Artifacts | Checksums |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.1.1** | 2026-02-04 | [Changelog](../current/08-changelog.md#version-011) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.1/SHA256SUMS.txt) |
| **v0.1.0** | 2026-02-03 | [Changelog](../current/08-changelog.md#version-010) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/SHA256SUMS.txt) |
| **v0.0.3** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.3/SHA256SUMS.txt) |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Data Source"
    This version table is synchronized with [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Each release tag (`vX.Y.Z`) corresponds to a frozen snapshot of the specification.

## /latest vs versioned URLs — avoid wrong citations

| URL | Use | Audit / evidence |
|-----|-----|------------------|
| **`/X.Y.Z/`** (e.g. `/0.1.1/`) | Frozen snapshot; never changes. | **MUST** use for audit citations and reproducible evidence. |
| **`/latest/`** | Redirect to the current release; updates when a new tag is released. | Reference only; **not recommended** for audit evidence (target can change). |

The **authoritative definition of "latest"** is the [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) **latest** tag. The site path `/latest/` is a redirect that points to that release. Only the **release workflow** (triggered by a tag push) updates `/latest/`; see [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

| Source | Role |
|--------|------|
| **GitHub Release latest tag** | SSOT — the only definition of "current release" |
| **Versions table** (this page) | Synchronized with releases via release workflow; must match the tag before deploy |
| **Changelog** | Normative change history; release notes reference it |
| **Site `/latest/`** | Redirect to the same version as GitHub Release latest |

For release process details, see [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) and the [release workflow](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml). The Versions table and Changelog are updated as part of release preparation so that they always match the deployed version.

## For auditors: Canonical URL and version pinning

To cite a specific version in audit reports and ensure reproducibility:

1. **Canonical URL**: Use the frozen documentation URL for that version, e.g.  
   `https://standard.aimoaas.com/0.1.1/` (replace `0.0.3` with the version you used).  
   **For v0.1.1 and later**: Prefer citing the versioned URL (e.g. `https://standard.aimoaas.com/0.1.1/`) rather than `/latest/` for audit evidence, so the snapshot is unambiguous.
2. **Version pinning**: Record the **release tag** (e.g. `v0.1.1`) and optionally the **commit hash** from the [GitHub Release](https://github.com/billyrise/aimo-standard/releases) page. This allows independent verification that the specification snapshot matches the release assets (PDF, ZIP, checksums).
3. **Evidence alignment**: State in your submission which AIMO Standard version (e.g. `v0.1.1`) your evidence bundle aligns with, and obtain the validator and schemas from that same release.

## Version layers

AIMO Standard uses three version concepts. For the current release they are aligned; future releases may version them independently.

| Layer | Description | Where it appears |
|-------|-------------|------------------|
| **Standard version** (site/release) | The release tag and documentation snapshot (e.g. `v0.1.1`). | Versions table, GitHub Releases, `/X.Y.Z/` URLs. |
| **Taxonomy schema version** | Version of the code system and taxonomy/schema definitions. | `taxonomy_version` in manifests; schema `$id` or docs. |
| **Dictionary content version** | Version of the dictionary entries (codes and definitions). | Dictionary metadata; same as taxonomy for 0.0.x. |

When citing "AIMO Standard vX.Y.Z", the **Standard version** is the one that defines the canonical snapshot. The Validator and Minimum Evidence Requirements refer to the artifacts and schemas of that release.

## Verification Procedure

Auditors and implementers should verify download integrity using SHA-256 checksums:

### 1. Download Release Assets

=== "Linux / macOS"

    ```bash
    # Download all assets for a specific version
    VERSION=v0.1.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Download all assets for a specific version
    $VERSION = "v0.1.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Verify Checksums

=== "Linux"

    ```bash
    # Verify all downloaded files against checksums
    sha256sum -c SHA256SUMS.txt

    # Expected output (all should show "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Verify all downloaded files against checksums
    shasum -a 256 -c SHA256SUMS.txt

    # Expected output (all should show "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verify each file
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Compare Hash output with SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Manual Verification (Alternative)

=== "Linux"

    ```bash
    # Compute hash for a specific file
    sha256sum trust_package.pdf

    # Compare output with SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Compute hash for a specific file
    shasum -a 256 trust_package.pdf

    # Compare output with SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Compute hash for a specific file
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # View checksums file
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "For Auditors"
    Always obtain the checksums file directly from the official GitHub Release, not from the submitting party. This ensures independent verification.

### 4. Verify Build Provenance (Attestation)

All release assets include cryptographically signed build provenance attestations generated by GitHub Actions. This allows you to verify that assets were built in the official repository without tampering.

**Prerequisites**: Install [GitHub CLI](https://cli.github.com/) (`gh`)

```bash
# Download release assets using GitHub CLI
VERSION=v0.1.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Verify attestation for each asset
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Expected output** (success):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Offline verification** (air-gapped environments):

```bash
# First, download the trusted root (requires network once)
gh attestation trusted-root > trusted-root.jsonl

# Then verify offline
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "What attestation proves"
    Build provenance attestation cryptographically proves that the release assets were:

    1. Built by GitHub Actions (not a developer's local machine)
    2. Built from the official `billyrise/aimo-standard` repository
    3. Built from the exact commit associated with the release tag
    4. Not modified after the build completed

## Compatibility

AIMO Standard follows [Semantic Versioning](https://semver.org/) (SemVer):

| Change Type | Version Bump | Impact |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Breaking changes — migration required |
| **MINOR** | 0.X.0 | Backward-compatible additions |
| **PATCH** | 0.0.X | Fixes and clarifications |

For the **operational policy** (URL semantics and MUST rules), see [Versioning & Reference Policy](../current/00-versioning-reference-policy.md). For the complete versioning policy, see [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migration

When upgrading between versions with breaking changes:

1. Check the [Changelog](../current/08-changelog.md) for breaking changes
2. Review the [Migration Guide](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) for specific upgrade paths
3. Update your Evidence Bundle to align with the new schema requirements
4. Re-run the validator to verify compliance

!!! warning "Breaking Changes"
    MAJOR version updates may require changes to existing Evidence Bundles. Always review the migration guide before upgrading.

## Versioned Documentation Snapshots

Each release creates a frozen documentation snapshot accessible at:

- Production: `https://standard.aimoaas.com/{version}/` (e.g., `/0.1.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### URL Types and Their Meaning

| URL Pattern | Description | For Audit Citations? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (e.g., `/0.1.1/`) | **Frozen release** — immutable snapshot | **Yes** (preferred) |
| `/latest/` | **Alias** — redirects to most recent release | Yes (resolves to `/X.Y.Z/`) |
| `/dev/` | **Preview** — unreleased main branch content | **No** (not for citations) |

!!! warning "Understanding `/latest/` vs `/dev/`"
    - **`/latest/`** is an alias (redirect) to the most recent **released** version. It is safe for citations as it resolves to a frozen snapshot.
    - **`/dev/`** reflects the current `main` branch and may contain **unreleased changes**. Never cite `/dev/` in audit reports.

### FAQ

??? question "Why is `/latest/` not a version number?"
    `/latest/` is a convenience alias that always redirects to the most recent stable release (e.g., `/0.1.1/`). This allows users to bookmark a single URL while automatically getting the current version. For formal audits requiring immutability, cite the explicit version URL instead.

??? question "Which URL should auditors cite?"
    - **Formal audits (immutability required)**: Use `/X.Y.Z/` (e.g., `https://standard.aimoaas.com/0.1.1/standard/current/`)
    - **General references**: `/latest/` is acceptable as it redirects to the current release
    - **Never cite**: `/dev/` (unreleased, subject to change)

??? question "What if `/latest/` shows different content than expected?"
    This would be a deployment bug. If you suspect `/latest/` differs from the most recent [GitHub Release](https://github.com/billyrise/aimo-standard/releases), please [report an issue](https://github.com/billyrise/aimo-standard/issues). The `/latest/` alias should always redirect to the most recent tagged release.

## Resources

- **[Releases Hub](../../releases/index.md)** — Submission preparation, auditor verification, non-overclaim statement
- **[Trust Package](../../governance/trust-package.md)** — Auditor-ready assurance materials
- **[Changelog (detailed)](../current/08-changelog.md)** — Full change history with deprecation tracking
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Complete versioning policy
