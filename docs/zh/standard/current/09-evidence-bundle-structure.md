---
description: 证据包之规范根结构与 manifest（v0.1）。完整性为 MUST；保管为实现定义。
---
<!-- aimo:translation_status=translated -->

# 证据包根结构（v0.1）

本页定义证据包之**规范**根布局与 manifest。验证器必须在进行任何模式验证前，拒绝不满足这些要求的组合。

## v0.1 规范 MUST（摘要）

- 组合根目录下**必须**有 **manifest.json**。
- **object_index** 与 **payload_index**：每笔条目必须包含 **sha256**（64 位小写十六进制）；路径必须为相对路径，且不得包含 `../` 或脱离组合根目录。
- **signing.signatures** 必须为非空数组（空数组无效）。
- 每笔签名条目必须具备：位于 `signatures/` 下之 **path**（禁止路径遍历）、**targets**（数组，至少一路径），且组合内至少一组签名必须在 **targets** 中列出 **manifest.json**（manifest 签名为强制）。
- **hash_chain**：v0.1 必须包含 **algorithm**、**head**、**path**（位于 `hashes/` 下）以及 **covers**（至少含 **manifest.json** 与 **objects/index.json**）。

验证器必须在接受组合前强制上述规则。JSON Schema 与参考验证器实现相同规则。

## 根必要结构（MUST）

组合根目录下必须存在下列项目：

| 项目 | 类型 | 用途 |
| --- | --- | --- |
| **manifest.json** | 文件 | 组合 manifest（见下）。组合的规范描述符。 |
| **objects/** | 目录 | 枚举对象（如元数据、索引）。列于 `manifest.json` 之 `object_index`。 |
| **payloads/** | 目录 | Payload 文件（如根 EV JSON、Evidence Pack 文件）。列于 `manifest.json` 之 `payload_index`。 |
| **signatures/** | 目录 | 数字签名。v0.1 必须至少包含一组参照 manifest 的签名文件（存在与目标参照；密码学验证为未来扩展）。 |
| **hashes/** | 目录 | 哈希链或完整性记录（依 `manifest.json` 之 `hash_chain` 所需）。 |

实现者不得提交缺少任一项的组合。根结构不完整时，验证器必须以明确消息失败。

## 完整性（规范）与保管（实现）

- **完整性**在 v0.1 为**规范**：标准要求组合具备完整性元数据（manifest、索引文件之 sha256、manifest 之签名存在）。验证器必须检查：
  - 必要目录与文件存在。
  - `manifest.json` 存在且有效（模式与前模式检查）。
  - `object_index` 与 `payload_index` 所列每个文件在给定路径存在，且内容与声明之 `sha256` 一致。
  - `signatures/` 至少包含一组以 manifest 为目标的签名（v0.1：仅存在与参照；v0.1.1：建议验证元数据；v0.2 规划：密码学验证纳入范围）。
- **保管**（存储、访问控制、保留、WORM）为**实现定义**。标准不规定保管人如何存储或保护组合；仅要求提交时之包满足上述完整性要求。

## manifest.json（MUST 字段）

manifest 至少须包含：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| **bundle_id** | string (UUID) | 本组合之唯一标识符。 |
| **bundle_version** | string (SemVer) | 组合版本。 |
| **created_at** | string (date-time) | 创建时间戳。 |
| **scope_ref** | string | 范围参照（如 `SC-001`）。模式 `SC-*`。 |
| **object_index** | array | 对象列表：`id`、`type`、`path`、`sha256`。路径必须为相对、不得含 `../` 或以 `/` 开头，且须位于证据包根目录内（验证器必须拒绝脱离组合根之路径）。 |
| **payload_index** | array | Payload 列表：`logical_id`、`path`、`sha256`、`mime`、`size`。路径规则与 object_index 相同（相对、无 `../`、无前导 `/`、位于组合根内）。 |
| **hash_chain** | object | **规范 (v0.1)：** 必须包含 `algorithm`（sha256 \| merkle）、`head`（64 位小写十六进制）、`path`（`hashes/` 下之相对路径；无 `../`、无前导 `/`）及 `covers`（数组，至少一元素）。v0.1 之 `covers` 必须包含 `manifest.json` 与 `objects/index.json`。 |
| **signing** | object | **规范 (v0.1)：** 必须包含 `signatures`（数组，至少一笔）。每笔须具：`signature_id`（如 SIG-... 或 UUID）、`path`（`signatures/` 下相对路径；无 `../`、无前导 `/`）、`targets`（数组，至少一路径；v0.1 至少一组签名之 targets 须含 `manifest.json`）、`algorithm`（ed25519、rsa-pss、ecdsa、unspecified 之一）。`created_at`（date-time）为 MAY。**注：** v0.1 不涵盖签名之密码学验证；仅要求参照（哪个文件、目标为何）。 |

**v0.1.1 可选签名元数据（建议供第三方重新执行）：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| **signer_identity** | string | 签署者身份（如 PGP 指纹、did:key）。 |
| **signed_at** | string (date-time) | 签名施加时间（ISO 8601）。 |
| **verification_command** | string | 供审计员重新执行验证的示例 CLI 命令。 |
| **canonicalization** | string | 签署 payload 之规范化方式：`rfc8785_json`、`cbor` 或 `unspecified`。 |

完整性与验证：**v0.1** — 仅参照与存在。**v0.1.1** — 建议验证用元数据。**v0.2**（规划）— 密码学验证纳入范围。

- **sha256** 值必须为 64 位小写十六进制字符。
- **path** 必须为相对路径；不得包含 `../` 或以 `/` 开头；路径须位于证据包根目录内。
- manifest 可包含明确自参照（如于 `object_index` 或专用字段），使 manifest 自身完整性被涵盖；验证器必须接受 manifest 列于某索引或由某签名明确参照的组合。

JSON Schema 见：`schemas/jsonschema/evidence_bundle_manifest.schema.json`。

## 未来扩展（参考）

- **Control/Requirement 链接**：未来版本可能新增将证据包元素链接至 Control 或 Requirement 标识符的标准方式（例如导出至 NIST OSCAL 或类似审计自动化格式）。v0.1 与 v0.1.1 不要求。

## 参考资料

- [证据包（工件总览）](../../../artifacts/evidence-bundle/) — 目的与目录
- [EV 模板 — 外部表单与审计交接索引](../06-ev-template/#external-forms-official-templateschecklists-attached-as-is) — 附上正式模板/检查表及于 manifest 参照之方式
- [签名验证路线图](../../../artifacts/signature-verification-roadmap/) — v0.1.1 元数据与 v0.2 验证计划
- [验证器](../../../validator/) — 验证器如何强制此结构
- [最低证据要求](../../../artifacts/minimum-evidence/) — MUST 级检查表
