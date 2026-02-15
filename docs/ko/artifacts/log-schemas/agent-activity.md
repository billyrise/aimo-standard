---
description: 에이전트 활동 로그 형식 - 기업의 에이전틱 AI 권한 행사, 도구 실행 및 재귀 작업 모니터링을 위한 벤더 중립 스키마.
---
<!-- aimo:translation_status=translated -->

# 에이전트 활동 로그 형식

## 목적

이 스키마는 **에이전틱 AI 권한 행사, 도구 실행 및 재귀 작업**을 문서화하는 로그를 위한 벤더 중립 형식을 정의합니다. 이를 통해 조직은 다음을 수행할 수 있습니다:

- 자율 에이전트 행동의 감사 가능한 기록 유지
- 컴플라이언스 및 인시던트 조사를 위해 "누가 어떤 권한으로 무엇을 했는지" 추적
- 감사 맥락에서 에이전틱 AI 운영의 설명 가능성 지원

## 이벤트 모델

스키마는 에이전틱 운영 생명주기를 캡처하는 네 가지 이벤트 유형을 지원합니다:

| 이벤트 유형 | 설명 |
| --- | --- |
| `agent_run` | 에이전트 실행 세션의 시작 또는 완료 |
| `tool_call` | 에이전트가 도구 또는 외부 작업 호출 |
| `tool_result` | 도구 호출에서 반환된 결과 |
| `escalation` | 에이전트가 사람 개입 또는 상승된 권한 요청 |

## 필수 필드 (MUST)

| 필드 | 유형 | 설명 | 예시 |
| --- | --- | --- | --- |
| `event_time` | string (ISO8601) | 이벤트의 타임스탬프 | `2026-01-15T09:30:00Z` |
| `agent_id` | string | 에이전트 식별자 | `agent-coding-assistant-v2` |
| `agent_version` | string | 에이전트 버전 | `2.1.0` |
| `run_id` | string | 이 실행/세션의 고유 식별자 | `run-20260115-abc123` |
| `event_type` | string | 이벤트 유형 | `agent_run`, `tool_call`, `tool_result`, `escalation` |
| `actor_id` | string | 시작한 사용자 또는 서비스 | `user@example.com` |
| `tool_name` | string | 호출된 도구 이름 | `file_write`, `api_call`, `shell_exec` |
| `tool_action` | string | 도구가 수행한 작업 | `create`, `read`, `update`, `delete`, `execute` |
| `tool_target` | string | 작업 대상 | `/path/to/file`, `https://api.example.com` |
| `auth_context` | string | 권한/역할 요약 | `role:developer, scope:project-x` |
| `input_ref` | string | 입력에 대한 해시 또는 URI (내용 자체가 아님) | `sha256:def456...` |
| `output_ref` | string | 출력에 대한 해시 또는 URI (내용 자체가 아님) | `sha256:ghi789...` |
| `decision` | string | 적용된 정책 결정 | `allow`, `block`, `needs_review`, `unknown` |
| `evidence_ref` | string | 관련 증거에 대한 참조 | `urn:evidence:...` |

## 선택적 필드 (SHOULD/MAY)

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `recursion_depth` | number | 중첩된 에이전트 호출의 현재 재귀 깊이 |
| `retry_count` | number | 이 작업의 재시도 횟수 |
| `policy_id` | string | 결정을 트리거한 정책 |
| `prompt_template_id` | string | 프롬프트 템플릿 식별자 |
| `model` | string | 이 작업에 사용된 모델 |
| `latency_ms` | number | 밀리초 단위 지연 시간 |
| `cost_estimate` | number | 이 작업의 예상 비용 |
| `error_code` | string | 작업 실패 시 오류 코드 |

## 안전 참고사항

!!! warning "에이전틱 리스크 가정"
    에이전틱 AI 활동을 로깅할 때 다음 리스크를 가정하세요:

    - **프롬프트 인젝션**: 악의적인 입력이 에이전트 동작을 조작하려 할 수 있음
    - **과잉 권한**: 에이전트가 특정 작업에 의도된 것보다 더 넓은 권한을 가질 수 있음
    - **재귀 루프**: 에이전트가 의도치 않은 재귀 실행 패턴에 진입할 수 있음
    - **혼란된 대리인**: 에이전트가 권한이 없는 당사자를 대신하여 행동하도록 속을 수 있음

    스키마는 사후 인시던트 분석 및 감사 설명을 지원하기 위해 "누가 어떤 권한으로 무엇을 했는지"를 캡처하도록 설계되었습니다. 이러한 리스크를 예방하지는 않으며; 조직은 적절한 가드레일을 구현해야 합니다.

!!! warning "데이터 처리"
    - **비밀, 자격 증명 또는 민감한 콘텐츠를** `input_ref` 또는 `output_ref`에 **포함하지 마세요**.
    - 별도로 저장된 콘텐츠에 대한 해시 참조 또는 보안 URI를 사용하세요.
    - 적절한 접근 통제 및 보존 정책을 적용하세요.

## JSON Schema

다운로드: [agent-activity.schema.json](https://github.com/billyrise/aimo-standard/blob/main/schemas/jsonschema/agent-activity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "event_time", "agent_id", "agent_version", "run_id", "event_type",
    "actor_id", "tool_name", "tool_action", "tool_target", "auth_context",
    "input_ref", "output_ref", "decision", "evidence_ref"
  ],
  "properties": {
    "event_time": { "type": "string", "format": "date-time" },
    "agent_id": { "type": "string", "minLength": 1 },
    "agent_version": { "type": "string", "minLength": 1 },
    "run_id": { "type": "string", "minLength": 1 },
    "event_type": { "type": "string", "enum": ["agent_run", "tool_call", "tool_result", "escalation"] },
    "actor_id": { "type": "string", "minLength": 1 },
    "tool_name": { "type": "string", "minLength": 1 },
    "tool_action": { "type": "string", "minLength": 1 },
    "tool_target": { "type": "string", "minLength": 1 },
    "auth_context": { "type": "string", "minLength": 1 },
    "input_ref": { "type": "string", "minLength": 1 },
    "output_ref": { "type": "string", "minLength": 1 },
    "decision": { "type": "string", "enum": ["allow", "block", "needs_review", "unknown"] },
    "evidence_ref": { "type": "string", "minLength": 1 }
  },
  "additionalProperties": true
}
```

## 관련 페이지

- [로그 스키마 인덱스](../)
- [Shadow AI 검색 로그](../shadow-ai-discovery/)
- [최소 증거 요구사항](../../minimum-evidence/)
- [분류체계: UC-010 에이전틱 자동화](../../../standard/current/03-taxonomy/)
