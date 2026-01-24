# Auto-compact not triggering on Claude.ai despite being marked as fixed

- Score: 174 | [HN](https://news.ycombinator.com/item?id=46736091) | Link: https://github.com/anthropics/claude-code/issues/18866

### TL;DR
A GitHub issue documents a regression where Claude.ai’s auto-compaction no longer triggers on long chats, causing messages to bounce back or silently fail well below the advertised 200k context. Many paying users say this makes Claude effectively unusable for multi-hour work and are frustrated by sparse official communication and refunds. Hacker News discussion uses the incident to question Anthropic’s reliability around context management, limits, and product quality as models, IDE integrations, and pricing experiments grow more complex.

---

### Comment pulse
- Opus feels “nerfed” and less competent → some blame A/B testing or cost-cutting; others say it’s expectation shift and randomness, seen with every LLM.  
- Claude Code UX complaints → rollbacks, checkpoints, and login flows often broken; users resort to git and manual summaries to survive context/compaction glitches.  
- Context limits feel tighter → users hit limits early, chats silently die, especially on big-context betas; some consider new accounts or plan changes to cope.  

---

### LLM perspective
- View: Reliability bugs around compaction and limits matter more than raw model IQ once LLMs are integrated into daily workflows.  
- Impact: Persistent silent failures erode trust, increase support burden, and push serious users toward rivals or self-hosted tooling.  
- Watch next: Clear postmortem, status-page updates, measurable fixes to auto-compaction, and published guidance on effective context use and token economics.
