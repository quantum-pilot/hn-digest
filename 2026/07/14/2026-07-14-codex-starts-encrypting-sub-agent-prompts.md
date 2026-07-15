# Codex starts encrypting sub-agent prompts

- Score: 406 | [HN](https://news.ycombinator.com/item?id=48905028) | Link: https://github.com/openai/codex/issues/28058

## TL;DR
Codex’s MultiAgentV2 now encrypts sub-agent task/message payloads end-to-end, storing only ciphertext in history. That means you can no longer see what instructions a parent agent gave to a spawned or messaged sub-agent, breaking auditability, debugging, and post-hoc analysis. The GitHub issue proposes a compromise: keep encrypted payloads for model delivery, but add a bounded plaintext “audit” field that’s stored locally and never sent to the child model. A prototype exists for `spawn_agent`; `send_message`/`followup_task` still need it.

---

## Comment pulse
- Change = encrypted sub-agent prompts → rationale: protect orchestration prompts, RL traces, and possibly latent compaction blobs viewed as core IP rather than shareable text.  
- Developers: this feels like DRM → rationale: user can’t inspect or debug instructions running on their own machine—counterpoint: some only care about tool calls, not prompt text.  
- Alternative theory: mainly cache-key transport and responses-API–style obfuscation → rationale: aligns with OpenAI’s push away from transparent chat completions toward more opaque, provider-controlled reasoning endpoints.

---

## LLM perspective
- View: Encrypting sub-agent prompts without a local audit copy is a governance and debugging regression, even if motivated by IP or privacy concerns.  
- Impact: Agent-framework users, security teams, and compliance auditors lose visibility into what autonomous agents actually executed.  
- Watch next: Whether Codex adopts the proposed dual-field audit design broadly, or instead doubles down on fully opaque agent orchestration.
