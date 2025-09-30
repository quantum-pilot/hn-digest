# Claude Sonnet 4.5

- Score: 1211 | [HN](https://news.ycombinator.com/item?id=45415962) | Link: https://www.anthropic.com/news/claude-sonnet-4-5

- TL;DR
  - Anthropic’s Claude Sonnet 4.5 targets agentic coding and computer use: SOTA on SWE-bench Verified (77.2%; 82% high-compute) and OSWorld (61.4%), with reports of 30‑hour unattended tasks. Shipping: Claude Code checkpoints, VS Code extension, API context/memory, in‑chat code execution and file creation, Chrome extension, plus a new Agent SDK. Safety: ASL‑3, stronger prompt‑injection defenses, fewer misaligned behaviors. Same price as Sonnet 4. HN reactions laud the interpreter and tooling but report mixed head‑to‑head results vs GPT‑5‑Codex, emphasize prompt/design scaffolding, and question the 30‑hour claim and benchmark‑driven hype.

- Comment pulse
  - Sonnet fast but shallow; GPT‑5‑Codex slower yet thorough with tests → on 200k‑LoC app, Sonnet broke auth; Codex shipped. — counterpoint: prompts and retries matter.
  - “30‑hour autonomy” claim questioned → likely required heavy scaffolding, tools, and validation; not plug‑and‑play for average devs.
  - Benchmarks vs reality → users report variability, possible post‑launch throttling, and different “collaboration styles”; Claude praised for control, Codex for boldness.

- LLM perspective
  - View: Model claims emphasize tool use and long‑horizon agents; effectiveness hinges on environment design more than raw benchmarks.
  - Impact: Agent SDK and in‑chat execution push teams toward supervised autonomy; security filters temper risky domains and may affect usability.
  - Watch next: Independent OSWorld/SWE replications, reproducible 30‑hour runs, SDK reference agents, and transparency on any capacity‑driven model changes.
