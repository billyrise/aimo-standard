---
description: AIMO Trust Package - Prüfungsbereites Materialienpaket. Mindestdokumentation für Prüfer, Rechtsabteilung und IT-Sicherheit zur Bewertung der KI-Governance-Einführungsbereitschaft.
---

# Trust Package (Assurance Package)

Diese Seite bündelt die Mindestmaterialien, die Prüfer, Rechtsabteilung und IT-Sicherheit benötigen, um die Einführungsbereitschaft zu bewerten.
Es ist nur ein Hub; detaillierte Evidence-TOC und Coverage-Tabellen werden in ihren jeweiligen Abschnitten gepflegt.

## Download

**[Trust Package PDF herunterladen (Neuestes Release)](https://github.com/billyrise/aimo-standard/releases/latest)**

Das Trust Package PDF konsolidiert prüfungsbereite Materialien in einem einzigen Dokument. Jedes GitHub Release enthält:

- `trust_package.pdf` — Englisches Trust Package
- `trust_package.ja.pdf` — Japanisches Trust Package
- `aimo-standard-artifacts.zip` — Schemas, Templates, Beispiele, Validator-Regeln
- `SHA256SUMS.txt` — Prüfsummen zur Verifizierung

## Was Sie erhalten

- **Konformität**: Wie man Compliance beansprucht und was die Stufen bedeuten — [Konformität](../conformance/index.md)
- **Coverage Map**: Zuordnung zu externen Standards — [Coverage Map-Index](../coverage-map/index.md), [Coverage Map-Methodologie](../coverage-map/methodology.md)
- **Standard**: Normative Anforderungen und Definitionen — [Standard (Aktuell)](../standard/current/index.md)
- **Taxonomie**: 8-Dimensionen-Klassifizierungssystem für KI-Governance — [Taxonomie](../standard/current/03-taxonomy.md), [Codes](../standard/current/04-codes.md), [Dictionary](../standard/current/05-dictionary.md)
- **Evidence Bundle**: Struktur, TOC, Nachverfolgbarkeit — [Evidence Bundle](../artifacts/evidence-bundle.md)
- **Mindestanforderungen an Evidence**: MUSS-Checkliste nach Lifecycle — [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md)
- **Validator**: Regeln und Referenzprüfungen — [Validator](../validator/index.md)
- **Beispiele**: Prüfungsbereite Beispiel-Bundles — [Beispiele](../examples/index.md)
- **Releases**: Änderungshistorie und Distribution — [Releases](../../releases/)
- **Governance**: Richtlinien, Sicherheit, Lizenzierung — [Governance](../governance/index.md)

## Mindestset für Audit-Bereitschaft

| Element | Wo zu finden | Ergebnis / Was es beweist |
| --- | --- | --- |
| Konformitätsstufen | [Konformität](../conformance/index.md) | Wie man Compliance beansprucht und der Umfang des erforderlichen Evidence |
| Coverage Mapping | [Coverage Map-Index](../coverage-map/index.md), [Coverage Map-Methodologie](../coverage-map/methodology.md) | Erklärbarkeit gegenüber externen Vorschriften und Standards |
| Taxonomie & Dictionary | [Taxonomie](../standard/current/03-taxonomy.md), [Codes](../standard/current/04-codes.md), [Dictionary](../standard/current/05-dictionary.md) | Klassifizierungssystem für KI-Systeme (8 Dimensionen, 91 Codes) |
| Evidence-Artefakte | [Evidence Bundle](../artifacts/evidence-bundle.md), [Mindestanforderungen](../artifacts/minimum-evidence.md), [EV-Template](../standard/current/06-ev-template.md) | Welche Daten existieren müssen, um Nachverfolgbarkeit zu unterstützen |
| Validator-Prüfungen | [Validator](../validator/index.md) | Wie interne Konsistenz und Vollständigkeit verifiziert werden |
| Beispiel-Bundle | [Beispiele](../examples/index.md) | Wie ein prüfungsbereites Paket in der Praxis aussieht |
| Änderungskontrolle | [Releases](../../releases/), [Governance](../governance/index.md) | Wie Updates verwaltet und kommuniziert werden |
| Sicherheit / Lizenz / Marken | [Governance](../governance/index.md) | Rechtliche und Sicherheitsposition für Einführungsentscheidungen |

## Zitierung

Verwenden Sie die Repository-README für Zitierhinweise und Kontext; Governance verlinkt zu den maßgeblichen Richtlinien.
Siehe [README.md](https://github.com/billyrise/aimo-standard/blob/main/README.md) und [Governance](../governance/index.md).

## Artefakte-ZIP-Inhalte

Das `aimo-standard-artifacts.zip` enthält:

- **Taxonomie (SSOT)**: `source_pack/03_taxonomy/` — Dictionary CSV (91 Codes), YAML, Code-System
- **JSON Schemas**: `schemas/jsonschema/` — Maschinenlesbare Validierungsschemas
- **Templates**: `templates/ev/` — Evidence-Datensatz-Templates (JSON + Markdown)
- **Beispiele**: `examples/` — Minimale Beispiel-Bundles für schnelle Einführung
- **Coverage Map**: `coverage_map/coverage_map.yaml` — Zuordnung zu externen Standards
- **Validator-Regeln**: `validator/rules/` — Validierungsregel-Definitionen
- **Governance-Dokumente**: `VERSIONING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE.txt`, etc.

## Verantwortungsgrenze

Der AIMO Standard bietet ein strukturiertes Evidence-Format und Erklärbarkeitsrahmen. Er bietet **keine** Rechtsberatung, Compliance-Zertifizierung, Risikobewertung oder Audit-Durchführung.

Für die vollständige Umfangsdefinition, Annahmen und Anwenderverantwortlichkeiten siehe [Verantwortungsgrenze](responsibility-boundary.md).

## Wie man ein Einreichungspaket vorbereitet

Folgen Sie diesen Schritten, um eine prüfungsbereite Einreichung vorzubereiten:

1. **Evidence Bundle generieren**: EV-Datensätze, Dictionary, Summary und Change Log gemäß [Evidence Bundle](../artifacts/evidence-bundle.md) und [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md) erstellen.
2. **Validator ausführen**: `python validator/src/validate.py bundle/root.json` ausführen, um strukturelle Konsistenz zu prüfen. Fehler vor dem Fortfahren beheben.
3. **Prüfsummen erstellen**: SHA-256-Prüfsummen für alle Einreichungsdateien generieren:

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
4. **Artefakte verpacken**: Erstellen Sie ein ZIP-Archiv Ihres Evidence Bundles:
   ```bash
   zip -r evidence_bundle.zip bundle_directory/
   ```
5. **Release-Version referenzieren**: Notieren Sie, welche AIMO Standard-Version (z.B. `v1.0.0`) Ihr Bundle verwendet.
6. **Übergeben**: Stellen Sie ZIP, Prüfsummen und Versionsreferenz Ihrem Prüfer oder Ihrer Compliance-Funktion bereit.

Für Release-Assets und Verifizierung siehe [Releases](../../releases/).

## Keine-Überbeanspruchung-Erklärung

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidence-Bereitschaft**. Er bietet **keine** Rechtsberatung, garantiert keine Compliance und zertifiziert keine Konformität mit Vorschriften oder Frameworks. Anwender müssen Ansprüche gegen maßgebliche Texte verifizieren und bei Bedarf professionelle Beratung einholen.

Siehe [Verantwortungsgrenze](responsibility-boundary.md) für Details zu Umfang, Annahmen und Anwenderverantwortlichkeiten.

## Für Prüfer: Verifizierungsverfahren

Bei Erhalt einer Evidence-Einreichung sollten Prüfer Integrität und Struktur mit den folgenden Schritten verifizieren:

!!! success "Build-Provenienz verfügbar"
    Alle Release-Assets enthalten kryptografisch signierte Build-Attestierungen. Siehe [Verifizierungsverfahren](../standard/versions/index.md#4-verify-build-provenance-attestation) für Attestierungsverifizierungsschritte.

### Schritt 1: Prüfsummen verifizieren (SHA-256)

=== "Linux"

    ```bash
    # SHA256SUMS.txt mit der Einreichung herunterladen oder erhalten
    # Verifizieren, dass alle Dateien ihren aufgezeichneten Prüfsummen entsprechen
    sha256sum -c SHA256SUMS.txt

    # Oder einzelne Dateien manuell verifizieren:
    sha256sum evidence_bundle.zip
    # Ausgabe mit dem Wert in SHA256SUMS.txt vergleichen
    ```

=== "macOS"

    ```bash
    # Verifizieren, dass alle Dateien ihren aufgezeichneten Prüfsummen entsprechen
    shasum -a 256 -c SHA256SUMS.txt

    # Oder einzelne Dateien manuell verifizieren:
    shasum -a 256 evidence_bundle.zip
    # Ausgabe mit dem Wert in SHA256SUMS.txt vergleichen
    ```

=== "Windows (PowerShell)"

    ```powershell
    # Einzelne Dateien verifizieren
    Get-FileHash .\evidence_bundle.zip -Algorithm SHA256

    # Hash-Ausgabe mit SHA256SUMS.txt vergleichen
    Get-Content .\SHA256SUMS.txt
    ```

Bei Prüfsummenfehlern sollte die Einreichung abgelehnt oder erneut angefordert werden.

### Schritt 2: Bundle-Struktur verifizieren (Validator)

**Voraussetzungen** (einmalige Einrichtung):

```bash
# Das offizielle AIMO Standard Release klonen
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard

# WICHTIG: Die exakte Version verwenden, die in der Einreichung angegeben ist
# VERSION durch die vom Einreicher angegebene Version ersetzen (z.B. v0.0.1)
VERSION=v0.0.1  # ← Version aus der Einreichung abgleichen
git checkout "$VERSION"

# Python-Umgebung einrichten
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

!!! warning "Versionsabgleich"
    Verwenden Sie immer die exakte AIMO Standard-Version, die in der Einreichung angegeben ist. Die Verwendung einer anderen Version kann aufgrund von Schema- oder Regeländerungen zwischen Versionen zu Validierungsabweichungen führen.

**Validierung ausführen**:

```bash
# Das eingereichte Bundle extrahieren
unzip evidence_bundle.zip -d bundle/

# Validator gegen das root.json des Bundles ausführen
python validator/src/validate.py bundle/root.json

# Erwartete Ausgabe: "validation OK" oder Liste von Fehlern
```

**Beispiel** (mit eingebautem Beispiel):

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

Der Validator prüft:

- Erforderliche Dateien existieren (EV-Datensätze, Dictionary)
- JSON-Dateien entsprechen Schema
- Querverweise (request_id, review_id, etc.) sind gültig
- Zeitstempel sind vorhanden und korrekt formatiert

### Schritt 3: Versionsausrichtung verifizieren

Prüfen, dass die Einreichung ein offizielles AIMO Standard Release referenziert:

1. Bestätigen, dass die angegebene Version (z.B. `v0.0.1`) unter [GitHub Releases](https://github.com/billyrise/aimo-standard/releases) existiert
2. Eingereichte Schemas mit den Release-Artefakten vergleichen
3. Abweichungen vom offiziellen Release notieren

### Worauf zu achten ist

| Prüfung | Bestanden-Kriterien | Fehlschlagen-Aktion |
| --- | --- | --- |
| Prüfsummen stimmen | Alle `sha256sum -c`-Prüfungen bestehen | Ablehnen oder erneut anfordern |
| Validator besteht | Keine Fehler von `validate.py` | Korrekturen vor Akzeptanz anfordern |
| Version existiert | Release-Tag existiert auf GitHub | Versionsausrichtung klären |
| Erforderliche Felder vorhanden | EV-Datensätze haben id, timestamp, source, summary | Vervollständigung anfordern |
| Nachverfolgbarkeit intakt | Querverweise lösen korrekt auf | Verknüpfungskorrekturen anfordern |

!!! info "Prüfer-Unabhängigkeit"
    Prüfer sollten Validator und Schemas direkt vom offiziellen AIMO Standard Release beziehen, nicht von der einreichenden Partei, um Verifizierungsunabhängigkeit zu gewährleisten.

## Audit-Reise

Von dieser Seite aus ist die empfohlene Audit-Reise:

1. **Klassifizierungssystem**: [Taxonomie](../standard/current/03-taxonomy.md) + [Dictionary](../standard/current/05-dictionary.md) — das 8-Dimensionen-Code-System verstehen
2. **Evidence-Struktur**: [Evidence Bundle](../artifacts/evidence-bundle.md) — Bundle-TOC und Nachverfolgbarkeit verstehen
3. **Erforderliches Evidence**: [Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md) — MUSS-Checkliste nach Lifecycle
4. **Framework-Ausrichtung**: [Coverage Map](../coverage-map/index.md) + [Methodologie](../coverage-map/methodology.md) — sehen, wie AIMO externen Frameworks zugeordnet ist
5. **Validierung**: [Validator](../validator/index.md) — strukturelle Konsistenzprüfungen ausführen
6. **Download**: [Releases](../../releases/) — Release-Assets herunterladen und Prüfsummen verifizieren
