---
description: Aperçu d'AIMO Standard. Définit la taxonomie partagée, le système de codes, le dictionnaire, les modèles de preuve et les contrôles du Validateur pour les audits de gouvernance IA.
---
<!-- aimo:translation_status=translated -->

# Aperçu（Overview）

**AIMO** signifie **AI Management Office**. AIMO Standard définit :
- une taxonomie partagée
- un système de codes
- un dictionnaire initial
- un modèle EV
- des contrôles du Validateur (spécification + implémentation de référence minimale)

Ce dépôt publie :
- une spécification lisible (HTML)
- des artefacts lisibles par machine (schémas/modèles/exemples)
- des versions PDF officielles

## Positionnement : complément à ISO/IEC 42001 (AIMS)

AIMO Standard est un **accélérateur d’implémentation pour la préparation des preuves et l’explicabilité**, utilisable pour soutenir les systèmes de management de l’IA (AIMS) alignés sur ISO/IEC 42001 et pour structurer des preuves prêtes pour l’audit. Il ne remplace pas ISO/IEC 42001 ni toute autre norme de système de management ; il ajoute une taxonomie, une structure Evidence Bundle et une Coverage Map qui aident à opérationnaliser et à prouver ces contrôles.

**Ce qu’AIMO fournit**

- Taxonomie et système de codes pour la classification de la gouvernance IA
- Structure Evidence Bundle (manifest, object_index, payload_index, intégrité)
- Validateur et Coverage Map pour la traçabilité
- Niveaux de conformité (Foundation, Operational, Audit-Ready) — niveaux de maturité propres à AIMO pour le conditionnement des preuves

**Ce qu’AIMO ne fournit pas**

- Conseil juridique
- Certification ISO ou substitut à la certification
- Garantie de conformité réglementaire
- Substitut au jugement de l’auditeur ou aux organismes de certification accrédités

**Pourquoi maintenant**

- **ISO/IEC 42006** (publiée juillet 2025) spécifie les exigences pour les organismes qui audient et certifient les systèmes de management de l’IA selon ISO/IEC 42001, renforçant les attentes en matière de preuves auditable et de traçabilité.
- L’**EU AI Act** est en application progressive (2025–2027) ; les normes harmonisées, une fois publiées au Journal officiel, fourniront une présomption de conformité. L’EU AI Office prépare des lignes directrices pratiques en 2026 (classification à haut risque, transparence Art. 50, incidents, éléments QMS).
- Les adoptants et organismes de certification utilisent de plus en plus ISO/IEC 42001 comme couche système pour la gouvernance IA ; AIMO aide à structurer les preuves qui soutiennent cette couche sans revendiquer de certification.

## Références

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — Exigences pour les organismes qui audient et certifient les systèmes de management de l’IA
- [Calendrier d’application de l’EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) (Service de la loi sur l'IA de la Commission européenne ; source primaire)
- [European Commission — Clear guidelines for AI (4 déc. 2025)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — Préparation des lignes directrices de l’AI Office (vérifier l’actualité Commission pour l’URL)
- [EPRS — EU AI Act implementation timeline (juin 2025)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — Briefing Parlement (informatif)
