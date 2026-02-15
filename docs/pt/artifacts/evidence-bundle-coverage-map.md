---
description: Modelo de mapa de cobertura do pacote de evidências (v0.1). Resumo informativo de uma página para auditores — escopo, tipos de evidência, mapeamento de controles, exclusões, prova de integridade.
---
<!-- aimo:translation_status=translated -->

# Mapa de cobertura do pacote de evidências (Modelo)

!!! info "Informativo — prática recomendada"
    Esta página define um **modelo de prática recomendada** para um mapa de cobertura do pacote de evidências de uma página. **Não** é um requisito normativo do padrão. Use-o para documentar o que um pacote cobre e não cobre para a entrega ao auditor. As referências (ex. a marcos) são estáveis; a adoção fica a critério do implementador.

---

## 1. Escopo

| Elemento | Descrição |
|------|--------------|
| **Referência de escopo** | `scope_ref` do manifesto do pacote (ex. `SC-001`). Liga este pacote ao escopo declarado. |
| **ID do pacote** | `bundle_id` (UUID) — identificador único deste pacote. |
| **Versão do pacote** | `bundle_version` (SemVer) — versão do pacote. |
| **Período / instantâneo** | Opcional: período ou data do instantâneo que este pacote representa (ex. 2026-Q1, as-of 2026-02-03). |

---

## 2. Tipos de evidência (EV / objects vs payloads)

| Categoria | Conteúdo | Exemplo mínimo v0.1 |
|----------|----------|------------------------|
| **object_index** | Objetos enumerados (metadados, índices). Cada entrada: `id`, `type`, `path`, `sha256`. | ex. `objects/index.json` (tipo index). |
| **payload_index** | Ficheiros de carga (EV JSON raiz, ficheiros Evidence Pack). Cada entrada: `logical_id`, `path`, `sha256`, `mime`, `size`. | ex. `payloads/root.json` (EV JSON raiz AIMO). |
| **Tipos EV** | Registos de evidência (na raiz ou cargas ligadas) — request, review, exception, renewal, change log. | Alinhado com o [Modelo Evidence Pack](../../standard/current/06-ev-template/) e os [Requisitos mínimos de evidência](../minimum-evidence/). |

*Os implementadores podem estender object_index e payload_index; os caminhos DEVEM permanecer dentro da raiz do pacote e satisfazer a [estrutura raiz do Pacote de Evidências (v0.1)](../../standard/current/09-evidence-bundle-structure/).*

---

## 3. Mapeamento de controles (apenas referência)

O mapeamento para marcos externos é **apenas para referência**; o padrão não exige conformidade com nenhuma regulamentação específica.

| Marco | Uso neste pacote | Referência |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | Opcional: documentar que temas AI MS este pacote suporta. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | Opcional: alinhamento de documentação/registos de alto nível. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | Opcional: mapeamento Govern, Map, Measure, Manage. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | Opcional: Model Documentation Form; anexar em External Forms, referenciar por logical_id. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/); perfil `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | Opcional: artefactos do perfil GenAI (AI 600-1). | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/); perfil `nist_ai_600_1_genai.json` |
| **UK ATRS** | Opcional: registo ATRS, avaliação de contratação. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); perfil `uk_atrs_procurement.json` |
| **JP Gov GenAI contratação** | Opcional: lista de verificação de contratação JP, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); perfil `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | Opcional: gestão de alterações, acesso, registo, integridade. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*Preencher « Uso neste pacote » por submissão; o padrão não exige cobertura de controlo específica.*

### External Forms e referência ao manifesto

**External Forms** (modelos/listas de verificação oficiais anexados tal como estão) devem ser listados no **payload_index** do pacote com `logical_id`, `path`, `sha256`, `mime` e `size` estáveis. Os auditores podem então rastrear do manifesto ao ficheiro e verificar o hash. Ver [Modelo EV — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) e [Modelo EV — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index).

---

## 4. Exclusões / pressupostos

| Área | O que este pacote **não** cobre (linhas de exemplo — ajustar por submissão) |
|------|-------------------------------------------------------------------------------|
| **Exclusões** | ex. Sistemas ou casos de uso fora do escopo; componentes de terceiros não evidenciados; período fora deste pacote. |
| **Pressupostos** | ex. Versão Dictionary/taxonomia; versão do validador/esquema utilizada; custódia e retenção são definidas pela implementação. |
| **Limitações** | ex. A verificação de assinaturas está fora do escopo em v0.1; nenhuma interpretação jurídica das regulamentações. |

