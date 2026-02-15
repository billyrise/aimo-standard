---
description: Format de journal d'activité des agents - Schéma neutre vis-à-vis des fournisseurs pour l'exercice des privilèges d'IA agentique, l'exécution d'outils et la surveillance des opérations récursives en entreprise.
---
<!-- aimo:translation_status=translated -->

# Format de journal d'activité des agents

## Objectif

Ce schéma définit un format neutre vis-à-vis des fournisseurs pour les journaux qui documentent **l'exercice des privilèges d'IA agentique, l'exécution d'outils et les opérations récursives**. Il permet aux organisations de :

- Maintenir un enregistrement auditable des actions d'agents autonomes
- Suivre « qui a fait quoi avec quelle autorité » pour la conformité et l'investigation d'incidents
- Soutenir l'explicabilité des opérations d'IA agentique dans les contextes d'audit

## Modèle d'événement

Le schéma prend en charge quatre types d'événements qui capturent le cycle de vie des opérations agentiques :

| Type d'événement | Description |
| --- | --- |
| `agent_run` | Début ou fin d'une session d'exécution d'agent |
| `tool_call` | Agent invoquant un outil ou une action externe |
| `tool_result` | Résultat retourné par une invocation d'outil |
| `escalation` | Agent demandant une intervention humaine ou des privilèges élevés |

## Champs requis (OBLIGATOIRE)

| Champ | Type | Description | Exemple |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | Horodatage de l'événement | `2026-01-15T09:30:00Z` |
| `agent_id` | string | Identifiant de l'agent | `agent-coding-assistant-v2` |
| `agent_version` | string | Version de l'agent | `2.1.0` |
| `run_id` | string | Identifiant unique pour cette exécution/session | `run-20260115-abc123` |
| `event_type` | string | Type d'événement | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | Utilisateur ou service initiateur | `user@example.com` |
| `tool_name` | string | Nom de l'outil invoqué | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | Action effectuée par l'outil | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | Cible de l'action | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | Résumé permission/rôle | `role:developer, scope:project-x` |
| `input_ref` | string | Hash ou URI vers l'entrée (pas le contenu lui-même) | `sha256:def456...` |
| `output_ref` | string | Hash ou URI vers la sortie (pas le contenu lui-même) | `sha256:ghi789...` |
| `decision` | string | Décision de politique appliquée | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | Référence aux preuves associées | `urn:evidence:...` |

## Champs optionnels (DEVRAIT/PEUT)

| Champ | Type | Description |
| --- | --- | --- |
| `recursion_depth` | number | Profondeur de récursion actuelle pour les appels d'agents imbriqués |
| `retry_count` | number | Nombre de tentatives pour cette action |
| `policy_id` | string | Politique qui a déclenché la décision |
| `prompt_template_id` | string | Identifiant du modèle de prompt |
| `model` | string | Modèle utilisé pour cette action |
| `latency_ms` | number | Latence en millisecondes |
| `cost_estimate` | number | Coût estimé de cette action |
| `error_code` | string | Code d'erreur si l'action a échoué |

## Notes de sécurité

!!! warning "Hypothèses de risque agentique"
    Lors de la journalisation de l'activité d'IA agentique, supposez les risques suivants :

    - **Injection de prompt** : Des entrées malveillantes peuvent tenter de manipuler le comportement de l'agent
    - **Sur-privilège** : Les agents peuvent avoir des permissions plus larges que prévu pour une tâche spécifique
    - **Boucles récursives** : Les agents peuvent entrer dans des schémas d'exécution récursifs non intentionnels
    - **Confused deputy** : Les agents peuvent être trompés pour agir au nom de parties non autorisées

    Le schéma est conçu pour capturer « qui a fait quoi avec quelle autorité » pour soutenir l'analyse post-incident et les explications d'audit. Il ne prévient pas ces risques ; les organisations doivent mettre en place des garde-fous appropriés.

!!! warning "Traitement des données"
    - **Ne pas intégrer** de secrets, identifiants ou contenu sensible dans `input_ref` ou `output_ref`.
    - Utilisez des références de hash ou des URI sécurisés vers du contenu stocké séparément.
    - Appliquez des contrôles d'accès et des politiques de rétention appropriés.

## Schéma JSON

Télécharger : [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "agent_id", "agent_version", "run_id", "event_type",
    "actor_id", "tool_name", "tool_action", "tool_target", "auth_context",
    "input_ref", "output_ref", "decision", "evidence_ref"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "agent_id": { "type": "string", "minLength": 1 },
    "agent_version": { "type": "string", "minLength": 1 },
    "run_id": { "type": "string", "minLength": 1 },
    "event_type": { "type": "string", "enum": ["agent_run", "tool_call", "tool_result", "escalation"] },
    "actor_id": { "type": "string", "minLength": 1 },
    "tool_name": { "type": "string", "minLength": 1 },
    "tool_action": { "type": "string", "minLength": 1 },
    "tool_target": { "type": "string", "minLength": 1 },
    "auth_context": { "type": "string", "minLength": 1 },
    "input_ref": { "type": "string", "minLength": 1 },
    "output_ref": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## Pages connexes

- [Index des schémas de journaux](../)
- [Journal de découverte de Shadow AI](../shadow-ai-discovery/)
- [Exigences minimales de preuves](../../minimum-evidence/)
- [Taxonomie : UC-010 Automatisation agentique](../../../standard/current/03-taxonomy/)
