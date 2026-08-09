# Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

- Score: 289 | [HN](https://news.ycombinator.com/item?id=47920787) | Link: https://github.com/dirac-run/dirac

### TL;DR

Dirac is an Apache-licensed Cline fork that curates coding-agent context through AST-derived file skeletons, hash-anchored edits, batched multi-target tools, and opportunistic context updates. Using Gemini 3 Flash Preview with high reasoning, it scored 65.2% on Terminal-Bench 2, above Google’s 47.6% baseline and Junie’s 64.3%, while its eight-task refactoring suite reports 8/8 successes at $0.18 average cost. Hacker News found the harness gains compelling but requested cross-model and latency tests, questioned anchor-token savings and parser coverage, and flagged default telemetry, hourly feature polling, and web requests routed through Dirac servers.

### Comment pulse

- Same-model gains suggest harness design matters, but leaderboard comparisons should span full model–harness combinations and account for benchmark optimization.
- Batching lists within tools may reliably induce parallelism where weaker models avoid issuing concurrent calls.
- Telemetry sends machine IDs, usage, and error snippets — counterpoint: the author says inherited Cline behavior stores no PII.

### LLM perspective

- **View:** Efficient context selection may matter more than edit syntax; isolating each optimization would show causal value.
- **Impact:** Lower token usage makes capable agents viable with cheaper models and repeated repository-scale work.
- **Watch next:** Independent reproductions, diverse model families, wall-clock latency, telemetry defaults, parser fallbacks, and corrected cache pricing.
