# Versioning Migration Result Report

**Generated:** 2026-02-01
**Status:** COMPLETE
**Branch:** hotfix/legacy-redirects-readme-os-commands

---

## 1. Summary

The versioning and deployment system has been updated to ensure:

1. **`/latest/` ALWAYS points to the most recent released version** (via redirect, not copy)
2. **`/dev/` tracks main branch preview** and is explicitly marked as unreleased (noindex)
3. **Versioned directories `/X.Y.Z/` are immutable** once released
4. **Content drift is prevented** by using `alias_type: redirect` instead of copy

---

## 2. Files Changed

### Core Configuration

| File | Change |
|------|--------|
| `mkdocs.yml` | Added mike plugin with `alias_type: redirect`, `canonical_version: latest` |
| `VERSIONING.md` | Complete rewrite with explicit semantics for latest/dev/versioned URLs |

### Documentation (EN)

| File | Change |
|------|--------|
| `docs/en/standard/versions/index.md` | Added URL types table, FAQ section explaining latest vs dev |
| `docs/en/governance/seo-canonical-policy.md` | Updated with alias_type redirect explanation, dev noindex details |

### Documentation (JA)

| File | Change |
|------|--------|
| `docs/ja/standard/versions/index.md` | Japanese mirror of EN changes |
| `docs/ja/governance/seo-canonical-policy.md` | Japanese mirror of EN changes |

### Theme Override

| File | Change |
|------|--------|
| `docs/overrides/main.html` | Added noindex meta tag injection for dev deployments |

### GitHub Actions Workflows

| File | Change |
|------|--------|
| `.github/workflows/deploy-dev.yml` | **NEW** - Replaces docs_current.yml, deploys only to /dev/ |
| `.github/workflows/docs_current.yml` | **DELETED** - Was incorrectly updating /latest/ on main push |
| `.github/workflows/release.yml` | Added version existence check, improved logging |
| `.github/workflows/repair-latest.yml` | **NEW** - Manual workflow to repair /latest/ if needed |
| `.github/workflows/quality-gate.yml` | Added version alias policy check |

### Tooling

| File | Change |
|------|--------|
| `tooling/checks/check_version_alias.py` | **NEW** - CI check for versioning policy compliance |
| `tooling/release/repair_latest_alias.sh` | **NEW** - One-time repair script |
| `tooling/audit/baseline_audit.py` | Added versioning policy checks |

### Reports

| File | Change |
|------|--------|
| `REPORTS/versioning_migration.md` | Initial findings and analysis |
| `REPORTS/versioning_migration_result.md` | This file |

---

## 3. New Operational Commands

### How to Release vX.Y.Z

```bash
# 1. Ensure all changes are merged to main
# 2. Create and push the tag
git tag v0.1.7
git push origin v0.1.7

# 3. The release.yml workflow will:
#    - Check that 0.1.7/ doesn't already exist (immutability)
#    - Run all quality gates
#    - Build docs and deploy to /0.1.7/
#    - Update /latest/ alias to redirect to /0.1.7/
#    - Create GitHub Release with assets
```

### How to Deploy Dev Preview

```bash
# Automatic: Push to main branch
# After quality-gate passes, deploy-dev.yml runs and:
#   - Builds docs with noindex flag
#   - Deploys only to /dev/ (never touches /latest/)
```

### How to Verify Alias Status

```bash
# Check current mike versions
mike list

# Expected output:
# 0.1.6 [latest] (default)
# dev

# Verify /latest/ redirects correctly
curl -sI https://standard.aimoaas.com/latest/ | grep -i location
# Expected: Location: ../0.1.6/ or similar
```

### How to Repair /latest/ (if needed)

```bash
# Option 1: Manual workflow (recommended)
# Go to GitHub Actions > repair-latest > Run workflow
# Set dry_run=false to apply

# Option 2: Local script
./tooling/release/repair_latest_alias.sh 0.1.6
```

---

## 4. Expected URL Behavior

| URL | Content | Mutable | Indexed |
|-----|---------|---------|---------|
| `https://standard.aimoaas.com/0.1.6/` | Frozen release v0.1.6 | **Never** | Yes |
| `https://standard.aimoaas.com/latest/` | Redirect → /0.1.6/ | Pointer on release | Yes |
| `https://standard.aimoaas.com/dev/` | Main branch preview | Always | No |

### Redirect Behavior

With `alias_type: redirect`:

```
GET /latest/
→ 302 Redirect to /0.1.6/

GET /latest/standard/current/
→ 302 Redirect to /0.1.6/standard/current/
```

No file duplication. No content drift possible.

---

## 5. Quality Gate Results

| Check | Status |
|-------|--------|
| `python tooling/audit/baseline_audit.py --check` | ✓ PASS (9 OK, 0 NG) |
| `python tooling/checks/lint_i18n.py` | ✓ PASS |
| `python tooling/checks/lint_schema.py` | ✓ PASS |
| `python tooling/checks/check_version_alias.py --check` | ✓ PASS (6/6) |
| `mkdocs build --strict` | ✓ PASS |

---

## 6. Quick Validation Checklist

After merging this PR:

- [ ] Push a test change to main → Verify `/dev/` updates but `/latest/` unchanged
- [ ] Check `mike list` shows correct aliases
- [ ] Verify `/dev/` pages have `<meta name="robots" content="noindex, nofollow">`
- [ ] (Next release) Push tag → Verify `/latest/` updates to new version

---

## 7. Breaking Changes

**None for end users.**

The URLs remain the same. The only difference is:
- `/latest/` now redirects instead of being a copy
- `/dev/` is explicitly marked as preview (noindex)

---

## 8. Rollback Plan

If issues arise:

1. Re-run the old `docs_current.yml` behavior (revert workflow deletion)
2. Remove mike plugin config from mkdocs.yml
3. Use `repair-latest.yml` workflow to reset alias

However, rollback would reintroduce the content drift problem.

---

## 9. Related Documentation

- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) - Complete policy
- [SEO & Canonical Policy](https://standard.aimoaas.com/latest/governance/seo-canonical-policy/) - URL strategy
- [Versions](https://standard.aimoaas.com/latest/standard/versions/) - User-facing docs