*Substituir o texto placeholder por exclusões e pressupostos específicos da submissão.*

---

## 5. Resumo da prova de integridade (v0.1)

| Elemento | O que é fornecido (v0.1 normativo) |
|---------|----------------------------------|
| **manifest.json** | Presente e válido ao esquema; inclui `object_index`, `payload_index`, `hash_chain`, `signing`. |
| **sha256** | Cada ficheiro em `object_index` e `payload_index` tem um sha256 hex em minúsculas de 64 caracteres declarado; o validador verifica a correspondência do conteúdo. |
| **Existência do índice** | Todos os caminhos listados existem sob a raiz do pacote; sem travessia de caminho (`../` ou `/` à frente). |
| **Existência de assinatura** | Pelo menos um ficheiro de assinatura em `signatures/`; o manifesto referencia-o via `signing.signatures[]` com `path` e `targets` (v0.1 DEVE incluir `manifest.json` em targets). A verificação criptográfica está fora do escopo em v0.1. |
| **Cadeia de hash** | `hash_chain` no manifesto: `algorithm`, `head` (64 caracteres hex), `path` (ficheiro sob `hashes/`), `covers` (v0.1 DEVE incluir `manifest.json` e `objects/index.json`). O ficheiro em `hash_chain.path` existe. |

*Esta tabela resume as garantias de integridade que o [Validador](../../validator/) verifica para pacotes v0.1. A custódia (armazenamento, controlo de acesso, retenção) é definida pela implementação.*

---

## Coverage Map (YAML) vs Perfis (JSON)

| Artefacto | Estado | Propósito |
|----------|--------|---------|
| **Coverage Map YAML** (`coverage_map/coverage_map.yaml` ou similar) | **Informativo** | Temas de mapeamento de alto nível entre evidência/artefactos AIMO e marcos externos (ISO 42001, NIST AI RMF, EU AI Act, etc.) para explicabilidade. Não impõe requisitos de validação normativos. |
| **Profile JSONs** (`coverage_map/profiles/*.json`) | **Normativo** | Especificações de conversão validadas contra `schemas/jsonschema/aimo-profile.schema.json`. Definem mapeamentos legíveis por máquina (ex. que objetos AIMO mapeiam para que cláusulas de marco). O [Validador](../../validator/) executa `--validate-profiles` para garantir que todos os profile JSON oficiais conformam ao esquema (padrão profile_id PR-*, enumeração target, target_version, mappings). |

### Perfis oficiais (validados pelo validador)

Os Profile JSON estão em `coverage_map/profiles/` e são validados pelo validador (`--validate-profiles`). Nomenclatura: nome do ficheiro `<target>_<purpose>.json`; cada um inclui `target_version`.

| Ficheiro | profile_id | target | target_version |
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

### Política de atualização de perfis

- **Refs EU AI Act (0.1.2)**: As referências a artigos do EU AI Act no mapa de cobertura e na documentação foram alinhadas ao Regulamento (UE) 2024/1689 para uma prontidão de evidência consistente; apenas informativo, não aconselhamento jurídico.
- **ISO 42001 / NIST AI RMF**: Novas versões do marco alvo podem ser adicionadas como novos ficheiros de perfil ou novos valores `target_version` numa versão futura do padrão; os perfis v0.1 permanecem congelados para a release v0.1.
- **EU AI Act Annex IV**: O Anexo IV e os artigos relacionados podem ser atualizados pelos reguladores; os mapeamentos de perfil podem ser atualizados via **PATCH** (ex. 0.1.x) para acompanhar alterações de redação ou cláusula mantendo o mesmo profile_id para continuidade. Os implementadores devem alinhar-se com a versão referenciada na `target_version` do perfil e nas notas de release.

---

## Ver também

- [Pacote de Evidências (resumo de artefacto)](../evidence-bundle/)
- [Estrutura raiz do Pacote de Evidências (v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [Requisitos mínimos de evidência](../minimum-evidence/)
- [Coverage Map (mapeamentos de marcos)](../../coverage-map/)
- [Validador](../../validator/)
