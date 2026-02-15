---
description: AIMO Log Schemas - Herstellerneutrale Log-Formate für KI-Evidence. Beinhaltet Shadow AI-Erkennung und Agentenaktivitätsüberwachungs-Schemas.
---
<!-- aimo:translation_status=translated -->

# Log Schemas

## Was ist das

Dieser Abschnitt definiert **normalisierte Log-Formate** für Evidence, das in einem Evidence Bundle enthalten sein kann. Diese Schemas bieten eine herstellerneutrale Struktur für Protokolle im Zusammenhang mit KI-Nutzungsüberwachung und agentenbasierten Operationen.

## Wann zu verwenden

- **Shadow AI-Sichtbarkeit**: Dokumentation von Erkennung, Inventarisierung und Behebung nicht genehmigter KI-Nutzung.
- **Agentenbasierte Operationsaudits**: Erklärung von autonomer Agentenberechtigungsausübung, Tool-Ausführung und rekursiven Operationen.
- **Incident-Reproduzierbarkeit**: Bereitstellung strukturierter Evidence für Incident-Untersuchung und Ursachenanalyse.

## Was es NICHT ist

!!! warning "Wichtig"
    Diese Schemas definieren **Log-Formate für die Evidence-Einreichung**. Sie:

    - Sammeln NICHT automatisch Protokolle aus Ihren Systemen
    - Stellen KEINE Log-Aggregations- oder Überwachungstools bereit
    - Garantieren KEINE Compliance mit Vorschriften oder Standards
    - Ersetzen KEINE herstellerspezifischen Protokollierungsimplementierungen

    Organisationen müssen ihre eigenen Log-Sammelpipelines implementieren und Protokolle für die Evidence-Einreichung auf diese Schemas normalisieren.

## Schemas

| Schema | Zweck | Download |
| --- | --- | --- |
| [Shadow AI Discovery Log](shadow-ai-discovery/) | Erkennung und Inventarisierung nicht genehmigter KI-Nutzung | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [Agent Activity Log](agent-activity/) | Agentenbasierte KI-Berechtigungsausübung und Tool-Ausführung | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## Verwandte Seiten

- [Mindestanforderungen an Evidence](../minimum-evidence/) — MUSS-Evidence-Checkliste
- [Evidence Bundle](../evidence-bundle/) — Bundle-Struktur und TOC
- [Taxonomie](../../standard/current/03-taxonomy/) — Klassifizierungscodes (einschließlich UC-010 Agentic Automation, IM-007 Shadow/Unmanaged)
