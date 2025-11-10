# Reverse engineering Codex CLI to get GPT-5-Codex-Mini to draw me a pelican

- Score: 145 | [HN](https://news.ycombinator.com/item?id=45862802) | Link: https://simonwillison.net/2025/Nov/9/gpt-5-codex-mini/

- TL;DR
  - Simon Willison modified OpenAI’s open-source Codex CLI (Rust) to add a “codex prompt” command that directly hits the private Codex backend, using the CLI’s auth and baked-in instructions. A --debug flag revealed request structure and that the backend rejects calls without those default instructions; a developer message can be injected while disabling tools. He benchmarked “pelican-on-a-bike” SVGs: GPT‑5‑Codex‑Mini performed poorly vs GPT‑5. HN debated outsourcing build steps to LLMs, Codex’s locked system prompt, and whether SVG is a meaningful capability test.

- Comment pulse
  - Delegating setup to LLMs boosts velocity in unfamiliar stacks → seeds context, automates cargo steps — counterpoint: erodes skills; cargo install is trivial.
  - Codex backend locks a single system prompt → hard to integrate other agents; translating tool calls without prompt control proved fruitless.
  - SVG pelican as eval is entertaining → cross‑model variance surfaced; but poor benchmark since models don’t perceive rendered output.

- LLM perspective
  - View: Open-source client loopholes let users probe gated models without new keys, revealing practical constraints on agent prompts and tooling.
  - Impact: Expect more community forks and quick hacks; vendors may lock down endpoints, obfuscate instructions, or tighten per-app auth.
  - Watch next: Official API access, controllable tool flags, transparent reasoning settings; comparative code/graphics evals beyond toy SVGs.
