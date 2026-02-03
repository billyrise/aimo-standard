import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def test_validate_ok(tmp_path):
    """Test valid payload with taxonomy-aligned dictionary and evidence."""
    payload = {
        "version": "0.1.0",
        "taxonomy_version": "0.1.0",
        "dictionary": {
            "taxonomy_version": "0.1.0",
            "entries": [
                {
                    "code": "FS-001",
                    "label_en": "End-user Productivity",
                    "label_ja": "社内生産性",
                    "definition_en": "AI for internal productivity.",
                    "status": "active"
                }
            ]
        },
        "evidence": [
            {
                "id": "EV-20260101-001",
                "timestamp": "2026-01-01T00:00:00Z",
                "source": "test-system",
                "summary": "Test evidence record",
                "taxonomy_version": "0.1.0",
                "codes": {
                    "FS": ["FS-001"],
                    "UC": ["UC-001"],
                    "DT": ["DT-002"],
                    "CH": ["CH-001"],
                    "IM": ["IM-002"],
                    "RS": ["RS-001"],
                    "LG": ["LG-001"]
                },
                "tags": ["test"]
            }
        ]
    }
    p = tmp_path / "root.json"
    p.write_text(json.dumps(payload), encoding="utf-8")

    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, f"Validation failed: {r.stderr}"
    assert "OK" in r.stdout

def test_validate_fail(tmp_path):
    """Test invalid payload (missing required fields)."""
    payload = {"version": "0.1.0"}  # missing dictionary/evidence
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(payload), encoding="utf-8")

    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0

EXPECTED_CODES_EV_MESSAGE = (
    "Invalid taxonomy dimension: 'EV' is reserved for Evidence artifact IDs. "
    "Use 'LG' for Log/Event Type."
)


def test_validate_rejects_ev_dimension_pre_schema(tmp_path):
    """Validator rejects codes.EV before schema and prints the normative message to stderr."""
    payload = {
        "version": "0.1.0",
        "taxonomy_version": "0.1.0",
        "dictionary": {"taxonomy_version": "0.1.0", "entries": []},
        "evidence": [
            {
                "id": "EV-20260101-001",
                "timestamp": "2026-01-01T00:00:00Z",
                "source": "test",
                "summary": "Test",
                "codes": {
                    "FS": ["FS-001"],
                    "UC": ["UC-001"],
                    "DT": ["DT-002"],
                    "CH": ["CH-001"],
                    "IM": ["IM-002"],
                    "RS": ["RS-001"],
                    "EV": ["EV-001"],
                },
            }
        ],
    }
    p = tmp_path / "bad_codes.json"
    p.write_text(json.dumps(payload), encoding="utf-8")
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject evidence.codes.EV before schema"
    assert EXPECTED_CODES_EV_MESSAGE in r.stderr, (
        f"Expected stderr to contain normative message; got: {r.stderr!r}"
    )


def test_validate_rejects_ev_dimension_in_codes(tmp_path):
    """Evidence.codes.EV is rejected by pre-schema check with the normative message."""
    payload = {
        "version": "0.1.0",
        "taxonomy_version": "0.1.0",
        "dictionary": {"taxonomy_version": "0.1.0", "entries": []},
        "evidence": [
            {
                "id": "EV-20260101-001",
                "timestamp": "2026-01-01T00:00:00Z",
                "source": "test",
                "summary": "Test",
                "codes": {
                    "FS": ["FS-001"],
                    "UC": ["UC-001"],
                    "DT": ["DT-002"],
                    "CH": ["CH-001"],
                    "IM": ["IM-002"],
                    "RS": ["RS-001"],
                    "EV": ["EV-001"],
                },
            }
        ],
    }
    p = tmp_path / "bad_codes.json"
    p.write_text(json.dumps(payload), encoding="utf-8")
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject evidence.codes.EV (use LG for Log/Event Type)"
    assert EXPECTED_CODES_EV_MESSAGE in r.stderr, (
        f"Expected pre-schema rejection message in stderr; got: {r.stderr!r}"
    )


