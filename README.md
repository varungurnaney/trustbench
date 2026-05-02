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

6 models evaluated on all 20 tasks (120 total runs). D4-D5 tasks use F1 scoring (penalizes false positives). D1-D3 use detection recall.

| Rank | Model | Provider | Avg Score (all 20) | Highest | Lowest |
|------|-------|----------|-------------------|---------|--------|
| 1 | GPT-5.5 | OpenAI | **82%** | 100% (8 tasks) | 18% (cc6.6-5) |
| 2 | Claude Sonnet 4.6 | Anthropic | **73%** | 100% (3 tasks) | 36% (cc9.1-5) |
| 3 | Claude Opus 4.7 | Anthropic | **65%** | 100% (2 tasks) | 33% (cc6.6-5) |
| 4 | GPT-4.1 | OpenAI | **57%** | 92% (cc8.1-4) | 0% (cc3.1-5, cc7.2-2) |
| 5 | Claude Haiku 4.5 | Anthropic | **54%** | 100% (cc6.1-3) | 12% (cc3.1-5) |
| 6 | GPT-4o | OpenAI | **43%** | 100% (cc8.1-4) | 0% (cc3.1-5, cc7.2-2) |

**Per-task breakdown (all 20 tasks, grouped by difficulty):**

| Task | D | Control | GPT-5.5 | Sonnet | Opus | GPT-4.1 | Haiku | GPT-4o | Avg |
|------|---|---------|---------|--------|------|---------|-------|--------|-----|
| cc6.1-1-002 | D1 | Logical Access | 80% | 53% | 100% | 43% | 50% | 44% | **62%** |
| cc8.1-1-001 | D1 | Change Mgmt | 100% | 55% | 38% | 55% | 55% | 75% | **63%** |
| cc7.2-2-001 | D2 | Monitoring | 86% | 38% | 50% | 0% | 53% | 0% | **57%** |
| cc6.1-3-001 | D3 | Logical Access | 100% | 100% | 100% | 89% | 100% | 78% | **94%** |
| cc6.3-3-001 | D3 | Data Access | 67% | 59% | 59% | 62% | 62% | 55% | **60%** |
| cc8.1-4-001 | D4 | Change Mgmt | 100% | 92% | 80% | 92% | 92% | 100% | **93%** |
| cc6.1-4-001 | D4 | Logical Access | 100% | 100% | 75% | 86% | 67% | 50% | **80%** |
| a1.2-4-001 | D4 | Backup/Recovery | 100% | 100% | 62% | 80% | 32% | 60% | **72%** |
| cc3.1-4-001 | D4 | Risk Assessment | 86% | 73% | 62% | 80% | 67% | 44% | **69%** |
| cc9.1-4-001 | D4 | Vendor Mgmt | 100% | 73% | 67% | 67% | 80% | 18% | **67%** |
| cc6.6-4-001 | D4 | System Boundaries | 100% | 100% | 57% | 55% | 25% | 44% | **64%** |
| cc6.3-4-001 | D4 | Data Access | 60% | 67% | 57% | 55% | 67% | 40% | **58%** |
| cc7.2-4-001 | D4 | Monitoring | 86% | 89% | 67% | 40% | 42% | 20% | **57%** |
| cc7.2-5-001 | D5 | Monitoring | 100% | 67% | 91% | 91% | 91% | 43% | **80%** |
| a1.2-5-001 | D5 | Backup/Recovery | 100% | 89% | 67% | 80% | 80% | 30% | **74%** |
| cc8.1-5-001 | D5 | Change Mgmt | 73% | 83% | 91% | 71% | 43% | 80% | **74%** |
| cc6.1-5-001 | D5 | Logical Access | 89% | 83% | 67% | 62% | 30% | 31% | **60%** |
| cc3.1-5-001 | D5 | Risk Assessment | 57% | 55% | 40% | 0% | 12% | 0% | **27%** |
| cc6.6-5-001 | D5 | System Boundaries | 18% | 55% | 33% | 20% | 27% | 20% | **29%** |
| cc9.1-5-001 | D5 | Vendor Mgmt | 33% | 36% | 40% | 20% | 14% | 20% | **27%** |

**No model dominates.** GPT-5.5 leads overall but scored 18% on system boundary judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73%). GPT-4o scored 100% on change management but 0% on risk assessment. Each model has blind spots.

**Three tasks average below 30%.** cc3.1-5-001 (risk assessment), cc9.1-5-001 (vendor incident), and cc6.6-5-001 (boundary materiality) are the hardest tasks. Two models scored 0% on risk assessment judgment. These tasks require materiality assessment where auditors disagree.

**Clear model tiers.** GPT-5.5 and Sonnet are the top tier (75-77%). Opus and GPT-4.1 form the middle tier (60-63%). Haiku and GPT-4o are the lower tier (40-51%) — they find gaps but drown them in false positives.

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
