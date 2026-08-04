# Claude Code uses Bun written in Rust now

- Score: 370 | [HN](https://news.ycombinator.com/item?id=48966569) | Link: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/

### TL;DR

Simon Willison verified that Claude Code 2.1.181+ embeds Bun’s Rust rewrite: its binary reports Bun 1.4.0, contains 563 Rust source paths, and exposes the embedded version through a preload hook. Bun says the change improved Linux startup by 10% and otherwise went unnoticed in production. HN viewed that quiet rollout as evidence of compatibility, but debated why a terminal UI needs React and JavaScript, whether Claude Code should be native, how much safety survives unsafe Rust, and what Anthropic ownership means for Bun’s governance.

### Comment pulse

- Web tooling looks wasteful in a TUI → users reported heavy CPU, battery, and memory costs — counterpoint: JavaScript accelerates iteration and preserves ecosystem compatibility.
- Rust provides agent guardrails → compiler feedback catches lifetime mistakes that manual Zig management missed, though extensive unsafe blocks weaken guarantees.
- Governance, not runtime, drove distrust → a huge rapidly merged rewrite and acquisition raised roadmap concerns despite the public patch and invisible migration.

### LLM perspective

- **View:** A successful runtime rewrite is validated less by generated code volume than by unchanged behavior under real workloads.
- **Impact:** Compiler-enforced constraints can make large agent-assisted ports safer, while stable JavaScript APIs preserve product velocity and plugin ecosystems.
- **Watch next:** Track crash rates, memory use, startup latency, unsafe-code audits, canary-to-stable promotion, and published governance commitments.
