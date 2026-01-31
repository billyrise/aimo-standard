# Versions

Official releases are frozen snapshots published with auditor-ready PDFs and machine-readable artifacts.

## Latest Release

!!! success "Current Version"
    **v0.1.0** (2026-01-31) — [View Documentation](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.1.0)

## Version History

| Version | Date | Release Notes | PDF (EN) | PDF (JA) | Artifacts | Checksums |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.1.0** | 2026-01-31 | [Changelog](../current/08-changelog.md#version-010-2026-01-31) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.1.0/SHA256SUMS.txt) |

!!! note "Data Source"
    This version table is synchronized with [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Each release tag (`vX.Y.Z`) corresponds to a frozen snapshot of the specification.

## Verification Procedure

Auditors and implementers should verify download integrity using SHA-256 checksums:

### 1. Download Release Assets

```bash
# Download all assets for a specific version
VERSION=v0.1.0
BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

curl -LO "${BASE_URL}/trust_package.pdf"
curl -LO "${BASE_URL}/trust_package.ja.pdf"
curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
curl -LO "${BASE_URL}/SHA256SUMS.txt"
```

### 2. Verify Checksums

```bash
# Verify all downloaded files against checksums
sha256sum -c SHA256SUMS.txt

# Expected output (all should show "OK"):
# trust_package.pdf: OK
# trust_package.ja.pdf: OK
# aimo-standard-artifacts.zip: OK
```

### 3. Manual Verification (Alternative)

```bash
# Compute hash for a specific file
sha256sum trust_package.pdf

# Compare output with SHA256SUMS.txt
cat SHA256SUMS.txt
```

!!! tip "For Auditors"
    Always obtain the checksums file directly from the official GitHub Release, not from the submitting party. This ensures independent verification.

## Compatibility

AIMO Standard follows [Semantic Versioning](https://semver.org/) (SemVer):

| Change Type | Version Bump | Impact |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Breaking changes — migration required |
| **MINOR** | 0.X.0 | Backward-compatible additions |
| **PATCH** | 0.0.X | Fixes and clarifications |

For the complete versioning policy, see [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

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

- Production: `https://standard.aimoaas.com/{version}/` (e.g., `/0.1.0/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

The `latest` alias always points to the most recent release.

## Resources

- **[Releases Hub](../../releases/index.md)** — Submission preparation, auditor verification, non-overclaim statement
- **[Trust Package](../../governance/trust-package.md)** — Auditor-ready assurance materials
- **[Changelog (detailed)](../current/08-changelog.md)** — Full change history with deprecation tracking
