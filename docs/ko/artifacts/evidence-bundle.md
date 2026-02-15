---
description: AIMO 증거 번들 구조. AI 거버넌스 컴플라이언스 및 감사자 제출을 위한 목차, 추적성, 산출물을 포함한 감사 패키지 형식.
---
<!-- aimo:translation_status=translated -->

# 증거 번들

**증거 번들**은 감사 패키지입니다: AI 거버넌스를 위한 설명 가능성과 추적성을 지원하는 구조화된 산출물 세트입니다. 이것은 제품 기능이 아니라 감사자와 컴플라이언스를 위한 제출 형식입니다.

## 번들 구조 및 명명

- **번들 루트 명명**: `{org}_{system}_{period}_{version}`과 같은 일관된 패턴을 사용합니다 (예: `acme_ai-usage_2026-Q1_v1`).
- **필수 파일**: [Evidence Pack 템플릿(EP)](../../standard/current/06-ev-template/)에 맞춘 최소 하나의 증거(EV) 세트, [딕셔너리](../../standard/current/05-dictionary/), 간략한 **요약**(번들의 경영진 요약), 번들 또는 그 내용의 변경에 대한 **변경 로그**(또는 참조).
- **선택적 첨부**: 로그, 검토 기록, 예외 승인, 갱신 기록; 일관된 명명을 유지하고 주요 EV/딕셔너리에서 참조 가능하게 합니다.

## 목차 (TOC)

| 섹션 | 산출물 | 필수? | 목적 | 최소 필드 | 검증 |
| --- | --- | --- | --- | --- | --- |
| 증거 | EV 레코드 (JSON/배열) | 예 | 발생한 내용의 기록; 요청/검토/예외/갱신에 대한 링크 | id, timestamp, source, summary; 선택적 생명주기 참조 | [검증기](../../validator/), aimo-ev.schema.json |
| 딕셔너리 | dictionary.json | 예 | 코드와 차원에 대한 키/레이블/설명 | entries (key, label, description) | aimo-dictionary.schema.json |
| 요약 | summary (문서 또는 필드) | 예 | 감사자를 위한 1페이지 개요 | scope, period, key decisions, exceptions | — |
| 변경 로그 | change_log 또는 참조 | 예 | 번들/콘텐츠 변경의 감사 추적 | id, timestamp, actor, change description, references | — |
| 요청 | 요청 레코드 | 해당시 | 사용을 위한 신청/요청 | id, timestamp, actor/role, scope, rationale | — |
| 검토/승인 | 검토 레코드 | 해당시 | 검토 및 승인 결과 | id, timestamp, actor/role, decision, references | — |
| 예외 | 예외 레코드 | 해당시 | 보완 통제와 만료가 있는 예외 | id, timestamp, scope, expiry, compensating controls, renewal ref | — |
| 갱신 | 갱신 레코드 | 해당시 | 재평가 및 갱신 | id, timestamp, actor/role, decision, references to prior exception/EV | — |

## 규범적 관계: EV 레코드(인덱스)와 Evidence Pack(payload)

이중 구축 및 감사 모호성을 피하기 위해 다음은 **규범**입니다. (1) EV 레코드(JSON)는 **인덱스/원장**(기계 검증 가능한 추적성)입니다. (2) Evidence Pack 파일(EP-01..EP-07 및 매니페스트)은 **payload**입니다. (3) EV 레코드는 `evidence_file_ids`(예: EP-01) 및/또는 해시로 payload를 참조하는 것이 좋습니다(SHOULD). [Validator](../../validator/)는 참조 무결성을 검사합니다. (4) **최소 제출 세트**: EV JSON + Dictionary + Summary + Change Log + Evidence Pack(zip). 문서 유형 EP-01..EP-07은 [Evidence Pack 템플릿](../../standard/current/06-ev-template/)을 참조하세요.

## 추적성

- **안정적인 ID**: 모든 레코드(EV, 요청, 검토, 예외, 갱신, 변경 로그 항목)는 안정적이고 고유한 식별자를 가져야 합니다(MUST).
- **상호 참조**: 요청 → 검토 → 예외(있는 경우) → 갱신을 연결하고 참조 필드(예: `request_id`, `review_id`, `exception_id`, `renewal_id`)를 통해 EV 항목을 이들에 연결합니다.
- **연결**: 감사자가 AI 사용(또는 예외)에서 요청, 승인, 예외 및 그 보완 통제와 만료, 갱신까지의 체인을 따라갈 수 있도록 합니다.

## 감사자의 활용 방법

감사자는 증거 번들을 사용하여 AI 사용이 요청되고, 검토되고, 승인되었는지; 예외가 시간 제한이 있고 보완 통제와 갱신이 있는지; 변경이 기록되어 있는지를 확인합니다. 목차와 추적성 규칙을 통해 필요한 산출물을 찾고 요청, 검토, 예외, 갱신, EV 레코드 전반에 걸쳐 ID와 참조를 따라갈 수 있습니다. 요약은 빠른 개요를 제공하고; 변경 로그는 변경 통제와 책임성을 지원합니다.

MUST 수준 필드와 생명주기 그룹에 대해서는 [최소 증거 요구사항](../minimum-evidence/)을 참조하세요.

## 운영 지침

!!! info "무결성 및 접근 통제"
    AIMO는 특정 통제를 규정하지 않지만, 채택자는 다음을 문서화해야 합니다:
    
    - **접근 역할**: 증거를 생성, 읽기, 업데이트 또는 삭제할 수 있는 사람
    - **보존 정책**: 증거가 얼마나 오래, 어떤 일정에 따라 보존되는지
    - **무결성 메커니즘**: 사용되는 해싱, WORM 스토리지 또는 디지털 서명
    - **감사 추적**: 번들에 대한 접근 및 변경 로그
    
    자세한 지침은 [최소 증거 요구사항 > 무결성 및 접근](../minimum-evidence/#6-integrity-access)을 참조하세요.

## 감사 여정

이 페이지에서 일반적인 감사 여정은 다음과 같이 계속됩니다:

1. **다음**: [최소 증거 요구사항](../minimum-evidence/) — 생명주기별 MUST 수준 체크리스트
2. **그 다음**: [커버리지 맵](../../coverage-map/) — 외부 프레임워크에 대한 매핑
3. **검증**: [검증기](../../validator/) — 구조적 검사 실행
4. **다운로드**: [릴리스](../../releases/) — 릴리스 자산 획득 및 체크섬 확인
