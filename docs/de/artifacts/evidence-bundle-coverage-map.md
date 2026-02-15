---
description: Evidence-Bundle-Coverage-Map-Vorlage (v0.1). Informative Ein-Seiten-Zusammenfassung für Prüfer — Umfang, Evidenztypen, Kontrollzuordnung, Ausschlüsse, Integritätsnachweis.
---
<!-- aimo:translation_status=translated -->

# Evidence Bundle Coverage Map (Vorlage)

!!! info "Informativ — empfohlene Praxis"
    Diese Seite definiert eine **empfohlene Praxis-Vorlage** für eine einseitige Evidence-Bundle-Coverage-Map. Sie ist **keine** normative Anforderung des Standards. Nutzen Sie sie, um zu dokumentieren, was ein Bundle abdeckt und nicht abdeckt, für die Prüferübergabe. Referenzen (z. B. zu Frameworks) sind stabil; die Übernahme liegt im Ermessen des Implementierers.

---

## 1. Umfang

| Element | Beschreibung |
|------|--------------|
| **Umfangsreferenz** | `scope_ref` aus dem Bundle-Manifest (z. B. `SC-001`). Verknüpft dieses Bundle mit dem deklarierten Umfang. |
| **Bundle-ID** | `bundle_id` (UUID) — eindeutiger Bezeichner für dieses Bundle. |
| **Bundle-Version** | `bundle_version` (SemVer) — Version des Bundles. |
| **Zeitraum / Snapshot** | Optional: Zeitraum oder Snapshot-Datum, das dieses Bundle repräsentiert (z. B. 2026-Q1, as-of 2026-02-03). |

---

## 2. Evidenztypen (EV / objects vs. Payloads)

| Kategorie | Inhalt | v0.1 minimales Beispiel |
|----------|----------|------------------------|
| **object_index** | Aufgezählte Objekte (Metadaten, Indizes). Jeder Eintrag: `id`, `type`, `path`, `sha256`. | z. B. `objects/index.json` (Index-Typ). |
| **payload_index** | Payload-Dateien (Root-EV-JSON, Evidence-Pack-Dateien). Jeder Eintrag: `logical_id`, `path`, `sha256`, `mime`, `size`. | z. B. `payloads/root.json` (Root-AIMO-EV-JSON). |
| **EV-Typen** | Evidence-Datensätze (in Root oder verlinkten Payloads) — request, review, exception, renewal, change log. | Ausgerichtet an [Evidence Pack Template](../../standard/current/06-ev-template/) und [Mindestanforderungen an Evidence](../minimum-evidence/). |

*Implementierer können object_index und payload_index erweitern; Pfade MÜSSEN innerhalb des Bundle-Roots bleiben und die [Evidence-Bundle-Root-Struktur (v0.1)](../../standard/current/09-evidence-bundle-structure/) erfüllen.*

---

## 3. Kontrollzuordnung (nur Referenz)

Die Zuordnung zu externen Frameworks dient **nur zur Referenz**; der Standard schreibt die Einhaltung keiner bestimmten Regulation vor.

| Framework | Nutzung in diesem Bundle | Referenz |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | Optional: dokumentieren, welche KI-MS-Themen dieses Bundle unterstützt. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | Optional: Übergeordnete Dokumentation/Aufzeichnungspflicht-Ausrichtung. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | Optional: Govern, Map, Measure, Manage-Zuordnung. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | Optional: Model Documentation Form; in External Forms anhängen, per logical_id referenzieren. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/); Profil `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | Optional: GenAI-Profil (AI 600-1)-Artefakte. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/); Profil `nist_ai_600_1_genai.json` |
| **UK ATRS** | Optional: ATRS-Aufzeichnung, Beschaffungsbewertung. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); Profil `uk_atrs_procurement.json` |
| **JP Gov GenAI Beschaffung** | Optional: JP-Beschaffungs-Checkliste, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); Profil `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | Optional: Änderungsmanagement, Zugriff, Protokollierung, Integrität. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*„Nutzung in diesem Bundle“ pro Einreichung ausfüllen; der Standard verlangt keine bestimmte Kontrollabdeckung.*

### External Forms und Manifest-Referenz

**External Forms** (offizielle Vorlagen/Checklisten unverändert angehängt) sollen im **payload_index** des Bundles mit stabilem `logical_id`, `path`, `sha256`, `mime` und `size` aufgeführt werden. Prüfer können dann vom Manifest zur Datei nachverfolgen und den Hash verifizieren. Siehe [EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) und [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index).

---

## 4. Ausschlüsse / Annahmen

