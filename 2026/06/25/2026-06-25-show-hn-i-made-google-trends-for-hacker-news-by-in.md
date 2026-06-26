# Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

- Score: 637 | [HN](https://news.ycombinator.com/item?id=48673671) | Link: https://hackernewstrends.com

### TL;DR
A developer built a “Google Trends for Hacker News” that indexes ~18 years of HN posts and comments, plotting how often terms appear over time. It looks like Google Trends but measures written discussion, not search queries, so it reflects what HN talks about, not what people search for. Commenters point to an existing real-time public ClickHouse HN dataset, debate whether the “Google Trends” analogy is misleading, note licensing concerns, report scaling/timeouts and rate limits, and spot (then see fixed) a date-range bug.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Public HN data lake exists → ClickHouse host offers a real-time, queryable HN dataset; one user objects on licensing grounds per HN terms.  
- “Google Trends” analogy overpromises → counts of posts/comments differ from search intent; visual similarity risks misinterpretation — counterpoint: in practice, topic curves resemble Google Trends and are still useful.  
- Scaling issues surfaced → API returns 502/504 errors and rate limits Upstash, plus a comparison-view bug; author reportedly fixes at least the truncation issue.

---

### LLM perspective
- View: Treat this as a discourse-trends tool—closer to Google Ngram for HN than to genuine search analytics.  
- Impact: Valuable for studying hype cycles, community interests, and historical context around technologies and companies on HN.  
- Watch next: Open methodology, exportable datasets, and more robust infra (caching, precomputed aggregates) will determine long-term utility and reliability.
