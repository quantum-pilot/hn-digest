# Reverse engineering Codex CLI to get GPT-5-Codex-Mini to draw me a pelican

- Score: 145 | [HN](https://news.ycombinator.com/item?id=45862802) | Link: https://simonwillison.net/2025/Nov/9/gpt-5-codex-mini/

### TL;DR

Simon Willison used Codex itself to modify the open-source Rust CLI, adding a `codex prompt` subcommand for direct, tool-free prompts through its existing ChatGPT authentication and privileged backend. Iteration revealed the endpoint rejects requests without Codex's default instructions, so the final version retained them while adding a developer message, model selection, streaming, and debug output. GPT-5-Codex-Mini produced the weakest pelican-on-a-bicycle SVG of three tested models. Discussion debated whether delegating basic build discovery saves momentum or erodes useful skills.

### Comment pulse

- Willison said building first primes the agent with repository context and proves it can test later edits.
- Critics noted SVG-from-text is a poor intelligence test because models cannot inspect their rendered result.

### LLM perspective

- View: The exercise exposes product-bound API assumptions more clearly than it evaluates the new model's coding ability.
- Impact: Open-source clients let users prototype missing interfaces, though undocumented endpoints remain fragile and privileged.
- Watch next: Official API access, instruction flexibility, endpoint stability, and task-relevant Mini evaluations.
