# TrustBench: A Benchmark for Evaluating LLMs on Security Compliance Auditing

## Summary

TrustBench is an open benchmark for measuring LLM performance on security compliance evidence review and gap detection. Tasks present models with synthetic audit evidence — policies, configurations, access logs, termination records, exception registers — containing planted compliance gaps, and measure detection accuracy against ground truth. Scoring is deterministic and keyword-based. No LLM-as-judge.

The benchmark is framework-agnostic. The initial task set covers SOC 2 Trust Service Criteria, with the schema designed to support ISO 27001, HIPAA, PCI-DSS, NIST CSF, FedRAMP, and any control-based compliance framework.

The benchmark is in early development. This post describes the design, the task schema, preliminary results from 9 models on a prototype task, and the roadmap to v1.

## Motivation

No benchmark exists for security compliance evaluation. The closest work:

- **AIReg-Bench** (Cambridge, 2025) — 120 samples testing LLMs against EU AI Act articles. Single regulation, single document type, proof-of-concept scale.
- **LegalBench** — 162 legal reasoning tasks. Tests rule-application, not multi-document evidence review.
- **CUAD** — contract clause extraction. Tests document comprehension, not compliance judgment.

None of these test what compliance teams actually do: cross-reference multiple evidence types (policy docs, technical configs, operational logs) against a control requirement, identify deficiencies, and distinguish real gaps from documented exceptions.

This is a gap that cuts across frameworks. Whether you're assessing an access control policy against SOC 2 CC6.1, ISO 27001 A.9.2, or HIPAA § 164.312(d), the underlying audit skill is the same: review evidence, cross-reference artifacts, identify gaps, assess materiality. The task structure is identical — only the control language and acceptance criteria change.

Meanwhile, GRC teams are already using LLMs for evidence review, gap analysis, control mapping, and questionnaire responses across all of these frameworks — with no way to evaluate accuracy systematically.

## Task Design

Each task is a JSON file defining an audit scenario. The schema is framework-agnostic — the `framework` and `control` fields accept any standard:

```json
{
  "id": "cc6.1-4-001",
  "version": "1.0",
  "framework": "SOC2",
  "control": "CC6.1",
  "difficulty": 4,
  "category": "red_herring",
  "evidence_files": [
    {"path": "evidence/access-control-policy.md", "type": "policy"},
    {"path": "evidence/gcp-service-accounts.json", "type": "config"},
    {"path": "evidence/exception-register.csv", "type": "exception_register"}
  ],
  "noise_files": [
    {"path": "evidence/business-continuity-plan-summary.md", "type": "policy"},
    {"path": "evidence/vendor-risk-assessment-q4.csv", "type": "report"}
  ],
  "findings": [
    {
      "id": "F-001",
      "type": "red_herring",
      "title": "Legacy ETL has manual key (valid CISO exception exists)",
      "detection_criteria": {
        "required_keywords": ["legacy-etl", "exception", "approved", "compensating"],
        "minimum_keyword_matches": 3,
        "exclusion_keywords": ["finding", "gap", "violation"]
      }
    },
    {
      "id": "F-002",
      "type": "gap",
      "severity": "critical",
      "title": "Terraform import SA with editor role — exception expired",
      "detection_criteria": {
        "required_keywords": ["terraform", "editor", "expired", "stale", "still active"],
        "minimum_keyword_matches": 3
      }
    }
  ],
  "scoring": {"method": "f1", "max_expected_findings": 8}
}
```

The same schema works for any framework. An ISO 27001 task would set `"framework": "ISO27001"` and `"control": "A.9.2.1"`. A HIPAA task would use `"framework": "HIPAA"` and `"control": "164.312(d)"`. The evidence types, scoring methods, and difficulty levels apply universally.

### Difficulty Levels

| Level | Skill Tested | Structure |
|-------|-------------|-----------|
| 1 | Single-document gap detection | 1 doc, obvious deficiency |
| 2 | Careful reading | 1 doc, gap buried in a table or timeline |
| 3 | Cross-referencing | 3-6 docs, policy contradicts config or logs |
| 4 | Red herring filtering | 3-6 docs + noise files + exception register; some "gaps" have valid explanations |
| 5 | Materiality judgment | Ambiguous scenarios where auditors would disagree |

