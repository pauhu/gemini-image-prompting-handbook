# Examples

This folder shows minimal, working prompt JSONs mapped to the schema.

Validate locally with:
```bash
python tools/validate_prompt.py examples/*.json
```

Mapping from slide to JSON
- Core -> core.subject, core.scene, core.objects, core.constraints
- Style -> style.primary_style, style.render_quality, style.lighting
- Technical -> technical.camera, technical.resolution
- Materials -> materials.*
- Environment -> environment.*
- Composition -> composition.*
- Quality Keywords -> quality_keywords.include + avoid

Current files
- photoreal-product.json - stainless-steel travel mug
- cinematic-portrait.json - marine biologist portrait
- documentary-street.json - real-world street reportage
- studio-fashion.json - fashion editorial shot
- illustrative-scene.json - illustrative (non-photo) control
