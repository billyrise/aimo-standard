---
description: 증거 번들 커버리지 맵 템플릿(v0.1). 감사자용 1페이지 요약 — 범위, 증거 유형, 통제 매핑, 제외, 무결성 증명.
---
<!-- aimo:translation_status=translated -->

# 증거 번들 커버리지 맵(템플릿)

!!! info "참고 — 권장 사례"
    이 페이지는 1페이지 증거 번들 커버리지 맵의 **권장 사례 템플릿**을 정의합니다. 표준의 **규범적 요건이 아닙니다**. 번들이 무엇을 포함·미포함하는지 감사 인수인계용으로 문서화할 때 사용합니다. 프레임워크 등에 대한 참조는 안정적이며, 채택은 구현자 재량입니다.

---

## 1. 범위

| 항목 | 설명 |
|------|--------------|
| **범위 참조** | 번들 manifest의 `scope_ref`(예: `SC-001`). 이 번들을 선언된 범위에 연결합니다. |
| **Bundle ID** | `bundle_id`(UUID) — 이 번들의 고유 식별자. |
| **Bundle 버전** | `bundle_version`(SemVer) — 번들 버전. |
| **기간 / 스냅샷** | 선택: 이 번들이 나타내는 기간 또는 스냅샷 일자(예: 2026-Q1, as-of 2026-02-03). |

---

## 2. 증거 유형(EV / objects vs payloads)

| 카테고리 | 내용 | v0.1 최소 예 |
|----------|----------|------------------------|
| **object_index** | 열거 객체(메타데이터, 인덱스). 각 항목: `id`, `type`, `path`, `sha256`. | 예: `objects/index.json`(index 유형). |
| **payload_index** | 페이로드 파일(루트 EV JSON, Evidence Pack 파일). 각 항목: `logical_id`, `path`, `sha256`, `mime`, `size`. | 예: `payloads/root.json`(루트 AIMO EV JSON). |
| **EV 유형** | 증거 기록(루트 또는 링크된 페이로드 내) — request, review, exception, renewal, change log. | [Evidence Pack 템플릿](../../standard/current/06-ev-template/) 및 [최소 증거 요구사항](../minimum-evidence/)에 맞춤. |

*구현자는 object_index와 payload_index를 확장할 수 있음. 경로는 번들 루트 내에 두고 [Evidence Bundle 루트 구조(v0.1)](../../standard/current/09-evidence-bundle-structure/)를 충족해야 함.*

---

## 3. 통제 매핑(참고만)

외부 프레임워크에 대한 매핑은 **참고용**이며, 표준은 특정 규제 준수를 강제하지 않습니다.

| 프레임워크 | 이 번들에서의 사용 | 참조 |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | 선택: 이 번들이 지원하는 AI MS 주제 문서화. | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | 선택: 고수준 문서/기록 유지 정렬. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | 선택: Govern, Map, Measure, Manage 매핑. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | 선택: Model Documentation Form; External Forms에 첨부하고 logical_id로 참조. | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/); 프로파일 `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | 선택: GenAI 프로파일(AI 600-1) 산출물. | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/); 프로파일 `nist_ai_600_1_genai.json` |
| **UK ATRS** | 선택: ATRS 기록, 조달 평가. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); 프로파일 `uk_atrs_procurement.json` |
| **JP Gov GenAI 조달** | 선택: JP 조달 체크리스트, AI Business Guidelines. | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/); 프로파일 `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | 선택: 변경 관리, 접근, 로깅, 무결성. | [Coverage Map → ISMS](../../coverage-map/isms/) |

*「이 번들에서의 사용」은 제출별로 기입. 표준은 특정 통제 적용 범위를 요구하지 않음.*

### External Forms 및 manifest 참조

**External Forms**(공식 템플릿/체크리스트를 그대로 첨부)는 번들의 **payload_index**에 안정적인 `logical_id`, `path`, `sha256`, `mime`, `size`로 나열해야 합니다. 감사자는 manifest에서 파일을 추적하고 해시를 검증할 수 있습니다. [EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) 및 [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index) 참조.

---

## 4. 제외 / 가정

| 영역 | 이 번들이 **다루지 않는** 내용(예시 행 — 제출별 조정) |
|------|-------------------------------------------------------------------------------|
| **제외** | 예: 범위 외 시스템/사용 사례, 증거 없는 제3자 구성요소, 이 번들 기간 외. |
| **가정** | 예: Dictionary/분류체계 버전, 사용한 validator/스키마 버전, 보관·보존은 구현 정의. |
| **한계** | 예: v0.1에서 서명 검증은 범위 외; 규제에 대한 법적 해석 없음. |

*플레이스홀더를 제출별 제외·가정으로 교체.*

---

## 5. 무결성 증명 요약(v0.1)

