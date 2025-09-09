---
name: New example submission
about: Submit a new example prompt
title: '[EXAMPLE] '
labels: example
assignees: ''

---

**Example name**
Brief name for your example (e.g., "abstract-art", "portrait-lighting")

**Use case**
What type of image generation does this example demonstrate?

**Example JSON**
```json
{
  "core": {
    "subject": "...",
    "action": "...",
    "objects": []
  },
  "style": {
    "primary_style": "..."
  }
  // ... rest of your example
}
```

**Why this example is valuable**
Explain how this example adds to the existing collection.

**Validation**
- [ ] I have run `python tools/validate_prompt.py` on this example
- [ ] The example passes all validation checks
- [ ] I have tested generating images with this prompt