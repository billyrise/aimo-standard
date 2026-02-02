---
description: AIMO 標準與歐盟 AI 法案對應。AIMO 分類代碼與歐盟 AI 法案風險類別和要求之間的可追溯性。
---

# 歐盟 AI 法案對應

> 可追溯性捷徑：分類法 → 最低證據 → 驗證器 → 人工監督協議。

- [分類法](../standard/current/03-taxonomy.md)
- [最低證據要求](../artifacts/minimum-evidence.md)
- [日誌結構描述](../artifacts/log-schemas/index.md)
- [驗證器](../validator/index.md)
- [人工監督協議](../governance/human-oversight-protocol.md)

本頁將選定的歐盟 AI 法案主題（文件、記錄保存、風險管理、人工監督、透明度）對應到 AIMO 證據和人工產物。這僅是高階對應，**不**構成法律建議或保證符合性。請對照官方法律文本驗證。


## 對應表

| 框架參照 / 主題 | AIMO 證據 / 在 AIMO 中的位置 | 證據包 / 最低證據 | 人工產物與驗證 | 備註 |
| --- | --- | --- | --- | --- |
| Art 9 – 風險管理（義務） | [範圍](../standard/current/02-scope.md) | request、review、exception | templates/ev/ | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 10 – 資料治理 | [字典](../standard/current/05-dictionary.md) | Dictionary、EV | schemas/jsonschema/；schema_validate_dictionary | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 11 – 文件（高風險） | [EV 範本](../standard/current/06-ev-template.md)、[證據包](../artifacts/evidence-bundle.md) | EV、Dictionary、Summary；request、review | schemas/jsonschema/、templates/ev/；schema_validate_ev | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 12 – 記錄保存 | [證據包](../artifacts/evidence-bundle.md)、[最低證據](../artifacts/minimum-evidence.md) | EV、change_log、request、review | examples/evidence_bundle_minimal/；schema_validate_ev | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 13 – 透明度（使用者資訊） | [範圍](../standard/current/02-scope.md) | Summary、EV；review | templates/ev/ | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 14 – 人工監督 | [最低證據](../artifacts/minimum-evidence.md) | review、exception；review、exception | templates/ev/ev_template.md | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 17 – 風險管理（高風險） | [範圍](../standard/current/02-scope.md) | request、review、exception、renewal | templates/ev/ | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 26 – 透明度（有限風險） | [範圍](../standard/current/02-scope.md) | Summary、EV；review | templates/ev/ | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 29 – 文件（通用 AI） | [EV 範本](../standard/current/06-ev-template.md) | EV、Dictionary、Summary；request、review | schemas/jsonschema/；schema_validate_ev | 僅高階；非法律建議。請對照官方文本驗證。 |
| Art 52 – 透明度（部署者） | [最低證據](../artifacts/minimum-evidence.md) | EV、Summary；review | templates/ev/ | 僅高階；非法律建議。請對照官方文本驗證。 |
| 序言 – 問責制 | [證據包](../artifacts/evidence-bundle.md) | EV、request、review、change_log | examples/evidence_bundle_minimal/；schema_validate_ev | 僅高階；非法律建議。請對照官方文本驗證。 |
