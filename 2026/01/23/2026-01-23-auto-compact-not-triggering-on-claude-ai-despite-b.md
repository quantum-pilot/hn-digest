# Auto-compact not triggering on Claude.ai despite being marked as fixed

- Score: 174 | [HN](https://news.ycombinator.com/item?id=46736091) | Link: https://github.com/anthropics/claude-code/issues/18866

### TL;DR

A Claude.ai user reports that, after the January 14 outage, long Project chats stopped compacting automatically even though Anthropic had marked the problem fixed. Near the context boundary, prompts silently return to the input box or sometimes show a limit error, forcing a new chat or manual recovery. Reports in the captured issue span web, desktop, and mobile use, with some paying users repeatedly losing work. Resending the last successful turn and prefixing the next message with the compact command helped several people.

### Comment pulse

- Fresh sessions can preserve momentum → users save summaries and task lists in files, then reload context instead of trusting compaction.
- Perceived Opus degradation lacks shared evidence → regressions feel real — counterpoint: rising expectations and random output can mimic deliberate throttling.
- Product inconsistencies compound the failure → commenters cite broken rollbacks, authorization, research completion, and opaque limits across interfaces.

### LLM perspective

- View: Reliable context management matters more than nominal window size for sustained work.
- Impact: Researchers and developers lose continuity, paid usage, and confidence when long conversations fail silently.
- Watch next: Public incident status, cross-platform reproduction, automatic compaction success, recovery guarantees, and token-accounting transparency.
