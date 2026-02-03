---
description: AIMO 증거 팩 템플릿 및 사용 가이드. 인덱스 관리 및 감사 준비 형식으로 AI 거버넌스 증거를 문서화하기 위한 구조.
---

# Evidence Pack 템플릿 (EP)

이 섹션은 증거 팩 템플릿과 그 사용을 정의합니다. 증거 팩은 AI 시스템에 대한 거버넌스 및 컴플라이언스를 입증하는 문서 모음입니다.

## 네임스페이스: Evidence Pack 문서 유형(EP) vs Taxonomy Log/Event Type(LG)

> **중요**: **EP-01..EP-07**은 *문서 유형*(증거 팩 파일 유형)을 나타냅니다. **LG-001, LG-002, …**는 [분류체계](./03-taxonomy.md)에서 *로그/기록 유형*(요청 레코드, 검토/승인 레코드 등)을 나타냅니다. **EV-**는 Evidence 산출물 ID 전용입니다. EP는 팩 구조, LG는 라이프사이클 증거 분류에 사용합니다.

## 핵심 원칙: 인덱스 및 차이 관리

중요한 것은 개별 제출물의 내용만이 아니라 증거 항목 전반에 걸친 **인덱스** 및 **차이 관리**입니다.

증거 팩은 AI 시스템을 거버넌스 산출물에 연결하는 인덱스 역할을 합니다. 가치는 다음에 있습니다:

1. **추적성**: 시간에 걸쳐 결정, 승인 및 변경 연결
2. **감사 가능성**: 감사자가 증거 구조를 탐색할 수 있게 함
3. **유지 관리 가능성**: 무엇이 언제 왜 변경되었는지 추적

## MVP 증거 세트 (EP-01 ~ EP-07)

다음 7가지 **Evidence Pack 문서 유형**(EP)이 AI 거버넌스를 입증하기 위한 **최소 실행 가능 세트**를 형성합니다. 각각은 문서 템플릿이며, 분류체계 **LG** 코드(요청 레코드, 검토/승인 등)는 번들 내 다른 곳과 `codes.LG`에서 *로그/기록* 증거 분류에 사용됩니다.

| ID | 문서 유형 | 목적 |
| --- | --- | --- |
| EP-01 | 시스템 개요 | AI 시스템과 그 목적 문서화 |
| EP-02 | 데이터 흐름 | 시스템을 통한 데이터 이동 매핑 |
| EP-03 | 인벤토리 | AI 자산 카탈로그 유지 |
| EP-04 | 리스크 및 영향 평가 | 리스크 평가 및 문서화 |
| EP-05 | 통제 및 승인 | 통제 및 승인 레코드 문서화 |
| EP-06 | 로깅 및 모니터링 | 로깅 및 모니터링 설정 정의 |
| EP-07 | 인시던트 및 예외 | 인시던트 및 예외 추적 |

## 증거 팩 매니페스트

각 증거 팩에는 다음을 포함하는 매니페스트 파일이 있어야 합니다(MUST):

### 필수 메타데이터

| 필드 | 설명 | 필수 |
| --- | --- | --- |
| `pack_id` | 고유 식별자 (예: EP-EXAMPLE-001) | 예 |
| `pack_version` | 팩의 SemVer 버전 | 예 |
| `taxonomy_version` | 사용된 AIMO 분류체계 버전 | 예 |
| `created_date` | 팩 생성 날짜 | 예 |
| `last_updated` | 마지막 업데이트 날짜 | 예 |
| `owner` | 책임 당사자 | 예 |

### AIMO 코드 (8개 차원)

