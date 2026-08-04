# Show HN: Smart model routing directly in Claude, Codex and Cursor

- Score: 133 | [HN](https://news.ycombinator.com/item?id=48688700) | Link: https://github.com/workweave/router

### TL;DR

Weave Router is a hosted or self-hosted proxy that exposes Anthropic, OpenAI, and Gemini-compatible endpoints, then selects a model per request using a small on-router embedder and cluster scorer. It supports Claude Code, Codex, opencode, and early-beta Cursor, plus open models through compatible providers; self-hosting keeps BYOK keys encrypted locally, and routing emits OTLP traces. HN welcomed potential API savings but questioned cache misses, model-specific prompting, agent orchestration, and scorer drift. The creator says switching thresholds account for cache cost and promised public coding-agent benchmarks.

### Comment pulse

- Prompt caching can erase routing savings → agent sessions pay heavily when models switch — counterpoint: the router raises its switch threshold after cache establishment.
- Agent harnesses already encode task and model choices → a proxy may disrupt planning, fallback, and model-specific prompting feedback loops.
- Evidence remains the adoption bottleneck → commenters requested coding-agent quality, cost, and latency comparisons plus an update strategy for frequent releases.

### LLM perspective

- **View:** Routing is plausible, but session context and cache economics make coding agents harder than stateless chat.
- **Impact:** If validated, teams could lower model spend without rewriting Claude Code, Codex, or opencode workflows.
- **Watch next:** Publish task-level routing logs, cache-adjusted costs, quality regressions, release adaptation speed, and benchmark methodology.
