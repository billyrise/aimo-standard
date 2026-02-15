---
description: Normative Root-Struktur und Manifest für Evidence Bundle (v0.1). Integrity MUST; Custody implementierungsdefiniert.
---
<!-- aimo:translation_status=translated -->

# Evidence Bundle Root-Struktur (v0.1)

Diese Seite definiert das **normative** Root-Layout und Manifest eines Evidence Bundle. Validatoren MÜSSEN Bündel, die diese Anforderungen nicht erfüllen, vor jeder Schema-Validierung ablehnen.

## v0.1 normative MUST (Zusammenfassung)

- **manifest.json** am Bündel-Root ist erforderlich.
- **object_index** und **payload_index**: Jeder Eintrag MUSS **sha256** (64 Kleinbuchstaben-Hex) enthalten; Pfade MÜSSEN relativ sein und DÜRFEN weder `../` enthalten noch den Bündel-Root verlassen.
- **signing.signatures** MUSS ein nichtleeres Array sein (leeres Array ist ungültig).
- Jeder Signatur-Eintrag MUSS haben: **path** unter `signatures/` (Pfad-Traversierung verboten), **targets** (Array, mindestens ein Pfad), und mindestens eine Signatur im Bündel MUSS **manifest.json** in **targets** aufführen (Manifest-Signierung ist Pflicht).
- **hash_chain**: v0.1 MUSS **algorithm**, **head**, **path** (unter `hashes/`) und **covers** mit mindestens **manifest.json** und **objects/index.json** enthalten.

Validatoren MÜSSEN dies durchsetzen, bevor ein Bündel akzeptiert wird. JSON Schema und Referenz-Validator implementieren dieselben Regeln.

## Root-erforderliche Struktur (MUST)

Am Bündel-Root MÜSSEN folgende Elemente vorhanden sein:

