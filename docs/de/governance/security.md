---
description: AIMO Standard Sicherheitsrichtlinie - Schwachstellenmeldung, Offenlegungsverfahren und Sicherheitsüberlegungen für KI-Governance-Implementierungen.
---

# Sicherheit

Diese Seite dokumentiert die Sicherheitsrichtlinie für den AIMO Standard, einschließlich Schwachstellenmeldung und Offenlegungsverfahren.

## Geltungsbereich

### Im Geltungsbereich

- Validator-Referenzimplementierung (`validator/`)
- Build- und Release-Tooling (`tooling/`)
- JSON-Schemas (`schemas/`)
- Dokumentations-Website-Infrastruktur

### Außerhalb des Geltungsbereichs

- Spezifikationsinhalt (normativer Text ist kein Sicherheitsartefakt)
- Anwenderimplementierungen, die den AIMO Standard verwenden
- Externe Abhängigkeiten (an Upstream-Maintainer melden)

## Unterstützte Versionen

| Version | Unterstützt |
| ------- | --------- |
| latest (dev) | Ja |
| Getaggte Releases (vX.Y.Z) | Ja (neueste 2 Minor-Versionen) |
| Ältere Releases | Nein (Upgrade empfohlen) |

## Eine Schwachstelle melden

Eröffnen Sie **kein** öffentliches GitHub-Issue für Sicherheitsschwachstellen.

### Prozess

1. Privat über GitHubs private Schwachstellenmeldung melden
2. Enthalten: Beschreibung, Reproduktionsschritte, betroffene Versionen, Auswirkung
3. Zeit für Bewertung und Fix-Entwicklung einräumen

### Zeitplan

| Phase | Zeitplan |
| ----- | -------- |
| Bestätigung | 72 Stunden |
| Erstbewertung | 7 Tage |
| Koordinierte Offenlegung | maximal 90 Tage |

## Offenlegungsrichtlinie

1. Schwachstellen werden privat gemeldet
2. Fixes werden vor öffentlicher Offenlegung entwickelt
3. Sicherheitshinweise werden veröffentlicht, nachdem Fixes verfügbar sind
4. Melder werden genannt (außer bei Wunsch nach Anonymität)

## Sicherheitsmaßnahmen

- CI/CD-Prüfungen bei allen Änderungen
- Signierte Releases mit SHA-256-Prüfsummen
- Obligatorische PR-Überprüfung vor Merge

## Vollständige Richtlinie

Siehe [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) für die vollständige Sicherheitsrichtlinie.

## Verwandte Seiten

- [Trust Package](../trust-package/) — Prüfungsbereite Materialien
- [Governance](../) — Projekt-Governance
