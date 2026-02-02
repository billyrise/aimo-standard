---
description: Shadow AI 검색 로그 스키마 - 기업에서 승인되지 않은 AI 사용의 탐지, 인벤토리 및 해결을 문서화하기 위한 벤더 중립 형식.
---

# Shadow AI 검색 로그 스키마

## 목적

이 스키마는 **승인되지 않은 AI 사용(Shadow AI)**의 탐지, 인벤토리 및 해결을 문서화하는 로그를 위한 벤더 중립 형식을 정의합니다. 이를 통해 조직은 다음을 수행할 수 있습니다:

- Shadow AI 탐지 이벤트의 감사 가능한 기록 유지
- 다양한 소스(CASB, 프록시, IdP, EDR, SaaS 감사 로그)의 로그를 일관된 형식으로 정규화
- 컴플라이언스 및 감사 목적의 증거 제출 지원

## 정규화 원칙

| 원칙 | 설명 |
| --- | --- |
| **벤더 중립** | 특정 벤더 로그 형식에 종속되지 않음; Netskope, Zscaler, Microsoft Defender 등에 적용 가능 |
| **최소 필수 필드** | 필수 필드만 MUST이며; 조직은 선택적 필드를 생략할 수 있음 |
| **확장 가능** | `additionalProperties: true`는 벤더별 또는 조직별 확장을 허용 |
| **개인정보 인식** | 필드는 민감한 콘텐츠를 포함하지 않고 참조하도록 설계됨 |

## 필수 필드 (MUST)

| 필드 | 유형 | 설명 | 예시 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 이벤트의 타임스탬프 | `2026-01-15T09:30:00Z` |
| `actor_id` | string | 사용자 또는 서비스 식별자 | `user@example.com` |
| `actor_type` | string | 행위자 유형 | `user` 또는 `service` |
| `source_system` | string | 이벤트를 탐지한 시스템 | `proxy`, `casb`, `idp`, `edr`, `saas_audit` |
| `ai_service` | string | 접근한 AI 제품 또는 도메인 | `chat.openai.com`, `claude.ai` |
| `action` | string | 수행된 작업 | `chat`, `upload`, `download`, `tool_execute`, `api_call` |
| `data_classification` | string | 데이터 분류 수준 | `public`, `internal`, `confidential`, `restricted` |
| `decision` | string | 적용된 정책 결정 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 관련 증거에 대한 참조 | `sha256:abc123...` 또는 `urn:evidence:...` |
| `record_id` | string | 이 레코드의 고유 식별자 | `evt-20260115-001` |

## 선택적 필드 (SHOULD/MAY)

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `session_id` | string | 세션 식별자 |
| `device_id` | string | 기기 식별자 |
| `ip` | string | IP 주소 |
| `user_agent` | string | 사용자 에이전트 문자열 |
| `department` | string | 조직 부서 |
| `project_id` | string | 프로젝트 식별자 |
| `prompt_category` | string | 프롬프트/쿼리 카테고리 |
| `model_family` | string | AI 모델 패밀리 (예: GPT-4, Claude) |
| `destination` | string | 목적지 URL 또는 엔드포인트 |
| `policy_id` | string | 결정을 트리거한 정책 |
| `remediation_ticket` | string | 해결 티켓 참조 |

## 개인정보/보안 참고사항

!!! warning "데이터 처리"
    - **PII, 자격 증명 또는 프롬프트 내용을** 로그 필드에 직접 **포함하지 마세요**.
    - `evidence_ref`를 사용하여 별도로 저장된 민감한 콘텐츠를 참조하세요.
    - 로그 저장소에 적절한 접근 통제를 적용하세요.
    - [최소 증거 요구사항](../minimum-evidence.md)에 맞춘 데이터 보존 정책을 고려하세요.

## JSON Schema

다운로드: [shadow-ai-discovery.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/shadow-ai-discovery.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "actor_id", "actor_type", "source_system",
    "ai_service", "action", "data_classification", "decision",
    "evidence_ref", "record_id"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string", "minLength": 1 },
    "actor_type": { "type": "string", "enum": ["user", "service"] },
    "source_system": { "type": "string", "minLength": 1 },
    "ai_service": { "type": "string", "minLength": 1 },
    "action": { "type": "string", "minLength": 1 },
    "data_classification": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 },
    "record_id": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 관련 페이지

- [로그 스키마 인덱스](index.md)
- [에이전트 활동 로그](agent-activity.md)
- [최소 증거 요구사항](../minimum-evidence.md)
- [분류체계: IM-007 Shadow/미관리](../../standard/current/03-taxonomy.md)
