---
description: Normative root structure and manifest for Evidence Bundle (v0.1). Integrity MUST; Custody is implementation-defined.
---
<!-- aimo:translation_status=translated -->

# Evidence Bundle root structure (v0.1)

This page defines the **normative** root layout and manifest for an Evidence Bundle. Validators MUST reject bundles that do not satisfy these requirements before any schema validation.

## v0.1 normative MUST (summary)

- **manifest.json** at bundle root is required.
- **object_index** and **payload_index**: each entry MUST include **sha256** (64 lowercase hex); paths MUST be relative and MUST NOT contain `../` or escape the bundle root.
- **signing.signatures** MUST be a non-empty array (empty array is invalid).
- Each signature entry MUST have: **path** under `signatures/` (path traversal forbidden), **targets** (array, at least one path), and at least one signature in the bundle MUST list **manifest.json** in **targets** (manifest signing is mandatory).
- **hash_chain**: v0.1 MUST include **algorithm**, **head**, **path** (under `hashes/`), and **covers** with at least **manifest.json** and **objects/index.json**.

Validators MUST enforce these before accepting a bundle. The JSON Schema and the reference validator implement the same rules.

## Root required structure (MUST)

At the bundle root, the following MUST be present:

| Item | Type | Purpose |
|------|------|---------|
| **manifest.json** | File | Bundle manifest (see below). Canonical descriptor for the bundle. |
| **objects/** | Directory | Enumerated objects (e.g. metadata, indexes). Listed in `manifest.json` `object_index`. |
| **payloads/** | Directory | Payload files (e.g. root EV JSON, Evidence Pack files). Listed in `manifest.json` `payload_index`. |
| **signatures/** | Directory | Digital signatures. v0.1 MUST contain at least one signature file that references the manifest (existence and target reference; cryptographic verification is a future extension). |
| **hashes/** | Directory | Hash chain or integrity records (as needed by `manifest.json` `hash_chain`). |

Implementers MUST NOT submit a bundle that omits any of these. The Validator MUST fail with a clear message when the root structure is incomplete.

## Integrity (normative) vs Custody (implementation)

- **Integrity** is **normative** in v0.1: the standard mandates that the bundle carries integrity metadata (manifest, sha256 for indexed files, signature presence for the manifest). Validators MUST check that:
  - Required directories and files exist.
  - `manifest.json` is present and valid (schema and pre-schema checks).
  - Every file listed in `object_index` and `payload_index` exists at the given path and its content matches the declared `sha256`.
  - `signatures/` contains at least one signature that targets the manifest (v0.1: existence and reference only; v0.1.1: verification metadata RECOMMENDED; v0.2 planned: cryptographic verification in scope).
- **Custody** (storage, access control, retention, WORM) is **implementation-defined**. The standard does not prescribe how custodians store or protect the bundle; it only requires that the package, when submitted, satisfies the Integrity requirements above.

## manifest.json (MUST fields)

The manifest MUST include at least:

| Field | Type | Description |
|-------|------|-------------|
| **bundle_id** | string (UUID) | Unique identifier for this bundle. |
| **bundle_version** | string (SemVer) | Version of the bundle. |
| **created_at** | string (date-time) | Creation timestamp. |
| **scope_ref** | string | Scope reference (e.g. `SC-001`). Pattern `SC-*`. |
| **object_index** | array | List of objects: `id`, `type`, `path`, `sha256`. Paths MUST be relative, MUST NOT contain `../` or start with `/`, and MUST remain within the Evidence Bundle root (validators MUST reject paths that escape the bundle root). |
| **payload_index** | array | List of payloads: `logical_id`, `path`, `sha256`, `mime`, `size`. Same path rules as object_index (relative, no `../`, no leading `/`, within bundle root). |
| **hash_chain** | object | **Normative (v0.1):** MUST include `algorithm` (sha256 \| merkle), `head` (64 lowercase hex), `path` (relative path under `hashes/`; no `../`, no leading `/`), and `covers` (array, at least one element). v0.1 MUST include `manifest.json` and `objects/index.json` in `covers`. |
| **signing** | object | **Normative (v0.1):** MUST include `signatures` (array, at least one entry). Each entry MUST have: `signature_id` (e.g. SIG-... or UUID), `path` (relative under `signatures/`; no `../`, no leading `/`), `targets` (array, at least one path; v0.1 MUST include `manifest.json` in at least one signature's targets), `algorithm` (one of ed25519, rsa-pss, ecdsa, unspecified). `created_at` (date-time) is MAY. **Note:** Cryptographic verification of signatures is out of scope for v0.1; reference (which file and what it targets) is required. |

**v0.1.1 optional signature metadata (RECOMMENDED for third-party re-performance):**

| Field | Type | Description |
|-------|------|-------------|
| **signer_identity** | string | Identity of the signer (e.g. PGP fingerprint, did:key). |
| **signed_at** | string (date-time) | When the signature was applied (ISO 8601). |
| **verification_command** | string | Example CLI command for an auditor to re-perform verification. |
| **canonicalization** | string | How the signed payload was canonicalized: `rfc8785_json`, `cbor`, or `unspecified`. |

Integrity and verification: **v0.1** — reference and existence only. **v0.1.1** — metadata for verification is RECOMMENDED. **v0.2** (planned) — cryptographic verification in scope.

- **sha256** values MUST be 64 lowercase hexadecimal characters.
- **path** MUST be a relative path; MUST NOT contain `../` or start with `/`; paths MUST stay within the Evidence Bundle root.
- The manifest MAY include an explicit self-reference (e.g. in `object_index` or a dedicated field) so that the manifest’s own integrity is covered; validators MUST accept a bundle where the manifest is either listed in an index or explicitly referenced by a signature.

See the JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json`.

## Future extensions (informative)

- **Control/Requirement linkage**: A future version may add a standard way to link Evidence Bundle elements to Control or Requirement identifiers (e.g. for export to NIST OSCAL or similar audit automation formats). This is not required in v0.1 or v0.1.1.

## References

- [Evidence Bundle (artifact overview)](../../../artifacts/evidence-bundle/) — purpose and TOC
- [EV Template — External Forms and Audit Handoff Index](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is) — where to attach official templates/checklists and how to reference them in the manifest
- [Signature verification roadmap](../../../artifacts/signature-verification-roadmap/) — v0.1.1 metadata and v0.2 verification plan
- [Validator](../../../validator/) — how the validator enforces this structure
- [Minimum Evidence Requirements](../../../artifacts/minimum-evidence/) — MUST-level checklist
