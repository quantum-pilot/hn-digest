# Open Source Isn't Dead

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47780712) | Link: https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats

### TL;DR

After Cal.com cited AI-scaled vulnerability discovery when closing its core codebase, open-source security vendor Strix argues secrecy will not remove externally visible APIs, browser states, network traffic, or business-logic flaws. It recommends continuous autonomous exploitation tests inside CI/CD instead of relying on human review or obscurity. Commenters agreed AI-generated reports now mix real findings with noisy edge cases, but disputed the binary: closed-source companies can scan internally while secrecy can still raise attackers’ costs.

### Comment pulse

- Some maintainers benefit from legitimate reports but face hallucinated bounty spam and a growing remediation backlog.
- Many read Cal.com’s change as standard open-core monetization with AI security as a convenient explanation.
- Strix’s argument seemed useful — counterpoint: its prescribed solution aligns directly with its commercial product.

### LLM perspective

- Open versus closed changes discovery economics; neither substitutes for authentication, isolation, patching, and monitoring.
- Automated defense must prioritize reproducible exploits and suppress noise before maintainers become the bottleneck.
- Publishing frequent audit results could turn marginal-cost scanning into verifiable security posture.
