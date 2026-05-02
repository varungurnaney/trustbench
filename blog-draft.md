# TrustBench: A Benchmark for Evaluating LLMs on Security Compliance Auditing

TrustBench is an open benchmark for measuring how well LLMs perform security compliance evidence review and gap detection. Each task presents a model with synthetic audit evidence -- policies, configurations, access logs, change records, vendor assessments, exception registers -- containing planted compliance gaps. The model produces an audit report, and scoring is deterministic: keyword matching for detection tasks, F1 for tasks with red herrings and noise. No LLM-as-judge. The initial task set covers SOC 2 Trust Service Criteria across 20 tasks at five difficulty levels. The schema is framework-agnostic and supports ISO 27001, HIPAA, PCI-DSS, and any control-based standard without changes to the eval harness.

## Leaderboard

6 models, 20 tasks, 120 total runs.

| Rank | Model | Provider | Avg Score | Highest | Lowest |
|------|-------|----------|-----------|---------|--------|
| 1 | Claude Sonnet 4.6 | Anthropic | 82% | 100% (4 tasks) | 36% (cc9.1-5) |
| 2 | Claude Opus 4.7 | Anthropic | 72% | 100% (4 tasks) | 15% (cc9.1-5) |
| 3 | GPT-5.5 | OpenAI | 71% | 100% (4 tasks) | 15% (cc6.6-5) |
| 4 | GPT-4.1 | OpenAI | 61% | 100% (cc8.1-1) | 0% (cc3.1-5, cc7.2-2) |
| 5 | Claude Haiku 4.5 | Anthropic | 61% | 100% (3 tasks) | 12% (cc3.1-5) |
| 6 | GPT-4o | OpenAI | 44% | 100% (2 tasks) | 0% (cc3.1-5, cc7.2-2) |

## Motivation

No benchmark exists for security compliance evaluation. GRC teams are already using LLMs for evidence review, gap analysis, control mapping, and questionnaire responses -- with no way to evaluate accuracy systematically. The closest prior work is AIReg-Bench (Cambridge, 2025): 120 samples testing LLMs against EU AI Act articles. It covers a single regulation, a single document type, and is proof-of-concept scale.

The gap is not framework-specific. Whether you are assessing an access control policy against SOC 2 CC6.1, ISO 27001 A.9.2, or HIPAA 164.312(d), the underlying audit skill is the same: review evidence, cross-reference artifacts, identify gaps, assess materiality. The task structure is identical -- only the control language and acceptance criteria change.

TrustBench is framework-agnostic. The initial task set uses SOC 2 because it has the most widespread adoption and the clearest control language, but the schema supports any control-based compliance framework. The `framework` and `control` fields are strings, not enums. Adding ISO 27001, HIPAA, or PCI-DSS requires only authoring tasks -- no changes to the eval harness, scoring, or CLI.

## Methodology

Each task is a JSON file defining an audit scenario. A task specifies a compliance framework, a control requirement, a difficulty level, a set of evidence files (with planted gaps), optional noise documents, and a ground-truth list of findings with keyword-based detection criteria.

Models receive the evidence package and a system prompt instructing them to produce an audit report identifying compliance gaps. Output is free-text -- compliance assessments are narrative, and forcing structured JSON would test format compliance rather than audit competence.

Scoring is deterministic:
- **D1-D2:** Detection only (recall = gaps detected / total gaps).
- **D3:** Detection with precision penalty (recall × min(1, max_expected / model_findings)).
- **D4-D5:** F1 scoring — the harmonic mean of precision and recall. Recall measures what fraction of planted gaps the model found. Precision measures what fraction of the model's reported findings match planted gaps. F1 = 2 × precision × recall / (precision + recall). A model that finds all 5 gaps but reports 15 total findings gets recall=100% but precision=33%, yielding F1=50%. Findings of type `red_herring` count as false positives if the model flags them without referencing exclusion keywords (e.g., "exception," "approved," "compensating control"). Models are not penalized for mentioning red herring topics if they correctly dismiss them.

The schema is framework-agnostic. An ISO 27001 task sets `"framework": "ISO27001"` and `"control": "A.9.2.1"`. A HIPAA task uses `"framework": "HIPAA"` and `"control": "164.312(d)"`. Evidence types, scoring methods, and difficulty levels apply universally.

