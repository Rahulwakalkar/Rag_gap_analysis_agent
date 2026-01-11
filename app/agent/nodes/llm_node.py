import json
import re
from app.services.llm import GroqLLM

llm = GroqLLM()

JSON_PATTERN = re.compile(r"\{.*\}|\[.*\]", re.DOTALL)

def extract_json(text: str):
    """
    Safely extract JSON from LLM output.
    """
    match = JSON_PATTERN.search(text)
    if not match:
        raise ValueError(f"No JSON found in LLM output:\n{text}")
    return json.loads(match.group())

def requirement_extraction_node(state):
    prompt = f"""
You are a compliance analyst.

TASK:
Extract regulatory requirements from the document below.

RULES (MANDATORY):
- Output ONLY valid JSON
- Do NOT add explanations
- Do NOT add markdown
- Do NOT add text outside JSON
- Return a JSON array ONLY

SCHEMA:
[
  {{
    "section": "string",
    "text": "string",
    "requirement_type": "mandatory | recommended"
  }}
]

DOCUMENT:
{state["regulatory_text"]}
"""

    raw_output = llm.invoke(prompt)

    try:
        state["extracted_requirements"] = extract_json(raw_output)
    except Exception as e:
        raise RuntimeError(
            f"Requirement extraction failed.\nLLM output:\n{raw_output}"
        ) from e

    return state