# Gemini Image Prompting Handbook (JSON-first)

[![Validate Prompts](https://github.com/pauhu/gemini-image-prompting-handbook/actions/workflows/validate.yml/badge.svg)](https://github.com/pauhu/gemini-image-prompting-handbook/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pull Requests Welcome](https://img.shields.io/badge/Pull%20Requests-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Developer Tool** for structured AI image generation with Google Gemini.

This repo provides a JSON schema validation framework that brings software engineering best practices to prompt engineering. Transform ad-hoc image generation into reproducible, version-controlled workflows.

> **Who this is for:** Software engineers, ML engineers, and technical teams building image generation features into production applications.

## What it does
- Validates prompts against a comprehensive schema  
- Ensures consistent, high-quality outputs  
- Makes prompts shareable and version-controllable  
- Integrates easily with CI/CD pipelines  

**Open Source Project** — We welcome contributions from the community!

---

## What’s inside

- `schema/prompt.schema.json` — opinionated JSON schema for image prompts (core/style/technical/materials/environment/composition/quality)
- `tools/validate_prompt.py` — lightweight validator for your prompt JSONs
- `examples/` — minimal JSON prompt examples
- `cookbook/` — step-by-step recipes (Gemini API calls in Python/JS mapped to the schema)
- `refs/` — canonical links and notes to official docs
- `CHANGELOG.md` — versioned changes

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

- **Precision:** isolate visual dimensions into named sections  
- **Reusability:** prompts become shareable objects (lintable, versionable)  
- **Control:** consistent wording, explicit tradeoffs, fewer surprises  

---

## Roadmap

1. Add more examples and cookbook recipes with Gemini calls (Python/JS)  
2. Extend linter rules  
3. Optional Node validator and pre-commit hooks  

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

**What it does:**
1. Sets up a Python virtual environment  
2. Installs dependencies (`jsonschema`, `pillow`, `google-genai`, `jq`)  
3. Validates the schema and all examples  
4. Runs the Python cookbook sample  
5. Runs the Node.js cookbook sample (if Node and `GEMINI_API_KEY` are available)  
6. Simulates the GitHub Actions CI check  
7. Runs basic repo hygiene checks  

---

## Contributing

We welcome contributions from the community! Please follow these rules to keep the project consistent.

### Scope of contributions
- **Examples:** new or improved prompt JSONs under `examples/` that pass validation  
- **Cookbook samples:** small, runnable Python or Node snippets under `cookbook/`  
- **Validator/tooling:** fixes or small features for `tools/validate_prompt.py`, CI, or docs  
- **Schema changes:** open an issue first. Describe the need, compatibility impact, and examples you'll provide. Wait for maintainer approval before opening a PR.  

### Ground rules
- JSON style: 2-space indent, UTF-8, no trailing commas, lowercase enum values  
- File naming: use `kebab-case.json` in `examples/`. Keep names short and descriptive  
- Keep examples minimal: only fields necessary to illustrate the idea  
- Docs: update `examples/README.md` or `cookbook/README.md` when adding new content  

### Local checks

Run all tests locally before pushing a PR:

```bash
./run_tests.sh
```

Please see **[CONTRIBUTING.md](CONTRIBUTING.md)** for details on submitting improvements and bug fixes.

---

## License

MIT — Copyright (c) 2025 Pauhu AI Ltd
