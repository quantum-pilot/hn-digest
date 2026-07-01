# Claude Code is steganographically marking requests

- Score: 1327 | [HN](https://news.ycombinator.com/item?id=48734373) | Link: https://thereallo.dev/blog/claude-code-prompt-steganography

### TL;DR
Anthropic’s Claude Code CLI was found to steganographically mark API requests—using environment-dependent prompt tweaks—to detect traffic going through custom proxies, likely to catch resellers and model-distillation labs. There was no clear disclosure. Many HN commenters see this as a serious trust and privacy breach that could also degrade responses for legitimate proxy users, and prefer auditable FOSS clients. Others argue it’s a pragmatic anti-abuse measure, harmless to normal customers, and much harder to evade than explicit telemetry.

*Content unavailable; summarizing from title and Hacker News comments.*

---

### Comment pulse
- Secret client changes feel like a rootkit → some fear undisclosed tagging implies more hidden data grabs (e.g., PII) and violates device autonomy.  
- Stego helps catch proxy resellers → gateways can’t easily strip subtle markers; better than explicit flags or KYC — counterpoint: sophisticated labs will evade it.  
- Anthropic’s approach looks crude → reverse-engineers expected subtler “underhanded code”; some think it’s just a temporary snapshot tool, and migrate to auditable FOSS CLIs.

---

### LLM perspective
- View: Undisclosed client fingerprinting for anti-distillation crosses a trust line; disclosure and opt-outs are feasible without nullifying defenses.  
- Impact: Enterprise security, compliance, and regulated industries will scrutinize AI tooling harder; some will standardize on auditable open-source clients.  
- Watch next: Whether Anthropic publishes technical docs, adds toggles, or doubles down; competitors’ telemetry choices will signal emerging industry norms.
