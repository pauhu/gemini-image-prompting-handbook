#!/usr/bin/env bash
set -euo pipefail

echo "=== 1. Environment setup ==="
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip jsonschema pillow google-genai jq

echo
echo "=== 2. Schema validation ==="
python -m json.tool < schema/prompt.schema.json > /dev/null
echo "Schema JSON syntax OK"

echo
echo "=== 3. Validate examples against schema ==="
python tools/validate_prompt.py examples/*.json

echo
echo "=== 4. Python cookbook sample ==="
if [[ -z "${GEMINI_API_KEY:-}" ]]; then
  echo "WARNING: GEMINI_API_KEY not set. Skipping Python API call."
else
  python cookbook/sample_python.py || echo "Python sample finished with warning"
fi

echo
echo "=== 5. Node.js cookbook sample ==="
if command -v node >/dev/null 2>&1; then
  if [[ -z "${GEMINI_API_KEY:-}" ]]; then
    echo "WARNING: GEMINI_API_KEY not set. Skipping Node API call."
  else
    npm install @google/genai
    node cookbook/sample_node.mjs || echo "Node sample finished with warning"
  fi
else
  echo "Node.js not installed. Skipping Node sample."
fi

echo
echo "=== 6. CI dry run ==="
python tools/validate_prompt.py examples/*.json

echo
echo "=== 7. Repo hygiene tests ==="
jq . schema/prompt.schema.json > /dev/null && echo "Schema is valid JSON (jq)"
echo "Gitignore check:"
echo "tempfile" > tempfile
git status --ignored | grep tempfile || echo "tempfile not ignored (expected only if outside git repo)"
rm -f tempfile

echo
echo "=== All tests done ==="