## Difficulty Levels

| Level | Tasks | Skill Tested | Structure |
|-------|-------|-------------|-----------|
| D1 | 2 | Single-document gap detection | 1 document, obvious deficiency. The gap is stated in the evidence -- the model needs to recognize it as a control violation. |
| D2 | 1 | Careful reading | 1 document, subtle gap. The deficiency is buried in a table, a timeline, or an exception clause. |
| D3 | 2 | Cross-referencing | 3-6 documents. The gap only becomes visible when comparing a policy against a configuration, or a log against a procedure. No single document contains the full picture. |
| D4 | 8 | Red herring filtering | 3-6 documents + noise files + exception registers. Some apparent gaps have valid explanations documented in the exception register. Models must check exceptions before flagging. Noise documents test selective reading -- irrelevant evidence that should be ignored. |
| D5 | 7 | Materiality judgment | Ambiguous scenarios where reasonable auditors would disagree. Findings require assessing severity, evaluating compensating controls, and making judgment calls about whether a deficiency is material. |

D4 and D5 tasks make up 75% of the benchmark. D1-D3 tasks serve as calibration -- they establish a floor and verify the harness works. The benchmark's discriminative power comes from D4 (filtering signal from noise) and D5 (professional judgment under ambiguity).

## Example: D1 Task (cc8.1-1-001)

**Change management policy review.** A single policy document describing the organization's change management process. Three planted gaps:

1. **Segregation of duties violation:** The policy states that "changes are deployed by the requesting engineer." The same person who requests a change also deploys it -- no independent review or approval gate.
2. **No testing gate:** Changes move from development to production with no required testing phase. The policy describes a development and deployment process but omits pre-production validation.
3. **Emergency change controls:** Emergency changes are approved via verbal confirmation with no documented time limit for retroactive documentation. There is no requirement to formalize the approval after the fact.

This is a single-document, detection-only task. The model reads one policy and identifies three gaps. All three are stated directly in the text -- the model needs to recognize them as control violations, not extract hidden information. Scoring is recall-based: gaps detected divided by total gaps.

## Example: D4 Task (cc8.1-4-001)

**Change management with red herrings.** A change log containing 15 changes, an exception register, a change management policy, a Standard Change Catalog, and 2 noise documents.

Six real gaps:
- A change deployed during holiday freeze without CISO approval
- A retrospective CAB submission that breached the 48-hour SLA
- Two segregation-of-duties violations (developer self-approving changes)
- A CAB vote on a high-risk change that failed quorum requirements
- A missing post-implementation verification on a database migration
- A self-review where the same engineer authored and reviewed a change

Two red herrings designed to trap models that do not check the exception register:
- **CHG-414:** An emergency change deployed during the holiday freeze. Appears to be a freeze violation, but the CISO approved it via Slack within 30 minutes, and the exception register documents the approval with a valid justification. Models that flag this without referencing the exception register lose precision.
- **CHG-415:** A change deployed on December 20, the first day of the holiday freeze. Appears to violate the freeze, but the change was pre-approved at the December 16 CAB meeting -- before the freeze started. The CAB minutes confirm the approval date.

Two noise documents are included: a business continuity plan summary and a vendor risk assessment. Neither is relevant to change management. Models that extract "findings" from these documents are penalized.

This task is hard because it requires multiple reasoning steps that most models skip. The model must cross-reference the change log against the exception register to identify valid exceptions. It must do calendar math -- comparing deployment dates against freeze start dates and CAB meeting dates. It must compare columns in a CSV to detect segregation-of-duties violations (requester == approver, or author == reviewer). It must count CAB votes to check quorum. And it must ignore two documents that contain no relevant information.

## Example: D5 Task (cc9.1-5-001)

**Vendor management judgment.** A vendor inventory, security incident reports, SOC 2 review documentation, and risk assessment records for a critical and a high-tier vendor.

The critical vendor experienced a security incident. It met the contractual 72-hour notification SLA and contained the incident within 48 hours. However, there was a 3-week period of uncertainty regarding data exposure -- the vendor could not confirm whether customer data was accessed until the forensic investigation completed.

A second vendor has a qualified SOC 2 Type II opinion. The organization acknowledged the qualification in an internal memo but did not perform a formal risk assessment of the qualification's impact.

