---
description: Mapeamento AIMO Standard para NIST AI RMF. Rastreabilidade entre códigos de taxonomia AIMO e funções do NIST AI Risk Management Framework.
---
<!-- aimo:translation_status=translated -->

# Mapeamento NIST AI RMF

> Atalhos de rastreabilidade: Taxonomia → Requisitos Mínimos de Evidências → Validador → Protocolo de Supervisão Humana.

- [Taxonomia](../../standard/current/03-taxonomy/)
- [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/)
- [Schemas de Log](../../artifacts/log-schemas/)
- [Validador](../../validator/)
- [Protocolo de Supervisão Humana](../../governance/human-oversight-protocol/)

Esta página mapeia temas selecionados do NIST AI Risk Management Framework (Govern, Map, Measure, Manage) para evidências e artefatos AIMO. É apenas para explicabilidade; não garante conformidade com o NIST AI RMF. Verifique contra a publicação do NIST.


## Tabela de mapeamento

| Referência do framework / tópico | Evidência AIMO / onde no AIMO | Pacote de Evidências / Requisitos Mínimos de Evidências | Artefatos e validação | Notas |
| --- | --- | --- | --- | --- |
| Govern 1.1 – Políticas | [Escopo](../../standard/current/02-scope/), [Taxonomia](../../standard/current/03-taxonomy/) | Dictionary, Summary, review; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicação NIST. |
| Govern 1.2 – Papéis e responsabilidades | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | request, review | templates/ev/ev_template.md | Informativo; verifique contra publicação NIST. |
| Govern 2.1 – Responsabilização | [Pacote de Evidências](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Informativo; verifique contra publicação NIST. |
| Govern 3.1 – Gestão de riscos | [Escopo](../../standard/current/02-scope/) | request, review, exception | templates/ev/ | Informativo; verifique contra publicação NIST. |
| Govern 4.1 – Cultura | [Visão Geral](../../standard/current/01-overview/) | Summary, review; review | — | Informativo; verifique contra publicação NIST. |
| Map 1.1 – Mapeamento de contexto | [Escopo](../../standard/current/02-scope/), [Dicionário](../../standard/current/05-dictionary/) | Dictionary, Summary; request | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicação NIST. |
| Map 2.1 – Dados e documentação | [Template EV](../../standard/current/06-ev-template/) | EV, Dictionary, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra publicação NIST. |
| Map 3.1 – Governança de dados | [Dicionário](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra publicação NIST. |
| Measure 1.1 – Desempenho e impacto | [Template EV](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra publicação NIST. |
| Measure 2.1 – Monitoramento | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | Informativo; verifique contra publicação NIST. |
| Measure 3.1 – Teste e validação | [Validador](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verifique contra publicação NIST. |
| Manage 1.1 – Alocação de recursos | [Visão Geral](../../standard/current/01-overview/) | Summary, review; review | — | Informativo; verifique contra publicação NIST. |
| Manage 2.1 – Incidentes e respostas | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | exception, renewal, change_log | templates/ev/ev_template.md | Informativo; verifique contra publicação NIST. |
| Manage 3.1 – Gestão de mudanças | [Pacote de Evidências](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verifique contra publicação NIST. |
| Manage 4.1 – Revisão e atualização | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | renewal, review; review, renewal | templates/ev/ | Informativo; verifique contra publicação NIST. |
| Manage 5.1 – Comunicação | [Pacote de Evidências](../../artifacts/evidence-bundle/) | Summary, change_log; change_log | templates/ev/ | Informativo; verifique contra publicação NIST. |
