---
description: 조달·공개 오버레이(영국, 일본). 영국 ATRS, 영국 조달 가이드, 일본 정부 GenAI 조달 및 AI 비즈니스 가이드라인. 참조 매핑만.
---
<!-- aimo:translation_status=translated -->

# 조달 및 공개 오버레이(영국, 일본)

이 페이지는 AIMO 증거와 선정된 **영국** 및 **일본** 조달·공개 프레임워크 간의 **참조 매핑**을 설명합니다. 목적은 **AIMO 증거 재사용으로 부담을 줄이는 것**입니다. **참고 매핑만**이며, AIMO는 정부 요구사항의 완전한 준수를 보장하지 않습니다. 아래 공식 출처로 확인하세요.

## 1차 출처

**영국**

- [Algorithmic Transparency Recording Standard (ATRS) Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub) — GOV.UK(템플릿, 가이드, 공개 기록)
- [ATRS 템플릿](https://www.gov.uk/government/publications/algorithmic-transparency-template) — 공공 부문 공식 템플릿
- [ATRS 사용 기관 가이드](https://www.gov.uk/government/publications/guidance-for-organisations-using-the-algorithmic-transparency-standard/algorithmic-transparency-recording-standard-guidance-for-public-sector-bodies) — GOV.UK

**일본**

- [디지털청 — GenAI 조달·활용 가이드](https://www.digital.go.jp/news/3579c42d-b11c-4756-b66e-3d3e35175623) — 디지털청(내각관방)
- [AI 비즈니스 가이드라인](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) — METI / MIC(경제산업성 / 총무성)

## 매핑 표(영국)

| 정부 요구사항(주제) | AIMO 산출물 | Evidence Bundle 내 위치 | 검증기 커버리지 | 비고 |
| --- | --- | --- | --- | --- |
| ATRS — 책임/소유자 | Summary, review | manifest; objects/ (EV, Summary); payload_index | schema_validate_ev | 참고 매핑; 완전 준수 보장 없음. |
| ATRS — 시스템/모델 설명 | Dictionary, EV | objects/; schemas/jsonschema/aimo-dictionary.schema.json | schema_validate_dictionary | 외부 양식에 공식 ATRS 기록 첨부; logical_id로 연결. |
| ATRS — 위험 고려 | Dictionary, request, review, exception | objects/; templates/ev/ | schema_validate_ev | 프로필: `coverage_map/profiles/uk_atrs_procurement.json`. |
| 조달 — 공급자 증거 | request, review, exception; Evidence Bundle | manifest, object_index, payload_index; examples/evidence_bundle_minimal/ | schema_validate_ev | 번들로 증거 구조화; 영국 공식 가이드가 권위. |

## 매핑 표(일본)

| 정부 요구사항(주제) | AIMO 산출물 | Evidence Bundle 내 위치 | 검증기 커버리지 | 비고 |
| --- | --- | --- | --- | --- |
| GenAI 조달 체크리스트(디지털청) | 외부 양식(원문 체크리스트); Dictionary, Summary | payload_index; 외부 양식 절; manifest 참조 | N/A(첨부) | 참고 매핑; 완전 준수 보장 없음. 프로필: `coverage_map/profiles/jp_gov_genai_procurement.json`. |
| AI 비즈니스 가이드라인 — 거버넌스/추적성 | Summary, dictionary, request, review, change_log | objects/; manifest; templates/ev/ | schema_validate_dictionary, schema_validate_ev | 추적성에 유용할 때 목록 항목을 AIMO 분류체계에 매핑. |
| 위험/책임 문서 | Dictionary, EV, review, exception | objects/; schemas/jsonschema/ | schema_validate_ev | 디지털청·METI/MIC 공식 가이드로 확인. |

## 영국: ATRS 및 AI 조달(요약)

| 주제 | AIMO 증거 / 매핑 | 비고 |
| --- | --- | --- |
| **영국 ATRS**(AI 투명성 기록) | Summary, review(책임 소유자), evidence(모델/시스템 설명), dictionary(위험 고려). 프로필: `coverage_map/profiles/uk_atrs_procurement.json`. | 외부 양식에 ATRS형 투명성 기록 첨부 또는 참조; logical_id로 번들 객체에 연결. |
| **영국 조달 가이드** | Request, review, exception; Evidence Bundle로 공급자 평가에 활용. | AIMO 번들로 조달 평가용 증거 구조화; 공식 영국 가이드가 권위. |

## 일본: 정부 GenAI 조달 및 AI 비즈니스 가이드라인(요약)

| 주제 | AIMO 증거 / 매핑 | 비고 |
| --- | --- | --- |
| **일본 정부 GenAI 조달 체크리스트** | 체크리스트를 외부 양식으로 첨부(예: payload: JP_PROCUREMENT_CHECKLIST); manifest에서 참조. 프로필: `coverage_map/profiles/jp_gov_genai_procurement.json`. | 참조 매핑만; AIMO는 공식 체크리스트를 대체하지 않음. |
| **AI 비즈니스 가이드라인** | Summary, dictionary; 추적성에 유용할 때 체크리스트 항목을 AIMO 분류체계 코드에 매핑. | 설명 가능성에 활용; 일본 공식 가이드로 확인. |

## 사용 방법

- **외부 양식**: 영국 또는 일본 공식 템플릿/체크리스트를 **그대로** 첨부(PDF, DOC 등), 해시하고 Evidence Bundle [payload_index](../../standard/current/09-evidence-bundle-structure/) 또는 [EV 템플릿 외부 양식 절](../../standard/current/06-ev-template/)에 나열. manifest 및 커버리지 매핑에서 logical_id로 참조.
- **프로필**: 위 프로필은 선택적 기계 가독 매핑을 정의하며, 법적·계약적 의무를 부과하지 않습니다.

수준은 [적합성](../../conformance/), 오버레이 요약은 [최소 증거 — 규제 오버레이](../../artifacts/minimum-evidence/)를 참조하세요.
