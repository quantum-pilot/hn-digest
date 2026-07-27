# Cloudflare's new AI traffic options for customers

- Score: 187 | [HN](https://news.ycombinator.com/item?id=49052564) | Link: https://blog.cloudflare.com/content-independence-day-ai-options/

- TL;DR  
  Cloudflare is rolling out fine-grained AI traffic controls for all customers, classifying bots into Search, Agent, and Training and letting sites block or allow each. From September 15, Training and Agent crawlers will be blocked by default on ad pages, and multi-purpose bots like Googlebot may be caught if they’re also used for model training. Enterprise customers get BotBase and content-use levels (immediate/reference/full). HN discussion focuses on impacts for Google, Cloudflare’s growing gatekeeper role, and the web’s economic endgame.

- Comment pulse  
  - Cloudflare's new rules will hit multi-purpose crawlers like Googlebot; many welcome pushback against free AI training — counterpoint: risks lost search traffic and stronger incumbents.  
  - Critics worry Cloudflare becomes a centralized gatekeeper deciding which bots can see much of the web, with little democratic or standards-body oversight.  
  - Others question long-term economics: will ADOG ever pay to crawl, or does this accelerate paywalled content, secret deals, and regulatory or IETF intervention?

- LLM perspective  
  - View: This nudges AI ecosystems toward explicit contracts: separate crawlers, declared content use, and revocable “verified” status tied to behavior.  
  - Impact: Small and ad-driven sites gain practical levers against parasitic scraping, but dependence on Cloudflare’s classifications creates new platform risk.  
  - Watch next: whether AI vendors adopt content-use headers, split search/training bots, or route around Cloudflare via partnerships and browser integrations.
