---
description: Hub do Validador AIMO - Quickstart de ferramentas de validação. Instale, execute e interprete resultados em 30 segundos. Validação de evidence pack e verificações de conformidade.
---
<!-- aimo:translation_status=translated -->

# Validador

Esta página é um hub para ferramentas e regras de validação. A especificação normativa do validador e suas regras está no Padrão.

## Quickstart (30 segundos)

**1. Pré-requisitos**

```bash
pip install jsonschema   # se não estiver instalado
```

**2. Execute validação contra um pacote de amostra**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. Leia o relatório e corrija erros/avisos**

Saída de exemplo (sucesso):

```
OK
```

Saída de exemplo (falha):

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

Códigos de saída: `0` = sucesso, `1` = erros de validação, `2` = erro de uso.

---

## O que verifica

- **Validação de schema**: objeto raiz, dicionário e evidências conformam a JSON Schema
- **Consistência de dicionário**: todos os códigos existem no dicionário de taxonomia
- **Status de código**: avisa para códigos deprecated, erros para códigos removidos

## O que NÃO verifica

- **Precisão de conteúdo**: validador verifica estrutura, não significado
- **Garantia de conformidade**: passar validação não garante conformidade regulatória
- **Julgamento humano**: decisões dependentes de contexto requerem revisão humana (veja [Protocolo de Supervisão Humana](../governance/human-oversight-protocol/))
- **Coleta automática de logs**: validador valida evidências submetidas; não coleta logs

---

## Recursos

- **Especificação**: [Padrão > Atual > Validador](../standard/current/07-validator/) — regras, verificações de referência e como validação se relaciona com evidências.
- **Regras e implementação**: repositório `validator/rules/` (checks), `validator/src/` (implementação de referência). Execução e uso de CI estão descritos na especificação.
- **Interpretação**: o que uma "falha" de validação significa para auditores (explicado na especificação).

Para conformidade e uso de artefatos, veja [Conformidade](../conformance/) e [Artefatos](../artifacts/).
