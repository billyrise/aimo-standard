---
description: Hub del Validator AIMO - Quickstart del tooling di validazione. Installare, eseguire e interpretare i risultati in 30 secondi. Validazione dell'evidence pack e controlli di conformità.
---

# Validator

Questa pagina è un hub per il tooling di validazione e le regole. La specifica normativa per il validator e le sue regole è nello Standard.

## Quickstart (30 secondi)

**1. Prerequisiti**

```bash
pip install jsonschema   # se non già installato
```

**2. Eseguire la validazione contro un bundle di esempio**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Leggere il report e correggere errori/avvisi**

Esempio di output (successo):

```
OK
```

Esempio di output (fallimento):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Codici di uscita: `0` = successo, `1` = errori di validazione, `2` = errore d'uso.

---

## Cosa controlla

- **Validazione schema**: l'oggetto root, il dizionario e l'evidence sono conformi allo JSON Schema
- **Coerenza del dizionario**: tutti i codici esistono nel dizionario della tassonomia
- **Stato dei codici**: avvisa per codici deprecati, errore per codici rimossi

## Cosa NON controlla

- **Accuratezza del contenuto**: il validator controlla la struttura, non il significato
- **Garanzia di conformità**: passare la validazione non garantisce la conformità normativa
- **Giudizio umano**: le decisioni dipendenti dal contesto richiedono revisione umana (vedere [Protocollo di Supervisione Umana](../governance/human-oversight-protocol.md))
- **Raccolta automatica dei log**: il validator valida l'evidence presentata; non raccoglie log

---

## Risorse

- **Specifica**: [Standard > Corrente > Validator](../standard/current/07-validator.md) — regole, controlli di riferimento e come la validazione si relaziona all'evidence.
- **Regole e implementazione**: nel repository `validator/rules/` (controlli), `validator/src/` (implementazione di riferimento). Esecuzione e uso CI sono descritti nella specifica.
- **Interpretazione**: cosa significa un "fail" di validazione per gli auditor (spiegato nella specifica).

Per conformità e uso degli artefatti, vedere [Conformità](../conformance/index.md) e [Artefatti](../artifacts/index.md).