def test_validate_examples(tmp_path):
    """Test that bundled examples validate successfully."""
    examples = [
        ROOT / "examples" / "evidence_bundle_minimal" / "root.json",
    ]
    for example in examples:
        if example.exists():
            cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(example)]
            r = subprocess.run(cmd, capture_output=True, text=True)
            assert r.returncode == 0, f"Example {example.name} failed: {r.stderr}"

BUNDLE_INTEGRITY_MESSAGE = (
    "Invalid Evidence Bundle: manifest integrity requirements not satisfied "
    "(missing sha256/signature/index mismatch)."
)


def test_validate_bundle_ok():
    """Valid v0.1 minimal bundle passes."""
    bundle_dir = ROOT / "examples" / "evidence_bundle_v01_minimal"
    if not bundle_dir.is_dir():
        return  # skip if example not present
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(bundle_dir)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, f"Bundle validation failed: {r.stderr}"
    assert "OK" in r.stdout


def test_validate_bundle_fail_sha256_mismatch(tmp_path):
    """Bundle with wrong sha256 in manifest fails with fixed message."""
    # Copy minimal bundle and corrupt manifest sha256 for one file
    import shutil
    src = ROOT / "examples" / "evidence_bundle_v01_minimal"
    if not src.is_dir():
        return
    dest = tmp_path / "bundle"
    shutil.copytree(src, dest)
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["payload_index"][0]["sha256"] = "0" * 64  # wrong hash
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject bundle with sha256 mismatch"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_fail_signature_missing(tmp_path):
    """Bundle with empty signatures/ fails with fixed message."""
    import shutil
    src = ROOT / "examples" / "evidence_bundle_v01_minimal"
    if not src.is_dir():
        return
    dest = tmp_path / "bundle"
    shutil.copytree(src, dest)
    sig_dir = dest / "signatures"
    for f in sig_dir.iterdir():
        f.unlink()
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject bundle with no signature file"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_fail_index_file_missing(tmp_path):
    """Bundle with payload_index pointing to missing file fails."""
    import shutil
    src = ROOT / "examples" / "evidence_bundle_v01_minimal"
    if not src.is_dir():
        return
    dest = tmp_path / "bundle"
    shutil.copytree(src, dest)
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["payload_index"].append({
        "logical_id": "missing",
        "path": "payloads/nonexistent.json",
        "sha256": "a" * 64,
        "mime": "application/json",
        "size": 0
    })
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject bundle when indexed file is missing"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def _copy_minimal_bundle(tmp_path):
    """Copy examples/evidence_bundle_v01_minimal to tmp_path/bundle. Returns dest or None if source missing."""
    import shutil
    src = ROOT / "examples" / "evidence_bundle_v01_minimal"
    if not src.is_dir():
        return None
    dest = tmp_path / "bundle"
    shutil.copytree(src, dest)
    return dest


def test_validate_bundle_rejects_path_traversal_in_object_index(tmp_path):
    """object_index[*].path with ../ is rejected (path traversal)."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["object_index"][0]["path"] = "objects/../payloads/root.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject path traversal in object_index.path"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_rejects_missing_signature_referenced_by_manifest(tmp_path):
    """signing.signatures[*].path pointing to non-existent file fails."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["signing"]["signatures"][0]["path"] = "missing.sig"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject when signature file referenced in manifest does not exist"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_rejects_signing_targets_without_manifest(tmp_path):
    """targets without manifest.json fails (v0.1 MUST)."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["signing"]["signatures"][0]["targets"] = ["payloads/root.json"]
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject when no signature targets manifest.json"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_rejects_hash_chain_path_missing(tmp_path):
    """hash_chain.path pointing to non-existent file fails."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["hash_chain"]["path"] = "nonexistent.head"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject when hash_chain.path file does not exist"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr


def test_validate_bundle_rejects_hash_chain_covers_missing_manifest_or_index(tmp_path):
    """hash_chain.covers missing manifest.json or objects/index.json fails (v0.1 MUST)."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["hash_chain"]["covers"] = ["manifest.json"]
    manifest_path.write_text(json.dumps(manifest, indent=2))
    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must reject when hash_chain.covers omits manifest.json or objects/index.json"
    assert BUNDLE_INTEGRITY_MESSAGE in r.stderr
