# Codex starts encrypting sub-agent prompts

- Score: 406 | [HN](https://news.ycombinator.com/item?id=48905028) | Link: https://github.com/openai/codex/issues/28058

### TL;DR

A Codex issue reports that MultiAgentV2 now encrypts `spawn_agent`, `send_message`, and `followup_task` payloads, leaving readable content empty in local rollout history, traces, and communication logs. Recipient models still get the message, but users cannot later inspect what was delegated or why a child thread existed. The proposed fix keeps encrypted delivery while persisting a bounded plaintext audit companion; a prototype covers spawning, with messaging work remaining. HN objected to opaque delegation on local machines, while speculative explanations included IP protection, cache transport, or training architecture; tool calls remain visible.

### Comment pulse

- Auditability is the core regression → users lose task provenance needed to debug agent decisions, trace costs, and judge whether delegation was appropriate.
- Local execution raised consent concerns → encrypted instructions can guide agents with shell access — counterpoint: observable tool calls still expose resulting actions.
- Motives remained uncertain → commenters proposed cache efficiency, orchestration secrecy, and distillation defense, but the issue provides no confirmation.

### LLM perspective

- **View:** Encryption and auditability are separate properties; recipient confidentiality need not erase a user-owned record of delegated intent.
- **Impact:** Custom integrations lose replay and diagnosis fidelity, while enterprises face weaker governance over automated work in their environments.
- **Watch next:** Audit fields across three tools, size limits, resume/replay tests, UI visibility, retention controls, and a documented threat model.
