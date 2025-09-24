# Shopify, pulling strings at Ruby Central, forces Bundler and RubyGems takeover

- Score: 408 | [HN](https://news.ycombinator.com/item?id=45348390) | Link: https://joel.drapper.me/p/rubygems-takeover/

- TL;DR
    - Article alleges Ruby Central, under financial pressure after Sidekiq withdrew $250k/yr, acceded to Shopify’s demands to seize control of RubyGems/Bundler repos and gems, locking out long‑time maintainers (incl. André Arko). RC frames it as supply‑chain security and a temporary lockdown; critics say they conflated operating the RubyGems service with owning its code, ignored forking, and targeted individuals. HN debates motives—security, culture‑war around DHH, or business risk—and flags a potential conflict with Spinel’s new rv tool.

- Comment pulse
    - Security-first governance → Shopify pushed tighter access to reduce supply-chain risk and meet compliance deadlines — counterpoint: no breach; RC conflated service ops with code ownership.
    - Culture-war lens → DHH’s platforming triggered Sidekiq’s $250k pull; factions aligned and power shifted under funding pressure, not purely engineering concerns.
    - Conflict-of-interest worry → targeting André/Sam amid Spinel’s rv launch suggests fear of competition; community fears trust erosion and potential forks.

- LLM perspective
    - View: Governance failure under financial duress; secure operations don’t require expropriating community repositories or excluding maintainers.
    - Impact: Erosion of maintainer trust, risk of forks, corporate capture concerns; enterprises may reevaluate dependency and supply-chain posture.
    - Watch next: Publish governance model, restore access, implement gem signing/audit trails, clarify Rails Foundation role, disclose sponsors, finalize Operator/Contributor Agreements.
