<p align="center">
  <img src="logo.svg" alt="TrustBench" width="400">
</p>

# TrustBench

> **This is an early-stage project (v0.1).** The current task set has 20 tasks across 8 controls — enough to show meaningful differentiation but not yet statistically robust. We need 50+ tasks before this benchmark produces reliable aggregate scores. If you're a compliance professional, we'd welcome your help building tasks grounded in real audit findings. See the [authoring guide](docs/authoring.md).

A benchmark for evaluating LLMs on security compliance auditing.

TrustBench measures whether models can review audit evidence, cross-reference documents, identify control gaps, and distinguish real findings from documented exceptions. Tasks are framework-agnostic — the initial set covers SOC 2, with the schema supporting ISO 27001, HIPAA, PCI-DSS, and any control-based standard.

## Quick Start

```bash
git clone https://github.com/your-repo/trustbench.git
cd trustbench
pip install -r requirements.txt

# Run a single task
python3 -m trustbench.cli run tasks/cc6.1-3-001 --model claude-sonnet-4-6

# Run all tasks
python3 -m trustbench.cli run-all --model claude-sonnet-4-6

# See results
python3 -m trustbench.cli leaderboard

# Validate task schemas
python3 -m trustbench.cli validate
```

Requires an `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` environment variable depending on the model.

## Results

6 models evaluated on all 20 tasks (120 total runs). D4-D5 tasks use F1 scoring (penalizes false positives). D1-D3 use detection-based scoring.

| Rank | Model | Provider | Avg Score | Highest | Lowest |
|------|-------|----------|-----------|---------|--------|
| 1 | Claude Sonnet 4.6 | Anthropic | **82%** | 100% (4 tasks) | 36% (cc9.1-5) |
| 2 | Claude Opus 4.7 | Anthropic | **72%** | 100% (4 tasks) | 15% (cc9.1-5) |
| 3 | GPT-5.5 | OpenAI | **71%** | 100% (4 tasks) | 15% (cc6.6-5) |
| 4 | GPT-4.1 | OpenAI | **61%** | 100% (cc8.1-1) | 0% (cc3.1-5, cc7.2-2) |
| 5 | Claude Haiku 4.5 | Anthropic | **61%** | 100% (3 tasks) | 12% (cc3.1-5) |
| 6 | GPT-4o | OpenAI | **44%** | 100% (2 tasks) | 0% (cc3.1-5, cc7.2-2) |

**Per-task breakdown (all 20 tasks, grouped by difficulty):**

