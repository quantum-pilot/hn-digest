# Go hard on agents, not on your filesystem

- Score: 573 | [HN](https://news.ycombinator.com/item?id=47550282) | Link: https://jai.scs.stanford.edu/

### TL;DR
jai is a small Linux sandbox tool aimed at safely running AI agents and shell commands without giving them full control of your account. It wraps an existing workflow with a one-command jail: current directory stays writable, home can be overlaid or hidden, and the rest of the system is mostly read-only, with three isolation modes. HN discussion contrasts jai with editor‑integrated sandboxes, classic Unix isolation (separate users, permissions), and even separate machines, while warning about both data loss and data exfiltration risks.

---

### Comment pulse
- Built‑in sandboxes (e.g., Claude’s filesystem config) exist → but are fragile, may change silently, and issues show they’re not yet fully trustworthy—counterpoint: OS‑level tools already solve this.  
- Many find it reckless to hand agents full personal machines → people underestimate that cloud inference already sees everything the agent “looks at,” regardless of local sandboxing.  
- Alternatives: separate Unix user + shared group folder, or a dedicated laptop/VM → reduces blast radius but adds friction; install instructions themselves must avoid “curl | bash” hypocrisy.

---

### LLM perspective
- View: Lightweight, default‑easy sandboxes are necessary if we expect non‑experts to run agents locally without catastrophic mistakes.  
- Impact: Individual developers and small teams get practical guardrails before enterprises standardize stricter container/VM policies.  
- Watch next: IDEs and agent frameworks bundling OS‑level sandboxes by default, with auditable configs and automated “prove the sandbox works” tests.
