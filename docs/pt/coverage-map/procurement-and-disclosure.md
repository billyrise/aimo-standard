---
description: Sobreposições de contratação e divulgação (Reino Unido, Japão). ATRS UK, orientação de contratação UK, contratação GenAI do governo japonês e diretrizes empresariais de IA. Apenas mapeamento de referência.
---
<!-- aimo:translation_status=translated -->

# Sobreposições de contratação e divulgação (Reino Unido, Japão)

Esta página descreve **mapeamentos de referência** entre evidências AIMO e quadros de contratação e divulgação selecionados do **Reino Unido** e do **Japão**. O objetivo é **reduzir a carga através da reutilização de evidência AIMO**. É **mapeamento informativo apenas**; a AIMO não garante cumprimento completo dos requisitos governamentais. Verifique face às fontes oficiais abaixo.

## Fontes primárias

**Reino Unido**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK (modelo, orientação, registos publicados)
- [Modelo ATRS](https://www.gov.uk/government/publications/algorithmic-transparency-template) — Modelo oficial para o setor público
- [Orientação para organizações que usam o ATRS](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**Japão**

- [Digital Agency — Orientação de contratação e utilização GenAI](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — Digital Agency (Cabinet Secretariat)
- [AI Business Guidelines](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC (Ministério da Economia, Comércio e Indústria / Ministério dos Assuntos Internos e Comunicações)

## Tabela de mapeamento (Reino Unido)

| Requisito governamental (tema) | Artefatos AIMO | Onde no Evidence Bundle | Cobertura do validador | Nota |
| --- | --- | --- | --- | --- |
| ATRS — responsabilidade / proprietário | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | Mapeamento informativo; não garante conformidade completa. |
| ATRS — descrição do sistema / modelo | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | Anexar registo ATRS oficial em Formulários externos; ligar por logical_id. |
| ATRS — considerações de risco | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. |
| Contratação — evidência do fornecedor | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | Usar o pacote para estruturar evidência; a orientação UK permanece autorizada. |

## Tabela de mapeamento (Japão)

| Requisito governamental (tema) | Artefatos AIMO | Onde no Evidence Bundle | Cobertura do validador | Nota |
| --- | --- | --- | --- | --- |
| Lista de verificação de contratação GenAI (Digital Agency) | Formulário externo (lista tal qual); Dictionary, Summary | payload_index; secção External Forms; referência no manifest | N/A (anexo) | Mapeamento informativo; não garante conformidade completa. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI Business Guidelines — governação / rastreabilidade | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | Mapear itens da lista para taxonomia AIMO quando útil. |
| Documentação de risco / responsabilidade | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | Verificar face à orientação oficial da Digital Agency e METI/MIC. |

## Reino Unido: ATRS e contratação de IA (resumo)

| Tema | Evidências AIMO / mapeamento | Notas |
| --- | --- | --- |
| **ATRS UK** (registo de transparência de IA) | Summary, review (responsável pela responsabilização), evidence (descrição do modelo/sistema), dictionary (considerações de risco). Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. | Anexar ou referenciar registo de transparência tipo ATRS em Formulários externos; ligar a objetos do pacote por logical_id. |
| **Orientação de contratação UK** | Request, review, exception; Pacote de Evidências para avaliação de fornecedores. | Utilizar o pacote AIMO para estruturar evidências para avaliação de contratação; a orientação oficial UK permanece autorizada. |

## Japão: Contratação GenAI do governo e diretrizes empresariais de IA (resumo)

| Tema | Evidências AIMO / mapeamento | Notas |
| --- | --- | --- |
| **Lista de verificação de contratação GenAI do governo JP** | Anexar lista como Formulário externo (ex.: payload: JP_PROCUREMENT_CHECKLIST); referenciar no manifest. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Apenas mapeamento de referência; a AIMO não substitui listas oficiais. |
| **Diretrizes empresariais de IA** | Summary, dictionary; mapear itens da lista para códigos de taxonomia AIMO quando útil para rastreabilidade. | Utilizar para explicabilidade; verificar contra orientação oficial japonesa. |

## Como utilizar

- **Formulários externos**: Anexar modelos/listas oficiais do Reino Unido ou do Japão **tal como estão** (PDF, DOC, etc.), fazer hash e listar no [payload_index](../../standard/current/09-evidence-bundle-structure/) do Pacote de Evidências ou na [secção Formulários externos do modelo EV](../../standard/current/06-ev-template/). Referenciar por logical_id no manifest e nos mapeamentos de cobertura.
- **Perfis**: Os perfis acima definem mapeamentos opcionais legíveis por máquina; não impõem obrigações legais ou contratuais.

Consulte [Conformidade](../../conformance/) para níveis e [Requisitos Mínimos de Evidências — Sobreposições regulamentares](../../artifacts/minimum-evidence/) para resumo das sobreposições.
