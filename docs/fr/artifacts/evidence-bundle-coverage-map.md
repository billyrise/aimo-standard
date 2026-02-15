---
description: Modèle de carte de couverture du lot de preuves (v0.1). Résumé informatif d'une page pour les auditeurs — périmètre, types de preuves, correspondance des contrôles, exclusions, preuve d'intégrité.
---
<!-- aimo:translation_status=translated -->

# Carte de couverture du lot de preuves (Modèle)

!!! info "Informatif — pratique recommandée"
    Cette page définit un **modèle de pratique recommandée** pour une carte de couverture du lot de preuves sur une page. Ce **n'est pas** une exigence normative du standard. Utilisez-la pour documenter ce qu'un lot couvre et ne couvre pas pour la transmission aux auditeurs. Les références (p. ex. aux cadres) sont stables ; l'adoption est à la discrétion de l'implémenteur.

---

## 1. Périmètre

| Élément | Description |
|------|--------------|
| **Référence de périmètre** | `scope_ref` du manifeste du lot (ex. `SC-001`). Lie ce lot au périmètre déclaré. |
| **ID du lot** | `bundle_id` (UUID) — identifiant unique de ce lot. |
| **Version du lot** | `bundle_version` (SemVer) — version du lot. |
| **Période / instantané** | Optionnel : période ou date d'instantané que ce lot représente (ex. 2026-Q1, as-of 2026-02-03). |

---

## 2. Types de preuves (EV / objects vs payloads)

| Catégorie | Contenu | Exemple minimal v0.1 |
|----------|----------|------------------------|
| **object_index** | Objets énumérés (métadonnées, index). Chaque entrée : `id`, `type`, `path`, `sha256`. | ex. `objects/index.json` (type index). |
| **payload_index** | Fichiers de charge (EV JSON racine, fichiers Evidence Pack). Chaque entrée : `logical_id`, `path`, `sha256`, `mime`, `size`. | ex. `payloads/root.json` (EV JSON racine AIMO). |
| **Types EV** | Enregistrements de preuves (dans la racine ou les charges liées) — request, review, exception, renewal, change log. | Aligné avec le [modèle Evidence Pack](../../standard/current/06-ev-template/) et les [Exigences minimales de preuves](../minimum-evidence/). |

*Les implémenteurs peuvent étendre object_index et payload_index ; les chemins DOIVENT rester dans la racine du lot et satisfaire la [structure racine du lot de preuves (v0.1)](../../standard/current/09-evidence-bundle-structure/).*

---

## 3. Correspondance des contrôles (référence uniquement)

La correspondance avec les cadres externes est **à titre de référence uniquement** ; le standard n'impose la conformité à aucune réglementation spécifique.

| Cadre | Utilisation dans ce lot | Référence |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | Optionnel : documenter quels thèmes AI MS ce lot prend en charge. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | Optionnel : alignement documentation/tenue de registres de haut niveau. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | Optionnel : correspondance Govern, Map, Measure, Manage. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | Optionnel : Model Documentation Form ; joindre dans External Forms, référencer par logical_id. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) ; profil `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | Optionnel : artefacts du profil GenAI (AI 600-1). | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) ; profil `nist_ai_600_1_genai.json` |
| **UK ATRS** | Optionnel : enregistrement ATRS, évaluation des marchés. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) ; profil `uk_atrs_procurement.json` |
| **JP Gov GenAI marchés** | Optionnel : liste de contrôle des marchés JP, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/) ; profil `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | Optionnel : gestion des changements, accès, journalisation, intégrité. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*Remplir « Utilisation dans ce lot » par soumission ; le standard n'exige aucune couverture de contrôle spécifique.*

### External Forms et référence au manifeste

**External Forms** (modèles/listes de contrôle officiels joints tels quels) doivent être listés dans le **payload_index** du lot avec un `logical_id`, `path`, `sha256`, `mime` et `size` stables. Les auditeurs peuvent alors tracer du manifeste au fichier et vérifier le hachage. Voir [Modèle EV — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) et [Modèle EV — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index).

---

## 4. Exclusions / hypothèses

