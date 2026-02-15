---
description: Modello di mappa di copertura dell'Evidence Bundle (v0.1). Riepilogo informativo di una pagina per gli auditor — ambito, tipi di evidence, mappatura dei controlli, esclusioni, prova di integrità.
---
<!-- aimo:translation_status=translated -->

# Mappa di copertura dell'Evidence Bundle (Modello)

!!! info "Informativo — pratica raccomandata"
    Questa pagina definisce un **modello di pratica raccomandata** per una mappa di copertura dell'Evidence Bundle di una pagina. **Non** è un requisito normativo dello standard. Usatela per documentare cosa copre e non copre un bundle per il passaggio all'auditor. I riferimenti (es. ai framework) sono stabili; l'adozione è a discrezione dell'implementatore.

---

## 1. Ambito

| Elemento | Descrizione |
|------|--------------|
| **Riferimento di ambito** | `scope_ref` dal manifesto del bundle (es. `SC-001`). Collega questo bundle all'ambito dichiarato. |
| **ID del bundle** | `bundle_id` (UUID) — identificatore univoco di questo bundle. |
| **Versione del bundle** | `bundle_version` (SemVer) — versione del bundle. |
| **Periodo / snapshot** | Opzionale: periodo o data dello snapshot che questo bundle rappresenta (es. 2026-Q1, as-of 2026-02-03). |

---

## 2. Tipi di evidence (EV / objects vs payloads)

| Categoria | Contenuto | Esempio minimo v0.1 |
|----------|----------|------------------------|
| **object_index** | Oggetti enumerati (metadati, indici). Ogni voce: `id`, `type`, `path`, `sha256`. | es. `objects/index.json` (tipo index). |
| **payload_index** | File di payload (EV JSON radice, file Evidence Pack). Ogni voce: `logical_id`, `path`, `sha256`, `mime`, `size`. | es. `payloads/root.json` (EV JSON radice AIMO). |
| **Tipi EV** | Record di evidence (nella radice o payload collegati) — request, review, exception, renewal, change log. | Allineato al [modello Evidence Pack](../../standard/current/06-ev-template/) e ai [Requisiti minimi di evidence](../minimum-evidence/). |

*Gli implementatori possono estendere object_index e payload_index; i percorsi DEVONO rimanere entro la radice del bundle e soddisfare la [struttura radice dell'Evidence Bundle (v0.1)](../../standard/current/09-evidence-bundle-structure/).*

---

## 3. Mappatura dei controlli (solo riferimento)

La mappatura verso framework esterni è **solo di riferimento**; lo standard non impone conformità a nessuna regolamentazione specifica.

| Framework | Uso in questo bundle | Riferimento |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | Opzionale: documentare quali temi AI MS questo bundle supporta. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | Opzionale: allineamento documentazione/tenuta registri di alto livello. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | Opzionale: mappatura Govern, Map, Measure, Manage. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | Opzionale: Model Documentation Form; allegare in External Forms, referenziare per logical_id. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/); profilo `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | Opzionale: artefatti del profilo GenAI (AI 600-1). | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/); profilo `nist_ai_600_1_genai.json` |
| **UK ATRS** | Opzionale: registrazione ATRS, valutazione appalti. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); profilo `uk_atrs_procurement.json` |
| **JP Gov GenAI appalti** | Opzionale: lista di controllo appalti JP, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); profilo `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | Opzionale: gestione modifiche, accesso, registrazione, integrità. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*Compilare « Uso in questo bundle » per submission; lo standard non richiede alcuna copertura di controllo specifica.*

### External Forms e riferimento al manifesto

**External Forms** (modelli/liste di controllo ufficiali allegati così come sono) devono essere elencati nel **payload_index** del bundle con `logical_id`, `path`, `sha256`, `mime` e `size` stabili. Gli auditor possono quindi rintracciare dal manifesto al file e verificare l'hash. Vedere [Modello EV — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) e [Modello EV — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index).

---

## 4. Esclusioni / ipotesi

