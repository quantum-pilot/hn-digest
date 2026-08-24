# Speed up responses with fast mode

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46926043) | Link: https://code.claude.com/docs/en/fast-mode

### TL;DR

Claude Code’s research-preview fast mode runs the same Opus 4.6 model through a lower-latency, higher-cost configuration, toggled with `/fast`. Pricing starts at $30 per million input tokens and $150 per million output tokens below 200K context, doubling input cost above that threshold. It always bills as extra usage, requires account or admin enablement, excludes third-party clouds, and falls back to standard speed when separately rate-limited. Switching mid-conversation can rebill the whole uncached context at fast rates. Commenters questioned the speed premium and requested an inverse, delay-tolerant discount for background jobs.

### Comment pulse

- One commenter estimated 2.5× throughput for six times the price, judging the latency premium difficult to justify against cheaper competitors.
- Subscribers cannot spend included quotas on fast mode; every token uses extra billing, even when normal allowance remains.
- Readers wanted the opposite option: queue nonurgent agents for idle capacity at reduced prices—counterpoint: providers may prefer monetizing scarce latency.

### LLM perspective

- View: Fast mode prices human waiting time explicitly; its value depends on whether saved minutes exceed marginal token costs.
- Impact: Interactive debugging accelerates for well-funded users; autonomous tasks remain economically better suited to standard throughput.
- Watch next: Latency distributions, quality parity, context rebilling, rate-limit fallbacks, controls, post-preview pricing, competitor responses, and queued discount tiers.
