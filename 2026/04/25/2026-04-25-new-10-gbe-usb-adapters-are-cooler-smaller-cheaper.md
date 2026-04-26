# New 10 GbE USB adapters are cooler, smaller, cheaper

- Score: 533 | [HN](https://news.ycombinator.com/item?id=47899053) | Link: https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/

### TL;DR
New 10 GbE USB 3.2 adapters using Realtek’s RTL8159 are much smaller, cooler, and cheaper (~$80) than older Thunderbolt 10G dongles. But they only hit near‑wire‑speed (~9.5 Gbps) on systems with a 20 Gbps USB 3.2 Gen 2x2 port; most laptops are limited to ~6–7 Gbps, making 5 Gbps or 2.5 Gbps USB adapters a better value. Macs work plug‑and‑play but still top out around 5–7 Gbps, so Thunderbolt remains the best way to get full 10GbE on Apple laptops.

---

### Comment pulse
- Benchmark accuracy concern → iperf3 single‑thread might cap results; others note modern CPUs and interrupt coalescing, and that single stream often reflects real‑world usage.  
- USB naming chaos → “USB 3.2” and Gen/lanes hide actual speeds; poor labeling means users guess capabilities—counterpoint: USB4 branding and power/speed icons slightly improve clarity.  
- Ecosystem implications → Apple lacks USB 3.2 Gen 2x2, so Thunderbolt 10GbE still wins there; some want SFP+ support, but RJ45 suits most users and existing cabling.

---

### LLM perspective
- View: These RTL8159 USB NICs are a sweet spot for homelabbers needing occasional 10G, not for everyone chasing maximum throughput.  
- Impact: Expect more budget USB‑C 10G NICs and laptop modules, but 2.5/5G will remain the mainstream “fast enough” wired option.  
- Watch next: Linux/Windows driver maturity, real‑world power and thermals vs 10GBASE‑T cards, and laptops explicitly advertising 20 Gbps USB‑C ports.
