# If you are good at code review, you will be good at using AI agents

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45310529) | Link: https://www.seangoedecke.com/ai-agents-and-code-review/

- TL;DR
  - The post argues AI coding agents behave like eager juniors: fast, but weak judgment. To get value, apply structural code review—question the approach, reuse existing systems, and interrupt over-engineering. “Vibe coding” stalls without this. The effective pattern today is centaur programming: human architectural judgment + machine throughput under close supervision. HN debates whether QC-after-the-fact can tame high-error agents, implications for juniors and OSS trust, and shares workflows ranging from heavy test guardrails to tight, stepwise supervision.

- Comment pulse
  - Build quality into process: LLMs are high-defect; use Deming-style guardrails, tests, constraints over QA—counterpoint: controlled C-to-Go translations with ported test suites can be acceptable.
  - Juniors risk floundering: mandated agent use without experience erodes mentorship and their ability to assess design; OSS loses educational value when unreviewed AI code lands.
  - Agent workflows often slower: effective patterns are small, interruptible tasks, autocomplete, and stepwise supervision; treat agents like erratic mid-levels you edit heavily.

- LLM perspective
  - View: Use agents for volume, keep humans on architecture; codify 'structural review' as prompts, checklists, and stop/redirect criteria.
  - Impact: Raises leverage of strong reviewers; widens gap for juniors; OSS may shift toward test-backed bulk ports over granular line review.
  - Watch next: Benchmark agent workflows vs humans on cost/defects; release translation pipelines; set org gates: coverage thresholds, review scope, permitted agent tasks.
