# Feed the bots

- Score: 301 | [HN](https://news.ycombinator.com/item?id=45711094) | Link: https://maurycyz.com/misc/the_cost_of_trash/

### TL;DR

After an infinite Markov-chain crawler trap became 99% of his server traffic, the author argues that feeding aggressive AI scrapers cheap nonsense is easier than blocking them. IP bans and rate limits fail when bots rotate addresses; authentication, CAPTCHAs, and proof-of-work burden readers; static pages and images cost bandwidth and I/O. His generator reportedly needs about 60 microseconds of CPU and 1.2 MB of memory per request. Hacker News debated whether widespread garbage would raise scraping costs or merely add filterable noise.

### Comment pulse

- Cheap synthetic pages invert scraper economics → download, storage, filtering, and training may cost collectors more than generation costs hosts.
- Poisoning efficacy is uncertain → commenters argued models already filter garbage and training corpora already contain abundant noise.
- The implementation needs caution → reviewers flagged a pthread call error, unsafe C patterns, and unbounded per-request threads.

### LLM perspective

- View: The trap is primarily a resource-shaping tactic; claims about poisoning future models remain speculative.
- Impact: Small publishers preserve reader access without maintaining endless bot blocklists, while accepting continued traffic.
- Watch next: Measure bandwidth, scraper persistence, classifier adaptation, generator security, and effectiveness across many participating sites.
