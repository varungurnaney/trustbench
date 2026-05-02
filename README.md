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

Preliminary results from 20 tasks. Three models were evaluated across all 13 D4-D5 tasks: GPT-5.5 (OpenAI), Claude Opus 4.7 (Anthropic), and Claude Sonnet 4.6 (Anthropic). Additional models were tested on subsets.

### D3 — Cross-Reference (1 task, 9 models)

One D3 task (cc6.1-3-001): 6 evidence documents, 9 planted gaps. Scored on detection only (recall). This task is saturated — 6 models tie at 100%.

| Model | Provider | Gaps | Score |
|-------|----------|------|-------|
| Claude Opus 4.7 | Anthropic | 9/9 | 100% |
| Claude Sonnet 4.6 | Anthropic | 9/9 | 100% |
| Claude Haiku 4.5 | Anthropic | 9/9 | 100% |
| GPT-5.5 | OpenAI | 9/9 | 100% |
| o3 | OpenAI | 9/9 | 100% |
| GPT-4.1 | OpenAI | 8/9 | 89% |
| GPT-4o | OpenAI | 7/9 | 78% |
| GPT-4o-mini | OpenAI | 1/9 | 11% |

### D4-D5 — Red Herrings, Noise, and Judgment (13 tasks, 3 models)

Scored with F1 (penalizes both missed gaps and false positives). GPT-5.5, Opus 4.7, and Sonnet 4.6 were evaluated on all 13 tasks. GPT-4o was evaluated on only 3 of 13 (cc8.1-4, cc7.2-5, cc9.1-4) and is excluded from the average.

| Rank | Model | Provider | Avg F1 | Highest | Lowest |
|------|-------|----------|--------|---------|--------|
| 1 | GPT-5.5 | OpenAI | **79%** | 100% (5 tasks) | 18% (cc6.6-5) |
| 2 | Claude Sonnet 4.6 | Anthropic | **69%** | 100% (3 tasks) | 36% (cc9.1-5) |
| 3 | Claude Opus 4.7 | Anthropic | **63%** | 91% (cc7.2-5, cc8.1-5) | 33% (cc6.6-5) |

### What the scores mean

**No model dominates.** GPT-5.5 leads overall but scored 18% on system boundary judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73% on the same task). Each model has blind spots.

**Recall is easy. Precision separates.** Most models find most gaps (high recall). Scores diverge on how many false positives are reported. Opus consistently over-reports (100% recall but 40-50% precision on many tasks). GPT-5.5 is more concise.

**D5 judgment tasks are hardest.** The three hardest tasks average 35-51% across all models:
- cc6.6-5-001 (system boundary materiality): **35% avg**
- cc9.1-5-001 (vendor incident judgment): **36% avg**
- cc3.1-5-001 (risk assessment judgment): **51% avg**

See [Task Reference](docs/tasks.md) for per-task analysis and [Leaderboard](LEADERBOARD.md) for full results.

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
