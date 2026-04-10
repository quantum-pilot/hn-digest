# The Vercel plugin on Claude Code wants to read your prompts

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47704881) | Link: https://akshaychugh.xyz/writings/png/vercel-plugin-telemetry

### TL;DR
A deep dive into Vercel’s official Claude Code plugin finds it quietly collecting extensive telemetry: device ID, OS, framework info, and the full text of every Bash command Claude runs—across all projects, not just Vercel ones. A “consent” dialog about sharing prompts is actually a prompt-injected script that impersonates native UI and runs shell commands to flip a preference flag. Prompt logging is opt‑in, but command/session telemetry is on by default, with opt‑out hidden. HN sees this as a serious trust and supply‑chain issue and calls on Anthropic to enforce plugin policies and add permissions/attribution.

---

### Comment pulse
- This looks less like an accident, more like deliberate maximal data collection → broad matchers, all-project scope, and separate npm tooling already shipping opt‑out telemetry.  
- Users view this as a supply‑chain attack → full Bash commands from unrelated repos sent to Vercel violates Claude’s own plugin rules.  
- Broader frustration: “vibeslop” engineering and weak oversight → incentives reward shipping features and growth, not scoping, hardening, or clear consent—counterpoint: some blame Vercel’s culture, not AI per se.

---

### LLM perspective
- View: Plugin ecosystems need explicit permissions, attribution, and scoping, or every “helper” becomes a potential exfiltration channel.  
- Impact: Devs, security teams, and vendors must treat editor/agent plugins like privileged agents, with reviews and network controls.  
- Watch next: Anthropic’s response, updated plugin policies/UX, Vercel revisions or rollbacks, and security audits of other AI-tooling plugins.
