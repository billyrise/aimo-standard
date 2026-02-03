# Minimal End-to-End Story (Authoring SSOT)

**Status**: Authoring input — not user-facing documentation  
**Canonical language**: English (EN)

This document provides a narrative walkthrough of the evidence bundle workflow: input → bundle → validate → checksum → release reference.

---

## Scenario

An organization wants to create an audit-ready evidence bundle for their AI system usage.

---

## Step 1: Create Input Records

The organization has the following governance records:

### Request Record

```json
{
  "id": "REQ-001",
  "timestamp": "2026-01-10T09:00:00Z",
  "actor": "requester",
  "scope": "Example AI use",
  "rationale": "Minimal bundle example"
}
```

### Review/Approval Record

```json
{
  "id": "REV-001",
  "timestamp": "2026-01-12T14:00:00Z",
  "actor": "reviewer",
  "decision": "approved",
  "rationale": "Within policy",
  "references": ["REQ-001"]
}
```

### Evidence Record

```json
{
  "id": "EV-20260115-001",
  "timestamp": "2026-01-15T10:00:00Z",
  "source": "example-system",
  "summary": "Minimal evidence record for Evidence Bundle example.",
  "tags": ["example", "evidence-bundle"]
}
```

---

## Step 2: Assemble Evidence Bundle

Create the bundle structure following `aimo-standard.schema.json`:

**File: `root.json`**

```json
{
  "version": "v0.1.0",
  "dictionary": {
    "entries": [
      { "key": "REQ-001", "label": "Request", "description": "AI use request" },
      { "key": "EV-20260115-001", "label": "Evidence", "description": "Use evidence record" }
    ]
  },
  "evidence": [
    {
      "id": "EV-20260115-001",
      "timestamp": "2026-01-15T10:00:00Z",
      "source": "example-system",
      "summary": "Minimal evidence record for Evidence Bundle example.",
      "tags": ["example", "evidence-bundle"]
    }
  ],
  "request": {
    "id": "REQ-001",
    "timestamp": "2026-01-10T09:00:00Z",
    "actor": "requester",
    "scope": "Example AI use",
    "rationale": "Minimal bundle example"
  },
  "review": {
    "id": "REV-001",
    "timestamp": "2026-01-12T14:00:00Z",
    "actor": "reviewer",
    "decision": "approved",
    "rationale": "Within policy",
    "references": ["REQ-001"]
  },
  "change_log": {
    "id": "CHG-001",
    "timestamp": "2026-01-15T10:00:00Z",
    "actor": "system",
    "change_description": "Initial bundle creation",
    "references": ["EV-20260115-001"]
  }
}
```

**Source**: `examples/evidence_bundle_minimal/root.json`

---

## Step 3: Validate Bundle

Run the reference validator:

```bash
python validator/src/validate.py examples/evidence_bundle_minimal/root.json
```

**Expected output**:
```
OK
```

If validation fails, fix errors and re-run.

---

## Step 4: Generate Checksums

Create SHA-256 checksums for verification:

```bash
cd examples/evidence_bundle_minimal/
sha256sum root.json dictionary.json > SHA256SUMS.txt
```

**Example SHA256SUMS.txt**:
```
abc123...  root.json
def456...  dictionary.json
```

---

## Step 5: Package Artifacts

Create a zip archive:

```bash
zip -r evidence_bundle.zip examples/evidence_bundle_minimal/
```

---

## Step 6: Reference Release Version

Document which AIMO Standard version the bundle aligns with:

```
AIMO Standard Version: v0.1.0
Bundle created: 2026-01-15
Reference: https://github.com/billyrise/aimo-standard/releases/tag/v0.1.0
```

---

## Step 7: Auditor Verification

When auditors receive the bundle, they verify:

### 7a. Verify checksums

```bash
sha256sum -c SHA256SUMS.txt
```

### 7b. Verify bundle structure

```bash
# Clone official AIMO Standard
git clone https://github.com/billyrise/aimo-standard.git
cd aimo-standard
git checkout v0.1.0

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run validator
python validator/src/validate.py path/to/root.json
```

### 7c. Verify version alignment

Check that stated version exists at GitHub Releases.

---

## Traceability Chain

```
REQ-001 (Request)
    ↓ references
REV-001 (Review)
    ↓ approved
EV-20260115-001 (Evidence)
    ↓ recorded
CHG-001 (Change Log)
```

---

## Authoring Notes

- This story uses actual examples from `examples/evidence_bundle_minimal/`.
- Do NOT fabricate outputs; use real validator behavior.
- This narrative is the authoring source for user-facing examples documentation.
