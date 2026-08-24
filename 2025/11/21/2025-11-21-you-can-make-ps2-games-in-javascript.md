# You can make PS2 games in JavaScript

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46006082) | Link: https://jslegenddev.substack.com/p/you-can-now-make-ps2-games-in-javascript

### TL;DR

AthenaEnv embeds a modified QuickJS interpreter in a native console program and exposes JavaScript APIs for graphics, assets, controllers, files, and sound. The author used PCSX2 to run a community port of his browser game, then built an animated, controller-driven sprite demonstration. Projects can iterate from host files or bundle the runtime, configuration, scripts, assets, and boot metadata into a distributable ISO. The abstraction resembles Canvas or Raylib rather than a complete engine, leaving collision and scene systems to developers; stronger 3D support remains under development.

### Comment pulse

- QuickJS makes high-level homebrew practical → Athena wraps native console libraries behind game-oriented APIs.
- Physical execution needs extra setup → modified consoles or memory-card and storage loaders remain necessary.

### LLM perspective

- View: The key achievement is a usable console API, not JavaScript interpretation alone.
- Impact: Web developers gain a gentler path into retro homebrew and distributable console projects.
- Watch next: Stable 3D support, hardware performance, ISO tooling, debugger ergonomics, and modern-console analogues.
