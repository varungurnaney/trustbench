# TrustBench Leaderboard

> Preliminary results from 10 prototype tasks. Full benchmark results pending v1 release.

## D3 — Cross-Reference (Detection Scoring)

Task `cc6.1-3-001`: 6 evidence documents, 9 planted gaps. Policy vs IAM config vs termination logs vs Okta config vs access review logs vs service account inventory.

| Rank | Model | Provider | Gaps Detected | Score |
|------|-------|----------|--------------|-------|
| 1 | Claude Opus 4.7 | Anthropic | 9/9 | 100% |
| 1 | Claude Opus 4.6 | Anthropic | 9/9 | 100% |
| 1 | Claude Sonnet 4.6 | Anthropic | 9/9 | 100% |
| 1 | Claude Haiku 4.5 | Anthropic | 9/9 | 100% |
| 1 | GPT-5.5 | OpenAI | 9/9 | 100% |
| 1 | o3 | OpenAI | 9/9 | 100% |
| 7 | GPT-4.1 | OpenAI | 8/9 | 89% |
| 8 | GPT-4o | OpenAI | 7/9 | 78% |
| 9 | GPT-4o-mini | OpenAI | 1/9 | 11% |

D3 is saturated for frontier models. Six models tied at 100%.

## D4-D5 — Red Herrings, Noise, and Judgment (F1 Scoring)

F1 scoring penalizes both missed gaps (recall) and false positives (precision). Models that over-report or flag red herrings as findings score lower.

### CC8.1-D4: Change Management
6 gaps, 2 red herrings (CHG-414: emergency during holiday freeze with CISO approval; CHG-415: deployed on freeze start date with pre-freeze CAB approval), 2 noise documents. Tests: holiday freeze exceptions, retrospective CAB SLAs, segregation of duties, CAB quorum requirements.

*Scores updated after fixing keyword scoring — original run had false positives from generic keywords ("freeze", "approved") matching unrelated context.*

| Rank | Model | Provider | Recall | Precision | F1 | Red Herring Handling |
|------|-------|----------|--------|-----------|-----|----------------------|
| 1 | GPT-5.5 | OpenAI | 100% | 100% | **100%** | Discussed CHG-415 in context of freeze policy but correctly noted it was pre-approved |
| 1 | GPT-4o | OpenAI | 100% | 100% | **100%** | Didn't discuss either red herring — focused only on real gaps |
| 3 | Claude Sonnet 4.6 | Anthropic | 100% | 86% | **92%** | Explicitly dismissed both with reasoning ("approved before freeze") |
| 4 | Claude Opus 4.7 | Anthropic | 100% | 67% | **80%** | Correctly dismissed CHG-414. Reported 9 findings total (3 non-planted extras) |
| 5 | GPT-4o-mini | OpenAI | 100% | 30% | **46%** | ~20 findings reported — real gaps buried in noise |

**Analysis — what models do well and where they fail on change management:**

- **GPT-5.5** used a concise table format with 7 findings. Found a legitimate non-planted issue (kernel patch incorrectly categorized as Standard Change under SC-001 which covers non-kernel patches only). Grouped CHG-410 and CHG-415 together but correctly noted CHG-415's pre-approval. The strongest response.
- **GPT-4o** was the most concise (5 findings). It simply ignored both red herrings rather than analyzing them — this scores well but doesn't demonstrate the reasoning that Sonnet showed. It also consolidated the two segregation violations (CHG-407 + CHG-411) into one finding.
- **Claude Sonnet 4.6** explicitly discussed both red herrings and dismissed them with reasoning: noted CHG-414's CISO approval and CHG-415's Dec 16 pre-freeze CAB approval. Only 1 extra finding beyond the 6 planted gaps. The most thorough red herring analysis.
- **Claude Opus 4.7** found all 6 gaps but reported 9 total findings. The 3 extras included legitimate observations (emergency approval via Slack DM lacks audit trail, verbal emergency approvals not independently evidenced, standard change deployed outside maintenance window). These are real issues an auditor might note — Opus over-reports because it's thorough, not because it's wrong.
- **GPT-4o-mini** found all 6 gaps (100% recall) but reported ~20 total findings, flagging nearly every line item in the change log. It lacks the judgment to distinguish a finding from an observation.

### CC7.2-D5: Monitoring & Alerting (Judgment)
5 gaps, 0 red herrings, 1 noise document. Tests: alert false positive rate thresholds, SLA adherence materiality, disabled detection rules with compensating controls, unresolved investigations.