각 증거 팩에는 8개 차원 모두의 코드가 포함되어야 합니다(MUST). **LG** 차원은 이 팩에 적용되는 *분류체계* 로그/기록 유형(예: 요청 레코드, 검토/승인)을 나열합니다. 문서 유형 코드가 아닙니다. 문서 유형은 `evidence_files[].file_id`(EP-01..EP-07)로 지정됩니다.

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
    "LG": ["LG-001", "LG-002", "LG-008", "LG-009"]
  }
}
```

### 증거 파일 목록

각 항목은 **file_id**(EP-01..EP-07)로 팩 내 문서를 식별합니다. 선택적으로 **ev_codes**에 해당 문서가 지원하는 분류체계 LG 코드(LG-xxx)를 나열할 수 있습니다.

```json
{
  "evidence_files": [
    {
      "file_id": "EP-01",
      "filename": "EP-01_system_overview.md",
      "title": "System Overview",
      "required": true
    }
  ]
}
```

## 템플릿 구조

각 증거 템플릿에는 다음이 포함됩니다:

1. **필수 메타데이터 블록** - pack_id, version, taxonomy_version, dates, owner
2. **AIMO 코드 테이블** - 적용 가능한 코드가 있는 8개 차원 모두
3. **콘텐츠 섹션** - 도메인별 문서 섹션
4. **참조** - 관련 증거에 대한 링크
5. **수정 이력** - 변경 추적

### 템플릿 헤더 예시

```markdown
# EP-01: 시스템 개요

---

## 필수 메타데이터

| 필드 | 값 |
| --- | --- |
| **pack_id** | `EP-EXAMPLE-001` |
| **pack_version** | `0.1.0` |
| **taxonomy_version** | `0.1.0` |
| **created_date** | `2026-01-31` |
| **last_updated** | `2026-01-31` |
| **owner** | `AI 거버넌스 팀` |

---

## AIMO 코드 (8개 차원)

| 차원 | 코드 | 레이블 |
| --- | --- | --- |
| **FS** | `FS-001` | 최종 사용자 생산성 |
| **UC** | `UC-001` | 일반 Q&A |
| **DT** | `DT-002` | 내부 |
| **CH** | `CH-001` | 웹 UI |
| **IM** | `IM-001` | 독립형 |
| **RS** | `RS-001` | 데이터 유출 |
| **OB** | `OB-001` | 효율성 |
| **LG** | `LG-001`, `LG-002` | 요청 레코드, 검토/승인 레코드 |
```

## 다운로드

### 템플릿

증거 팩 템플릿은 다음에서 이용 가능합니다:

매니페스트에서 **file_id** EP-01..EP-07을 사용하세요. 파일명은 EP-01_... 또는 하위 호환용 EV-01_...를 사용할 수 있습니다.

- `source_pack/04_evidence_pack/templates/EV-01_system_overview.md` → file_id **EP-01**
- `source_pack/04_evidence_pack/templates/EV-02_data_flow.md` → file_id **EP-02**
- `source_pack/04_evidence_pack/templates/EV-03_inventory.md` → file_id **EP-03**
- `source_pack/04_evidence_pack/templates/EV-04_risk_impact.md` → file_id **EP-04**
- `source_pack/04_evidence_pack/templates/EV-05_controls_approvals.md` → file_id **EP-05**
- `source_pack/04_evidence_pack/templates/EV-06_logging_monitoring.md` → file_id **EP-06**
- `source_pack/04_evidence_pack/templates/EV-07_incident_exception.md` → file_id **EP-07**

### 스키마 및 예제

- 스키마: `source_pack/04_evidence_pack/schemas/evidence_pack_manifest.schema.json`
- 예제: `source_pack/04_evidence_pack/examples/evidence_pack_manifest.example.json`

다운로드 가능 패키지는 [릴리스](../../releases/index.md)를 참조하세요.

## 배포 모델

> **참고**: 주요 배포 대상은 개별 기업이 아닌 **감사법인 및 시스템 통합자**(템플릿 배포자)입니다.

템플릿은 다음을 위해 설계되었습니다:

1. 감사자와 컨설턴트가 표준 산출물로 채택
2. 소스 귀속이 보존된 상태로 기업에 배포
3. AIMO 표준과 함께 버전 관리

기업은 표준 버전과의 연결을 유지하는 감사자, 컨설턴트 또는 내부 거버넌스 팀을 통해 템플릿을 받습니다.

## 참조

- [분류체계](./03-taxonomy.md) - 차원 정의
- [코드](./04-codes.md) - 코드 형식
- [검증기](./07-validator.md) - 검증 규칙
- [증거 번들](../../artifacts/evidence-bundle.md) - 번들 구조
