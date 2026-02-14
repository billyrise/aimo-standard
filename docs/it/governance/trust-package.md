---
description: Trust Package AIMO - Bundle di materiali pronti per l'auditor. Documentazione minima per auditor, legale e sicurezza IT per valutare la prontezza all'adozione della governance dell'IA.
---

# Trust Package (Pacchetto di Assicurazione)

Questa pagina raggruppa i materiali minimi necessari ad auditor, legale e sicurezza IT per valutare la prontezza all'adozione.
È solo un hub; il TOC dettagliato dell'Evidence e le tabelle di Coverage sono mantenuti nelle rispettive sezioni.

## Download

**[Scarica Trust Package PDF (Ultima Release)](https://github.com/billyrise/aimo-standard/releases/latest)**

Il Trust Package PDF consolida i materiali pronti per l'auditor in un singolo documento. Ogni Release GitHub include:

- `trust_package.pdf` — Trust Package inglese
- `trust_package.ja.pdf` — Trust Package giapponese
- `aimo-standard-artifacts.zip` — Schemi, template, esempi, regole del validator
- `SHA256SUMS.txt` — Checksum per la verifica

## Cosa ottieni

- **Conformità**: come dichiarare la conformità e cosa significano i livelli — [Conformità](../../conformance/)
- **Mappa di Copertura**: mappatura verso standard esterni — [Indice Mappa di Copertura](../../coverage-map/), [Metodologia Mappa di Copertura](../../coverage-map/methodology/)
- **Standard**: requisiti e definizioni normative — [Standard (Corrente)](../../standard/current/)
- **Tassonomia**: sistema di classificazione a 8 dimensioni per la governance dell'IA — [Tassonomia](../../standard/current/03-taxonomy/), [Codici](../../standard/current/04-codes/), [Dizionario](../../standard/current/05-dictionary/)
- **Evidence Bundle**: struttura, TOC, tracciabilità — [Evidence Bundle](../../artifacts/evidence-bundle/)
- **Requisiti Minimi di Evidence**: checklist MUST-level per ciclo di vita — [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/)
- **Validator**: regole e controlli di riferimento — [Validator](../../validator/)
- **Esempi**: bundle di esempio pronti per l'audit — [Esempi](../../examples/)
- **Release**: cronologia delle modifiche e distribuzione — [Release](../../releases/)
- **Governance**: politiche, sicurezza, licenze — [Governance](../../governance/)

## Set minimo per la prontezza all'audit

| Elemento | Dove trovarlo | Risultato / cosa dimostra |
| --- | --- | --- |
| Livelli di conformità | [Conformità](../../conformance/) | Come dichiarare la conformità e l'ambito dell'evidence richiesta |
| Mappatura di copertura | [Indice Mappa di Copertura](../../coverage-map/), [Metodologia Mappa di Copertura](../../coverage-map/methodology/) | Spiegabilità verso normative e standard esterni |
| Tassonomia & Dizionario | [Tassonomia](../../standard/current/03-taxonomy/), [Codici](../../standard/current/04-codes/), [Dizionario](../../standard/current/05-dictionary/) | Sistema di classificazione per i sistemi IA (8 dimensioni, 91 codici) |
| Artefatti di evidence | [Evidence Bundle](../../artifacts/evidence-bundle/), [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/), [Template EV](../../standard/current/06-ev-template/) | Quali dati devono esistere per supportare la tracciabilità |
| Controlli del validator | [Validator](../../validator/) | Come verificare la coerenza interna e la completezza |
| Bundle di esempio | [Esempi](../../examples/) | Come appare in pratica un pacchetto pronto per l'audit |
| Controllo delle modifiche | [Release](../../releases/), [Governance](../../governance/) | Come gli aggiornamenti sono gestiti e comunicati |
| Sicurezza / Licenza / Marchi | [Governance](../../governance/) | Postura legale e di sicurezza per le decisioni di adozione |

## Come citare

Usare il README del repository per la guida alle citazioni e il contesto; la governance punta alle politiche autorevoli.
Vedere [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) e [Governance](../../governance/).

## Contenuto dello zip degli artefatti

L'`aimo-standard-artifacts.zip` include:

- **Tassonomia (SSOT)**: `source_pack/03_taxonomy/` — Dictionary CSV (91 codici), YAML, code system
- **JSON Schemas**: `schemas/jsonschema/` — Schemi di validazione leggibili da macchina
- **Template**: `templates/ev/` — Template di record di evidence (JSON + Markdown)
- **Esempi**: `examples/` — Bundle di esempio minimi per un'adozione rapida
- **Mappa di Copertura**: `coverage_map/coverage_map.yaml` — Mappatura verso standard esterni
- **Regole del Validator**: `validator/rules/` — Definizioni delle regole di validazione
- **Documenti di governance**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, ecc.

## Confini di responsabilità

Lo Standard AIMO fornisce un formato di evidence strutturato e un framework di spiegabilità. **Non** fornisce consulenza legale, certificazione di conformità, valutazione del rischio o esecuzione di audit.

Per la definizione completa dell'ambito, le assunzioni e le responsabilità degli adottanti, vedere [Confini di Responsabilità](../responsibility-boundary/).

## Come preparare un pacchetto di submission

Seguire questi passaggi per preparare una submission pronta per l'audit:

1. **Generare l'Evidence Bundle**: Creare record EV, Dizionario, Riepilogo e Change Log secondo [Evidence Bundle](../../artifacts/evidence-bundle/) e [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/).
2. **Eseguire il Validator**: Eseguire `python validator/src/validate.py bundle/root.json` per controllare la coerenza strutturale. Correggere eventuali errori prima di procedere.
3. **Creare i Checksum**: Generare checksum SHA-256 per tutti i file della submission:

    === "Linux"

        ```bash
        sha256sum *.json *.pdf > SHA256SUMS.txt
        ```

    === "macOS"

        ```bash
        shasum -a 256 *.json *.pdf > SHA256SUMS.txt
        ```

    === "Windows (PowerShell)"

        ```powershell
        Get-ChildItem *.json, *.pdf | ForEach-Object {
            $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
            "$hash  $($_.Name)"
        } | Out-File SHA256SUMS.txt -Encoding UTF8
        ```
4. **Impacchettare gli Artefatti**: Creare un archivio zip della directory dell'evidence bundle:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Referenziare la Versione di Release**: Annotare quale versione dello Standard AIMO (es. `v1.0.0`) il bundle è allineato.
6. **Consegnare**: Fornire lo zip, i checksum e il riferimento alla versione al proprio auditor o funzione di conformità.

Per gli asset di release e la verifica, vedere [Release](../../releases/).

## Dichiarazione di non sovra-dichiarazione

!!! warning "Importante"
    Lo Standard AIMO supporta **spiegabilità e prontezza dell'evidence**. **Non** fornisce consulenza legale, garantisce conformità o certifica la conformità a qualsiasi normativa o framework. Gli adottanti devono verificare le dichiarazioni contro i testi autorevoli e ottenere consulenza professionale quando appropriato.

Vedere [Confini di Responsabilità](../responsibility-boundary/) per dettagli su ambito, assunzioni e responsabilità degli adottanti.

## Per gli auditor: Procedura di verifica

Quando si riceve una submission di evidence, gli auditor dovrebbero verificare l'integrità e la struttura usando i seguenti passaggi:

!!! success "Build Provenance Disponibile"
    Tutti gli asset di release includono attestazioni di build firmate crittograficamente. Vedere [Procedura di Verifica](../../standard/versions/#4-verify-build-provenance-attestation) per i passaggi di verifica delle attestazioni.

### Passaggio 1: Verificare i checksum (SHA-256)

=== "Linux"

    ```bash
    # Scaricare o ricevere SHA256SUMS.txt con la submission
    # Verificare che tutti i file corrispondano ai checksum registrati
    sha256sum -c SHA256SUMS.txt

    # O verificare singoli file manualmente:
    sha256sum evidence_bundle.zip
    # Confrontare l'output con il valore in SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Verificare che tutti i file corrispondano ai checksum registrati
    shasum -a 256 -c SHA256SUMS.txt

    # O verificare singoli file manualmente:
    shasum -a 256 evidence_bundle.zip
    # Confrontare l'output con il valore in SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verificare singoli file
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Confrontare l'output Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

Se qualsiasi checksum fallisce, la submission dovrebbe essere rifiutata o ri-richiesta.

### Passaggio 2: Verificare la struttura del bundle (Validator)

**Prerequisiti** (setup una tantum):

```bash
# Clonare la release ufficiale dello Standard AIMO
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# IMPORTANTE: Usare la versione esatta indicata nella submission
# Sostituire VERSION con la versione dichiarata dal mittente (es. v0.0.1)
VERSION=v0.0.1  # ← Corrispondere alla versione nella submission
git checkout "$VERSION"

# Configurare l'ambiente Python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Corrispondenza Versione"
    Usare sempre la versione esatta dello Standard AIMO indicata nella submission. Usare una versione diversa può causare discrepanze nella validazione a causa di modifiche allo schema o alle regole tra le versioni.

**Eseguire la validazione**:

```bash
# Estrarre il bundle inviato
unzip evidence_bundle.zip -d bundle/

# Eseguire il validator contro il root.json del bundle
python validator/src/validate.py bundle/root.json

# Output atteso: "validation OK" o lista di errori
```

**Esempio** (usando il campione integrato):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

Il validator controlla:

- I file richiesti esistono (record EV, Dizionario)
- I file JSON sono conformi allo schema
- I riferimenti incrociati (request_id, review_id, ecc.) sono validi
- I timestamp sono presenti e formattati correttamente

### Passaggio 3: Verificare l'allineamento della versione

Controllare che la submission referenzi una release ufficiale dello Standard AIMO:

1. Confermare che la versione indicata (es. `v0.0.1`) esista su [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)
2. Confrontare gli schemi inviati con gli artefatti della release
3. Annotare eventuali deviazioni dalla release ufficiale

### Cosa cercare

| Controllo | Criteri di Successo | Azione in Caso di Fallimento |
| --- | --- | --- |
| Checksum corrispondono | Tutti i controlli `sha256sum -c` passano | Rifiutare o ri-richiedere |
| Validator passa | Nessun errore da `validate.py` | Richiedere correzioni prima dell'accettazione |
| Versione esiste | Il tag di release esiste su GitHub | Chiarire l'allineamento della versione |
| Campi richiesti presenti | I record EV hanno id, timestamp, source, summary | Richiedere completamento |
| Tracciabilità intatta | I riferimenti incrociati si risolvono correttamente | Richiedere correzioni ai collegamenti |

!!! info "Indipendenza dell'auditor"
    Gli auditor dovrebbero ottenere il validator e gli schemi direttamente dalla release ufficiale dello Standard AIMO, non dalla parte che invia, per assicurare l'indipendenza della verifica.

## Percorso di audit

Da questa pagina, il percorso di audit raccomandato è:

1. **Sistema di classificazione**: [Tassonomia](../../standard/current/03-taxonomy/) + [Dizionario](../../standard/current/05-dictionary/) — comprendere il sistema di codici a 8 dimensioni
2. **Struttura dell'evidence**: [Evidence Bundle](../../artifacts/evidence-bundle/) — comprendere il TOC del bundle e la tracciabilità
3. **Evidence richiesta**: [Requisiti Minimi di Evidence](../../artifacts/minimum-evidence/) — checklist MUST-level per ciclo di vita
4. **Allineamento ai framework**: [Mappa di Copertura](../../coverage-map/) + [Metodologia](../../coverage-map/methodology/) — vedere come AIMO si mappa ai framework esterni
5. **Validazione**: [Validator](../../validator/) — eseguire controlli di coerenza strutturale
6. **Download**: [Release](../../releases/) — ottenere gli asset di release e verificare i checksum
