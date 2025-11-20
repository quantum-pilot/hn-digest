# Building more with GPT-5.1-Codex-Max

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45982649) | Link: https://openai.com/index/gpt-5-1-codex-max/

## TL;DR
GPT‑5.1-Codex-Max is OpenAI’s new flagship “agentic” coding model, optimized for long, complex software tasks. It introduces compaction, letting the model work coherently across multiple context windows for hours or even a day, enabling project-scale refactors and long debugging sessions. It’s 30% more token‑efficient at similar reasoning levels and sets new SOTA scores on SWE‑Bench Verified, SWE‑Lancer, and TerminalBench. HN users report Codex as highly literal, persistent, and strong for large, correctness-critical changes, and generally preferring it over Gemini and Claude for deep engineering work.

---

## Comment pulse
- Codex as “literal genie” → follows every instruction doggedly, great for huge refactors but can over-engineer weird specs—counterpoint: some prefer Claude’s more “common sense” judgment.
- Real-world use → users report 30–45 minute, large-scale rewrites (e.g., flight sim coordinate system) that “just worked,” with Codex strictly adhering to brief, high-level directions.
- Model comparisons → many find Codex a better collaborator than Gemini 3 and Claude for planning and integration; Gemini writes nicer code but hallucinates and skips requirements.

---

## LLM perspective
- View: Codex-Max pushes from “autocomplete” to durable software agents that can own substantial chunks of development workflows.
- Impact: Strongest leverage is for senior devs and teams doing big refactors, migrations, and long-running maintenance tasks.
- Watch next: API release details, concrete pricing vs 5.1, richer context-management features (subagents/hooks), and real-world cybersecurity policy updates as capabilities increase.
