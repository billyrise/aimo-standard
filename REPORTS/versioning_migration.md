# Versioning Migration Report

**Generated:** 2026-02-01
**Author:** Automated Analysis
**Status:** STEP 0 Complete - Ready for Implementation

---

## 1. Current State Findings

### A) mike Configuration

| Item | Current Value | File Path |
|------|---------------|-----------|
| mike used? | **Yes** | `mkdocs.yml` |
| version.provider | `mike` | `mkdocs.yml:40-41` |
| gh-pages branch | `gh-pages` (default) | `.github/workflows/*.yml` |
| deploy_prefix | None (root `/`) | N/A |
| alias_type | **NOT SET (defaults to `copy`)** | ⚠️ PROBLEM |

**Evidence from mkdocs.yml:**

```yaml
extra:
  version:
    provider: mike
```

mike plugin is NOT explicitly configured under `plugins:` - only referenced via Material's version provider.

### B) alias_type Configuration

**Current:** Not explicitly set → defaults to `copy`

**Problem:** When alias_type=copy (default), mike **copies** all files from the versioned directory to create the alias. This means:
- `/latest/` is a full copy of `/0.1.6/`
- If main branch is deployed, `/latest/` gets overwritten with main's content
- `/latest/` and `/0.1.6/` can have different content!

**Required:** `alias_type: redirect` or `alias_type: symlink`

### C) Workflow Analysis - Which Updates /latest/

| Workflow | Trigger | Updates /latest/? | Problem? |
|----------|---------|-------------------|----------|
| `release.yml` | `push: tags: v*` | Yes - `mike deploy VER latest dev --update-aliases` | OK |
| `docs_current.yml` | `push: main` (after quality-gate) | **Yes - `mike deploy latest dev`** | ⚠️ **CRITICAL BUG** |
| `quality-gate.yml` | PR/push to main | No | OK |

**Critical Bug in docs_current.yml (lines 44-53):**

```yaml
# Deploy main branch as 'latest' with 'dev' as alias
# This ensures language switcher links use /latest/ (not /dev/)
- name: Deploy current to gh-pages (latest + dev in sync)
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    git fetch origin gh-pages:gh-pages || true
    # Remove existing 'dev' version if it exists (to convert to alias)
    mike delete dev --push 2>/dev/null || true
    # Deploy as 'latest' (primary) with 'dev' as alias
    mike deploy latest dev --update-aliases --push
    mike set-default latest --push
```

**This is the root cause of /latest/ drift!**  
Every push to main overwrites `/latest/` with unreleased content.

### D) dev/Preview Deployment

| Item | Current State | Problem |
|------|---------------|---------|
| dev exists? | Yes, as alias to `latest` | `dev` = `latest` (not separate) |
| Separate preview? | No | Cannot preview unreleased changes |
| noindex for dev? | No | dev could be indexed by search engines |

---

## 2. Risk Analysis

### Why /latest/ and /0.1.6/ Can Diverge

```
Timeline of Events:
1. v0.1.6 tag created → release.yml deploys 0.1.6/ and sets latest=0.1.6 ✓
2. PR merged to main → docs_current.yml deploys main content to /latest/ ✗
3. Now: /latest/ = main (unreleased), /0.1.6/ = frozen release
4. Auditor cites /latest/ → gets unreleased content!
```

### SEO and Canonical Issues

1. **Duplicate content:** /latest/ and /0.1.6/ may have same content (copy) or different (drift)
2. **No noindex on dev:** Unreleased content can be indexed
3. **Canonical confusion:** auditors may cite wrong version

### Audit/Compliance Risks

1. **Immutability violation:** Cited version may change after audit
2. **Non-reproducible audits:** /latest/ content varies by when accessed
3. **Trust erosion:** Auditors cannot rely on stable URLs

---

## 3. File Inventory for Changes

### Files Requiring Modification

