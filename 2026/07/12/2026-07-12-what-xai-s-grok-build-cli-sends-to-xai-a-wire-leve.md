# What xAI's Grok build CLI sends to xAI: A wire-level analysis

- Score: 395 | [HN](https://news.ycombinator.com/item?id=48877371) | Link: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547

- TL;DR
    - Grok’s build CLI, analyzed at the wire level, appears to upload your entire git-tracked repository and history to xAI via a separate endpoint, beyond normal tool calls. Commenters see this as risky data exfiltration that can silently reconstruct proprietary codebases and secrets, especially with opaque auto-updating native agents. Others argue any tool running in a repo effectively “owns” that directory, but many recommend sandboxing CLIs with bubblewrap, constrained filesystems, and network isolation to limit unintended exposure.
    - *Content unavailable; summarizing from title/comments.*

- Comment pulse
    - Sandbox CLIs aggressively → run agents inside bubblewrap or similar, with minimal filesystem access and restricted network, so “yolo” automation can’t leak unrelated secrets.
    - Native coding agents are privacy hazards → opaque updates and server-side tools can exfiltrate whole repos; open agents via APIs feel safer, not truly secure.
    - Some expect repo-wide access → agents must read many files; a distinct bulk-upload endpoint looks like training-data harvesting—counterpoint: could also reduce tool-call latency.

- LLM perspective
    - View: Treat any proprietary agent runner as untrusted remote code with full-folder access; architect workflows assuming eventual data leakage.
    - Impact: Enterprises, contractors, and regulated sectors must formalize policies for LLM tooling, including mandatory sandboxing and approved data scopes.
    - Watch next: Independent audits of other tools’ network traffic, clearer vendor data-retention terms, and OS-level permissions models for AI assistants.
