"""Results saving and aggregation."""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from dataclasses import asdict
from collections import defaultdict

from .scorer import TaskScore


def save_result(task_dir: str, score: TaskScore, raw_response: str, usage: dict | None = None):
    results_dir = Path(task_dir) / "results"
    results_dir.mkdir(exist_ok=True)

    safe_model = score.model.replace("/", "_")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = results_dir / f"{safe_model}_{ts}.json"

    data = {
        "task_id": score.task_id,
        "model": score.model,
        "timestamp": datetime.now().isoformat(),
        "score": asdict(score),
        "usage": usage or {},
        "raw_response": raw_response,
    }

    with open(result_file, "w") as f:
        json.dump(data, f, indent=2)

    return str(result_file)


def load_all_results(tasks_dir: str) -> list[dict]:
    results = []
    for task_dir in sorted(Path(tasks_dir).iterdir()):
        results_dir = task_dir / "results"
        if not results_dir.exists():
            continue
        for result_file in sorted(results_dir.glob("*.json")):
            with open(result_file) as f:
                data = json.load(f)
                data["_file"] = str(result_file)
                results.append(data)
    return results


def generate_leaderboard(tasks_dir: str) -> str:
    results = load_all_results(tasks_dir)
    if not results:
        return "No results found."

    model_scores = defaultdict(list)
    model_by_difficulty = defaultdict(lambda: defaultdict(list))
    model_by_control = defaultdict(lambda: defaultdict(list))

    for r in results:
        model = r["model"]
        s = r["score"]
        score_val = s["score"]
        model_scores[model].append(score_val)

        task_id = r["task_id"]
        parts = task_id.split("-")
        if len(parts) >= 3:
            control = parts[0].upper()
            try:
                difficulty = int(parts[1])
            except ValueError:
                difficulty = 0
            model_by_difficulty[model][difficulty].append(score_val)
            model_by_control[model][control].append(score_val)

    lines = []
    lines.append("# TrustBench Leaderboard\n")

    lines.append("## Overall Scores\n")
    lines.append("| Rank | Model | Avg Score | Tasks |")
    lines.append("|------|-------|-----------|-------|")

    ranked = sorted(model_scores.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)
    for rank, (model, scores) in enumerate(ranked, 1):
        avg = sum(scores) / len(scores)
        lines.append(f"| {rank} | {model} | {avg:.1%} | {len(scores)} |")

    lines.append("\n## Scores by Difficulty\n")
    lines.append("| Model | D1 | D2 | D3 | D4 | D5 |")
    lines.append("|-------|----|----|----|----|----|")
    for model, _ in ranked:
        row = f"| {model} |"
        for d in range(1, 6):
            scores = model_by_difficulty[model].get(d, [])
            if scores:
                avg = sum(scores) / len(scores)
                row += f" {avg:.0%} |"
            else:
                row += " — |"
        lines.append(row)

    lines.append("\n## Scores by Control\n")
    all_controls = sorted(set(c for m in model_by_control.values() for c in m.keys()))
    header = "| Model | " + " | ".join(all_controls) + " |"
    sep = "|-------" + "|-----" * len(all_controls) + "|"
    lines.append(header)
    lines.append(sep)
    for model, _ in ranked:
        row = f"| {model} |"
        for c in all_controls:
            scores = model_by_control[model].get(c, [])
            if scores:
                avg = sum(scores) / len(scores)
                row += f" {avg:.0%} |"
            else:
                row += " — |"
        lines.append(row)

    return "\n".join(lines)
