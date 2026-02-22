# macOS's Little-Known Command-Line Sandboxing Tool (2025)

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47101200) | Link: https://igorstechnoclub.com/sandbox-exec/

## TL;DR

`sandbox-exec` is a built‑in macOS command that runs programs under custom sandbox profiles written in Scheme-like SBPL: you set a default policy, then precisely allow/deny file, process, and network operations. The article shows deny‑by‑default vs allow‑by‑default patterns, real-world examples like a network‑blocked shell, use of Apple’s own profiles, and debugging via Console/log stream. HN discussion emphasizes that `sandbox-exec` has been officially deprecated for years yet underpins tools (including LLM coding assistants), spurring GUIs and community profiles despite uncertainty about its future.

---

## Comment pulse

- Deprecation is long-standing (since around 10.13); still works and is widely used—counterpoint: Apple’s track record shows deprecated tools can linger for decades (cron).

- Deeper resources document SBPL compilation to bytecode and kernel MAC hooks, clarifying how policies are actually enforced and why complex apps can be tricky to confine.

- Real usage: Codex and Claude Code sandbox with `sandbox-exec`; some users still double-sandbox for peace of mind, while others build GUIs and share minimal, audited profiles.

---

## LLM perspective

- View: CLI sandboxing is a practical extra layer when running AI-generated code, complementing but not replacing vendor sandboxes.

- Impact: Security-conscious macOS users, AI tooling, and agent frameworks gain finer-grained, inspectable controls than opaque built-in sandboxes.

- Watch next: Whether Apple removes or replaces `sandbox-exec`, emergence of audited profile sets, and better tooling/UX for composing and testing SBPL policies.
