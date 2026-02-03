---
description: Normative root structure and manifest for Evidence Bundle (v0.1). Integrity MUST; Custody is implementation-defined.
---

# Evidence Bundle root structure (v0.1)

This page defines the **normative** root layout and manifest for an Evidence Bundle. Validators MUST reject bundles that do not satisfy these requirements before any schema validation.

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
  - `signatures/` contains at least one signature that targets the manifest (v0.1: existence and reference only; verification is out of scope for v0.1).
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

- **sha256** values MUST be 64 lowercase hexadecimal characters.
- **path** MUST be a relative path; MUST NOT contain `../` or start with `/`; paths MUST stay within the Evidence Bundle root.
- The manifest MAY include an explicit self-reference (e.g. in `object_index` or a dedicated field) so that the manifest’s own integrity is covered; validators MUST accept a bundle where the manifest is either listed in an index or explicitly referenced by a signature.

See the JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json`.

## References

- [Evidence Bundle (artifact overview)](../../artifacts/evidence-bundle.md) — purpose and TOC
- [Validator](../../validator/index.md) — how the validator enforces this structure
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence.md) — MUST-level checklist
