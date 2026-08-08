# The Zig project's rationale for their anti-AI contribution policy

- Score: 633 | [HN](https://news.ycombinator.com/item?id=47957294) | Link: https://simonwillison.net/2026/Apr/30/zig-anti-ai/

### TL;DR

Zig bans LLM use in issues, pull requests, and comments because maintainers treat review as investment in people, not merely code. Its contributor-poker model accepts imperfect work to develop newcomers into trusted collaborators; AI-assisted submissions consume review capacity without demonstrating or growing that understanding, while enabling low-effort spam. Bun cited the policy when declining to upstream a 4× compile-speed patch, though Zig contributors raised architectural objections. Hacker News largely found the rationale coherent, while distinguishing careless generated PRs from supervised work and noting the policy depends on abundant contributors.

### Comment pulse

- Zig reports hallucinated, noncompiling drive-bys, 10,000-line first PRs, and contributors unable to explain work despite denying LLM use.
- Compilation and lint gates catch superficial failures, but not architectural mismatch, review dialogue, or whether a contributor can maintain code.
- Some call this AI-enabled spam — counterpoint: careful iterative assistance can condense substantial human judgment into reviewable changes.

### LLM perspective

- **View:** The scarce resource is maintainer attention and future trust, not patch generation.
- **Impact:** A blanket ban sacrifices some good patches to protect community formation and signal expectations.
- **Watch next:** Enforcement consistency, contributor pipeline, Bun fork divergence, and whether supervised AI disclosure becomes acceptable.
