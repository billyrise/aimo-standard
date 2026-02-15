---
description: Beschaffungs- und Offenlegungs-Overlays (UK, Japan). UK ATRS, UK-Beschaffungsleitfaden, japanische Regierungs-GenAI-Beschaffung und AI Business Guidelines. Nur Referenzzuordnung.
---
<!-- aimo:translation_status=translated -->

# Beschaffungs- und Offenlegungs-Overlays (UK, Japan)

Diese Seite beschreibt **Referenzzuordnungen** zwischen AIMO-Evidenz und ausgewählten **UK-** und **Japan-**Beschaffungs- und Offenlegungsrahmen. Es handelt sich **nur um Referenzzuordnung**; AIMO ersetzt keine offiziellen Checklisten oder behördlichen Leitfäden.

## UK: ATRS und KI-Beschaffung

| Thema | AIMO-Evidenz / Zuordnung | Hinweise |
| --- | --- | --- |
| **UK ATRS** (AI Transparency Record) | Summary, review (Verantwortungsträger), evidence (Modell-/Systembeschreibung), dictionary (Risikoerwägungen). Profil: `coverage_map/profiles/uk_atrs_procurement.json`. | ATRS-artigen Transparenzbericht in External Forms anfügen oder referenzieren; über logical_id mit Bündelobjekten verknüpfen. |
| **UK-Beschaffungsleitfaden** | Request, review, exception; Evidence Bundle für Lieferantenbewertung. | AIMO-Bündel zur Strukturierung von Evidenz für Beschaffungsbewertung nutzen; offizieller UK-Leitfaden bleibt maßgeblich. |

## Japan: Regierungs-GenAI-Beschaffung und AI Business Guidelines

| Thema | AIMO-Evidenz / Zuordnung | Hinweise |
| --- | --- | --- |
| **JP Regierungs-GenAI-Beschaffungs-Checkliste** | Checkliste als External Form anfügen (z. B. payload: JP_PROCUREMENT_CHECKLIST); im Manifest referenzieren. Profil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Nur Referenzzuordnung; AIMO ersetzt keine offiziellen Checklisten. |
| **AI Business Guidelines** | Summary, dictionary; Checklistenpunkte wo sinnvoll für Nachverfolgbarkeit auf AIMO-Taxonomiecodes abbilden. | Zur Erklärbarkeit nutzen; gegen offizielle japanische Leitlinie prüfen. |

## Nutzung

- **External Forms**: UK- oder Japan-offizielle Vorlagen/Checklisten **unverändert** anfügen (PDF, DOC usw.), hashen und im Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) oder im [EV-Vorlage-External-Forms-Abschnitt](../../standard/current/06-ev-template/) aufführen. Im Manifest und in Coverage-Zuordnungen per logical_id referenzieren.
- **Profile**: Die genannten Profile definieren optionale maschinenlesbare Zuordnungen; sie begründen keine rechtlichen oder vertraglichen Verpflichtungen.

Stufen siehe [Konformität](../../conformance/); Overlay-Übersicht siehe [Mindestanforderungen an Evidence — Regulatorische Overlays](../../artifacts/minimum-evidence/).
