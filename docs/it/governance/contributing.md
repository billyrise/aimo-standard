---
description: Guida ai contributi dello Standard AIMO - Come contribuire codice, documentazione e traduzioni. Linee guida per issue e PR.
---

# Contribuire

Questa pagina fornisce linee guida per contribuire allo Standard AIMO.

## Avvio Rapido

1. Fare il fork del repository
2. Creare un branch per la feature
3. Apportare le modifiche seguendo le linee guida sotto
4. Eseguire i controlli di qualità
5. Inviare una pull request

## Principi Chiave

| Principio | Descrizione |
| --------- | ----------- |
| L'inglese è canonico | Modificare prima `docs/en/`, poi aggiornare `docs/ja/` |
| SSOT | Questo repository è la single source of truth |
| Nessuna modifica manuale ai file generati | Modificare le fonti, rigenerare, committare |
| Tutte le modifiche via PR | Anche i maintainer usano le pull request |

## Controlli di Qualità

Prima di inviare una PR, eseguire:

```bash
# Attivare l'ambiente virtuale
source .venv/bin/activate

# Eseguire i lint
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Buildare la documentazione
mkdocs build --strict
```

## Tipi di Modifiche

| Tipo | Esempi | Requisiti di Revisione |
| ---- | -------- | ------------------- |
| Normativo | Modifiche allo schema, requisiti | Maintainer + discussione |
| Non-normativo | Errori di battitura, chiarimenti | Approvazione maintainer |
| i18n | Traduzioni | La struttura deve corrispondere a EN |
| Tooling | CI/CD, script | Approvazione maintainer |

## Linee Guida i18n

### Ordine di Aggiornamento

1. Modificare la fonte inglese (`docs/en/...`)
2. Aggiornare la traduzione giapponese (`docs/ja/...`)
3. Eseguire `lint_i18n.py` per verificare la coerenza
4. Committare entrambe insieme

### Requisiti di Struttura

- Stessi nomi file in entrambe le lingue
- Stessa gerarchia di heading
- Stesso numero di pagine per sezione

## Checklist PR

Quando si invia una PR, verificare:

- [ ] Tipo di modifica identificato (docs / schema / examples / tooling)
- [ ] Valutazione delle modifiche breaking completata
- [ ] i18n: EN e JA aggiornati insieme (se applicabile)
- [ ] Controlli di qualità superati
- [ ] Issue correlate collegate

## Modifiche Breaking

Le modifiche breaking richiedono:

1. Discussione nell'issue prima dell'implementazione
2. Incremento di versione secondo [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Voce nel changelog con guida alla migrazione

## Aggiornamenti delle Dichiarazioni di Conformità

Per aggiungere o modificare dichiarazioni di conformità:

1. Aggiornare la coverage map YAML
2. Aggiornare le pagine di documentazione corrispondenti
3. Eseguire i test del validator
4. Documentare la motivazione della mappatura

## Linee Guida Complete

Vedere [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) per la guida a livello root.

## Pagine Correlate

- [Governance](index.md) — Governance del progetto
- [Guida alla Localizzazione](../contributing/localization.md) — Dettagli i18n
- [Confini di Responsabilità](responsibility-boundary.md) — Cosa fornisce AIMO
