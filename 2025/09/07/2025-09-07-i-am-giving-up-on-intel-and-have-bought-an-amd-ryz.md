# I am giving up on Intel and have bought an AMD Ryzen 9950X3D

- Score: 341 | [HN](https://news.ycombinator.com/item?id=45155986) | Link: https://michael.stapelberg.ch/posts/2025-09-07-bye-intel-hi-amd-9950x3d/

- TL;DR
  - The author’s Intel Core Ultra 9 285K failed twice; the second failure followed a 4-hour CPU-only OCR batch at ~100°C—within Intel spec. Frustrated with stability, he switched to a Ryzen 9 9950X3D on an ASUS X870+ for Linux. Results: slightly faster compiles, but meaningfully higher idle and peak power; household energy rose from ~9.x to 10–11 kWh/day. Linux 6.13 lets him choose V‑Cache vs frequency cores. HN leans toward better thermals, conservative board settings, and ECC where possible; stability beats marginal speed.

- Comment pulse
  - Use ECC-capable platforms → reduces silent faults and eases debugging; AMD supports UDIMM ECC but motherboard support inconsistent — counterpoint: ECC RAM can cost ~2×.
  - Fix thermals and defaults → 100°C suggests poor airflow, VRM heat, or aggressive board power limits; CPUs should throttle, and 285K’s spec is 105°C.
  - Expect instability trade-offs → high-end desktop parts from both vendors show quirky crashes; prebuilts with service and conservative settings save time versus endless component swaps.

- LLM perspective
  - View: This is reliability over vanity metrics; marginal perf gains are outweighed by RMA risk and higher whole-system power.
  - Impact: Linux desktop builders favor AMD for cache-tuned performance, but pay with higher idle draw and stricter cooling/motherboard choices.
  - Watch next: Independent idle-power benchmarks, BIOS-default audits, Linux 6.13 V-Cache effects, and vendor matrices clarifying ECC support per board.
