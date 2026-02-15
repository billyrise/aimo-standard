---
description: 证据包覆盖映射模板（v0.1）。面向审计方的一页摘要 — 范围、证据类型、控制映射、排除、完整性证明。
---
<!-- aimo:translation_status=translated -->

# 证据包覆盖映射（模板）

!!! info "参考 — 推荐实践"
    本页定义一页式证据包覆盖映射的**推荐实践模板**。**非**标准规范性要求。用于记录包所覆盖与未覆盖范围以便审计交接。对框架等的引用稳定；采用由实施方自行决定。

---

## 1. 范围

| 项目 | 说明 |
|------|--------------|
| **范围引用** | 包 manifest 的 `scope_ref`（如 `SC-001`）。将本包与声明的范围关联。 |
| **Bundle ID** | `bundle_id`（UUID）— 本包的一标识符。 |
| **Bundle 版本** | `bundle_version`（SemVer）— 包的版本。 |
| **期间 / 快照** | 可选：本包所代表的时间段或快照日期（如 2026-Q1、as-of 2026-02-03）。 |

---

## 2. 证据类型（EV / objects 与 payloads）

| 类别 | 内容 | v0.1 最小例 |
|----------|----------|------------------------|
| **object_index** | 枚举对象（元数据、索引）。每项：`id`, `type`, `path`, `sha256`。 | 如 `objects/index.json`（index 类型）。 |
| **payload_index** | 载荷文件（根 EV JSON、Evidence Pack 文件）。每项：`logical_id`, `path`, `sha256`, `mime`, `size`。 | 如 `payloads/root.json`（根 AIMO EV JSON）。 |
| **EV 类型** | 证据记录（根或链接载荷内）— request, review, exception, renewal, change log。 | 与 [Evidence Pack 模板](../../standard/current/06-ev-template/) 及 [最低证据要求](../minimum-evidence/) 一致。 |

*实施方可扩展 object_index 与 payload_index；路径须保持在包根内并满足 [证据包根结构（v0.1）](../../standard/current/09-evidence-bundle-structure/)。*

---

## 3. 控制映射（仅供参考）

与外部框架的映射**仅供参考**；标准不强制任何特定法规的合规。

| 框架 | 本包中的使用 | 参考 |
|-----------|--------------------|-----------|
| **ISO/IEC 42001** | 可选：文档化本包支持的 AI MS 主题。 | [Coverage Map → ISO 42001](../../coverage-map/iso-42001/) |
| **EU AI Act** | 可选：高层文档/记录保存对齐。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/) |
| **NIST AI RMF** | 可选：Govern、Map、Measure、Manage 映射。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/) |
| **EU GPAI CoP** | 可选：Model Documentation Form；在 External Forms 中附上并以 logical_id 引用。 | [Coverage Map → EU AI Act](../../coverage-map/eu-ai-act/)；配置 `eu_gp_ai_cop.json` |
| **NIST AI RMF / GenAI** | 可选：GenAI 配置（AI 600-1）制品。 | [Coverage Map → NIST AI RMF](../../coverage-map/nist-ai-rmf/)；配置 `nist_ai_600_1_genai.json` |
| **UK ATRS** | 可选：ATRS 记录、采购评估。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；配置 `uk_atrs_procurement.json` |
| **JP Gov GenAI 采购** | 可选：JP 采购清单、AI Business Guidelines。 | [Procurement & Disclosure](../../coverage-map/procurement-and-disclosure/)；配置 `jp_gov_genai_procurement.json` |
| **ISMS (27001/27002)** | 可选：变更管理、访问、日志、完整性。 | [Coverage Map → ISMS](../../coverage-map/isms/) |

*“本包中的使用”按每次提交填写；标准不要求任何特定控制覆盖。*

### External Forms 与 manifest 引用

