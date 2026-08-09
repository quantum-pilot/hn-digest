# An update on recent Claude Code quality reports

- Score: 525 | [HN](https://news.ycombinator.com/item?id=47878905) | Link: https://www.anthropic.com/engineering/april-23-postmortem

### TL;DR

Anthropic says three product-layer changes—not the API or inference stack—caused recent Claude Code degradation: a default effort cut from high to medium, a bug that repeatedly discarded older reasoning after an hour-idle session, and a terse system-prompt instruction that reduced an evaluation score by 3%. The changes were reversed or fixed by April 20, and subscriber limits were reset. Readers welcomed the unusually specific postmortem but questioned whether cost pressure motivated context pruning and reported continuing Opus 4.7 oddities beyond the identified incidents.

### Comment pulse

- Long-session users expect persistent coworker-like memory — counterpoint: full cache rewrites after idle can consume substantial limits without pruning.
- Stochastic results complicated diagnosis: identical settings produced excellent and poor plans, while retries multiplied expense.
- Reports of models answering internal instructions or ignoring hooks suggest prompt-layer behavior still merits targeted reproduction.

### LLM perspective

- Version and expose every default, context transformation, and system-prompt revision in a per-session audit log.
- Add regression tests that resume stale, tool-using sessions and compare retained causal context turn by turn.
- Track public-build quality by cohort; aggregate averages conceal narrow regressions affecting specific workflows.
