We are going through lesson-01-model-selection from Udacity in our vibecoding folder.

Here we will use a model for processing alerts for a weather service app.

The demo has a **file structure** of:

- src/
  - helpers.ts
  - index.ts
  - models.ts
  - sample_alerts.ts
- package.json

Models.ts includes the different models we can use for our applicaiton.

Sample_alerts.ts includes some sample alerts; for each complexity we will use different models.

```typescript
/**
 * Claude Model Selection
 *
 * Tas: A weather service processes thousands of alerts daily.
 * Simple updates need fast processing; severe warnings need deeper analysis.
 *
 * This demo shows how to pick the right model for different tasks.
 */

import Anthropic from "@anthropic-ai/sdk";
import { MODELS, ModelKey } from "./models.js"; // These are the models and their respective ids we pulled from the anthropic docs
import { ALERTS } from "./sample-alerts.js"; // These are our sample alerts
import {
  calculateCost,
  logStats,
  displayComparison,
  ensureParsedResponse,
} from "./helpers.js"; // Helper stats for model comparison

import dotenv from "dotenv";
dotenv.config(); // Reads our API keys using the dotenv node package

/**Initialize the Anthropic client */

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// -----------------------------------------------------------------------------
// Helper: Call Claude and return the response with usage stats
// -----------------------------------------------------------------------------

async function callClaude(
  modelKey: ModelKey,
  system: string,
  userMessage: string,
) {
  const model = MODELS[modelKey];
  // start timer
  const start = Date.now();

  const rawResponse = await client.messages.create({
    model: model.id,
    max_tokens: 4096,
    system,
    messages: [{ role: "user", content: userMessage }],
  }); // The model's actual response

  // Ensure response is parsed (handles Vocareum proxy environment)
  const response = ensureParsedResponse(rawResponse as any);

  // stop timer
  const ms = Date.now() - start;
  // get usage stats
  const inputTokens = response.usage.input_tokens;
  const outputTokens = response.usage.output_tokens;
  // calculate cost
  const cost = calculateCost(inputTokens, outputTokens, model);

  const text =
    response.content[0].type === "text" ? response.content[0].text : "";

  return { text, inputTokens, outputTokens, ms, cost };
}

// -----------------------------------------------------------------------------
// Step 1: Haiku - Fast classification for simple alerts
// -----------------------------------------------------------------------------

async function testHaiku() {
  console.log(`\n--- STEP 1: Haiku for Simple Classification ---\n`);

  const system = `Classify weather severity as: LOW, MEDIUM, HIGH, or CRITICAL.`;

  const result = await callClaude("haiku", system, ALERTS.simple);

  console.log(`Result: ${result.text}`);

  logStats(result);

  console.log(`\n💡 Haiku is perfect for simple tasks - fast and cheap!`);
}

// -----------------------------------------------------------------------------
// Step 2: Sonnet - Balanced analysis for moderate alerts
// -----------------------------------------------------------------------------

async function testSonnet() {
  console.log("\n--- STEP 2: Sonnet for Detailed Analysis ---\n");

  const system = `Analyze the weather alert. Extract:
                  1. Severity level
                  2. Hazards listed
                  3. Key measurements
                  4. Recommended actions
                  Be concise.`;

  const result = await callClaude("sonnet", system, ALERTS.moderate);

  console.log("\nResult:\n", result.text);

  logStats(result);

  console.log("\n💡 Sonnet balances quality and cost - great for most tasks!");
}

// -----------------------------------------------------------------------------
// Step 3: Opus - Complex reasoning for multi-hazard events
// -----------------------------------------------------------------------------

async function testOpus() {
  console.log("\n--- STEP 3: Opus for Complex Reasoning ---\n");

  const system = `You are a senior meteorologist. Provide:
                  1. Event summary
                  2. Phase-by-phase timeline
                  3. Risk assessment (infrastructure, safety)
                  4. Preparedness recommendations
                  Think through each element carefully.`;

  const result = await callClaude("opus", system, ALERTS.complex);

  console.log("\nResult:\n", result.text);

  logStats(result);

  console.log("\n💡 Opus excels at complex, multi-factor reasoning!");
}

// -----------------------------------------------------------------------------
// Step 4: Compare all models on the same task
// -----------------------------------------------------------------------------

async function testCompare() {
  console.log("\n--- STEP 4: Model Comparison ---\n");

  const system = `Analyze the alert. Provide:
                  1. Severity (low/medium/high/critical)
                  2. Main hazard
                  3. One recommended action`;

  const results = [];
  for (const key of ["haiku", "sonnet", "opus"] as ModelKey[]) {
    const r = await callClaude(key, system, ALERTS.moderate);
    results.push({ model: MODELS[key].name, ...r });
  }

  displayComparison(results);

  console.log("\n💡 Pick the right model for the job!");
}

// -----------------------------------------------------------------------------
// Main
// -----------------------------------------------------------------------------

async function main() {
  console.log("=".repeat(60));
  console.log("  DEMO: Claude Model Selection");
  console.log("  Scenario: Weather Notification Service");
  console.log("=".repeat(60));

  await testHaiku();
  await testSonnet();
  await testOpus();
  await testCompare();
}

main().catch(console.error);
```
