---
description: Roadmap for Evidence Bundle signature verification. v0.1 reference only; v0.1.1 metadata; v0.2 cryptographic verification and provenance.
---
<!-- aimo:translation_status=translated -->

# Signature verification and Evidence-as-Code roadmap

This page is **informative**. It describes the planned evolution of Evidence Bundle signing and verification so that auditors can re-perform verification and so that integrity is cryptographically assured in a future version.

## Current state (v0.1)

- **Normative**: The bundle MUST have at least one signature entry that **references** the manifest (path under `signatures/`, `targets` including `manifest.json`). Validators check existence and reference only.
- **Out of scope**: Cryptographic verification of signature bytes; canonical form of the signed payload; signer identity; verification procedure.

## v0.1.1 — Verification metadata (RECOMMENDED)

v0.1.1 adds **optional** fields to each signature entry in `manifest.json` so that an auditor can understand how to re-perform verification in the future:

| Field | Purpose |
|-------|---------|
| `signer_identity` | Who signed (e.g. PGP fingerprint, did:key). |
| `signed_at` | When the signature was applied (ISO 8601). |
| `verification_command` | Example CLI for an auditor (e.g. `aimo verify --pubkey ...`). |
| `canonicalization` | How the signed payload was produced (e.g. `rfc8785_json`, `cbor`). |

Implementers are **RECOMMENDED** to populate these so that v0.2 tooling can consume them. Validators in v0.1.1 **MAY** read and report these fields (e.g. in `--format json`) but do **not** perform cryptographic verification.

## v0.2 (planned) — Cryptographic verification and provenance

Planned for a future standard version (target 2026 Q4–2027):

1. **Verification in scope**: Validators MAY verify signature bytes against the declared algorithm and signer (e.g. public key). Failure of verification SHALL be reported.
2. **Provenance**: Alignment with SLSA-style provenance (builder, build type, materials) and/or in-toto layout may be specified so that the bundle can attest to how it was produced.
3. **Canonical form**: Normative rules for canonicalizing the signed payload (e.g. RFC 8785 JSON) so that verification is reproducible.

This roadmap is subject to change; the normative specification for each version is in the standard and schema for that version.

## References

- [Evidence Bundle structure](../standard/current/09-evidence-bundle-structure.md) — normative root and manifest
- [v0.2 roadmap](../standard/current/10-roadmap-v0.2.md) — broader roadmap (object model, Evidence-as-Code, profiles)
