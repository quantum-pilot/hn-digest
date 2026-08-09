# Turbo Vision 2.0 – a modern port

- Score: 190 | [HN](https://news.ycombinator.com/item?id=47898597) | Link: https://github.com/magiblot/tvision

### TL;DR

This port updates Borland’s Turbo Vision 2.0 C++ text-interface framework while preserving source compatibility with old applications and DOS builds. It runs on Linux and Windows with UTF-8, double-width and combining characters, 24-bit color, richer keyboard and mouse protocols, resizing, clipboard access, timers, CMake, and vcpkg. The original widget, window, menu, dialog, editor, and event model remains compact and hides terminal quirks. Hacker News readers called it a practical cultural treasure, reporting .NET wrappers and an LLDB frontend; nostalgia was tempered by antique palettes, manual layout, and sparse contemporary guidance.

### Comment pulse

- Backward compatibility is tangible: one user compiled 1993 code and prototyped an LLDB interface, while wrapper authors brought it to .NET.
- Several developers still prefer its compact framework to newer TUI libraries, crediting Borland’s architecture and manuals.
- Modernization remains incomplete: palettes and manual layout feel antique, splitters are absent, and searchable community knowledge is thin.

### LLM perspective

- **View:** Preserving old abstractions while replacing platform edges makes this revival evolutionary rather than ornamental.
- **Impact:** Terminal-tool authors gain mature widgets without repeatedly solving input, rendering, clipboard, and cross-platform behavior.
- **Watch next:** Stable releases, automatic layout, higher-level bindings, refreshed documentation, highlighted Unicode shortcuts, and ZWJ handling.
