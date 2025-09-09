/**
 * Minimal example: read a JSON prompt, call Gemini API for image generation.
 *
 * Requires:
 *   npm install @google/generative-ai
 *
 * Docs:
 *   https://ai.google.dev/gemini-api/docs/image-generation
 */

import fs from "fs";
import path from "path";
import { GoogleGenerativeAI } from "@google/generative-ai";

// Load JSON prompt
const promptJson = JSON.parse(
  fs.readFileSync(path.join("examples", "photoreal-product.json"), "utf-8")
);

// Initialize Gemini client
const client = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);

// Build prompt string from JSON (simplified)
const promptText = `Subject: ${promptJson.core.subject}\nStyle: ${promptJson.style.primary_style}`;
console.log("Prompt sent to Gemini:\n", promptText);

// Call Gemini for image generation
const model = client.getGenerativeModel({ model: "gemini-1.5-pro" });
const result = await model.generateImages({ prompt: promptText });

// Save first image
if (result.images && result.images.length > 0) {
  const img = result.images[0];
  fs.writeFileSync("output_image.png", img.data, "base64");
  console.log("Saved output_image.png");
}
