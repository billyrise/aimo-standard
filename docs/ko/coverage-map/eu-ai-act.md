---
description: AIMO Standard와 EU AI 법 매핑. AIMO 분류체계 코드와 EU AI 법 위험 범주·요구사항 간 추적성.
---
<!-- aimo:translation_status=translated -->

# EU AI 법 매핑

> 추적성 바로가기: 분류체계 → 최소 증거 → 검증기 → 인간 감독 프로토콜.

- [분류체계](../../standard/current/03-taxonomy/)
- [최소 증거 요구사항](../../artifacts/minimum-evidence/)
- [로그 스키마](../../artifacts/log-schemas/)
- [검증기](../../validator/)
- [인간 감독 프로토콜](../../governance/human-oversight-protocol/)

이 페이지는 선정된 EU AI 법 주제(문서화, 기록 유지, 위험 관리, 인간 감독, 투명성)를 AIMO 증거 및 산출물에 매핑합니다. 개요 수준이며 **법적 조언**이나 적합성 보장을 구성하지 않습니다. 공식 법문으로 확인하세요.

**참조:** 규칙 (EU) 2024/1689(인공지능법). 아래 조 번호는 해당 규칙을 가리킵니다.

## 매핑 테이블

| 프레임워크 참조 / 주제 | AIMO 증거 / AIMO 내 위치 | 증거 번들 / 최소 증거 | 산출물 및 검증 | 비고 |
| --- | --- | --- | --- | --- |
| 제4조 – AI 리터러시 | [범위](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | 횡단; 조직 역량/교육 증거(개요). 법적 조언 아님. 공식 텍스트로 확인. |
| 제9조 – 위험 관리 시스템 | [범위](../../standard/current/02-scope/) | request, review, exception, renewal | templates/ev/ | 고위험 AI 시스템(제3편). 법적 조언 아님. 공식 텍스트로 확인. |
| 제10조 – 데이터 및 데이터 거버넌스 | [사전](../../standard/current/05-dictionary/) | Dictionary, EV | schemas/jsonschema/; schema_validate_dictionary | 법적 조언 아님. 공식 텍스트로 확인. |
| 제11조 – 기술 문서(고위험) | [EV 템플릿](../../standard/current/06-ev-template/), [증거 번들](../../artifacts/evidence-bundle/) | EV, Dictionary, Summary; request, review | schemas/jsonschema/, templates/ev/; **부록 IV**: [예시 > EU 부록 IV 샘플](../../examples/) (`examples/evidence_bundle_v01_annex_iv_sample/`); 프로필: `coverage_map/profiles/eu_ai_act_annex_iv.json`. 샘플 번들은 규범 준수(signatures/, hashes/, 부록 IV 중심 기술 문서 payload). 예시 참조(추가 샘플은 향후 릴리스). | 개요만; 법적 조언 아님. 공식 텍스트로 확인. |
| 제12조 – 기록 유지 | [증거 번들](../../artifacts/evidence-bundle/), [최소 증거](../../artifacts/minimum-evidence/) | EV, change_log, request, review | examples/evidence_bundle_minimal/; schema_validate_ev | 법적 조언 아님. 공식 텍스트로 확인. |
| 제13조 – 배포자/사용자에 대한 투명성 및 정보 제공 | [범위](../../standard/current/02-scope/) | Summary, EV; review | templates/ev/ | 고위험 맥락. 법적 조언 아님. 공식 텍스트로 확인. |
| 제14조 – 인간 감독 | [최소 증거](../../artifacts/minimum-evidence/) | review, exception | templates/ev/ev_template.md | 법적 조언 아님. 공식 텍스트로 확인. |
| 제15조 – 정확성, 견고성, 사이버보안 | [최소 증거](../../artifacts/minimum-evidence/) | EV(증거 코드/위험 코드, 개요) | templates/ev/ | 개요 매핑만. 법적 조언 아님. 공식 텍스트로 확인. |
| 제17조 – 품질 관리 시스템 | [범위](../../standard/current/02-scope/) | Summary, review(조직 프로세스) | templates/ev/ | 제9조(위험 관리 시스템)와 구별. 법적 조언 아님. 공식 텍스트로 확인. |
| 투명성 의무(사용 사례 의존) | [범위](../../standard/current/02-scope/), [최소 증거](../../artifacts/minimum-evidence/) | Summary, EV; review | templates/ev/ | 적용 규정은 사용 사례(제한적 위험, 배포자 의무 등)에 따름. 법적 조언 아님. 공식 텍스트로 확인. |
| GPAI 모델 의무 | [EV 템플릿](../../standard/current/06-ev-template/), [증거 번들](../../artifacts/evidence-bundle/) | EV 템플릿, 증거 번들(증거 구조화 프레임) | schemas/jsonschema/; schema_validate_ev | AIMO는 증거 정리 프레임을 제공하며; 실제 의무는 규칙으로 정의. 법적 조언 아님. 공식 텍스트로 확인. |
| 전문 – 책임 | [증거 번들](../../artifacts/evidence-bundle/) | EV, request, review, change_log | examples/evidence_bundle_minimal/; schema_validate_ev | 법적 조언 아님. 공식 텍스트로 확인. |

## 시행일 / 적용(개요)

아래는 **EU 공식 일정**(AI 법 서비스 데스크/위원회)에 맞춘 개요입니다. **법적 조언이 아니며** 정확성을 보장하지 않습니다. **공식 법문**과 관할 기관으로 반드시 확인하세요.

| 단계 | 날짜 | 적용 내용(개요) |
| --- | --- | --- |
| 발효 | 2024년 8월 | 규칙 발효; 대부분의 실질적 의무는 아직 미적용. |
| 일반 규정 및 금지 | 2025년 2월 2일 | 금지 관행(허용 불가 위험); AI 리터러시 관련 규정 일부. |
| GPAI 규칙 및 거버넌스 | 2025년 8월 2일 | 지정 기관, GPAI, 거버넌스, 비밀 유지, 제재; 실무 규범. |
| 주요 규칙 및 부록 III 고위험 및 제50조 투명성 | 2026년 8월 2일 | 고위험 AI 시스템(부록 III) 완전 적용, 제50조 투명성 의무. |
| 규제 제품에 내장된 고위험 | 2027년 8월 2일 | EU 제품 법률 대상 제품에 내장된 고위험 AI 시스템. |

## 조화 표준 및 적합성 추정(제40조)

AI 법에 따라 EU 공보에 **조화 표준**이 공포되면, 이에 대한 준수는 해당 요구사항에 대한 **적합성 추정**을 제공할 수 있습니다. 정확한 목록과 날짜는 표준화 작업과 공보 공고에 따릅니다. AIMO 매핑은 참고용이며 적합성 추정을 부여하지 않습니다. 현황은 위원회 [AI 법 표준화](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) 페이지 및 아래 **참고 문헌**을 참조하세요.

## 2026년 AI 사무국 가이드라인(이행 세부사항)

유럽 위원회는 **AI 사무국**이 2026년에 **실무 가이드라인**을 마련할 것이라고 밝혔으며, 다음을 포함합니다:

- 고위험 분류
- 제50조(투명성) 이행
- 사고 보고
- QMS 관련 요소

이 가이드라인은 AIMO 프로필 및 커버리지 매핑의 **업데이트 트리거**입니다: 공포 후 채택자는 증거와 매핑을 최신 공식 가이드에 맞춰야 합니다. AIMO는 해당 가이드라인의 해석이나 준수를 보장하지 않습니다.

!!! warning "법적 조언 아님"
    이 페이지는 설명 목적으로만 제공됩니다. 적용 범위와 날짜는 공식 규칙 및 시행·개정 법률로 확인하세요. AIMO는 법적 조언이나 준수 보장을 제공하지 않습니다.

!!! note "법적 고지 / 참고 매핑"
    이 페이지는 **참고용**입니다. 법적 해석은 공식 규칙(EUR-Lex) 및 유럽 위원회 공간에 의거해야 합니다. AIMO는 법적 조언이나 준수 보장을 제공하지 않습니다.

## 참고 문헌

**1차 출처**

- [규칙 (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)(EUR-Lex) — 인공지능법(법문)
- [EU AI 법 이행 일정](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — 유럽 위원회 AI 법 서비스 데스크(이행 일정)
- [AI 법 표준화](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) — 유럽 위원회 디지털 전략(조화 표준, 적합성 추정)

**기타**

- 유럽 위원회 / AI 사무국 — 가이드라인 및 일정(서비스 데스크 및 위원회 뉴스에서 최신 URL 확인)
- [EPRS — EU AI 법 이행](https://www.europarl.europa.eu/thinktank/) — 의회 브리핑(참고)
