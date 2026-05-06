# TrustBench Leaderboard

153 tasks. 17 compliance themes. 6 models. 920 total runs.

## Overall Rankings

| Rank | Model | Provider | Avg Score |
|------|-------|----------|-----------|
| 1 | Claude Sonnet 4.6 | Anthropic | **70%** |
| 2 | GPT-5.5 | OpenAI | **64%** |
| 3 | Claude Opus 4.7 | Anthropic | **63%** |
| 4 | Claude Haiku 4.5 | Anthropic | **59%** |
| 5 | GPT-4.1 | OpenAI | **57%** |
| 6 | GPT-4o | OpenAI | **40%** |

## By Difficulty

| Level | Tasks | Sonnet | GPT-5.5 | Opus | Haiku | GPT-4.1 | GPT-4o |
|-------|-------|--------|---------|------|-------|---------|--------|
| D1 | 17 | 90% | 93% | 93% | 93% | 69% | 50% |
| D2 | 17 | 95% | 92% | 98% | 96% | 84% | 59% |
| D3 | 17 | 74% | 72% | 68% | 68% | 74% | 71% |
| D4 | 51 | 58% | 56% | 50% | 45% | 46% | 29% |
| D5 | 51 | 67% | 50% | 53% | 47% | 49% | 30% |

D1-D2 are near-saturated (most models >90%). D4-D5 produce the differentiation.

## By Control Domain

| Control | Domain | Tasks | Sonnet | GPT-5.5 | Opus | Haiku | GPT-4.1 | GPT-4o | Avg |
|---------|--------|-------|--------|---------|------|-------|---------|--------|-----|
| CC8.1 | Change Mgmt | 9 | 84% | 75% | 77% | 71% | 76% | 68% | **75%** |
| C1.1 | Data Protection | 9 | 83% | 84% | 83% | 68% | 77% | 53% | **75%** |
| CC6.3 | Data Access | 9 | 67% | 69% | 71% | 71% | 68% | 48% | **66%** |
| CC3.1 | Risk Assessment | 9 | 70% | 66% | 65% | 56% | 64% | 55% | **63%** |
| CC1.1 | Governance | 9 | 78% | 56% | 65% | 61% | 68% | 48% | **63%** |
| CC6.1 | Logical Access | 9 | 75% | 70% | 70% | 63% | 60% | 38% | **63%** |
| A1.2 | Backup/Recovery | 9 | 75% | 64% | 58% | 64% | 72% | 34% | **61%** |
| P1.1 | Privacy | 9 | 70% | 67% | 63% | 56% | 64% | 42% | **61%** |
| CC6.6 | System Boundaries | 9 | 72% | 70% | 58% | 55% | 66% | 40% | **60%** |
| CC7.2 | Monitoring | 9 | 76% | 61% | 72% | 70% | 35% | 24% | **56%** |
| CC7.1 | Vuln Mgmt + Maint | 18 | 68% | 61% | 58% | 54% | 54% | 35% | **55%** |
| CC9.1 | Vendor Mgmt | 9 | 64% | 66% | 57% | 57% | 59% | 29% | **55%** |
| CC6.4 | Physical Security | 9 | 61% | 59% | 53% | 63% | 55% | 33% | **54%** |
| PI1.1 | System Integrity | 9 | 62% | 58% | 52% | 51% | 49% | 46% | **53%** |
| CC1.4 | HR Security | 9 | 69% | 54% | 62% | 54% | 30% | 36% | **51%** |
| CC7.3 | Incident Response | 9 | 51% | 44% | 51% | 39% | 16% | 11% | **36%** |

## Observations

1. **Sonnet leads at 70%.** Consistent across domains — never the worst on any control. GPT-5.5 (64%) and Opus (63%) are close behind.

2. **Incident Response is the hardest domain (36% avg).** GPT-4.1 scores 16% and GPT-4o scores 11%. These tasks require cross-referencing incident logs, post-mortem reports, and SLA timelines — the most evidence-intensive tasks in the benchmark.

3. **D1-D2 are saturated.** 4 of 6 models score >90% on D1-D2. These tasks validate the harness but don't differentiate frontier models.

4. **D4-D5 scores are 29-67%.** This is where the benchmark has discriminative power. The gap between best (Sonnet 58-67%) and worst (GPT-4o 29-30%) is 30+ percentage points.

5. **GPT-4o consistently trails.** 40% overall, with 11% on Incident Response and 24% on Monitoring. It struggles with multi-document cross-referencing and red herring filtering.

6. **F1 scoring favors concise models.** Sonnet reports fewer extra findings than Opus, which contributes to its higher precision. See the scoring caveat in the README.

## Regenerate

```bash
python3 -m trustbench.cli leaderboard
```
