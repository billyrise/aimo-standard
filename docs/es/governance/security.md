---
description: Política de seguridad de AIMO Standard - Reporte de vulnerabilidades, procedimientos de divulgación y consideraciones de seguridad para implementaciones de gobernanza de IA.
---
<!-- aimo:translation_status=translated -->

# Seguridad

Esta página documenta la política de seguridad para AIMO Standard, incluyendo reporte de vulnerabilidades y procedimientos de divulgación.

## Alcance

### En Alcance

- Implementación de referencia del validador (`validator/`)
- Build y release tooling (`tooling/`)
- JSON schemas (`schemas/`)
- Infraestructura del sitio web de documentación

### Fuera de Alcance

- Contenido de especificación (el texto normativo no es un artefacto de seguridad)
- Implementaciones de adoptantes usando AIMO Standard
- Dependencias externas (reporte a mantenedores upstream)

## Versiones Soportadas

| Versión | Soportada |
| ------- | --------- |
| latest (dev) | Sí |
| Releases etiquetados (vX.Y.Z) | Sí (últimas 2 versiones menores) |
| Releases más antiguos | No (se recomienda actualizar) |

## Reportar una Vulnerabilidad

**No** abra un issue público de GitHub para vulnerabilidades de seguridad.

### Proceso

1. Reporte privadamente vía reporte de vulnerabilidades privado de GitHub
2. Incluya: descripción, pasos de reproducción, versiones afectadas, impacto
3. Permita tiempo para evaluación y desarrollo de corrección

### Cronograma

| Fase | Cronograma |
| ----- | -------- |
| Reconocimiento | 72 horas |
| Evaluación inicial | 7 días |
| Divulgación coordinada | 90 días máximo |

## Política de Divulgación

1. Las vulnerabilidades se reportan privadamente
2. Las correcciones se desarrollan antes de la divulgación pública
3. Los avisos de seguridad se publican después de que las correcciones estén disponibles
4. Los reportadores son acreditados (a menos que se solicite anonimato)

## Medidas de Seguridad

- Verificaciones CI/CD en todos los cambios
- Releases firmados con checksums SHA-256
- Revisión de PR obligatoria antes de merge

## Política Completa

Consulte [SECURITY.md](https://github.com/billyrise/aimo-standard/blob/main/SECURITY.md) para la política de seguridad completa.

## Páginas Relacionadas

- [Paquete de Confianza](trust-package.md) — Materiales listos para auditores
- [Gobernanza](index.md) — Gobernanza del proyecto
