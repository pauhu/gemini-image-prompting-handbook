#!/usr/bin/env python3
"""
Validate a JSON image prompt against the Pauhu schema and lint for weak wording.

Usage:
  python tools/validate_prompt.py examples/photoreal-product.json
  python tools/validate_prompt.py path/to/prompt1.json path/to/prompt2.json
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Set

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("Missing dependency jsonschema. Install with: pip install jsonschema\n")
    sys.exit(2)

# Get the absolute path to the schema relative to this script's location
SCHEMA_PATH = Path(__file__).parent.parent / "schema" / "prompt.schema.json"

DISCOURAGED: Dict[str, str] = {
    r"\b4k\b": "Prefer explicit resolution object (technical.resolution.target = '4k') rather than free text.",
    r"\bHDR\b": "Prefer 'technical.rendering.color_depth = high' or describe range precisely.",
    r"\bAI[- ]art\b": "Avoid meta terms; describe visual traits instead.",
}

FORBIDDEN_QUALITY: Set[str] = {"digital artifacts", "unrealistic proportions", "oversaturated colors", "blurry", "overprocessed"}

def load_schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def stringify_for_lint(obj: Any) -> str:
    try:
        return json.dumps(obj, ensure_ascii=False).lower()
    except Exception:
        return ""

def lint(content: Dict[str, Any]) -> List[str]:
    warnings = []
    text = stringify_for_lint(content)
    for pat, msg in DISCOURAGED.items():
        if re.search(pat, text, flags=re.IGNORECASE):
            warnings.append(f"lint: discouraged token '{pat}': {msg}")
    avoid = set(map(str.lower, content.get("quality_keywords", {}).get("avoid", [])))
    bad = avoid & set(map(str.lower, FORBIDDEN_QUALITY))
    if bad:
        warnings.append(f"lint: 'quality_keywords.avoid' contains redundant items already implied by schema best-practices: {sorted(bad)}")
    objs = content.get("core", {}).get("objects", [])
    if isinstance(objs, list) and len(objs) < 1:
        warnings.append("lint: consider listing distinct 'core.objects' for better visual control.")
    return warnings

def main(paths: List[str]) -> None:
    schema = load_schema()
    validator = Draft202012Validator(schema)
    overall_rc = 0
    for p in paths:
        path = Path(p)
        try:
            data = read_json(path)
        except Exception as e:
            print(f"[{path}] cannot read JSON: {e}")
            overall_rc = 1
            continue
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        warns = lint(data)
        if errors:
            print(f"[{path}] schema errors:")
            for e in errors:
                loc = list(e.path)
                where = ".".join(map(str, loc)) if loc else "(root)"
                print(f"   - {where}: {e.message}")
            overall_rc = 1
        else:
            print(f"[{path}] schema valid")
        if warns:
            print(f"[{path}] lint warnings:")
            for w in warns:
                print(f"   - {w}")
    sys.exit(overall_rc)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
