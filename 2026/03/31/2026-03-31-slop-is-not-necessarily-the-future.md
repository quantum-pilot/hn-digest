# Slop is not necessarily the future

- Score: 163 | [HN](https://news.ycombinator.com/item?id=47587953) | Link: https://www.greptile.com/blog/ai-slopware-future

### TL;DR

Greptile argues AI-generated “slop” is a transitional phase, not software’s endpoint: simple, modifiable code consumes less context, compute, and tokens, so competition should eventually reward models that maintain it well. Its 2025 data show code per developer rising from 4,450 to 7,839 lines and median PR size increasing 33%, alongside a cited rise in outages. HN largely accepted the complexity risk but challenged the product-versus-craft framing, arguing internal quality becomes customer-visible through reliability, performance, maintainability, and response speed—especially in infrastructure and concurrent systems.

### Comment pulse

- Removing code-writing throughput as a bottleneck may expose nonlinear design and maintenance costs before better tooling catches up.
- Current agents lack an explicit design-level representation beyond prompts and code; commenters asked whether useful intermediate representations are being developed.
- “Build only what must last” appealed to some — counterpoint: software teams rarely agree which qualities are luxury versus baseline safety.

### LLM perspective

- **View:** Token efficiency may favor simplicity, but per-output vendors need incentives aligned with lifecycle cost rather than generation volume.
- **Impact:** Teams adopting agents fastest will shift scarce effort from typing toward architecture, review, observability, and deletion.
- **Watch next:** Longitudinal defect rates, maintenance-token spend, rollback frequency, codebase growth, and benchmarks that reward small correct patches.
