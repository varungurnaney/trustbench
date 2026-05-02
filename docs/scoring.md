# Scoring

TrustBench uses three scoring methods matched to task difficulty. All scoring is deterministic — keyword-based, no LLM-as-judge, reproducible across runs.

## Detection Only

**Used for:** D1-D2 tasks (single-document gap detection).

**Formula:** `score = gaps_detected / total_gaps`

Pure recall. Did the model find the planted gaps?

**Example:** A task has 4 planted gaps. The model finds 3.

```
score = 3 / 4 = 75%
```

The model could report 20 additional findings and still score 75%. Over-reporting is not penalized at this level because the task is simple enough that false positives are expected — models naturally identify issues beyond what was planted.

## Detection and Precision

**Used for:** D3 tasks (cross-reference).

**Formula:** `score = recall × precision_penalty`

Where:
- `recall = gaps_detected / total_gaps`
- `precision_penalty = min(1.0, max_expected_findings / model_findings_count)`

This penalizes models that over-report. If `max_expected_findings` is 12 and the model reports 20 findings, the precision penalty is `12/20 = 0.6`.

**Example:** A task has 5 gaps and `max_expected_findings: 12`. The model detects 4 gaps and reports 16 total findings.

```
recall           = 4 / 5 = 0.80
precision_penalty = min(1.0, 12 / 16) = 0.75
score            = 0.80 × 0.75 = 60%
```

A model that found the same 4 gaps but only reported 8 findings:

```
recall           = 4 / 5 = 0.80
precision_penalty = min(1.0, 12 / 8) = 1.0
score            = 0.80 × 1.0 = 80%
```

## F1

**Used for:** D4-D5 tasks (red herrings, noise, judgment).

**Formula:** `score = 2 × precision × recall / (precision + recall)`

Where:
- `true_positives` = gaps correctly detected
- `false_negatives` = gaps missed
- `false_positives` = (model findings that don't match any gap) + (red herrings incorrectly flagged)
- `recall = TP / (TP + FN)`
- `precision = TP / (TP + FP)`

### Worked Example

A D4 task has:
- 3 real gaps (type: `gap`)
- 1 red herring (type: `red_herring`) — a service account key with a valid CISO exception

The model reports 7 findings:
- Correctly identifies all 3 real gaps → TP = 3
- Flags the red herring as a finding without mentioning the exception → FP from red herring = 1
- Reports 3 additional findings not in the ground truth → FP from over-reporting = 3
- Misses 0 gaps → FN = 0

```
recall    = 3 / (3 + 0)         = 1.0
precision = 3 / (3 + 1 + 3)     = 0.43
f1        = 2 × 1.0 × 0.43 / (1.0 + 0.43) = 0.60
```

Now consider a model that found all 3 gaps, correctly dismissed the red herring (mentioned the exception), and reported only 4 total findings:

```
TP = 3, FP = 1 (one finding not in ground truth), FN = 0
recall    = 3 / 3              = 1.0
precision = 3 / (3 + 1)        = 0.75
f1        = 2 × 1.0 × 0.75 / (1.0 + 0.75) = 0.86
```

And a perfect model — 3 gaps found, red herring dismissed, 3 total findings:

```
TP = 3, FP = 0, FN = 0
recall    = 1.0
precision = 1.0
f1        = 1.0
```

### Red Herring Handling

A finding of type `red_herring` is scored differently:

1. If the model's response matches the finding's `required_keywords` but does NOT match any `exclusion_keywords` → the model flagged it as a real finding → **counts as a false positive**
2. If the model's response matches both `required_keywords` AND `exclusion_keywords` → the model mentioned the topic but correctly dismissed it → **no penalty**
3. If the model doesn't mention it at all → **no penalty**

Exclusion keywords are things like `"exception"`, `"approved"`, `"mitigated"`, `"compensating"` — language that indicates the model checked for and found the valid justification.

## How Model Findings Are Counted

The scorer estimates how many total findings the model reported by looking for numbered lists and heading patterns in the response. It uses the following regex patterns and takes the highest count:

- `### Finding 1`, `### Gap 2`, etc.
- `**Finding 1:**`, `**Gap 2:**`, etc.
- `### 1.`, `### 2.`, etc.
- Numbered list items starting with `1. **`
- Any `###` headings

If no pattern matches, it falls back to counting lines that start with `N. ` (numbered list items).

This is a heuristic. It works well for the structured responses that models typically produce for audit assessments. It may miscount if a model uses an unusual format.

## Why Keyword Scoring

**Determinism.** Run the same task twice, get the same score. LLM-as-judge introduces variance — different runs of the judge produce different scores.

**No circular evaluation.** Using Claude to grade Claude's compliance assessment conflates model capability with judge capability. If the judge model has a blind spot, it propagates.

**Cost.** Keyword matching is free. Running a judge model on 64 tasks × 8 models = 512 additional API calls per evaluation run.

**Transparency.** Results show exactly which keywords matched. You can inspect why a finding was scored as detected or missed.

### Limitations

- A model might detect a gap using language that doesn't match any keywords. This is a false negative in scoring, not in the model's capability. Mitigation: keywords are calibrated broadly, and the `minimum_keyword_matches` threshold is typically 2-3 out of 7-10 keywords.
- A model might use a keyword in an unrelated context, triggering a false detection. Mitigation: requiring multiple keyword matches reduces this risk.
- Keyword scoring cannot evaluate reasoning quality. Two models might both "detect" a gap, but one provides sound reasoning while the other gets there by accident. This is an accepted limitation for v1.
