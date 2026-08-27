# A postmortem of three recent issues

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45281139) | Link: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues

### TL;DR

Anthropic attributes intermittent Claude degradation from August into September to three overlapping infrastructure bugs: Sonnet 4 requests routed to inappropriate one-million-token servers, TPU output corruption from a runtime optimization, and an XLA approximate-top-k miscompilation. Sticky routing amplified some users’ exposure, while platform differences, noisy evaluations, and privacy limits complicated diagnosis. Fixes included corrected routing, rollbacks, exact top-k with higher precision, new character-corruption tests, continuous production evaluations, and better feedback-debugging tools. These details are Anthropic’s own postmortem.

### Comment pulse

- Users welcome the disclosure but question service reliability, status-page completeness, and whether all degradation has been found.
- Anthropic says a feedback modal explicitly warns that submitting a thumbs-down report sends the entire conversation.

### LLM perspective

- View: Model quality is partly a distributed-systems property; correct weights cannot compensate for faulty routing, sampling, or compiler behavior.
- Impact: Intermittent, platform-specific degradation undermines benchmarks and makes customers doubt whether changed behavior is their prompt or infrastructure.
- Watch next: Whether production evals detect subtle regressions earlier and Anthropic reports measurable reductions in recurrence and remediation time.
