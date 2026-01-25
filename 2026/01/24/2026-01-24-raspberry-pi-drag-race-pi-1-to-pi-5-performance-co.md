# Raspberry Pi Drag Race: Pi 1 to Pi 5 – Performance Comparison

- Score: 110 | [HN](https://news.ycombinator.com/item?id=46745922) | Link: https://the-diy-life.com/raspberry-pi-drag-race-pi-1-to-pi-5-performance-comparison/

- TL;DR  
Across 13 years and five generations, the author benchmarks Raspberry Pi 1–5 on CPU, GPU, storage, networking, video playback, and power. Pi 1 now struggles to boot, Pi 2–3 can’t do usable 1080p in-browser, Pi 4 is borderline, and Pi 5 finally feels like a small desktop. Sysbench shows Pi 5 over 600× faster than Pi 1 and ~200× better performance per watt. Hardware gains (PCIe, NVMe, better GPU) come with higher power budgets and a higher $50 entry price. Comments note Pi 3’s power sweet-spot and Pi 5’s limits.

- Comment pulse  
  - User’s brute-force solver shows runtime dropping from 680s (Pi 3) to 131s (Pi 5), but x86 desktops and Apple M2 Max still 2–3× faster.  
  - Pi 3 often called sweet-spot for cost, IO and power draw — counterpoint: others say Pi 4’s similar idle use makes its higher performance preferable.  
  - Several repurpose ancient Pis as Tailscale exit nodes, weather stations, or print servers; some question energy efficiency versus consolidating loads on newer, more performant hardware.

- LLM perspective  
  - View: Benchmarks reinforce that model choice should follow workload: media/desktop needs Pi 4–5; automation and gateways suit Pi 1–3.  
  - Impact: Power-per-watt gains mean upgrading from Pi 1–2 can both cut energy use and expand capabilities for always-on services.  
  - Watch next: Watch for better-standardized Pi power benchmarks and maturing PCIe/NVMe accessories, clarifying when Pi 5 beats cheap x86 mini-PCs.
