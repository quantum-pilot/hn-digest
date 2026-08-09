# Fully Featured Audio DSP Firmware for the Raspberry Pi Pico

- Score: 255 | [HN](https://news.ycombinator.com/item?id=47901433) | Link: https://github.com/WeebLabs/DSPi

### TL;DR

DSPi is GPLv3 firmware that turns RP2040 and RP2350 Raspberry Pi Pico boards into low-cost USB audio processors. It accepts stereo 16- or 24-bit PCM at 44.1, 48, or 96kHz and routes it through preamp, parametric EQ, leveling, crossfeed, loudness compensation, matrix mixing, per-output delay, and volume stages. RP2040 supports four S/PDIF/I2S channels; RP2350 supports eight, plus a mutually constrained PDM subwoofer path. Presets, diagnostics, configurable pins, and USB updates are included. HN admired the scope but flagged external-output hardware as the adoption hurdle.

### Comment pulse

- One reader achieved inexpensive room correction with CamillaDSP, a calibrated microphone, and an older Pi using roughly 20% CPU.
- DSPi currently processes one stereo USB input and outputs only, limiting multi-input applications.
- Hardware setup seems intimidating — counterpoint: the creator plans an introductory video and plug-and-play board with connectors and codecs.

### LLM perspective

- Publish reference schematics, bills of materials, measured noise, latency, and distortion alongside firmware features.
- A custom board could turn an enthusiast project into a reproducible active-speaker platform.
- Watch S/PDIF input, host-console maturity, and real-world stability at the RP2040 overclock.
