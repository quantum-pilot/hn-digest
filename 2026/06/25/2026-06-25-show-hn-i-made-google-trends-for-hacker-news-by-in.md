# Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

- Score: 637 | [HN](https://news.ycombinator.com/item?id=48673671) | Link: https://hackernewstrends.com

### TL;DR

Hacker Trends indexes 45 million Hacker News posts and comments across 18 years, letting users chart and overlay mentions of tools, people, or ideas, then inspect the underlying discussions by date, term, or author. It runs live date histograms on Upstash Redis Search and includes many curated comparisons. HN liked the exploration but warned that mention frequency measures published discourse, not search intent, so it should not be interpreted exactly like Google Trends. Launch traffic triggered timeouts, rate limits, and one quickly fixed date-range bug.

### Comment pulse

- Metric choice shapes conclusions → search demand includes routine needs, while HN mentions emphasize newsworthy subjects and discussion intensity.
- The proxy remains useful for zeitgeist shifts → commenters found some term crossovers resembled Google Trends despite measuring different behavior.
- Public data invites reuse and consent questions → a ClickHouse corpus enables SQL alternatives — counterpoint: one user challenged redistribution under HN terms.

### LLM perspective

- **View:** This is a corpus-frequency explorer: strongest for attention cycles, weakest when treated as evidence of demand, adoption, or sentiment.
- **Impact:** Researchers and developers gain an interface for finding when technical narratives emerged and retrieving the conversations behind each spike.
- **Watch next:** Add normalization for corpus growth, distinct-user counts, post-versus-comment controls, uptime metrics, and an explicit methodology page.
