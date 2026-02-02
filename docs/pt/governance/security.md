---
description: AIMO Standard security policy - Vulnerability reporting, disclosure procedures, and security considerations for AI governance implementations.
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/governance/security.md
source_hash: 035ba54290c8cf46
translation_date: 2026-02-02
translator: pending
translation_status: needs_translation
---

# Security

This page documents the security policy for AIMO Standard, including vulnerability reporting and disclosure procedures.

## Scope

### In Scope

- Validator reference implementation (`validator/`)
- Build and release tooling (`tooling/`)
- JSON schemas (`schemas/`)
- Documentation website infrastructure

### Out of Scope

- Specification content (normative text is not a security artifact)
- Adopter implementations using AIMO Standard
- External dependencies (report to upstream maintainers)

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest (dev) | Yes |
| Tagged releases (vX.Y.Z) | Yes (latest 2 minor versions) |
| Older releases | No (upgrade recommended) |

## Reporting a Vulnerability

**Do not** open a public GitHub issue for security vulnerabilities.

### Process

1. Report privately via GitHub's private vulnerability reporting
2. Include: description, reproduction steps, affected versions, impact
3. Allow time for assessment and fix development

### Timeline

| Phase | Timeline |
| ----- | -------- |
| Acknowledgment | 72 hours |
| Initial assessment | 7 days |
| Coordinated disclosure | 90 days max |

## Disclosure Policy

1. Vulnerabilities are reported privately
2. Fixes are developed before public disclosure
3. Security advisories are published after fixes are available
4. Reporters are credited (unless anonymity requested)

## Security Measures

- CI/CD checks on all changes
- Signed releases with SHA-256 checksums
- Mandatory PR review before merge

## Full Policy

See [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) for the complete security policy.

## Related Pages

- [Trust Package](trust-package.md) — Auditor-ready materials
- [Governance](index.md) — Project governance
