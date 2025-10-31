# Feed the bots

- Score: 301 | [HN](https://news.ycombinator.com/item?id=45711094) | Link: https://maurycyz.com/misc/the_cost_of_trash/

- TL;DR
  - A blogger built an “infinite nonsense” endpoint to absorb LLM scrapers that ignore robots.txt, rotate IPs, and hammer servers. Traditional defenses (blocks, rate limits, paywalls/CAPTCHAs, ZIP-bombs, fake 404s) either fail or harm users. Serving static pages is bandwidth/disk-bound; instead, a tiny Markov generator serves junk in ~60 microseconds/request using ~1.2 MB RAM with no disk I/O, making bot traffic tolerable. HN debates effectiveness, code safety, and the economics; widespread adoption could force scrapers to pre-filter or pay for cleaner data.

- Comment pulse
  - Garbage-flooding raises costs if many sites join → network, storage, and pre-filtering add up — counterpoint: LLMs cheaply filter junk; models already ingest noise.
  - Markov babbler is tiny and fast → but code has pthread_detach misuse, unsafe C, unbounded threads; sandbox or container recommended.
  - Shared Basic Auth credentials stop users more than bots → trivially bypassed; only effective while obscure.

- LLM perspective
  - View: Garbage traps push scrapers toward content provenance, deduplication, and on-crawl classification, shrinking free crawling.
  - Impact: Scrapers invest in pre-filtering, storage audits, or licensed datasets; small sites gain negotiating leverage via block-or-poison tactics.
  - Watch next: Open-source junk-page detectors, trap honeypot lists, and policies or lawsuits clarifying robots.txt and opt-out enforcement.
