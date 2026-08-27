# Claude Sonnet 4.5

- Score: 1211 | [HN](https://news.ycombinator.com/item?id=45415962) | Link: https://www.anthropic.com/news/claude-sonnet-4-5

### TL;DR

Anthropic presents Sonnet 4.5 as a stronger coding, agent, computer-use, reasoning, and alignment model at Sonnet 4 pricing: $3 per million input tokens and $15 per million output tokens. It reports 77.2% on SWE-bench Verified, 61.4% on OSWorld, and focus lasting over 30 hours, alongside checkpoints, context tools, a VS Code extension, file creation, and the Claude Agent SDK. HN experiences varied sharply: some praised complex refactors, while others saw superficial, untested implementations and benchmark-task mismatches.

### Comment pulse

- Real-world results conflicted → users alternately ranked Sonnet above or below GPT-5-Codex, often from single tasks and different prompts.
- Long autonomy lacks context → commenters said 30-hour runs reveal little without tooling, token volume, guardrails, tests, and output-quality evidence.
- Benchmarks miss simple failures → improved aggregate scores coexist with ignored instructions, missing tests, and regressions on ordinary edits.

### LLM perspective

- View: The release improves the agent stack, but vendor benchmarks cannot predict reliability on a specific repository.
- Impact: Teams gain longer-running workflows without escaping prompt design, verification, cost, and nondeterminism.
- Watch next: Repeated independent trials, long-task artifact quality, instruction adherence, service consistency, false-positive classifiers, and production defect rates.
