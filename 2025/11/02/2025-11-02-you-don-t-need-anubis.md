# You Don't Need Anubis

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45787775) | Link: https://fxgn.dev/blog/anubis/

- TL;DR
  - The author argues Anubis’s JavaScript proof‑of‑work is overkill for blocking LLM scrapers; most don’t run JS, so a tiny “set‑cookie then reload” gate works, without 10‑second delays. For real DDoS, use Cloudflare‑class protection; PoW costs are trivial to attackers and temporary anyway. HN debate pushes back on the “$0” claim, notes Anubis helping against scraping floods, highlights misconfigurations like curl bypass, and flags collateral damage to NoScript/TUI users and the “political” motive of annoying AI bots.

- Comment pulse
  - Anubis works for scraping DDoS → buys uptime for repos/forums; admins accept delays reluctantly — counterpoint: PoW hurts users more than attackers with optimized solvers.
  - PoW economics disputed → “$0” claim challenged; scrapers may not reuse tokens, but JS hashing is inefficient and native code trivializes challenges.
  - Default curl bypass criticized → maintainer: avoid breaking automation; challenge only “Mozilla” UAs to force bot re-identification.

- LLM perspective
  - View: Start with JS cookie gate + behavioral throttling; skip PoW unless telemetry shows scraper JS execution or volumetric abuse.
  - Impact: Ops teams must monitor scraper fingerprints, adjust UA rules, and provide non‑JS fallbacks to avoid locking out legitimate users.
  - Watch next: Track bots executing JS, standardized bot IDs/attestation, and open alternatives to Cloudflare with measured efficacy.
