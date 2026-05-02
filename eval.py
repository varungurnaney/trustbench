#!/usr/bin/env python3
"""TrustBench evaluation harness — v0.2"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime


def load_task(task_dir: str) -> dict:
    task_path = Path(task_dir) / "task.json"
    with open(task_path) as f:
        task = json.load(f)

    evidence_texts = []
    for evidence_file in task["evidence_files"]:
        evidence_path = Path(task_dir) / evidence_file
        with open(evidence_path) as f:
            evidence_texts.append(f.read())

    task["_evidence_content"] = evidence_texts
    return task


def build_prompt(task: dict) -> str:
    evidence = "\n\n---\n\n".join(task["_evidence_content"])
    return f"""You are a SOC 2 auditor performing a readiness assessment.

## Control Under Review

**{task['control']}**: {task['control_description']}

## Evidence Provided

{evidence}

## Instructions

{task['prompt']}

For each finding, provide:
1. A short title
2. Which section of the document it relates to
3. Why it's a gap (what's missing or insufficient)
4. Severity (High / Medium / Low)
"""


def call_anthropic(model: str, prompt: str) -> str:
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def call_openai(model: str, prompt: str) -> str:
    import openai
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


OPENAI_MODELS = {"gpt-4o", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o1", "o3", "o3-mini", "o4-mini"}


def call_model(model: str, prompt: str) -> str:
    if model in OPENAI_MODELS or model.startswith("gpt-") or model.startswith("o1") or model.startswith("o3") or model.startswith("o4"):
        return call_openai(model, prompt)
    else:
        return call_anthropic(model, prompt)


def score_response(response_text: str, task: dict) -> dict:
    results = []
    response_lower = response_text.lower()

    for gap in task["planted_gaps"]:
        keywords = gap["detection_keywords"]
        matched_keywords = [kw for kw in keywords if kw.lower() in response_lower]
        detected = len(matched_keywords) >= 2

        results.append({
            "gap_id": gap["id"],
            "category": gap["category"],
            "severity": gap["severity"],
            "detected": detected,
            "matched_keywords": matched_keywords,
            "total_keywords": len(keywords),
        })

    detected_count = sum(1 for r in results if r["detected"])
    total_count = len(results)

    return {
        "score": detected_count / total_count if total_count > 0 else 0,
        "detected": detected_count,
        "total": total_count,
        "gaps": results,
    }


def run_eval(task_dir: str, model: str = "claude-sonnet-4-6", quiet: bool = False):
    task = load_task(task_dir)
    prompt = build_prompt(task)

    print(f"Task: {task['id']}")
    print(f"Control: {task['control']}")
    print(f"Difficulty: {task['difficulty']}")
    print(f"Model: {model}")
    print(f"Planted gaps: {len(task['planted_gaps'])}")
    print("=" * 60)
    print("Sending to model...\n")

    response_text = call_model(model, prompt)

    if not quiet:
        print("MODEL RESPONSE:")
        print("-" * 60)
        print(response_text)
        print("-" * 60)

    scoring = score_response(response_text, task)

    print(f"\nSCORE: {scoring['detected']}/{scoring['total']} gaps detected ({scoring['score']:.0%})")
    print()
    for gap_result in scoring["gaps"]:
        status = "DETECTED" if gap_result["detected"] else "MISSED"
        print(f"  [{status}] {gap_result['gap_id']} ({gap_result['category']}) — severity: {gap_result['severity']}")
        print(f"           matched: {gap_result['matched_keywords']}")

    results_dir = Path(task_dir) / "results"
    results_dir.mkdir(exist_ok=True)
    safe_model = model.replace("/", "_")
    result_file = results_dir / f"{safe_model}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    result_data = {
        "task_id": task["id"],
        "model": model,
        "timestamp": datetime.now().isoformat(),
        "scoring": scoring,
        "raw_response": response_text,
    }
    with open(result_file, "w") as f:
        json.dump(result_data, f, indent=2)

    print(f"\nResults saved to: {result_file}")
    return scoring


if __name__ == "__main__":
    task_dir = sys.argv[1] if len(sys.argv) > 1 else "tasks/cc6.1-001"
    model = sys.argv[2] if len(sys.argv) > 2 else "claude-sonnet-4-6"
    quiet = "--quiet" in sys.argv
    run_eval(task_dir, model, quiet)
