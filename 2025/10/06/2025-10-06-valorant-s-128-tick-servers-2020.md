# Valorant's 128-Tick Servers (2020)

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45496146) | Link: https://technology.riotgames.com/news/valorants-128-tick-servers

### TL;DR

Riot explains how Valorant reduced server-frame time from about 50 milliseconds to below two milliseconds so 128-tick matches could run three games per CPU core. The team established a 2.34-millisecond budget, instrumented code by subsystem, and attacked replication, animation, gameplay, networking, hardware, scheduler, NUMA, power-state, and clock-source costs. Production-like measurement exposed surprises, including an Erlang scheduler spawning threads across every core. The resulting capacity forecast reportedly landed within 1%, enabling free high-tick-rate servers at launch.

### Comment pulse

- Readers praised the disciplined combination of application profiling, hardware experiments, and operating-system tuning.
- Discussion emphasized that benchmark environments must match production topology and background services.

### LLM perspective

- View: The breakthrough came from budgets and observability, not one exotic optimization.
- Impact: Organization-wide performance accounting made an expensive latency target economically deployable.
- Watch next: Revalidate budgets as game logic, player behavior, hardware generations, and fleet software change.
