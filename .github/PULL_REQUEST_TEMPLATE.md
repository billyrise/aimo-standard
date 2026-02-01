## Summary

<!-- Brief description of the changes -->

## Change Type

<!-- Check all that apply -->

- [ ] Documentation (docs/)
- [ ] JSON Schemas (schemas/)
- [ ] Templates (templates/)
- [ ] Examples (examples/)
- [ ] Validator (validator/)
- [ ] Tooling (tooling/)
- [ ] CI/CD Workflows

## Breaking Change Assessment

- [ ] This is NOT a breaking change
- [ ] This is a breaking change (requires version bump and migration guide)

## i18n Checklist

<!-- If documentation changes are included -->

- [ ] English documentation updated (docs/en/)
- [ ] Japanese documentation updated (docs/ja/)
- [ ] Structure matches between EN and JA
- [ ] N/A (no documentation changes)

## Quality Checks

<!-- Verify these pass before requesting review -->

- [ ] `python tooling/checks/lint_i18n.py` passes
- [ ] `python tooling/checks/lint_schema.py` passes
- [ ] `python tooling/audit/baseline_audit.py --check` passes
- [ ] `mkdocs build --strict` passes

## Evidence

<!-- Link related files, issues, or releases affected -->

- Related issue: #
- Affected files:
- Release impact:

## Notes for Reviewers

<!-- Any additional context for reviewers -->
