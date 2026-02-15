---
description: Informative Roadmap für v0.2. Audit-Objekt-SSOT, Evidence-as-Code, Ausgabeprofile, Testbibliothek, Lebenszyklus, JNC.
---
<!-- aimo:translation_status=translated -->

# v0.2-Roadmap (informativ)

Diese Seite fasst geplante Richtungen für eine **zukünftige Hauptversion** (v0.2) zusammen. Sie ist **nur informativ**; die normative Spezifikation für jede Freigabe ist der Standard und die Schemas für diese Version. Zielzeitraum: 2026 Q4–2027.

## Geplante Themen

| Thema | Zusammenfassung |
| --- | --- |
| **Audit-Objektmodell (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange als normative Objekte mit festen IDs und Referenzintegrität. |
| **Externer Rahmenbrücke** | Ausgabeprofile für EU-Anhang IV, GPAI-Formular, ISO 42001, NIST AI RMF; maschinenlesbare Zuordnung und optionaler Ein-Klick-Export. |
| **Evidence-as-Code** | Normative Integrität: Signaturverifizierung, Herkunft (z. B. SLSA-artig), Reproduzierbarkeit und Änderungsverfolgung. |
| **Testverfahrensbibliothek** | Standard-Testvorlagen pro Kontrolle; Ausrichtung mit ISAE 3000, SOC 2, ISO 19011. |
| **Operativer Lebenszyklus** | Ereignisgesteuerter Prozess (Intake → Review → Exception → Renewal → Change → Decommission) mit erforderlichen Protokollen und Evidenz. |
| **Branchen-/Rechtsraumprofile** | Optionale Profile nach Sektor und Rechtsraum. |
| **Begründete Nichtkonformität (JNC)** | Optionaler Mechanismus zur Erfassung und Rechtfertigung vorsätzlicher Nichtkonformität (informativ). |
| **OSCAL-Anbindung** | Standardweg zur Verknüpfung des Evidence Bundle mit Control/Requirement für Export nach NIST OSCAL oder ähnlich. |

## Referenzen

- [v0.1-Objektmodellumfang](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — v0.1 MUST vs. reserviert
- [Signaturverifizierungs-Roadmap](../../../artifacts/signature-verification-roadmap/) — Entwicklung von Signierung und Verifizierung
- [Releases](../../../releases/) — Release-Artefakte und Changelog
