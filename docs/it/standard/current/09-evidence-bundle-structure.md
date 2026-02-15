---
description: Struttura radice normativa e manifest dell'Evidence Bundle (v0.1). Integrity MUST; Custody è definito dall'implementazione.
---
<!-- aimo:translation_status=translated -->

# Struttura radice dell'Evidence Bundle (v0.1)

Questa pagina definisce il **layout radice normativo** e il manifest di un Evidence Bundle. I validator DEVONO rifiutare i pacchetti che non soddisfano questi requisiti prima di qualsiasi validazione dello schema.

## MUST normativo v0.1 (riepilogo)

- **manifest.json** alla radice del pacchetto è obbligatorio.
- **object_index** e **payload_index**: ogni voce DEVE includere **sha256** (64 hex minuscole); i percorsi DEVONO essere relativi e NON DEVONO contenere `../` né uscire dalla radice del pacchetto.
- **signing.signatures** DEVE essere un array non vuoto (array vuoto non valido).
- Ogni voce di firma DEVE avere: **path** sotto `signatures/` (attraversamento percorso vietato), **targets** (array, almeno un percorso), e almeno una firma nel pacchetto DEVE elencare **manifest.json** in **targets** (firma del manifest obbligatoria).
- **hash_chain**: v0.1 DEVE includere **algorithm**, **head**, **path** (sotto `hashes/`) e **covers** con almeno **manifest.json** e **objects/index.json**.

I validator DEVONO far rispettare queste regole prima di accettare un pacchetto.

## Struttura radice richiesta (MUST)

Alla radice del pacchetto DEVONO essere presenti: **manifest.json**, **objects/**, **payloads/**, **signatures/**, **hashes/** (descriti nella norma). Gli implementatori NON DEVONO inviare un pacchetto che ometta uno di questi. Il Validator DEVE fallire con messaggio chiaro quando la struttura radice è incompleta.

## Integrity (normativo) vs. Custody (implementazione)

- **Integrity** è **normativo** in v0.1: la norma richiede che il pacchetto porti metadati di integrità (manifest, sha256 dei file indicizzati, presenza firma del manifest). I validator DEVONO verificare esistenza e validità del manifest, esistenza e corrispondenza sha256 dei file indicizzati e presenza di almeno una firma che abbia come target il manifest.
- **Custody** (archiviazione, controllo accessi, conservazione, WORM) è **definito dall'implementazione**.

## manifest.json (campi MUST)

Il manifest DEVE includere almeno: **bundle_id** (UUID), **bundle_version** (SemVer), **created_at** (date-time), **scope_ref** (pattern SC-*), **object_index**, **payload_index**, **hash_chain**, **signing**. Regole percorso: relativi, senza `../`, senza `/` iniziale, entro la radice dell'Evidence Bundle.

**Metadati firma opzionali v0.1.1 (RECOMMENDED per riesecuzione da terzi):** signer_identity, signed_at, verification_command, canonicalization.

## Estensioni future (informativo)

- **Collegamento Control/Requirement**: Una versione futura potrebbe aggiungere un modo standard per collegare gli elementi dell'Evidence Bundle agli identificatori Control o Requirement (es. per export verso NIST OSCAL).

## Riferimenti

- [Evidence Bundle (panoramica artefatto)](../../../artifacts/evidence-bundle/) — scopo e indice
- [Modello EV — Formulari esterni e indice handoff audit](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is)
- [Roadmap verifica firme](../../../artifacts/signature-verification-roadmap/) — metadati v0.1.1 e piano di verifica v0.2
- [Validator](../../../validator/) — come il validator applica questa struttura
- [Requisiti Minimi di Evidence](../../../artifacts/minimum-evidence/) — elenco di controllo MUST
