# Issue: Claude Code is unusable for complex engineering tasks with Feb updates

- Score: 711 | [HN](https://news.ycombinator.com/item?id=47660925) | Link: https://github.com/anthropics/claude-code/issues/42796

### TL;DR

A GitHub issue argues that Claude Code’s complex-engineering quality collapsed after February. Mining 6,852 sessions, 17,871 thinking blocks, and 234,760 tool calls, its author correlated shorter apparent reasoning with reads per edit falling from 6.6 to 2.0, edits without recent reads rising from 6.2% to 33.7%, and 173 premature-stop violations after March 8. Anthropic replied that redaction only hides thoughts; adaptive thinking and a medium effort default changed behavior, with high/max controls available. Users reported similar symptoms, but the report’s causal attribution remains disputed.

### Comment pulse

- The reporter says max effort and disabled adaptive thinking did not restore quality, alleging subscription-side, load-sensitive rationing that Anthropic has not acknowledged.
- Other users recognized “simplest fix,” premature wrap-up, ignored failures, and instruction reversals — counterpoint: anecdotes span different providers, models, settings, and outages.
- Critics noted the irony of trusting the allegedly impaired model to analyze its own logs; supporters credited the surrounding observability pipeline.

### LLM perspective

- **View:** The dataset documents a regression signal convincingly, but signature length and timing correlations do not isolate its cause.
- **Impact:** Inconsistent agents erase automation gains by forcing exhaustive review, especially across concurrent, long-running sessions with broad write access.
- **Watch next:** Controlled subscription-versus-API experiments, fixed prompt suites, explicit effort telemetry, change logs, and Anthropic reproduction across identical harnesses.
