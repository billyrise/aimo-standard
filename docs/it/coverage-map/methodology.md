---
description: Metodologia della Mappa di Copertura - Come AIMO si mappa ai framework esterni. Utilizzo negli audit, relazione con l'Evidence Bundle e approccio alla tracciabilità.
---
<!-- aimo:translation_status=translated -->

# Metodologia

> Nota: Questa metodologia supporta la tracciabilità e la prontezza dell'evidence. Non garantisce la conformità con alcuna specifica normativa/standard.

Questa pagina spiega cosa è e cosa non è la Mappa di Copertura, come usarla nell'audit e come si relaziona con l'Evidence Bundle e i Requisiti Minimi di Evidence.

## Cosa è la mappatura

- Una mappatura **informativa** dai riferimenti di framework/normative esterne (per argomento) verso evidence AIMO, elementi TOC dell'Evidence Bundle, gruppi del ciclo di vita dei Requisiti Minimi di Evidence, artefatti e controlli del validator.
- Uno strumento di supporto per la **spiegabilità**: quale evidence e artefatti AIMO possono aiutare a dimostrare o spiegare l'allineamento con un dato requisito esterno (senza dichiarare conformità).

## Cosa non è la mappatura

- **Non** è una garanzia di conformità con alcun framework o normativa.
- **Non** è consulenza legale o un sostituto della verifica contro i testi autorevoli.
- **Non** è esaustiva; è un sottoinsieme pratico per la prontezza all'audit e la spiegabilità.

## Come usarla nell'audit

Usare il flusso: **requisito → evidence → artefatto → validazione**.

1. **Requisito**: Identificare il riferimento del framework esterno e l'argomento (es. documentazione ISO 42001, conservazione dei registri EU AI Act).
2. **Evidence**: Vedere quali elementi dell'Evidence Bundle AIMO e gruppi del ciclo di vita dei Requisiti Minimi di Evidence (richiesta, revisione, eccezione, rinnovo, change_log, integrità) supportano la spiegabilità per quel requisito.
3. **Artefatto**: Localizzare gli artefatti (schemi, template, esempi) che implementano o illustrano quell'evidence.
4. **Validazione**: Usare il validator e i controlli di schema referenziati per verificare la coerenza strutturale.

I lettori devono verificare contro il testo autorevole di ogni framework o normativa.

## Relazione con Evidence Bundle e Requisiti Minimi di Evidence

- **[Evidence Bundle](../../artifacts/evidence-bundle/)**: Definisce la struttura del bundle, il TOC e la tracciabilità. Le righe della Mappa di Copertura referenziano le sezioni dell'Evidence Bundle (es. EV, Dizionario, Riepilogo, change_log, richiesta, revisione, eccezione, rinnovo).
- **[Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/)**: Definisce i gruppi del ciclo di vita MUST-level (richiesta, revisione, eccezione, rinnovo, change_log, integrità). Le righe della Mappa di Copertura referenziano questi gruppi in `minimum_evidence_refs`.

Usare la Mappa di Copertura per vedere quali elementi dell'Evidence Bundle e gruppi dei Requisiti Minimi supportano la spiegabilità per un dato requisito esterno.

## Dichiarazione di non sovra-dichiarazione

!!! warning "Importante"
    Lo Standard AIMO supporta **spiegabilità e prontezza dell'evidence**. **Non** fornisce consulenza legale, garantisce conformità o certifica la conformità a qualsiasi normativa o framework. Gli adottanti devono verificare le dichiarazioni contro i testi autorevoli e ottenere consulenza professionale quando appropriato.

Vedere [Confini di Responsabilità](../../governance/responsibility-boundary/) per ambito, assunzioni e responsabilità degli adottanti.

## Percorso di audit

Da questa pagina, continuare verso:

1. **Mappature framework**: [ISO 42001](../iso-42001/), [NIST AI RMF](../nist-ai-rmf/), [EU AI Act](../eu-ai-act/), [ISMS](../isms/)
2. **Validazione**: [Validator](../../validator/) — eseguire controlli strutturali
3. **Download**: [Release](../../releases/) — ottenere gli asset di release