| Bereich | Was dieses Bundle **nicht** abdeckt (Beispielzeilen — pro Einreichung anpassen) |
|------|-------------------------------------------------------------------------------|
| **Ausschlüsse** | z. B. Systeme oder Anwendungsfälle außerhalb des Umfangs; nicht belegte Drittanbieterkomponenten; Zeitraum außerhalb dieses Bundles. |
| **Annahmen** | z. B. Dictionary/Taxonomie-Version; verwendete Validator-/Schema-Version; Aufbewahrung und Retention sind implementierungsdefiniert. |
| **Einschränkungen** | z. B. Signaturverifikation ist in v0.1 außerhalb des Umfangs; keine rechtliche Auslegung von Regulationen. |

*Platzhaltertext durch einreichungsspezifische Ausschlüsse und Annahmen ersetzen.*

---

## 5. Integritätsnachweis-Zusammenfassung (v0.1)

| Element | Was bereitgestellt wird (v0.1 normativ) |
|---------|----------------------------------|
| **manifest.json** | Vorhanden und schema-valide; enthält `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Jede Datei in `object_index` und `payload_index` hat einen deklarierten 64-Zeichen-Kleinbuchstaben-Hex-SHA256; der Validator prüft die Inhaltsübereinstimmung. |
| **Index-Existenz** | Alle aufgelisteten Pfade existieren unter dem Bundle-Root; kein Pfaddurchlauf (`../` oder führendes `/`). |
| **Signatur-Existenz** | Mindestens eine Signaturdatei in `signatures/`; das Manifest referenziert sie über `signing.signatures[]` mit `path` und `targets` (v0.1 MUSS `manifest.json` in targets enthalten). Kryptografische Verifikation ist in v0.1 außerhalb des Umfangs. |
| **Hash-Chain** | `hash_chain` im Manifest: `algorithm`, `head` (64-Zeichen-Hex), `path` (Datei unter `hashes/`), `covers` (v0.1 MUSS `manifest.json` und `objects/index.json` enthalten). Datei unter `hash_chain.path` existiert. |

*Diese Tabelle fasst die Integritätsgarantien zusammen, die der [Validator](../../validator/) für v0.1-Bundles prüft. Custody (Speicherung, Zugriffskontrolle, Retention) ist implementierungsdefiniert.*

---

## Coverage Map (YAML) vs. Profile (JSON)

| Artefakt | Status | Zweck |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` o. ä.) | **Informativ** | Übergeordnete Zuordnungsthemen zwischen AIMO-Evidence/Artefakten und externen Frameworks (ISO 42001, NIST AI RMF, EU AI Act usw.) zur Erklärbarkeit. Er legt keine normativen Validierungsanforderungen fest. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normativ** | Konversionsspezifikationen, validiert gegen `schemas/jsonschema/aimo-profile.schema.json`. Sie definieren maschinenlesbare Zuordnungen (z. B. welche AIMO-Objekte welchen Framework-Klauseln zugeordnet sind). Der [Validator](../../validator/) führt `--validate-profiles` aus, um sicherzustellen, dass alle offiziellen Profil-JSONs dem Schema entsprechen (profile_id PR-*-Muster, target-Enum, target_version, mappings). |

### Offizielle Profile (validator-validiert)

Profil-JSONs liegen in `coverage_map/profiles/` und werden vom Validator (`--validate-profiles`) validiert. Benennung: Dateiname `<target>_<purpose>.json`; jede enthält `target_version`.

| Datei | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### Profil-Aktualisierungspolitik

- **EU AI Act-Refs (0.1.2)**: Die Artikelreferenzen für den EU AI Act in der Coverage Map und in den Docs wurden an die Verordnung (EU) 2024/1689 für konsistente Evidence-Bereitschaft angeglichen; nur informativ, keine Rechtsberatung.
- **ISO 42001 / NIST AI RMF**: Neue Versionen des Ziel-Frameworks können in einer zukünftigen Standardversion als neue Profildateien oder neue `target_version`-Werte hinzugefügt werden; v0.1-Profile bleiben für das v0.1-Release eingefroren.
- **EU AI Act Annex IV**: Annex IV und zugehörige Artikel können von Aufsichtsbehörden aktualisiert werden; Profilzuordnungen können per **PATCH** (z. B. 0.1.x) an Formulierungs- oder Klauseländerungen angepasst werden, unter Beibehaltung derselben profile_id zur Kontinuität. Implementierer sollten sich an die in der `target_version` des Profils und den Release Notes referenzierte Version halten.

---

## Siehe auch

- [Evidence Bundle (Artefaktübersicht)](../evidence-bundle/)
- [Evidence Bundle Root-Struktur (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Mindestanforderungen an Evidence](../minimum-evidence/)
- [Coverage Map (Framework-Zuordnungen)](../../coverage-map/)
- [Validator](../../validator/)
