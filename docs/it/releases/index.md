---
description: Release dello Standard AIMO - Download di PDF versionati, artefatti e checksum. Changelog, guide alla migrazione e attestazioni di build provenance.
---

# Release

Questa sezione è un hub per le release versionati, changelog, migrazione e artefatti di distribuzione.

## Scarica l'Ultima Release

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — è la fonte unica di verità del release "latest". Il percorso del sito `/latest/` reindirizza alla stessa versione.

## Procedura di verifica (pagina permanente)

La **procedura di verifica** completa (download degli asset, verifica dei checksum, attestazione di provenienza) è disponibile come pagina permanente, non solo in PDF:

- **[Standard → Versioni → Procedura di Verifica](../standard/versions/)** — verifica passo-passo dei checksum (Linux/macOS/Windows) e attestazione di provenienza.

Utilizzare questa pagina quando è necessario verificare gli asset di release o documentare i passaggi di verifica nei deliverable di audit.

## Asset di Release

Ogni release ufficiale (tag `vX.Y.Z`) include:

| Asset | Descrizione |
| --- | --- |
| `trust_package.pdf` | Trust Package inglese — materiali di assicurazione pronti per l'auditor |
| `trust_package.ja.pdf` | Trust Package giapponese |
| `aimo-standard-artifacts.zip` | Schemi, template, esempi, regole del validator |
| `SHA256SUMS.txt` | Checksum SHA-256 per tutti gli asset |

### Verifica dei Download

Dopo il download, verificare l'integrità dei file usando i checksum:

=== "Linux"

    ```bash
    # Scaricare il file dei checksum
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verificare un file specifico
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # O verificare manualmente:
    sha256sum trust_package.pdf
    # Confrontare l'output con SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Scaricare il file dei checksum
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Verificare un file specifico
    shasum -a 256 -c SHA256SUMS.txt

    # O verificare manualmente:
    shasum -a 256 trust_package.pdf
    # Confrontare l'output con SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Scaricare il file dei checksum
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Verificare un file specifico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Confrontare l'output Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

## Contenuto dello Zip degli Artefatti

L'`aimo-standard-artifacts.zip` contiene:

- `schemas/jsonschema/*` — JSON Schemas per la validazione
- `templates/ev/*` — Template di evidence (JSON + Markdown)
- `examples/*` — Bundle di evidence di esempio
- `coverage_map/coverage_map.yaml` — Mappatura verso standard esterni
- `validator/rules/*` — Definizioni delle regole di validazione
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, ecc.

## Risorse

- **Tabella Cronologia Versioni**: [Standard > Versioni](../standard/versions/) — tabella delle versioni con link diretti a tutti gli asset di release (PDF, ZIP, SHA256)
- **Changelog (specifica)**: [Standard > Corrente > Changelog](../standard/current/08-changelog/) — cronologia delle modifiche normative e non-normative.
- **Processo di release**: tagging `vX.Y.Z`, build CI, PDF sotto `dist/`, checksum, asset GitHub Release. Vedere [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) e [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) nel repository.
- **Guida alla migrazione**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — percorsi di upgrade per modifiche breaking.

Per la governance e la politica di versionamento, vedere [Governance](../governance/).

## Preparare il pacchetto di submission

Quando si prepara l'evidence per la submission di audit:

1. **Creare l'Evidence Bundle**: Seguire [Evidence Bundle](../artifacts/evidence-bundle/) e [Requisiti Minimi di Evidence](../artifacts/minimum-evidence/) per creare record EV, Dizionario, Riepilogo e Change Log.
2. **Eseguire il Validator**: Eseguire `python validator/src/validate.py bundle/root.json` per controllare la coerenza strutturale. Correggere tutti gli errori prima di procedere.
3. **Generare i Checksum**: Creare checksum SHA-256 per la verifica:

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
4. **Impacchettare**: Creare un archivio zip della directory del bundle.
5. **Documentare l'allineamento della versione**: Annotare quale release dello Standard AIMO (es. `v1.0.0`) l'evidence è allineata.
6. **Consegnare**: Fornire il pacchetto, i checksum e il riferimento alla versione al proprio auditor.

Per la guida completa alla preparazione, vedere [Trust Package](../governance/trust-package/).

## Per gli auditor: Procedura di verifica

Gli auditor che ricevono submission di evidence dovrebbero verificare integrità e struttura:

1. **Verificare i checksum**: Eseguire la verifica dei checksum (Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`) per confermare l'integrità dei file
2. **Eseguire il validator**: Eseguire `python validator/src/validate.py bundle/root.json` per controllare la struttura
3. **Confermare la versione**: Verificare che la versione dichiarata dello Standard AIMO esista su [GitHub Releases](https://github.com/billyrise/aimo-standard/releases)

!!! tip "Ottenere gli strumenti indipendentemente"
    Gli auditor dovrebbero scaricare il validator e gli schemi direttamente dalla release ufficiale dello Standard AIMO, non dalla parte che invia.

Per la procedura completa di verifica (checksum, attestazione, passo-passo), vedere **[Standard → Versioni → Procedura di Verifica](../standard/versions/)**. Vedere anche [Trust Package](../governance/trust-package/) per materiali pronti per l'auditor.

## Dichiarazione di non sovra-dichiarazione

!!! warning "Importante"
    Lo Standard AIMO supporta **spiegabilità e prontezza dell'evidence**. **Non** fornisce consulenza legale, garantisce conformità o certifica la conformità a qualsiasi normativa o framework. Gli adottanti devono verificare le dichiarazioni contro i testi autorevoli e ottenere consulenza professionale quando appropriato.

Vedere [Confini di Responsabilità](../governance/responsibility-boundary/) per ambito, assunzioni e responsabilità degli adottanti.
