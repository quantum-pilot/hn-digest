# Mousefood – Build embedded terminal UIs for microcontrollers

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46798402) | Link: https://github.com/ratatui/mousefood

### TL;DR

Mousefood is a no-std Rust backend that lets Ratatui applications render through embedded-graphics on microcontroller displays. It supplies Unicode-capable bitmap fonts for box drawing and Braille, configurable bold and italic faces, color themes, a desktop simulator, and optional support for WeAct and Waveshare e-paper panels. The hardware-agnostic crate has been tested on ESP32, ESP32-C6, STM32, RP2040, and RP2350. Richer fonts improve widget compatibility but consume scarce flash and can require optimization for acceptable frame rates.

### Comment pulse

- Developers debated drawing primitives directly versus text glyphs; supporters said character-cell constraints save memory and simplify UI construction.
- Embedded Rust users praised HAL portability, compile-time peripheral checks, and Embassy async — counterpoint: C and C++ still offer broader drivers and tutorials.
- One commenter jokingly contrasted Rust with TypeScript-driven terminal interfaces.

### LLM perspective

- View: It repurposes a mature terminal-widget ecosystem for small screens instead of inventing another embedded UI toolkit.
- Impact: Shared Ratatui components could shorten firmware UI work while retaining no-std portability across common microcontrollers.
- Watch next: Flash footprint, display-driver coverage, partial-refresh performance, input handling, and adoption beyond demos.
