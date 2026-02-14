---
description: AIMO 標準與 ISMS（ISO 27001/27002）對應。AIMO 分類法與資訊安全管理系統控制措施之間的可追溯性。
---

# ISMS 視角（ISO/IEC 27001/27002）對應

> 可追溯性捷徑：分類法 → 最低證據 → 驗證器 → 人工監督協議。

- [分類法](../../standard/current/03-taxonomy/)
- [最低證據要求](../../artifacts/minimum-evidence/)
- [日誌結構描述](../../artifacts/log-schemas/)
- [驗證器](../../validator/)
- [人工監督協議](../../governance/human-oversight-protocol/)

本頁將選定的 ISO/IEC 27001/27002 主題（變更管理、存取控制、日誌、證據完整性）對應到 AIMO 證據和人工產物。這僅用於可解釋性；它不保證符合 ISO/IEC 27001 或 27002。請對照已發布的標準驗證。


## 對應表

| 框架參照 / 主題 | AIMO 證據 / 在 AIMO 中的位置 | 證據包 / 最低證據 | 人工產物與驗證 | 備註 |
| --- | --- | --- | --- | --- |
| A.5.24 – 專案管理中的資訊安全 | [範圍](../../standard/current/02-scope/) | request、review | templates/ev/ | 參考性；請對照官方文本驗證。 |
| A.5.29 – 中斷期間的資訊安全 | [最低證據](../../artifacts/minimum-evidence/) | exception、renewal | templates/ev/ev_template.md | 參考性；請對照官方文本驗證。 |
| A.5.30 – 業務持續性的 ICT 就緒 | [概述](../../standard/current/01-overview/) | Summary；integrity | — | 參考性；請對照官方文本驗證。 |
| A.8.1 – 資產清冊 | [字典](../../standard/current/05-dictionary/) | Dictionary、EV | schemas/jsonschema/aimo-dictionary.schema.json；schema_validate_dictionary | 參考性；請對照官方文本驗證。 |
| A.8.2 – 資訊分類 | [分類法](../../standard/current/03-taxonomy/) | Dictionary；review | schemas/jsonschema/aimo-dictionary.schema.json；schema_validate_dictionary | 參考性；請對照官方文本驗證。 |
| A.8.3 – 存取控制 | [最低證據](../../artifacts/minimum-evidence/) | —；integrity | — | 參考性；請對照官方文本驗證。 |
| A.8.15 – 日誌記錄 | [EV 範本](../../standard/current/06-ev-template/) | EV、change_log；change_log | schemas/jsonschema/aimo-ev.schema.json；schema_validate_ev | 參考性；請對照官方文本驗證。 |
| A.8.16 – 監控活動 | [最低證據](../../artifacts/minimum-evidence/) | EV、change_log；change_log、integrity | templates/ev/ | 參考性；請對照官方文本驗證。 |
| A.8.32 – 變更管理 | [證據包](../../artifacts/evidence-bundle/) | change_log；change_log | schemas/jsonschema/aimo-standard.schema.json | 參考性；請對照官方文本驗證。 |
| A.8.33 – 測試資訊 | [驗證器](../../standard/current/07-validator/) | EV | validator/rules/、validator/src/；schema_validate_ev | 參考性；請對照官方文本驗證。 |