| 요소 | 제공 내용(v0.1 규범) |
|---------|----------------------------------|
| **manifest.json** | 존재하고 스키마 유효; `object_index`, `payload_index`, `hash_chain`, `signing` 포함. |
| **sha256** | `object_index`와 `payload_index`의 모든 파일에 64자 소문자 hex sha256 선언; Validator가 내용 일치 검사. |
| **인덱스 존재** | 나열된 경로는 번들 루트 아래에 존재; 경로 순회(`../` 또는 선행 `/`) 없음. |
| **서명 존재** | `signatures/`에 최소 1개 서명 파일; manifest는 `signing.signatures[]`로 `path`와 `targets` 참조(v0.1에서 targets에 `manifest.json` MUST 포함). v0.1에서 암호 검증은 범위 외. |
| **Hash chain** | manifest의 `hash_chain`: `algorithm`, `head`(64자 hex), `path`(`hashes/` 하위 파일), `covers`(v0.1에서 `manifest.json`과 `objects/index.json` MUST 포함). `hash_chain.path` 파일 존재. |

*이 표는 [Validator](../../validator/)가 v0.1 번들에 대해 검사하는 무결성 보장 요약. Custody(저장, 접근 통제, 보존)는 구현 정의.*

---

## Coverage Map(YAML) vs 프로파일(JSON)

| 산출물 | 상태 | 목적 |
|----------|--------|---------|
| **Coverage Map YAML**(`coverage_map/coverage_map.yaml` 등) | **참고** | AIMO 증거/산출물과 외부 프레임워크(ISO 42001, NIST AI RMF, EU AI Act 등) 간 고수준 매핑 주제, 설명 가능성용. 규범적 검증 요건을 부과하지 않음. |
| **Profile JSON**(`coverage_map/profiles/*.json`) | **규범** | `schemas/jsonschema/aimo-profile.schema.json`로 검증하는 변환 사양. 기계 가독 매핑(어떤 AIMO 객체가 어떤 프레임워크 조항에 매핑되는지) 정의. [Validator](../../validator/)는 `--validate-profiles`로 모든 공식 profile JSON이 스키마(profile_id PR-* 패턴, target 열거, target_version, mappings)를 준수하는지 확인. |

### 공식 프로파일(Validator 검증)

Profile JSON은 `coverage_map/profiles/`에 있으며 Validator(`--validate-profiles`)로 검증됩니다. 명명: 파일명 `<target>_<purpose>.json`; 각 파일에 `target_version` 포함.

| 파일 | profile_id | target | target_version |
|------|------------|--------|----------------|
| `iso42001.json` | PR-ISO42001-v0.1 | ISO_42001 | 1.0 |
| `iso_42001_readiness.json` | PR-ISO42001-READINESS-v0.1 | ISO_42001 | 2023 |
| `nist_ai_rmf.json` | PR-NIST-AI-RMF-v0.1 | NIST_AI_RMF | 1.0 |
| `nist_ai_600_1_genai.json` | PR-NIST-AI-600-1-v0.1 | NIST_AI_600_1 | 1.0 |
| `eu_ai_act_annex_iv.json` | PR-EU-AI-ACT-ANNEX-IV-v0.1 | EU_AI_ACT_ANNEX_IV | Annex IV |
| `eu_ai_act_high_risk.json` | PR-EU-AI-ACT-HIGH-RISK-v0.1 | EU_AI_ACT_HIGH_RISK | 2024/1689 |
| `eu_gp_ai_cop.json` | PR-EU-GPAI-COP-v0.1 | EU_GPAI_COP | current |
| `uk_atrs_procurement.json` | PR-UK-ATRS-v0.1 | UK_ATRS | current |
| `jp_gov_genai_procurement.json` | PR-JP-GOV-GENAI-PROCUREMENT-v0.1 | JP_GOV_GENAI_PROCUREMENT | current |

### 프로파일 업데이트 정책

- **EU AI Act 참조(0.1.2)**: 증거 준비 일관성을 위해 Coverage Map 및 문서 내 EU AI Act 조문 참조를 Regulation (EU) 2024/1689에 맞춤. 참고이며 법적 해석 아님.
- **ISO 42001 / NIST AI RMF**: 대상 프레임워크 신규 버전은 향후 표준 버전에서 새 프로파일 파일 또는 새 `target_version`으로 추가 가능. v0.1 프로파일은 v0.1 릴리스에서 고정.
- **EU AI Act Annex IV**: Annex IV 및 관련 조문은 규제 기관에 의해 갱신될 수 있음. 프로파일 매핑은 **PATCH**(예: 0.1.x)로 문구/조항 변경을 반영하여 동일 profile_id로 연속 유지. 구현자는 프로파일의 `target_version` 및 릴리스 노트에서 참조하는 버전에 맞출 것.

---

## 참고

- [증거 번들(산출물 개요)](../evidence-bundle/)
- [Evidence Bundle 루트 구조(v0.1)](../../standard/current/09-evidence-bundle-structure/)
- [최소 증거 요구사항](../minimum-evidence/)
- [Coverage Map(프레임워크 매핑)](../../coverage-map/)
- [Validator](../../validator/)
