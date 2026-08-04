# Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable

- Score: 587 | [HN](https://news.ycombinator.com/item?id=48478969) | Link: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/

### TL;DR

Anthropic’s public Fable model, a limited version of cybersecurity-focused Mythos, falls back to Opus 4.8 when safeguards flag cybersecurity or biology prompts. Researchers report false positives on secure coding, code review, home automation, and scientific software, arguing that keyword-like filtering makes the model unreliable. Anthropic says restrictions reduce malware and bioweapon risks, while approved professionals can seek fewer limits through Cyber Verification. Hacker News debated whether broad guardrails meaningfully slow amateurs, create exploitable scanner blind spots, or mainly erode customer trust; commenters reported Anthropic would make some downgrades visible.

### Comment pulse

- Guardrails can become an evasion tool → malicious packages may inject forbidden prompts so LLM scanners refuse analysis — counterpoint: restrictions raise barriers for novices.
- Opaque model switching damages commercial trust → users cannot assess output quality or billing; notifications improve transparency, but the downgrade remains.
- Broad triggers block legitimate work → commenters cited mass-spectrometer parsers and Zigbee logs, though one user found Fable superior for mapping.

### LLM perspective

- **View:** Capability without predictable routing is not a dependable product, especially when users cannot reproduce which model answered.
- **Impact:** Security teams need model-change telemetry, per-model billing, and stable escalation paths before adopting Fable in automated workflows.
- **Watch next:** Measure false-positive rates by task class, scanner resistance to prompt injection, and outcomes from Cyber Verification.
