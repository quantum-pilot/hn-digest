# The Zig project's rationale for their anti-AI contribution policy

- Score: 633 | [HN](https://news.ycombinator.com/item?id=47957294) | Link: https://simonwillison.net/2026/Apr/30/zig-anti-ai/

- TL;DR  
Zig forbids LLM-written issues, PRs, and bug-tracker comments because maintainers view reviews as investments in *people*, not code. VP Loris Cro’s “contributor poker” model says the goal is to grow trusted long-term contributors, so even a perfect AI patch yields poor return on scarce reviewer time. The Bun fork’s 4× compile-speed improvements dramatize the policy but also clash with Zig’s language-level roadmap. HN discussion centers on AI-driven spam, CI defenses, and whether maintainers should just use LLMs directly.

- Comment pulse  
  - LLM PRs are mostly hallucinated, non-compiling drive‑bys → they waste reviewer time and feel like spam, though better CI could filter some noise.  
  - Zig–Bun fork clash → some say the AI ban blocks a 4× speedup; maintainers point to roadmap conflicts and patch complexity—counterpoint: policy excludes LLM work.  
  - Community-first strategy → like ZeroMQ, Zig prioritizes humans over raw performance; some argue maintainers can just query LLMs directly, bypassing AI-assisted drive‑by contributors.

- LLM perspective  
  - View: Zig optimizes for social capital, betting that a smaller, highly invested contributor base outperforms maximizing short-term code inflow.  
  - Impact: Policy advantages mature projects overloaded with PRs; nascent libraries or under-maintained tools may benefit more from permissive, AI-friendly workflows.  
  - Watch next: Expect experiments with dual tracks: core repos disallow AI, while peripheral tooling and documentation welcome clearly labeled, reviewed LLM-assisted contributions.
