---
description: Livelli di conformità dello Standard AIMO. Come le organizzazioni dichiarano la conformità, requisiti di evidence e cosa significa ogni livello per la governance dell'IA.
---
<!-- aimo:translation_status=translated -->

# Conformità

!!! warning "Importante: non certificazione, non assurance, non dichiarazione di conformità legale"
    AIMO Standard definisce un **formato di impacchettamento e validazione delle evidence**. Non certifica la conformità a leggi o norme.
    Le opinioni di audit e di assurance restano responsabilità dei verificatori indipendenti e dell'organizzazione adottante.
    **Dichiarazione appropriata:** "Un Evidence Bundle è stato prodotto secondo AIMO Standard v0.1.2 e validato strutturalmente dal Validator AIMO."
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Dichiarazione inappropriata:** "Conforme alla Legge sull'IA dell'UE", "ISO 42001 certificato", "approvato dal governo".
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

Questi livelli sono **livelli interni di maturità delle evidence** per impacchettamento e tracciabilità. **Non** sono certificazione, **non** sono opinione di assurance né conformità legale o normativa.

!!! note "Alias del nome del livello"
    Il livello superiore è stato indicato informalmente come "Gold" in passato; il **nome ufficiale del livello è Audit-Ready**.

## Quadro di conformità AIMO (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Componente | Descrizione | Aspettative di evidence |
| --- | --- | --- |
| **AIMO-MS** | Struttura orientata al sistema di gestione: politiche, ruoli, artefatti allineati PDCA che possono supportare controlli tipo ISO/IEC 42001. | Request, review, exception, renewal, change log; Summary e Dictionary. |
| **AIMO-Controls** | Controlli del ciclo di vita e integrità: request→review→exception→renewal, hashing, firma (secondo [struttura Evidence Bundle](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing; registri del ciclo di vita. |
| **AIMO-Audit** | Preparazione al passaggio di audit: validatore superato, checksum, attestation opzionale e indice di handoff audit. | Output del validatore, bundle_id, identità del produttore, metadati firma opzionali e indice di handoff. |

Le aspettative di evidence sono descritte in [Requisiti Minimi di Evidence](../artifacts/minimum-evidence/) e [Evidence Bundle](../artifacts/evidence-bundle/).

## Livelli di conformità (solo AIMO)

### Livello 1 — Foundation

**Scopo:** Baseline rintracciabile. Insieme minimo per rendere il pacchetto identificabile, verificabile in integrità e controllato dal validatore.

### Livello 2 — Operational

**Scopo:** Evidence di controllo operativo. Si costruisce su Foundation con traccia del ciclo di vita e monitoraggio.

### Livello 3 — Audit-Ready

**Scopo:** Qualità del passaggio di audit. Attestation completa, riproducibilità e slot per formulari esterni.

## Evidence minima per livello (riepilogo)

| Livello | MUST (riepilogo) |
| --- | --- |
| **Foundation** | Struttura del pacchetto (manifest, object_index, payload_index); sha256 per oggetti referenziati; bundle_id, created_at, producer; esecuzione validatore + versione; baseline dizionario evidence; dichiarazione di accesso e conservazione. SHOULD: voce minima nel change log. |
| **Operational** | Tutti i MUST Foundation; traccia del ciclo di vita; ≥1 artefatto di monitoraggio; voci del change log referenziano oggetti impattati; dichiarazione esplicita del limite prova vs. assurance. |
| **Audit-Ready** | Tutti i MUST Operational; ≥1 firma sul manifest; TSA o "no TSA"; pacchetto di riproducibilità; Formulari esterni elencati e referenziati; dichiarazione di completezza limitata; indice di handoff audit. |

La **presenza** di almeno una firma (che abbia come target il manifest) è richiesta dalla [struttura Evidence Bundle](../../standard/current/09-evidence-bundle-structure/) normativa per tutti i pacchetti.

## Mappatura ISO/IEC 42001 (informativa)

Vedere [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) e [Toolkit di preparazione alla certificazione ISO 42001](../artifacts/iso-42001-certification-readiness-toolkit/) per i dettagli.

## Modelli di formulazione delle dichiarazioni (anti-sovraccertificazione)

Utilizzare solo dichiarazioni che descrivano accuratamente quanto effettuato. La certificazione e la conformità legale restano responsabilità degli adottanti e degli organismi accreditati.

**Accettabili (esempi):** "Siamo conformi AIMO (Livello 2) a AIMO Standard v0.1.2; ciò non implica certificazione ISO né conformità legale." / "Un Evidence Bundle è stato prodotto secondo AIMO Standard v0.1.2 e validato strutturalmente dal Validator AIMO."

**Inaccettabili (esempi):** "Conforme alla Legge sull'IA dell'UE" / "ISO 42001 certificato" / "Approvato dal governo" (AIMO non certifica conformità normativa; la certificazione è rilasciata dagli organismi accreditati.)

## Pagine correlate

- [Trust Package](../governance/trust-package/) — Punto di ingresso consolidato per i verificatori
- [Responsibility Boundary](../governance/responsibility-boundary/) — Cosa AIMO fornisce e non fornisce
- [Standard (Current)](../standard/current/) — Requisiti normativi
- [Artifacts](../artifacts/) — Struttura delle evidence e requisiti minimi
- [Validator](../validator/) — Validazione strutturale
