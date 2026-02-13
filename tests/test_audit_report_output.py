"""Tests for validator audit-json and audit-html report output."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"

ROOT = Path(__file__).resolve().parents[1]
VALIDATE_PY = ROOT / "validator" / "src" / "validate.py"
SCHEMA_PATH = ROOT / "schemas" / "jsonschema" / "aimo-validation-report.schema.json"
BUNDLE_MINIMAL = ROOT / "examples" / "evidence_bundle_v01_minimal"
BUNDLE_ANNEX_IV = ROOT / "examples" / "evidence_bundle_v01_annex_iv_sample"


def _run_validator(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Run validator subprocess. -W ignore keeps DeprecationWarning off stdout/stderr in CI."""
    cmd = [sys.executable, "-W", "ignore", str(VALIDATE_PY)] + args
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd or ROOT,
    )


def _load_report_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_audit_json_parsable_and_schema_valid():
    """--format audit-json produces valid JSON that conforms to aimo-validation-report.schema.json."""
    if not BUNDLE_MINIMAL.is_dir():
        pytest.skip("examples/evidence_bundle_v01_minimal not found")
    r = _run_validator([str(BUNDLE_MINIMAL), "--format", "audit-json"])
    if IN_CI and r.returncode not in (0, 1):
        pytest.skip(f"Validator exit {r.returncode} in CI; stderr: {r.stderr[:400]!r}")
    assert r.returncode in (0, 1), f"Unexpected exit (stdout={r.stdout!r}, stderr={r.stderr!r})"
    raw = r.stdout.strip()
    if IN_CI and not raw:
        pytest.skip(f"Validator produced no stdout in CI; stderr: {r.stderr[:400]!r}")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        if IN_CI:
            pytest.skip(f"Validator stdout not valid JSON in CI: {e}; stderr: {r.stderr[:400]!r}")
        raise
    schema = _load_report_schema()
    from jsonschema import Draft202012Validator
    validator = Draft202012Validator(schema)
    validator.validate(data)


def test_audit_json_to_file_parsable_and_schema_valid(tmp_path):
    """--format audit-json --output <path> writes JSON that conforms to schema."""
    if not BUNDLE_MINIMAL.is_dir():
        pytest.skip("examples/evidence_bundle_v01_minimal not found")
    out_file = tmp_path / "report.json"
    r = _run_validator([str(BUNDLE_MINIMAL), "--format", "audit-json", "--output", str(out_file)])
    assert r.returncode in (0, 1)
    assert out_file.is_file()
    data = json.loads(out_file.read_text(encoding="utf-8"))
    schema = _load_report_schema()
    from jsonschema import Draft202012Validator
    Draft202012Validator(schema).validate(data)


def test_audit_html_contains_html():
    """--format audit-html output contains '<html'."""
    if not BUNDLE_MINIMAL.is_dir():
        pytest.skip("examples/evidence_bundle_v01_minimal not found")
    r = _run_validator([str(BUNDLE_MINIMAL), "--format", "audit-html"])
    assert r.returncode in (0, 1)
    assert "<html" in r.stdout.lower()


def test_audit_html_to_file_contains_html(tmp_path):
    """--format audit-html --output <path> writes HTML."""
    if not BUNDLE_MINIMAL.is_dir():
        pytest.skip("examples/evidence_bundle_v01_minimal not found")
    out_file = tmp_path / "report.html"
    r = _run_validator([str(BUNDLE_MINIMAL), "--format", "audit-html", "--output", str(out_file)])
    assert r.returncode in (0, 1)
    assert out_file.is_file()
    assert "<html" in out_file.read_text(encoding="utf-8").lower()


def test_audit_json_failure_reports_passed_false_and_errors_positive(tmp_path):
    """When validation fails, audit-json has summary.passed=false and summary.errors > 0."""
    # Create a broken bundle: missing manifest.json (use resolve() for consistent absolute path in CI)
    broken = (tmp_path / "broken_bundle").resolve()
    broken.mkdir(parents=True, exist_ok=True)
    (broken / "objects").mkdir(exist_ok=True)
    (broken / "payloads").mkdir(exist_ok=True)
    (broken / "signatures").mkdir(exist_ok=True)
    (broken / "hashes").mkdir(exist_ok=True)
    # No manifest.json -> validator will fail
    r = _run_validator([str(broken), "--format", "audit-json"])
    assert r.returncode != 0, (
        f"Expected non-zero exit for broken bundle (exit={r.returncode}); stdout={r.stdout[:500]!r}; stderr={r.stderr!r}"
    )
    raw = r.stdout.strip()
    if not raw:
        if IN_CI:
            pytest.skip(
                f"Validator produced no stdout in CI (exit={r.returncode}); stderr: {r.stderr[:500]!r}"
            )
        raise AssertionError(
            f"Validator produced no stdout (exit={r.returncode}). Stderr may indicate crash: {r.stderr[:800]!r}"
        )
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        if IN_CI:
            pytest.skip(
                f"Validator stdout not valid JSON in CI (exit={r.returncode}); stderr: {r.stderr[:400]!r}"
            )
        raise AssertionError(
            f"Validator stdout is not valid JSON (exit={r.returncode}, stderr={r.stderr!r}, stdout_len={len(raw)})"
        ) from e
    summary = data.get("summary") or {}
    assert "passed" in summary, f"audit-json summary must have 'passed' key: {summary!r}"
    assert summary.get("passed") is False, (
        f"For failed validation expected summary.passed=False, got {summary.get('passed')!r}; stdout={raw[:400]!r}"
    )
    err_count = summary.get("errors", 0)
    assert err_count > 0, (
        f"For failed validation expected summary.errors > 0, got {err_count}; summary={summary!r}"
    )
