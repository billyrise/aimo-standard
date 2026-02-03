---
description: Validador AIMO - Garante que Evidence Packs conformam aos schemas do AIMO Standard. Regras de validação, tratamento de erros e implementação de referência para verificações de conformidade.
---

# Validador

O Validador AIMO garante que Evidence Packs e artefatos relacionados conformam aos schemas e requisitos do AIMO Standard.

Veja também: [Protocolo de Supervisão Humana](../../governance/human-oversight-protocol.md) — limite de responsabilidade para revisão máquina vs. humano.

## Validador na prática

Para um quickstart de 30 segundos (instalar, executar, interpretar saída), veja [Hub do Validador](../../validator/index.md).

## Requisitos MVP do Validador

O validador mínimo viável DEVE realizar as seguintes verificações:

### 1. Validação de Campos Obrigatórios

Verificar que todos os campos obrigatórios estão presentes:

| Artefato | Campos Obrigatórios |
| --- | --- |
| Manifesto Evidence Pack | pack_id, pack_version, taxonomy_version, created_date, last_updated, codes, evidence_files |
| Objeto Codes | FS, UC, DT, CH, IM, RS, EV (OB opcional) |
| Entrada de Arquivo de Evidência | file_id (EP-01..EP-07), filename, title (ev_type / ev_codes opcional) |

### 2. Validação de Código de Dimensão

Verificar que cada dimensão obrigatória tem pelo menos um código:

| Dimensão | Requisito |
| --- | --- |
| FS (Escopo Funcional) | Exatamente 1 código |
| UC (Classe de Caso de Uso) | Pelo menos 1 código |
| DT (Tipo de Dados) | Pelo menos 1 código |
| CH (Canal) | Pelo menos 1 código |
| IM (Modo de Integração) | Exatamente 1 código |
| RS (Superfície de Risco) | Pelo menos 1 código |
| OB (Resultado / Benefício) | Opcional (0 ou mais) |
| LG (Tipo de Log/Registro) | Pelo menos 1 código |

### 3. Verificação de Existência no Dicionário

Validar que todos os códigos existem no dicionário de taxonomia:

- Carregar o dicionário de taxonomia para o `taxonomy_version` especificado
- Verificar que cada código no manifesto existe no dicionário
- Reportar códigos inválidos com sua dimensão e valor

### 4. Validação de Formato de Código

Verificar que todos os códigos correspondem ao formato esperado:

```regex
^(FS|UC|DT|CH|IM|RS|OB|LG)-\d{3}$
```

### 5. Validação de Schema

Validar contra JSON Schemas:

| Schema | Propósito |
| --- | --- |
| `evidence_pack_manifest.schema.json` | Manifestos de Evidence Pack |
| `taxonomy_pack.schema.json` | Definições de pacote de taxonomia |
| `changelog.schema.json` | Entradas de changelog |

## Regras de Validação

### Regra: Dimensões Obrigatórias

```yaml
rule_id: required_dimensions
description: Todas as dimensões obrigatórias devem ter pelo menos um código
severity: error
check: |
  - FS: exatamente 1
  - UC: pelo menos 1
  - DT: pelo menos 1
  - CH: pelo menos 1
  - IM: exatamente 1
  - RS: pelo menos 1
  - LG: pelo menos 1
```

### Regra: Códigos Válidos

```yaml
rule_id: valid_codes
description: Todos os códigos devem existir no dicionário de taxonomia
severity: error
check: |
  Para cada código em manifest.codes:
    - Código existe no dicionário para taxonomy_version especificado
    - Status do código é 'active' (avisar se 'deprecated')
```

### Regra: Formato de Código

```yaml
rule_id: code_format
description: Todos os códigos devem corresponder ao formato padrão
severity: error
pattern: "^(FS|UC|DT|CH|IM|RS|OB|LG)-\\d{3}$"
```

### Regra: Formato de Versão

```yaml
rule_id: version_format
description: Versões devem ser SemVer válido
severity: error
pattern: "^\\d+\\.\\d+\\.\\d+$"
fields:
  - pack_version
  - taxonomy_version
```

## Formato de Saída de Erro

Erros de validação são reportados no seguinte formato:

```
<caminho>: <severidade>: <mensagem>
```

**Exemplos:**

```
codes.FS: error: Dimensão obrigatória 'FS' não tem códigos
codes.UC[0]: error: Código 'UC-999' não existe no dicionário v0.1.0
pack_version: error: Formato de versão inválido 'v1.0' (esperado SemVer)
codes.RS[1]: warning: Código 'RS-002' está deprecated em v0.2.0
```

## O que o Validador NÃO Verifica

O validador foca em conformidade estrutural, não qualidade de conteúdo:

| Aspecto | Razão |
| --- | --- |
| Precisão de conteúdo | Validador verifica estrutura, não significado |
| Completude de evidências | Templates são guias, não formatos aplicados |
| Resolução de referências cruzadas | Existência de arquivo não verificada |
| Validade de timestamp | ISO-8601 não estritamente validado |
| Unicidade de ID | Não aplicado atualmente |
| Hashes de integridade | Responsabilidade do adotante |

## Implementação de Referência

Uma implementação de referência é fornecida em Python:

```
validator/src/validate.py
```

### Uso

```bash
python validator/src/validate.py <manifest.json>
```

### Saída de Exemplo

```
Validating: evidence_pack_manifest.json
Taxonomy version: 0.1.0

Checking required dimensions...
  FS: OK (1 código)
  UC: OK (3 códigos)
  DT: OK (1 código)
  CH: OK (1 código)
  IM: OK (1 código)
  RS: OK (3 códigos)
  OB: OK (2 códigos)
  LG: OK (7 códigos)

Checking code validity...
  Todos os códigos válidos.

Validation: PASSED
```

## Política de Versionamento

Regras do validador seguem SemVer:

- **MAJOR**: Breaking changes de regras (novas verificações obrigatórias que falham packs válidos existentes)
- **MINOR**: Novas verificações opcionais, avisos ou mensagens informativas
- **PATCH**: Correções de bug que não mudam resultados de validação

## Referências de Schema

| Schema | Localização |
| --- | --- |
| Evidence Pack Manifest | `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json` |
| Taxonomy Pack | `source_pack/03_taxonomy/schemas/taxonomy_pack.schema.json` |
| Changelog | `source_pack/03_taxonomy/schemas/changelog.schema.json` |

## Referências

- [Taxonomia](./03-taxonomy.md) - Definições de dimensão
- [Códigos](./04-codes.md) - Formato de código
- [Dicionário](./05-dictionary.md) - Dicionário de códigos
- [Regras do Validador](../../validator/index.md) - Documentação completa de regras
