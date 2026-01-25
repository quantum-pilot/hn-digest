# Claude Code's new hidden feature: Swarms

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46743908) | Link: https://twitter.com/NicerInPerson/status/2014989679796347375

### TL;DR
Claude Code’s hidden “Swarms” feature is essentially task‑oriented multi‑agent orchestration: a main “manager” model delegates work to specialized subagents that operate in parallel, track progress via task boards/mailboxes, and coordinate largely without constant user prompting. Enthusiasts report impressive results and reduced cognitive load when treating this as an AI project team, sometimes mixing models and isolated worktrees. Skeptics worry current models generate too much low‑quality, hard‑to‑review code, arguing that human‑in‑the‑loop workflows, small diffs, and strong review remain essential.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Multi‑agent “AI team” works → Coordinator/manager agent plus specialized subagents (backend, frontend, docs, CAB, etc.) can port large systems while user mostly supervises.  
- Swarms vs “just subagents” → New mode is task‑centric with team/mailbox abstractions; Claude manages Claude, reducing chat micromanagement—counterpoint: plans still too shallow for reliability.  
- Code volume and trust issues → Big autonomous changes are hard to review; many prefer small stacked PRs plus reviewer agents instead of letting swarms freely generate long‑lived code.

---

### LLM perspective
- View: Swarms are orchestration UX, not magic; success hinges on tight scopes, guardrails, and reviewable increments.  
- Impact: Most helpful for large refactors/ports where humans define architecture but offload repetitive implementation and documentation.  
- Watch next: Metrics on defect rates and code churn from swarm‑generated changes versus traditional copilot or human‑only workflows.
