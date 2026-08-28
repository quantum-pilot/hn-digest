# Ban me at the IP level if you don't like me

- Score: 599 | [HN](https://news.ycombinator.com/item?id=45010183) | Link: https://boston.conman.org/2025/08/21.1

### TL;DR

A site operator reports that a crawler identifying itself as Thinkbot ignored `robots.txt` and told administrators to block its IP if troublesome. During one month it used 74 addresses across 41 network blocks, all attributed by the author to Tencent. The author responded by blocking those ranges, covering nearly 476,600 addresses, while explicitly labeling speculation about Chinese state motives as “tin foil hat” conjecture. The episode illustrates why distributed crawlers make address-level blocking blunt and expensive, especially when operators lack a stable contact or documented bot policy.

### Comment pulse

- A crawler developer described treating a timed-out `robots.txt` as a site-wide disallow rule.
- Operators reported bots consuming bandwidth, cache capacity, connections, and expensive dynamically generated pages.
- Others warned that endless blocklist maintenance can cost more than tolerating harmless crawling.

### LLM perspective

- View: A bot that shifts addresses while delegating blocking costs is not offering meaningful operator control.
- Impact: Broad ASN blocks reduce load but risk collateral denial for unrelated users and services.
- Watch next: Prefer stable identity, rate limits, contact metadata, conservative robots handling, and workload-specific defenses.
