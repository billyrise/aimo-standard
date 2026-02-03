# Evidence Bundle v0.1 minimal example

This directory is a **normative minimal** Evidence Bundle that satisfies v0.1 MUST requirements. It is used by CI (quality-gate and release) to ensure the validator and schema stay aligned with the spec.

## Structure

- **manifest.json** — Bundle manifest (bundle_id, object_index, payload_index, hash_chain, signing).
- **objects/index.json** — Index object; listed in `object_index` with `sha256`.
- **payloads/root.json** — Root EV payload; listed in `payload_index` with `sha256`.
- **hashes/chain.sha256** — Hash chain file; `hash_chain.path` points here; `hash_chain.covers` MUST include `manifest.json` and `objects/index.json`.
- **signatures/manifest.sig** — Signature file; at least one entry in `signing.signatures` MUST have `path` pointing here and `targets` including `manifest.json`.

## Reproducibility (regenerating hashes)

If you change any of the indexed files, update the manifest so that all `sha256` values match the actual file contents. Use the same algorithm as the validator (SHA-256, lowercase hex).

### 1. Compute SHA-256 of indexed files

```bash
# From repo root
sha256sum examples/evidence_bundle_v01_minimal/objects/index.json
# Use the 64-char hex (first column) in manifest.json object_index[].sha256

sha256sum examples/evidence_bundle_v01_minimal/payloads/root.json
# Use in manifest.json payload_index[].sha256
```

On macOS:

```bash
shasum -a 256 examples/evidence_bundle_v01_minimal/objects/index.json
shasum -a 256 examples/evidence_bundle_v01_minimal/payloads/root.json
```

### 2. Update manifest.json

- Set **object_index[0].sha256** to the hash of `objects/index.json`.
- Set **payload_index[0].sha256** to the hash of `payloads/root.json`.
- **hash_chain.head** may be the hash of the chain file (`hashes/chain.sha256`) or a derived head; this example uses the same hash as `objects/index.json` for simplicity. **hash_chain.covers** MUST include `manifest.json` and `objects/index.json`.

### 3. Signing (v0.1)

- **signatures/manifest.sig** must exist; content may be a placeholder for v0.1 (cryptographic verification is out of scope).
- **signing.signatures** must have at least one entry with:
  - **path**: path under `signatures/` (e.g. `manifest.sig`), no `../`, no leading `/`.
  - **targets**: array including `manifest.json`.

### 4. Validate

From repo root:

```bash
python validator/src/validate.py examples/evidence_bundle_v01_minimal
```

Must print `OK` and exit 0.
