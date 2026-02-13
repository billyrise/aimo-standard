---
description: AIMO Standard to EU AI Act mapping. Traceability between AIMO taxonomy codes and EU AI Act risk categories and requirements.
---

# EU AI Act mapping

> Traceability shortcuts: Taxonomy → Minimum Evidence → Validator → Human Oversight Protocol.

- [Taxonomy](../standard/current/03-taxonomy.md)
- [Minimum Evidence Requirements](../artifacts/minimum-evidence.md)
- [Log Schemas](../artifacts/log-schemas/index.md)
- [Validator](../validator/index.md)
- [Human Oversight Protocol](../governance/human-oversight-protocol.md)

This page maps selected EU AI Act themes (documentation, record-keeping, risk management, human oversight, transparency) to AIMO evidence and artifacts. It is high-level only and does **not** constitute legal advice or guarantee conformity. Verify against the official legal text.


## Mapping table

| Framework reference / topic | AIMO evidence / where in AIMO | Evidence Bundle / Minimum Evidence | Artifacts & validation | Notes |
| --- | --- | --- | --- | --- |
| Art 9 – Risk management (obligations) | [Scope](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | High-level only; not legal advice. Verify against official text. |
| Art 10 – Data governance | [Dictionary](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | High-level only; not legal advice. Verify against official text. |
| Art 11 – Documentation (high-risk) | [EV Template](../standard/current/06-ev-template.md), [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Annex IV sample**: [Examples > EU Annex IV sample](../examples/index.md) (`examples/evidence_bundle_v01_annex_iv_sample/`); profile: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Sample bundle is normative-compliant (signatures/, hashes/, payload with Annex IV–oriented technical documentation). | High-level only; not legal advice. Verify against official text. |
| Art 12 – Record-keeping | [Evidence Bundle](../artifacts/evidence-bundle.md), [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | High-level only; not legal advice. Verify against official text. |
| Art 13 – Transparency (user information) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | High-level only; not legal advice. Verify against official text. |
| Art 14 – Human oversight | [Minimum Evidence](../artifacts/minimum-evidence.md) | review, exception; review, exception | templates/ev/ev_template.md | High-level only; not legal advice. Verify against official text. |
| Art 17 – Risk management (high-risk) | [Scope](../standard/current/02-scope.md) | request, review, exception, renewal | templates/ev/ | High-level only; not legal advice. Verify against official text. |
| Art 26 – Transparency (limited risk) | [Scope](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | High-level only; not legal advice. Verify against official text. |
| Art 29 – Documentation (general-purpose AI) | [EV Template](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | High-level only; not legal advice. Verify against official text. |
| Art 52 – Transparency (deployer) | [Minimum Evidence](../artifacts/minimum-evidence.md) | EV, Summary; review | templates/ev/ | High-level only; not legal advice. Verify against official text. |
| Recitals – Accountability | [Evidence Bundle](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | High-level only; not legal advice. Verify against official text. |
