---
description: Sobreposições de contratação e divulgação (Reino Unido, Japão). ATRS UK, orientação de contratação UK, contratação GenAI do governo japonês e diretrizes empresariais de IA. Apenas mapeamento de referência.
---
<!-- aimo:translation_status=translated -->

# Sobreposições de contratação e divulgação (Reino Unido, Japão)

Esta página descreve **mapeamentos de referência** entre evidências AIMO e quadros de contratação e divulgação selecionados do **Reino Unido** e do **Japão**. É **apenas mapeamento de referência**; a AIMO não substitui listas de verificação oficiais nem orientação governamental.

## Reino Unido: ATRS e contratação de IA

| Tema | Evidências AIMO / mapeamento | Notas |
| --- | --- | --- |
| **ATRS UK** (registo de transparência de IA) | Summary, review (responsável pela responsabilização), evidence (descrição do modelo/sistema), dictionary (considerações de risco). Perfil: `coverage_map/profiles/uk_atrs_procurement.json`. | Anexar ou referenciar registo de transparência tipo ATRS em Formulários externos; ligar a objetos do pacote por logical_id. |
| **Orientação de contratação UK** | Request, review, exception; Pacote de Evidências para avaliação de fornecedores. | Utilizar o pacote AIMO para estruturar evidências para avaliação de contratação; a orientação oficial UK permanece autorizada. |

## Japão: Contratação GenAI do governo e diretrizes empresariais de IA

| Tema | Evidências AIMO / mapeamento | Notas |
| --- | --- | --- |
| **Lista de verificação de contratação GenAI do governo JP** | Anexar lista como Formulário externo (ex.: payload: JP_PROCUREMENT_CHECKLIST); referenciar no manifest. Perfil: `coverage_map/profiles/jp_gov_genai_procurement.json`. | Apenas mapeamento de referência; a AIMO não substitui listas oficiais. |
| **Diretrizes empresariais de IA** | Summary, dictionary; mapear itens da lista para códigos de taxonomia AIMO quando útil para rastreabilidade. | Utilizar para explicabilidade; verificar contra orientação oficial japonesa. |

## Como utilizar

- **Formulários externos**: Anexar modelos/listas oficiais do Reino Unido ou do Japão **tal como estão** (PDF, DOC, etc.), fazer hash e listar no [payload_index](../../standard/current/09-evidence-bundle-structure/) do Pacote de Evidências ou na [secção Formulários externos do modelo EV](../../standard/current/06-ev-template/). Referenciar por logical_id no manifest e nos mapeamentos de cobertura.
- **Perfis**: Os perfis acima definem mapeamentos opcionais legíveis por máquina; não impõem obrigações legais ou contratuais.

Consulte [Conformidade](../../conformance/) para níveis e [Requisitos Mínimos de Evidências — Sobreposições regulamentares](../../artifacts/minimum-evidence/) para resumo das sobreposições.
