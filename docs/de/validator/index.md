---
description: AIMO Validator-Hub - Validierungstools-Schnellstart. Installation, Ausführung und Ergebnisinterpretation in 30 Sekunden. Evidence Pack-Validierung und Compliance-Prüfungen.
---
<!-- aimo:translation_status=translated -->

# Validator

Diese Seite ist ein Hub für Validierungstools und Regeln. Die normative Spezifikation für den Validator und seine Regeln befindet sich im Standard.

## Schnellstart (30 Sekunden)

**1. Voraussetzungen**

```bash
pip install jsonschema   # falls noch nicht installiert
```

**2. Validierung gegen ein Beispiel-Bundle ausführen**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Bericht lesen und Fehler/Warnungen beheben**

Beispielausgabe (Erfolg):

```
OK
```

Beispielausgabe (Fehlschlag):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Exit-Codes: `0` = Erfolg, `1` = Validierungsfehler, `2` = Nutzungsfehler.

---

## Was geprüft wird

- **Schema-Validierung**: Root-Objekt, Dictionary und Evidence entsprechen JSON Schema
- **Dictionary-Konsistenz**: Alle Codes existieren im Taxonomie-Dictionary
- **Code-Status**: Warnt bei veralteten Codes, Fehler bei entfernten Codes

## Was NICHT geprüft wird

- **Inhaltsgenauigkeit**: Der Validator prüft Struktur, nicht Bedeutung
- **Compliance-Garantie**: Bestandene Validierung garantiert keine regulatorische Compliance
- **Menschliche Beurteilung**: Kontextabhängige Entscheidungen erfordern menschliche Überprüfung (siehe [Human Oversight Protocol](../governance/human-oversight-protocol/))
- **Automatische Log-Sammlung**: Der Validator validiert eingereichte Evidence; er sammelt keine Logs

---

## Ressourcen

- **Spezifikation**: [Standard > Aktuell > Validator](../standard/current/07-validator/) — Regeln, Referenzprüfungen und wie Validierung sich auf Evidence bezieht.
- **Regeln und Implementierung**: Repository `validator/rules/` (Prüfungen), `validator/src/` (Referenzimplementierung). Ausführung und CI-Nutzung sind in der Spezifikation beschrieben.
- **Interpretation**: Was ein Validierungs-"Fehlschlag" für Prüfer bedeutet (in der Spezifikation erklärt).

Für Konformität und Artefakt-Nutzung siehe [Konformität](../conformance/) und [Artefakte](../artifacts/).
