---
description: Guía de contribución a AIMO Standard - Cómo contribuir código, documentación y traducciones. Guías para issues y PRs.
---
<!-- aimo:translation_status=translated -->

# Contribuir

Esta página proporciona guías para contribuir al AIMO Standard.

## Inicio Rápido

1. Fork del repositorio
2. Crear una rama de característica
3. Hacer cambios siguiendo las guías abajo
4. Ejecutar verificaciones de calidad
5. Enviar un pull request

## Principios Clave

| Principio | Descripción |
| --------- | ----------- |
| El inglés es canónico | Edite `docs/en/` primero, luego actualice `docs/ja/` |
| SSOT | Este repositorio es la única fuente de verdad |
| Sin ediciones manuales a archivos generados | Edite fuentes, regenere, haga commit |
| Todos los cambios vía PR | Incluso los mantenedores usan pull requests |

## Verificaciones de Calidad

Antes de enviar un PR, ejecute:

```bash
# Activar entorno virtual
source .venv/bin/activate

# Ejecutar lints
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# Construir documentación
mkdocs build --strict
```

## Tipos de Cambio

| Tipo | Ejemplos | Requisitos de Revisión |
| ---- | -------- | ------------------- |
| Normativo | Cambios de esquema, requisitos | Mantenedor + discusión |
| No-normativo | Erratas, clarificaciones | Aprobación de mantenedor |
| i18n | Traducciones | Estructura debe coincidir con EN |
| Tooling | CI/CD, scripts | Aprobación de mantenedor |

## Guías de i18n

### Orden de Actualización

1. Editar fuente en inglés (`docs/en/...`)
2. Actualizar traducción al japonés (`docs/ja/...`)
3. Ejecutar `lint_i18n.py` para verificar consistencia
4. Hacer commit de ambos juntos

### Requisitos de Estructura

- Mismos nombres de archivo en ambos idiomas
- Misma jerarquía de encabezados
- Mismo conteo de páginas por sección

## Lista de Verificación de PR

Al enviar un PR, verifique:

- [ ] Tipo de cambio identificado (docs / schema / examples / tooling)
- [ ] Evaluación de cambio disruptivo completada
- [ ] i18n: EN y JA actualizados juntos (si aplica)
- [ ] Verificaciones de calidad pasan
- [ ] Issues relacionados vinculados

## Cambios Disruptivos

Los cambios disruptivos requieren:

1. Discusión de issue antes de implementación
2. Bump de versión según [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md)
3. Entrada de changelog con guía de migración

## Actualizaciones de Reclamaciones de Conformidad

Para agregar o modificar reclamaciones de conformidad:

1. Actualizar el YAML del mapa de cobertura
2. Actualizar páginas de documentación correspondientes
3. Ejecutar pruebas del validador
4. Documentar la justificación del mapeo

## Guías Completas

Consulte [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) para la guía a nivel de raíz.

## Páginas Relacionadas

- [Gobernanza](../) — Gobernanza del proyecto
- [Guía de Localización](../../contributing/localization/) — Detalles de i18n
- [Límite de Responsabilidad](../responsibility-boundary/) — Qué proporciona AIMO
