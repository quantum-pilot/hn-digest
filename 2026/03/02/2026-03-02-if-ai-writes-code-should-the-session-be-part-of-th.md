# If AI writes code, should the session be part of the commit?

- Score: 460 | [HN](https://news.ycombinator.com/item?id=47212355) | Link: https://github.com/mandel-macaque/memento

### TL;DR

Memento attaches AI coding-session provenance to commits using Git notes, with Codex/Claude tooling and support for rewritten or merged history. Its newer design puts a reviewed summary in the ordinary notes stream while preserving the raw transcript and integrity metadata in a separate audit ref. HN debated whether this aids future debugging and on-demand questioning or merely archives noisy false starts, mistakes, red herrings, and unverifiable narration. Many preferred committing evolving specifications and final plans as durable intent, while retaining full sessions only as optional audit material.

### Comment pulse

- Full sessions preserve corrections where requirements crystallize — counterpoint: raw logs contain dead ends and may not prove the committed code’s provenance.
- Several developers version design, plan, and debug documents, gaining reusable intent without forcing future readers through every exchange.
- Others expect future agents to query archived sessions dynamically, recovering answers that no fixed commit message could anticipate.

### LLM perspective

- **View:** Layered storage is sensible: reviewed intent by default, raw sessions as queryable, access-controlled evidence.
- **Impact:** Provenance could improve audits and maintenance, but uncontrolled logs increase repository weight, privacy exposure, and false confidence.
- **Watch next:** Redaction, authenticity, note portability, history rewrites, selective retrieval, and whether future agents measurably benefit.
