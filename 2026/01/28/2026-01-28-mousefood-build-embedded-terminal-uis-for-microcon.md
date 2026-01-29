# Mousefood – Build embedded terminal UIs for microcontrollers

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46798402) | Link: https://github.com/ratatui/mousefood

### TL;DR

Mousefood is a no-std Rust backend that lets Ratatui terminal widgets render via embedded-graphics on microcontroller displays, including e‑ink. It supplies Unicode-capable fonts, bold/italic styles, color themes, a simulator, and hardware-agnostic integration hooks tested on ESP32, STM32, and RP2040-class chips. Hacker News discussion focuses on how text-based UIs compare with manual drawing on bitmap displays, and on Rust’s evolving embedded ecosystem versus traditional C/C++, with some relief this avoids web/TypeScript stacks.

---

### Comment pulse

- Text-mode graphics advocates: using rich fonts and box-drawing on bitmap displays is faster and simpler than imperative drawing, proven on 8‑bit games.  
- Rust-on-embedded fans: HALs and typestate catch pin mistakes and decouple drivers from vendors; embassy async gives RTOS-like scheduling — counterpoint: C/C++ still supports more chips.  
- Others appreciate a modern TUI stack in pure Rust instead of React/TypeScript, avoiding browser-era bloat on tiny microcontrollers.  

---

### LLM perspective

- View: Shared Ratatui layouts could target both desktop terminals and physical devices, shrinking UI code duplication across toolchains.  
- Impact: Standardizing on an embedded text-UI stack may make instrumentation, test rigs, and hobby gadgets look far more polished.  
- Watch next: Memory-use benchmarks, more display-driver examples, and vendor-backed HALs will show whether this can scale to commercial firmware.
