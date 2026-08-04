# WriteUp: 16 Bytes of x86 that turn Matrix rain into sound

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48173962) | Link: https://hellmood.111mb.de//wake_up_16b_writeup.html

### TL;DR

A 16-byte real-mode DOS program turns VGA text memory into both canvas and instrument. It selects mode 0, points DS at 0xB800, repeatedly reads a byte, moves backward 56 bytes, XORs memory, and sends the result to PC-speaker port 0x61. The recurrence implements Rule 60, producing Sierpinski structure; bit 1 drives square-wave audio while other bits generate flickering glyphs. Address arithmetic stretches the cycle to 8,192 steps and shears output into 10 columns. HN celebrated the audiovisual density and traded favorite sizecoding demos.

### Comment pulse

- Technical compression served the art → commenters found the eerie visuals and looping tone compelling even apart from the 16-byte achievement.
- Reliability beat fidelity → the author chose PC-speaker output after a better-sounding COVOX version failed intermittently.
- Sizecoding inspires lineage, not isolation → HN surfaced floppy-drive-only Freespin, 128-byte Spongy, 32-byte Rainy, and the author’s earlier Memories writeup.

### LLM perspective

- **View:** Extreme constraints reward instruction-level reuse: the same evolving byte simultaneously stores state, paints characters, and controls an actuator.
- **Impact:** For systems programmers and artists, the demo is a lesson in memory layout, modular arithmetic, and hardware side effects.
- **Watch next:** Compare machines and emulators, document initial-memory fingerprints, measure timing-dependent pitch, and test whether extra setup bytes improve reproducibility.
