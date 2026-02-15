---
description: Politica di sicurezza dello Standard AIMO - Segnalazione vulnerabilità, procedure di disclosure e considerazioni sulla sicurezza per le implementazioni di governance dell'IA.
---

# Sicurezza

Questa pagina documenta la politica di sicurezza per lo Standard AIMO, incluse la segnalazione delle vulnerabilità e le procedure di disclosure.

## Ambito

### In Ambito

- Implementazione di riferimento del Validator (`validator/`)
- Tooling di build e release (`tooling/`)
- JSON schemas (`schemas/`)
- Infrastruttura del sito di documentazione

### Fuori Ambito

- Contenuto della specifica (il testo normativo non è un artefatto di sicurezza)
- Implementazioni degli adottanti che usano lo Standard AIMO
- Dipendenze esterne (segnalare ai maintainer upstream)

## Versioni Supportate

| Versione | Supportata |
| ------- | --------- |
| latest (dev) | Sì |
| Release taggate (vX.Y.Z) | Sì (ultime 2 versioni minor) |
| Release più vecchie | No (upgrade raccomandato) |

## Segnalare una Vulnerabilità

**Non** aprire una issue pubblica su GitHub per vulnerabilità di sicurezza.

### Processo

1. Segnalare privatamente tramite la segnalazione privata delle vulnerabilità di GitHub
2. Includere: descrizione, passaggi per riprodurre, versioni interessate, impatto
3. Attendere il tempo per la valutazione e lo sviluppo della fix

### Tempistiche

| Fase | Tempistica |
| ----- | -------- |
| Riconoscimento | 72 ore |
| Valutazione iniziale | 7 giorni |
| Disclosure coordinata | Max 90 giorni |

## Politica di Disclosure

1. Le vulnerabilità vengono segnalate privatamente
2. Le fix vengono sviluppate prima della disclosure pubblica
3. Gli advisory di sicurezza vengono pubblicati dopo che le fix sono disponibili
4. I segnalatori vengono accreditati (a meno che non sia richiesto l'anonimato)

## Misure di Sicurezza

- Controlli CI/CD su tutte le modifiche
- Release firmate con checksum SHA-256
- Revisione PR obbligatoria prima del merge

## Politica Completa

Vedere [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) per la politica di sicurezza completa.

## Pagine Correlate

- [Trust Package](trust-package.md) — Materiali pronti per l'auditor
- [Governance](index.md) — Governance del progetto
