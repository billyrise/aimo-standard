---
description: Informative roadmap for v0.2. Audit object SSOT, Evidence-as-Code, output profiles, Test library, lifecycle, JNC.
---

# v0.2 roadmap (informative)

This page summarizes planned directions for a **future major version** (v0.2). It is **informative** only; the normative specification for any release is the standard and schemas for that version. Target timeline: 2026 Q4–2027.

## Planned themes

| Theme | Summary |
|-------|---------|
| **Audit object model (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange as normative objects with fixed IDs and reference integrity. |
| **External framework bridge** | Output profiles for EU Annex IV, GPAI Form, ISO 42001, NIST AI RMF; machine-readable mapping and optional one-click export. |
| **Evidence-as-Code** | Normative integrity: signature verification, provenance (e.g. SLSA-style), reproducibility and change tracking. |
| **Test procedure library** | Standard test templates per control; alignment with ISAE 3000, SOC 2, ISO 19011. |
| **Operational lifecycle** | Event-driven process (Intake → Review → Exception → Renewal → Change → Decommission) with required logs and evidence. |
| **Industry / jurisdiction profiles** | Optional profiles by sector and jurisdiction. |
| **Justified non-compliance (JNC)** | Optional mechanism to record and justify intentional non-compliance (informative). |
| **OSCAL linkage** | Standard way to link Evidence Bundle to Control/Requirement for export to NIST OSCAL or similar. |

## References

- [v0.1 object model scope](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — v0.1 MUST vs reserved
- [Signature verification roadmap](../../artifacts/signature-verification-roadmap.md) — signing and verification evolution
- [Releases](../../../releases/) — release assets and changelog
