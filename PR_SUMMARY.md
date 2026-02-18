# AIMO Standard v0.1.2 — Single PR Doc Update — Summary

## Commands executed (copyable) + results

```bash
# Build
cd /path/to/aimo-standard && python -m mkdocs build --strict
# Result: PASS (exit 0). Documentation built in ~6s. Pre-existing INFO (ko links, 04-codes anchor) unchanged.

# Internal link check
python tooling/checks/check_internal_links.py --check
# Result: PASS. "OK: All nav targets exist for all built locales."

# Safety grep (no problematic claim phrasing)
grep -r "AIMO compliance\|AIMO certified\|AIMO guarantees\|AIMO assures" docs/
# Result: No matches. PASS.

# No version bump (VERSIONING.md and release workflow untouched)
# Result: No changes to VERSIONING.md or .github/workflows. v0.1.2 remains throughout. PASS.
```

## Final changed files (18 files, en + ja only)

| File | Phase |
|------|--------|
| docs/en/coverage-map/eu-ai-act.md | P1 |
| docs/ja/coverage-map/eu-ai-act.md | P1 |
| docs/en/standard/current/01-overview.md | P1 (EU timeline link → primary) |
| docs/ja/standard/current/01-overview.md | P1 (EU timeline link → primary) |
| docs/en/coverage-map/iso-42001.md | P0 |
| docs/ja/coverage-map/iso-42001.md | P0 |
| docs/en/coverage-map/nist-ai-rmf.md | P0 |
| docs/ja/coverage-map/nist-ai-rmf.md | P0 |
| docs/en/artifacts/iso-42001-certification-readiness-toolkit.md | P0 |
| docs/ja/artifacts/iso-42001-certification-readiness-toolkit.md | P0 |
| docs/en/conformance/index.md | P2 |
| docs/ja/conformance/index.md | P2 |
| docs/en/governance/responsibility-boundary.md | P2 |
| docs/ja/governance/responsibility-boundary.md | P2 |
| docs/en/governance/trust-package.md | P2 |
| docs/ja/governance/trust-package.md | P2 |
| docs/en/coverage-map/procurement-and-disclosure.md | P3 |
| docs/ja/coverage-map/procurement-and-disclosure.md | P3 |

---

## PR title

`docs: v0.1.2 primary sources, conformance language, procurement mapping (en+ja) — no version bump`

---

## PR body (draft)

### Summary

Single-PR documentation update for AIMO Standard v0.1.2. No version bump; no changes to VERSIONING.md or release workflow. All edits are en + ja only (minimal diff).

### Changes (P1 → P0 → P2 → P3)

**P1 — EU AI Act (coverage map + overview)**  
- Replaced secondary source (artificialintelligenceact.eu) with EU primary sources: EC AI Act Service Desk (implementation timeline), EC Digital Strategy (AI Act standardisation), EUR-Lex (Regulation (EU) 2024/1689).  
- Timeline dates aligned to Service Desk; no unsupported “guidelines by date” claims.  
- Added “Legal note / Informative mapping” (en + ja).  
- Updated References to primary-first; same primary URLs in ja.

**P0 — ISO/IEC 42001, NIST AI RMF, ISO toolkit**  
- **Primary source** blocks added: ISO/IEC 42001 (iso.org), NIST AI RMF 1.0 (nist.gov).  
- NIST: “Verify against” text now links to NIST primary URL.  
- ISO 42001 page: explicit “AIMO does not certify”; certification by certification bodies; AIMO supports evidence readiness.  
- Toolkit: ISO primary URL + alignment with Conformance and Responsibility Boundary (no certification claims).

**P2 — Conformance, Responsibility Boundary, Trust Package**  
- **Conformance**: New sections “Compatibility claims (ISO/NIST/EU)” and “Non-claims (what AIMO does NOT claim)”; links to coverage maps as informative mappings; AIMO defined as assurance / audit handoff / continuous evidence layer (not a certifier).  
- **Responsibility Boundary**: New “Proof vs assurance boundary” table; compliance/certification decisions clearly external (customer, auditor, certification body); AIMO produces evidence packs + validators.  
- **Trust Package**: Wording aligned with Conformance/Boundary (assurance and audit handoff; no certification or compliance guarantee).

**P3 — Procurement & Disclosure (UK, Japan)**  
- **Primary sources** added: UK (gov.uk ATRS hub, template, guidance), Japan (Digital Agency GenAI procurement guideline, METI/MIC AI Business Guidelines).  
- **Mapping tables** (UK and Japan): Government requirement | AIMO artifact(s) | Evidence Bundle location | Validator coverage | Note (“informative mapping; does not guarantee full compliance”).  
- Framing: burden reduction via reuse of AIMO evidence; no “we meet all requirements” claims.

### Checks run

- `python -m mkdocs build --strict` — **PASS**  
- `python tooling/checks/check_internal_links.py --check` — **PASS**  
- Safety grep (AIMO compliance / certified / guarantees / assures) — **no matches**  
- No version bump — **confirmed** (v0.1.2 unchanged; VERSIONING.md and release workflow untouched)  
- Localization parity — **en + ja** updated for EU, ISO/NIST, conformance, responsibility-boundary, procurement

### Risk notes

- **Docs only.** No schema, code, or workflow changes.  
- Pre-existing MkDocs INFO (e.g. ko locale links, 04-codes anchor) unchanged and unrelated to this PR.

### Branch / PR

- One branch; one PR. No additional branches or PRs.
