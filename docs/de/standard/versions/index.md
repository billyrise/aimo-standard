---
description: AIMO Standard Versionshistorie. Offizielle eingefrorene Releases mit prüfungsbereiten PDFs, maschinenlesbaren Artefakten, Prüfsummen und Build-Provenienz-Attestierungen.
---

# Versionen

Offizielle Releases sind eingefrorene Snapshots, die mit prüfungsbereiten PDFs und maschinenlesbaren Artefakten veröffentlicht werden.

## Neuestes Release

!!! success "Aktuelle Version"
    **v0.0.2** (2026-02-02) — [Dokumentation ansehen](../current/index.md) | [GitHub Release](https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2)

## Versionshistorie

| Version | Datum | Release-Hinweise | PDF (EN) | PDF (JA) | Artefakte | Prüfsummen |
| :------ | :--- | :------------ | :------- | :------- | :-------- | :-------- |
| **v0.0.2** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.2/SHA256SUMS.txt) |
| **v0.0.1** | 2026-02-02 | [Changelog](../current/08-changelog.md) | [trust_package.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.pdf) | [trust_package.ja.pdf](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/trust_package.ja.pdf) | [ZIP](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/aimo-standard-artifacts.zip) | [SHA256](https://github.com/billyrise/aimo-standard/releases/download/v0.0.1/SHA256SUMS.txt) |

!!! note "Datenquelle"
    Diese Versionstabelle ist mit [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) synchronisiert. Jedes Release-Tag (`vX.Y.Z`) entspricht einem eingefrorenen Snapshot der Spezifikation.

## Verifizierungsverfahren

Prüfer und Implementierer sollten die Download-Integrität mit SHA-256-Prüfsummen verifizieren:

### 1. Release-Assets herunterladen

=== "Linux / macOS"

    ```bash
    # Alle Assets für eine bestimmte Version herunterladen
    VERSION=v0.0.1
    BASE_URL="https://github.com/billyrise/aimo-standard/releases/download/${VERSION}"

    curl -LO "${BASE_URL}/trust_package.pdf"
    curl -LO "${BASE_URL}/trust_package.ja.pdf"
    curl -LO "${BASE_URL}/aimo-standard-artifacts.zip"
    curl -LO "${BASE_URL}/SHA256SUMS.txt"
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Alle Assets für eine bestimmte Version herunterladen
    $VERSION = "v0.0.1"
    $BASE_URL = "https://github.com/billyrise/aimo-standard/releases/download/$VERSION"

    Invoke-WebRequest -Uri "$BASE_URL/trust_package.pdf" -OutFile trust_package.pdf
    Invoke-WebRequest -Uri "$BASE_URL/trust_package.ja.pdf" -OutFile trust_package.ja.pdf
    Invoke-WebRequest -Uri "$BASE_URL/aimo-standard-artifacts.zip" -OutFile aimo-standard-artifacts.zip
    Invoke-WebRequest -Uri "$BASE_URL/SHA256SUMS.txt" -OutFile SHA256SUMS.txt
    ```

### 2. Prüfsummen verifizieren

=== "Linux"

    ```bash
    # Alle heruntergeladenen Dateien gegen Prüfsummen verifizieren
    sha256sum -c SHA256SUMS.txt

    # Erwartete Ausgabe (alle sollten "OK" zeigen):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "macOS"

    ```bash
    # Alle heruntergeladenen Dateien gegen Prüfsummen verifizieren
    shasum -a 256 -c SHA256SUMS.txt

    # Erwartete Ausgabe (alle sollten "OK" zeigen):
    # trust_package.pdf: OK
    # trust_package.ja.pdf: OK
    # aimo-standard-artifacts.zip: OK
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Jede Datei verifizieren
    Get-FileHash .\trust_package.pdf -Algorithm SHA256
    Get-FileHash .\trust_package.ja.pdf -Algorithm SHA256
    Get-FileHash .\aimo-standard-artifacts.zip -Algorithm SHA256

    # Hash-Ausgabe mit SHA256SUMS.txt vergleichen
    Get-Content .\SHA256SUMS.txt
    ```

### 3. Manuelle Verifizierung (Alternative)

=== "Linux"

    ```bash
    # Hash für eine bestimmte Datei berechnen
    sha256sum trust_package.pdf

    # Ausgabe mit SHA256SUMS.txt vergleichen
    cat SHA256SUMS.txt
    ```

=== "macOS"

    ```bash
    # Hash für eine bestimmte Datei berechnen
    shasum -a 256 trust_package.pdf

    # Ausgabe mit SHA256SUMS.txt vergleichen
    cat SHA256SUMS.txt
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Hash für eine bestimmte Datei berechnen
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Prüfsummen-Datei ansehen
    Get-Content .\SHA256SUMS.txt
    ```

!!! tip "Für Prüfer"
    Beziehen Sie die Prüfsummen-Datei immer direkt vom offiziellen GitHub Release, nicht von der einreichenden Partei. Dies gewährleistet unabhängige Verifizierung.

### 4. Build-Provenienz verifizieren (Attestierung)

Alle Release-Assets enthalten kryptografisch signierte Build-Provenienz-Attestierungen, die von GitHub Actions generiert werden. Dies ermöglicht es Ihnen zu verifizieren, dass Assets im offiziellen Repository ohne Manipulation erstellt wurden.

**Voraussetzungen**: [GitHub CLI](https://cli.github.com/) (`gh`) installieren

```bash
# Release-Assets mit GitHub CLI herunterladen
VERSION=v0.0.1
gh release download "$VERSION" --repo billyrise/aimo-standard

# Attestierung für jedes Asset verifizieren
gh attestation verify trust_package.pdf --repo billyrise/aimo-standard
gh attestation verify trust_package.ja.pdf --repo billyrise/aimo-standard
gh attestation verify aimo-standard-artifacts.zip --repo billyrise/aimo-standard
gh attestation verify SHA256SUMS.txt --repo billyrise/aimo-standard
```

**Erwartete Ausgabe** (Erfolg):

```
Loaded digest sha256:abc123... for file trust_package.pdf
Loaded 1 attestation from GitHub API
✓ Verification succeeded!
```

**Offline-Verifizierung** (Air-Gapped-Umgebungen):

```bash
# Zuerst den trusted root herunterladen (erfordert einmalig Netzwerk)
gh attestation trusted-root > trusted-root.jsonl

# Dann offline verifizieren
gh attestation verify trust_package.pdf \
  --repo billyrise/aimo-standard \
  --custom-trusted-root trusted-root.jsonl
```

!!! info "Was Attestierung beweist"
    Build-Provenienz-Attestierung beweist kryptografisch, dass die Release-Assets:

    1. Von GitHub Actions erstellt wurden (nicht auf einem Entwickler-Rechner)
    2. Aus dem offiziellen `billyrise/aimo-standard`-Repository erstellt wurden
    3. Aus dem exakten Commit erstellt wurden, der mit dem Release-Tag verbunden ist
    4. Nach Abschluss des Builds nicht modifiziert wurden

## Kompatibilität

AIMO Standard folgt [Semantic Versioning](https://semver.org/) (SemVer):

| Änderungstyp | Versionserhöhung | Auswirkung |
| :---------- | :----------- | :----- |
| **MAJOR** | X.0.0 | Breaking Changes — Migration erforderlich |
| **MINOR** | 0.X.0 | Rückwärtskompatible Ergänzungen |
| **PATCH** | 0.0.X | Korrekturen und Klarstellungen |

Für die vollständige Versionierungsrichtlinie siehe [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md).

## Migration

Beim Upgrade zwischen Versionen mit Breaking Changes:

1. Prüfen Sie das [Changelog](../current/08-changelog.md) auf Breaking Changes
2. Lesen Sie den [Migrationsleitfaden](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) für spezifische Upgrade-Pfade
3. Aktualisieren Sie Ihr Evidence Bundle, um es an die neuen Schema-Anforderungen anzupassen
4. Führen Sie den Validator erneut aus, um Compliance zu verifizieren

!!! warning "Breaking Changes"
    MAJOR-Versions-Updates können Änderungen an bestehenden Evidence Bundles erfordern. Lesen Sie immer den Migrationsleitfaden vor dem Upgrade.

## Versionierte Dokumentations-Snapshots

Jedes Release erstellt einen eingefrorenen Dokumentations-Snapshot, der zugänglich ist unter:

- Produktion: `https://standard.aimoaas.com/{version}/` (z.B. `/0.0.1/`)
- GitHub Pages: `https://billyrise.github.io/aimo-standard/{version}/`

### URL-Typen und ihre Bedeutung

| URL-Muster | Beschreibung | Für Audit-Zitierungen? |
|-------------|-------------|---------------------|
| `/X.Y.Z/` (z.B. `/0.0.1/`) | **Eingefrorenes Release** — unveränderlicher Snapshot | **Ja** (bevorzugt) |
| `/latest/` | **Alias** — leitet zum neuesten Release weiter | Ja (löst zu `/X.Y.Z/` auf) |
| `/dev/` | **Vorschau** — unveröffentlichter Main-Branch-Inhalt | **Nein** (nicht für Zitierungen) |

!!! warning "Verständnis von `/latest/` vs `/dev/`"
    - **`/latest/`** ist ein Alias (Weiterleitung) zur neuesten **veröffentlichten** Version. Es ist sicher für Zitierungen, da es zu einem eingefrorenen Snapshot auflöst.
    - **`/dev/`** spiegelt den aktuellen `main`-Branch und kann **unveröffentlichte Änderungen** enthalten. Zitieren Sie `/dev/` niemals in Auditberichten.

### FAQ

??? question "Warum ist `/latest/` keine Versionsnummer?"
    `/latest/` ist ein Komfort-Alias, der immer zum neuesten stabilen Release weiterleitet (z.B. `/0.0.1/`). Dies ermöglicht es Benutzern, eine einzelne URL zu bookmarken und automatisch die aktuelle Version zu erhalten. Für formelle Audits, die Unveränderlichkeit erfordern, zitieren Sie stattdessen die explizite Versions-URL.

??? question "Welche URL sollten Prüfer zitieren?"
    - **Formelle Audits (Unveränderlichkeit erforderlich)**: Verwenden Sie `/X.Y.Z/` (z.B. `https://standard.aimoaas.com/0.0.1/standard/current/`)
    - **Allgemeine Verweise**: `/latest/` ist akzeptabel, da es zum aktuellen Release weiterleitet
    - **Niemals zitieren**: `/dev/` (unveröffentlicht, änderbar)

??? question "Was wenn `/latest/` anderen Inhalt zeigt als erwartet?"
    Dies wäre ein Deployment-Bug. Wenn Sie vermuten, dass `/latest/` vom neuesten [GitHub Release](https://github.com/billyrise/aimo-standard/releases) abweicht, [melden Sie bitte ein Issue](https://github.com/billyrise/aimo-standard/issues). Der `/latest/`-Alias sollte immer zum neuesten getaggten Release weiterleiten.

## Ressourcen

- **[Releases-Hub](../../releases/index.md)** — Einreichungsvorbereitung, Prüfer-Verifizierung, Keine-Überbeanspruchung-Erklärung
- **[Trust Package](../../governance/trust-package.md)** — Prüfungsbereite Assurance-Materialien
- **[Changelog (detailliert)](../current/08-changelog.md)** — Vollständige Änderungshistorie mit Deprecation-Tracking
- **[VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)** — Vollständige Versionierungsrichtlinie
