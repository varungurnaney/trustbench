# Schema Reference

The canonical schema is at `schema/trustbench-schema.json`. All tasks validate against it via `trustbench validate`.

## Task Fields

### Identity

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier. Format: `{control}-{difficulty}-{sequence}`. Example: `cc6.1-4-001` |
| `version` | string | yes | Schema version. Currently `"1.0"` |
| `framework` | string | yes | Compliance framework. Examples: `"SOC2"`, `"ISO27001"`, `"HIPAA"`, `"PCI-DSS"` |
| `control` | string | yes | Control identifier. Examples: `"CC6.1"`, `"A.9.2.1"`, `"164.312(d)"` |
| `control_description` | string | yes | Full text of the control requirement |

### Classification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `difficulty` | integer (1-5) | yes | See [Difficulty Levels](#difficulty-levels) |
| `category` | enum | yes | Primary skill tested: `detection`, `cross_reference`, `noise_filtering`, `red_herring`, `judgment` |

### Evidence

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `evidence_files` | array of objects | yes | Documents provided to the model. Each has `path`, `type`, `description` |
| `noise_files` | array of objects | no | Irrelevant documents included to test precision. Same structure as evidence_files |

### Prompt

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | string | yes | Audit instructions given to the model |

### Findings

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `findings` | array of objects | yes | Ground-truth findings. See [Finding Object](#finding-object) |

### Scoring

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scoring.method` | enum | no | `detection_only`, `detection_and_precision`, `f1`. Default: `detection_only` |
| `scoring.max_expected_findings` | integer | no | Upper bound on reasonable findings. Used by `detection_and_precision` scoring |

### Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `metadata.author` | string | yes | Who created the task |
| `metadata.created_date` | string (date) | yes | Creation date (YYYY-MM-DD) |
| `metadata.estimated_human_time` | string | yes | How long this would take a competent auditor. Examples: `"5 minutes"`, `"45 minutes"` |
| `metadata.documents_count` | integer | yes | Total documents provided (evidence + noise) |
| `metadata.relevant_documents_count` | integer | yes | Documents that contain or relate to findings |
| `metadata.tags` | array of strings | no | Descriptive tags |

## Difficulty Levels

| Level | Name | Structure | Scoring Method |
|-------|------|-----------|---------------|
| 1 | Trivial | 1 document, obvious gap | `detection_only` |
| 2 | Subtle | 1 document, gap buried in detail | `detection_only` |
| 3 | Cross-reference | 3-6 documents, policy contradicts config/logs | `detection_and_precision` |
| 4 | Red herring | 3-6 docs + noise + exceptions; some gaps have valid explanations | `f1` |
| 5 | Judgment | Ambiguous materiality; auditors would disagree | `f1` |

D4-D5 tasks make up ~62% of the benchmark. D1-D3 are calibration tasks.

## Evidence Types

| Type | Description | File formats |
|------|-------------|-------------|
| `policy` | Written policies, procedures, plans | `.md` |
| `config` | Technical configurations (IAM, MFA, firewall) | `.json`, `.yaml`, `.md` |
| `log` | Operational records (terminations, backups, access reviews) | `.csv` |
| `spreadsheet` | Inventories, registers, lists | `.csv` |
| `screenshot` | Console views, approval emails, dashboard captures | `.png`, `.jpg`, `.jpeg`, `.webp` |
| `ticket` | Change/access request records | `.csv`, `.json`, `.md` |
| `exception_register` | Approved deviations with compensating controls | `.csv` |
| `report` | Test results, assessments, summaries | `.json`, `.md` |
| `architecture_diagram` | Network topology, data flow, system boundaries | `.png`, `.jpg`, `.md` |

Screenshot and architecture diagram files are sent to models as base64-encoded images via multimodal APIs.

## Finding Object

Each finding in the `findings` array has:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique within the task. Example: `"F-001"` |
| `type` | enum | yes | `"gap"` (real finding) or `"red_herring"` (has valid explanation) |
| `severity` | enum | yes | `"critical"`, `"high"`, `"medium"`, `"low"` |
| `title` | string | yes | Short finding title |
| `description` | string | yes | Detailed explanation |
| `evidence_sources` | array of strings | yes | Which evidence files must be referenced |
| `expected_reasoning` | string | yes | The reasoning chain a competent auditor would follow |
| `detection_criteria` | object | yes | See below |

### Detection Criteria

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `required_keywords` | array of strings | yes | Keywords that indicate detection |
| `minimum_keyword_matches` | integer | yes | How many keywords must match (typically 2-3) |
| `exclusion_keywords` | array of strings | no | For red herrings: keywords that indicate the model correctly dismissed the finding |

### Gap vs Red Herring

**`type: "gap"`** — A real compliance deficiency. The model should flag this. Counts as a true positive if detected.

**`type: "red_herring"`** — Looks like a gap but has a valid explanation elsewhere in the evidence (e.g., a CISO-approved exception with compensating controls). The model should NOT flag this as a finding. If the model flags it without referencing exclusion keywords, it counts as a false positive. If the model mentions the topic but correctly notes the exception (matches exclusion keywords), no penalty.
