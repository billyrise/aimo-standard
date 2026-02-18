---
description: Beschaffungs- und Offenlegungs-Overlays (UK, Japan). UK ATRS, UK-Beschaffungsleitfaden, japanische Regierungs-GenAI-Beschaffung und AI Business Guidelines. Nur Referenzzuordnung.
---
<!-- aimo:translation_status=translated -->

# Beschaffungs- und Offenlegungs-Overlays (UK, Japan)

Diese Seite beschreibt **Referenzzuordnungen** zwischen AIMO-Evidenz und ausgewählten **UK-** und **Japan-**Beschaffungs- und Offenlegungsrahmen. Ziel ist **Kostenreduzierung durch Wiederverwendung von AIMO-Evidenz**. Es handelt sich um **nur informative Zuordnung**; AIMO garantiert keine vollständige Konformität mit behördlichen Anforderungen. Prüfen Sie gegen die offiziellen Quellen unten.

## Primärquellen

**UK**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (Vorlage, Leitfaden, veröffentlichte Berichte)
- [ATRS-Vorlage](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Offizielle Vorlage für den öffentlichen Sektor
- [Leitfaden für Organisationen zur Nutzung des ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Japan**

- [Digital Agency — GenAI procurement and utilisation guideline](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat)
- [AI Business Guidelines](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (Ministry of Economy, Trade and Industry / Ministry of Internal Affairs and Communications)

## Zuordnungstabelle (UK)

| Behördliche Anforderung (Thema) | AIMO-Artefakte | Wo im Evidence Bundle | Validator-Abdeckung | Hinweis |
| --- | --- | --- | --- | --- |
| ATRS — Verantwortung / Eigentümer | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | Informative Zuordnung; garantiert keine vollständige Konformität. |
| ATRS — System-/Modellbeschreibung | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Offiziellen ATRS-Bericht in External Forms anfügen; per logical_id verknüpfen. |
| ATRS — Risikoerwägungen | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | Profil: `coverage_map/profiles/uk_atrs_procurement.json`. |
| Beschaffung — Lieferantenevidenz | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | Bündel zur Evidenzstrukturierung nutzen; UK-Leitfaden bleibt maßgeblich. |

## Zuordnungstabelle (Japan)

| Behördliche Anforderung (Thema) | AIMO-Artefakte | Wo im Evidence Bundle | Validator-Abdeckung | Hinweis |
| --- | --- | --- | --- | --- |
| GenAI-Beschaffungs-Checkliste (Digital Agency) | External Form (Checkliste unverändert); Dictionary, Summary | payload_index; Abschnitt External Forms; Manifest-Referenz | N/A (Anhang) | Informative Zuordnung; garantiert keine vollständige Konformität. Profil: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — Governance / Nachverfolgbarkeit | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Checklistenpunkte wo nützlich der AIMO-Taxonomie zuordnen. |
| Risiko- / Verantwortungsdokumentation | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | Gegen offizielle Leitfäden von Digital Agency und METI/MIC prüfen. |

## UK: ATRS und KI-Beschaffung (Zusammenfassung)

| Thema | AIMO-Evidenz / Zuordnung | Hinweise |
| --- | --- | --- |
| **UK ATRS** (AI Transparency Record) | Summary, review (Verantwortungsträger), evidence (Modell-/Systembeschreibung), dictionary (Risikoerwägungen). Profil: `coverage_map/profiles/uk_atrs_procurement.json`. | ATRS-artigen Transparenzbericht in External Forms anfügen oder referenzieren; über logical_id mit Bündelobjekten verknüpfen. |
| **UK-Beschaffungsleitfaden** | Request, review, exception; Evidence Bundle für Lieferantenbewertung. | AIMO-Bündel zur Strukturierung von Evidenz für Beschaffungsbewertung nutzen; offizieller UK-Leitfaden bleibt maßgeblich. |

## Japan: Regierungs-GenAI-Beschaffung und AI Business Guidelines (Zusammenfassung)

| Thema | AIMO-Evidenz / Zuordnung | Hinweise |
| --- | --- | --- |
| **JP Regierungs-GenAI-Beschaffungs-Checkliste** | Checkliste als External Form anfügen (z. B. payload: JP_PROCUREMENT_CHECKLIST); im Manifest referenzieren. Profil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Nur Referenzzuordnung; AIMO ersetzt keine offiziellen Checklisten. |
| **AI Business Guidelines** | Summary, dictionary; Checklistenpunkte wo sinnvoll für Nachverfolgbarkeit auf AIMO-Taxonomiecodes abbilden. | Zur Erklärbarkeit nutzen; gegen offizielle japanische Leitlinie prüfen. |

## Nutzung

- **External Forms**: UK- oder Japan-offizielle Vorlagen/Checklisten **unverändert** anfügen (PDF, DOC usw.), hashen und im Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) oder im [EV-Vorlage-External-Forms-Abschnitt](../../standard/current/06-ev-template/) aufführen. Im Manifest und in Coverage-Zuordnungen per logical_id referenzieren.
- **Profile**: Die genannten Profile definieren optionale maschinenlesbare Zuordnungen; sie begründen keine rechtlichen oder vertraglichen Verpflichtungen.

Stufen siehe [Konformität](../../conformance/); Overlay-Übersicht siehe [Mindestanforderungen an Evidence — Regulatorische Overlays](../../artifacts/minimum-evidence/).
