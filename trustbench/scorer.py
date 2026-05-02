"""Scoring engine for TrustBench evaluations."""

import re
from dataclasses import dataclass, field
from .loader import Task, Finding


@dataclass
class FindingResult:
    finding_id: str
    finding_type: str  # "gap" or "red_herring"
    severity: str
    detected: bool
    matched_keywords: list[str]
    total_keywords: int
    correctly_dismissed: bool = False  # for red herrings: model mentioned exclusion keywords


@dataclass
class TaskScore:
    task_id: str
    model: str
    scoring_method: str
    recall: float
    precision: float
    f1: float
    score: float  # the primary score based on scoring_method
    gaps_detected: int
    gaps_total: int
    red_herrings_flagged: int  # false positives from red herrings
    red_herrings_total: int
    model_findings_count: int
    finding_results: list[FindingResult] = field(default_factory=list)


def _count_model_findings(response: str) -> int:
    patterns = [
        r'(?m)^#+\s*(?:Finding|Gap|Issue|Deficiency)\s*\d+',
        r'(?m)^#{1,4}\s*\d+[\.\):]',
        r'(?m)^\*\*(?:Finding|Gap|Issue)\s*\d+',
        r'(?m)^\d+\.\s+\*\*',
        r'(?m)^###\s+',
        r'(?m)^\|\s*\d+\s*\|',
    ]
    counts = []
    for pattern in patterns:
        matches = re.findall(pattern, response)
        if matches:
            counts.append(len(matches))

    if counts:
        return max(counts)

    numbered = re.findall(r'(?m)^\d+\.\s+\S', response)
    return len(numbered) if numbered else 1


def score_finding(finding: Finding, response_lower: str) -> FindingResult:
    matched = [kw for kw in finding.required_keywords if kw.lower() in response_lower]
    detected = len(matched) >= finding.minimum_keyword_matches

    correctly_dismissed = False
    if finding.type == "red_herring" and finding.exclusion_keywords:
        exclusion_matched = [kw for kw in finding.exclusion_keywords if kw.lower() in response_lower]
        correctly_dismissed = len(exclusion_matched) >= 1

    return FindingResult(
        finding_id=finding.id,
        finding_type=finding.type,
        severity=finding.severity,
        detected=detected,
        matched_keywords=matched,
        total_keywords=len(finding.required_keywords),
        correctly_dismissed=correctly_dismissed,
    )


def score_response(task: Task, response: str, model: str) -> TaskScore:
    response_lower = response.lower()
    model_findings_count = _count_model_findings(response)

    finding_results = []
    gaps_detected = 0
    gaps_total = 0
    red_herrings_flagged = 0
    red_herrings_total = 0

    for finding in task.findings:
        result = score_finding(finding, response_lower)
        finding_results.append(result)

        if finding.type == "gap":
            gaps_total += 1
            if result.detected:
                gaps_detected += 1
        elif finding.type == "red_herring":
            red_herrings_total += 1
            if result.detected and not result.correctly_dismissed:
                red_herrings_flagged += 1

    recall = gaps_detected / gaps_total if gaps_total > 0 else 1.0

    true_positives = gaps_detected
    false_positives = max(0, model_findings_count - true_positives) + red_herrings_flagged
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 1.0

    if recall + precision > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0.0

    if task.scoring_method == "detection_only":
        score = recall
    elif task.scoring_method == "detection_and_precision":
        precision_penalty = min(1.0, task.max_expected_findings / model_findings_count) if model_findings_count > 0 else 1.0
        score = recall * precision_penalty
    elif task.scoring_method == "f1":
        score = f1
    else:
        score = recall

    return TaskScore(
        task_id=task.id,
        model=model,
        scoring_method=task.scoring_method,
        recall=recall,
        precision=precision,
        f1=f1,
        score=score,
        gaps_detected=gaps_detected,
        gaps_total=gaps_total,
        red_herrings_flagged=red_herrings_flagged,
        red_herrings_total=red_herrings_total,
        model_findings_count=model_findings_count,
        finding_results=finding_results,
    )
