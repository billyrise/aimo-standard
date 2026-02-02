---
description: Cronologia delle versioni dello Standard AIMO. Release ufficiali congelate con PDF pronti per l'auditor, artefatti leggibili da macchina, checksum e attestazioni di build provenance.
---

# Versioni

Le release ufficiali sono snapshot congelati pubblicati con PDF pronti per l'auditor e artefatti leggibili da macchina.

## Ultima Release

!!! success "Versione Corrente"
    **v0.0.2** (2026-02-02) — [Visualizza Documentazione](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## Cronologia delle Versioni

| Versione | Data | Note di Release | PDF (EN) | PDF (JA) | Artefatti | Checksum |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Fonte dei Dati"
    Questa tabella delle versioni è sincronizzata con [GitHub Releases](https://github.com/billyrise/aimo-standard/releases). Ogni tag di release (`vX.Y.Z`) corrisponde a uno snapshot congelato della specifica.

## Procedura di Verifica

Auditor e implementatori dovrebbero verificare l'integrità dei download usando i checksum SHA-256:

### 1. Scaricare gli Asset di Release

=== "Linux / macOS"

    ```bash
    # Scaricare tutti gli asset per una versione specifica
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Scaricare tutti gli asset per una versione specifica
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Verificare i Checksum

=== "Linux"

    ```bash
    # Verificare tutti i file scaricati contro i checksum
    sha256sum -c SHA256SUMS.txt

    # Output atteso (tutti dovrebbero mostrare "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Verificare tutti i file scaricati contro i checksum
    shasum -a 256 -c SHA256SUMS.txt

    # Output atteso (tutti dovrebbero mostrare "OK"):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Verificare ogni file
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Confrontare l'output Hash con SHA256SUMS.txt
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Verifica Manuale (Alternativa)

=== "Linux"

    ```bash
    # Calcolare l'hash per un file specifico
    sha256sum trust_package.pdf

    # Confrontare l'output con SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Calcolare l'hash per un file specifico
    shasum -a 256 trust_package.pdf

    # Confrontare l'output con SHA256SUMS.txt
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Calcolare l'hash per un file specifico
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Visualizzare il file dei checksum
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "Per gli Auditor"
    Ottenere sempre il file dei checksum direttamente dalla GitHub Release ufficiale, non dalla parte che invia. Questo assicura una verifica indipendente.

### 4. Verificare Build Provenance (Attestazione)

Tutti gli asset di release includono attestazioni di build provenance firmate crittograficamente generate da GitHub Actions. Questo permette di verificare che gli asset siano stati costruiti nel repository ufficiale senza manomissioni.

**Prerequisiti**: Installare [GitHub CLI](https://cli.github.com/) (`gh`)

```bash
# Scaricare gli asset di release usando GitHub CLI
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Verificare l'attestazione per ogni asset
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Output atteso** (successo):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Verifica offline** (ambienti air-gapped):

```bash
# Prima, scaricare la trusted root (richiede rete una volta)
gh attestation trusted-root > trusted-root.jsonl

# Poi verificare offline
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "Cosa dimostra l'attestazione"
    L'attestazione di build provenance dimostra crittograficamente che gli asset di release sono stati:

    1. Costruiti da GitHub Actions (non dalla macchina locale di uno sviluppatore)
    2. Costruiti dal repository ufficiale `billyrise/aimo-standard`
    3. Costruiti dal commit esatto associato al tag di release
    4. Non modificati dopo il completamento del build

## Compatibilità

Lo Standard AIMO segue [Semantic Versioning](https://semver.org/) (SemVer):

| Tipo di Modifica | Incremento Versione | Impatto |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Modifiche breaking — migrazione richiesta |
| **MINOR** | 0.X.0 | Aggiunte retrocompatibili |
| **PATCH** | 0.0.X | Fix e chiarimenti |

Per la politica di versionamento completa, vedere [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migrazione

Quando si aggiorna tra versioni con modifiche breaking:

1. Controllare il [Changelog](../current/08-changelog.md) per le modifiche breaking
2. Rivedere la [Guida alla Migrazione](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) per percorsi di upgrade specifici
3. Aggiornare l'Evidence Bundle per allinearsi ai nuovi requisiti dello schema
4. Rieseguire il validator per verificare la conformità

!!! warning "Modifiche Breaking"
    Gli aggiornamenti di versione MAJOR possono richiedere modifiche agli Evidence Bundle esistenti. Rivedere sempre la guida alla migrazione prima di aggiornare.

## Snapshot di Documentazione Versionati

Ogni release crea uno snapshot di documentazione congelato accessibile su:

- Produzione: `https://standard.aimoaas.com/{version}/` (es. `/0.0.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### Tipi di URL e il Loro Significato

| Pattern URL | Descrizione | Per Citazioni di Audit? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (es. `/0.0.1/`) | **Release congelata** — snapshot immutabile | **Sì** (preferito) |
| `/latest/` | **Alias** — redirect alla release più recente | Sì (risolve a `/X.Y.Z/`) |
| `/dev/` | **Anteprima** — contenuto non rilasciato del branch main | **No** (non per citazioni) |

!!! warning "Comprendere `/latest/` vs `/dev/`"
    - **`/latest/`** è un alias (redirect) alla versione **rilasciata** più recente. È sicuro per le citazioni poiché risolve a uno snapshot congelato.
    - **`/dev/`** riflette il branch `main` corrente e può contenere **modifiche non rilasciate**. Mai citare `/dev/` nei report di audit.

### FAQ

??? question "Perché `/latest/` non è un numero di versione?"
    `/latest/` è un alias di convenienza che redirect sempre alla release stabile più recente (es. `/0.0.1/`). Questo permette agli utenti di salvare un singolo URL mentre ottengono automaticamente la versione corrente. Per audit formali che richiedono immutabilità, citare invece l'URL della versione esplicita.

??? question "Quale URL dovrebbero citare gli auditor?"
    - **Audit formali (immutabilità richiesta)**: Usare `/X.Y.Z/` (es. `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **Riferimenti generali**: `/latest/` è accettabile poiché redirect alla release corrente
    - **Mai citare**: `/dev/` (non rilasciato, soggetto a modifiche)

??? question "Cosa fare se `/latest/` mostra contenuto diverso da quello atteso?"
    Questo sarebbe un bug di deployment. Se sospetti che `/latest/` differisca dalla [GitHub Release](https://github.com/billyrise/aimo-standard/releases) più recente, per favore [segnala un problema](https://github.com/billyrise/aimo-standard/issues). L'alias `/latest/` dovrebbe sempre redirect alla release taggata più recente.

## Risorse

- **[Hub Release](../../releases/index.md)** — Preparazione della submission, verifica per auditor, dichiarazione di non sovra-dichiarazione
- **[Trust Package](../../governance/trust-package.md)** — Materiali di assicurazione pronti per l'auditor
- **[Changelog (dettagliato)](../current/08-changelog.md)** — Cronologia completa delle modifiche con tracciamento deprecazioni
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Politica di versionamento completa
