/**
 * Minimal example: read a JSON prompt and call the Gemini API for image generation.
 *
 * Setup:
 *   npm install @google/genai
 *   (optional for saving): uses built-in fs
 *
 * Environment:
 *   export GEMINI_API_KEY=YOUR_KEY
 *
 * Docs:
 *   https://ai.google.dev/gemini-api/docs/image-generation
 *   https://ai.google.dev/gemini-api/docs/quickstart
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { GoogleGenAI } from "@google/genai";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load JSON prompt
const promptPath = path.join(__dirname, "..", "examples", "photoreal-product.json");
if (!fs.existsSync(promptPath)) {
  console.error(`Error: Example file not found at ${promptPath}`);
  process.exit(1);
}

let promptJson;
try {
  promptJson = JSON.parse(fs.readFileSync(promptPath, "utf-8"));
} catch (error) {
  console.error(`Error: Invalid JSON in ${promptPath}: ${error.message}`);
  process.exit(1);
}

// Build a simple text prompt from the JSON
const promptText = `Subject: ${promptJson.core.subject}\nStyle: ${promptJson.style.primary_style}`;
console.log("Prompt sent to Gemini:\n", promptText);

// Check for API key
if (!process.env.GEMINI_API_KEY) {
  console.error("Error: GEMINI_API_KEY environment variable not set");
  console.error("Set it with: export GEMINI_API_KEY=YOUR_KEY");
  process.exit(1);
}

// Initialize client (reads GEMINI_API_KEY from env by default)
let ai;
try {
  ai = new GoogleGenAI({});
} catch (error) {
  console.error(`Error initializing Gemini client: ${error.message}`);
  process.exit(1);
}

// Generate image (Gemini 2.5 Flash Image Preview)
let response;
try {
  response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image-preview",
    contents: promptText,
  });
} catch (error) {
  console.error(`Error generating image: ${error.message}`);
  process.exit(1);
}

// Save first returned image (if any)
try {
  if (response.candidates && response.candidates.length > 0) {
    let foundImage = false;
    for (const part of response.candidates[0].content.parts) {
      if (part.inlineData) {
        const imageData = part.inlineData.data;
        const buffer = Buffer.from(imageData, "base64");
        const outputPath = path.join(process.cwd(), "output_image.png");
        fs.writeFileSync(outputPath, buffer);
        console.log(`Saved ${outputPath}`);
        foundImage = true;
        break;
      }
    }
    if (!foundImage) {
      console.log("No image data returned in first candidate.");
    }
  } else {
    console.log("No candidates returned in response.");
  }
} catch (error) {
  console.error(`Error processing response: ${error.message}`);
  process.exit(1);
}
