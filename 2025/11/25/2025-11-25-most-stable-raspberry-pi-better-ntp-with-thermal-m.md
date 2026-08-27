# Most Stable Raspberry Pi? Better NTP with Thermal Management

- Score: 279 | [HN](https://news.ycombinator.com/item?id=46042946) | Link: https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/

### TL;DR

A hobbyist stabilized a Raspberry Pi time server by holding its CPU near 54°C, reducing temperature-driven crystal drift. The setup pins chronyd and PPS interrupts to CPU 0, runs them with real-time priority, and uses PID-controlled load on three other cores as a heater. In this single-device, author-reported comparison, frequency variability fell 81% and median GPS-PPS RMS offset reached 38 ns. Commenters proposed cheaper alternatives: thermal mass, controlled fans, direct crystal heating, or a TCXO.

### Comment pulse

- Deliberately burning compute can improve clock stability → constant temperature removes a major source of oscillator drift.
- The experiment sacrifices three cores and power → commenters favor insulating or replacing the oscillator for practical deployments.
- CPU isolation may be imperfect → unavoidable kernel work on CPU 0 could argue for placing timing tasks elsewhere.

### LLM perspective

- View: This is a clever demonstration of environmental control, not a general Raspberry Pi timing benchmark.
- Impact: Dedicated timing appliances can trade efficiency for predictability when nanosecond-scale consistency matters.
- Watch next: Replicate across devices and ambient conditions, then compare fan control, crystal heating, and TCXO retrofits.
