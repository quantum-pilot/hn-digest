# How is the Bun rewrite in Rust going?

- Score: 446 | [HN](https://news.ycombinator.com/item?id=49067854) | Link: https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html

- TL;DR  
  - The article questions marketing around Bun’s “rewritten in Rust in 11 days for $165k,” arguing it’s being used as proof that Anthropic’s Claude can replace open‑source maintainers. By looking at missing release tags, thousands of open AI-generated PRs, intense CI usage, and Anthropic engineers’ direct involvement, the author infers ongoing work and much higher real costs. HN commenters, including Bun’s creator, counter that the Rust engine is already in production for Claude Code users, the rewrite is largely successful, and the delay is about compatibility targets, not failure.

- Comment pulse  
  - Rust rewrite is effectively shipped → Claude Code already uses it; v1.4 waits on promised Node.js test coverage, not on serious bugs.  
  - AI ROI is murky → thousands of AI-generated PRs and long CI runs imply substantial hidden infrastructure and human review costs beyond token spend.  
  - LLMs excel at fast ports, not maintenance → devs report quick prototypes but painful integration and debugging—counterpoint: keeping architecture identical can make post-rewrite onboarding manageable.

- LLM perspective  
  - View: AI-assisted large rewrites work when backed by exhaustive tests, human reviewers, and willingness to absorb big infra costs.  
  - Impact: Maintainers gain ambition to tackle risky refactors; small projects may be priced out of serious LLM-driven rewrites.  
  - Watch next: Bun’s v1.4 postmortem, transparent cost breakdowns, and independent benchmarks comparing Rust Bun, Zig Bun, and Node.js.
