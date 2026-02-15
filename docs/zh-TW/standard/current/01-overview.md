---
description: AIMO Standard 概述。定義 AI 治理審計的共享分類法、代碼體系、詞典、證據範本與驗證器檢查。
---
<!-- aimo:translation_status=translated -->

# 概述（Overview）

**AIMO** 代表 **AI Management Office**（AI 管理辦公室）。AIMO Standard 定義：
- 共享分類法
- 代碼體系
- 初始詞典
- EV 範本
- 驗證器檢查（規範 + 最小參考實作）

本儲存庫發布：
- 人類可讀規範（HTML）
- 機器可讀製品（結構描述/範本/範例）
- 官方 PDF 發布版

## 定位：ISO/IEC 42001（AIMS）的配套

AIMO Standard 是**證據就緒與可解釋性的實施加速器**，可用於支援與 ISO/IEC 42001 對齊的 AI 管理體系（AIMS）並建構可審計證據。它不替代 ISO/IEC 42001 或任何其他管理體系標準；而是增加分類法、Evidence Bundle 結構與 Coverage Map，以協助實施並為這些控制提供證據。

**AIMO 提供的內容**

- AI 治理分類的分類法與代碼體系
- Evidence Bundle 結構（manifest、object_index、payload_index、完整性）
- 可追溯性的驗證器與 Coverage Map
- 符合性等級（Foundation、Operational、Audit-Ready）— 證據打包的 AIMO 專屬成熟度層級

**AIMO 不提供的內容**

- 法律建議
- ISO 認證或認證替代
- 法規符合性保證
- 審計判斷或認可認證機構的替代

**為何是現在**

- **ISO/IEC 42006**（2025-07 發布）規定依 ISO/IEC 42001 對 AI 管理體系進行審計與認證的機構要求，提高對可審計證據與可追溯性的期望。
- **EU AI Act** 正在分階段適用（2025–2027）；於官方公報公布的調和標準將提供符合性推定。EU AI Office 正於 2026 年準備實用指南（高風險分類、第 50 條透明度、事件、QMS 要素）。
- 採用者與認證機構越來越多地將 ISO/IEC 42001 用作 AI 治理的系統層；AIMO 協助建構支援該層級的證據，而不主張認證。

## 參考資料

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — 對 AI 管理體系進行審計與認證的機構要求
- [EU AI Act 實施時程](https://artificialintelligenceact.eu/implementation-timeline)（AI Act Service Desk / 委員會一致；參考）
- [European Commission — Clear guidelines for AI (2025年12月4日)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — AI Office 指南準備（請查閱委員會新聞取得最新 URL）
- [EPRS — EU AI Act implementation timeline (2025年6月)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — 議會簡報（參考）
