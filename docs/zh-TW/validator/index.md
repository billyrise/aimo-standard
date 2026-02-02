---
description: AIMO 驗證器中心 - 驗證工具快速入門。在 30 秒內安裝、執行和解讀結果。證據包驗證和合規性檢查。
---

# 驗證器

本頁是驗證工具和規則的中心。驗證器及其規則的規範性規格在標準中。

## 快速入門（30 秒）

**1. 先決條件**

```bash
pip install jsonschema   # 如果尚未安裝
```

**2. 對樣本套件執行驗證**

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**3. 閱讀報告並修復錯誤/警告**

範例輸出（成功）：

```
OK
```

範例輸出（失敗）：

```
Schema validation failed:
<root>: 'version' is a required property
<root>: 'dictionary' is a required property
<root>: 'evidence' is a required property
```

退出碼：`0` = 成功、`1` = 驗證錯誤、`2` = 使用錯誤。

---

## 它檢查什麼

- **結構描述驗證**：root 物件、字典和證據符合 JSON Schema
- **字典一致性**：所有代碼存在於分類字典中
- **代碼狀態**：對已棄用的代碼發出警告，對已移除的代碼發出錯誤

## 它不檢查什麼

- **內容準確性**：驗證器檢查結構，而非含義
- **合規保證**：通過驗證不保證法規合規性
- **人工判斷**：依賴情境的決策需要人工審查（請參閱[人工監督協議](../governance/human-oversight-protocol.md)）
- **自動日誌收集**：驗證器驗證提交的證據；它不收集日誌

---

## 資源

- **規格**：[標準 > 當前 > 驗證器](../standard/current/07-validator.md) — 規則、參考檢查，以及驗證如何與證據相關。
- **規則和實作**：儲存庫 `validator/rules/`（檢查）、`validator/src/`（參考實作）。執行和 CI 使用在規格中說明。
- **解讀**：驗證「失敗」對稽核員意味著什麼（在規格中解釋）。

如需符合性和人工產物使用，請參閱[符合性](../conformance/index.md)和[人工產物](../artifacts/index.md)。
