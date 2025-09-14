# Raspberry Pi Synthesizers – How the Pi is transforming synths

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45229227) | Link: https://www.gearnews.com/raspberry-pi-synthesizers-how-the-pi-is-transforming-synths/

TL;DR
- Raspberry Pi modules now power many digital synths, from Korg’s Wavestate/Modwave/Opsix to DIY/open boxes like Zynthian, Organelle, and GR‑1. Manufacturers gain cheap, integrated CPU/RAM/storage; software does the heavy lifting, so it isn’t “cheating.” HN notes modern Pis deliver ample DSP (NEON, multi‑core) for 96 kHz, high‑polyphony work, making legacy DSP chips unnecessary and cutting BOM costs. Still, audio has hard real‑time constraints—Linux reliability and scheduling guarantees matter. Mobile and DIY ecosystems further lower barriers, rivaling dedicated hardware.

Comment pulse
- Pi has ample DSP for complex synths → NEON FMAs and four cores yield ~10 GFLOPS; 96 kHz/32-voice leaves thousands of ops per note.
- Dedicated DSPs are fading → modern SBCs are faster/cheaper; porting saved ~$9 BOM, enabling ~$50 lower retail. — counterpoint: Linux gaps risk pops; consider RTOS.
- Tools and alternatives simplify creation → RNBO deploys patches to Pi; iOS apps + Bluetooth MIDI rival hardware; Pico/MeeBlip show fun low-cost DIY paths.

LLM perspective
- View: Pi commoditizes synth guts; differentiation shifts to sound design, UI latency, durability, and long-term software support.
- Impact: Lower BOM accelerates mid-tier gear and boutique DIY; pressure increases on legacy DSP vendors and analog-only marketing.
- Watch next: PREEMPT_RT maturity, Pi CM supply, low-latency HAT drivers, and Pi 5 vs custom DSP benchmarks in production gear.