| Element | Typ | Zweck |
| --- | --- | --- |
| **manifest.json** | Datei | Bündel-Manifest (siehe unten). Kanonischer Deskriptor für das Bündel. |
| **objects/** | Verzeichnis | Aufgezählte Objekte (z. B. Metadaten, Indizes). In `manifest.json` object_index aufgeführt. |
| **payloads/** | Verzeichnis | Payload-Dateien (z. B. Root-EV-JSON, Evidence-Pack-Dateien). In `manifest.json` payload_index aufgeführt. |
| **signatures/** | Verzeichnis | Digitale Signaturen. v0.1 MUSS mindestens eine das Manifest referenzierende Signaturdatei enthalten (Existenz und Zielreferenz; kryptografische Verifizierung ist zukünftige Erweiterung). |
| **hashes/** | Verzeichnis | Hash-Kette oder Integritätsaufzeichnungen (wie von `manifest.json` hash_chain gefordert). |

Implementierer DÜRFEN kein Bündel einreichen, dem eines davon fehlt. Der Validator MUSS mit klarer Meldung fehlschlagen, wenn die Root-Struktur unvollständig ist.

## Integrity (normativ) vs. Custody (Implementierung)

- **Integrity** ist in v0.1 **normativ**: Die Norm verlangt, dass das Bündel Integritätsmetadaten trägt (Manifest, sha256 für indizierte Dateien, Signaturvorhandensein für das Manifest). Validatoren MÜSSEN prüfen, dass:
  - Erforderliche Verzeichnisse und Dateien existieren.
  - `manifest.json` vorhanden und gültig ist (Schema- und Vorschema-Checks).
  - Jede in object_index und payload_index aufgeführte Datei am angegebenen Pfad existiert und ihr Inhalt mit dem deklarierten `sha256` übereinstimmt.
  - `signatures/` mindestens eine das Manifest zum Ziel habende Signatur enthält (v0.1: nur Existenz und Referenz; v0.1.1: Verifizierungsmetadaten RECOMMENDED; v0.2 geplant: kryptografische Verifizierung im Umfang).
- **Custody** (Speicherung, Zugriffskontrolle, Aufbewahrung, WORM) ist **implementierungsdefiniert**. Die Norm schreibt nicht vor, wie Verwahrer das Bündel speichern oder schützen; sie verlangt nur, dass das Paket bei Einreichung die obigen Integrity-Anforderungen erfüllt.

## manifest.json (MUST-Felder)

Das Manifest MUSS mindestens enthalten:

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| **bundle_id** | string (UUID) | Eindeutiger Bezeichner für dieses Bündel. |
| **bundle_version** | string (SemVer) | Version des Bündels. |
| **created_at** | string (date-time) | Erstellungszeitstempel. |
| **scope_ref** | string | Umfangsreferenz (z. B. `SC-001`). Muster `SC-*`. |
| **object_index** | array | Liste der Objekte: `id`, `type`, `path`, `sha256`. Pfade MÜSSEN relativ sein, DÜRFEN weder `../` enthalten noch mit `/` beginnen und MÜSSEN innerhalb des Evidence-Bundle-Roots bleiben (Validatoren MÜSSEN den Root verlassende Pfade ablehnen). |
| **payload_index** | array | Liste der Payloads: `logical_id`, `path`, `sha256`, `mime`, `size`. Gleiche Pfadregeln wie object_index (relativ, kein `../`, kein führendes `/`, innerhalb Bündel-Root). |
| **hash_chain** | object | **Normativ (v0.1):** MUSS `algorithm` (sha256 \| merkle), `head` (64 Kleinbuchstaben-Hex), `path` (relativer Pfad unter `hashes/`; kein `../`, kein führendes `/`) und `covers` (Array, mindestens ein Element) enthalten. v0.1 MUSS `manifest.json` und `objects/index.json` in `covers` enthalten. |
| **signing** | object | **Normativ (v0.1):** MUSS `signatures` (Array, mindestens ein Eintrag) enthalten. Jeder Eintrag MUSS haben: `signature_id` (z. B. SIG-... oder UUID), `path` (relativ unter `signatures/`; kein `../`, kein führendes `/`), `targets` (Array, mindestens ein Pfad; v0.1 MUSS in mindestens einer Signatur targets `manifest.json` enthalten), `algorithm` (eines von ed25519, rsa-pss, ecdsa, unspecified). `created_at` (date-time) ist MAY. **Hinweis:** Kryptografische Verifizierung von Signaturen liegt in v0.1 außerhalb des Umfangs; Referenz (welche Datei und was sie zum Ziel hat) ist erforderlich. |

**v0.1.1 optionale Signaturmetadaten (RECOMMENDED für Dritt-Wiederausführung):**

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| **signer_identity** | string | Identität des Signaturgebers (z. B. PGP-Fingerabdruck, did:key). |
| **signed_at** | string (date-time) | Zeitpunkt der Signaturanwendung (ISO 8601). |
| **verification_command** | string | Beispiel-CLI-Befehl für einen Prüfer zur erneuten Verifizierung. |
| **canonicalization** | string | Wie die signierte Payload kanonisiert wurde: `rfc8785_json`, `cbor` oder `unspecified`. |

Integrity und Verifizierung: **v0.1** — nur Referenz und Existenz. **v0.1.1** — Metadaten zur Verifizierung RECOMMENDED. **v0.2** (geplant) — kryptografische Verifizierung im Umfang.

- **sha256**-Werte MÜSSEN 64 Kleinbuchstaben-Hexadezimalzeichen sein.
- **path** MUSS ein relativer Pfad sein; DARF weder `../` enthalten noch mit `/` beginnen; Pfade MÜSSEN innerhalb des Evidence-Bundle-Roots bleiben.
- Das Manifest KANN eine explizite Selbstreferenz (z. B. in object_index oder einem eigenen Feld) enthalten, sodass die eigene Integrität des Manifests abgedeckt ist; Validatoren MÜSSEN ein Bündel akzeptieren, in dem das Manifest entweder in einem Index aufgeführt oder von einer Signatur explizit referenziert ist.

Siehe JSON Schema: `schemas/jsonschema/evidence_bundle_manifest.schema.json`.

## Zukünftige Erweiterungen (informativ)

- **Control/Requirement-Verknüpfung**: Eine zukünftige Version könnte einen Standardweg hinzufügen, Evidence-Bundle-Elemente mit Control- oder Requirement-Kennungen zu verknüpfen (z. B. für Export nach NIST OSCAL oder ähnliche Audit-Automatisierungsformate). In v0.1 oder v0.1.1 nicht erforderlich.

## Referenzen

- [Evidence Bundle (Artefaktübersicht)](../../../artifacts/evidence-bundle/) — Zweck und Inhaltsverzeichnis
- [EV-Vorlage — External Forms und Audit-Handoff-Index](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is) — wo offizielle Vorlagen/Checklisten angefügt und im Manifest referenziert werden
- [Signaturverifizierungs-Roadmap](../../../artifacts/signature-verification-roadmap/) — v0.1.1-Metadaten und v0.2-Verifizierungsplan
- [Validator](../../../validator/) — wie der Validator diese Struktur durchsetzt
- [Mindestanforderungen an Evidence](../../../artifacts/minimum-evidence/) — MUST-Checkliste
