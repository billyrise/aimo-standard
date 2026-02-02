---
description: Politique de sécurité du standard AIMO - Signalement de vulnérabilités, procédures de divulgation et considérations de sécurité pour les implémentations de gouvernance IA.
---

# Sécurité

Cette page documente la politique de sécurité pour le standard AIMO, y compris le signalement de vulnérabilités et les procédures de divulgation.

## Périmètre

### Dans le périmètre

- Implémentation de référence du validateur (`validator/`)
- Outillage de build et de release (`tooling/`)
- Schémas JSON (`schemas/`)
- Infrastructure du site de documentation

### Hors périmètre

- Contenu de spécification (le texte normatif n'est pas un artefact de sécurité)
- Implémentations des adopteurs utilisant le standard AIMO
- Dépendances externes (signaler aux mainteneurs amont)

## Versions supportées

| Version | Supportée |
| ------- | --------- |
| latest (dev) | Oui |
| Versions taguées (vX.Y.Z) | Oui (2 dernières versions mineures) |
| Anciennes versions | Non (mise à niveau recommandée) |

## Signaler une vulnérabilité

**Ne pas** ouvrir une issue GitHub publique pour les vulnérabilités de sécurité.

### Processus

1. Signaler en privé via le signalement de vulnérabilité privé de GitHub
2. Inclure : description, étapes de reproduction, versions affectées, impact
3. Laisser le temps pour l'évaluation et le développement du correctif

### Délais

| Phase | Délai |
| ----- | -------- |
| Accusé de réception | 72 heures |
| Évaluation initiale | 7 jours |
| Divulgation coordonnée | 90 jours max |

## Politique de divulgation

1. Les vulnérabilités sont signalées en privé
2. Les correctifs sont développés avant la divulgation publique
3. Les avis de sécurité sont publiés après que les correctifs sont disponibles
4. Les rapporteurs sont crédités (sauf si l'anonymat est demandé)

## Mesures de sécurité

- Vérifications CI/CD sur tous les changements
- Versions signées avec checksums SHA-256
- Revue PR obligatoire avant merge

## Politique complète

Voir [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) pour la politique de sécurité complète.

## Pages connexes

- [Package de confiance](trust-package.md) — Matériaux prêts pour les auditeurs
- [Gouvernance](index.md) — Gouvernance du projet
