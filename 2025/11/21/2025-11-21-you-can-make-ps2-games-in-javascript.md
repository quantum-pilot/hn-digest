# You can make PS2 games in JavaScript

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46006082) | Link: https://jslegenddev.substack.com/p/you-can-now-make-ps2-games-in-javascript

### TL;DR

AthenaEnv embeds a modified QuickJS runtime in a native PlayStation 2 program and exposes JavaScript APIs for rendering, assets, input, files, and sound. The author tested a JavaScript Sonic runner in PCSX2, then documented packaging the runtime, configuration, scripts, assets, and boot files into a distributable ISO. A small example covers sprite animation, controller movement, mirroring, text, and frame timing. Athena offers low-level, canvas-like building blocks rather than a full engine; its developing version 4 is expected to emphasize 3D.

### Comment pulse

- Readers highlighted QuickJS’s enabling role and Athena’s usefulness for homebrew applications beyond games.
- Physical-console options and comparable JavaScript environments prompted discussion about console security restrictions and JIT-free runtimes.

### LLM perspective

- View: The notable achievement is a practical hardware API around JavaScript, not JavaScript interpretation alone.
- Impact: Familiar language and fast emulator iteration lower the entry barrier to PS2 homebrew experimentation.
- Watch next: Athena version 4’s 3D maturity and safer, reproducible ISO-building workflows.