| Area | Cosa questo bundle **non** copre (righe di esempio — adattare per submission) |
|------|-------------------------------------------------------------------------------|
| **Esclusioni** | es. Sistemi o casi d'uso fuori ambito; componenti di terze parti non evidenziati; periodo fuori da questo bundle. |
| **Ipotesi** | es. Versione Dictionary/tassonomia; versione validatore/schema utilizzata; custodia e conservazione sono definite dall'implementazione. |
| **Limitazioni** | es. La verifica delle firme è fuori ambito in v0.1; nessuna interpretazione legale delle regolamentazioni. |

*Sostituire il testo placeholder con esclusioni e ipotesi specifiche della submission.*

---

## 5. Riepilogo della prova di integrità (v0.1)

| Elemento | Cosa è fornito (v0.1 normativo) |
|---------|----------------------------------|
| **manifest.json** | Presente e valido allo schema; include `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Ogni file in `object_index` e `payload_index` ha un sha256 hex minuscolo a 64 caratteri dichiarato; il validatore verifica la corrispondenza del contenuto. |
| **Esistenza dell'indice** | Tutti i percorsi elencati esistono sotto la radice del bundle; nessuna traversata di percorso (`../` o `/` iniziale). |
| **Esistenza della firma** | Almeno un file di firma in `signatures/`; il manifesto lo referenzia tramite `signing.signatures[]` con `path` e `targets` (v0.1 DEVE includere `manifest.json` in targets). La verifica crittografica è fuori ambito in v0.1. |
| **Catena di hash** | `hash_chain` nel manifesto: `algorithm`, `head` (64 caratteri hex), `path` (file sotto `hashes/`), `covers` (v0.1 DEVE includere `manifest.json` e `objects/index.json`). Il file in `hash_chain.path` esiste. |

*Questa tabella riassume le garanzie di integrità che il [Validator](../../validator/) verifica per i bundle v0.1. La custodia (archiviazione, controllo accessi, conservazione) è definita dall'implementazione.*

---

## Coverage Map (YAML) vs Profili (JSON)

| Artefatto | Stato | Scopo |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` o simile) | **Informativo** | Temi di mappatura di alto livello tra evidence/artefatti AIMO e framework esterni (ISO 42001, NIST AI RMF, EU AI Act, ecc.) per la spiegabilità. Non impone requisiti di validazione normativi. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normativo** | Specifiche di conversione validate rispetto a `schemas/jsonschema/aimo-profile.schema.json`. Definiscono mappature leggibili da macchina (es. quali oggetti AIMO mappano a quali clausole di framework). Il [Validator](../../validator/) esegue `--validate-profiles` per assicurare che tutti i profile JSON ufficiali conformino allo schema (pattern profile_id PR-*, enum target, target_version, mappings). |

### Profili ufficiali (validati dal validatore)

I Profile JSON si trovano in `coverage_map/profiles/` e sono validati dal validatore (`--validate-profiles`). Nomenclatura: nome file `<target>_<purpose>.json`; ciascuno include `target_version`.

| File | profile_id | target | target_version |
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

### Politica di aggiornamento dei profili

- **Refs EU AI Act (0.1.2)**: I riferimenti agli articoli dell'EU AI Act nella mappa di copertura e nella documentazione sono stati allineati al Regolamento (UE) 2024/1689 per una prontezza dell'evidence coerente; solo informativo, non parere legale.
- **ISO 42001 / NIST AI RMF**: Nuove versioni del framework target possono essere aggiunte come nuovi file di profilo o nuovi valori `target_version` in una versione futura dello standard; i profili v0.1 restano congelati per la release v0.1.
- **EU AI Act Annex IV**: L'Allegato IV e gli articoli correlati possono essere aggiornati dai regolatori; le mappature dei profili possono essere aggiornate tramite **PATCH** (es. 0.1.x) per seguire modifiche di formulazione o clausola mantenendo lo stesso profile_id per continuità. Gli implementatori devono allinearsi alla versione referenziata nella `target_version` del profilo e nelle note di release.

---

## Vedi anche

- [Evidence Bundle (panoramica artefatto)](../evidence-bundle/)
- [Struttura radice dell'Evidence Bundle (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Requisiti minimi di evidence](../minimum-evidence/)
- [Coverage Map (mappature di framework)](../../coverage-map/)
- [Validator](../../validator/)
