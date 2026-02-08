# Orchestrate teams of Claude Code sessions

- Score: 387 | [HN](https://news.ycombinator.com/item?id=46902368) | Link: https://code.claude.com/docs/en/agent-teams

### TL;DR
Anthropic’s new Claude Code “Agent Teams” feature lets multiple Claude coding agents work in parallel under a coordinator, speeding up large code changes and tests while multiplying token usage. HN sees it as the inevitable native version of orchestrators like Gas Town and other multi-agent setups, conceptually similar to classic actor frameworks. Discussion focuses on whether this is genuinely new, how well it works in practice, and whether the productivity gains justify higher costs and subscription limits.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Multi-agent orchestrators are “obvious” and long-predicted → many built similar systems already, drawing parallels to Akka-style actor trees and earlier Gas Town experiments — counterpoint: Anthropic still validates and productizes the pattern.

- Performance vs. cost → real-world example: 4 agents cut a 50k‑LOC FastAPI task from ~20 to ~6 minutes but cost ~4× tokens; best for short bursts, not continuous use.

- Design and UX → Claude’s Agent Teams are simpler and less whimsical than Gas Town (leader + workers, fewer roles), closer to how users were already manually spawning sub-sessions to avoid context loss.

---

### LLM perspective
- View: Native agent orchestration inside coding tools was inevitable; the novelty is polish, guardrails, and integration, not the underlying coordination idea.

- Impact: Most useful for teams with expensive engineers and sizeable codebases; solo devs feel token burn more acutely than time savings.

- Watch next: Benchmarks on quality/regressions, better conflict-aware file planning, open-source orchestrators, and clearer pricing/quota models for multi-agent workloads.
