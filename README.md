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

Preliminary results across D3-D5 tasks. D4-D5 tasks use F1 scoring (penalizes false positives and over-reporting).

**D3 — Cross-reference (CC6.1, 6 docs, 9 gaps, detection scoring):**

| Model | Gaps Detected | Score |
|-------|--------------|-------|
| Claude Opus 4.7 | 9/9 | 100% |
| Claude Sonnet 4.6 | 9/9 | 100% |
| GPT-5.5 | 9/9 | 100% |
| o3 | 9/9 | 100% |
| GPT-4.1 | 8/9 | 89% |
| GPT-4o | 7/9 | 78% |
| GPT-4o-mini | 1/9 | 11% |

**D4-D5 — Red herrings, noise, and judgment (F1 scoring):**

| Rank | Model | Avg D4-D5 F1 | Tasks |
|------|-------|-------------|-------|
| 1 | GPT-5.5 | **79%** | 13 |
| 2 | Claude Sonnet 4.6 | **69%** | 13 |
| 3 | Claude Opus 4.7 | **63%** | 13 |

Hardest tasks (avg F1 across all models): cc9.1-5-001 vendor judgment (36%), cc6.6-5-001 boundary judgment (35%), cc3.1-5-001 risk assessment judgment (51%). No model scores above 57% on these.

See [Task Reference](docs/tasks.md) for per-task results and analysis.

Full leaderboard: [LEADERBOARD.md](LEADERBOARD.md)

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
