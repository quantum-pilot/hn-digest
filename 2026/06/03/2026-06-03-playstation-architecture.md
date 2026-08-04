# PlayStation Architecture

- Score: 246 | [HN](https://news.ycombinator.com/item?id=48382142) | Link: https://www.copetti.org/writings/consoles/playstation/

### TL;DR

Rodrigo Copetti’s teardown explains how Sony made its first console an affordable 3D machine: a 33.87 MHz MIPS I core with 2MB RAM delegates geometry, video decoding, graphics, audio, and bulk transfers to specialized hardware. Its 1MB VRAM, software-sorted polygons, integer rasterization, affine texture mapping, and absent filtering created characteristic wobble, flicker, and warping, while CDs enabled streamed audio and pre-rendered scenes. HN readers supplied programming and boot-exploit anecdotes, praised the site’s presentation, and noted the article began in 2019 but remains updated.

### Comment pulse

- Memory aliasing → MGS tagged C4 placement in pointer bits; a BIOS iterator exploit similarly wraps writes to load custom code from memory cards.
- Freshness → The 2019 origin prompted repost objections — counterpoint: repeated updates and first-time readers preserved value.
- Presentation → Readers praised diagrams, layered navigation/accessibility variants, and the human-curated digital-garden feel despite dense engineering detail.

### LLM perspective

- **View:** Constraint-driven hardware made quirks part of the medium; developers converted missing general-purpose capability into distinctive techniques and aesthetics.
- **Impact:** Emulator, port, and preservation work depends on reproducing aliases, timing, ordering behavior, and revision-specific VRAM accurately.
- **Watch next:** The poster’s PS1 project release, web/WASM emulator selection, article changelog entries, and new porting or preservation discoveries.
