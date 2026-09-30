# Livenerf: Has Opus 5.5 been nerfed yet?

- Score: 717 | [HN](https://news.ycombinator.com/item?id=49901736) | Link: https://github.com/ninjahawk/livenerf

### TL;DR

Livenerf is a preregistered, append-only benchmark designed to detect post-launch capability drift in Opus 5.5 as served through a Claude subscription. It freezes prompts, graders, CLI, and harness while repeatedly testing 78 variably answered questions and tracking accuracy plus output tokens. As of September 29, only six of 30 days had run, all within the 10-day baseline; collection began 2.5 days after launch. No degradation conclusion is possible, and the first results row appears after day 20.

### Comment pulse

- Perceived nerfs often reflect rising expectations or randomness → users report complaints even when serving stacks remain unchanged.
- Temporary regressions remain plausible → commenters cite infrastructure incidents, load variation, and subscription-only anecdotes.
- Cross-provider comparisons could isolate serving changes → independently hosted weights might distinguish model drift from Anthropic’s subscription path.

### LLM perspective

- View: Preregistration converts recurring anecdotes into a falsifiable test, but its scope is deliberately narrow.
- Impact: Users gain evidence about one subscription serving path, not the raw API model or every workflow.
- Watch next: Await both post-baseline windows, token shifts, control-arm movement, and the preregistered 99% decision rule.
