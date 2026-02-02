---
description: Schéma de journal de découverte de Shadow AI - Format neutre vis-à-vis des fournisseurs pour documenter la détection, l'inventaire et la remédiation de l'utilisation non approuvée de l'IA en entreprise.
---

# Schéma de journal de découverte de Shadow AI

## Objectif

Ce schéma définit un format neutre vis-à-vis des fournisseurs pour les journaux qui documentent la détection, l'inventaire et la remédiation de **l'utilisation non approuvée de l'IA (Shadow AI)**. Il permet aux organisations de :

- Maintenir un enregistrement auditable des événements de détection de Shadow AI
- Normaliser les journaux de diverses sources (CASB, proxy, IdP, EDR, journaux d'audit SaaS) dans un format cohérent
- Soutenir la soumission de preuves pour la conformité et les besoins d'audit

## Principes de normalisation

| Principe | Description |
| --- | --- |
| **Neutre vis-à-vis des fournisseurs** | Pas de dépendance aux formats de journaux de fournisseurs spécifiques ; applicable à Netskope, Zscaler, Microsoft Defender et autres |
| **Champs requis minimaux** | Seuls les champs essentiels sont OBLIGATOIRES ; les organisations peuvent omettre les champs optionnels |
| **Extensible** | `additionalProperties: true` permet des extensions spécifiques au fournisseur ou à l'organisation |
| **Conscient de la confidentialité** | Les champs sont conçus pour référencer (pas intégrer) le contenu sensible |

## Champs requis (OBLIGATOIRE)

| Champ | Type | Description | Exemple |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Horodatage de l'événement | `2026-01-15T09:30:00Z` |
| `actor_id` | string | Identifiant utilisateur ou service | `user@example.com` |
| `actor_type` | string | Type d'acteur | `user` ou `service` |
| `source_system` | string | Système qui a détecté l'événement | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | Produit ou domaine IA accédé | `chat.openai.com`, `claude.ai` |
| `action` | string | Action effectuée | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | Niveau de classification des données | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | Décision de politique appliquée | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Référence aux preuves associées | `sha256:abc123...` ou `urn:evidence:...` |
| `record_id` | string | Identifiant unique pour cet enregistrement | `evt-20260115-001` |

## Champs optionnels (DEVRAIT/PEUT)

| Champ | Type | Description |
| --- | --- | --- |
| `session_id` | string | Identifiant de session |
| `device_id` | string | Identifiant d'appareil |
| `ip` | string | Adresse IP |
| `user_agent` | string | Chaîne user agent |
| `department` | string | Département organisationnel |
| `project_id` | string | Identifiant de projet |
| `prompt_category` | string | Catégorie du prompt/requête |
| `model_family` | string | Famille de modèle IA (ex. GPT-4, Claude) |
| `destination` | string | URL ou endpoint de destination |
| `policy_id` | string | Politique qui a déclenché la décision |
| `remediation_ticket` | string | Référence du ticket de remédiation |

## Notes de confidentialité/sécurité

!!! warning "Traitement des données"
    - **Ne pas intégrer** de données personnelles, identifiants ou contenu de prompt directement dans les champs de journal.
    - Utilisez `evidence_ref` pour référencer du contenu sensible stocké séparément.
    - Appliquez des contrôles d'accès appropriés au stockage des journaux.
    - Considérez des politiques de rétention des données alignées avec les [exigences minimales de preuves](../minimum-evidence.md).

## Schéma JSON

Télécharger : [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## Pages connexes

- [Index des schémas de journaux](index.md)
- [Journal d'activité des agents](agent-activity.md)
- [Exigences minimales de preuves](../minimum-evidence.md)
- [Taxonomie : IM-007 Shadow/Non géré](../../standard/current/03-taxonomy.md)
