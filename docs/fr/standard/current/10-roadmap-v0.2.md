---
description: Feuille de route informative pour v0.2. SSOT des objets d'audit, Evidence-as-Code, profils de sortie, bibliothèque de tests, cycle de vie, JNC.
---
<!-- aimo:translation_status=translated -->

# Feuille de route v0.2 (informatif)

Cette page résume les orientations prévues pour une **future version majeure** (v0.2). Elle est **informatif uniquement** ; la spécification normative de toute version est la norme et les schémas de cette version. Calendrier cible : 2026 T4–2027.

## Thèmes prévus

| Thème | Résumé |
| --- | --- |
| **Modèle d'objets d'audit (SSOT)** | Requirement, Control, Claim, Evidence, Test, Finding, Remediation, Approval, Scope, VersionChange comme objets normatifs avec IDs fixes et intégrité référentielle. |
| **Pont vers cadres externes** | Profils de sortie pour Annexe IV UE, formulaire GPAI, ISO 42001, NIST AI RMF ; correspondance lisible par machine et export en un clic optionnel. |
| **Evidence-as-Code** | Intégrité normative : vérification des signatures, provenance (p. ex. style SLSA), reproductibilité et suivi des changements. |
| **Bibliothèque de procédures de test** | Modèles de test standard par contrôle ; alignement avec ISAE 3000, SOC 2, ISO 19011. |
| **Cycle de vie opérationnel** | Processus piloté par les événements (Intake → Review → Exception → Renewal → Change → Decommission) avec journaux et preuves requis. |
| **Profils secteur / juridiction** | Profils optionnels par secteur et juridiction. |
| **Non-conformité justifiée (JNC)** | Mécanisme optionnel pour enregistrer et justifier la non-conformité intentionnelle (informatif). |
| **Liaison OSCAL** | Méthode standard pour lier le Paquet de preuves à Control/Requirement pour l'export vers NIST OSCAL ou similaire. |

## Références

- [Périmètre du modèle d'objets v0.1](https://github.com/billyrise/aimo-standard/blob/main/source_pack/07_release/v0.1_object_model_scope.md) — MUST v0.1 vs. réservé
- [Feuille de route de vérification des signatures](../../../artifacts/signature-verification-roadmap/) — évolution de la signature et de la vérification
- [Releases](../../../releases/) — ressources de version et changelog
