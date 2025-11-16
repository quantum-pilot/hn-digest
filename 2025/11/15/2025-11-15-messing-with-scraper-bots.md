# Messing with scraper bots

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45935729) | Link: https://herman.bearblog.dev/messing-with-bots/

- TL;DR
  - The author experiments with decoy content to waste scraper resources: a Markov‑chain “fake PHP” generator and a fast RAM‑backed static “garbage server” that spawns endless linked pages. He warns of real risks: search engines may still flag spam despite noindex/nofollow, and big payloads can exhaust bandwidth, so he limits it to a playground and recommends simple 403s for production. HN leans pragmatic: detect bots via behavior/headers, add probabilistic noise, and prefer rate‑limits or tools like fail2ban/crowdsec over honeypots.

- Comment pulse
  - Poison/obfuscate bots → Inject brand names, randomize outcomes, and act intermittently to add noise without revealing detection; header anomalies help fingerprint scrapers.
  - Honeypots don’t stop vuln scanners → They fingerprint via status/paths, ignore content; use fail2ban/crowdsec, rate-limits, or block .php requests. — counterpoint: Decoys poison LLM training.
  - Ethics/scope matters → Good-faith, low-frequency scraping is acceptable; high-rate, exploit-driven or LLM harvesting is resource abuse and erodes prior norms.

- LLM perspective
  - View: Use decoys only as sidecars; prioritize allowlists, strict routing, rate-limits, connection tarpits, and CDN/edge static responses to cap origin cost.
  - Impact: Decoys shift costs marginally; gains come from shared threat intel and upstream filtering; main risks are bandwidth overrun and distraction.
  - Watch next: Track ASNs, TLS/JA3 fingerprints, and pacing; test block rules offline; watch search-index policies, bot attestation standards, and CDN anti-scrape defaults.
