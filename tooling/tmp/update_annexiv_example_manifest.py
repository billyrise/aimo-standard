#!/usr/bin/env python3
"""
Update manifest.json for the Annex IV example bundle: recompute sha256 and size
for all object_index and payload_index entries, set hash_chain.head, and write
hashes/chain.sha256 for audit. Run from repo root.

Usage:
    python tooling/tmp/update_annexiv_example_manifest.py [BUNDLE_ROOT]
    Default BUNDLE_ROOT: examples/evidence_bundle_v01_annex_iv_sample
"""

import hashlib
import json
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    bundle_root = repo_root / "examples" / "evidence_bundle_v01_annex_iv_sample"
    if len(sys.argv) > 1:
        bundle_root = Path(sys.argv[1]).resolve()

    manifest_path = bundle_root / "manifest.json"
    if not manifest_path.is_file():
        print(f"ERROR: {manifest_path} not found", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    # Update object_index
    for i, obj in enumerate(manifest.get("object_index", [])):
        path = obj.get("path", "")
        if not path:
            continue
        full = bundle_root / path
        if not full.is_file():
            print(f"WARN: object_index[{i}] path not found: {path}", file=sys.stderr)
            continue
        manifest["object_index"][i]["sha256"] = sha256_file(full)

    # Update payload_index (sha256 + size)
    for i, pl in enumerate(manifest.get("payload_index", [])):
        path = pl.get("path", "")
        if not path:
            continue
        full = bundle_root / path
        if not full.is_file():
            print(f"WARN: payload_index[{i}] path not found: {path}", file=sys.stderr)
            continue
        manifest["payload_index"][i]["sha256"] = sha256_file(full)
        manifest["payload_index"][i]["size"] = full.stat().st_size

    # Set hash_chain.head to hash of objects/index.json (conventional chain head for v0.1)
    index_path = bundle_root / "objects" / "index.json"
    if index_path.is_file():
        manifest["hash_chain"]["head"] = sha256_file(index_path)

    # Write manifest
    manifest_path.write_text(json.dumps(manifest, indent=None) + "\n", encoding="utf-8")

    # Build chain file: for each path in covers, emit "sha256  path" (audit-readable)
    covers = manifest.get("hash_chain", {}).get("covers") or []
    cover_hashes = {}
    for rel in covers:
        full = bundle_root / rel
        if full.is_file():
            cover_hashes[rel] = sha256_file(full)
        else:
            # manifest.json was just written; recompute
            if rel == "manifest.json":
                cover_hashes[rel] = sha256_file(manifest_path)
            else:
                cover_hashes[rel] = "(file not found)"
    chain_path = bundle_root / "hashes" / "chain.sha256"
    chain_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{cover_hashes.get(rel, '')}  {rel}" for rel in covers]
    chain_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Updated manifest.json and hashes/chain.sha256")
    return 0


if __name__ == "__main__":
    sys.exit(main())
