AI models that systems put to work in productions -- the loops, the tools, the context strategies, the configuration are what turns this model into a reliable product. We call this **harness engineering**

Introduction:

I have installed claude and put the API key in my env. I was able to ask claude about the udacity repo I am learning on through the interactive terminal, and also programatically with lesson-00. Very cool stuff!

New Terms:

- Vocareum: Online VSCode emulator with Claude installed
- Claude Code: LLM
- Claude Agent SDK: An extracted library ersion of the agent harness that powers Claude Code's LLM and allows developers to embed autonomous agent loops directly into applications.

**Claude 4.5 Model Family:**

Choosing the right model is very important. Without this your application could be too slow, too expensive or not smart enough. We need to balance the speed, intelligence and cost.

**Haiku:**

- The sprinter
- The fastest and most cost effective model
- Suitable for applications that require near-instant responses or handle high volume of requests affordably
- Ex: real-time content moderation, quick customer service chat, categorizing user input, etc

**Sonnet:**

- The workhorse
- Provides a strong balance of intelligence and speed
- Suitable for wide range of workloads and recommended as a starting point
- Ex: summarizing long documents, drafting professional communications, assisting with coding tasks, etc

**Opus:**

- The strategist
- The most intelligent and powerful model
- Built to handle highly complex tasks that demand reasoning, analysis and problem-solving
- Ex: in-depth financial analysis, complex business or marketing strategies, designing new software arch., etc

We can **compare** models with the following metrics:

- Intelligence -> deep reasoning. Benchmarks like SWE-bench, which tests real-world coding problems serves as a good proxy for a model's intelligence
- Speed -> latency. Low latency is crucial for quick responses.
- Cost -> Usually based on the number of tokens in the input and output.

Instead of using one model for all task we can use a multi-model strategy by dynamically choosing the best model for each individual task. This is known as **smart routing**.
