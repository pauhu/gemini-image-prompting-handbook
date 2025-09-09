"""
Minimal example: read a JSON prompt and call the Gemini API for image generation.

Setup:
  pip install -U google-genai pillow

Environment:
  export GEMINI_API_KEY=YOUR_KEY

Docs:
  https://ai.google.dev/gemini-api/docs/image-generation
  https://ai.google.dev/gemini-api/docs/quickstart
"""

import json
import sys
import os
from io import BytesIO
from pathlib import Path

from PIL import Image  # for saving image bytes
from google import genai  # Google Gen AI Python SDK

# Load JSON prompt
prompt_path = Path(__file__).parent.parent / "examples" / "photoreal-product.json"
if not prompt_path.exists():
    print(f"Error: Example file not found at {prompt_path}")
    sys.exit(1)

try:
    prompt_json = json.loads(prompt_path.read_text(encoding="utf-8"))
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in {prompt_path}: {e}")
    sys.exit(1)

# Build a simple text prompt from the JSON (keep it minimal)
prompt_lines = [
    f"Subject: {prompt_json['core']['subject']}",
    f"Style: {prompt_json['style']['primary_style']}",
]
prompt_text = "\n".join(prompt_lines)
print("Prompt sent to Gemini:\n", prompt_text)

# Check for API key
if not os.getenv("GEMINI_API_KEY"):
    print("Error: GEMINI_API_KEY environment variable not set")
    print("Set it with: export GEMINI_API_KEY=YOUR_KEY")
    sys.exit(1)

# Initialize client (reads GEMINI_API_KEY from env by default)
try:
    client = genai.Client()
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    sys.exit(1)

# Generate image (Gemini 2.5 Flash Image Preview)
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt_text],
    )
except Exception as e:
    print(f"Error generating image: {e}")
    sys.exit(1)

# Save first returned image (if any)
try:
    if response.candidates:
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                output_path = Path("output_image.png")
                image.save(output_path)
                print(f"Saved {output_path.absolute()}")
                break
        else:
            print("No image data returned in first candidate.")
    else:
        print("No candidates returned in response.")
except Exception as e:
    print(f"Error processing response: {e}")
    sys.exit(1)
