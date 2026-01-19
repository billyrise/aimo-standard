import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def test_validate_ok(tmp_path):
    payload = {
        "version": "v0.1.0",
        "dictionary": {
            "entries": [{"key": "K", "label": "L", "description": "D"}]
        },
        "evidence": [
            {"id": "EV1", "timestamp": "2026-01-01T00:00:00Z", "source": "s", "summary": "x", "tags": ["t"]}
        ]
    }
    p = tmp_path / "root.json"
    p.write_text(json.dumps(payload), encoding="utf-8")

    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0
    assert "OK" in r.stdout

def test_validate_fail(tmp_path):
    payload = {"version": "v0.1.0"}  # missing dictionary/evidence
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(payload), encoding="utf-8")

    cmd = [sys.executable, str(ROOT / "validator" / "src" / "validate.py"), str(p)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode != 0
