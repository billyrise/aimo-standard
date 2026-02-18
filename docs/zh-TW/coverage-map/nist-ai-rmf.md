---
description: AIMO 標準與 NIST AI RMF 對應。AIMO 分類代碼與 NIST AI 風險管理框架功能之間的可追溯性。
---
<!-- aimo:translation_status=translated -->

# NIST AI RMF 對應

!!! note "主要來源"
    **NIST AI Risk Management Framework (AI RMF 1.0)** — [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework)（NIST 官方出版物與資源）。請對照此主要來源驗證對應與適用性。

> 可追溯性捷徑：分類法 → 最低證據 → 驗證器 → 人工監督協議。

- [分類法](../../standard/current/03-taxonomy/)
- [最低證據要求](../../artifacts/minimum-evidence/)
- [日誌結構描述](../../artifacts/log-schemas/)
- [驗證器](../../validator/)
- [人工監督協議](../../governance/human-oversight-protocol/)

本頁將選定的 NIST AI 風險管理框架（Govern、Map、Measure、Manage）主題對應到 AIMO 證據和人工產物。這僅用於可解釋性；它不保證符合 NIST AI RMF。請對照 [NIST AI RMF 1.0 出版物](https://www.nist.gov/itl/ai-risk-management-framework)驗證。


## 對應表

| 框架參照 / 主題 | AIMO 證據 / 在 AIMO 中的位置 | 證據包 / 最低證據 | 人工產物與驗證 | 備註 |
| --- | --- | --- | --- | --- |
| Govern 1.1 – 政策 | [範圍](../../standard/current/02-scope/)、[分類法](../../standard/current/03-taxonomy/) | Dictionary、Summary、review；review | schemas/jsonschema/aimo-dictionary.schema.json；schema_validate_dictionary | 參考性；請對照 NIST 出版物驗證。 |
| Govern 1.2 – 角色和職責 | [最低證據](../../artifacts/minimum-evidence/) | request、review | templates/ev/ev_template.md | 參考性；請對照 NIST 出版物驗證。 |
| Govern 2.1 – 問責制 | [證據包](../../artifacts/evidence-bundle/) | EV、request、review、change_log | examples/evidence_bundle_minimal/；schema_validate_ev | 參考性；請對照 NIST 出版物驗證。 |
| Govern 3.1 – 風險管理 | [範圍](../../standard/current/02-scope/) | request、review、exception | templates/ev/ | 參考性；請對照 NIST 出版物驗證。 |
| Govern 4.1 – 文化 | [概述](../../standard/current/01-overview/) | Summary、review；review | — | 參考性；請對照 NIST 出版物驗證。 |
| Map 1.1 – 背景對應 | [範圍](../../standard/current/02-scope/)、[字典](../../standard/current/05-dictionary/) | Dictionary、Summary；request | schemas/jsonschema/aimo-dictionary.schema.json；schema_validate_dictionary | 參考性；請對照 NIST 出版物驗證。 |
| Map 2.1 – 資料和文件 | [EV 範本](../../standard/current/06-ev-template/) | EV、Dictionary、change_log；change_log | schemas/jsonschema/aimo-ev.schema.json；schema_validate_ev | 參考性；請對照 NIST 出版物驗證。 |
| Map 3.1 – 資料治理 | [字典](../../standard/current/05-dictionary/) | Dictionary、EV | schemas/jsonschema/aimo-dictionary.schema.json；schema_validate_dictionary | 參考性；請對照 NIST 出版物驗證。 |
| Measure 1.1 – 績效和影響 | [EV 範本](../../standard/current/06-ev-template/) | EV | schemas/jsonschema/aimo-ev.schema.json；schema_validate_ev | 參考性；請對照 NIST 出版物驗證。 |
| Measure 2.1 – 監控 | [最低證據](../../artifacts/minimum-evidence/) | EV、change_log；change_log、integrity | templates/ev/ | 參考性；請對照 NIST 出版物驗證。 |
| Measure 3.1 – 測試和驗證 | [驗證器](../../standard/current/07-validator/) | EV | validator/rules/、validator/src/；schema_validate_ev | 參考性；請對照 NIST 出版物驗證。 |
| Manage 1.1 – 資源配置 | [概述](../../standard/current/01-overview/) | Summary、review；review | — | 參考性；請對照 NIST 出版物驗證。 |
| Manage 2.1 – 事件和回應 | [最低證據](../../artifacts/minimum-evidence/) | exception、renewal、change_log | templates/ev/ev_template.md | 參考性；請對照 NIST 出版物驗證。 |
| Manage 3.1 – 變更管理 | [證據包](../../artifacts/evidence-bundle/) | change_log；change_log | schemas/jsonschema/aimo-standard.schema.json | 參考性；請對照 NIST 出版物驗證。 |
| Manage 4.1 – 審查和更新 | [最低證據](../../artifacts/minimum-evidence/) | renewal、review；review、renewal | templates/ev/ | 參考性；請對照 NIST 出版物驗證。 |
| Manage 5.1 – 溝通 | [證據包](../../artifacts/evidence-bundle/) | Summary、change_log；change_log | templates/ev/ | 參考性；請對照 NIST 出版物驗證。 |
