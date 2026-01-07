# Stop Doom Scrolling, Start Doom Coding: Build via the terminal from your phone

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46517458) | Link: https://github.com/rberg27/doom-coding

### TL;DR
This guide shows how to turn your phone into a thin terminal for an always‑on development machine at home, with Claude Code doing most of the coding. You install Tailscale and enable SSH on your computer, use Termius (with Mosh) on your phone to SSH into it via MagicDNS, then run the `claude` CLI to edit, run, and iterate on code from anywhere. Best practices include tmux sessions, HTTP servers for previews, and using Claude to keep a running CLAUDE.md log. HN discussion compares this to cloud dev VMs, Termux-style local setups, and GitHub/Copilot automation.

---

### Comment pulse
- Cloud dev environments instead → happy.engineering, OpenCode, or Claude Code’s own hosted VM remove the need for a home box or VPN.  
- Local or VPS + plain SSH → Termux/ConnectBot + tmux/vim or a cheap VPS give a similar “phone as terminal” workflow without Claude dependence.  
- Control via bots/email → some propose email/Telegram interfaces to Claude/CLI for changes—counterpoint: latency and clunkiness beat the simplicity of interactive SSH over Tailscale.

---

### LLM perspective
- View: Pattern is “AI pair‑programmer on a stable box, phone as dumb terminal”; ergonomics, not raw capability, is the focus.  
- Impact: Best for solo hackers and travelers who already keep a dev machine or VPS running and are comfortable with SSH tooling.  
- Watch next: Native mobile IDEs with integrated Claude/Copilot and persistent sandboxes may make VPN + home machine setups unnecessary.
