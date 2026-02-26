# Claude Code Remote Control

- Score: 473 | [HN](https://news.ycombinator.com/item?id=47148454) | Link: https://code.claude.com/docs/en/remote-control

### TL;DR
Claude Code’s new Remote Control lets you start a local Claude Code session on your machine and continue it from phone or browser, using your full local environment (filesystem, tools, MCP servers) without moving compute to the cloud. It tunnels over Anthropic’s API (outbound HTTPS only), supports QR linking, auto-reconnects after sleep, and is Pro/Max-only with one remote session per instance. HN users like the concept but report severe instability and prefer mature SSH/tmux-style setups or existing third‑party tools.

---

### Comment pulse
- Remote Control is very buggy → frequent disconnects, unkillable generations, stuck “plan mode,” missing QR, broken mobile integration, and opaque failures that waste Opus tokens—counterpoint: some accept this as prerelease roughness.  
- Many already use Tailscale/SSH + tmux/Zellij/zmx → gives persistent, device-agnostic CLI sessions today, with better control and predictability than the official feature.  
- Competing tools exist → Opencode “web” mode and happy.engineering already expose local AI sessions via browser/phone with fewer bugs, underscoring expectations set by long‑reliable SSH.

---

### LLM perspective
- View: The idea is right—unified local+mobile coding—but execution must reach SSH-level reliability before pros switch from DIY solutions.  
- Impact: If stabilized, this mainly benefits individual Pro/Max users who want local tools plus structured UI on the go.  
- Watch next: Better observability, token accounting, offline tests, and tighter mobile UX will determine whether Remote Control beats tmux-over-VPN in practice.
