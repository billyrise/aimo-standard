---
description: AIMO 標準貢獻指南 - 如何貢獻程式碼、文件和翻譯。Issue 和 PR 指引。
---

# 貢獻

本頁提供貢獻 AIMO 標準的指引。

## 快速開始

1. Fork 儲存庫
2. 建立功能分支
3. 按照以下指引進行變更
4. 執行品質檢查
5. 提交 pull request

## 主要原則

| 原則 | 說明 |
| --------- | ----------- |
| 英文是規範版本 | 先編輯 `docs/en/`，然後更新 `docs/ja/` |
| SSOT | 此儲存庫是單一事實來源 |
| 不手動編輯產生的檔案 | 編輯來源，重新產生，提交 |
| 所有變更透過 PR | 即使是維護者也使用 pull request |

## 品質檢查

提交 PR 前，執行：

```bash
# 啟動虛擬環境
source .venv/bin/activate

# 執行 lint
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
python tooling/audit/baseline_audit.py --check

# 建置文件
mkdocs build --strict
```

## 變更類型

| 類型 | 範例 | 審查要求 |
| ---- | -------- | ------------------- |
| 規範性 | 結構描述變更、要求 | 維護者 + 討論 |
| 非規範性 | 錯字、澄清 | 維護者核准 |
| i18n | 翻譯 | 結構必須符合 EN |
| 工具 | CI/CD、腳本 | 維護者核准 |

## i18n 指引

### 更新順序

1. 編輯英文來源（`docs/en/...`）
2. 更新日文翻譯（`docs/ja/...`）
3. 執行 `lint_i18n.py` 驗證一致性
4. 一起提交

### 結構要求

- 兩種語言使用相同檔名
- 相同的標題層級
- 每個章節相同的頁面數量

## PR 檢查清單

提交 PR 時，驗證：

- [ ] 已識別變更類型（docs / schema / examples / tooling）
- [ ] 已完成破壞性變更評估
- [ ] i18n：EN 和 JA 一起更新（如適用）
- [ ] 品質檢查通過
- [ ] 已連結相關 issue

## 破壞性變更

破壞性變更需要：

1. 實作前的 issue 討論
2. 根據 [VERSIONING.md](https://github.com/billyrise/aimo-standard/blob/main/VERSIONING.md) 進行版本提升
3. 包含遷移指引的變更日誌條目

## 符合性聲明更新

要新增或修改符合性聲明：

1. 更新覆蓋範圍對應 YAML
2. 更新對應的文件頁面
3. 執行驗證器測試
4. 記錄對應理由

## 完整指引

請參閱 [CONTRIBUTING.md](https://github.com/billyrise/aimo-standard/blob/main/CONTRIBUTING.md) 了解根目錄層級指南。

## 相關頁面

- [治理](../) — 專案治理
- [在地化指南](../../contributing/localization/) — i18n 詳細資訊
- [責任邊界](../responsibility-boundary/) — AIMO 提供的內容
