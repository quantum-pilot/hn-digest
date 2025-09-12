# This blog is running on a recycled Google Pixel 5 (2024)

- Score: 365 | [HN](https://news.ycombinator.com/item?id=45110209) | Link: https://blog.ctms.me/posts/2024-08-29-running-this-blog-on-a-pixel-5/

- TL;DR
  - An Android Pixel 5 now hosts the author’s Hugo blog using Termux (sshd, screen/cron, dufs, rsync), served over Ethernet via USB‑OTG and powered by a 100W panel + Jackery battery. Setup avoided proot/ROMs; it’s fast, with minor hiccups (Hugo version mismatch, battery watching). HN debated efficiency vs simply using S3/Pages or low‑power x86, questioned skipping Wi‑Fi for latency reliability, and flagged risks: unpatched Android exposure and swollen batteries—suggesting charge limits, timers, or dummy packs.

- Comment pulse
  - Old phones make efficient servers; <5W vs desktops. — counterpoint: static hosting or low-power x86 rival efficiency; dollar savings are small.
  - Ethernet chosen for consistent latency and throughput; Wi‑Fi variability cited. Some note older Wi‑Fi stacks add jitter and hurt tail latencies; author’s Wi‑Fi unreliable.
  - Battery swell risk; mitigate with 80% charge caps, smart-switch timers, or dummy batteries—root sometimes required. Security updates for older phones are a concern.

- LLM perspective
  - View: Phones + Termux handle light services well; bottlenecks are networking, updates, and battery management, not compute.
  - Impact: Practical for hobbyists, edge caches, or off‑grid demos; less compelling for production static sites versus CDN or serverless.
  - Watch next: Measure idle/load watts, latency percentiles, and uptime; test charging-limit apps; document security hardening for Termux and Android exposure.
