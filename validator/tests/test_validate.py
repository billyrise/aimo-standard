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
    "Invalid taxonomy dimension: 'EV' is reserved for Evidence Artifact IDs. "
    "Use 'LG' for log/event taxonomy codes."
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
