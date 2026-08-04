# How is the Bun rewrite in Rust going?

- Score: 446 | [HN](https://news.ycombinator.com/item?id=49067854) | Link: https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html

### TL;DR

An audit challenges claims that Bun’s AI-assisted Rust rewrite was finished in 11 days for $165,000. Six weeks after merging, no public release tag had appeared; 2,475 Robobun pull requests remained open, CI kept running, and Anthropic employees were increasingly involved, suggesting substantial unreported work and cost. Bun creator Jarred Sumner replied that Claude Code users had received the Rust version unnoticed and v1.4 awaited promised Node.js compatibility tests. HN debate centered on whether translation speed matters without lifecycle cost, maintenance, and quality evidence.

### Comment pulse

- Release cadence is ambiguous evidence → major rewrites slow development, canary users reported no major issues, and v1.4 was intentionally gated on compatibility.
- Generation is only the opening phase → commenters emphasized integration, architecture, bug fixing, security, support, and ownership as the enduring engineering burden.
- The rewrite can still be an engineering success → preserving tests and feature parity quickly may justify ambition — counterpoint: full costs remain undisclosed.

### LLM perspective

- **View:** A repository transition and a production-ready release are different milestones; claims should identify which one elapsed time describes.
- **Impact:** AI-assisted rewrites shift bottlenecks from code generation toward validation, CI capacity, review throughput, and long-term maintainership.
- **Watch next:** Track v1.4 regressions, performance, unsafe-code reduction, total compute spend, review backlog, and maintainer workload after release.
