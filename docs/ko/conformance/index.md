---
description: AIMO Standard 적합성 수준. 조직의 적합성 주장 방식, 증거 요구사항, 각 수준이 AI 거버넌스에서 의미하는 바.
---
<!-- aimo:translation_status=translated -->

# 적합성

!!! warning "중요: 인증이 아니며, 보증이 아니며, 법·규제 적합성 주장이 아님"
    AIMO Standard는 **증거 패키징 및 검증 형식**을 정의합니다. 법률 또는 표준 준수를 인증하지 않습니다.
    감사 및 보증 의견은 독립 감사인과 채택 기관의 책임입니다.
    **적절한 주장 예:** "Evidence Bundle은 AIMO Standard v0.1.2에 따라 작성되었으며 AIMO 검증기로 구조 검증되었습니다."
    <!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
    **부적절한 주장 예:** "EU AI 법 준수", "ISO 42001 인증", "정부 승인".
    <!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

AIMO Standard는 **보증/감사 인수인계/지속 증거** 계층으로 위치합니다. 채택자와 감사인이 구조화된 증거로 작업할 수 있도록 증거 패키징, 검증기, 추적성을 제공합니다. AIMO는 **인증 기관이 아닙니다.** 인증·적합성 결정은 인정 인증 기관, 감사인, 채택 기관의 책임입니다.

이 계층은 패키징과 추적성을 위한 **내부 증거 성숙도 수준**입니다. 인증이 아니며, 보증 의견이 아니며, 법·규제 적합성이 **아닙니다**.

## 호환성 주장(ISO/NIST/EU AI 법)

다음 **참고 매핑**은 AIMO 증거 및 산출물을 외부 프레임워크에 연결합니다. 설명 가능성과 감사 인수인계를 지원하며; 인증을 부여하거나 준수를 보장하지 **않습니다**. 각 프레임워크의 권위 본문과 대조하여 확인하세요.

- [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) — ISO/IEC 42001(AI 관리 시스템) 매핑
- [Coverage Map — NIST AI RMF](../coverage-map/nist-ai-rmf/) — NIST AI Risk Management Framework 매핑
- [Coverage Map — EU AI 법](../coverage-map/eu-ai-act/) — EU AI 법 주제 매핑(상위 수준; 법적 조언 아님)

1차 출처 및 주장 문구는 각 Coverage Map 페이지와 [책임 경계](../governance/responsibility-boundary/)에 문서화되어 있습니다.

## 비주장 사항(AIMO가 주장하지 않는 것)

- AIMO는 ISO/IEC 42001, NIST AI RMF, EU AI 법 또는 기타 프레임워크에 대한 준수 인증을 **하지 않습니다**.
- AIMO는 규제·법적 준수를 **보장하지 않습니다**.
- AIMO는 보증 의견이나 법적 조언을 **제공하지 않습니다**.
- AIMO는 조직이 외부 요구사항을 충족하는지 **판단하지 않습니다**; 이는 채택자, 감사인, 인증 기관의 책임입니다.

!!! note "계층 이름 별칭"
    최상위 계층은 비공식 논의에서 이전에 "Gold"로 불렸습니다; **공식 계층 이름은 Audit-Ready**입니다.

## AIMO 적합성 프레임워크(AIMO-MS / AIMO-Controls / AIMO-Audit)

| 구성요소 | 설명 | 증거 기대 |
| --- | --- | --- |
| **AIMO-MS** | 관리 시스템 지향 구조: ISO/IEC 42001형 통제를 지원할 수 있는 정책, 역할, PDCA 정렬 산출물. | Request, review, exception, renewal, change log; Summary 및 Dictionary. |
| **AIMO-Controls** | 생명주기 및 무결성 통제: request→review→exception→renewal, 해시, 서명([증거 번들 구조](../../standard/current/09-evidence-bundle-structure/) 준거). | Object_index, payload_index, hash_chain, signing; 생명주기 기록. |
| **AIMO-Audit** | 감사 인수 준비: 검증기 통과, 체크섬, 선택적 attestation 및 감사 인수 인덱스. | 검증기 출력, bundle_id, producer identity, 선택적 서명 메타데이터 및 인수 인덱스. |

증거 기대는 [최소 증거 요구사항](../artifacts/minimum-evidence/) 및 [증거 번들](../artifacts/evidence-bundle/)을 참조하세요.

## 적합성 수준(AIMO 전용)

### 수준 1 — Foundation

**목적:** 추적 가능한 기준선. 번들을 식별 가능·무결성 검증 가능·검증기 검사 대상으로 만드는 최소 집합.

| 항목 | 요구사항 |
| --- | --- |
| **필수 산출물** | [증거 번들](../artifacts/evidence-bundle/) 구조(manifest.json, objects/, 사양별 payload_index); [검증기](../validator/) 통과; [최소 증거](../artifacts/minimum-evidence/) 링크. |
| **전형적 감사 질문** | 범위는 무엇인가? 번들을 누가 작성했는가? 해시를 검증할 수 있는가? |
| **전형적 격차** | manifest 메타데이터(bundle_id, created_at, producer) 누락; 검증기 미실행 또는 미첨부. |

### 수준 2 — Operational

**목적:** 운영 통제 증거. Foundation 위에 생명주기 궤적과 모니터링을 구축.

| 항목 | 요구사항 |
| --- | --- |
| **필수 산출물** | Foundation MUST 항목 전부; 생명주기 통제 궤적(request/승인, review, exception 또는 "예외 없음", renewal 일정); 최소 1개의 모니터링 산출물(사고 로그 또는 정기 점검 또는 인간 감독 샘플링); 무결성 링크가 있는 change log; 증명 대 보증 경계 진술. |
| **전형적 감사 질문** | 사용 승인자는 누구인가? 예외는 어떻게 추적하는가? 마지막 검토는 언제인가? |
| **전형적 격차** | review/승인이 request에 연결되지 않음; 모니터링 산출물 없음; change log가 영향 객체를 참조하지 않음. |

