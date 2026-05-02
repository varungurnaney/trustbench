"""Model runner — dispatches to Anthropic, OpenAI, or Google Gemini APIs."""

from __future__ import annotations

import base64
import mimetypes
import time
import random
from pathlib import Path


OPENAI_PREFIXES = ("gpt-", "o1", "o3", "o4")
GEMINI_PREFIXES = ("gemini-",)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def is_openai_model(model: str) -> bool:
    return any(model.startswith(p) for p in OPENAI_PREFIXES)


def is_gemini_model(model: str) -> bool:
    return any(model.startswith(p) for p in GEMINI_PREFIXES)


def _is_image(path: str) -> bool:
    return Path(path).suffix.lower() in IMAGE_EXTENSIONS


def _encode_image(path: str) -> tuple[str, str]:
    media_type = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode("utf-8")
    return data, media_type


def call_anthropic(model: str, content: list, max_tokens: int = 8192) -> tuple[str, dict]:
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": content}],
    )
    usage = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    return response.content[0].text, usage


def call_openai(model: str, content: list, max_tokens: int = 8192) -> tuple[str, dict]:
    import openai
    client = openai.OpenAI()

    oai_content = []
    for block in content:
        if block["type"] == "text":
            oai_content.append({"type": "text", "text": block["text"]})
        elif block["type"] == "image":
            oai_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{block['source']['media_type']};base64,{block['source']['data']}",
                },
            })

    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=max_tokens,
        messages=[{"role": "user", "content": oai_content}],
    )
    usage = {}
    if response.usage:
        usage = {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
        }
    return response.choices[0].message.content, usage


def call_gemini(model: str, content: list, max_tokens: int = 8192) -> tuple[str, dict]:
    from google import genai
    from google.genai import types
    import os

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    parts = []
    for block in content:
        if block["type"] == "text":
            parts.append(types.Part.from_text(text=block["text"]))
        elif block["type"] == "image":
            parts.append(types.Part.from_bytes(
                data=base64.standard_b64decode(block["source"]["data"]),
                mime_type=block["source"]["media_type"],
            ))

    response = client.models.generate_content(
        model=model,
        contents=[types.Content(role="user", parts=parts)],
        config=types.GenerateContentConfig(max_output_tokens=max_tokens),
    )

    usage = {}
    if response.usage_metadata:
        usage = {
            "input_tokens": response.usage_metadata.prompt_token_count,
            "output_tokens": response.usage_metadata.candidates_token_count,
        }
    return response.text, usage


def call_model(model: str, content: list, max_retries: int = 3) -> tuple[str, dict]:
    if is_gemini_model(model):
        caller = call_gemini
    elif is_openai_model(model):
        caller = call_openai
    else:
        caller = call_anthropic

    for attempt in range(max_retries):
        try:
            return caller(model, content)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait = (2 ** attempt) + random.random()
            print(f"  Retry {attempt + 1}/{max_retries} after error: {e}")
            time.sleep(wait)


def build_message_content(task) -> list:
    all_docs = []

    for i, ef in enumerate(task.evidence_files):
        all_docs.append({
            "description": ef["description"],
            "content": task.evidence_content[i],
            "path": ef["path"],
            "type": ef.get("type", "policy"),
        })

    for i, nf in enumerate(task.noise_files):
        all_docs.append({
            "description": nf["description"],
            "content": task.noise_content[i],
            "path": nf["path"],
            "type": nf.get("type", "policy"),
        })

    seed = hash(task.id) % (2**32)
    rng = random.Random(seed)
    rng.shuffle(all_docs)

    content_blocks = []

    prompt_text = f"""You are a compliance auditor performing a readiness assessment.

## Control Under Review

**{task.control}**: {task.control_description}

## Evidence Provided

The following documents have been provided for review:

"""
    content_blocks.append({"type": "text", "text": prompt_text})

    for doc in all_docs:
        full_path = str(Path(task.task_dir) / doc["path"])

        if _is_image(full_path):
            content_blocks.append({
                "type": "text",
                "text": f"\n### {doc['description']}\n\n[Screenshot: {Path(doc['path']).name}]\n",
            })
            data, media_type = _encode_image(full_path)
            content_blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": data,
                },
            })
        else:
            content_blocks.append({
                "type": "text",
                "text": f"\n### {doc['description']}\n\n{doc['content']}\n\n---\n",
            })

    instructions = f"""
## Instructions

{task.prompt}

For each finding, provide:
1. A short title
2. Which section of the document it relates to
3. Why it's a gap (what's missing or insufficient)
4. Severity (Critical / High / Medium / Low)
"""
    content_blocks.append({"type": "text", "text": instructions})

    return content_blocks
