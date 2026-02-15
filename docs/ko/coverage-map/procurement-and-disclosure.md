---
description: 조달·공개 오버레이(영국, 일본). 영국 ATRS, 영국 조달 가이드, 일본 정부 GenAI 조달 및 AI 비즈니스 가이드라인. 참조 매핑만.
---
<!-- aimo:translation_status=translated -->

# 조달 및 공개 오버레이(영국, 일본)

이 페이지는 AIMO 증거와 선정된 **영국** 및 **일본** 조달·공개 프레임워크 간의 **참조 매핑**을 설명합니다. **참조 매핑만**이며, AIMO는 공식 체크리스트나 정부 가이드를 대체하지 않습니다.

## 영국: ATRS 및 AI 조달

| 주제 | AIMO 증거 / 매핑 | 비고 |
| --- | --- | --- |
| **영국 ATRS**(AI 투명성 기록) | Summary, review(책임 소유자), evidence(모델/시스템 설명), dictionary(위험 고려). 프로필: `coverage_map/profiles/uk_atrs_procurement.json`. | 외부 양식에 ATRS형 투명성 기록 첨부 또는 참조; logical_id로 번들 객체에 연결. |
| **영국 조달 가이드** | Request, review, exception; Evidence Bundle로 공급자 평가에 활용. | AIMO 번들로 조달 평가용 증거 구조화; 공식 영국 가이드가 권위. |

## 일본: 정부 GenAI 조달 및 AI 비즈니스 가이드라인

| 주제 | AIMO 증거 / 매핑 | 비고 |
| --- | --- | --- |
| **일본 정부 GenAI 조달 체크리스트** | 체크리스트를 외부 양식으로 첨부(예: payload: JP_PROCUREMENT_CHECKLIST); manifest에서 참조. 프로필: `coverage_map/profiles/jp_gov_genai_procurement.json`. | 참조 매핑만; AIMO는 공식 체크리스트를 대체하지 않음. |
| **AI 비즈니스 가이드라인** | Summary, dictionary; 추적성에 유용할 때 체크리스트 항목을 AIMO 분류체계 코드에 매핑. | 설명 가능성에 활용; 일본 공식 가이드로 확인. |

## 사용 방법

- **외부 양식**: 영국 또는 일본 공식 템플릿/체크리스트를 **그대로** 첨부(PDF, DOC 등), 해시하고 Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) 또는 [EV 템플릿 외부 양식 절](../../standard/current/06-ev-template/)에 나열. manifest 및 커버리지 매핑에서 logical_id로 참조.
- **프로필**: 위 프로필은 선택적 기계 가독 매핑을 정의하며, 법적·계약적 의무를 부과하지 않습니다.

수준은 [적합성](../../conformance/), 오버레이 요약은 [최소 증거 — 규제 오버레이](../../artifacts/minimum-evidence/)를 참조하세요.
