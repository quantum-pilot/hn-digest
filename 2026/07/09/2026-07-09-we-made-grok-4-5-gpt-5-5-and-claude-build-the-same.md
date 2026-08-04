# We made Grok 4.5, GPT-5.5, and Claude build the same apps

- Score: 169 | [HN](https://news.ycombinator.com/item?id=48838772) | Link: https://www.tryai.dev/blog/grok-4.5-vs-gpt-5.5-vs-claude-build-off

### TL;DR

A TryAI launch-day comparison asked Grok 4.5, GPT-5.5, Claude Opus 4.8, and Claude Fable 5 to one-shot three self-contained HTML apps, allowing one retry only when rendering failed. Both Claude models built animated Rubik’s cubes immediately; Grok succeeded on retry and GPT failed. All produced particle sandboxes and playable Breakout games, with GPT favored aesthetically for particles. A separate short-prompt harness found Grok cheapest and fastest-streaming, while Fable was slowest and costliest. The post crowned Grok on value, but HN questioned that verdict, the tiny subjective sample, and AI-like prose.

### Comment pulse

- Builder reliability favored Claude → both variants solved the hardest stateful task first try, while Grok required its permitted retry and GPT failed.
- The declared winner reflects weighting → Grok led cost and streaming speed — counterpoint: commenters valued first-pass correctness above doing weaker work faster.
- Presentation undermined trust → repetitive benchmark-copy phrasing led readers to suspect the article itself was model-generated, distracting from the artifacts.

### LLM perspective

- **View:** The raw builds are useful examples, but one attempt and taste-based judgments cannot establish a robust model ranking.
- **Impact:** Model choice depends on whether first-pass correctness, visual polish, latency, or token cost dominates the actual workload.
- **Watch next:** Repeat blinded trials, score behavior with tests, separate build latency from short-answer metrics, and publish failure-adjusted cost.
