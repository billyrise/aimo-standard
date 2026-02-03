---
description: Versioning and reference policy for documentation URLs. Defines immutable /X.Y.Z/, stable /latest/, and non-citable /dev/. Operational rules for audit and citation.
---

# Versioning & Reference Policy

This page defines the **operational policy** for documentation URLs. Third parties (auditors, implementers, and tooling) MUST interpret URLs according to these rules.

## Normative URL semantics

| URL pattern | Meaning | MUST |
|-------------|---------|------|
| **`/X.Y.Z/`** (e.g. `/0.0.3/`) | **Immutable release** — frozen snapshot. Content MUST NOT change after release. | Use for audit citations and reproducible references. Once published, `/X.Y.Z/` is **never** rewritten. |
| **`/latest/`** | **Latest stable release only.** Alias (redirect) to the most recent **released** version. | MUST point only to a tagged release. MUST NOT point to development, PR previews, or `/dev/`. |
| **`/dev/`** | **Development (unstable).** Preview of the main branch; content may change at any time. | MUST NOT be used for audit submission or citation. For reference and reproducibility, use `/latest/` or `/X.Y.Z/` instead. |

## Rules (MUST)

1. **`/X.Y.Z/` is immutable.**  
   A released version directory is frozen at release time. No further edits, fixes, or replacements to that path are permitted. If a fix is required, release a new version (e.g. `X.Y.Z+1`).

2. **`/latest/` means “latest stable” only.**  
   `/latest/` MUST redirect to the current **tagged** release (e.g. the version indicated by the GitHub Releases “latest” tag). It MUST NOT serve development builds, pull-request previews, or unreleased content.

3. **`/dev/` is development (unstable).**  
   `/dev/` reflects the current main branch and is explicitly **unreleased**. It MUST NOT be cited or submitted as evidence in audits. The site MAY apply `noindex` and/or a visible “Development Preview” notice for `/dev/` to avoid misuse.

4. **Release process updates `/latest/`.**  
   The `/latest/` alias is updated **only** by the official release process. That process MUST:
   - Be triggered by a **version tag** (e.g. `vX.Y.Z`) pushed to the repository;
   - Run quality gates (tests, lints) before deploy;
   - Deploy the versioned documentation to `/X.Y.Z/`;
   - Set or update the `latest` alias to point to that `/X.Y.Z/` (e.g. via `mike set-default latest` or equivalent);
   - Create the corresponding GitHub Release with assets (e.g. PDFs, artifacts, checksums).

   Routine pushes to `main` (without a version tag) MUST NOT change `/latest/`; they may update `/dev/` only.

## Summary for auditors

- **Canonical, reproducible citation:** Use `https://standard.aimoaas.com/X.Y.Z/` (e.g. `0.0.3`) and record the version and, if needed, the release tag or commit from the [GitHub Release](https://github.com/billyrise/aimo-standard/releases) page.
- **General reference:** `/latest/` is acceptable as it redirects to the current stable release.
- **Do not cite:** `/dev/` — it is development-only and not for audit or submission.

## See also

- [Versions](../versions/index.md) — Version history, SSOT for “latest,” and verification procedure
- [Changelog](08-changelog.md) — Normative change history
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Full versioning policy and release flow
- [Release workflow](https://github.com/billyrise/aimo-standard/blob/main/.github/workflows/release.yml) — How tagging updates `/latest/` and deploys `/X.Y.Z/`
