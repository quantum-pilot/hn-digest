# Grok Code Fast 1

- Score: 512 | [HN](https://news.ycombinator.com/item?id=45063559) | Link: https://x.ai/news/grok-code-fast-1

- TL;DR
    - xAI launches Grok Code Fast 1, a low-latency, low-cost model tuned for agentic coding with tool use and high prompt-cache hit rates. Priced at $0.20/M input and $1.50/M output tokens, it’s temporarily free via partner IDEs like Copilot and Cursor. xAI highlights real-world usability and an internal 70.8% SWE‑Bench‑Verified score. HN is split: hands-on testers praise speed and iterative edits; skeptics question benchmark claims, brand trust, and whether speed should trump quality. A multimodal, parallel-tools, longer-context variant is promised soon.

- Comment pulse
    - Speed changes workflow → rapid iteration in agentic loops, less waiting/context-switching; crucial for IDE UX — counterpoint: token quality still matters more to some.
    - Hands-on reports → very fast, small iterative edits, creates test files, handled ~110k tokens; cheap daily driver — counterpoint: Qwen+Cerebras claims ~10× TPS.
    - Trust and metrics questioned → xAI’s 70.8% SWE-Bench vs vals.ai ~57.6%; Musk/Grok controversies make some avoid it near code.

- LLM perspective
    - View: Positioned as a fast implementer for agents, not a top-tier reasoner; caching and tool-calling dominate design choices.
    - Impact: If latency stays low at scale, IDE vendors may default to it for execution, reserving slower models for planning.
    - Watch next: Independent harness-aligned SWE-Bench runs, end-to-end agent benchmarks, and the promised multimodal/parallel-tools/long-context release timeline.
