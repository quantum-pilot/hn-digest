# Vibe coding cleanup as a service

- Score: 220 | [HN](https://news.ycombinator.com/item?id=45320431) | Link: https://donado.co/en/articles/2025-09-16-vibe-coding-cleanup-as-a-service/

- TL;DR
  - The article argues that “vibe coding” (AI-generated code by prompt) ships fast but is brittle at scale—driving a new market for cleanup specialists who refactor, secure, and productionize AI-built MVPs. Cited evidence: higher churn, more vulns, architectural drift, and “competency debt.” Proposed model: AI for prototypes; humans for design, tests, and hardening. HN largely agrees demand for rescues is real, debates whether vibe coding was misinterpreted hype, and weighs MVP speed versus long-term maintainability, with some touting plan-first LLM workflows.

- Comment pulse
  - “Vibe coding” was a joke/experiment, not production guidance → misread due to hype; still, many now use AI to ship fast — counterpoint: it’s just AI assistance, stop sneering.
  - Rescue consultants: same chaos as outsourcing, just more volume → plan mode and sign-off diffs improve outcomes; sustainability needs specs, tests, docs, ownership.
  - Speed wins early-stage → traction justifies cleanup; risk: prototypes ossify into prod; consider no-code/spec tools to prevent debt from becoming architecture.

- LLM perspective
  - View: Treat AI as a junior; require plan reviews, diff approvals, tests, and security gates; budget cleanup explicitly.
  - Impact: New “AI code remediation” roles, marketplaces, and product-spec pipelines; architects gain leverage, juniors upskill via cleanup.
  - Watch next: Measurables on churn/vuln rates; IDE “plan mode” defaults; enterprise policies for AI-origin tagging and refactor SLAs.
