# Agents need control flow, not more prompts

- Score: 292 | [HN](https://news.ycombinator.com/item?id=48051562) | Link: https://bsuh.bearblog.dev/agents-need-control-flow/

### TL;DR

The essay argues complex agents become reliable by moving orchestration out of prose and into deterministic software. Prompts are probabilistic, weakly specified, and non-composable; emphatic instructions cannot guarantee sequencing or truthful success. Explicit state transitions, validation checkpoints, and programmatic error detection should surround the LLM as one component. Otherwise teams must babysit every step, exhaustively audit outputs, or accept failures blindly. Commenters report prompt-managed loops missing or repeating work after dozens of items, while simple harnesses that iterate tasks, persist results, and invoke narrow model judgments work far better.

### Comment pulse

- A QA workflow became reliable only after code enumerated 200 requirement files and called the model once per test.
- Teams use models to write parsers, generators, and reusable tools, leaving runtime AI mainly for ambiguous interpretation and failure repair.
- Managed platforms were criticized for privileging autonomous prompting — counterpoint: context compaction and persistent task lists sometimes help long runs complete.

### LLM perspective

- Place determinism outside model decisions and inside tools; validation should reject malformed actions before execution.
- Human review remains essential for irreversible customer mutations, even when AI prepares compliant commands.
- Measure omission, duplication, retry, and recovery rates as task count grows—not just final-answer quality.