These levels map to universal audit skills, not framework-specific knowledge. A D3 cross-reference task works the same way whether you're comparing an access policy against an IAM config (SOC 2), a data processing agreement against server logs (HIPAA), or an encryption policy against a TLS configuration (PCI-DSS).

### Evidence Types

The schema supports evidence types common across frameworks:

| Type | Examples |
|------|----------|
| `policy` | Access control policies, incident response plans, data retention policies |
| `config` | IAM credential reports, MFA configs, firewall rules, TLS settings |
| `log` | Termination records, access review logs, backup execution logs, audit trails |
| `spreadsheet` | Service account inventories, asset registers, vendor lists |
| `screenshot` | Console configurations, access review sign-offs, approval emails, dashboard views |
| `ticket` | Change management tickets, access request records |
| `exception_register` | CISO/DPO-approved deviations with compensating controls |
| `report` | Restore test results, penetration test summaries, risk assessments |
| `architecture_diagram` | Network topology, data flow diagrams, system boundary definitions |

Screenshot evidence is sent to models as base64-encoded images via multimodal APIs (Anthropic vision, OpenAI vision). This tests whether models can extract compliance-relevant information from visual evidence — a common audit artifact that text-only benchmarks cannot evaluate.

### Scoring Methods

| Method | Formula | Used For |
|--------|---------|----------|
| `detection_only` | recall = gaps_detected / total_gaps | D1-D2 |
| `detection_and_precision` | recall × min(1, max_expected / model_findings) | D3 |
| `f1` | 2PR / (P+R), where FP includes flagged red herrings | D4-D5 |

Findings of type `red_herring` count as false positives if the model flags them without referencing the exclusion keywords (e.g., "exception," "approved," "mitigated"). Models are not penalized for mentioning red herring topics if they correctly dismiss them.

## Preliminary Results

### D3 — Cross-Reference (Detection Scoring)

9 models on a D3 task: 6 evidence documents, 9 planted gaps (stale service accounts, termination SLA breaches, MFA policy contradictions, access review scope gaps).

| Model | Gaps Detected | Score |
|-------|--------------|-------|
| Claude Opus 4.7 | 9/9 | 100% |
| Claude Sonnet 4.6 | 9/9 | 100% |
| GPT-5.5 | 9/9 | 100% |
| o3 | 9/9 | 100% |
| GPT-4.1 | 8/9 | 89% |
| GPT-4o | 7/9 | 78% |
| GPT-4o-mini | 1/9 | 11% |

D3 is saturated for frontier models — six tied at 100%. GPT-4o-mini caught only the most obvious gap (a 7-day termination delay) and missed all findings requiring cross-document reasoning.

### D4-D5 — Red Herrings, Noise, and Judgment (F1 Scoring)

D4-D5 tasks use F1 scoring, which penalizes both missed gaps and false positives. We ran 4 models across 3 tasks.

**CC8.1-D4: Change Management** — 15 changes in the log. 6 real gaps (freeze violation without CISO approval, retrospective CAB SLA breach, two segregation-of-duties violations, CAB quorum failure on a high-risk change, missing post-implementation verification). 2 red herrings (emergency change during holiday freeze with valid CISO approval; change deployed on freeze start date with pre-freeze CAB approval). 2 noise documents.

| Model | Provider | Recall | Precision | F1 |
|-------|----------|--------|-----------|-----|
| GPT-5.5 | OpenAI | 100% | 100% | 100% |
| GPT-4o | OpenAI | 100% | 100% | 100% |
| Claude Sonnet 4.6 | Anthropic | 100% | 86% | 92% |
| Claude Opus 4.7 | Anthropic | 100% | 67% | 80% |
| GPT-4o-mini | OpenAI | 100% | 30% | 46% |

GPT-5.5 used a concise table format with 7 findings, including a legitimate non-planted issue (kernel patch miscategorized under the Standard Change Catalog). Sonnet explicitly analyzed both red herrings and dismissed them with reasoning. Opus found all gaps but reported 9 findings total (3 legitimate extras that lower precision).

