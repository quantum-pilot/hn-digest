# Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46366998) | Link: https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server

### TL;DR
Meta is trialing SCX-LAVD, a Linux scheduler originally built for Valve’s Steam Deck, as a general-purpose “default” scheduler across its server fleet. SCX-LAVD runs on top of Meta’s own sched_ext framework and was developed by Igalia for Valve to improve latency and frame pacing on handheld gaming hardware. Meta found that its latency-critical, virtual-deadline design also scales well to large, heterogeneous servers, offering good performance and load balancing without per-workload custom schedulers. HN highlights gaming’s outsized role in driving Linux and systems innovations.

---

### Comment pulse
- Gaming pushes Linux forward → Valve-funded work on Proton, graphics, and schedulers spills into servers and desktops, improving performance everywhere—counterpoint: many non-gaming sponsors also drive kernel work.
- Valve’s model → small, game-focused core team; highly specialized infrastructure and kernel work (like SCX-LAVD) contracted to firms such as Igalia, yielding cost-effective, high-impact upstream changes.
- Open source cross-pollination → Meta adopts Valve’s scheduler; SteamOS distros adopt Meta’s Kyber I/O scheduler, showing bidirectional reuse despite differing licenses and proprietary patches.

---

### LLM perspective
- View: SCX-LAVD’s success shows that latency-focused designs for interactive workloads can generalize to large-scale, mixed server environments.
- Impact: Hyperscalers, gaming vendors, and desktop distros gain a shared, tunable scheduler stack instead of siloed, bespoke kernel forks.
- Watch next: broader sched_ext adoption, benchmarks versus EEVDF under varied loads, and whether memory/swap management gets similar cross-industry, gaming-driven overhauls.
