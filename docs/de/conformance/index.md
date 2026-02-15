---
description: AIMO Standard Konformitätsstufen. Wie Organisationen Konformität geltend machen, Evidenzanforderungen und was jede Stufe für KI-Governance bedeutet.
---
<!-- aimo:translation_status=translated -->

# Konformität

!!! warning "Wichtig: Keine Zertifizierung, keine Prüfung, kein Rechts-/Regelkonformitätsanspruch"
    AIMO Standard definiert ein **Evidenzverpackungs- und Validierungsformat**. Er zertifiziert keine Konformität mit Gesetzen oder Normen.
    Audit- und Prüfungsmeinungen bleiben Verantwortung der unabhängigen Prüfer und der adoptierenden Organisation.
    **Angemessener Anspruch:** „Ein Evidence Bundle wurde gemäß AIMO Standard v0.1.2 erstellt und vom AIMO Validator strukturell validiert.“
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **Unangemessener Anspruch:** „EU-KI-Verordnung konform“, „ISO 42001 zertifiziert“, „behördlich genehmigt“.
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

Diese Stufen sind **interne Evidenzreifegrade** für Verpackung und Nachverfolgbarkeit. Sie sind **keine** Zertifizierung, **keine** Prüfungsmeinung und **keine** rechtliche oder regulatorische Konformität.

!!! note "Stufenname-Alias"
    Die oberste Stufe wurde in informellen Diskussionen früher „Gold“ genannt; der **offizielle Stufenname ist Audit-Ready**.

## AIMO-Konformitätsrahmen (AIMO-MS / AIMO-Controls / AIMO-Audit)

| Komponente | Beschreibung | Evidenzerwartungen |
| --- | --- | --- |
| **AIMO-MS** | Managementsystem-orientierte Struktur: Richtlinien, Rollen, PDCA-orientierte Artefakte, die ISO/IEC-42001-artige Kontrollen unterstützen können. | Request, review, exception, renewal, change log; Summary und Dictionary. |
| **AIMO-Controls** | Lebenszyklus- und Integritätskontrollen: request→review→exception→renewal, Hashing, Signierung (gemäß [Evidence Bundle-Struktur](../../standard/current/09-evidence-bundle-structure/)). | Object_index, payload_index, hash_chain, signing; Lebenszyklusaufzeichnungen. |
| **AIMO-Audit** | Bereitschaft zur Audit-Übergabe: Validator-Bestanden, Prüfsummen, optionale Attestation und Audit-Handoff-Index. | Validator-Ausgabe, bundle_id, Producer-Identität, optionale Signatur-Metadaten und Handoff-Index. |

Evidenzerwartungen werden in [Mindestanforderungen an Evidence](../artifacts/minimum-evidence/) und [Evidence Bundle](../artifacts/evidence-bundle/) beschrieben.

## Konformitätsstufen (nur AIMO)

### Stufe 1 — Foundation

**Zweck:** Nachverfolgbare Basis. Mindestmenge, damit das Bündel identifizierbar, integritätsprüfbar und validatorgeprüft ist.

| Punkt | Anforderung |
| --- | --- |
| **Erforderliche Artefakte** | [Evidence Bundle](../artifacts/evidence-bundle/)-Struktur (manifest.json, objects/, payload_index pro Spez.); [Validator](../validator/)-Bestanden; Verknüpfung zu [Mindestanforderungen an Evidence](../artifacts/minimum-evidence/). |
| **Typische Audit-Fragen** | Was ist im Umfang? Wer hat das Bündel erstellt? Können Hashes verifiziert werden? |
| **Typische Lücken** | Fehlende Manifest-Metadaten (bundle_id, created_at, producer); Validator nicht ausgeführt oder nicht beigefügt. |

### Stufe 2 — Operational

**Zweck:** Evidenz operativer Kontrolle. Baut auf Foundation mit Lebenszyklusnachweis und Überwachung auf.

| Punkt | Anforderung |
| --- | --- |
| **Erforderliche Artefakte** | Alle Foundation-MUST-Punkte; Lebenszyklus-Kontrollnachweis (request/Genehmigung, review, exception oder „keine Ausnahmen“, renewal-Plan); mindestens ein Überwachungsartefakt (Vorfallprotokoll oder periodische Prüfung oder Human-Oversight-Stichprobe); change log mit Integritätsverknüpfung; Nachweis-vs.-Prüfungsgrenzen-Erklärung. |
| **Typische Audit-Fragen** | Wer hat die Nutzung genehmigt? Wie werden Ausnahmen verfolgt? Wann war die letzte Überprüfung? |
| **Typische Lücken** | Review/Genehmigung nicht mit request verknüpft; kein Überwachungsartefakt; change log referenziert betroffene Objekte nicht. |

### Stufe 3 — Audit-Ready

**Zweck:** Qualität der Audit-Übergabe. Vollständige Attestation, Reproduzierbarkeit und External-Forms-Slot.