**CC7.2-D5: Monitoring Judgment** — 3 months of alert summary data across 8 alert rules. 5 gaps requiring materiality assessment: two production services deployed without monitoring (25+ days past 5-day SLA), S3 bulk access alert at 95-97% false positive rate for the entire quarter (policy threshold: 30%), SQL injection rule disabled for 2 months (CISO-approved with WAF compensating control), 5 unresolved impossible travel investigations in December, brute force alert SLA adherence drop to 96% during an attack spike. 1 noise document.

| Model | Provider | Recall | Precision | F1 |
|-------|----------|--------|-----------|-----|
| GPT-5.5 | OpenAI | 100% | 100% | 100% |
| Claude Opus 4.7 | Anthropic | 100% | 83% | 91% |
| Claude Sonnet 4.6 | Anthropic | 100% | 50% | 67% |
| GPT-4o | OpenAI | 100% | 28% | 43% |

GPT-5.5 achieved perfect precision — reported only the 5 planted findings. Opus reported ~6 (1 extra). GPT-4o reported ~18, treating every observation as a finding.

**CC9.1-D4: Vendor Management** — 14 vendors across 4 tiers. 4 gaps (Stripe uses GCP as a carved-out subservice org with no independent assessment, Snowflake SOC 2 review pending on a critical vendor, no business reviews for high-tier vendors processing PII, multiple vendors with unassessed carved-out subservice orgs). 2 red herrings (DataRobot — critical vendor without SOC 2 but with active CISO exception and compensating controls; HubSpot — SOC 2 not provided but CISO exception with alternative assessment including ISO 27001 confirmation). 1 noise document.

| Model | Provider | Recall | Precision | F1 |
|-------|----------|--------|-----------|-----|
| GPT-5.5 | OpenAI | 100% | 100% | 100% |
| Claude Sonnet 4.6 | Anthropic | 100% | 57% | 73% |
| Claude Opus 4.7 | Anthropic | 100% | 50% | 67% |
| GPT-4o | OpenAI | 50% | 11% | 18% |

GPT-5.5 scored 100% — found all 4 gaps, correctly dismissed both red herrings. GPT-4o flagged both red herrings as findings without checking the exception register and missed the subservice org carve-out gaps.

### Summary

**Cross-task average F1 (D4-D5):**

| Rank | Model | Provider | CC8.1-D4 | CC7.2-D5 | CC9.1-D4 | Average |
|------|-------|----------|----------|----------|----------|---------|
| 1 | GPT-5.5 | OpenAI | 100% | 100% | 100% | **100%** |
| 2 | Claude Opus 4.7 | Anthropic | 80% | 91% | 67% | **79%** |
| 3 | Claude Sonnet 4.6 | Anthropic | 92% | 67% | 73% | **77%** |
| 4 | Gemini 2.5 Flash | Google | 0% | 67% | 100% | **56%** |
| 5 | GPT-4o | OpenAI | 100% | 43% | 18% | **54%** |

GPT-5.5 is the only model to score 100% across all D4-D5 tasks — perfect recall, perfect precision, correct red herring handling on every task. This indicates the current D4-D5 tasks still have headroom; harder tasks (deeper CSV haystacks, calendar math traps, conflicting evidence) are needed to differentiate at the top.

Below GPT-5.5, the picture is more nuanced. Claude Opus 4.7 leads on the judgment task (91%) but loses precision on red herrings. Gemini 2.5 Flash is inconsistent — 100% on vendor management, 17% on change management. GPT-4o has strong change management performance but fails on vendor-specific compliance knowledge. No model except GPT-5.5 is consistent across all compliance domains.

Gemini 3.1 Pro and Flash Lite could not be benchmarked due to free-tier API quota limits. Results will be added when paid API access is available.

These are preliminary results from 10 tasks across 6 controls. The v1 benchmark will include 64 tasks across 8 controls.

## Comparison to Existing Benchmarks

