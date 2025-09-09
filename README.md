# Gemini Image Prompting Handbook (JSON-first)

[![Validate Prompts](https://github.com/YOUR_USERNAME/gemini-image-prompting-handbook/actions/workflows/validate.yml/badge.svg)](https://github.com/YOUR_USERNAME/gemini-image-prompting-handbook/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Practical, JSON-first patterns for Google Gemini image generation.
This repo turns a field-tested slide framework into a validated JSON schema, working examples, and a tiny CLI validator.

> Who this is for: engineers and prompt authors who want repeatable, high-fidelity image outputs and structured requests.

**Open Source Project** - We welcome contributions from the community!

---

## What's inside

- schema/prompt.schema.json - opinionated JSON schema for image prompts (core/style/technical/materials/environment/composition/quality).
- tools/validate_prompt.py - lightweight validator for your prompt JSONs.
- examples/ - minimal JSON prompt examples.
- cookbook/ - step-by-step recipes (Gemini API calls in Python/JS mapped to the schema).
- refs/ - canonical links and notes to official docs.
- CHANGELOG.md - versioned changes.

---

## Status

- Initial scaffolding
- Schema, validator, and examples included

---

## Install (dev)

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip jsonschema
```

---

## Why JSON-first?

- Precision: isolate visual dimensions into named sections.
- Reusability: prompts become shareable objects (lintable, versionable).
- Control: consistent wording, explicit tradeoffs, fewer surprises.

---

## Roadmap

1. Add more examples and cookbook recipes with Gemini calls (Python/JS).
2. Extend linter rules.
3. Optional Node validator and pre-commit hooks.

---

## References

- Gemini Image Generation: https://ai.google.dev/gemini-api/docs/image-generation
- Gemini API Quickstarts and SDKs: https://ai.google.dev/gemini-api
- Structured responses and schemas: https://ai.google.dev/gemini-api/docs/structured-output

---

## Tests

You can run all validation and cookbook samples in one go with:

```bash
./run_tests.sh
```

What it does:
1. Sets up a Python virtual environment
2. Installs dependencies (jsonschema, pillow, google-genai, jq)
3. Validates the schema and all examples
4. Runs the Python cookbook sample
5. Runs the Node.js cookbook sample (if Node and GEMINI_API_KEY are available)
6. Simulates the GitHub Actions CI check
7. Runs basic repo hygiene checks

---
## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit improvements and bug fixes.

## License

MIT - Copyright (c) 2025 Pauhu AI Ltd
