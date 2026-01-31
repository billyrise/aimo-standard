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

```bash
# Download the checksums file
curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

# Verify a specific file
sha256sum -c SHA256SUMS.txt --ignore-missing
```

Or manually:

```bash
sha256sum trust_package.pdf
# Compare output with SHA256SUMS.txt
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

- **Changelog (spec)**: [Standard > Current > Changelog](../standard/current/08-changelog.md) — normative and non-normative change history.
- **Versioned snapshots**: [Standard > Versions](../standard/versions/index.md) — frozen releases and past versions.
- **Release process**: tagging `vX.Y.Z`, CI build, PDF under `dist/`, checksums, GitHub Release assets. See [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) and [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) in the repository.
- **Migration and checksums**: documented per release; breaking changes require migration guidance.

For governance and versioning policy, see [Governance](../governance/index.md).
