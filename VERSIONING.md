# Versioning Policy (SemVer)

## Scope

This policy applies to the normative specification and machine-readable artifacts (schemas, templates, validator rules).

## English Canonical

English documentation is canonical. Japanese translations follow and may lag.

---

## Terminology

| Term | Definition |
|------|------------|
| **Released version** | Immutable snapshot tied to a Git tag `vX.Y.Z`. Directory `/X.Y.Z/` is frozen at release time and MUST NOT be modified. |
| **`latest`** | An **alias** (redirect) pointing to the most recent released version. Updated only by the release workflow when a new tag is pushed. `latest` is NOT a version—it is a pointer. |
| **`dev`** | Preview of the `main` branch. Explicitly **UNRELEASED**. May change at any time. Not suitable for audit citations. Must have `noindex` to avoid search engine indexing. |

---

## URL Contract

| URL Pattern | Behavior | Indexable | Mutable |
|-------------|----------|-----------|---------|
| `https://standard.aimoaas.com/X.Y.Z/` | Frozen release snapshot | Yes | **Never** (immutable) |
| `https://standard.aimoaas.com/latest/` | Redirect to most recent `/X.Y.Z/` | Yes (via target) | Pointer updated on release only |
| `https://standard.aimoaas.com/dev/` | Preview of main branch | **No** (noindex) | Continuous with main |

### Examples

- `/0.0.1/` — Frozen snapshot of v0.0.1
- `/latest/` → `/0.0.1/` (redirect, not copy)
- `/dev/` — Current main branch preview (unreleased)

---

## SemVer Rules

- **MAJOR**: Breaking changes to schemas, codes, or normative requirements
- **MINOR**: Backward-compatible additions (new fields with defaults, new optional codes)
- **PATCH**: Backward-compatible fixes and clarifications (including validator bug fixes)

---

## Release Flow

### 1. Development (main branch)

- All changes merged to `main` are deployed to `/dev/` only.
- `/latest/` is **never updated** by main branch pushes.
- The `deploy-dev.yml` workflow handles this.

### 2. Release (tag push)

When a tag `vX.Y.Z` is pushed:

1. **Pre-check**: Verify `/X.Y.Z/` does NOT already exist (prevent rewrite).
2. **Quality gates**: All lints and tests must pass.
3. **Deploy docs**: `mike deploy --push --update-aliases X.Y.Z latest`
4. **Set default**: `mike set-default --push latest`
5. **Create GitHub Release**: Upload PDFs, artifacts ZIP, checksums.

The `release.yml` workflow handles this.

### 3. Non-Negotiable Rules

1. **Never rewrite a released version.** If `/0.1.6/` needs fixes, release `0.1.7`.
2. **`latest` is an alias, not a version.** Only the release workflow (tag push) updates it; nothing else must change `/latest/`.
3. **`dev` is explicitly unreleased.** Must have noindex; not for audit citations.
4. **alias_type must be `redirect`** (not `copy`) to prevent content drift.

### 5. Standard governance (v0.1.1)

- **Major version upgrades**: When releasing a MAJOR version (breaking changes), the project SHOULD provide an automated migration tool (migrator) and a migration guide so adopters can transition without ambiguity.
- **Deprecated versions**: Released versions that are superseded SHOULD be marked as deprecated and retained as read-only archives. A deprecation period (e.g. 3 years) MAY be defined so that citations remain valid for a known interval.
- **Change impact**: Changes that affect IDs, terminology, or normative requirements SHOULD be accompanied by an impact analysis (e.g. diff) and an explicit compatibility statement (e.g. "backward compatible" or "breaking; see migration guide").

### 4. Audit citation and /latest

- **Audit citations MUST use a versioned URL** (`https://standard.aimoaas.com/X.Y.Z/...`). `/latest/` is for convenience and reference only; it is **not recommended for audit evidence** because the target can change when a new release is published.
- **Updates to `/latest/`** happen only when a **tag** is pushed and the `release.yml` workflow runs (`mike deploy --push --update-aliases`). There is no other mechanism that updates the public `/latest/` alias.
- **Drift detection**: The workflow `monitor-latest-drift.yml` runs daily (09:00 JST) and compares the public site’s `/latest/` redirect target to the latest `v*` tag. If they differ, the job fails so the team can fix the deployment (e.g. by re-running the release workflow or repairing the alias).

---

## Releases

- Official releases are tagged as `vX.Y.Z`.
- Each release must include:
  - Versioned spec site snapshot at `/X.Y.Z/`
  - PDF: `trust_package.pdf` (EN) and `trust_package.ja.pdf` (JA)
  - Packaged artifacts: `aimo-standard-artifacts.zip`
  - Checksums: `SHA256SUMS.txt`
  - Build provenance attestation

---

## Errata / Documentation-Only Revisions

If a post-release clarification is needed without changing normative meaning:

- Publish an errata note under the same version, and
- Prefer documenting in `docs/standard/current/08-changelog.md` and linking from `versions/`.
- **If normative content must change, release a new PATCH version.**

---

## FAQ

### Why is `latest` not a version number?

`latest` is a convenience alias that always points to the most recent stable release. It allows users to bookmark a single URL while automatically getting updates. However, for **audit citations**, always use the explicit version URL (`/X.Y.Z/`) to ensure immutability.

### Which URL should auditors cite?

| Use Case | Recommended URL |
|----------|-----------------|
| **Formal audit / evidence (MUST)** | `https://standard.aimoaas.com/X.Y.Z/...` — use a fixed version; do not rely on `/latest/` for audit evidence. |
| General reference (acceptable) | `https://standard.aimoaas.com/latest/...` — convenient but not pinned; avoid for citations that must be reproducible. |
| **Never cite** | `https://standard.aimoaas.com/dev/...` |

See the [Versions](https://standard.aimoaas.com/latest/standard/versions/) page for the difference between versioned URLs and `/latest/`.

### What if `/latest/` differs from the latest release?

This is a deployment bug. Verify against [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) and report the issue. The `latest` alias should always redirect to the most recent tagged release.

### How do I verify which version `/latest/` points to?

```bash
# Check redirect target
curl -sI https://standard.aimoaas.com/latest/ | grep -i location

# Or check mike alias list (requires repo access)
mike list
```

---

## Related Documentation

- [Versions Page](https://standard.aimoaas.com/latest/standard/versions/)
- [SEO & Canonical Policy](https://standard.aimoaas.com/latest/governance/seo-canonical-policy/)
- [Releases Hub](https://standard.aimoaas.com/latest/releases/)
