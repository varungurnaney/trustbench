<p align="center">
  <img src="logo.svg" alt="TrustBench" width="400">
</p>

# TrustBench

> **This is an early-stage project (v0.1).** The current task set has 10 tasks across 6 controls — not enough to draw reliable conclusions about model performance. Results shown below are preliminary and will change as more tasks are added. We need 50+ tasks across all difficulty levels before this benchmark produces statistically meaningful scores. If you're a compliance professional, we'd welcome your help building tasks grounded in real audit findings. See the [authoring guide](docs/authoring.md).

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

| Task | GPT-5.5 | Opus 4.7 | Sonnet 4.6 | GPT-4o |
|------|---------|----------|------------|--------|
| CC8.1-D4 (change mgmt, 6 gaps + 2 red herrings) | 100% | 80% | 92% | 100% |
| CC7.2-D5 (monitoring judgment, 5 gaps) | 100% | 91% | 67% | 43% |
| CC9.1-D4 (vendor mgmt, 4 gaps + 2 red herrings) | 100% | 67% | 73% | 18% |
| **Average** | **100%** | **79%** | **77%** | **54%** |

D4-D5 tasks successfully differentiate models that score identically on D3. GPT-5.5 is the only model to score 100% across all D4-D5 tasks. Recall is high across models — precision (not over-reporting, not flagging red herrings) is what separates the rest.

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
| D1 | Single-document gap detection | 12.5% |
| D2 | Subtle gap detection | 12.5% |
| D3 | Cross-document reasoning | 12.5% |
| D4 | Red herring filtering + noise | 25% |
| D5 | Materiality judgment | 37.5% |

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
