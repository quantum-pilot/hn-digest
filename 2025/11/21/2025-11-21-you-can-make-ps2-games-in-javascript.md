# You can make PS2 games in JavaScript

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46006082) | Link: https://jslegenddev.substack.com/p/you-can-now-make-ps2-games-in-javascript

## TL;DR
A PS2 homebrew framework called AthenaEnv embeds the QuickJS engine, letting you write real PS2 games in JavaScript instead of C/C++. The author discovers a fan-made PS2 port of their Sonic web game, then walks through using AthenaEnv: configuring `athena.ini`, running `athena.elf` in PCSX2, packaging assets and JS into a bootable ISO, and building a “Hello World” that handles sprites, animation, controller input, mirroring, and text/FPS rendering. HN comments connect this to wider homebrew, QuickJS, and JS-on-consoles experiments.

---

## Comment pulse
- AthenaEnv extends earlier PS2 work like Enceladus/Lua → both power not only games but popular homebrew apps and custom dashboards.
- QuickJS is celebrated as the enabler → Fabrice Bellard’s tiny engine lets constrained consoles run JS at all—counterpoint: it still can’t match JIT performance on modern hardware.
- Deployment sparks discussion → from ISO burning plus FreeDVDBoot/FreeMcBoot to parallels with Nintendo’s past web SDKs and QuickJS-based nx.js for the Switch.

---

## LLM perspective
- View: This bridges web and console dev, turning retro hardware into an accessible playground for JavaScript programmers.
- Impact: Homebrew devs, educators, and hobbyists can reuse web-game code and learn console constraints without deep C/C++ tooling.
- Watch next: Measure AthenaEnv performance vs native code, test 3D in v4, and track QuickJS-based runtimes on current-gen consoles.
