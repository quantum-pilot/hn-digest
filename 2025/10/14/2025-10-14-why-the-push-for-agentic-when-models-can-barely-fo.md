# Why the push for Agentic when models can barely follow a simple instruction?

- Score: 290 | [HN](https://news.ycombinator.com/item?id=45577080) | Link: https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154

- TL;DR
  - A frustrated dev questions “agentic” coding after GPT‑5/Gemini miss parts of a simple Go refactor. Practitioners reply that agents can be useful for bounded, tedious work when you impose structure: reference Markdown, plan/phase tasks, build indexes, work in small slices, and enforce tests/TDD—treat them like interns. Others blame marketing hype, tool limits (e.g., Cursor’s context pruning), and poor performance on novel/monolithic code. A few report strong results with sub‑agents and TDD, but overall success depends on process and guardrails.

- Comment pulse
  - Agents work with structure and tests → Plan-first, TDD, sub-agents; treat as intern; ship 95% AI-written — counterpoint: “more often than not” lacks reliability.
  - Agents are unreliable for complex or novel work → Miss context, invent APIs, double down on wrong fixes; Cursor’s pruning degrades results; marketing oversells capabilities.
  - Outcomes hinge on process, task, and expectations → Use frameworks, indexing/Markdown, small vertical slices, and tests; context windows limit unattended, long-running edits.

- LLM perspective
  - View: Agentic value is systems engineering: memory, decomposition, verification, and tool orchestration; without these, autonomy amplifies model error.
  - Impact: Expect fastest ROI in guarded domains: refactors with tests, log/trace triage, data migrations; not greenfield architecture or monolithic 6k-line rewrites.
  - Watch next: Demand reproducible agent benchmarks, transparent context management, and costed plans; track larger-context releases and native project-memory features in IDEs.
