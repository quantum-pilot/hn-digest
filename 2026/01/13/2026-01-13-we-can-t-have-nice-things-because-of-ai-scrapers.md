# We can't have nice things because of AI scrapers

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46608840) | Link: https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/

TL;DR  
Anubis is a JavaScript proof‑of‑work gate meant to slow AI and bulk scrapers that overload small sites, forcing them to close or lock down. It makes each visit cheap for humans but expensive at crawler scale, as a stopgap until better bot fingerprinting exists. HN commenters zoom out to a coordination problem: how to give LLMs standardized, low‑impact access to text (dumps, new /.well-known/ files, national datasets) without wrecking privacy, copyrights, or the open web.

Comment pulse
- AI scraping is a coordination failure → sites would rather publish dumps or /well-known metadata like “llms.txt” than endure abusive crawlers.
- Bot shields like Cloudflare or Anubis protect fragile sites → but centralize gatekeeping and break VPN or nonstandard browsers. — counterpoint: admins accept this tradeoff.
- Others blame misaligned incentives, not tech → propose national training datasets, shorter copyrights, and paid, cleaned corpora instead of wasteful adversarial scraping.

LLM perspective
- View: Proof‑of‑work gates are reasonable short‑term friction but harm accessibility; long‑term, standardized opt‑in data feeds seem healthier.
- Impact: Small volunteer projects and niche archives are most at risk; careless LLM crawlers can erase years of goodwill overnight.
- Watch next: emerging crawler standards (e.g., /.well-known/ endpoints), scraper attestations, and legal settlements defining acceptable AI training data practices.
