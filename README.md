<p align="center">
  <img src="logo.svg" alt="TrustBench" width="400">
</p>

# TrustBench

**[varungurnaney.github.io/trustbench](https://varungurnaney.github.io/trustbench/)** | **[Draft Paper (PDF)](https://github.com/varungurnaney/trustbench/blob/main/TrustBench_Paper.pdf)**

> **v0.2** — 153 tasks across 17 compliance themes. 920 benchmark runs across 6 models. Results are directional — we welcome compliance professionals to contribute tasks and help validate task quality. See the [authoring guide](docs/authoring.md).

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

6 models evaluated on all 153 tasks (920 total runs). 17 compliance themes. 67% D4-D5 tasks.

**How scoring works:** D1-D3 tasks use detection scoring (did the model find the planted gaps?). D4-D5 tasks use F1 scoring — the harmonic mean of recall (what fraction of real gaps were found) and precision (what fraction of the model's reported findings were real gaps). F1 penalizes both missed gaps AND over-reporting.

| Rank | Model | Provider | Avg Score |
|------|-------|----------|-----------|
| 1 | Claude Sonnet 4.6 | Anthropic | **70%** |
| 2 | GPT-5.5 | OpenAI | **64%** |
| 3 | Claude Opus 4.7 | Anthropic | **63%** |
| 4 | Claude Haiku 4.5 | Anthropic | **59%** |
| 5 | GPT-4.1 | OpenAI | **57%** |
| 6 | GPT-4o | OpenAI | **40%** |

**By difficulty level:**

| Level | Tasks | Sonnet | GPT-5.5 | Opus | Haiku | GPT-4.1 | GPT-4o |
|-------|-------|--------|---------|------|-------|---------|--------|
| D1 | 17 | 90% | 93% | 93% | 93% | 69% | 50% |
| D2 | 17 | 95% | 92% | 98% | 96% | 84% | 59% |
| D3 | 17 | 74% | 72% | 68% | 68% | 74% | 71% |
| D4 | 51 | 58% | 56% | 50% | 45% | 46% | 29% |
| D5 | 51 | 67% | 50% | 53% | 47% | 49% | 30% |

**By control domain (avg across all models):**

| Control | Domain | Tasks | Avg |
|---------|--------|-------|-----|
| CC8.1 | Change Mgmt | 9 | 75% |
| C1.1 | Data Protection | 9 | 75% |
| CC6.3 | Data Access | 9 | 66% |
| CC3.1 | Risk Assessment | 9 | 63% |
| CC1.1 | Governance | 9 | 63% |
| CC6.1 | Logical Access | 9 | 63% |
| A1.2 | Backup/Recovery | 9 | 61% |
| P1.1 | Privacy | 9 | 61% |
| CC6.6 | System Boundaries | 9 | 60% |
| CC7.2 | Monitoring | 9 | 56% |
| CC7.1 | Vuln Mgmt + Maint | 18 | 55% |
| CC9.1 | Vendor Mgmt | 9 | 55% |
| CC6.4 | Physical Security | 9 | 54% |
| PI1.1 | System Integrity | 9 | 53% |
| CC1.4 | HR Security | 9 | 51% |
| CC7.3 | Incident Response | 9 | 36% |

**Incident Response is the hardest domain (36% avg).** Change Management and Data Protection are the easiest (75%).

### A note on scoring and over-reporting

F1 scoring penalizes models that report findings beyond the planted gaps. In a real audit, this is debatable — extra findings might be legitimate compliance observations. Our keyword-based scorer cannot distinguish "useful extra finding" from "noise." This favors concise models over thorough ones. Sonnet's lead is partly driven by reporting fewer findings per task. For v2, we plan to add an LLM-as-judge secondary scorer to evaluate extra findings. The primary keyword score remains for reproducibility.

See [Leaderboard](LEADERBOARD.md) for full results.

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
