---
description: Coverage Map Methodologie - Wie AIMO externen Frameworks zugeordnet wird. Verwendung in Audits, Beziehung zum Evidence Bundle und Nachverfolgbarkeitsansatz.
---

# Methodologie

> Hinweis: Diese Methodologie unterstützt Nachverfolgbarkeit und Evidence-Bereitschaft. Sie garantiert keine Compliance mit einer bestimmten Vorschrift/einem Standard.

Diese Seite erklärt, was die Coverage Map ist und nicht ist, wie sie im Audit verwendet wird und wie sie sich auf das Evidence Bundle und die Mindestanforderungen an Evidence bezieht.

## Was die Zuordnung ist

- Eine **informative** Zuordnung von externen Framework-/Vorschriftsreferenzen (nach Thema) zu AIMO Evidence, Evidence Bundle TOC-Elementen, Mindestanforderungen-Lifecycle-Gruppen, Artefakten und Validator-Prüfungen.
- Ein Unterstützungswerkzeug für **Erklärbarkeit**: welches AIMO Evidence und welche Artefakte helfen können, die Ausrichtung an einer gegebenen externen Anforderung zu demonstrieren oder zu erklären (ohne Konformität zu beanspruchen).

## Was die Zuordnung nicht ist

- **Keine** Garantie für Compliance mit einem Framework oder einer Vorschrift.
- **Keine** Rechtsberatung oder Ersatz für die Überprüfung gegen maßgebliche Texte.
- **Nicht** erschöpfend; es ist eine praktische Teilmenge für Audit-Bereitschaft und Erklärbarkeit.

## Verwendung im Audit

Verwenden Sie den Ablauf: **Anforderung → Evidence → Artefakt → Validierung**.

1. **Anforderung**: Identifizieren Sie die externe Framework-Referenz und das Thema (z.B. ISO 42001-Dokumentation, EU AI Act-Aufzeichnungspflichten).
2. **Evidence**: Sehen Sie, welche AIMO Evidence Bundle-Elemente und Mindestanforderungen-Lifecycle-Gruppen (request, review, exception, renewal, change_log, integrity) die Erklärbarkeit für diese Anforderung unterstützen.
3. **Artefakt**: Lokalisieren Sie die Artefakte (Schemas, Templates, Beispiele), die dieses Evidence implementieren oder illustrieren.
4. **Validierung**: Verwenden Sie den Validator und die referenzierten Schema-Prüfungen, um strukturelle Konsistenz zu verifizieren.

Leser müssen gegen den maßgeblichen Text jedes Frameworks oder jeder Vorschrift prüfen.

## Beziehung zum Evidence Bundle und Mindestanforderungen an Evidence

- **[Evidence Bundle](../artifacts/evidence-bundle.md)**: Definiert die Bundle-Struktur, TOC und Nachverfolgbarkeit. Coverage Map-Zeilen referenzieren Evidence Bundle-Abschnitte (z.B. EV, Dictionary, Summary, change_log, request, review, exception, renewal).
- **[Mindestanforderungen an Evidence](../artifacts/minimum-evidence.md)**: Definiert MUSS-Lifecycle-Gruppen (request, review, exception, renewal, change_log, integrity). Coverage Map-Zeilen referenzieren diese Gruppen in `minimum_evidence_refs`.

Verwenden Sie die Coverage Map, um zu sehen, welche Evidence Bundle-Elemente und Mindestanforderungen-Gruppen die Erklärbarkeit für eine gegebene externe Anforderung unterstützen.

## Keine-Überbeanspruchung-Erklärung

!!! warning "Wichtig"
    Der AIMO Standard unterstützt **Erklärbarkeit und Evidence-Bereitschaft**. Er bietet **keine** Rechtsberatung, garantiert keine Compliance und zertifiziert keine Konformität mit einer Vorschrift oder einem Framework. Anwender müssen Ansprüche gegen maßgebliche Texte prüfen und bei Bedarf professionelle Beratung einholen.

Siehe [Verantwortungsgrenze](../governance/responsibility-boundary.md) für Umfang, Annahmen und Anwenderverantwortlichkeiten.

## Audit-Reise

Von dieser Seite aus weiter zu:

1. **Framework-Zuordnungen**: [ISO 42001](iso-42001.md), [NIST AI RMF](nist-ai-rmf.md), [EU AI Act](eu-ai-act.md), [ISMS](isms.md)
2. **Validieren**: [Validator](../validator/index.md) — strukturelle Prüfungen durchführen
3. **Download**: [Releases](../releases/index.md) — Release-Assets herunterladen