### 수준 3 — Audit-Ready

**목적:** 감사 인수 품질. 완전한 attestation, 재현성, 외부 양식 슬롯.

| 항목 | 요구사항 |
| --- | --- |
| **필수 산출물** | Operational MUST 항목 전부; manifest를 포함하는 최소 1개의 디지털 서명(서명자 identity + 알고리즘); TSA 또는 "TSA 없음" 진술; 재현 패킷(정확한 검증기 명령, 예상 출력, 환경 메타데이터); 공식 템플릿/체크리스트를 그대로 첨부·상호 참조한 외부 양식 절; 유계 완전성 진술; 1페이지 감사 인수 인덱스(산출물 → 해시 → producer → 날짜). |
| **전형적 감사 질문** | 감사인이 검증을 재실행하는 방법은? 외부 체크리스트는 어디에 있으며 번들에 어떻게 매핑하는가? |
| **전형적 격차** | 서명은 있으나 서명자/알고리즘이 문서화되지 않음; 인수 인덱스 없음; 외부 양식이 해시되지 않았거나 manifest에서 참조되지 않음. |

## 수준별 최소 증거(요약)

| 수준 | MUST(요약) |
| --- | --- |
| **Foundation** | 번들 구조(manifest, object_index, payload_index); 참조 객체의 sha256; bundle_id, created_at, producer; 검증기 실행 + 버전; 증거 사전 기준(시스템명, 소유자, 목적, 데이터 범주, 생명주기 단계); 접근·보존 진술(대상, 기간, 저장 유형, 위변조 증거). SHOULD: 최소 change log 항목. |
| **Operational** | Foundation MUST 전부; 생명주기 궤적(request/승인, review, exception 또는 "없음", renewal + 최근 renewal); ≥1 모니터링 산출물; change log 항목이 영향 객체 참조; 명시적 증명 대 보증 경계 진술. |
| **Audit-Ready** | Operational MUST 전부; manifest에 대한 ≥1 서명(서명자 identity + 알고리즘); TSA 또는 "TSA 없음"; 재현 패킷; 외부 양식 나열 및 상호 참조; 유계 완전성 진술; 감사 인수 인덱스. |

서명 **존재**(manifest를 대상으로 하는 최소 1개 서명)는 규범적 [증거 번들 구조](../../standard/current/09-evidence-bundle-structure/)에 따라 모든 번들에 필요합니다. **Audit-Ready**는 제3자가 재검증할 수 있도록 더 엄격한 **암호학적 attestation**(서명자 identity, 알고리즘, TSA 진술, 재검증 지침)을 추가합니다.

## ISO/IEC 42001 매핑(참고)

다음 표는 AIMO 산출물이 전형적인 ISO/IEC 42001 조항군의 증거를 **어떻게 지원하는지** 보여줍니다. 참고용이며 인증이나 적합성을 의미하지 않습니다.

| ISO/IEC 42001 조항군 | 증거를 지원하는 AIMO 산출물 |
| --- | --- |
| 조직의 맥락 | Summary, Dictionary, scope_ref |
| 리더십 / 정책 | Summary, review, dictionary |
| 기획(위험, 목표) | request, review, exception, EV, Dictionary |
| 지원(자원, 역량, 문서) | Summary, review, EV, change_log |
| 운영 | EV, request, review, exception; 운영 통제 |
| 성과 평가(모니터링, 내부 감사, 경영 검토) | EV, change_log, review, renewal |
| 개선 | exception, renewal, change_log |

자세한 내용은 [Coverage Map — ISO/IEC 42001](../coverage-map/iso-42001/) 및 [ISO 42001 인증 준비 도구 키트](../artifacts/iso-42001-certification-readiness-toolkit/)를 참조하세요.

## 주장 문구 템플릿(과대 주장 방지)

실제 수행한 내용을 정확히 기술한 주장만 사용하세요. 인증과 법적 준수는 채택자와 인정 기관의 책임입니다.

**수용 가능(예)**

- "당사는 AIMO Standard v0.1.2에 대한 AIMO 적합(수준 2)입니다; ISO 인증이나 법적 준수를 의미하지 않습니다."
- "AIMO 산출물로 ISO/IEC 42001 준비를 지원합니다; 인증 결정은 인정 인증 기관에 있습니다."
- "Evidence Bundle은 AIMO Standard v0.1.2에 따라 작성되었으며 AIMO 검증기로 구조 검증되었습니다."

<!-- UNACCEPTABLE_CLAIMS_EXAMPLES -->
**수용 불가(예)**

- "EU AI 법 준수"(AIMO는 규제 준수를 인증하지 않습니다.)
- "ISO 42001 인증"(인증은 인정 인증 기관이 발급하며 AIMO가 아닙니다.)
- "정부 승인"(AIMO는 정부 승인 제도가 아닙니다.)
<!-- /UNACCEPTABLE_CLAIMS_EXAMPLES -->

## 관련 페이지

- [Trust Package](../governance/trust-package/) — 감사인용 통합 진입점
- [Responsibility Boundary](../governance/responsibility-boundary/) — AIMO가 제공하는 것·하지 않는 것
- [Standard (Current)](../standard/current/) — 규범 요구사항
- [Artifacts](../artifacts/) — 증거 구조 및 최소 증거
- [Validator](../validator/) — 구조 검증
