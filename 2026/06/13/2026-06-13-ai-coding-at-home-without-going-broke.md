# AI coding at home without going broke

- Score: 344 | [HN](https://news.ycombinator.com/item?id=48518969) | Link: https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/

### TL;DR

Home AI coding has three cost strategies: buy hardware and self-host, rent open models by API, or exploit heavily discounted frontier subscriptions. The author recommends combining the latter two: reserve OpenAI and Anthropic plans for difficult reasoning and specifications, then give mechanical implementation to metered open models, targeting roughly $1,000 for a month of twenty-engineer-equivalent output. HN commenters disputed the assumed usage pattern, noting many professional workflows never exhaust modest plans, while high parallelism, broad agent access, privacy needs, and unattended pipelines can materially change the economics.

### Comment pulse

- Modest plans can be sufficient → iterative, human-reviewed work rarely needs overnight generation — counterpoint: ten parallel agents and automated feedback loops consume far more.

- Self-hosting buys privacy and control → electricity and hardware remain costs, but durable high-memory GPUs, resale value, or existing machines soften depreciation.

- API pricing reduces commitment → DeepSeek users reported very low spend, while enterprise zero-data-retention plans can cost vastly more than subsidized consumer subscriptions.

### LLM perspective

- **View:** Cost optimization starts with measuring useful completed work per dollar, not maximizing token volume or keeping agents perpetually busy.

- **Impact:** Solo developers gain flexible capacity, but review attention and task definition remain the binding constraints for reliable output.

- **Watch next:** Compare identical projects across local, open-model API, and subscription workflows, including power, review time, failures, and resale value.
