---
description: Mappatura dello Standard AIMO verso la Legge sull'IA dell'UE. Tracciabilità tra codici della tassonomia AIMO e categorie di rischio e requisiti della Legge sull'IA dell'UE.
---
<!-- aimo:translation_status=translated -->

# Mappatura Legge sull'IA dell'UE

> Scorciatoie di tracciabilità: Tassonomia → Requisiti Minimi di Evidence → Validator → Protocollo di Supervisione Umana.

- [Tassonomia](../../standard/current/03-taxonomy/)
- [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/)
- [Schemi Log](../../artifacts/log-schemas/)
- [Validator](../../validator/)
- [Protocollo di Supervisione Umana](../../governance/human-oversight-protocol/)

Questa pagina mappa temi selezionati della Legge sull'IA dell'UE (documentazione, tenuta dei registri, gestione del rischio, supervisione umana, trasparenza) verso evidence e artefatti AIMO. È solo di alto livello e **non** costituisce parere legale né garanzia di conformità. Verificare contro il testo legale ufficiale.

**Riferimento:** Regolamento (UE) 2024/1689 (Legge sull'intelligenza artificiale). Tutti i numeri di articolo seguenti si riferiscono a tale regolamento.

## Tabella di mappatura

| Riferimento quadro / tema | Evidence AIMO / dove in AIMO | Evidence Bundle / Requisiti Minimi | Artefatti e validazione | Note |
| --- | --- | --- | --- | --- |
| Art. 4 – Alfabetizzazione IA | [Ambito](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Trasversale; evidence di capacità/formazione organizzativa (alto livello). Non parere legale. Verificare contro testo ufficiale. |
| Art. 9 – Sistema di gestione del rischio | [Ambito](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | Sistemi di IA ad alto rischio (Titolo III). Non parere legale. Verificare contro testo ufficiale. |
| Art. 10 – Dati e governance dei dati | [Dizionario](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Non parere legale. Verificare contro testo ufficiale. |
| Art. 11 – Documentazione tecnica (alto rischio) | [Modello EV](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Allegato IV**: [Esempi > Campione Allegato IV UE](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); profilo: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Pacchetto di esempio conforme. Vedi Esempi (ulteriore contenuto in versione futura). | Solo alto livello; non parere legale. Verificare contro testo ufficiale. |
| Art. 12 – Tenuta dei registri | [Evidence Bundle](../../artifacts/evidence-bundle/), [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Non parere legale. Verificare contro testo ufficiale. |
| Art. 13 – Trasparenza e informazioni a implementatori/utenti | [Ambito](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Contesto ad alto rischio. Non parere legale. Verificare contro testo ufficiale. |
| Art. 14 – Supervisione umana | [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | Non parere legale. Verificare contro testo ufficiale. |
| Art. 15 – Accuratezza, robustezza, cybersecurity | [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) | EV (codici evidence/rischio, alto livello) | templates/ev/ | Solo mappatura di alto livello. Non parere legale. Verificare contro testo ufficiale. |
| Art. 17 – Sistema di gestione della qualità | [Ambito](../../standard/current/02-scope/) | Summary, review (processo organizzativo) | templates/ev/ | Distinto dall'art. 9 (sistema di gestione del rischio). Non parere legale. Verificare contro testo ufficiale. |
| Obblighi di trasparenza (dipendenti dal caso d'uso) | [Ambito](../../standard/current/02-scope/), [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | Le disposizioni applicabili dipendono dal caso d'uso. Non parere legale. Verificare contro testo ufficiale. |
| Obblighi dei modelli GPAI | [Modello EV](../../standard/current/06-ev-template/), [Evidence Bundle](../../artifacts/evidence-bundle/) | Modello EV, Evidence Bundle (struttura evidence) | schemas/jsonschema/; schema_validate_ev | AIMO fornisce un quadro per organizzare le evidence; gli obblighi effettivi sono definiti dal regolamento. Non parere legale. Verificare contro testo ufficiale. |
| Considerando – Responsabilità | [Evidence Bundle](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Non parere legale. Verificare contro testo ufficiale. |

## Date di applicazione / applicabilità (alto livello)

Quanto segue si allinea al **calendario ufficiale UE** (Servizio Legge sull'IA / Commissione). **Non è parere legale** e non garantisce accuratezza. Confermare sempre con il **testo legale ufficiale** e le autorità competenti.

| Fase | Data | Cosa si applica (alto livello) |
| --- | --- | --- |
| Entrata in vigore | Agosto 2024 | Regolamento in vigore; la maggior parte degli obblighi sostanziali non ancora applicabili. |
| Disposizioni generali e divieti | 02 feb 2025 | Pratiche vietate (rischio inaccettabile); determinate disposizioni sull'alfabetizzazione IA. |
| Regole GPAI e governance | 02 ago 2025 | Regole su organismi notificati, GPAI, governance, riservatezza, sanzioni; codici di condotta. |
| Regole principali + Allegato III alto rischio + Art. 50 trasparenza | 02 ago 2026 | Piena applicabilità per sistemi di IA ad alto rischio (Allegato III), obblighi di trasparenza art. 50. |
| Alto rischio incorporato in prodotti regolamentati | 02 ago 2027 | Sistemi di IA ad alto rischio incorporati in prodotti soggetti alla legislazione UE sui prodotti. |

## Norme armonizzate e presunzione di conformità (art. 40)

Quando le **norme armonizzate** sono pubblicate nella Gazzetta ufficiale dell'UE ai sensi della Legge sull'IA, la conformità ad esse può fornire **presunzione di conformità** ai requisiti corrispondenti. L'elenco e le date esatte dipendono dai lavori di normazione e dalla pubblicazione nella GU. Le mappature AIMO sono informative e non conferiscono presunzione di conformità. Per lo stato attuale, vedere le fonti della Commissione e dell'Ufficio IA in **Riferimenti** sotto.

## Linee guida 2026 dell'Ufficio IA (dettaglio di attuazione)

La Commissione europea ha indicato che l'**Ufficio IA** preparerà **linee guida pratiche** nel 2026, tra l'altro su: classificazione ad alto rischio; attuazione art. 50 (trasparenza); segnalazione di incidenti; elementi correlati al QMS. Queste linee guida sono **trigger di aggiornamento** per i profili e le mappature di copertura AIMO: una volta pubblicate, gli adottanti devono allineare evidence e mappature con l'ultima guida ufficiale. AIMO non interpreta né garantisce conformità a tali linee guida.

!!! warning "Non parere legale"
    Questa pagina è solo a scopo esplicativo. È necessario verificare l'applicabilità e le date rispetto al regolamento ufficiale e a eventuali atti di esecuzione o di modifica. AIMO non fornisce parere legale né garantisce conformità.

## Riferimenti

- [Regolamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex) — Legge sull'intelligenza artificiale
- [Calendario di attuazione della Legge sull'IA dell'UE](https://artificialintelligenceact.eu/implementation-timeline) (Servizio Legge sull'IA / allineato Commissione; informativo)
- Commissione europea / Ufficio IA — linee guida e calendario (verificare notizie Commissione e Servizio Legge sull'IA per URL attuali)
- [EPRS — Attuazione Legge sull'IA dell'UE](https://www.europarl.europa.eu/thinktank/) — briefing del Parlamento (informativo)
