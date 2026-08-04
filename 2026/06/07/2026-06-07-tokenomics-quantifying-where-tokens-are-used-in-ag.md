# Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering

- Score: 165 | [HN](https://news.ycombinator.com/item?id=48430923) | Link: https://arxiv.org/abs/2601.14470

### TL;DR

An arXiv study analyzes token use across 30 ChatDev software tasks run with a GPT-5 reasoning model. Mapping traces to design, coding, completion, review, testing, and documentation, it finds iterative code review consumes 59.4% of tokens on average, while input accounts for 53.9%, suggesting refinement and verification—not initial generation—drive agentic engineering cost. HN anecdotes reported even more input-heavy workloads, unexpected 250,000-token queries, and wasteful test loops. Commenters proposed better code navigation, cached compacted context, deterministic checks, and explicit testing requirements, while questioning unstable pricing and provider incentives.

### Comment pulse

- Context overhead → One practitioner sees roughly 10:1 input-to-output usage, with agents rereading huge repositories for tiny patches.
- Optimization → ASTs, language servers, documentation, prefix caching, and one-time compaction could reduce repeated context ingestion across parallel subagents.
- Verification quality → Agents may generate many semantically flawed unit tests — counterpoint: teams can require broader dynamic validation during planning.

### LLM perspective

- **View:** Token efficiency is largely workflow efficiency; repeated context and unconstrained review loops dominate avoidable spend.
- **Impact:** Teams need stage-level budgets and quality gates before multi-agent systems become financially predictable.
- **Watch next:** Replicate across frameworks, repositories, models, task difficulty, cache pricing, defect rates, latency, and energy use.
