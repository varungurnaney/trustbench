# Task Authoring Guide

## Overview

A TrustBench task simulates a compliance audit scenario. You provide evidence documents with planted gaps, and the benchmark measures whether models find them.

Each task is a directory:

```
tasks/{control}-{difficulty}-{sequence}/
  task.json
  evidence/
    policy.md
    config.json
    logs.csv
    ...
```

## Step by Step

### 1. Pick a control and difficulty

Choose a control from any framework (SOC 2, ISO 27001, HIPAA, etc.) and a difficulty level:

- **D1-D3**: Start here if you're new to task authoring
- **D4-D5**: Where the benchmark needs the most contributions

### 2. Create the directory

```bash
mkdir -p tasks/cc6.1-4-002/evidence
```

Naming convention: `{control}-{difficulty}-{sequence}`, all lowercase. The sequence number avoids collisions.

### 3. Write the evidence documents

Create realistic documents in `evidence/`. Use the formats auditors actually work with:

- `.md` for policies and procedures
- `.json` for technical configurations (IAM, MFA, firewall rules)
- `.csv` for logs and inventories
- `.png`/`.jpg` for screenshots of console configs or approval emails

Make them realistic. Use plausible company names, dates, employee names, and system details. The documents should read like actual audit evidence, not contrived test cases.

### 4. Plant the gaps

Insert compliance deficiencies into the evidence. These should be:

- **Based on real control failures** you've seen in audits
- **Detectable from the evidence provided** — don't plant a gap that requires information not in the documents
- **Clearly a gap** (for D1-D3) or **arguably a gap** (for D5)

For D4 tasks, also plant at least one **red herring** — something that looks like a gap but has a valid explanation in another document (e.g., an exception register entry).

### 5. Write task.json

Use an existing task as a template. The best templates:

- **D1-D2**: `tasks/cc8.1-1-001/task.json`
- **D3**: `tasks/cc6.3-3-001/task.json`
- **D4**: `tasks/cc6.1-4-001/task.json` (has red herrings + noise files)
- **D5**: `tasks/a1.2-5-001/task.json` (judgment calls)

Key fields to get right:

- `detection_criteria.required_keywords` — pick 7-10 keywords, varying in specificity. Include the specific entity name (e.g., `"jenkins-legacy"`), the category of issue (e.g., `"rotation"`), and the nature of the gap (e.g., `"expired"`).
- `detection_criteria.minimum_keyword_matches` — use 2 for D1-D2, 3 for D3-D5. Higher thresholds reduce false detections but risk missing legitimate findings phrased differently.
- `expected_reasoning` — write out the reasoning chain. This isn't used in scoring but documents why the gap matters and helps future contributors understand the task.

### 6. Add noise files (D4-D5)

For D4 and D5 tasks, include 2-5 documents in `noise_files` that are plausible audit evidence but irrelevant to the control under review. Examples:

- Business continuity plan for an access control task
- Vendor risk assessment for a change management task
- Employee handbook for a backup/recovery task

Good noise files are ones that a hasty reviewer might reference — they contain security-related content but don't relate to the specific control being assessed.

### 7. Validate

```bash
python3 -m trustbench.cli validate
```

Fix any schema errors before testing.

### 8. Spot-test

Run the task against one model to verify the gaps are detectable and the keywords trigger correctly:

```bash
python3 -m trustbench.cli run tasks/your-task --model claude-sonnet-4-6
```

Check:
- Do all planted gaps get detected? If not, broaden the keywords.
- Does the model flag the red herrings? If not, the red herring might be too obviously benign — make it more ambiguous.
- Does the keyword scorer match findings you'd consider correctly detected? If not, adjust `minimum_keyword_matches`.

## D4-D5 Design Patterns

These patterns create tasks that differentiate frontier models. Use them when authoring D4 and D5 tasks.

### Exception Chain Reasoning (D4)

Plant a gap, then add an exception register entry that partially covers it. The exception should have a condition that is no longer met.

Example: Service account has a manual key → exception register shows CISO approval → but the exception expired 3 months ago, or the exception requires quarterly review and the last review was 8 months ago.

The model must: find the gap → check the exception → verify the exception's conditions → conclude the exception doesn't apply.

### Calendar Math (D4-D5)

Use dates that require business-day calculations or span holidays.

Example: Employee terminated November 27 (Wednesday before Thanksgiving). Access removed December 3 (Tuesday). Policy says "within 24 hours." Naive count: 6 days. Correct count: 2 business days (Nov 28 = Thanksgiving, Nov 29 = holiday, Nov 30-Dec 1 = weekend). A good model should note the holiday context.

### Large CSV Haystack (D4-D5)

Create CSV logs with 100-200+ rows. Bury the anomaly deep — row 147 of 200. Most entries should be clean/normal.

Example: 92 days of backup logs where 90 succeed and 2 fail — one on day 34, one on day 47. The model must process the full file to find them.

### Conflicting Evidence (D5)

Two documents provide contradictory information about the same control. No third document resolves the conflict.

Example: The Okta user export shows 156 active users. The HR headcount report shows 148 employees + 6 contractors = 154. The access review log says 152 users were reviewed. Three different numbers. The model should identify the discrepancy and note that compliance cannot be confirmed without reconciliation — not pick a side.

### Materiality Judgment (D5)

Plant a technical violation that's arguably immaterial.

Example: A single backup failed out of 92 days (99% success rate). The failure was due to a transient network error, and WAL archiving provided continuous point-in-time recovery capability throughout. Is this a finding or an observation? Strict interpretation: backup control failed. Pragmatic interpretation: compensating control (WAL) maintained RPO. Both are defensible.

The task should reward models that:
- Identify the issue
- Acknowledge the compensating control
- State their assessment of materiality with reasoning
- Do NOT dogmatically call it critical or dismiss it

### Noise Document Trap (D4)

Include a noise document that contains language similar to the control under review but is about a different topic.

Example: For a CC6.1 (access control) task, include a vendor risk assessment that mentions "access" and "controls" in the context of third-party vendor management — not the organization's own access controls. Models that cite this document in their findings are over-indexing on keyword matches instead of understanding scope.

## Quality Checklist

Before submitting a task:

- [ ] `python3 -m trustbench.cli validate` passes
- [ ] Evidence documents are realistic (plausible names, dates, system details)
- [ ] Gaps are based on real control failures, not contrived scenarios
- [ ] Detection keywords are broad enough to catch varied phrasing (7-10 keywords, threshold 2-3)
- [ ] D4 tasks have at least 1 red herring with exclusion keywords
- [ ] D4-D5 tasks have 2-5 noise files
- [ ] Spot-tested against at least 1 model
- [ ] `expected_reasoning` is written for every finding
- [ ] Evidence files referenced in `evidence_sources` actually exist
