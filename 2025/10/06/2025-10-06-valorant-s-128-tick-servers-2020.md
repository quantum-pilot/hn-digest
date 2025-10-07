# Valorant's 128-Tick Servers (2020)

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45496146) | Link: https://technology.riotgames.com/news/valorants-128-tick-servers

TL;DR
- Valorant delivered free 128-tick servers by cutting server frame time from ~50ms to <2ms and fitting ~3 games per core. They replaced UE4’s polling replication with RPC “push,” throttled/disabled server animation, and enforced subsystem budgets using telemetry. Load tests exposed platform bottlenecks; moving to Xeon Scalable, NUMA pinning, CFS tweaks, limiting C-states, clocksource changes, and revisiting hyperthreading netted 1–30% gains. Goal: reduce peeker’s advantage and predict capacity within 1%, sparking HN debate on tick rate vs latency and genre needs.

Comment pulse
- Higher tick rate feels night-and-day: BF4 moved to 120–144 Hz; CS:GO community ran 128 Hz; Fortnite reportedly 30 Hz — counterpoint: CS2 subtick often disappoints.
- Latency still rules outcomes: skill-based matchmaking mixes pings; ubiquitous Wi‑Fi adds ~10 ms first-hop; Riot’s private backbone aimed to keep player RTTs under ~35 ms.
- Buy-phase optimization isn’t lobby bloat: Valorant/CS pause ~60 seconds each round to purchase; server disables animation then without affecting match pace.

LLM perspective
- View: Data-driven profiling plus OS/CPU tuning beats “more hardware” for tight latency budgets at scale.
- Impact: Normalizes 128 Hz expectations in competitive shooters; raises hosting cost bars for studios lacking network/infra investments.
- Watch next: Independent measurements comparing 64/128/sub-tick, end-to-end lag auditing per player, and QoS/peering expansion beyond major metros.
