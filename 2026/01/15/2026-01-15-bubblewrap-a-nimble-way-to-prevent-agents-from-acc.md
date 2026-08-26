# Bubblewrap: A nimble way to prevent agents from accessing your .env files

- Score: 173 | [HN](https://news.ycombinator.com/item?id=46626836) | Link: https://patrickmccanna.net/a-better-way-to-limit-claude-code-and-other-coding-agents-access-to-secrets/

### TL;DR

The author recommends wrapping coding agents with Linux Bubblewrap as a user-controlled defense layer. Read-only system mounts, a writable project bind, namespace isolation, optional network sharing, and `/dev/null` overlays for `.env` files can constrain an autonomous agent without Docker’s daemon or a separate account’s ACL friction. HN readers agreed that reducing accidental secret exposure is valuable, but challenged the sample’s writable `~/.claude` mount, which contains credentials and transcripts. Others preferred full VMs, Docker images, or a complete sandbox root for stronger isolation.

### Comment pulse

- A lightweight sandbox blocks common accidental leaks → counterpoint: every layer has escapes, so serious unattended work may still warrant a VM.
- Binding `~/.claude` preserves login convenience → it also exposes credentials, prior transcripts, and cross-project state to prompt injection.
- A full unpacked container root reduces host leakage → add separate project state, unshare namespaces, drop capabilities, and restrict networking.

### LLM perspective

- View: Bubblewrap is useful defense-in-depth when its allowlist is narrower than the sample configuration.
- Impact: Developers gain faster autonomous workflows, but become responsible for maintaining precise mounts and network policy.
- Watch next: Per-project auth storage, tested escape harnesses, safer presets, and comparable local VM ergonomics.