| Punkt | Anforderung |
| --- | --- |
| **Erforderliche Artefakte** | Alle Operational-MUST-Punkte; mindestens eine digitale Signatur über das Manifest (Signaturgeber-Identität + Algorithmus); TSA- oder „kein TSA“-Erklärung; Reproduzierbarkeitspaket (exakter Validator-Befehl, erwartete Ausgaben, Umgebungsmetadaten); External-Forms-Abschnitt mit offiziellen Vorlagen/Checklisten unverändert angefügt und querverwiesen; begrenzte Vollständigkeitserklärung; einseitiger Audit-Handoff-Index (Artefakt → Hash → Producer → Datum). |
| **Typische Audit-Fragen** | Wie kann ein Prüfer die Validierung erneut ausführen? Wo sind externe Checklisten und wie werden sie dem Bündel zugeordnet? |
| **Typische Lücken** | Signatur vorhanden, aber Signaturgeber/Algorithmus nicht dokumentiert; kein Handoff-Index; External Forms nicht gehasht oder im Manifest nicht referenziert. |

## Mindestevidenz nach Stufe (Zusammenfassung)

| Stufe | MUST (Zusammenfassung) |
| --- | --- |
| **Foundation** | Bündelstruktur (manifest, object_index, payload_index); sha256 für referenzierte Objekte; bundle_id, created_at, producer; Validator-Lauf + Version; Evidenzwörterbuch-Basis (Systemname, Owner, Zweck, Datenkategorien, Lebenszyklusphase); Zugriffs- und Aufbewahrungserklärung (wer, Dauer, Speicherart, Manipulationsnachweis). SHOULD: minimaler change-log-Eintrag. |
| **Operational** | Alle Foundation-MUST; Lebenszyklusnachweis (request/Genehmigung, review, exception oder „keine“, renewal + letzte renewal); ≥1 Überwachungsartefakt; change-log-Einträge referenzieren betroffene Objekte; ausdrückliche Nachweis-vs.-Prüfungsgrenzen-Erklärung. |
| **Audit-Ready** | Alle Operational-MUST; ≥1 Signatur über Manifest (Signaturgeber-Identität + Algorithmus); TSA oder „kein TSA“; Reproduzierbarkeitspaket; External Forms aufgeführt und querverwiesen; begrenzte Vollständigkeitserklärung; Audit-Handoff-Index. |

**Vorhandensein** mindestens einer Signatur (die das Manifest zum Ziel hat) ist durch die normative [Evidence Bundle-Struktur](../../standard/current/09-evidence-bundle-structure/) für alle Bündel gefordert. **Audit-Ready** fügt strengere **kryptografische Attestation** hinzu (Signaturgeber-Identität, Algorithmus, TSA-Erklärung, Revalidierungsanleitung), damit Dritte die Prüfungen erneut durchführen können.

## ISO/IEC 42001-Zuordnung (informativ)

Die folgende Tabelle zeigt, wie AIMO-Artefakte **Evidenz für** typische ISO/IEC-42001-Klauselfamilien unterstützen. Sie ist nur informativ; sie impliziert keine Zertifizierung oder Konformität.

| ISO/IEC 42001-Klauselfamilie | AIMO-Artefakte, die Evidenz unterstützen |
| --- | --- |
| Kontext der Organisation | Summary, Dictionary, scope_ref |
| Führung / Politik | Summary, review, dictionary |
| Planung (Risiken, Ziele) | request, review, exception, EV, Dictionary |
| Unterstützung (Ressourcen, Kompetenz, Dokumentation) | Summary, review, EV, change_log |
| Betrieb | EV, request, review, exception; operative Kontrollen |
| Leistungsbewertung (Überwachung, internes Audit, Managementreview) | EV, change_log, review, renewal |
| Verbesserung | exception, renewal, change_log |

Siehe [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) und [ISO-42001-Zertifizierungsvorbereitungs-Toolkit](../artifacts/iso-42001-certification-readiness-toolkit/) für Details.

## Anspruchsformulierungen (Anti-Überbeanspruchung)

Nur Ansprüche verwenden, die das tatsächlich Durchgeführte zutreffend beschreiben. Zertifizierung und rechtliche Konformität bleiben Verantwortung der Adoptierenden und akkreditierten Stellen.

**Akzeptabel (Beispiele)**

- „Wir sind AIMO-konform (Stufe 2) gegen AIMO Standard v0.1.2; dies impliziert keine ISO-Zertifizierung oder rechtliche Konformität.“
- „Wir nutzen AIMO-Artefakte zur ISO/IEC-42001-Vorbereitung; Zertifizierungsentscheidungen liegen bei akkreditierten Zertifizierungsstellen.“
- „Ein Evidence Bundle wurde gemäß AIMO Standard v0.1.2 erstellt und vom AIMO Validator strukturell validiert.“

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**Unakzeptabel (Beispiele)**

- „EU-KI-Verordnung konform“ (AIMO zertifiziert keine regulatorische Konformität.)
- „ISO 42001 zertifiziert“ (Zertifizierung wird von akkreditierten Stellen ausgestellt, nicht von AIMO.)
- „Behördlich genehmigt“ (AIMO ist kein behördliches Genehmigungssystem.)
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## Verwandte Seiten

- [Trust Package](../governance/trust-package/) — Konsolidierter Einstieg für Prüfer
- [Responsibility Boundary](../governance/responsibility-boundary/) — Was AIMO bietet und nicht bietet
- [Standard (Current)](../standard/current/) — Normative Anforderungen
- [Artifacts](../artifacts/) — Evidenzstruktur und Mindestanforderungen
- [Validator](../validator/) — Strukturvalidierung