| Task | D | Control | Sonnet | Opus | GPT-5.5 | GPT-4.1 | Haiku | GPT-4o | Avg |
|------|---|---------|--------|------|---------|---------|-------|--------|-----|
| cc8.1-1-001 | D1 | Change Mgmt | 100% | 100% | 100% | 100% | 100% | 100% | **100%** |
| cc6.1-1-002 | D1 | Logical Access | 100% | 100% | 100% | 75% | 100% | 50% | **88%** |
| cc7.2-2-001 | D2 | Monitoring | 75% | 100% | 75% | 0% | 100% | 0% | **58%** |
| cc6.1-3-001 | D3 | Logical Access | 100% | 88% | 100% | 89% | 100% | 78% | **92%** |
| cc6.3-3-001 | D3 | Data Access | 100% | 100% | 100% | 80% | 80% | 60% | **87%** |
| cc8.1-4-001 | D4 | Change Mgmt | 92% | 80% | 86% | 92% | 92% | 100% | **90%** |
| cc6.1-4-001 | D4 | Logical Access | 100% | 75% | 100% | 86% | 67% | 50% | **80%** |
| a1.2-4-001 | D4 | Backup/Recovery | 100% | 62% | 80% | 80% | 32% | 60% | **69%** |
| cc9.1-4-001 | D4 | Vendor Mgmt | 73% | 67% | 100% | 67% | 80% | 18% | **67%** |
| cc3.1-4-001 | D4 | Risk Assessment | 73% | 62% | 50% | 80% | 67% | 44% | **63%** |
| cc6.3-4-001 | D4 | Data Access | 67% | 57% | 60% | 55% | 67% | 40% | **58%** |
| cc6.6-4-001 | D4 | System Boundaries | 100% | 57% | 62% | 55% | 25% | 44% | **57%** |
| cc7.2-4-001 | D4 | Monitoring | 89% | 67% | 67% | 20% | 42% | 20% | **51%** |
| cc8.1-5-001 | D5 | Change Mgmt | 83% | 91% | 73% | 71% | 43% | 80% | **74%** |
| cc7.2-5-001 | D5 | Monitoring | 67% | 91% | 83% | 91% | 59% | 43% | **72%** |
| a1.2-5-001 | D5 | Backup/Recovery | 89% | 67% | 73% | 80% | 80% | 30% | **70%** |
| cc6.1-5-001 | D5 | Logical Access | 83% | 67% | 57% | 62% | 30% | 31% | **55%** |
| cc6.6-5-001 | D5 | System Boundaries | 55% | 33% | 15% | 20% | 27% | 20% | **28%** |
| cc9.1-5-001 | D5 | Vendor Mgmt | 36% | 40% | 15% | 20% | 14% | 20% | **24%** |
| cc3.1-5-001 | D5 | Risk Assessment | 55% | 40% | 33% | 0% | 12% | 0% | **23%** |

**No model dominates.** Sonnet leads overall but scored 36% on vendor judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73%). GPT-4o scored 100% on change management but 0% on risk assessment. Each model has blind spots.

**Three tasks average below 28%.** cc3.1-5-001 (risk assessment, 23%), cc9.1-5-001 (vendor incident, 24%), and cc6.6-5-001 (boundary materiality, 28%). Two models scored 0% on risk assessment judgment. These require materiality assessment where auditors disagree.

**Sonnet leads because it's both thorough and concise.** It achieves 100% recall on 16 of 20 tasks (vs 13 for GPT-5.5) while reporting an average of 7.4 findings per task (vs 8.5 for GPT-5.5, 9.6 for Opus). Larger models find the gaps but also report more non-planted observations — legitimate in a real audit, but penalized by F1 against a defined ground truth. This is a known limitation of keyword-based scoring: it cannot distinguish "useful extra finding" from "false positive."

See [Task Reference](docs/tasks.md) for per-task analysis and [Leaderboard](LEADERBOARD.md) for full results.

## Task Structure

Each task is a directory containing `task.json` and an `evidence/` folder:

```
tasks/cc6.1-4-001/
  task.json                          # Task definition
  evidence/
    access-control-policy.md         # Policy document
    gcp-service-accounts.json        # Technical configuration
    exception-register.csv           # CISO-approved exceptions
    business-continuity-plan.md      # Noise document
```

Tasks span 5 difficulty levels. D4-D5 tasks make up ~62% of the benchmark:

| Level | Skill | % of tasks |
|-------|-------|-----------|
| D1-D2 | Single-document gap detection | 15% |
| D3 | Cross-document reasoning | 10% |
| D4 | Red herring filtering + noise | 35% |
| D5 | Materiality judgment | 40% |

## Documentation

- [Task Reference](docs/tasks.md) — all 10 tasks with evidence structure, planted findings, and complexity analysis
- [Schema Reference](docs/schema.md) — task.json fields, evidence types, finding types
- [Task Authoring Guide](docs/authoring.md) — how to create tasks, D4-D5 design patterns
- [Scoring Deep Dive](docs/scoring.md) — detection, precision, F1 with worked examples
- [Evaluation Guide](docs/running.md) — CLI usage, API keys, cost estimates

## Contributing

We're looking for compliance professionals to contribute tasks. See the [authoring guide](docs/authoring.md).

## License

MIT
