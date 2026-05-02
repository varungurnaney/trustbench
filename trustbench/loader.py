"""Task loading and discovery."""

from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Finding:
    id: str
    type: str  # "gap" or "red_herring"
    severity: str
    title: str
    description: str
    evidence_sources: list[str]
    expected_reasoning: str
    required_keywords: list[str]
    minimum_keyword_matches: int
    exclusion_keywords: list[str] = field(default_factory=list)


@dataclass
class Task:
    id: str
    version: str
    framework: str
    control: str
    control_description: str
    difficulty: int
    category: str
    evidence_files: list[dict]
    noise_files: list[dict]
    prompt: str
    findings: list[Finding]
    scoring_method: str
    max_expected_findings: int
    metadata: dict
    evidence_content: list[str] = field(default_factory=list)
    noise_content: list[str] = field(default_factory=list)
    task_dir: str = ""


def load_task(task_dir: str) -> Task:
    task_path = Path(task_dir) / "task.json"
    with open(task_path) as f:
        raw = json.load(f)

    findings = []
    for f_raw in raw["findings"]:
        dc = f_raw["detection_criteria"]
        findings.append(Finding(
            id=f_raw["id"],
            type=f_raw["type"],
            severity=f_raw["severity"],
            title=f_raw["title"],
            description=f_raw["description"],
            evidence_sources=f_raw["evidence_sources"],
            expected_reasoning=f_raw["expected_reasoning"],
            required_keywords=dc["required_keywords"],
            minimum_keyword_matches=dc["minimum_keyword_matches"],
            exclusion_keywords=dc.get("exclusion_keywords", []),
        ))

    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

    evidence_content = []
    for ef in raw["evidence_files"]:
        p = Path(task_dir) / ef["path"]
        if p.suffix.lower() in image_extensions:
            evidence_content.append(f"[Screenshot: {p.name}]")
        else:
            with open(p) as f:
                evidence_content.append(f.read())

    noise_content = []
    for nf in raw.get("noise_files", []):
        p = Path(task_dir) / nf["path"]
        if p.suffix.lower() in image_extensions:
            noise_content.append(f"[Screenshot: {p.name}]")
        else:
            with open(p) as f:
                noise_content.append(f.read())

    scoring = raw.get("scoring", {})

    return Task(
        id=raw["id"],
        version=raw["version"],
        framework=raw["framework"],
        control=raw["control"],
        control_description=raw["control_description"],
        difficulty=raw["difficulty"],
        category=raw["category"],
        evidence_files=raw["evidence_files"],
        noise_files=raw.get("noise_files", []),
        prompt=raw["prompt"],
        findings=findings,
        scoring_method=scoring.get("method", "detection_only"),
        max_expected_findings=scoring.get("max_expected_findings", 20),
        metadata=raw["metadata"],
        evidence_content=evidence_content,
        noise_content=noise_content,
        task_dir=str(task_dir),
    )


def load_all_tasks(
    tasks_dir: str,
    control: str | None = None,
    difficulty: int | None = None,
    category: str | None = None,
) -> list[Task]:
    tasks = []
    tasks_path = Path(tasks_dir)
    for task_dir in sorted(tasks_path.iterdir()):
        if not task_dir.is_dir():
            continue
        task_json = task_dir / "task.json"
        if not task_json.exists():
            continue
        task = load_task(str(task_dir))
        if control and task.control != control:
            continue
        if difficulty is not None and task.difficulty != difficulty:
            continue
        if category and task.category != category:
            continue
        tasks.append(task)
    return tasks
