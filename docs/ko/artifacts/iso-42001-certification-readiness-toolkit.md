---
description: ISO/IEC 42001 인증 준비 도구 키트. AIMO 산출물로 ISO 42001에 맞춘 감사 준비 증거까지의 최단 경로. 준비 지원만 제공하며 인증을 부여하지 않음.
---
<!-- aimo:translation_status=translated -->

# ISO/IEC 42001 인증 준비 도구 키트

이 페이지는 AIMO 산출물을 사용해 **ISO/IEC 42001**에 맞춘 **감사 준비 증거**를 만드는 **실무·도입 중심** 가이드입니다. **준비를 지원**할 뿐 인증을 **부여하지 않습니다**. 인증 결정은 **인정 인증 기관**이 합니다.

## 목표

ISO/IEC 42001형 통제(컨텍스트, 경영, 기획, 지원, 운영, 성과 평가, 개선)를 지원하는, 검증기로 검사된 Evidence Bundle을 만들어 감사인이 증거를 효율적으로 찾고 검증할 수 있게 한다.

## 5단계 워크플로우

| 단계 | 조치 |
| --- | --- |
| **1. 범위 및 AI 인벤토리 수립** | scope_ref로 범위 정의; [분류체계](../../standard/current/03-taxonomy/)와 [사전](../../standard/current/05-dictionary/)으로 AI 시스템 분류. |
| **2. 관리체계 산출물 설정** | 정책·역할·PDCA에 맞는 산출물을 작성하거나 참조. [AIMO-MS / AIMO-Controls](../../conformance/)를 구조로; [Evidence Pack 템플릿](../../standard/current/06-ev-template/) (EP-01..EP-07) 참조. |
| **3. Evidence Bundle + 최소 증거 산출** | [Evidence Bundle 구조](../../standard/current/09-evidence-bundle-structure/)에 따라 manifest, object_index, payload_index, hash_chain, signing 구성. [최소 증거 요구사항](minimum-evidence.md)에 따라 request, review, exception, renewal, change_log 포함. |
| **4. 검증기 실행 + 체크섬 + 변경 통제** | `python validator/src/validate.py <bundle_path> --validate-profiles` 실행. 검증기 버전과 출력 기록. SHA-256 체크섬 생성; 영향 받는 객체를 참조하는 change log 유지. |
| **5. 감사 팩 준비** | 번들을 패키징(zip 등); 체크섬 제공. [감사 보고 출력](../../standard/current/07-validator/) (audit-json / audit-html) 선택 첨부. 표준 인용 시 버전 URL(예 `/0.1.2/`) 사용. Audit-Ready 수준에서는 [Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index)와 [External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) 추가. |

## 체크리스트: ISO 42001 조항군 → AIMO 산출물 → 증거 출력

| ISO 42001 조항군 | AIMO 산출물 | 증거 출력 |
| --- | --- | --- |
| 컨텍스트 (4.1) | Summary, Dictionary, scope_ref | manifest scope_ref; Summary; Dictionary |
| 경영/방침 (5.x) | Summary, review, dictionary | 검토 기록; 방침 참조 |
| 기획 (6.x) | request, review, exception, EV, Dictionary | 요청/승인; EV 또는 Dictionary의 위험/목표 |
| 지원 (7.x) | Summary, review, EV, change_log | 문서; 역량/인식 증거 |
| 운영 (8.x) | EV, request, review, exception | 운영 통제; 적용성 |
| 성과 평가 (9.x) | EV, change_log, review, renewal | 모니터링; 내부 감사; 경영 검토 |
| 개선 (10.x) | exception, renewal, change_log | 시정 조치; 지속적 개선 |

[Coverage Map — ISO/IEC 42001](../../coverage-map/iso-42001/) 및 [ISO/IEC 42006](https://www.iso.org/standard/42006)에서 감사 기관 기대사항 참조.

## 안전한 표현

- **사용**: "We use AIMO artifacts to support ISO/IEC 42001 readiness; certification decisions remain with accredited certification bodies."
- **미사용**: "ISO 42001 certified by AIMO" 또는 "AIMO certifies compliance."

## 관련

- [적합성](../../conformance/) — 수준(Foundation, Operational, Audit-Ready) 및 주장 문구
- [Trust Package](../../governance/trust-package/) — 감사자용 자료
- [Responsibility Boundary](../../governance/responsibility-boundary/) — AIMO가 제공·비제공하는 내용
