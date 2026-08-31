# Creepy Crawlies

- Score: 1258 | [HN](https://news.ycombinator.com/item?id=49491791) | Link: https://people.kernel.org/monsieuricon/creepy-crawlies

### TL;DR

The git.kernel.org operator reports roughly six million daily requests for random commit pages, estimating legitimate traffic at only about 2%. Although repositories and mailing-list archives are directly clonable, crawlers repeatedly render duplicated commits across hundreds of forks and combinatorial cgit URLs. Anubis proof-of-work rejects 66% of requests, yet one-third now solve it; scraper rendering continuously consumes 14–16 of 90 CPU cores across five nodes. Operators are disabling expensive anonymous features while keeping bulk data downloadable, because residential-proxy traffic defeats simple IP blocking.

### Comment pulse

- Critics argued proof-of-work favors optimized bots over mobile users and cannot sustain a long-term advantage.
- Defenders countered that rejecting two-thirds of requests still provides useful relief, even if temporary.
- Other operators reported similar indiscriminate crawling, including residential-IP rotation and enormous bursts against small code hosts.

### LLM perspective

- View: This is primarily a protocol-selection failure: crawlers ignore efficient bulk access and externalize rendering costs.
- Impact: Open services lose anonymous functionality as defensive friction becomes cheaper than subsidizing abusive retrieval.
- Watch next: Whether crawler operators adopt repository-aware ingestion or defenses shift from proof-of-work to access pricing.
