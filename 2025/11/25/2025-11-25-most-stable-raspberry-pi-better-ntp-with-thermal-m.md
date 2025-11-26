# Most Stable Raspberry Pi? Better NTP with Thermal Management

- Score: 279 | [HN](https://news.ycombinator.com/item?id=46042946) | Link: https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/

## TL;DR

A Raspberry Pi GPS‑PPS NTP server showed sub‑µs accuracy but its clock frequency wandered with CPU temperature. The author pins chronyd and PPS interrupts to one core, forces a performance governor, then runs a PID‑controlled “time burner” on the other three cores to hold the CPU at 54 °C, stabilizing the nearby crystal oscillator. Frequency variability drops by ~81% and RMS offset by ~50% to ~35–40 ns. HN discussion explores better core isolation and more direct hardware thermal control.

---

## Comment pulse

- Precision clock gear often uses crude but effective thermal tricks: WWVB’s water‑bottle thermal mass and classic crystal ovens show the Pi hack mirrors real practice.  

- Several suggest avoiding CPU0, using idle=poll, and isolating another core; unavoidable kernel work on CPU0 limits ultimate timing precision.  

- Others propose hardware fixes: swap in a TCXO/OCXO or heat/insulate the crystal directly with a resistor and foam—counterpoint: requires delicate soldering and mechanical work.

---

## LLM perspective

- View: This shows how far careful systems work plus cheap sensors can push commodity SBCs into lab‑grade timing territory.  

- Impact: Hobbyists and small labs can get nanosecond‑class NTP without buying dedicated GPSDO‑backed time appliances.  

- Watch next: Side‑by‑side benchmarks of Pi+PPS+thermal tricks vs TCXO/OCXO or GPSDO‑disciplined solutions, including power and complexity trade‑offs.
