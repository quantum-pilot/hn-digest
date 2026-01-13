# Cowork: Claude Code for the rest of your work

- Score: 520 | [HN](https://news.ycombinator.com/item?id=46593022) | Link: https://claude.com/blog/cowork-research-preview

### TL;DR
Cowork is Anthropic’s new “Claude Code for everything else”: an agent inside the macOS Claude app that gets controlled access to local folders and connectors, then autonomously executes multi‑step tasks (organizing files, drafting docs, building spreadsheets, working via the browser). It asks before significant actions but can still delete or overwrite files and remains vulnerable to prompt‑injection risks, so usage guidance is cautious. HN discussion centers on sandboxing quality, irrecoverable data loss, confusing ToS for business use, and missing Linux support.

---

### Comment pulse
- Sandboxing and prompt injection: users want “lethal trifecta”-safe designs; today’s model still leans on user vigilance. — counterpoint: Anthropic notes full-VM execution and early but ongoing safety work.  
- Irreversible changes worry people: filesystem operations lack easy rollback; commenters predict horror stories unless Cowork adds built-in versioning or leverages OS snapshots transparently.  
- Product fit vs. ecosystem: Max ToS ban commercial use while tool targets work; Linux users feel neglected despite Anthropic’s dependence on Linux infrastructure.

---

### LLM perspective
- View: Cowork is a step toward mainstream, file-level AI agents, but current safety UX is closer to “power tool” than appliance.  
- Impact: Knowledge workers with messy local data benefit first; IT/security teams will scrutinize deployments and set guardrails.  
- Watch next: Native snapshot/rollback integration, clearer enterprise licensing, and serious Linux/Windows parity will determine real-world adoption.
