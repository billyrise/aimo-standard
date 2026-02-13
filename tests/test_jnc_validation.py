"""
Tests for optional JNC (Justified Non-Compliance) payload validation in Evidence Bundle.
When payload_index contains logical_id JNC/jnc/JUSTIFIED_NON_COMPLIANCE, the validator
must schema-validate that payload; when absent, no JNC check is performed (PASS).
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATE_PY = ROOT / "validator" / "src" / "validate.py"
MINIMAL_BUNDLE = ROOT / "examples" / "evidence_bundle_v01_minimal"
VALID_JNC = ROOT / "examples" / "justified_non_compliance.json"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _copy_minimal_bundle(tmp_path: Path) -> Path | None:
    if not MINIMAL_BUNDLE.is_dir():
        return None
    dest = tmp_path / "bundle"
    shutil.copytree(MINIMAL_BUNDLE, dest)
    return dest


def test_bundle_with_valid_jnc_passes(tmp_path):
    """Bundle with payloads/jnc.json and payload_index JNC entry (valid schema) passes."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    jnc_path = dest / "payloads" / "jnc.json"
    jnc_content = json.loads(VALID_JNC.read_text(encoding="utf-8"))
    jnc_path.write_text(json.dumps(jnc_content, indent=2), encoding="utf-8")
    sha = _sha256_file(jnc_path)
    size = jnc_path.stat().st_size

    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["payload_index"].append({
        "logical_id": "JNC",
        "path": "payloads/jnc.json",
        "sha256": sha,
        "mime": "application/json",
        "size": size,
    })
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    cmd = [sys.executable, str(VALIDATE_PY), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, f"Expected PASS: {r.stderr}"
    assert "OK" in r.stdout


def test_bundle_with_invalid_jnc_fails(tmp_path):
    """Bundle with JNC payload that violates schema fails with non-zero exit."""
    dest = _copy_minimal_bundle(tmp_path)
    if dest is None:
        return
    jnc_path = dest / "payloads" / "jnc.json"
    # Schema violation: missing required "approver", wrong risk_assessment enum
    invalid_jnc = {
        "version": "0.1.2",
        "non_compliances": [
            {
                "id": "JNC-001",
                "aimo_item_ref": "minimum-evidence:exception",
                "title": "Test",
                "rationale": "Test rationale",
                "risk_assessment": {
                    "likelihood": "invalid_enum",
                    "impact": "medium",
                    "mitigation": "None",
                },
                "review_schedule": "quarterly",
            }
        ],
    }
    jnc_path.write_text(json.dumps(invalid_jnc, indent=2), encoding="utf-8")
    sha = _sha256_file(jnc_path)
    size = jnc_path.stat().st_size

    manifest_path = dest / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["payload_index"].append({
        "logical_id": "jnc",
        "path": "payloads/jnc.json",
        "sha256": sha,
        "mime": "application/json",
        "size": size,
    })
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    cmd = [sys.executable, str(VALIDATE_PY), str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0, "Validator must fail when JNC payload violates schema"
    assert "JNC" in r.stderr or "schema" in r.stderr.lower()
