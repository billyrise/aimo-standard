---
description: AIMO 로그 스키마 - AI 증거를 위한 벤더 중립 로그 형식. Shadow AI 검색 및 에이전트 활동 모니터링 스키마 포함.
---

# 로그 스키마

## 이것이 무엇인가

이 섹션은 증거 번들에 포함될 수 있는 증거를 위한 **정규화된 로그 형식**을 정의합니다. 이 스키마는 AI 사용 모니터링 및 에이전틱 운영과 관련된 로그를 위한 벤더 중립 구조를 제공합니다.

## 사용 시기

- **Shadow AI 가시성**: 승인되지 않은 AI 사용의 탐지, 인벤토리 및 해결 문서화.
- **에이전틱 운영 감사**: 자율 에이전트 권한 행사, 도구 실행 및 재귀 작업 설명.
- **인시던트 재현성**: 인시던트 조사 및 근본 원인 분석을 위한 구조화된 증거 제공.

## 이것이 아닌 것

!!! warning "중요"
    이 스키마는 **증거 제출을 위한 로그 형식**을 정의합니다. 다음은 수행하지 않습니다:

    - 시스템에서 자동으로 로그 수집
    - 로그 집계 또는 모니터링 도구 제공
    - 규정 또는 표준 준수 보장
    - 벤더별 로깅 구현 대체

    조직은 자체 로그 수집 파이프라인을 구현하고 증거 제출을 위해 이 스키마로 로그를 정규화해야 합니다.

## 스키마

| 스키마 | 목적 | 다운로드 |
| --- | --- | --- |
| [Shadow AI 검색 로그](shadow-ai-discovery.md) | 승인되지 않은 AI 사용 탐지 및 인벤토리 | [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json) |
| [에이전트 활동 로그](agent-activity.md) | 에이전틱 AI 권한 행사 및 도구 실행 | [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json) |

## 관련 페이지

- [최소 증거 요구사항](../minimum-evidence.md) — MUST 수준 증거 체크리스트
- [증거 번들](../evidence-bundle.md) — 번들 구조 및 목차
- [분류체계](../../standard/current/03-taxonomy.md) — 분류 코드 (UC-010 에이전틱 자동화, IM-007 Shadow/미관리 포함)
