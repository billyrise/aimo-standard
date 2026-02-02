---
description: AIMO Standard contribution guide - How to contribute code, documentation, and translations. Issue and PR guidelines.
---

# Contributing

This page provides guidelines for contributing to AIMO Standard.

## Quick Start

1. Fork the repository
2. Create a feature branch
3. Make changes following the guidelines below
4. Run quality checks
5. Submit a pull request

## Key Principles

| Principle | Description |
| --------- | ----------- |
| English is canonical | Edit `docs/en/` first, then update `docs/ja/` |
| SSOT | This repository is the single source of truth |
| No manual edits to generated files | Edit sources, regenerate, commit |
| All changes via PR | Even maintainers use pull requests |

## Quality Checks

Before submitting a PR, run:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run lints
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Build documentation
mkdocs build --strict
```

## Change Types

| Type | Examples | Review Requirements |
| ---- | -------- | ------------------- |
| Normative | Schema changes, requirements | Maintainer + discussion |
| Non-normative | Typos, clarifications | Maintainer approval |
| i18n | Translations | Structure must match EN |
| Tooling | CI/CD, scripts | Maintainer approval |

## i18n Guidelines

### Update Order

1. Edit English source (`docs/en/...`)
2. Update Japanese translation (`docs/ja/...`)
3. Run `lint_i18n.py` to verify consistency
4. Commit both together

### Structure Requirements

- Same file names in both languages
- Same heading hierarchy
- Same page count per section

## PR Checklist

When submitting a PR, verify:

- [ ] Change type identified (docs / schema / examples / tooling)
- [ ] Breaking change assessment completed
- [ ] i18n: EN and JA updated together (if applicable)
- [ ] Quality checks pass
- [ ] Related issues linked

## Breaking Changes

Breaking changes require:

1. Issue discussion before implementation
2. Version bump per [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Changelog entry with migration guidance

## Conformance Claim Updates

To add or modify conformance claims:

1. Update the coverage map YAML
2. Update corresponding documentation pages
3. Run validator tests
4. Document the mapping rationale

## Full Guidelines

See [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) for the root-level guide.

## Related Pages

- [Governance](index.md) — Project governance
- [Localization Guide](../contributing/localization.md) — i18n details
- [Responsibility Boundary](responsibility-boundary.md) — What AIMO provides
