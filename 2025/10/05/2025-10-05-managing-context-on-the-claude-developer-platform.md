# Managing context on the Claude Developer Platform

- Score: 177 | [HN](https://news.ycombinator.com/item?id=45479006) | Link: https://www.anthropic.com/news/context-management

- TL;DR
    - Anthropic adds context editing and a client-side memory tool to the Claude Developer Platform, letting agents prune stale tool outputs and persist state across sessions. Sonnet 4.5 tracks token budget, yielding internal gains: +39% with memory+editing, +29% editing alone; 100‑turn searches finished with 84% fewer tokens. Available in public beta, including Bedrock and Vertex AI. HN welcomes better long-running agents but asks for manual context controls, flags hallucination/kv-cache pitfalls when pruning, and worries these APIs formalize existing patterns and increase vendor lock‑in.

- Comment pulse
    - Power-user context control → Desire checkboxes/editable transcripts to exclude stale snippets and fix bad replies — counterpoint: chat UIs prioritize simplicity over surgical editing.
    - Pruning risks coherence → Removing tool outputs can break KV-cache assumptions and trigger hallucinations; some split work between short-lived and long-lived agents to limit churn.
    - Incremental, not novel → APIs formalize common patterns (summarize/obliterate outputs, file-backed memory); benefits are bandwidth/latency, but risk provider lock-in.

- LLM perspective
    - View: A standardized memory and pruning API reduces boilerplate and errors in agents; the novelty is model-aware token budgeting.
    - Impact: Most useful for coding/research agents with heavy tool use; ops teams gain predictable token usage and fewer stalled long workflows.
    - Watch next: Benchmarks on open models and real repos; UI for manual inclusion/exclusion; server-side histories without lock-in via exportable or client-managed stores.
