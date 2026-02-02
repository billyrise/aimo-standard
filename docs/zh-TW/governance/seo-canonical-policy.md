---
description: AIMO SEO and canonical URL policy - URL canonicalization strategy for search engines, auditors, and external references.
# TRANSLATION METADATA - DO NOT REMOVE
source_file: en/governance/seo-canonical-policy.md
source_hash: 3932484358683f0c
translation_date: 2026-02-02
translator: pending
translation_status: needs_translation
---

# SEO & Canonical Policy

This page documents how AIMO Standard manages URL canonicalization for search engines, auditors, and external references.

## Production vs Mirror Sites

| Environment | URL | Role | Indexable |
|-------------|-----|------|-----------|
| **Production** | `https://standard.aimoaas.com/` | Canonical site for all purposes | Yes |
| GitHub Pages | `https://billyrise.github.io/aimo-standard/` | Temporary mirror / CI preview | No (noindex) |

**Key principle**: Production (`standard.aimoaas.com`) is the authoritative URL. GitHub Pages serves as a temporary backup/mirror and should not be cited in audit reports or external references.

## Canonical URL Strategy

### How Canonical URLs Are Generated

AIMO Standard uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) with the following configuration:

```yaml
# mkdocs.yml
site_url: https://standard.aimoaas.com/
```

This `site_url` setting ensures:

1. **`<link rel="canonical">`** — Each generated HTML page includes a canonical link pointing to the Production URL.
2. **`sitemap.xml`** — All URLs in the sitemap reference Production.
3. **`robots.txt`** — Sitemap reference points to Production.
4. **`hreflang` alternates** — Language alternates use Production URLs.

### Language-Specific Canonicals

| Language | URL Pattern | Example |
|----------|-------------|---------|
| English (default) | `https://standard.aimoaas.com/{path}` | `https://standard.aimoaas.com/governance/` |
| Japanese | `https://standard.aimoaas.com/ja/{path}` | `https://standard.aimoaas.com/ja/governance/` |

Each language version is self-canonical and includes `hreflang` alternates to the other language(s) plus `x-default` pointing to the English version.

### Versioned Documentation and Canonicals

AIMO Standard uses [mike](https://github.com/jimporter/mike) for documentation versioning with `alias_type: redirect`:

| Version | URL Pattern | Canonical Status | Indexable |
|---------|-------------|------------------|-----------|
| Versioned (e.g., `0.0.1`) | `https://standard.aimoaas.com/0.0.1/` | Canonical for that specific version | Yes |
| `latest` (alias) | `https://standard.aimoaas.com/latest/` | **Redirects** to current release | Yes (via target) |
| `dev` | `https://standard.aimoaas.com/dev/` | Preview only | **No** (noindex enforced) |

**Critical distinctions:**

| Aspect | `/X.Y.Z/` | `/latest/` | `/dev/` |
|--------|-----------|------------|---------|
| Content | Frozen snapshot | Redirect to `/X.Y.Z/` | Main branch preview |
| Mutable | Never | Pointer updates on release | Continuous |
| For audits | **Yes (preferred)** | Yes (resolves to frozen) | **Never** |
| SEO | Indexed | Indexed via target | noindex |

**How alias_type: redirect works:**

Instead of copying files, `/latest/` contains redirect pages pointing to the current release:

```html
<!-- /latest/index.html -->
<meta http-equiv="refresh" content="0; url=../0.0.1/">
<link rel="canonical" href="https://standard.aimoaas.com/0.0.1/">
```

This ensures:

1. **No content drift** — `/latest/` cannot diverge from the release it points to.
2. **No duplicate content** — Search engines see one canonical source.
3. **Atomic updates** — Changing the alias updates all pages at once.

!!! info "Git Tag vs. Site Path"
    Git release tags use `v` prefix (e.g., `v0.0.1`), but site paths omit the `v` (e.g., `/0.0.1/`). This is standard practice for documentation versioning tools like mike.

## Auditor Guidance: Which URL to Cite

When citing AIMO Standard in audit reports, compliance documentation, or external references:

### Recommended Citation URLs

| Use Case | Recommended URL |
|----------|-----------------|
| Current stable specification | `https://standard.aimoaas.com/latest/standard/current/` |
| Specific version (for audit) | `https://standard.aimoaas.com/{X.Y.Z}/standard/current/` |
| Governance & policies | `https://standard.aimoaas.com/latest/governance/` |
| Trust Package | `https://standard.aimoaas.com/latest/governance/trust-package/` |

### Do NOT Cite

- ~~`https://billyrise.github.io/aimo-standard/`~~ — Temporary mirror, not canonical
- ~~`https://standard.aimoaas.com/dev/`~~ — Development version, subject to change

### Versioned Citation for Immutability

For formal audits requiring immutable references, use versioned snapshot URLs:

```
https://standard.aimoaas.com/1.0.0/standard/current/01-overview/
```

Versioned snapshots are frozen at release time and will not change.

!!! note "URL Format"
    Site paths use version numbers without the `v` prefix. For version `v1.0.0`, use `/1.0.0/` in URLs.

## Technical Implementation

### Generated HTML Example

Every generated HTML page includes canonical and hreflang tags in the `<head>`:

```html
<!-- Canonical (always points to Production) -->
<link rel="canonical" href="https://standard.aimoaas.com/latest/governance/">

<!-- Language alternates -->
<link rel="alternate" hreflang="en" href="https://standard.aimoaas.com/latest/governance/">
<link rel="alternate" hreflang="ja" href="https://standard.aimoaas.com/latest/ja/governance/">
<link rel="alternate" hreflang="x-default" href="https://standard.aimoaas.com/latest/governance/">
```

### robots.txt

```
User-agent: *
Allow: /

Sitemap: https://standard.aimoaas.com/sitemap.xml
```

### Sitemap

The sitemap is generated by `mkdocs-static-i18n` plugin and includes:

- All Production URLs
- `hreflang` alternates for each language

## Noindex Configuration

### `/dev/` (Preview) — Mandatory Noindex

The `/dev/` version contains unreleased content and MUST have noindex to prevent:

- Search engines indexing unstable content
- Users finding `/dev/` via search and citing it in audits
- Confusion between released and unreleased content

**Implementation:**

The `deploy-dev.yml` workflow injects a noindex meta tag into all `/dev/` pages via theme override:

```html
<!-- Injected into /dev/ pages only -->
<meta name="robots" content="noindex, nofollow">
```

### GitHub Pages Mirror — Noindex

When deploying to GitHub Pages (the mirror site at `billyrise.github.io`), all pages should have noindex to prevent duplicate indexing:

```html
<meta name="robots" content="noindex, nofollow">
```

This ensures search engines always prioritize the Production canonical URLs at `standard.aimoaas.com`.

## Verification

After each build, you can verify canonical URLs by:

1. **Inspecting generated HTML** — Check `site/` directory after `mkdocs build`
2. **Using browser DevTools** — Inspect `<head>` section on deployed pages
3. **Google Search Console** — Monitor which URLs are indexed

Example verification command:

```bash
mkdocs build
grep -r 'rel="canonical"' site/ | head -5
```

Expected output should show Production URLs, e.g.:

```
site/index.html:<link rel="canonical" href="https://standard.aimoaas.com/">
site/governance/index.html:<link rel="canonical" href="https://standard.aimoaas.com/governance/">
```

## Related Documentation

- [Trust Package](trust-package.md) — Auditor-ready materials
- [Releases](../releases/index.md) — Version history and changelog
- [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) — Version policy
