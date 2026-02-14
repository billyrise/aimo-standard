---
description: Changelog e politica di versionamento dello Standard AIMO. Documenta la cronologia delle versioni, le regole di semantic versioning e la guida alla migrazione tra release.
---

# Changelog

Questa sezione documenta la politica di versionamento e la cronologia delle modifiche per lo Standard AIMO.

## Politica di Versionamento

Lo Standard AIMO segue [Semantic Versioning](https://semver.org/) (SemVer):

### Formato Versione: MAJOR.MINOR.PATCH

| Tipo di Modifica | Incremento Versione | Esempi |
| --- | --- | --- |
| **MAJOR** | X.0.0 | Modifiche breaking allo schema, rimozione codici, modifiche ai campi richiesti |
| **MINOR** | 0.X.0 | Nuovi codici, nuovi campi opzionali, nuove dimensioni (opzionali) |
| **PATCH** | 0.0.X | Fix alla documentazione, chiarimenti alle definizioni, bug fix del validator |

### Modifiche Breaking vs. Compatibili

**Modifiche Breaking (MAJOR):**

- Rimozione di codici (dopo il periodo di deprecazione)
- Modifiche ai campi richiesti negli schemi
- Modifiche strutturali che invalidano documenti esistenti
- Modifiche ai pattern di formato dei codici

**Modifiche Retrocompatibili (MINOR):**

- Aggiunta di nuovi codici a dimensioni esistenti
- Aggiunta di nuovi campi opzionali agli schemi
- Aggiunta di nuove dimensioni opzionali
- Aggiunta di nuovi template di evidence

**Modifiche Non-breaking (PATCH):**

- Correzioni alla documentazione
- Chiarimento di definizioni esistenti
- Miglioramenti alle traduzioni
- Bug fix del validator

## Politica di Deprecazione

### Processo di Deprecazione

1. **Marcare come Deprecato**: Il codice o la feature è marcata con `status: deprecated` e `deprecated_in: X.Y.Z`
2. **Periodo di Deprecazione**: Deve passare almeno una versione MINOR prima della rimozione
3. **Fornire Sostituzione**: Se applicabile, `replaced_by` indica la sostituzione
4. **Rimuovere in MAJOR**: La rimozione avviene nella prossima versione MAJOR

### Esempio di Ciclo di Vita

```
v0.0.1: FS-007 introdotto (status: active)
v0.1.0: FS-007 deprecato (status: deprecated, replaced_by: FS-008)
v0.2.0: FS-007 ancora disponibile con avviso di deprecazione
v1.0.0: FS-007 rimosso (status: removed)
```

### Usare Codici Deprecati

- I codici deprecati rimangono validi per la validazione
- Il validator DOVREBBE emettere un avviso per i codici deprecati
- Le nuove implementazioni DOVREBBERO usare i codici di sostituzione
- I documenti esistenti POSSONO continuare a usare codici deprecati fino alla migrazione

## Artefatti di Release

Ogni release ufficiale include:

| Artefatto | Descrizione |
| --- | --- |
| Snapshot del sito versionato | `https://standard.aimoaas.com/0.0.1/` |
| Specifica PDF | `trust_package.pdf` |
| Pacchetto asset (ZIP) | Schemi, template, dizionario |
| Checksum | Hash SHA-256 per l'integrità |
| Changelog | Questo documento |

## Cronologia delle Modifiche

### Non rilasciato (correzioni namespace e normativa)

**Riepilogo:** Risoluzione collisione codici EV, chiarimento EV (indice) vs Evidence Pack (payload), hardening /dev contro citazione errata in audit. Tipi di documento Evidence Pack: EP-01..EP-07; Taxonomy EV resta per tipi di evento. Relazione normativa EV↔Evidence Pack documentata. Banner e canonical per /dev.

### Versione 0.0.1 (2026-02-02)

**Riepilogo:** Release iniziale dello Standard AIMO con code system a 8 dimensioni, template Evidence Pack e documentazione di governance completa.

#### Aggiunto

**Code System (8 Dimensioni)**

| Dimensione | Codici Aggiunti | Descrizione |
| --- | --- | --- |
| FS | FS-001 a FS-006 | Functional Scope |
| UC | UC-001 a UC-010 | Use Case Class |
| DT | DT-001 a DT-008 | Data Type |
| CH | CH-001 a CH-006 | Channel |
| IM | IM-001 a IM-005 | Integration Mode |
| RS | RS-001 a RS-005 | Risk Surface |
| OB | OB-001 a OB-005 | Outcome / Benefit |
| LG | LG-001 a LG-015 | Log/Event Type |

**Schemi**

- `taxonomy_pack.schema.json`: Definizione taxonomy pack
- `changelog.schema.json`: Voci del changelog
- `evidence_pack_manifest.schema.json`: Manifest Evidence Pack
- `shadow-ai-discovery.schema.json`: Evidence scoperta Shadow AI
- `agent-activity.schema.json`: Evidence attività agent

**Template Evidence Pack (MVP)**

- EV-01: Panoramica del Sistema
- EV-02: Flusso dei Dati
- EV-03: Inventario IA
- EV-04: Valutazione Rischi & Impatto
- EV-05: Controlli & Approvazioni
- EV-06: Logging & Monitoraggio
- EV-07: Gestione Incidenti & Eccezioni

**Documentazione**

- Documentazione della tassonomia con definizioni a 8 dimensioni
- Specifica del formato Code System
- Specifica del formato CSV del dizionario
- Politica di versionamento e modifiche
- Requisiti MVP del validator
- Protocollo di Supervisione Umana
- Coverage Map (ISO 42001, NIST AI RMF, EU AI Act, ISMS)
- Trust Package

#### Retrocompatibilità

Questa è la release iniziale; nessuna preoccupazione di retrocompatibilità.

---

## Changelog Leggibile da Macchina

Un changelog leggibile da macchina è disponibile:

- `changelog/changelog.json`

Questo file segue lo schema `changelog.schema.json` e può essere parsato programmaticamente.

## Riferimenti

- [Tassonomia](../03-taxonomy/) - Definizioni delle dimensioni
- [Dizionario](../05-dictionary/) - Dizionario dei codici
- [Politica di Versionamento](../../../governance/) - Politica di versionamento (vedere VERSIONING.md nella root del repository)
