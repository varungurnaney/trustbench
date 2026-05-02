"""TrustBench CLI."""

import argparse
import sys
from pathlib import Path

from .loader import load_task, load_all_tasks
from .runner import build_message_content, call_model
from .scorer import score_response
from .reporter import save_result, generate_leaderboard


TASKS_DIR = str(Path(__file__).parent.parent / "tasks")


def cmd_run(args):
    task = load_task(args.task)
    content = build_message_content(task)
    has_images = any(b.get("type") == "image" for b in content)

    print(f"Task: {task.id}")
    print(f"Control: {task.control}")
    print(f"Difficulty: {task.difficulty}")
    print(f"Category: {task.category}")
    print(f"Model: {args.model}")
    print(f"Findings: {len(task.findings)} ({sum(1 for f in task.findings if f.type == 'gap')} gaps, {sum(1 for f in task.findings if f.type == 'red_herring')} red herrings)")
    print(f"Scoring: {task.scoring_method}")
    if has_images:
        print(f"Evidence includes screenshots (multimodal)")
    print("=" * 60)

    if args.dry_run:
        print("\n[DRY RUN] Message content blocks:\n")
        for b in content:
            if b["type"] == "text":
                print(b["text"])
            else:
                print(f"[IMAGE: {b['source']['media_type']}]")
        return

    print("Sending to model...\n")
    response, usage = call_model(args.model, content)

    if not args.quiet:
        print("MODEL RESPONSE:")
        print("-" * 60)
        print(response)
        print("-" * 60)

    score = score_response(task, response, args.model)

    print(f"\nSCORE: {score.score:.0%}  (recall={score.recall:.0%}, precision={score.precision:.0%}, f1={score.f1:.0%})")
    print(f"Gaps: {score.gaps_detected}/{score.gaps_total} detected")
    if score.red_herrings_total > 0:
        print(f"Red herrings: {score.red_herrings_flagged}/{score.red_herrings_total} incorrectly flagged")
    print(f"Model reported ~{score.model_findings_count} findings")
    print()

    for fr in score.finding_results:
        if fr.finding_type == "gap":
            status = "DETECTED" if fr.detected else "MISSED"
        else:
            if fr.detected and not fr.correctly_dismissed:
                status = "FALSE POSITIVE"
            elif fr.correctly_dismissed:
                status = "CORRECTLY DISMISSED"
            else:
                status = "NOT MENTIONED"
        print(f"  [{status}] {fr.finding_id} ({fr.finding_type}) — {fr.severity}")
        print(f"           matched: {fr.matched_keywords}")

    result_path = save_result(args.task, score, response, usage)
    print(f"\nResults saved to: {result_path}")


def cmd_run_all(args):
    tasks = load_all_tasks(
        args.tasks_dir or TASKS_DIR,
        control=args.control,
        difficulty=args.difficulty,
        category=args.category,
    )

    if not tasks:
        print("No tasks found matching filters.")
        return

    print(f"Running {len(tasks)} tasks with model {args.model}\n")

    for i, task in enumerate(tasks, 1):
        print(f"[{i}/{len(tasks)}] {task.id} (D{task.difficulty}, {task.category})")
        content = build_message_content(task)

        try:
            response, usage = call_model(args.model, content)
            score = score_response(task, response, args.model)
            save_result(task.task_dir, score, response, usage)
            print(f"  Score: {score.score:.0%} ({score.gaps_detected}/{score.gaps_total} gaps)")
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\nDone. Run `trustbench leaderboard` to see results.")


def cmd_leaderboard(args):
    tasks_dir = args.tasks_dir or TASKS_DIR
    print(generate_leaderboard(tasks_dir))


def cmd_validate(args):
    try:
        import jsonschema
    except ImportError:
        print("Install jsonschema: pip install jsonschema")
        sys.exit(1)

    schema_path = Path(__file__).parent.parent / "schema" / "trustbench-schema.json"
    import json
    with open(schema_path) as f:
        schema = json.load(f)

    tasks_dir = Path(args.tasks_dir or TASKS_DIR)
    errors = 0
    total = 0

    for task_dir in sorted(tasks_dir.iterdir()):
        task_json = task_dir / "task.json"
        if not task_json.exists():
            continue
        total += 1
        with open(task_json) as f:
            task_data = json.load(f)
        try:
            jsonschema.validate(task_data, schema)
            print(f"  ✓ {task_dir.name}")
        except jsonschema.ValidationError as e:
            print(f"  ✗ {task_dir.name}: {e.message}")
            errors += 1

    print(f"\n{total - errors}/{total} tasks valid")
    if errors:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(prog="trustbench", description="TrustBench — SOC 2 compliance benchmark for LLMs")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run a single task")
    run_parser.add_argument("task", help="Path to task directory")
    run_parser.add_argument("--model", default="claude-sonnet-4-6", help="Model to evaluate")
    run_parser.add_argument("--quiet", action="store_true", help="Suppress model response output")
    run_parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")

    run_all_parser = subparsers.add_parser("run-all", help="Run all tasks")
    run_all_parser.add_argument("--model", default="claude-sonnet-4-6", help="Model to evaluate")
    run_all_parser.add_argument("--tasks-dir", help="Tasks directory (default: built-in)")
    run_all_parser.add_argument("--control", help="Filter by control (e.g., CC6.1)")
    run_all_parser.add_argument("--difficulty", type=int, help="Filter by difficulty (1-5)")
    run_all_parser.add_argument("--category", help="Filter by category")

    lb_parser = subparsers.add_parser("leaderboard", help="Show leaderboard")
    lb_parser.add_argument("--tasks-dir", help="Tasks directory")

    val_parser = subparsers.add_parser("validate", help="Validate all task schemas")
    val_parser.add_argument("--tasks-dir", help="Tasks directory")

    args = parser.parse_args()

    if args.command == "run":
        cmd_run(args)
    elif args.command == "run-all":
        cmd_run_all(args)
    elif args.command == "leaderboard":
        cmd_leaderboard(args)
    elif args.command == "validate":
        cmd_validate(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
