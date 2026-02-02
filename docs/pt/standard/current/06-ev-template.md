---
description: Templates e guia de uso do Evidence Pack AIMO. Estrutura para documentar evidências de governança de IA com gestão de índice e formatação pronta para auditoria.
---

# Template EV

Esta seção define os templates de Evidence Pack e seu uso. Um Evidence Pack é uma coleção de documentação que demonstra governança e conformidade para um sistema de IA.

## Princípio Chave: Gestão de Índice e Diff

> **Importante**: O que importa não é o conteúdo de submissões individuais, mas o **índice** e **gestão de diff** entre itens de evidência.

Um Evidence Pack serve como um índice vinculando sistemas de IA aos seus artefatos de governança. O valor está em:

1. **Rastreabilidade**: Vinculando decisões, aprovações e mudanças ao longo do tempo
2. **Auditabilidade**: Permitindo que auditores naveguem pela estrutura de evidências
3. **Manutenibilidade**: Rastreando o que mudou, quando e por quê

## Conjunto MVP de Evidências (EV-01 a EV-07)

Os seguintes sete tipos de evidência formam o **conjunto mínimo viável** para demonstrar governança de IA:

| ID | Tipo de Evidência | Código | Propósito |
| --- | --- | --- | --- |
| EV-01 | Visão Geral do Sistema | EV-001 | Documentar o sistema de IA e seu propósito |
| EV-02 | Fluxo de Dados | EV-002 | Mapear movimento de dados pelo sistema |
| EV-03 | Inventário | EV-003 | Manter catálogo de ativos de IA |
| EV-04 | Avaliação de Risco e Impacto | EV-004 | Avaliar e documentar riscos |
| EV-05 | Controles e Aprovações | EV-005 | Documentar controles e registros de aprovação |
| EV-06 | Logging e Monitoramento | EV-006 | Definir configuração de logging e monitoramento |
| EV-07 | Incidentes e Exceções | EV-007 | Rastrear incidentes e exceções |

## Manifesto do Evidence Pack

Cada Evidence Pack DEVE incluir um arquivo de manifesto contendo:

### Metadados Obrigatórios

| Campo | Descrição | Obrigatório |
| --- | --- | --- |
| `pack_id` | Identificador único (ex: EP-EXAMPLE-001) | Sim |
| `pack_version` | Versão SemVer do pack | Sim |
| `taxonomy_version` | Versão da taxonomia AIMO usada | Sim |
| `created_date` | Data de criação do pack | Sim |
| `last_updated` | Data da última atualização | Sim |
| `owner` | Parte responsável | Sim |

### Códigos AIMO (8 Dimensões)

Cada Evidence Pack DEVE incluir códigos de todas as 8 dimensões:

```json
{
  "codes": {
    "FS": ["FS-001"],
    "UC": ["UC-001", "UC-002"],
    "DT": ["DT-002"],
    "CH": ["CH-001"],
    "IM": ["IM-001"],
    "RS": ["RS-001", "RS-003"],
    "OB": ["OB-001"],
    "EV": ["EV-001", "EV-002", "EV-003", "EV-004", "EV-005", "EV-006", "EV-007"]
  }
}
```

### Lista de Arquivos de Evidência

```json
{
  "evidence_files": [
    {
      "file_id": "EV-01",
      "filename": "EV-01_system_overview.md",
      "ev_type": "EV-001",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## Estrutura do Template

Cada template de evidência inclui:

1. **Bloco de Metadados Obrigatórios** - pack_id, version, taxonomy_version, datas, owner
2. **Tabela de Códigos AIMO** - Todas as 8 dimensões com códigos aplicáveis
3. **Seções de Conteúdo** - Seções de documentação específicas do domínio
4. **Referências** - Links para evidências relacionadas
5. **Histórico de Revisões** - Rastreamento de mudanças

### Exemplo de Cabeçalho de Template

```markdown
# EV-01: Visão Geral do Sistema

---

## Metadados Obrigatórios

| Campo | Valor |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI Governance Team` |

---

## Códigos AIMO (8 Dimensões)

| Dimensão | Código(s) | Rótulo |
| --- | --- | --- |
| **FS** | `FS-001` | Produtividade do Usuário Final |
| **UC** | `UC-001` | Q&A Geral |
| **DT** | `DT-002` | Interno |
| **CH** | `CH-001` | UI Web |
| **IM** | `IM-001` | Standalone |
| **RS** | `RS-001` | Vazamento de Dados |
| **OB** | `OB-001` | Eficiência |
| **EV** | `EV-001` | Visão Geral do Sistema |
```

## Downloads

### Templates

Templates de Evidence Pack estão disponíveis em:

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md`
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md`
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md`
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md`
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md`
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md`
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md`

### Schemas e Exemplos

- Schema: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- Exemplo: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

Veja [Releases](../../releases/index.md) para pacotes para download.

## Modelo de Distribuição

> **Nota**: Os alvos primários de distribuição são **firmas de auditoria e integradores de sistemas** (distribuidores de template), não empresas individuais.

Os templates são projetados para serem:

1. Adotados por auditores e consultores como artefatos padrão
2. Distribuídos para empresas com atribuição de fonte preservada
3. Versionados junto com o AIMO Standard

Empresas recebem templates através de seus auditores, consultores ou equipes internas de governança que mantêm a vinculação com a versão do padrão.

## Referências

- [Taxonomia](./03-taxonomy.md) - Definições de dimensão
- [Códigos](./04-codes.md) - Formato de código
- [Validador](./07-validator.md) - Regras de validação
- [Pacote de Evidências](../../artifacts/evidence-bundle.md) - Estrutura do pacote
