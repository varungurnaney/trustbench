# TrustBench Leaderboard

> Preliminary results from 20 tasks across 8 controls. 6 models evaluated on all 15 D4-D5 tasks.

## Overall Rankings

Average F1 score across D4-D5 tasks. F1 penalizes both missed gaps (recall) and false positives (precision).

| Rank | Model | Provider | Avg F1 | Tasks | Highest | Lowest |
|------|-------|----------|--------|-------|---------|--------|
| 1 | GPT-5.5 | OpenAI | **77%** | 13 | 100% (5 tasks) | 18% (cc6.6-5) |
| 2 | Claude Sonnet 4.6 | Anthropic | **75%** | 13 | 100% (3 tasks) | 36% (cc9.1-5) |
| 3 | Claude Opus 4.7 | Anthropic | **63%** | 13 | 91% (cc7.2-5, cc8.1-5) | 33% (cc6.6-5) |
| 4 | GPT-4.1 | OpenAI | **60%** | 15 | 92% (cc8.1-4) | 0% (cc3.1-5) |
| 5 | Claude Haiku 4.5 | Anthropic | **51%** | 15 | 92% (cc8.1-4) | 12% (cc3.1-5) |
| 6 | GPT-4o | OpenAI | **40%** | 15 | 100% (cc8.1-4) | 0% (cc3.1-5) |

## Per-Task Breakdown

Sorted by 6-model average (hardest first). All models evaluated on every task.

| Task | D | Control | GPT-5.5 | Sonnet | Opus | GPT-4.1 | Haiku | GPT-4o | Avg |
|------|---|---------|---------|--------|------|---------|-------|--------|-----|
| cc3.1-5-001 | D5 | Risk Assessment | 57% | 55% | 40% | 0% | 12% | 0% | **27%** |
| cc9.1-5-001 | D5 | Vendor Mgmt | 33% | 36% | 40% | 20% | 14% | 20% | **27%** |
| cc6.6-5-001 | D5 | System Boundaries | 18% | 55% | 33% | 20% | 27% | 20% | **29%** |
| cc7.2-4-001 | D4 | Monitoring | 86% | 89% | 67% | 40% | 42% | 20% | **57%** |
| cc6.3-4-001 | D4 | Data Access | 60% | 67% | 57% | 55% | 67% | 40% | **58%** |
| cc6.1-5-001 | D5 | Logical Access | 89% | 83% | 67% | 62% | 30% | 31% | **60%** |
| cc6.6-4-001 | D4 | System Boundaries | 100% | 100% | 57% | 55% | 25% | 44% | **64%** |
| cc9.1-4-001 | D4 | Vendor Mgmt | 100% | 73% | 67% | 67% | 80% | 18% | **67%** |
| cc3.1-4-001 | D4 | Risk Assessment | 86% | 73% | 62% | 80% | 67% | 44% | **69%** |
| a1.2-4-001 | D4 | Backup/Recovery | 100% | 100% | 62% | 80% | 32% | 60% | **72%** |
| cc8.1-5-001 | D5 | Change Mgmt | 73% | 83% | 91% | 71% | 43% | 80% | **74%** |
| cc7.2-5-001 | D5 | Monitoring | 100% | 67% | 91% | 91% | 91% | 43% | **80%** |
| cc8.1-4-001 | D4 | Change Mgmt | 100% | 92% | 80% | 92% | 92% | 100% | **93%** |

## Observations

1. **Clear model tiers.** GPT-5.5 and Sonnet form the top tier (75-77%). Opus and GPT-4.1 form the middle tier (60-63%). Haiku and GPT-4o are the lower tier (40-51%).

2. **No model dominates across all tasks.** GPT-5.5 leads overall but scored 18% on system boundary judgment. Opus scored 91% on change management judgment (beating GPT-5.5's 73%). GPT-4o scored 100% on change management but 0% on risk assessment. Every model has blind spots.

3. **Three tasks average below 30%.** cc3.1-5-001 (risk assessment judgment), cc9.1-5-001 (vendor incident judgment), and cc6.6-5-001 (boundary materiality) are the hardest. GPT-4.1 and GPT-4o scored 0% on risk assessment judgment — they couldn't identify any of the planted gaps with the right keywords.

4. **Change management is the easiest domain.** cc8.1-4-001 averages 93% across all 6 models. Even GPT-4o scored 100%. The change management evidence structure (change log CSV + policy + CAB minutes) is well-suited to LLM cross-referencing.

5. **Recall is easy. Precision separates.** Haiku achieves 100% recall on 8 of 15 tasks but averages only 51% F1 because it over-reports massively (precision often below 30%). GPT-5.5 and Sonnet are more concise.

6. **GPT-4.1 is inconsistent.** 92% on change management and 91% on monitoring judgment, but 0% on risk assessment judgment. It performs well on structured evidence (change logs, alert data) but fails on ambiguous judgment tasks.

7. **Haiku punches above its weight on some tasks.** 92% on cc8.1-4 (matching GPT-4.1) and 91% on cc7.2-5 (matching Opus). But it collapses on tasks requiring precision — 12% on cc3.1-5 and 14% on cc9.1-5 due to extreme over-reporting.

8. **GPT-4o is the weakest frontier model on compliance.** 40% average, with 0% on risk assessment and 18% on vendor management. It flags red herrings without checking exception registers and misses domain-specific findings (SOC 2 carve-out methodology).

## Regenerate

```bash
python3 -m trustbench.cli leaderboard
```
