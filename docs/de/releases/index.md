---
description: AIMO Standard Releases - Versionierte PDFs, Artefakte und Prüfsummen herunterladen. Changelog, Migrationsleitfäden und Build-Provenienz-Attestierungen.
---
<!-- aimo:translation_status=translated -->

# Releases

Dieser Abschnitt ist ein Hub für versionierte Releases, Changelog, Migration und Verteilungsartefakte.

## Neuestes Release herunterladen

**[GitHub Releases](https://github.com/billyrise/aimo-standard/releases/latest)** — dies ist die einzige autoritative Quelle für das „latest“-Release. Der Site-Pfad `/latest/` leitet auf dieselbe Version weiter.

## Verifizierungsverfahren (dauerhafte Webseite)

Das vollständige **Verifizierungsverfahren** (Download der Assets, Prüfsummenverifizierung, Build-Provenienz-Attestierung) ist als dauerhafte Webseite verfügbar, nicht nur als PDF:

- **[Standard → Versionen → Verifizierungsverfahren](../standard/versions/)** — schrittweise Prüfsummenverifizierung (Linux/macOS/Windows) und Attestierung der Provenienz.

Nutzen Sie diese Seite, wenn Sie Release-Assets verifizieren oder Verifizierungsschritte in Prüfungsdeliverables dokumentieren müssen.

## Release-Assets

Jedes offizielle Release (`vX.Y.Z`-Tag) enthält:

| Asset | Beschreibung |
| --- | --- |
| `trust_package.pdf` | Englisches Trust Package — prüfungsbereite Assurance-Materialien |
| `trust_package.ja.pdf` | Japanisches Trust Package |
| `aimo-standard-artifacts.zip` | Schemas, Templates, Beispiele, Validator-Regeln |
| `SHA256SUMS.txt` | SHA-256-Prüfsummen für alle Assets |

### Downloads verifizieren

Nach dem Download Dateiintegrität mit Prüfsummen verifizieren:

=== "Linux"

    ```bash
    # Prüfsummen-Datei herunterladen
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Bestimmte Datei verifizieren
    sha256sum -c SHA256SUMS.txt --ignore-missing

    # Oder manuell verifizieren:
    sha256sum trust_package.pdf
    # Ausgabe mit SHA256SUMS.txt vergleichen
    ```

=== "macOS"

    ```bash
    # Prüfsummen-Datei herunterladen
    curl -LO https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt

    # Bestimmte Datei verifizieren
    shasum -a 256 -c SHA256SUMS.txt

    # Oder manuell verifizieren:
    shasum -a 256 trust_package.pdf
    # Ausgabe mit SHA256SUMS.txt vergleichen
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Prüfsummen-Datei herunterladen
    Invoke-WebRequest -Uri "https://github.com/billyrise/aimo-standard/releases/latest/download/SHA256SUMS.txt" -OutFile SHA256SUMS.txt

    # Bestimmte Datei verifizieren
    Get-FileHash .\trust_package.pdf -Algorithm SHA256

    # Hash-Ausgabe mit SHA256SUMS.txt vergleichen
    Get-Content .\SHA256SUMS.txt
    ```

## Artefakte-ZIP-Inhalte

Das `aimo-standard-artifacts.zip` enthält:

- `schemas/jsonschema/*` — JSON Schemas zur Validierung
- `templates/ev/*` — Evidence-Templates (JSON + Markdown)
- `examples/*` — Beispiel-Evidence-Bundles
- `coverage_map/coverage_map.yaml` — Zuordnung zu externen Standards
- `validator/rules/*` — Validierungsregel-Definitionen
- `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, etc.

## Ressourcen

- **Versionshistorie-Tabelle**: [Standard > Versionen](../standard/versions/) — Versionstabelle mit direkten Links zu allen Release-Assets (PDF, ZIP, SHA256)
- **Changelog (Spezifikation)**: [Standard > Aktuell > Changelog](../standard/current/08-changelog/) — normative und nicht-normative Änderungshistorie.
- **Release-Prozess**: Tagging `vX.Y.Z`, CI-Build, PDF unter `dist/`, Prüfsummen, GitHub Release-Assets. Siehe [GOVERNANCE.md](https://github.com/billyrise/aimo-standard/blob/main/GOVERNANCE.md) und [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) im Repository.
- **Migrationsleitfaden**: [MIGRATION.md](https://github.com/billyrise/aimo-standard/blob/main/MIGRATION.md) — Upgrade-Pfade für Breaking Changes.

Für Governance- und Versionierungsrichtlinie siehe [Governance](../governance/).

## Einreichungspaket vorbereiten

Bei der Vorbereitung von Evidence für Audit-Einreichung:

1. **Evidence Bundle erstellen**: Folgen Sie [Evidence Bundle](../artifacts/evidence-bundle/) und [Mindestanforderungen an Evidence](../artifacts/minimum-evidence/), um EV-Datensätze, Dictionary, Summary und Change Log zu erstellen.
2. **Validator ausführen**: Führen Sie `python validator/src/validate.py bundle/root.json` aus, um strukturelle Konsistenz zu prüfen. Beheben Sie alle Fehler vor dem Fortfahren.
3. **Prüfsummen generieren**: SHA-256-Prüfsummen zur Verifizierung erstellen:

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
4. **Verpacken**: ZIP-Archiv Ihres Bundle-Verzeichnisses erstellen.
5. **Versionsausrichtung dokumentieren**: Notieren Sie, mit welchem AIMO Standard Release (z.B. `v1.0.0`) Ihr Evidence ausgerichtet ist.
6. **Übergeben**: Stellen Sie das Paket, Prüfsummen und Versionsreferenz Ihrem Prüfer bereit.

Für den vollständigen Vorbereitungsleitfaden siehe [Trust Package](../governance/trust-package/).

## Für Prüfer: Verifizierungsverfahren

Prüfer, die Evidence-Einreichungen erhalten, sollten Integrität und Struktur verifizieren:

1. **Prüfsummen verifizieren**: Prüfsummenverifizierung ausführen (Linux: `sha256sum -c`, macOS: `shasum -a 256 -c`, Windows: `Get-FileHash`), um Dateiintegrität zu bestätigen
2. **Validator ausführen**: `python validator/src/validate.py bundle/root.json` ausführen, um Struktur zu prüfen
3. **Version bestätigen**: Verifizieren, dass die angegebene AIMO Standard-Version unter [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) existiert

!!! tip "Tools unabhängig beziehen"
    Prüfer sollten Validator und Schemas direkt vom offiziellen AIMO Standard Release herunterladen, nicht von der einreichenden Partei.

Für das vollständige Verifizierungsverfahren (Prüfsummen, Attestierung, Schritt-für-Schritt) siehe **[Standard → Versionen → Verifizierungsverfahren](../standard/versions/)**. Siehe auch [Trust Package](../governance/trust-package/) für prüfungsbereite Materialien.

## Keine-Überbeanspruchung-Erklärung

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidence-Bereitschaft**. Er bietet **keine** Rechtsberatung, garantiert keine Compliance und zertifiziert keine Konformität mit Vorschriften oder Frameworks. Anwender müssen Ansprüche gegen maßgebliche Texte verifizieren und bei Bedarf professionelle Beratung einholen.

Siehe [Verantwortungsgrenze](../governance/responsibility-boundary/) für Umfang, Annahmen und Anwenderverantwortlichkeiten.
