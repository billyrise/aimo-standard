---
description: Guia de citação do AIMO Standard - Como citar em artigos acadêmicos, relatórios de auditoria e propostas. Formatos CITATION.cff e BibTeX.
---
<!-- aimo:translation_status=translated -->

# Como Citar

Esta página fornece orientação de citação para o AIMO Standard em artigos acadêmicos, relatórios de auditoria e propostas.

## CITATION.cff

O repositório inclui um arquivo [CITATION.cff](https://github.com/billyrise/aimo-standard/blob/main/CITATION.cff) seguindo o padrão Citation File Format.

O GitHub automaticamente exibe informações de citação deste arquivo.

## Citação Recomendada

### Forma Curta (Inline)

> AIMO Standard Contributors. (2026). AIMO Standard. https://standard.aimoaas.com/

### BibTeX

```bibtex
@software{aimo_standard,
  author = {{AIMO Standard Contributors}},
  title = {AIMO Standard},
  url = {https://standard.aimoaas.com/},
  version = {0.0.2},
  year = {2026}
}
```

### Estilo APA

> AIMO Standard Contributors. (2026). *AIMO Standard* (Version 0.0.2) [Software]. https://standard.aimoaas.com/

## Citação de Versão Específica

Ao citar uma versão específica:

> AIMO Standard Contributors. (2026). AIMO Standard v0.0.2. https://github.com/billyrise/aimo-standard/releases/tag/v0.0.2

## Documentação de Auditoria

Para relatórios de auditoria e documentação de conformidade:

| Campo | Valor |
| ----- | ----- |
| Nome do Padrão | AIMO Standard |
| Versão | (especifique a versão usada, ex: v0.0.1) |
| Website | https://standard.aimoaas.com/ |
| Repositório | https://github.com/billyrise/aimo-standard |
| Release | https://github.com/billyrise/aimo-standard/releases |

## Orientação de URL

### URLs Canônicas

Use estas URLs em documentação oficial:

| Propósito | URL |
| ------- | --- |
| Documentação mais recente | https://standard.aimoaas.com/latest/ |
| Versão específica | https://standard.aimoaas.com/0.0.2/ |
| Releases GitHub | https://github.com/billyrise/aimo-standard/releases |

!!! note "Formato de Caminho do Site"
    Caminhos do site usam números de versão sem o prefixo `v`. Para versão `v0.0.1`, use `/0.0.1/` nas URLs.

### Evitar

- URLs espelho do GitHub Pages (temporário)
- URLs específicas de branch (podem mudar)

## Páginas Relacionadas

- [Trust Package](../trust-package/) — Materiais prontos para auditoria
- [Governança](../) — Governança do projeto
- [Licença](../license/) — Termos de licenciamento
