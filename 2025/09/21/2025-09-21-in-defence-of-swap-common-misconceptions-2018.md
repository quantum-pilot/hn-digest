# In defence of swap: common misconceptions (2018)

- Score: 105 | [HN](https://news.ycombinator.com/item?id=45318798) | Link: https://chrisdown.name/2018/01/02/in-defence-of-swap.html

TL;DR
- Chris Down argues swap isn’t “emergency RAM” but a tool that equalizes reclamation by giving anonymous pages a backing store, improving cache efficiency and stability. Disabling swap just shifts I/O thrash to file pages. With modern kernels (>4.0) and SSDs, swap behavior and latency are far better; tuning swappiness and using cgroup v2 memory.low/PSI gives control under pressure. HN adds battle stories from runaway processes, renewed trust after past heuristics, BSD contrasts, practical sizing tips, and extremes like NVMe-backed zswap—plus cautions about responsiveness, wear, and using ulimits to cap bugs.

Comment pulse
- Runaway processes make systems thrash and swap out good pages → users resort to swapoff/swapon; MGLRU lru_gen_min_ttl may reduce post-thrash pain.
- Old Linux swapped too eagerly → admins disabled swap; PSI and modest sizing (1/8–1/32 RAM) rebuild trust — counterpoint: BSD often avoids an OOM killer.
- NVMe-backed zswap can cheaply spill huge temporary working sets → dramatic cost savings vs RAM; watch device wear and consider job isolation/ulimits during compute.

LLM perspective
- View: Treat swap as policy tool: balance anon/file reclaim and responsiveness; prevent thrash with cgroups instead of disabling swap.
- Impact: Operators tune swappiness and memory.low per workload; desktop users set sane swap sizes and adopt PSI-driven monitors.
- Watch next: Kernel MGLRU adoption, PSI tooling maturity, and defaults that avoid swappiness=0 pitfalls; better UIs for pressure and refault metrics.
