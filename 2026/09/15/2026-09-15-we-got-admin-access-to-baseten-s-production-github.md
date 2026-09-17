# We got admin access to Baseten's production GitHub

- Score: 322 | [HN](https://news.ycombinator.com/item?id=49716476) | Link: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover

### TL;DR

Strix says its autonomous security agent found an anonymously pullable Baseten container, then discovered a three-year-old GitHub token embedded in Docker build history. The still-active token had admin or write access to product, GitOps, Homebrew, and customer-specific repositories. Strix limited verification to read-only requests and disclosed the issue; Baseten privatized the registry and rotated the token the next day, saying logs showed no exploitation or customer-data exposure. HN praised remediation but questioned authorization, disclosure rewards, and the strength of that assurance.

### Comment pulse

- Old images are durable secret leaks → deleting files from layers is insufficient when expanded build arguments remain in image metadata.
- Rapid remediation earned praise → Baseten confirmed collaboration and revoked access, but commenters challenged the logging claim and token-rotation sequence.
- Autonomous probing raises governance questions → defenders valued speed, while others asked whether testing a prospective vendor without prior authorization crossed a boundary.

### LLM perspective

- View: The agent's advantage was persistent, cheap exploration of a conventional attack chain, not discovery of an unprecedented technique.
- Impact: Container publishers must audit public projects, every historical layer, build metadata, and overprivileged credentials—not merely current source code.
- Watch next: Adopt expiring least-privilege tokens, BuildKit secret mounts, registry exposure monitoring, and explicit rules of engagement for autonomous scanners.
