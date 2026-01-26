# Nvidia-smi hangs indefinitely after ~66 days

- Score: 196 | [HN](https://news.ycombinator.com/item?id=46750425) | Link: https://github.com/NVIDIA/open-gpu-kernel-modules/issues/971

### TL;DR
NVIDIA’s open GPU kernel driver for B200 (Blackwell) GPUs has a reproducible long-uptime bug: after ~66 days 12 hours, `nvidia-smi` and NVLink-related operations hang, often tanking clusters until reboot. Multiple independent reports across driver branches (570, 580) and kernels (6.6, 6.8) show identical NVLink error logs and broken multi-GPU jobs. NVIDIA has confirmed it as a driver issue under internal bug IDs, with a fix “in the works”; a community PR suggests it’s a timer/jiffies overflow and switches to `ktime_get_raw_ts64`.

---

### Comment pulse
- Long-uptime hardware bugs are common → TPM example: a timer overflow caused synchronized failures across all machines after a fixed number of days.
- The pattern screams timer wraparound → discussion centers on 32‑bit counters, jiffies, and using `time_before()/time_after()` to compare timestamps safely.
- Observers spot numerology → one internal bug ID equals 66.5 days in seconds, reinforcing overflow suspicions and prompting jokes plus speculation about scaled counters and NVLink.

---

### LLM perspective
- View: This is a textbook “only shows up at scale/uptime” bug; serious for large AI clusters depending on NVLink.
- Impact: Operators may need enforced sub‑60‑day reboot schedules and tighter monitoring on NVLink errors until a fixed driver is deployed.
- Watch next: Driver release notes referencing nvbugs 5746052/5607938, PR #1014’s fate, and reports from clusters validating stability past 70–80 days.
