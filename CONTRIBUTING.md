# Contributing to AIMO Standard

Thank you for your interest in contributing to AIMO Standard. This document provides guidelines for contributing to the project.

For detailed contribution workflows and policies, see the full documentation:
**[Contributing Guide (Website)](https://standard.aimoaas.com/latest/governance/contributing/)**

## Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run quality checks (see below)
5. Submit a pull request

## Quality Checks

Before submitting a PR, run these checks:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run all lints
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Build documentation
mkdocs build --strict
```

## Key Principles

- **English is canonical**: Edit `docs/en/` first.
- **Development: English only**: During day-to-day development, update **English docs only** (`docs/en/`). Do not update other locales until release.
- **Translation at release**: When creating a new version (bumping version number, tagging `vX.Y.Z`), run **full translation to all other languages** (ja, es, fr, de, pt, it, zh, zh-TW, ko) so the release ships with all locales in sync. See release process (e.g. `.cursor/rules/02-release-process.md` or prepare-release workflow).
- **SSOT**: This repository is the single source of truth
- **No manual edits to generated files**: Edit sources, regenerate, commit
- **All changes via PR**: Even maintainers use pull requests

## Change Types

| Type | Examples | Review |
| ---- | -------- | ------ |
| Normative | Schema changes, requirements | Maintainer + discussion |
| Non-normative | Typos, clarifications | Maintainer approval |
| i18n | Translations | Structure must match EN |
| Tooling | CI/CD, scripts | Maintainer approval |

## i18n Guidelines

- English (`docs/en/`) is the authoritative source.
- **During development**: Update only `docs/en/`. Other locales are updated at release time.
- **At release**: Translate from English to all locales (ja, es, fr, de, pt, it, zh, zh-TW, ko); all must mirror the same structure and pass `lint_i18n.py`.
- Keep the same heading hierarchy and page count across locales.
- Run `lint_i18n.py` to verify consistency (required for release).

## Questions?

Open a GitHub issue for questions or discussion.

## Related Resources

- [GOVERNANCE.md](GOVERNANCE.md) — Project governance
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community guidelines
- [SECURITY.md](SECURITY.md) — Security policy
