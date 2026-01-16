# Bubblewrap: A nimble way to prevent agents from accessing your .env files

- Score: 173 | [HN](https://news.ycombinator.com/item?id=46626836) | Link: https://patrickmccanna.net/a-better-way-to-limit-claude-code-and-other-coding-agents-access-to-secrets/

### TL;DR
Bubblewrap is proposed as a simple, host-controlled way to sandbox coding agents like Claude Code so they can edit your project while being unable to touch secrets (e.g., `~/.aws`, `.env`, SSH keys). Unlike trusting Anthropic’s embedded sandbox or juggling a dedicated Unix user or Docker, you explicitly define what paths and capabilities are visible. The post includes concrete `bwrap` invocations, shows how to overlay `.env` with `/dev/null`, and frames this as defense‑in‑depth for all agents, not just Claude.

---

### Comment pulse
- Two modes preferred: tightly supervised, unsandboxed local agent vs fully unsupervised agent in isolated VM; middle-ground sandboxes add complexity without clear benefits — counterpoint: lightweight sandboxes cheaply block accidental secret leaks.
- Mounting `~/.claude` leaks sensitive past transcripts; writable directories and toolchains should be per-project rather than shared across all agent runs.
- Some use Docker or bwrap + unpacked Docker images as full roots; containers help, but don’t prevent prompt-injection abusing network access.

---

### LLM perspective
- View: OS-level tools like Bubblewrap give practical, auditable control, but misconfiguration remains the main failure mode.
- Impact: Developers running agents on laptops/servers containing unrelated secrets and SSH keys gain a straightforward risk-reduction pattern.
- Watch next: Opinionated bwrap profiles, IDE/agent integration, and comparative studies of escape resistance vs Docker, VMs, and vendor sandboxes.
