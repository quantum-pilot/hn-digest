# I-have-ADHD: A skill to stop coding agents from burying the answer

- Score: 465 | [HN](https://news.ycombinator.com/item?id=49610631) | Link: https://github.com/ayghri/i-have-adhd

### TL;DR

The i-have-ADHD project is an MIT-licensed agent skill and plugin that enforces action-first, concise responses: numbered steps, one next action, limited lists, visible progress, minimal tangents, and no preambles or closers. Its repository claims 32,600 stars, multiple harness integrations, tests, and evaluation tooling; the name describes an output preference rather than requiring a diagnosis. Commenters liked the goal but argued the example removed useful explanation, reported that models forget style rules over long sessions, and raised supply-chain concerns about agent-directed installation.

### Comment pulse

- Some preferred verbosity that explains causes over terse instructions that encourage blind execution.
- Users reported Claude-specific verbosity and rule decay — counterpoint: output styles or stop hooks may enforce concision more reliably.
- Copy-pasting repository installation prompts worried commenters because agents may fetch and execute unreviewed or misidentified code.

### LLM perspective

- View: Concision is valuable only when it preserves rationale, warnings, and enough state for informed decisions.
- Impact: Users gain scannable actions, but overcompression can obscure risk and reduce learning.
- Watch next: Long-session adherence, task-completion evals, security review, configurable detail levels, and comparison with native output styles.
