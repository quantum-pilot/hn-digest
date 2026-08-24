# Most Stable Raspberry Pi? Better NTP with Thermal Management

- Score: 279 | [HN](https://news.ycombinator.com/item?id=46042946) | Link: https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/

### TL;DR

After correlating clock drift with board temperature, the author stabilized a GPS-disciplined Raspberry Pi by reserving one core for chronyd and PPS interrupts while a PID controller heated the other three to 54°C. The experiment reports 81% less frequency variability, 77% lower frequency standard deviation, and 49% lower RMS timing offset, reaching a 38-nanosecond median. It deliberately spends power and processor capacity for negligible everyday benefit. Commenters proposed isolating a nonzero core, adding thermal mass, heating the crystal directly, or installing a better oscillator.

### Comment pulse

- Thermal stability improved discipline → holding the nearby crystal’s environment steady narrowed frequency drift despite daily room-temperature swings.
- The method trades efficiency for precision → three cores burn cycles and annual energy rises, making it unsuitable for shared workloads.
- Hardware fixes may be cleaner → direct crystal heating, insulation, TCXO, or OCXO attacks the oscillator rather than simulating load.

### LLM perspective

- View: This is a successful measurement-driven homelab experiment, not a sensible general NTP configuration.
- Impact: Precision projects gain a reproducible way to test temperature-induced clock error with commodity hardware.
- Watch next: Nonzero-core isolation, idle polling, direct heater control, seasonal stability, and comparison with TCXO or OCXO hardware.
