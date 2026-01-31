# Minimum Evidence Requirements（最小証跡要件）

本ページは、ライフサイクル別に整理した MUST レベルの最小証跡要件を定義する。説明可能性と証跡準備を支えるものであり、法的助言の提供や適合の保証は行わない。

## 1) Request（申請）

- **MUST フィールド**: 識別子、タイムスタンプ、actor/role、scope（申請内容）、rationale（理由）。
- **MUST リンク**: request id を review および利用を記録する EV 項目から参照する。
- **示すこと**: 利用が承認・実施前に申請されスコープが定められていること。

## 2) Review / Approval（審査/承認）

- **MUST フィールド**: 識別子、タイムスタンプ、actor/role、decision（承認/却下/条件付き）、scope、rationale、request への参照。
- **MUST リンク**: review id を EV および後続の exception/renewal から参照する。
- **示すこと**: 利用（または例外）の前に定義された審査・承認が行われていること。

## 3) Exception（例外）

- **MUST フィールド**: 識別子、タイムスタンプ、scope、expiry（期限）、compensating controls、rationale、review/request への参照。
- **MUST リンク**: exception → 代替統制；exception → 有効期限；exception → renewal（再評価時期）。
- **示すこと**: 逸脱が有効期限付きであり、代替統制と renewal に紐づいていること。

## 4) Renewal / Re-evaluation（更新/再評価）

- **MUST フィールド**: 識別子、タイムスタンプ、actor/role、decision（更新/取り消し/条件付き）、先行 exception/request/review/EV への参照。
- **MUST リンク**: renewal は更新対象の exception または承認を参照；EV 項目は renewal id を参照可能。
- **示すこと**: 例外・承認が定義に基づき再評価され、更新または取り消しされていること。

## 5) Change Log（変更管理）

- **MUST フィールド**: 識別子、タイムスタンプ、actor/role、変更内容、references（変更対象の EV/request/review/exception/renewal 等）。
- **MUST リンク**: change log エントリは変更対象アーティファクトを参照する。
- **示すこと**: バンドルまたはその内容の変更が記録され追跡可能であること。

## 6) Integrity & Access（完全性/アクセス制御）

- **実装**: 推奨（アクセス制御、ハッシュ、WORM、監査ログ等）。要件は説明可能性の観点で記載する（誰がアクセスしたか、完全性をどう保全したか）。
- **示すこと**: 証跡が保全され、監査の依拠を支えるアクセス制御が行われていること。

## Important note

本最小セットは説明可能性と証跡準備を支援する。法的助言の提供および適合の保証は行わない。

バンドル構造と TOC は [Evidence Bundle](evidence-bundle.md)、フィールドレベルの整合は [EV Template](../standard/current/06-ev-template.md) およびスキーマを参照。
