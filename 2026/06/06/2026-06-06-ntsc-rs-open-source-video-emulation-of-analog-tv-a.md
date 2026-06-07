# Ntsc-rs – open-source video emulation of analog TV and VHS artifacts

- Score: 231 | [HN](https://news.ycombinator.com/item?id=48428025) | Link: https://ntsc.rs/

### TL;DR
ntsc-rs is an open-source Rust-based tool that accurately emulates analog NTSC TV and VHS artifacts, using real signal-processing models instead of simple overlays. It’s multithreaded and SIMD-accelerated, fast enough for real-time use at resolutions far beyond original NTSC, and ships as a standalone app, web app, and plugins (After Effects, Premiere, OpenFX hosts). HN discussion mixes nostalgia and media-theory takes with more technical wishes for PAL and analog-receiver behavior, plus calls for better audio-era emulators.

---

### Comment pulse
- Art-from-glitches → Imperfections of old media become aesthetic signatures and nostalgia fuel; VHS artifacts now read as “character,” not failure.  
  — counterpoint: For those who fought these glitches professionally, this “nostalgia” feels more like PTSD than charm.

- Deeper simulation wish-list → Users want PAL support, bad deinterlacing, frame blending, rolling/losing sync, and receiver-like failure modes, not just cosmetic filters.

- Parallel domains → People ask for similarly accurate emulation of vinyl crackle, tape warble, and ham-radio noise, plus VHS-style audio compression artifacts.

---

### LLM perspective
- View: This represents a shift from “VHS look” as a texture pack to genuine reverse-engineering of analog video pipelines.

- Impact: Video editors, retro game/film makers, and VFX artists get reproducible, controllable “old TV” looks for period-accurate or stylized work.

- Watch next: Broader standards support (PAL/SECAM), integrated audio-path modeling, and benchmarks against real captured signals to validate authenticity.
