# Messing with scraper bots

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45935729) | Link: https://herman.bearblog.dev/messing-with-bots/

### TL;DR

Instead of merely rejecting abusive crawlers, the author built efficient decoy endpoints that serve endless public-domain prose or plausible-looking PHP from memory. Branching links can occupy rule-breaking scrapers, while fake PHP responses target bots probing for vulnerable WordPress installations. The experiment uses noindex and nofollow but remains isolated from important sites because search engines might still classify the content as spam. The author ultimately recommends conventional 403 responses for serious sites, noting bandwidth costs and uncertainty about whether vulnerability scanners even read response bodies.

### Comment pulse

- Commenters shared older countermeasures that quietly polluted scraper data or detected bots through inconsistent browser headers.
- Critics argued PHP probes may only inspect status or fingerprints, making generated payloads less efficient than blocking tools.

### LLM perspective

- View: Deception is entertaining, but cheap rejection remains the safer default for resource-asymmetric bot traffic.
- Impact: Honeypots can gather insight yet also waste bandwidth, risk indexing penalties, and reveal detection logic.
- Watch next: Measure whether suspect clients consume bodies before investing in elaborate decoy generation.
