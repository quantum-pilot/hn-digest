# Ex-GitHub CEO launches a new developer platform for AI agents

- Score: 272 | [HN](https://news.ycombinator.com/item?id=46961345) | Link: https://entire.io/blog/hello-entire-world/

- TL;DR  
Ex-GitHub CEO Thomas Dohmke launched Entire, a heavily funded ($60M seed) developer platform aimed at AI-agent-centric coding. Its first product is an open-source CLI that records “Checkpoints”: full AI session metadata linked to each Git commit on a separate branch, turning agent reasoning into queryable history. Supporters see clearer auditability and better handoffs for AI-generated code; skeptics argue it’s a thin Git extension, question venture-scale economics, and worry about bloated repos versus lighter summarised workflows.

- Comment pulse  
  - Capturing agent context with commits is useful → improves traceability, helps answer “why X not Y?”, and lets future AI prompts reuse original rationale.  
  - Skeptics: this is just storing extra text alongside Git commits, hardly worth $60M or a new platform— counterpoint: seed rounds fund these speculative platform bets.  
  - Others already log AI conversations via summaries or design docs and prefer concise, curated context over dumping full prompt transcripts into Git branches.

- LLM perspective  
  - View: Platformizing agent context is directionally right; implementation details and ergonomics will determine real adoption beyond hype.  
  - Impact: If it works, code review, compliance, and multi-agent collaboration workflows in large orgs could centralize around structured reasoning history.  
  - Watch next: Benchmark whether checkpoints meaningfully reduce token usage, review time, and defect rates versus existing practices like ADRs and manual prompt logs.
