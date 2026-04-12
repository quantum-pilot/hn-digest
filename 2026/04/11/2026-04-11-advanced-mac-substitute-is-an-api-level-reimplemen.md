# Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS

- Score: 178 | [HN](https://news.ycombinator.com/item?id=47731506) | Link: https://www.v68k.org/advanced-mac-substitute/

### TL;DR
Advanced Mac Substitute (AMS) reimplements the classic 1980s Mac OS at the API level, letting unmodified 68k Mac apps run without Apple ROMs or original system software. A portable 68k emulator backend and SDL2/X11/macOS/framebuffer frontends provide 1‑bit graphics, windows, menus, dialogs, and file sandboxing, demonstrated with MacPaint, Lode Runner, and other early titles. HN commenters discuss the engineering effort, hardware-quirk compatibility, performance vs original machines, and using AMS as a foundation for modern, native-feeling classic app support.

---

### Comment pulse
- API-level recreation avoids proprietary ROMs → emulator devs see it as a cleaner, portable way to run classic Mac apps with modern conveniences.  
- Compatibility looks good → early Macs had a clean, simple architecture, reducing timing/graphics hacks—counterpoint: many real apps still relied on subtle implementation quirks.  
- Basis for modern wrapper → commenters imagine Carbon-like shims giving classic apps native windows and host files; AMS’ sandboxed directories already support Finder-launched documents.  

---

### LLM perspective
- View: API-level OS reimplementations neatly sidestep ROM legality and hardware emulation complexity while preserving “feel,” but require meticulous compatibility and test coverage.  
- Impact: If extended beyond games, AMS-like layers could keep legacy productivity tools usable for decades, easing archival, niche workflows, and educational access to old UIs.  
- Watch next: Key milestones: broader Toolbox coverage, networking/printing support, automated app-compat test suites, and packaging into user-friendly launchers for macOS, Linux, and Windows.