| Rank | Model | Provider | Recall | Precision | F1 |
|------|-------|----------|--------|-----------|-----|
| 1 | GPT-5.5 | OpenAI | 100% | 100% | **100%** |
| 2 | Claude Opus 4.7 | Anthropic | 100% | 83% | **91%** |
| 3 | Claude Sonnet 4.6 | Anthropic | 100% | 50% | **67%** |
| 4 | GPT-4o | OpenAI | 100% | 28% | **43%** |

Notes:
- GPT-5.5 achieved perfect precision — reported only the 5 planted findings.
- Opus reported ~6 findings (1 extra). GPT-4o reported ~18.

### CC9.1-D4: Vendor Management
4 gaps, 2 red herrings, 1 noise document. Tests: subservice organization carve-out assessment requirements, SOC 2 review timeliness, exception register validation.

| Rank | Model | Provider | Recall | Precision | F1 | Red Herring Handling |
|------|-------|----------|--------|-----------|-----|----------------------|
| 1 | GPT-5.5 | OpenAI | 100% | 100% | **100%** | Both correctly dismissed |
| 2 | Claude Sonnet 4.6 | Anthropic | 100% | 57% | **73%** | Both correctly dismissed |
| 3 | Claude Opus 4.7 | Anthropic | 100% | 50% | **67%** | Both correctly dismissed |
| 4 | GPT-4o | OpenAI | 50% | 11% | **18%** | Both flagged as findings |

Notes:
- GPT-4o flagged DataRobot and HubSpot as findings without checking the exception register — both have current CISO-approved exceptions.
- GPT-4o also missed the Stripe and Amplitude subservice org carve-out gaps.

## Cross-Task Summary (D4-D5)

| Rank | Model | Provider | CC8.1-D4 | CC7.2-D5 | CC9.1-D4 | Average F1 |
|------|-------|----------|----------|----------|----------|------------|
| 1 | GPT-5.5 | OpenAI | 100% | 100% | 100% | **100%** |
| 2 | Claude Opus 4.7 | Anthropic | 80% | 91% | 67% | **79%** |
| 3 | Claude Sonnet 4.6 | Anthropic | 92% | 67% | 73% | **77%** |
| 4 | GPT-4o | OpenAI | 100% | 43% | 18% | **54%** |
| 5 | GPT-4o-mini | OpenAI | 46% | — | — | **46%** |

## Observations

1. **GPT-5.5 is the only model to score 100% across all D4-D5 tasks.** Perfect recall, perfect precision, correct red herring handling. It also found legitimate non-planted issues (e.g., kernel patch miscategorized under Standard Change Catalog). The D4-D5 tasks need to be harder to differentiate GPT-5.5 from the field.

2. **D4-D5 tasks differentiate models that D3 cannot.** Six models tied at 100% on D3. On D4-D5, scores range from 18% to 100%.

3. **Recall is easy. Precision separates.** Most frontier models achieve 100% recall. Scores diverge on how many false positives the model reports. Opus reported 9 findings on a 6-gap task (3 extras were legitimate observations, but they lower the F1 score). GPT-4o reported exactly 5.

4. **Red herring handling varies by approach, not just accuracy.** Claude models explicitly analyzed red herrings and dismissed them with reasoning. GPT-4o and GPT-5.5 often just didn't mention red herrings at all. Both approaches score well, but the Claude approach demonstrates deeper reasoning.

5. **Model-specific blind spots exist across providers.** GPT-4o scored 100% on change management but 18% on vendor management (missed carve-out assessment gaps, flagged both exception-covered vendors). No model except GPT-5.5 is consistent across all compliance domains.

6. **Over-reporting is a real problem for compliance use cases.** GPT-4o-mini reported ~20 findings on a 6-gap task. Opus reported 9. In a real audit, each false positive costs analyst time to investigate and dismiss. The F1 scoring method correctly penalizes this — a model that finds everything but reports 3x as many findings as necessary is less useful than one that finds everything and reports only real issues.

7. **Keyword scoring limitations were exposed during this analysis.** The original CC8.1-D4 run used generic keywords ("freeze", "approved") that matched incidentally from unrelated context, inflating some scores. After tightening to task-specific keywords ("CHG-415", "rate limit thresholds", "December 20 freeze"), scores changed for multiple models. This underscores the importance of careful keyword calibration — a v2 scorer using LLM-as-judge would avoid this class of errors.

8. **Google Gemini models could not be benchmarked** due to free-tier API quota limits. Results will be added when paid API access is available.

## Regenerate

```bash
python3 -m trustbench.cli leaderboard
```
