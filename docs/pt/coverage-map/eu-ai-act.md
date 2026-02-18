---
description: Mapeamento AIMO Standard para a Lei de IA da UE. Rastreabilidade entre códigos de taxonomia AIMO e categorias de risco e requisitos da Lei de IA da UE.
---
<!-- aimo:translation_status=translated -->

# Mapeamento Lei de IA da UE

> Atalhos de rastreabilidade: Taxonomia → Requisitos Mínimos de Evidências → Validador → Protocolo de Supervisão Humana.

- [Taxonomia](../../standard/current/03-taxonomy/)
- [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/)
- [Schemas de Log](../../artifacts/log-schemas/)
- [Validador](../../validator/)
- [Protocolo de Supervisão Humana](../../governance/human-oversight-protocol/)

Esta página mapeia temas selecionados da Lei de IA da UE (documentação, registo, gestão de riscos, supervisão humana, transparência) para evidências e artefactos AIMO. É apenas de alto nível e **não** constitui aconselhamento jurídico nem garante conformidade. Verifique contra o texto legal oficial.

**Referência:** Regulamento (UE) 2024/1689 (Lei da Inteligência Artificial). Todos os números de artigo abaixo referem-se a este regulamento.

## Tabela de mapeamento

| Referência do quadro / tema | Evidências AIMO / onde na AIMO | Pacote de Evidências / Evidências Mínimas | Artefactos e validação | Notas |
| --- | --- | --- | --- | --- |
| Art. 4 – Literacia em IA | [Âmbito](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Transversal; evidência de capacidade/formação organizacional (alto nível). Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 9 – Sistema de gestão de riscos | [Âmbito](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | Sistemas de IA de alto risco (Título III). Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 10 – Dados e governação de dados | [Dicionário](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 11 – Documentação técnica (alto risco) | [Modelo EV](../../standard/current/06-ev-template/), [Pacote de Evidências](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **Anexo IV**: [Exemplos > Amostra Anexo IV UE](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); perfil: `coverage_map/profiles/eu_ai_act_annex_iv.json`. Pacote de exemplo conforme. Ver Exemplos (mais conteúdo numa versão futura). | Apenas alto nível; não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 12 – Registo | [Pacote de Evidências](../../artifacts/evidence-bundle/), [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 13 – Transparência e informação a implementadores/utilizadores | [Âmbito](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | Contexto de alto risco. Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 14 – Supervisão humana | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 15 – Precisão, robustez, cibersegurança | [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | EV (códigos de evidência/risco, alto nível) | templates/ev/ | Apenas mapeamento de alto nível. Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Art. 17 – Sistema de gestão da qualidade | [Âmbito](../../standard/current/02-scope/) | Summary, review (processo organizacional) | templates/ev/ | Distinto do Art. 9 (sistema de gestão de riscos). Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Obrigações de transparência (dependentes do caso de uso) | [Âmbito](../../standard/current/02-scope/), [Requisitos Mínimos de Evidências](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | Disposições aplicáveis dependem do caso de uso. Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Obrigações dos modelos GPAI | [Modelo EV](../../standard/current/06-ev-template/), [Pacote de Evidências](../../artifacts/evidence-bundle/) | Modelo EV, Pacote de Evidências (estrutura de evidências) | schemas/jsonschema/; schema_validate_ev | A AIMO fornece um quadro para organizar evidências; as obrigações reais são definidas pelo regulamento. Não é aconselhamento jurídico. Verifique contra texto oficial. |
| Considerandos – Responsabilização | [Pacote de Evidências](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | Não é aconselhamento jurídico. Verifique contra texto oficial. |

## Datas de aplicação / aplicabilidade (alto nível)

O que se segue alinha-se com o **calendário oficial da UE** (Serviço da Lei de IA / Comissão). **Não é aconselhamento jurídico** e não garante exatidão. Confirme sempre com o **texto legal oficial** e as autoridades competentes.

| Fase | Data | O que se aplica (alto nível) |
| --- | --- | --- |
| Entrada em vigor | Agosto 2024 | Regulamento em vigor; a maioria das obrigações substantivas ainda não aplicáveis. |
| Disposições gerais e proibições | 02 fev 2025 | Práticas proibidas (risco inaceitável); certas disposições sobre literacia em IA. |
| Regras GPAI e governação | 02 ago 2025 | Regras sobre organismos notificados, GPAI, governação, confidencialidade, sanções; códigos de conduta. |
| Regras principais + Anexo III alto risco + Art. 50 transparência | 02 ago 2026 | Aplicabilidade plena para sistemas de IA de alto risco (Anexo III), obrigações de transparência do Art. 50. |
| Alto risco embutido em produtos regulados | 02 ago 2027 | Sistemas de IA de alto risco embutidos em produtos sujeitos à legislação de produtos da UE. |

## Normas harmonizadas e presunção de conformidade (Art. 40)

Quando **normas harmonizadas** forem publicadas no Jornal Oficial da UE ao abrigo da Lei de IA, a sua conformidade pode conferir **presunção de conformidade** com os requisitos correspondentes. A lista e as datas exatas dependem dos trabalhos de normalização e da publicação no JO. Os mapeamentos AIMO são informativos e não conferem presunção de conformidade. Para o estado atual, consulte a página de [normalização da Lei de IA](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) da Comissão e **Referências** abaixo.

## Orientações 2026 do Gabinete de IA (detalhe de aplicação)

A Comissão Europeia indicou que o **Gabinete de IA** preparará **orientações práticas** durante 2026, incluindo sobre: classificação de alto risco; aplicação do Art. 50 (transparência); notificação de incidentes; elementos relacionados com o SGQ. Estas orientações são **gatilhos de atualização** para perfis e mapeamentos de cobertura AIMO: uma vez publicadas, os adoptantes devem alinhar evidências e mapeamentos com a última orientação oficial. A AIMO não interpreta nem garante conformidade com estas orientações.

!!! warning "Não é aconselhamento jurídico"
    Esta página é apenas para uso explicativo. Deve verificar a aplicabilidade e as datas contra o regulamento oficial e quaisquer atos de execução ou alteração. A AIMO não fornece aconselhamento jurídico nem garante conformidade.

!!! note "Nota legal / Mapeamento informativo"
    Esta página é **informativa**. A interpretação jurídica deve basear-se no regulamento oficial (EUR-Lex) e nas publicações da Comissão Europeia. A AIMO não fornece aconselhamento jurídico nem garante conformidade.

## Referências

**Fontes primárias**

- [Regulamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) (EUR-Lex) — Lei da Inteligência Artificial (texto legal)
- [Calendário de aplicação da Lei de IA da UE](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — Serviço da Lei de IA da Comissão Europeia (calendário de aplicação)
- [Normalização da Lei de IA](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) — Estratégia Digital da Comissão Europeia (normas harmonizadas, presunção de conformidade)

**Outros**

- Comissão Europeia / Gabinete de IA — orientações e calendário (ver Serviço da Lei de IA e notícias da Comissão para URLs atuais)
- [EPRS — Aplicação da Lei de IA da UE](https://www.europarl.europa.eu/thinktank/) — resumo do Parlamento (informativo)
