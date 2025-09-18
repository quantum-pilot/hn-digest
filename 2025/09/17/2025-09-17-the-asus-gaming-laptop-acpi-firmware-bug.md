# The Asus gaming laptop ACPI firmware bug

- Score: 432 | [HN](https://news.ycombinator.com/item?id=45271484) | Link: https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive

- TL;DR
  - A deep dive ties widespread ROG laptop stutters to firmware, not Windows/drivers: a periodic ACPI GPE (_GPE._L02) runs ECLV, which sleeps 25–100 ms and re‑arms EC events, serializing ACPI/EC work on CPU0 and spiking ACPI.sys latency (~13 ms bursts every 30–60s). Firmware also issues GPU power transitions without checking MUX state (HGMD), power‑cycling the dGPU in Ultimate mode, occasionally causing WIN32K_POWER_WATCHDOG_TIMEOUT BSODs. Cross‑model since 2021; BIOS must remove sleeps/self‑rearm and respect MUX state. HN applauds the forensics, faults QA/reviews, and laments AML.

- Comment pulse
  - QA failure → Ubiquitous, reproducible; missed by support; brand risk — counterpoint: mostly hits Ultimate dGPU-only users, reducing RMAs.
  - AML critique → ACPI bytecode enables reverse-engineering, but encourages hacky, privileged logic many devs avoid on Linux.
  - Review gap → Reviewers seldom test dGPU-only long runs; LatencyMon >120s needed; sponsorship bias suspected.

- LLM perspective
  - View: Shift ACPI workload to deferred contexts; use Notify to schedule driver work instead of EC polling inside GPE methods.
  - Impact: Forces OEMs to audit EC event loops, GPU power paths, and MUX-awareness across ROG, TUF, Zephyrus firmware.
  - Watch next: Firmware changelogs citing ECLV/LGPA changes, HGMD conditionals; HLK GlitchFree passes; corroborating trace packs from affected models.
