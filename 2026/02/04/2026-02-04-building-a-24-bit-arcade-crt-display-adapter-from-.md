# Building a 24-bit arcade CRT display adapter from scratch

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46888795) | Link: https://www.scd31.com/posts/building-an-arcade-display-adapter

### TL;DR

Stephen built a Linux-compatible USB adapter that drives an arcade cabinet’s nonstandard CRT at 336×262, 60 Hz, and 24-bit color. An RP2040 prototype generated VGA through PIO and implemented GUD, but full-speed USB capped practical frame rate. Two custom STM32 revisions followed: one missed the external high-speed PHY and shorted power planes; the next added ULPI, RAM, resistor DACs, and LTDC, ultimately producing smooth, band-free output. Commenters praised the detailed failures while recommending ESD protection, buffered or dedicated DACs, wider traces, cleaner grounding, and newer RP2350 techniques.

### Comment pulse

- Failure details teach most → USB bit-versus-byte math, hidden PHY requirements, stale pours, and missing oscillator bias drove successive redesigns.
- Hardware review found durability gaps → add low-capacitance ESD protection, buffer VGA, consider a DAC IC, widen traces, and preserve ground-return paths.
- Alternatives remain viable → RP2350 HSTX relaxes earlier PIO limits, while upstream GUD keeps the finished adapter driverless on modern Linux.

### LLM perspective

- View: The project succeeds by composing standard peripherals and iterating through integration mistakes, not by inventing a new display protocol.
- Impact: RCade gains arbitrary-resolution, full-color output; makers gain reusable GUD firmware, board files, DAC calculations, and candid failure analysis.
- Watch next: USB failure root cause, ESD revision, audio and controls, multi-buffer compatibility, GUD documentation, and long-term 24/7 reliability.
