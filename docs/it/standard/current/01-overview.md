---
description: Overview of AIMO Standard. Defines shared taxonomy, code system, dictionary, evidence templates, and validator checks for AI governance audits.
---

# Overview

**AIMO** stands for **AI Management Office**. AIMO Standard defines:
- a shared taxonomy
- a code system
- an initial dictionary
- an EV template
- validator checks (spec + minimal reference implementation)

This repository publishes:
- human-readable spec (HTML)
- machine-readable artifacts (schemas/templates/examples)
- official PDF releases

## Positioning: Companion to ISO/IEC 42001 (AIMS)

AIMO Standard is an **implementation accelerator for evidence readiness and explainability** that can be used to support ISO/IEC 42001–aligned AI Management Systems (AIMS) and to structure audit-ready evidence. It does not replace ISO/IEC 42001 or any other management-system standard; it adds a taxonomy, evidence bundle structure, and coverage mapping that help operationalize and evidence those controls.

**What AIMO is**

- Taxonomy and code system for AI governance classification
- Evidence bundle structure (manifest, object_index, payload_index, integrity)
- Validator and coverage mapping for traceability
- Conformance levels (Foundation, Operational, Audit-Ready) — AIMO-only maturity tiers for evidence packaging

**What AIMO is not**

- Legal advice
- ISO certification or a substitute for certification
- A guarantee of regulatory compliance
- A replacement for auditor judgment or accredited certification bodies

**Why now**

- **ISO/IEC 42006** (published 2025-07) specifies requirements for bodies auditing and certifying AI management systems against ISO/IEC 42001, raising expectations for auditable evidence and traceability.
- The **EU AI Act** is in progressive application (2025–2027); harmonised standards, when published in the Official Journal, will provide presumption of conformity. The EU AI Office is preparing practical guidelines during 2026 (high-risk classification, Article 50 transparency, incidents, QMS elements).
- Adopters and certification bodies increasingly use ISO/IEC 42001 as a system layer for AI governance; AIMO helps structure evidence that supports that layer without claiming certification.

## References

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — Requirements for bodies auditing and certifying AI management systems
- [EU AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline) (AI Act Service Desk / Commission-aligned; informative)
- [European Commission — Clear guidelines for AI (Dec 4 2025)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — AI Office guidelines preparation (check Commission news for current URL)
- [EPRS — EU AI Act implementation timeline (June 2025)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — Parliament briefing (informative)
