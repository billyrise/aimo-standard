---
description: AIMO Standard Beitragsleitfaden - Wie man Code, Dokumentation und Übersetzungen beiträgt. Issue- und PR-Richtlinien.
---

# Beitragen

Diese Seite bietet Richtlinien für Beiträge zum AIMO Standard.

## Schnellstart

1. Repository forken
2. Feature-Branch erstellen
3. Änderungen gemäß den folgenden Richtlinien vornehmen
4. Qualitätsprüfungen ausführen
5. Pull Request einreichen

## Grundprinzipien

| Prinzip | Beschreibung |
| --------- | ----------- |
| Englisch ist kanonisch | Zuerst `docs/en/` bearbeiten, dann `docs/ja/` aktualisieren |
| SSOT | Dieses Repository ist die einzige Quelle der Wahrheit |
| Keine manuellen Bearbeitungen generierter Dateien | Quellen bearbeiten, regenerieren, committen |
| Alle Änderungen via PR | Auch Maintainer verwenden Pull Requests |

## Qualitätsprüfungen

Vor dem Einreichen eines PRs ausführen:

```bash
# Virtuelle Umgebung aktivieren
source .venv/bin/activate

# Lints ausführen
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Dokumentation erstellen
mkdocs build --strict
```

## Änderungstypen

| Typ | Beispiele | Review-Anforderungen |
| ---- | -------- | ------------------- |
| Normativ | Schema-Änderungen, Anforderungen | Maintainer + Diskussion |
| Nicht-normativ | Tippfehler, Klarstellungen | Maintainer-Genehmigung |
| i18n | Übersetzungen | Struktur muss EN entsprechen |
| Tooling | CI/CD, Skripte | Maintainer-Genehmigung |

## i18n-Richtlinien

### Update-Reihenfolge

1. Englische Quelle bearbeiten (`docs/en/...`)
2. Japanische Übersetzung aktualisieren (`docs/ja/...`)
3. `lint_i18n.py` ausführen, um Konsistenz zu überprüfen
4. Beide zusammen committen

### Strukturanforderungen

- Gleiche Dateinamen in beiden Sprachen
- Gleiche Überschriftenhierarchie
- Gleiche Seitenanzahl pro Abschnitt

## PR-Checkliste

Beim Einreichen eines PRs überprüfen:

- [ ] Änderungstyp identifiziert (docs / schema / examples / tooling)
- [ ] Breaking-Change-Bewertung abgeschlossen
- [ ] i18n: EN und JA zusammen aktualisiert (falls zutreffend)
- [ ] Qualitätsprüfungen bestanden
- [ ] Verwandte Issues verknüpft

## Breaking Changes

Breaking Changes erfordern:

1. Issue-Diskussion vor der Implementierung
2. Versionserhöhung gemäß [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Changelog-Eintrag mit Migrationsanleitung

## Konformitätsanspruchs-Updates

Um Konformitätsansprüche hinzuzufügen oder zu ändern:

1. Coverage Map YAML aktualisieren
2. Entsprechende Dokumentationsseiten aktualisieren
3. Validator-Tests ausführen
4. Zuordnungsbegründung dokumentieren

## Vollständige Richtlinien

Siehe [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) für den Leitfaden auf Root-Ebene.

## Verwandte Seiten

- [Governance](index.md) — Projekt-Governance
- [Lokalisierungsleitfaden](../contributing/localization.md) — i18n-Details
- [Verantwortungsgrenze](responsibility-boundary.md) — Was AIMO bereitstellt
