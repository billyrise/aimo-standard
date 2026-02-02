---
description: Mapeamento AIMO Standard para EU AI Act. Rastreabilidade entre códigos de taxonomia AIMO e categorias de risco e requisitos do EU AI Act.
---

# Mapeamento EU AI Act

> Atalhos de rastreabilidade: Taxonomia → Requisitos Mínimos de Evidências → Validador → Protocolo de Supervisão Humana.

- [Taxonomia](../standard/current/03-taxonomy.md)
- [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md)
- [Schemas de Log](../artifacts/log-schemas/index.md)
- [Validador](../validator/index.md)
- [Protocolo de Supervisão Humana](../governance/human-oversight-protocol.md)

Esta página mapeia temas selecionados do EU AI Act (documentação, manutenção de registros, gestão de riscos, supervisão humana, transparência) para evidências e artefatos AIMO. É apenas de alto nível e **não** constitui aconselhamento jurídico nem garante conformidade. Verifique contra o texto legal oficial.


## Tabela de mapeamento

| Referência do framework / tópico | Evidência AIMO / onde no AIMO | Pacote de Evidências / Requisitos Mínimos de Evidências | Artefatos e validação | Notas |
| --- | --- | --- | --- | --- |
| Art 9 – Gestão de riscos (obrigações) | [Escopo](../standard/current/02-scope.md) | request, review, exception | templates/ev/ | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 10 – Governança de dados | [Dicionário](../standard/current/05-dictionary.md) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 11 – Documentação (alto risco) | [Template EV](../standard/current/06-ev-template.md), [Pacote de Evidências](../artifacts/evidence-bundle.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; schema_validate_ev | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 12 – Manutenção de registros | [Pacote de Evidências](../artifacts/evidence-bundle.md), [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 13 – Transparência (informação ao usuário) | [Escopo](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 14 – Supervisão humana | [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md) | review, exception; review, exception | templates/ev/ev_template.md | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 17 – Gestão de riscos (alto risco) | [Escopo](../standard/current/02-scope.md) | request, review, exception, renewal | templates/ev/ | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 26 – Transparência (risco limitado) | [Escopo](../standard/current/02-scope.md) | Summary, EV; review | templates/ev/ | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 29 – Documentação (IA de propósito geral) | [Template EV](../standard/current/06-ev-template.md) | EV, Dictionary, Summary; request, review | schemas/jsonschema/; schema_validate_ev | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art 52 – Transparência (implantador) | [Requisitos Mínimos de Evidências](../artifacts/minimum-evidence.md) | EV, Summary; review | templates/ev/ | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Considerandos – Responsabilidade | [Pacote de Evidências](../artifacts/evidence-bundle.md) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
