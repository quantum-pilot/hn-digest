# Staying ahead of censors in 2025

- Score: 228 | [HN](https://news.ycombinator.com/item?id=46417844) | Link: https://forum.torproject.org/t/staying-ahead-of-censors-in-2025-what-weve-learned-from-fighting-censorship-in-iran-and-russia/20898

### TL;DR

Tor’s 2025 anti-censorship work responded to Iran’s blackout and Russia’s increasingly adaptive blocking. In-region probes now test domain-fronting configurations; Snowflake gained better NAT assignment, metrics, and staging; Conjure hides connections across cooperating ISP address space; and WebTunnel added SNI imitation, certificate pinning, and Telegram bridge distribution. HN discussion mostly shifted toward Western speech restrictions, prompting others to distinguish legal moderation from the article’s technical problem: defeating network-level blocking without unacceptable collateral damage.

### Comment pulse

- Mimicry raises censorship costs → traffic resembling ordinary HTTPS forces blockers to disrupt widely used services.
- Comparisons with Britain and the EU divided readers → critics cited speech laws, while others stressed Tor remains technically reachable there.
- Distribution is as important as transport → rapidly enumerated public bridges require adaptive, region-specific delivery channels.

### LLM perspective

- View: Anti-censorship resilience is a feedback loop combining regional measurement, traffic disguise, and continuously changing distribution.
- Impact: Iranian and Russian users gain more fallback paths, while volunteer proxy and bridge operators become critical infrastructure.
- Watch next: Monitor Conjure deployment, WebTunnel enumeration rates, Snowflake reliability during blackouts, and censor-induced collateral damage.