| Domaine | Ce que ce lot **ne** couvre **pas** (lignes d'exemple — adapter par soumission) |
|------|-------------------------------------------------------------------------------|
| **Exclusions** | ex. Systèmes ou cas d'usage hors périmètre ; composants tiers non prouvés ; période hors de ce lot. |
| **Hypothèses** | ex. Version Dictionary/taxonomie ; version validateur/schéma utilisée ; la custodie et la conservation sont définies par l'implémentation. |
| **Limitations** | ex. La vérification des signatures est hors périmètre en v0.1 ; aucune interprétation juridique des réglementations. |

*Remplacer le texte placeholder par des exclusions et hypothèses spécifiques à la soumission.*

---

## 5. Résumé de la preuve d'intégrité (v0.1)

| Élément | Ce qui est fourni (v0.1 normatif) |
|---------|----------------------------------|
| **manifest.json** | Présent et valide au schéma ; inclut `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Chaque fichier dans `object_index` et `payload_index` a un sha256 hex minuscule de 64 caractères déclaré ; le validateur vérifie la correspondance du contenu. |
| **Existence des index** | Tous les chemins listés existent sous la racine du lot ; pas de traversée de chemin (`../` ou `/` en tête). |
| **Existence des signatures** | Au moins un fichier de signature dans `signatures/` ; le manifeste le référence via `signing.signatures[]` avec `path` et `targets` (v0.1 DOIT inclure `manifest.json` dans targets). La vérification cryptographique est hors périmètre en v0.1. |
| **Chaîne de hachage** | `hash_chain` dans le manifeste : `algorithm`, `head` (64 caractères hex), `path` (fichier sous `hashes/`), `covers` (v0.1 DOIT inclure `manifest.json` et `objects/index.json`). Le fichier à `hash_chain.path` existe. |

*Ce tableau résume les garanties d'intégrité que le [Validateur](../../validator/) vérifie pour les lots v0.1. La custodie (stockage, contrôle d'accès, conservation) est définie par l'implémentation.*

---

## Coverage Map (YAML) vs Profils (JSON)

| Artefact | Statut | Objectif |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` ou similaire) | **Informatif** | Thèmes de correspondance de haut niveau entre preuves/artefacts AIMO et cadres externes (ISO 42001, NIST AI RMF, EU AI Act, etc.) pour l'explicabilité. Il n'impose pas d'exigences de validation normatives. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normatif** | Spécifications de conversion validées contre `schemas/jsonschema/aimo-profile.schema.json`. Ils définissent des correspondances lisibles par machine (ex. quels objets AIMO correspondent à quelles clauses de cadre). Le [Validateur](../../validator/) exécute `--validate-profiles` pour s'assurer que tous les profile JSON officiels sont conformes au schéma (modèle profile_id PR-*, énumération target, target_version, mappings). |

### Profils officiels (validés par le validateur)

Les Profile JSON se trouvent dans `coverage_map/profiles/` et sont validés par le validateur (`--validate-profiles`). Nommage : nom de fichier `<target>_<purpose>.json` ; chacun inclut `target_version`.

| Fichier | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### Politique de mise à jour des profils

- **Réfs EU AI Act (0.1.2)** : Les références aux articles de l'EU AI Act dans la carte de couverture et la documentation ont été alignées sur le Règlement (UE) 2024/1689 pour une préparation des preuves cohérente ; informatif uniquement, pas d'avis juridique.
- **ISO 42001 / NIST AI RMF** : De nouvelles versions du cadre cible peuvent être ajoutées sous forme de nouveaux fichiers de profil ou de nouvelles valeurs `target_version` dans une future version du standard ; les profils v0.1 restent figés pour la release v0.1.
- **EU AI Act Annex IV** : L'Annexe IV et les articles connexes peuvent être mis à jour par les régulateurs ; les correspondances de profils peuvent être mises à jour via **PATCH** (ex. 0.1.x) pour suivre les changements de libellé ou de clause tout en conservant le même profile_id pour la continuité. Les implémenteurs doivent s'aligner sur la version référencée dans la `target_version` du profil et les notes de release.

---

## Voir aussi

- [Lot de preuves (aperçu des artefacts)](../evidence-bundle/)
- [Structure racine du lot de preuves (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Exigences minimales de preuves](../minimum-evidence/)
- [Coverage Map (correspondances de cadres)](../../coverage-map/)
- [Validateur](../../validator/)
