# A year of fighting scrapers on my 1.5 million-page website

- Score: 359 | [HN](https://news.ycombinator.com/item?id=49211386) | Link: https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/

### TL;DR

PatronView’s owner found server logs showing 1.28 million pages served in a week against 5,977 analytics pageviews—about 214 unobserved loads per visible one. After waves from hundreds of thousands of IPs, declared AI crawlers, cloud hosts, and residential proxies, he built Cloudflare rules that block low-value bots and challenge datacenters, stale browsers, and abnormal rates. Claude once fetched 35,000 pages per referred visitor; Amazon reached 117,000 daily requests. The rules reduced traffic with few human solves, but require continual tuning and motivate pay-per-crawl economics.

### Comment pulse

- Critics warned Cloudflare-based gatekeeping excludes legitimate scripts, JavaScript-disabled users, VPNs, old systems, and regions.
- Others recommended proof-of-work or cheaper hosting — counterpoint: determined headless and residential scrapers can absorb friction or mimic humans.
- Commenters distinguished occasional public-data collection from repeated industrial recrawling that externalizes infrastructure costs.

### LLM perspective

- View: Referral-adjusted crawl volume is a practical value metric, though not a universal access principle.
- Impact: Small publishers increasingly need edge defenses or must subsidize machine consumption.
- Watch next: Pay-per-crawl adoption, residential-proxy defenses, and false-positive measurements.
