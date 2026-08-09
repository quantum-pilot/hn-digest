# Miasma: A tool to trap AI web scrapers in an endless poison pit

- Score: 275 | [HN](https://news.ycombinator.com/item?id=47561819) | Link: https://github.com/austin-weeks/miasma

### TL;DR

Miasma is a small GPL-licensed Rust server that sends suspected scrapers poisoned text plus several self-referential links, aiming to trap crawlers in an endless synthetic-content loop. A site can hide links to a proxied `/bots` route, cap concurrent requests, return 429 beyond the limit, gzip responses, and exempt friendly crawlers through `robots.txt`. HN questioned both efficacy and collateral damage: capable bots may ignore hidden links, search engines may punish deceptive markup, and defenders could spend more effort than attackers. Others argued automated resource consumption can still deter abusive crawlers.

### Comment pulse

- Hidden `display:none` links may be skipped by simple parsers and rendered agents alike, undermining the advertised trap.
- Google can penalize hidden deceptive links — counterpoint: sites rejecting large search indexes may accept that outcome.
- For many publishers the urgent harm is bandwidth exhaustion, not model training or whether copying public text counts as theft.

### LLM perspective

- **View:** A tarpit works only when detection is accurate and the scraper’s crawl policy follows the bait.
- **Impact:** Small sites may trade bandwidth protection and protest value for SEO, accessibility, and operational risk.
- **Watch next:** Crawler identification, egress costs, search penalties, false positives, loop duration, poisoning evidence, and comparison with rate limits.
