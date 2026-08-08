# A year of fighting scrapers on my 1.5 million-page website

- Score: 359 | [HN](https://news.ycombinator.com/item?id=49211386) | Link: https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/

- TL;DR  
  - A 1.5M‑page philanthropy database found ~214 bot page loads per human view, mostly from SEO, AI crawlers, and residential botnets. Using Cloudflare WAF, the author now blocks whole countries, data-center ASNs, misbehaving AI crawlers, empty/ancient user-agents, and rate-limits everything else, judged by a “pages crawled per visitor referred” metric. Bots generate 99% of traffic and most cost. HN debates Cloudflare as gatekeeper, harm to atypical users and tools, hosting choices, and LLMs freeloading on web content.

- Comment pulse  
  - Cloudflare as de facto gatekeeper → owners outsource access control; JS-free, old-browser, or scripted access often blocked, so real users silently lose information access.  
  - Alternative defenses like Anubis proof-of-work → add friction and slow sites; scrapers can afford CPU, humans on phones pay the latency and battery cost.  
  - Cost focus → use cheaper static/VPS hosting instead of Cloudflare D1; others report Claude fetching 200k+ pages for 0–1 referrals—counterpoint: LLMs’ value isn’t direct traffic.

- LLM perspective  
  - View: “Pages crawled per visitor” is a pragmatic metric; site owners can justify or deny bots based on measurable reciprocity.  
  - Impact: Stricter bot blocking and Cloudflare-style controls will increasingly marginalize atypical clients, headless tools, and research crawlers without clear governance.  
  - Watch next: pay-per-crawl markets, standardized crawler identities, and browser-level consent signals could rebalance incentives between site operators and AI/search platforms.
