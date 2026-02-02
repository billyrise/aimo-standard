# Security Policy

This document describes the security policy for the AIMO Standard repository, including supported versions, vulnerability reporting procedures, and disclosure timelines.

## Scope

This security policy covers:

- **Validator reference implementation** (`validator/`)
- **Build and release tooling** (`tooling/`)
- **JSON schemas** (`schemas/`)
- **Documentation website infrastructure** (MkDocs configuration, CI/CD workflows)

This policy does **not** cover:

- **Specification content**: The normative text of the AIMO Standard is not a security artifact
- **Adopter implementations**: Third-party implementations using AIMO Standard schemas
- **External dependencies**: Report issues in third-party libraries to their maintainers

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest (dev) | ✅ Yes |
| Tagged releases (vX.Y.Z) | ✅ Yes (latest 2 minor versions) |
| Older releases | ❌ No (upgrade recommended) |

## Reporting a Vulnerability

**DO NOT** open a public GitHub issue for security vulnerabilities.

### Reporting Process

1. **Report privately**: Email security concerns to the maintainers via GitHub's private vulnerability reporting feature, or contact the repository owner directly
2. **Include details**: Provide a clear description, steps to reproduce, affected versions, and potential impact
3. **Allow time**: We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days

### What to Expect

| Phase | Timeline | Description |
| ----- | -------- | ----------- |
| Acknowledgment | 72 hours | Confirmation that the report was received |
| Initial assessment | 7 days | Preliminary severity classification and triage |
| Fix development | Varies | Depends on severity and complexity |
| Coordinated disclosure | 90 days max | Public disclosure after fix is available |

### Severity Classification

We use CVSS-based severity classification:

- **Critical/High**: Immediate attention, expedited fix
- **Medium**: Scheduled for next minor release
- **Low/Informational**: Addressed as resources permit

## Disclosure Policy

We follow coordinated disclosure principles:

1. **Private reporting**: Vulnerabilities are reported privately
2. **Fix development**: A fix is developed and tested before disclosure
3. **Public disclosure**: After a fix is available, we publish a security advisory
4. **Credit**: Reporters are credited (unless anonymity is requested)

## Prohibited Actions

The following actions are **prohibited** and may result in exclusion from the project:

- Publishing exploit details before a fix is available (0-day disclosure)
- Using vulnerabilities to attack production systems
- Social engineering project maintainers
- Denial-of-service attacks against project infrastructure

## Security Measures in Place

- **CI/CD checks**: Automated linting, schema validation, and build verification
- **Dependency scanning**: Regular review of third-party dependencies
- **Signed releases**: Tagged releases with checksums (SHA256SUMS.txt)
- **Review requirements**: All changes require PR review before merging

## Related Resources

- [Governance](https://standard.aimoaas.com/latest/governance/) — Project governance and policies
- [Trust Package](https://standard.aimoaas.com/latest/governance/trust-package/) — Auditor-ready materials
- [Releases](https://github.com/billyrise/aimo-standard/releases) — Official releases with checksums

## Contact

For security concerns, use GitHub's private vulnerability reporting feature or contact the repository maintainers.
