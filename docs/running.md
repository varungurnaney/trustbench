# Evaluation Guide

## Prerequisites

```bash
git clone https://github.com/your-repo/trustbench.git
cd trustbench
pip install -r requirements.txt
```

Set your API key(s):

```bash
# For Anthropic models (claude-*)
export ANTHROPIC_API_KEY=sk-ant-...

# For OpenAI models (gpt-*, o1, o3, o4)
export OPENAI_API_KEY=sk-...

# For Google Gemini models (gemini-*)
export GEMINI_API_KEY=AIza...
```

## CLI Commands

### Run a single task

```bash
python3 -m trustbench.cli run tasks/cc6.1-3-001 --model claude-sonnet-4-6
```

Options:
- `--quiet` — suppress model response, show only scores
- `--dry-run` — print the prompt without calling the API

Output includes: score, recall, precision, F1, per-finding detection status with matched keywords.

### Run all tasks

```bash
python3 -m trustbench.cli run-all --model claude-sonnet-4-6
```

Filters:
- `--control CC6.1` — run only tasks for a specific control
- `--difficulty 4` — run only D4 tasks
- `--category red_herring` — run only red herring tasks
- `--tasks-dir path/to/tasks` — use a custom tasks directory

### View the leaderboard

```bash
python3 -m trustbench.cli leaderboard
```

Shows:
- Overall scores ranked by model
- Scores broken down by difficulty level (D1-D5)
- Scores broken down by control

### Validate tasks

```bash
python3 -m trustbench.cli validate
```

Validates all `task.json` files against the schema. Run this after creating or modifying tasks.

## Results

Results are saved to `tasks/{task_id}/results/{model}_{timestamp}.json`:

```json
{
  "task_id": "cc6.1-4-001",
  "model": "claude-sonnet-4-6",
  "timestamp": "2026-04-30T18:20:10",
  "score": {
    "score": 0.86,
    "recall": 1.0,
    "precision": 0.75,
    "f1": 0.86,
    "gaps_detected": 3,
    "gaps_total": 3,
    "red_herrings_flagged": 0,
    "red_herrings_total": 1,
    "model_findings_count": 4,
    "finding_results": [...]
  },
  "usage": {
    "input_tokens": 4521,
    "output_tokens": 2847
  },
  "raw_response": "..."
}
```

## Supported Models

Any model available through the Anthropic, OpenAI, or Google Gemini APIs. Tested models:

**Anthropic:** `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`

**OpenAI:** `gpt-5.5`, `gpt-4.1`, `gpt-4o`, `gpt-4o-mini`, `o3`

**Google:** `gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`

The runner auto-detects which API to use based on model name prefix (`claude-*` → Anthropic, `gpt-*/o1/o3/o4` → OpenAI, `gemini-*` → Google).

## Cost Estimates

Per task, approximate (varies with evidence size):

| Model | Provider | Input | Output | Cost/task |
|-------|----------|-------|--------|-----------|
| Claude Sonnet 4.6 | Anthropic | ~4-8K tokens | ~2-4K tokens | ~$0.03-0.06 |
| Claude Opus 4.7 | Anthropic | ~4-8K tokens | ~2-4K tokens | ~$0.10-0.20 |
| GPT-5.5 | OpenAI | ~4-8K tokens | ~2-4K tokens | ~$0.05-0.15 |
| GPT-4o | OpenAI | ~4-8K tokens | ~2-4K tokens | ~$0.02-0.05 |
| GPT-4o-mini | OpenAI | ~4-8K tokens | ~2-4K tokens | ~$0.001-0.003 |
| Gemini 2.5 Flash | Google | ~4-8K tokens | ~2-4K tokens | ~$0.01-0.03 |
| Gemini 2.5 Pro | Google | ~4-8K tokens | ~2-4K tokens | ~$0.05-0.10 |

Full benchmark (64 tasks × 1 model): ~$1-13 depending on model.

D4-D5 tasks with more evidence documents and noise files will be on the higher end.

## Multimodal Evidence

Tasks with screenshot evidence (`.png`, `.jpg`, `.jpeg`, `.webp`) are automatically sent as base64-encoded images via the model's vision API. The CLI indicates when a task includes screenshots:

```
Evidence includes screenshots (multimodal)
```

Models without vision capabilities will not be able to process screenshot evidence. The scorer still evaluates keyword matches in the text response — it does not attempt to evaluate what the model "saw" in the image beyond what it wrote about it.
