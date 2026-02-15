---
description: Mapeamento AIMO Standard para ISMS (ISO 27001/27002). Rastreabilidade entre taxonomia AIMO e controles de sistema de gestão de segurança da informação.
---
<!-- aimo:translation_status=translated -->

# Mapeamento visão ISMS (ISO/IEC 27001/27002)

> Atalhos de rastreabilidade: Taxonomia → Requisitos Mínimos de Evidências → Validador → Protocolo de Supervisão Humana.

- [Taxonomia](../../standard/current/03-taxonomy/)
- [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/)
- [Schemas de Log](../../artifacts/log-schemas/)
- [Validador](../../validator/)
- [Protocolo de Supervisão Humana](../../governance/human-oversight-protocol/)

Esta página mapeia temas selecionados ISO/IEC 27001/27002 (gestão de mudanças, controle de acesso, logging, integridade de evidências) para evidências e artefatos AIMO. É apenas para explicabilidade; não garante conformidade com ISO/IEC 27001 ou 27002. Verifique contra os padrões publicados.


## Tabela de mapeamento

| Referência do framework / tópico | Evidência AIMO / onde no AIMO | Pacote de Evidências / Requisitos Mínimos de Evidências | Artefatos e validação | Notas |
| --- | --- | --- | --- | --- |
| A.5.24 – Segurança da informação em gestão de projetos | [Escopo](../../standard/current/02-scope/) | request, review | templates/ev/ | Informativo; verifique contra texto oficial. |
| A.5.29 – Segurança da informação durante interrupção | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | exception, renewal | templates/ev/ev_template.md | Informativo; verifique contra texto oficial. |
| A.5.30 – Prontidão de TIC para continuidade de negócios | [Visão Geral](../../standard/current/01-overview/) | Summary; integrity | — | Informativo; verifique contra texto oficial. |
| A.8.1 – Inventário de ativos | [Dicionário](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra texto oficial. |
| A.8.2 – Classificação de informação | [Taxonomia](../../standard/current/03-taxonomy/) | Dictionary; review | schemas/jsonschema/aimo-dictionary.schema.json; schema_validate_dictionary | Informativo; verifique contra texto oficial. |
| A.8.3 – Controle de acesso | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | —; integrity | — | Informativo; verifique contra texto oficial. |
| A.8.15 – Logging | [Template EV](../../standard/current/06-ev-template/) | EV, change_log; change_log | schemas/jsonschema/aimo-ev.schema.json; schema_validate_ev | Informativo; verifique contra texto oficial. |
| A.8.16 – Atividades de monitoramento | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | EV, change_log; change_log, integrity | templates/ev/ | Informativo; verifique contra texto oficial. |
| A.8.32 – Gestão de mudanças | [Pacote de Evidências](../../artifacts/evidence-bundle/) | change_log; change_log | schemas/jsonschema/aimo-standard.schema.json | Informativo; verifique contra texto oficial. |
| A.8.33 – Informação de teste | [Validador](../../standard/current/07-validator/) | EV | validator/rules/, validator/src/; schema_validate_ev | Informativo; verifique contra texto oficial. |
