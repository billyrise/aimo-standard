---
description: ISO/IEC 42001 Zertifizierungsbereitschafts-Toolkit. Kürzester Weg zu prüffähiger Evidence mit AIMO-Artefakten, abgestimmt auf ISO 42001. Unterstützt nur die Bereitschaft; verleiht keine Zertifizierung.
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 Certification Readiness Toolkit

Diese Seite ist eine **praktische, adoptionsorientierte** Anleitung zur Erstellung **prüffähiger Evidence** in Anlehnung an ISO/IEC 42001 mit AIMO-Artefakten. Sie **unterstützt die Bereitschaft**; sie **verleiht keine** Zertifizierung. Zertifizierungsentscheidungen obliegen **akkreditierten Zertifizierungsstellen**.

## Ziel

Ein strukturiertes, vom Validator geprüftes Evidence Bundle erstellen, das ISO/IEC 42001-artige Kontrollen (Kontext, Führung, Planung, Unterstützung, Betrieb, Bewertung, Verbesserung) unterstützt, damit Prüfer Evidence effizient finden und verifizieren können.

## 5-Schritte-Workflow

| Schritt | Aktion |
| --- | --- |
| **1. Umfang und KI-Inventar festlegen** | Umfang mit scope_ref definieren; KI-Systeme mit [Taxonomie](../../standard/current/03-taxonomy/) und [Dictionary](../../standard/current/05-dictionary/) klassifizieren. |
| **2. Managementsystem-Artefakte setzen** | Richtlinien, Rollen und PDCA-orientierte Artefakte anlegen oder referenzieren. [AIMO-MS / AIMO-Controls](../../conformance/) als Struktur; [Evidence Pack Template](../../standard/current/06-ev-template/) (EP-01..EP-07) referenzieren. |
| **3. Evidence Bundle + Mindestevidence erzeugen** | Manifest, object_index, payload_index, hash_chain, signing gemäß [Evidence Bundle-Struktur](../../standard/current/09-evidence-bundle-structure/) aufbauen. Request, review, exception, renewal, change_log gemäß [Mindestanforderungen an Evidence](minimum-evidence.md) einbeziehen. |
| **4. Validator + Checksums + Änderungskontrolle ausführen** | `python validator/src/validate.py <bundle_path> --validate-profiles` ausführen. Validator-Version und Ausgabe dokumentieren. SHA-256-Checksums erzeugen; Change-Log-Einträge pflegen, die betroffene Objekte referenzieren. |
| **5. Prüfpack vorbereiten** | Bundle verpacken (zip o. ä.); Checksums bereitstellen. Optional [Audit-Report-Ausgabe](../../standard/current/07-validator/) (audit-json / audit-html) anfügen. Bei Standardzitaten versionierte URLs (z. B. `/0.1.2/`) verwenden. Für Audit-Ready-Stufe [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) und [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) ergänzen. |

## Checkliste: ISO 42001 Klauselfamilie → AIMO-Artefakte → Evidence-Ausgaben

| ISO-42001-Klauselfamilie | AIMO-Artefakte | Evidence-Ausgaben |
| --- | --- | --- |
| Kontext (4.1) | Summary, Dictionary, scope_ref | manifest scope_ref; Summary; Dictionary |
| Führung / Politik (5.x) | Summary, review, dictionary | Prüfaufzeichnungen; Politikreferenzen |
| Planung (6.x) | request, review, exception, EV, Dictionary | Antrag/Genehmigung; Risiko/Ziele in EV oder Dictionary |
| Unterstützung (7.x) | Summary, review, EV, change_log | Dokumentation; Kompetenz-/Bewusstseinsnachweise |
| Betrieb (8.x) | EV, request, review, exception | operative Kontrollen; Anwendbarkeit |
| Bewertung (9.x) | EV, change_log, review, renewal | Überwachung; internes Audit; Managementreview |
| Verbesserung (10.x) | exception, renewal, change_log | Korrekturmaßnahmen; kontinuierliche Verbesserung |

Siehe [Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) und [ISO/IEC 42006](https://www.iso.org/standard/42006) für Erwartungen an Prüforganisationen.

## Sichere Formulierung

- **Verwenden:** „Wir nutzen AIMO-Artefakte zur Unterstützung der ISO/IEC 42001-Bereitschaft; Zertifizierungsentscheidungen obliegen akkreditierten Zertifizierungsstellen.“
- **Nicht verwenden:** „ISO 42001 zertifiziert durch AIMO“ oder „AIMO zertifiziert Konformität.“

Offizielle Norm (Primärquelle): [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) (ISO). Dieses Toolkit ist mit [Konformität](../../conformance/) und [Verantwortungsgrenze](../../governance/responsibility-boundary/) abgestimmt — AIMO zertifiziert nicht und garantiert keine Konformität.

## Verwandte Themen

- [Konformität](../../conformance/) — Stufen (Foundation, Operational, Audit-Ready) und Claim-Sprache
- [Trust Package](../../governance/trust-package/) — prüfergerechte Materialien
- [Responsibility Boundary](../../governance/responsibility-boundary/) — Was AIMO leistet und nicht leistet
