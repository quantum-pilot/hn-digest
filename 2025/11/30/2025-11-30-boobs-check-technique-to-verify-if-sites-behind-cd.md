# "Boobs check" – Technique to verify if sites behind CDN are hosted in Iran

- Score: 155 | [HN](https://news.ycombinator.com/item?id=46100323) | Link: https://twitter.com/hkashfi/status/1995109785679573167

### TL;DR

An operator proposes requesting a deliberately censored image path through a site's CDN. A 403 response containing a 10.10.34.x address is presented as evidence that the origin sits inside Iran, where filtering intercepts the upstream request. The method cannot reveal a path through ordinary end-to-end TLS; commenters said its result depends on how the CDN reaches and trusts the origin. No test site appeared, so the technique remains a conditional heuristic rather than a hosting detector.

### Comment pulse

- TLS termination is decisive → visitor-to-CDN encryption does not protect a plain-HTTP origin leg, while local trust infrastructure may enable interception.
- The signal has compliance and provenance uses → readers cited sanctions screening and identifying Iranian-hosted sites, while admitting motives were uncertain.
- Reproducibility remains weak → requests for a working sample received jokes rather than verified evidence.

### LLM perspective

- View: The check detects censorship behavior, not geography directly.
- Impact: CDN configurations can unintentionally expose an origin's regulatory environment.
- Watch next: Controlled tests across Iranian origins, TLS modes, CDNs, and certificate chains.
