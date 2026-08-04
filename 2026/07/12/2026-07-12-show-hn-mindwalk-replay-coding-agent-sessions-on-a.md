# Show HN: Mindwalk – Replay coding-agent sessions on a 3D map of your codebase

- Score: 146 | [HN](https://news.ycombinator.com/item?id=48878682) | Link: https://github.com/cosmtrek/mindwalk

### TL;DR

Mindwalk turns Claude Code, Codex, and pi logs into local 3D repository replays, showing which files agents saw, read, edited, or ignored. A Go server normalizes traces and deterministic codebase maps, while a React/Three.js UI adds playback, inspection, subagent lenses, friction signals, and client-side video export. Viewing stays local; optional evaluation sends a compact session summary through the user’s CLI for evidence-linked process and task scoring. HN liked the metaphor but questioned whether replay beats diffs, suggesting comparative and aggregate model analysis as the stronger use case.

### Comment pulse

- Comparative analysis drew the clearest demand → side-by-side models or averaged repeated runs could expose strategy differences and variance.
- Spatial interfaces excited some readers → agent work may benefit from new metaphors beyond linear logs and diffs.
- Utility remained contested → replay reveals investigative shape — counterpoint: critics saw added friction without a concrete decision it improves.

### LLM perspective

- **View:** The map is most useful as behavioral telemetry, not as a replacement for code review.
- **Impact:** Deterministic layouts and normalized traces create a foundation for comparing agents, prompts, and repository-specific guidance.
- **Watch next:** Add quantitative overlays, run-to-run aggregation, and studies showing faster detection of scope drift or weak verification.
