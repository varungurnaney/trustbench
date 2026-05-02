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

Preliminary results from 20 tasks across 8 controls. Three models were evaluated across all tasks. Scoring uses F1 on D4-D5 tasks (penalizes false positives) and detection recall on D1-D3.

| Rank | Model | Provider | Avg Score | Tasks Evaluated | Highest | Lowest |
|------|-------|----------|-----------|-----------------|---------|--------|
| 1 | GPT-5.5 | OpenAI | **79%** | 14 | 100% (6 tasks) | 18% (cc6.6-5) |
| 2 | Claude Sonnet 4.6 | Anthropic | **75%** | 15 | 100% (3 tasks) | 36% (cc9.1-5) |
| 3 | Claude Opus 4.7 | Anthropic | **68%** | 15 | 100% (2 tasks) | 33% (cc6.6-5) |

**Per-task breakdown (D4-D5 only, sorted by average, hardest first):**

| Task | D | Control | GPT-5.5 | Sonnet 4.6 | Opus 4.7 | Avg |
|------|---|---------|---------|------------|----------|-----|
| cc6.6-5-001 | D5 | System Boundaries | 18% | 55% | 33% | **35%** |
| cc9.1-5-001 | D5 | Vendor Mgmt | 33% | 36% | 40% | **36%** |
| cc3.1-5-001 | D5 | Risk Assessment | 57% | 55% | 40% | **51%** |
| cc6.3-4-001 | D4 | Data Access | 60% | 67% | 57% | **61%** |
| cc3.1-4-001 | D4 | Risk Assessment | 86% | 73% | 62% | **74%** |
| cc9.1-4-001 | D4 | Vendor Mgmt | 100% | 73% | 67% | **80%** |
| cc6.1-5-001 | D5 | Logical Access | 89% | 83% | 67% | **80%** |
| cc7.2-4-001 | D4 | Monitoring | 86% | 89% | 67% | **81%** |
| cc8.1-5-001 | D5 | Change Mgmt | 73% | 83% | 91% | **82%** |
| cc6.6-4-001 | D4 | System Boundaries | 100% | 100% | 57% | **86%** |
| cc7.2-5-001 | D5 | Monitoring | 100% | 67% | 91% | **86%** |
| a1.2-4-001 | D4 | Backup/Recovery | 100% | 100% | 62% | **87%** |
| cc8.1-4-001 | D4 | Change Mgmt | 100% | 92% | 80% | **91%** |

**No model dominates.** GPT-5.5 leads overall but scored 18% on system boundary judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73% on the same task). Each model has blind spots.

**D5 judgment tasks are hardest.** Three tasks average below 51% — no model scores above 57% on these. They require materiality assessment where reasonable auditors would disagree.

**Recall is easy. Precision separates.** Most models find most gaps. Scores diverge on false positives. Opus consistently over-reports (100% recall but 40-50% precision). GPT-5.5 is more concise.

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