| File | Change Type | Description |
|------|-------------|-------------|
| `mkdocs.yml` | Modify | Add mike plugin config with alias_type=redirect |
| `VERSIONING.md` | Modify | Add explicit semantics for latest/dev/versioned |
| `.github/workflows/docs_current.yml` | **Rename → deploy-dev.yml** | Deploy to dev only, never touch latest |
| `.github/workflows/release.yml` | Modify | Add version existence check, enforce alias behavior |
| `docs/en/standard/versions/index.md` | Modify | Add FAQ and semantics explanation |
| `docs/ja/standard/versions/index.md` | Modify | Mirror EN changes |
| `docs/en/governance/seo-canonical-policy.md` | Modify | Update dev noindex guidance |
| `docs/ja/governance/seo-canonical-policy.md` | Modify | Mirror EN changes |
| `tooling/checks/check_version_alias.py` | **Create** | CI assertion for alias policy |
| `tooling/audit/baseline_audit.py` | Modify | Add versioning checks |

### Files for One-Time Repair

| File | Purpose |
|------|---------|
| `tooling/release/repair_latest_alias.sh` | One-time script to fix current gh-pages |

---

## 4. Proposed Target Behavior

### URL Contract

| URL | Behavior | Indexable | Mutable |
|-----|----------|-----------|---------|
| `https://standard.aimoaas.com/latest/` | **Redirect** to most recent /X.Y.Z/ | Yes (via target) | Pointer updates on release |
| `https://standard.aimoaas.com/dev/` | Preview of main branch | **No (noindex)** | Changes with main |
| `https://standard.aimoaas.com/X.Y.Z/` | Frozen release snapshot | Yes | **Never** |

### Release Flow

```
┌────────────────────────────────────────────────────────────┐
│ Push to main branch                                        │
│ ↓                                                          │
│ quality-gate.yml → passes → deploy-dev.yml                │
│ ↓                                                          │
│ mike deploy --push dev                                     │
│ (Only /dev/ updated; /latest/ unchanged)                  │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ Push tag v0.1.7                                            │
│ ↓                                                          │
│ release.yml                                                │
│ ↓                                                          │
│ 1. Check: 0.1.7/ must NOT exist in gh-pages               │
│ 2. Build + quality gates                                   │
│ 3. mike deploy --push --update-aliases 0.1.7 latest       │
│ 4. mike set-default --push latest                          │
│ 5. Create GitHub Release with assets                       │
│                                                            │
│ Result: /0.1.7/ created, /latest/ → redirect to /0.1.7/   │
└────────────────────────────────────────────────────────────┘
```

### Alias Strategy

```yaml
# Target mkdocs.yml config
plugins:
  - mike:
      alias_type: redirect      # NOT copy!
      canonical_version: latest
      version_selector: true
```

With `alias_type: redirect`:
- `/latest/index.html` contains `<meta http-equiv="refresh" content="0; url=../0.1.6/">`
- No file duplication
- No content drift possible

### dev noindex

Add to dev pages via theme override or robots meta:

```html
<!-- Only on /dev/ pages -->
<meta name="robots" content="noindex, nofollow">
```

---

## 5. Implementation Order

1. **STEP 1:** Update VERSIONING.md and docs pages with explicit semantics
2. **STEP 2:** Configure mike in mkdocs.yml (alias_type=redirect, dev noindex)
3. **STEP 3:** Split workflows (deploy-dev.yml + release.yml fixes)
4. **STEP 4:** One-time repair of gh-pages (fix latest alias)
5. **STEP 5:** Add CI assertions to prevent regression
6. **STEP 6:** Run all gates and produce final report

---

## 6. Verification Commands

After implementation:

```bash
# List mike versions and aliases
mike list

# Expected output:
# 0.1.6 [latest] (default)
# dev

# Verify /latest/ is redirect, not copy
curl -sI https://standard.aimoaas.com/latest/ | grep -i location
# Should show redirect to /0.1.6/
```

---

## Appendix: Current Workflow Excerpts

### docs_current.yml (problematic lines)

```yaml
# Line 44-53: This overwrites /latest/ with main branch content!
- name: Deploy current to gh-pages (latest + dev in sync)
  run: |
    mike delete dev --push 2>/dev/null || true
    mike deploy latest dev --update-aliases --push
    mike set-default latest --push
```

### release.yml (correct pattern, but also deploys dev alias)

```yaml
# Line 94-105: Deploys version with latest and dev as aliases
- name: Deploy version snapshot to gh-pages
  run: |
    mike delete dev --push 2>/dev/null || true
    mike delete latest --push 2>/dev/null || true
    mike deploy "${{ steps.v.outputs.ver }}" latest dev --update-aliases --push
    mike set-default latest --push
```

The release workflow is mostly correct, but dev should be a separate deployment, not an alias to the release.
