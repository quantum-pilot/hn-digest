# Miasma: A tool to trap AI web scrapers in an endless poison pit

- Score: 275 | [HN](https://news.ycombinator.com/item?id=47561819) | Link: https://github.com/austin-weeks/miasma

- TL;DR  
  - Miasma is a small Rust server that returns “poisoned” text plus self-referential links, so AI scrapers sent to a hidden path (like /bots) loop endlessly on low-value data while normal users never see it. You deploy it behind Nginx and exempt legit bots via robots.txt. Hacker News likes the symbolism but doubts impact: critics note SEO risks, whack‑a‑mole dynamics, and that many real crawlers won’t follow hidden links, suggesting rate limits or LLM‑friendly mirrors instead.

- Comment pulse  
  - Poison pit as guerilla tactic → Can waste scrapers’ resources and deter “unprofitable” targets — counterpoint: hidden links violate policies and can damage search ranking.  
  - Anti-scraper tricks resemble copy-protection whack‑a‑mole → Arms race entertains adversaries, consumes maintainer time, and risks harming availability of the legitimate site.  
  - Scraping seen less as “theft” than misuse → Main issue is overload and unwanted model training; some prefer rate limits or LLM‑friendly mirrors over poisoning.

- LLM perspective  
  - View: Clever protest tool but limited coverage; many serious scrapers ignore hidden links or constrain crawl depths, reducing trapping effectiveness.  
  - Impact: Likely most useful for small sites targeting specific abusive crawlers; overuse risks SEO loss and maintenance distraction for publishers.  
  - Watch next: Standardized “AI training allowed/forbidden” protocols plus server-side rate‑limiting and legal frameworks will matter more than ad‑hoc poisoning scripts.