| | SWE-bench Pro | CyBench | CyberGym | GAIA | TrustBench |
|---|---|---|---|---|---|
| **Domain** | Software engineering | Cybersecurity CTFs | Vulnerability analysis | General reasoning | Compliance auditing |
| **Input** | Issue + repo | CTF challenge | Vulnerable source | Question + files | Evidence package |
| **Output** | Code patch | Flag string | PoC exploit | Short answer | Audit findings |
| **Evaluation** | Test suite | String match | Crash/no-crash | Exact match | Keyword + precision |
| **Environment** | Docker | Kali Docker | Docker (no network) | Browser + tools | None (document-only) |
| **Tasks** | 1,865 | 40 | 1,507 | 466 | 64 (v1 target) |
| **Top D4-D5 avg** | ~46% | 17.5% | ~20% | ~45% | 100% (GPT-5.5) |

### Design Decisions

**Keyword scoring over LLM-as-judge.** Deterministic and reproducible. Using an LLM to grade compliance assessments introduces circular evaluation and non-deterministic results. Keywords are calibrated broadly to catch varied phrasing. LLM-as-judge may be added as an optional secondary scorer in v2.

**Free-text output.** Compliance assessments are narrative. Forcing structured JSON output would test format compliance, not audit competence.

**No Docker.** Tasks are document-based. The model reads files and produces findings. This makes the benchmark runnable with just API keys — no infrastructure.

**Framework-agnostic schema.** The `framework` and `control` fields are strings, not enums constrained to SOC 2. The same task structure, difficulty levels, and scoring methods apply to any control-based compliance standard. The initial task set uses SOC 2 because it has the most widespread adoption and the clearest control language, but the architecture imposes no framework dependency.

**Explicit difficulty levels.** Each level tests a specific audit skill. Score-by-difficulty curves show where a model's compliance reasoning breaks down — independent of which framework the task targets.

### Anti-Saturation Mechanisms

Learned from benchmarks that saturated (HumanEval at 95%+, SWE-bench Verified deprecated, GPQA Diamond exceeded by models):

- Precision scoring penalizes over-reporting
- Red herring findings require checking exception registers before flagging
- Noise documents test selective reading
- D5 judgment tasks have no single correct answer — models must assess materiality
- Large CSV logs (92+ rows) test whether models process full documents or truncate

## Roadmap

**Current state:** 10 tasks across 6 controls (CC6.1, CC6.3, CC7.2, CC8.1, CC9.1, A1.2). Eval harness supports Anthropic and OpenAI APIs with all three scoring methods, red herring handling, noise document support, and multimodal evidence (screenshots). Schema defined and validated.

**v1 target:**
- 64 tasks across 8 controls (adding CC6.6, CC3.1)
- D4-D5 tasks are the majority of the benchmark (~60-70% of tasks). D1-D3 tasks serve as calibration — they establish a floor and verify the harness works. The benchmark's discriminative power comes from D4 (red herring filtering, noise documents) and D5 (materiality judgment, conflicting evidence, calendar math).
- Per-control target: 1 D1, 1 D2, 1 D3, 2 D4, 3 D5
- Baseline evaluation across 8 models
- Public leaderboard with scores by difficulty and control
- pip-installable package

**v2 and beyond:**
- ISO 27001 Annex A task set
- HIPAA Security Rule task set
- PCI-DSS v4.0 task set
- NIST CSF 2.0 task set
- LLM-as-judge as optional secondary scorer
- Community-contributed tasks from auditors and assessors

The schema is designed so that adding a new framework requires only authoring tasks — no changes to the eval harness, scoring, or CLI.

## Code

The schema, eval harness, and prototype tasks are at [github.com/your-repo/trustbench](https://github.com/your-repo/trustbench).

```bash
git clone https://github.com/your-repo/trustbench.git
cd trustbench
pip install -r requirements.txt

# Run a single task
python3 -m trustbench.cli run tasks/cc6.1-3-001 --model claude-sonnet-4-6

# Validate all tasks against schema
python3 -m trustbench.cli validate

# Generate leaderboard from results
python3 -m trustbench.cli leaderboard
```

Contributions welcome — particularly from compliance professionals who can author tasks grounded in real audit findings across any framework.
