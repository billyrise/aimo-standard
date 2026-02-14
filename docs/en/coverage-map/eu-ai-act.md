---
description: AIMO Standard to EU AI Act mapping. Traceability between AIMO taxonomy codes and EU AI Act risk categories and requirements.
---

# EU AI Act mapping

> Traceability shortcuts: Taxonomy → Minimum Evidence → Validator → Human Oversight Protocol.

- [Taxonomy](../../standard/current/03-taxonomy/)
- [Minimum Evidence Requirements](../../artifacts/minimum-evidence/)
- [Log Schemas](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Human Oversight Protocol](../../governance/human-oversight-protocol/)

This page maps selected EU AI Act themes (documentation, record-keeping, risk management, human oversight, transparency) to AIMO evidence and artifacts. It is high-level only and does **not** constitute legal advice or guarantee conformity. Verify against the official legal text.

**Reference:** Regulation (EU) 2024/1689 (Artificial Intelligence Act). All article numbers below refer to that regulation.

## Mapping table

| Framework reference / topic | AIMO evidence / where in AIMO | Evidence Bundle / Minimum Evidence | Artifacts & validation | Notes |
| --- | --- | --- | --- | --- |
| Art 4 – AI literacy | [Scope](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Cross-cutting; evidence of organisational capability/training (high-level). Not legal advice. Verify against official text. |
| Art 9 – Risk management system | [Scope](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | High-risk AI systems (Title III). Not legal advice. Verify against official text. |
| Art 10 – Data and data governance | [Dictionary](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Not legal advice. Verify against official text. |
| Art 11 – Technical documentation (high-risk) | [EV Template](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Annex IV**: see [Examples > EU Annex IV sample](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); profile: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Sample bundle is normative-compliant (signatures/, hashes/, payload with Annex IV–oriented technical documentation). See Examples for details (further sample content in a future release). | High-level only; not legal advice. Verify against official text. |
| Art 12 – Record-keeping | [Evidence Bundle](../../artifacts/evidence-bundle/), [Minimum Evidence](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Not legal advice. Verify against official text. |
| Art 13 – Transparency and provision of information to deployers/users | [Scope](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | High-risk context. Not legal advice. Verify against official text. |
| Art 14 – Human oversight | [Minimum Evidence](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | Not legal advice. Verify against official text. |
| Art 15 – Accuracy, robustness, cybersecurity | [Minimum Evidence](../../artifacts/minimum-evidence/) | EV (evidence codes / risk codes, high-level) | templates/ev/ | High-level mapping only. Not legal advice. Verify against official text. |
| Art 17 – Quality management system | [Scope](../../standard/current/02-scope/) | Summary, review (organisation process) | templates/ev/ | Distinct from Art 9 (risk management system). Not legal advice. Verify against official text. |
| Transparency obligations (use-case dependent) | [Scope](../../standard/current/02-scope/), [Minimum Evidence](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | Applicable provisions depend on use case (e.g. limited-risk, deployer duties). Not legal advice. Verify against official text. |
| GPAI models obligations | [EV Template](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | EV Template, Evidence Bundle (evidence-structuring framework) | schemas/jsonschema/; schema_validate_ev | AIMO provides a framework for organising evidence; actual obligations are defined by the regulation. Not legal advice. Verify against official text. |
| Recitals – Accountability | [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Not legal advice. Verify against official text. |

## Effective dates / applicability (high-level)

The following is a **high-level, non-exhaustive** summary of key application dates under Regulation (EU) 2024/1689. It is **not legal advice** and does not guarantee accuracy. Always confirm with the **official legal text** and competent authorities.

| Phase | Date (approximate) | What applies (high-level) |
|-------|--------------------|----------------------------|
| Entry into force | August 2024 | Regulation in force; most substantive obligations not yet applicable. |
| First application | February 2025 | Prohibited practices (unacceptable risk); certain AI literacy–related provisions. |
| GPAI codes of practice | May 2025 | Codes of practice for general-purpose AI models to be ready. |
| Notified bodies, GPAI, governance | August 2025 | Rules on notified bodies, GPAI, governance, confidentiality, penalties. |
| High-risk systems | 2026–2027 | Full applicability for high-risk AI systems; compliance and enforcement. |

**Official reference:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex). For a timeline overview, see also the [EU AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline) (external; not an official EU source).

This page is for explanatory use only. **You must verify applicability and dates against the official regulation and any implementing or amending acts.**
