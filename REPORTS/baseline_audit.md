# Baseline Audit Report

**Generated:** 2026-02-01 11:18:35

## Summary

| Category | OK | NG | WARN |
|----------|----|----|------|
| Broken Links | 1 | 0 | 0 |
| Translation Coverage | 1 | 0 | 0 |
| Reference Integrity | 1 | 0 | 0 |
| Unreferenced Files | 1 | 0 | 0 |
| Redirect Targets | 1 | 0 | 0 |
| Release Requirements | 1 | 0 | 0 |
| Versioning Policy | 3 | 0 | 0 |

**Status: ALL CHECKS PASSED** ✓

## Detailed Findings

### Broken Links

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `docs/` | All links resolved successfully | - |

### Translation Coverage

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `docs/` | All EN files have JA translations | - |

### Reference Integrity

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `schemas/, examples/` | All references valid and examples conform to schemas | - |

### Unreferenced Files

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `docs/` | All docs files are referenced in nav or linked | - |

### Redirect Targets

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `tooling/release/build_redirects.py` | All 10 redirect targets exist | - |

### Release Requirements

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `.github/workflows/release.yml` | Release workflow properly configured for required assets | - |

### Versioning Policy

#### OK

| File | Message | Recommendation |
|------|---------|----------------|
| `mkdocs.yml` | alias_type: redirect is configured | - |
| `deploy-dev.yml` | deploy-dev.yml correctly deploys only to dev | - |
| `docs_current.yml` | Old workflow removed | - |
