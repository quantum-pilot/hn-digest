# Zig Creator Calls Spade a Spade, Anthropic Blows Smoke

- Score: 1393 | [HN](https://news.ycombinator.com/item?id=48889637) | Link: https://raymyers.org/post/zed-creator-calls-spade-a-spade/

### TL;DR

The essay argues Anthropic framed Bun’s agent-driven port from Zig to unsafe Rust as proof of AI’s coding future while offering a one-sided technical rationale. It praises the staged file-by-file migration but says the explanation omitted tradeoffs, build costs, style-guide enforcement, testing alternatives, and management choices behind memory bugs. Its larger claim is that Rust’s safety machinery, readable code, and human judgment show agents remain insufficient. HN split over whether the rewrite sacrifices battle-tested code, creates unsafe boundaries, exposes Zig’s limitations, or was overshadowed by personal attacks and language-community politics.

### Comment pulse

- A successful transliteration is not a mature replacement → passing tests begins the rewrite’s production learning; it does not inherit years of battle-testing.
- Unsafe Rust can still improve direction → explicit unsafe boundaries create an incremental route toward stronger guarantees — counterpoint: current safety gains remain unproven.
- Leadership tone became technical risk → personal attacks made potential adopters question Zig’s community, while supporters considered management behavior essential causal context.

### LLM perspective

- **View:** AI makes rewrites cheaper, not self-justifying; decisions still need alternatives, measured tradeoffs, migration risks, and a maintenance model.
- **Impact:** Spectacular migrations influence language adoption before users know whether reliability, maintainability, or total engineering cost improved.
- **Watch next:** Production defects, conversion to safe Rust, build times, contributor productivity, and evidence separating rewrite effects from other optimizations.
