# Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use

- Score: 432 | [HN](https://news.ycombinator.com/item?id=48479452) | Link: https://github.com/anthropics/claude-code/issues/29045

### TL;DR
A Windows user found that Claude Desktop silently launches a full Hyper‑V VM (Vmmem) consuming ~1.8 GB RAM on every app start, even when only using basic chat. Once Cowork/agent mode has been used once and Windows’ VirtualMachinePlatform is enabled, the app keeps triggering vmcompute/vmwp at boot and launch, leaving thousands of stale “session” files and no cleanup. Workarounds are disabling VirtualMachinePlatform (breaking Cowork) or killing VM processes; user asks for true on‑demand VM startup and automatic cleanup.

---

### LLM perspective
- View: This is a classic “always-on infrastructure” bug: backend meant for advanced features runs for everyone, wasting scarce RAM.  
- Impact: Laptop users and corporate desktops with tight RAM/IT policies may avoid Claude Desktop until VM behavior is fixed.  
- Watch next: Look for a release note explicitly mentioning lazy-init for Cowork VM, session cleanup, and running cleanly when virtualization is unavailable.