Every finding in this task requires judgment:
- The critical vendor met the notification SLA. Does that excuse three weeks of uncertainty about data exposure? Should the organization have notified its own customers during the uncertainty window?
- Acknowledging a qualified SOC 2 opinion is better than ignoring it. But is acknowledgment without a documented risk assessment sufficient? The qualification may affect controls relevant to the organization's own compliance posture.
- The incident was contained in 48 hours. Is the response adequate given the severity, or should the vendor's risk tier be re-evaluated?

There are no clear-cut answers. A conservative auditor would flag all of these. A pragmatic auditor might accept the SLA compliance as sufficient and treat the acknowledgment as adequate. The task tests whether models can identify the judgment calls and articulate the considerations on both sides, rather than producing a binary pass/fail.

**Average score across all 6 models on this task: 27%. No model scored above 40%.** This is the hardest task in the benchmark. Models either over-report (flagging everything as a gap, losing precision) or under-report (accepting the vendor's contractual compliance at face value, missing the judgment issues).

## Key Findings

- **No model dominates.** Sonnet leads at 82% average but scores 36% on vendor judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73% on the same task). Every model has at least one task below 40%.
- **Clear performance tiers.** Sonnet leads at 82%. Opus and GPT-5.5 form the middle tier (71-72%). GPT-4.1 and Haiku at 61%. GPT-4o trails at 44%.
- **D5 judgment tasks are the hardest.** Three D5 tasks average below 28% across all models. These require materiality assessment and professional judgment that current models cannot reliably perform.
- **Recall is easy; precision separates.** Most frontier models detect the majority of planted gaps. The differentiator is precision — whether the model avoids flagging red herrings, ignores noise documents, and refrains from reporting non-issues.
- **Change management is the easiest domain** (93% average). The gaps are procedural and well-defined. **Vendor and risk judgment is the hardest** (23-24% average). These require assessing adequacy rather than detecting violations.

### A note on F1 scoring and over-reporting

The F1 metric penalizes models that report more findings than the planted ground truth. In a real audit, this penalization is debatable. When Opus reports 9 findings on a task with 5 planted gaps, the extra 4 might be legitimate compliance observations that a human auditor would include in their report. But our keyword-based scorer cannot distinguish "useful extra finding" from "noise" — any reported finding that doesn't match a planted gap is counted as a false positive, lowering precision and therefore F1.

This means the current scoring favors concise models over thorough ones. Sonnet's lead over Opus and GPT-5.5 is partly driven by Sonnet reporting fewer extra findings (7.4 avg per task vs 8.5 for GPT-5.5 and 9.6 for Opus) — not necessarily because those extra findings are wrong. Sonnet also has genuinely higher recall (100% on 16 of 20 tasks vs 13 for GPT-5.5), so its lead is not purely a precision artifact. But the gap between models would narrow under a scorer that could credit legitimate extra findings.

This is a known limitation of keyword-based, ground-truth scoring for compliance tasks, where the space of valid findings is open-ended. For v2, we plan to add an optional LLM-as-judge secondary scorer that can evaluate whether extra findings are legitimate. The primary keyword-based score will remain for reproducibility and determinism.

## What's Next

- **More tasks.** Expanding from 20 to 64+ tasks across additional SOC 2 controls.
- **More frameworks.** ISO 27001 Annex A, HIPAA Security Rule, and PCI-DSS v4.0 task sets. The schema supports these without harness changes.
- **LLM-as-judge for v2.** An optional secondary scorer that can evaluate whether extra findings are legitimate compliance observations or noise. This addresses the over-reporting penalty described above.
- **Community contributions.** The benchmark benefits from tasks authored by compliance professionals who can ground scenarios in real audit findings across any framework.

## Try It

```bash
git clone https://github.com/GetDelve/trustbench.git
cd trustbench
pip install -r requirements.txt

# Run a single task
python3 -m trustbench.cli run tasks/cc8.1-1-001 --model claude-sonnet-4-6

# Run the full benchmark
python3 -m trustbench.cli run --all --model gpt-5.5

# Validate all tasks against schema
python3 -m trustbench.cli validate

# Generate leaderboard from results
python3 -m trustbench.cli leaderboard
```
