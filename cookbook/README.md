# Cookbook

Minimal working samples showing how to use the JSON prompts with the Gemini API for image generation.

## Python
```bash
pip install -U google-genai pillow
export GEMINI_API_KEY=YOUR_KEY
python cookbook/sample_python.py
```

## Node.js (ESM)
```bash
npm install @google/genai
export GEMINI_API_KEY=YOUR_KEY
node cookbook/sample_node.mjs
```

Both scripts:
- Read `examples/photoreal-product.json`
- Convert the JSON to a minimal text prompt
- Call `gemini-2.5-flash-image-preview` via `generateContent`
- Save `output_image.png` if an image is returned