**External Forms**（原样附上的官方模板/清单）应在包的 **payload_index** 中列出，并具有稳定的 `logical_id`、`path`、`sha256`、`mime`、`size`。审计方可从 manifest 追溯到文件并验证哈希。见 [EV Template — External Forms](../../standard/current/06-ev-template/#external-forms-official-templateschecklists-attached-as-is) 与 [EV Template — Audit Handoff Index](../../standard/current/06-ev-template/#audit-handoff-index)。

---

## 4. 排除 / 假设

| 领域 | 本包**不覆盖**的内容（示例行 — 按提交调整） |
|------|-------------------------------------------------------------------------------|
| **排除** | 如：范围外的系统/用例、无证据的第三方组件、本包期间以外。 |
| **假设** | 如：Dictionary/分类法版本、所用 validator/模式版本、保管与保留由实现定义。 |
| **限制** | 如：v0.1 中签名验证在范围外；不对法规进行法律解释。 |

*将占位符替换为提交专用的排除与假设。*

---

## 5. 完整性证明摘要（v0.1）

| 要素 | 提供内容（v0.1 规范性） |
|---------|----------------------------------|
| **manifest.json** | 存在且模式有效；含 `object_index`、`payload_index`、`hash_chain`、`signing`。 |
| **sha256** | `object_index` 与 `payload_index` 中每个文件声明 64 字符小写 hex sha256；Validator 检查内容匹配。 |
| **索引存在** | 所列路径均在包根下存在；无路径穿越（`../` 或前导 `/`）。 |
| **签名存在** | `signatures/` 中至少一个签名文件；manifest 通过 `signing.signatures[]` 引用 `path` 与 `targets`（v0.1 的 targets 必须含 `manifest.json`）。v0.1 不包含密码学验证。 |
| **Hash chain** | manifest 中的 `hash_chain`：`algorithm`、`head`（64 字符 hex）、`path`（`hashes/` 下文件）、`covers`（v0.1 必须含 `manifest.json` 与 `objects/index.json`）。`hash_chain.path` 处文件存在。 |

*本表概括 [Validator](../../validator/) 对 v0.1 包检查的完整性保证。Custody（存储、访问控制、保留）由实现定义。*

---

## Coverage Map（YAML）与配置（JSON）

| 制品 | 状态 | 目的 |
|----------|--------|---------|
| **Coverage Map YAML**（`coverage_map/coverage_map.yaml` 等） | **参考** | AIMO 证据/制品与外部框架（ISO 42001、NIST AI RMF、EU AI Act 等）的高层映射主题，用于可解释性。不施加规范性验证要求。 |
| **Profile JSON**（`coverage_map/profiles/*.json`） | **规范** | 按 `schemas/jsonschema/aimo-profile.schema.json` 验证的转换规格。定义机器可读映射（如哪些 AIMO 对象对应哪些框架条款）。[Validator](../../validator/) 使用 `--validate-profiles` 确保所有官方 profile JSON 符合模式（profile_id PR-* 模式、target 枚举、target_version、mappings）。 |

### 官方配置（Validator 验证）

Profile JSON 位于 `coverage_map/profiles/`，由 Validator（`--validate-profiles`）验证。命名：文件名 `<target>_<purpose>.json`；每文件含 `target_version`。

| 文件 | profile_id | target | target_version |
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

### 配置更新政策

- **EU AI Act 引用（0.1.2）**：为证据准备一致，Coverage Map 与文档中 EU AI Act 条文引用已与 Regulation (EU) 2024/1689 对齐；仅供参考，非法律意见。
- **ISO 42001 / NIST AI RMF**：目标框架新版本可在未来标准版本中以新配置文件或新 `target_version` 加入；v0.1 配置在 v0.1 发布中冻结。
- **EU AI Act Annex IV**：Annex IV 及相关条文可能由监管机构更新；配置映射可通过 **PATCH**（如 0.1.x）随条文或条款变更更新，并保持同一 profile_id 以延续。实施方应与配置中 `target_version` 及发布说明所引版本一致。

---

## 参见

- [证据包（制品概览）](../evidence-bundle/)
- [证据包根结构（v0.1）](../../standard/current/09-evidence-bundle-structure/)
- [最低证据要求](../minimum-evidence/)
- [Coverage Map（框架映射）](../../coverage-map/)
- [Validator](../../validator/)
