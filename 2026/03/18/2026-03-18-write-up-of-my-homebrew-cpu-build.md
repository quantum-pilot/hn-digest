# Write up of my homebrew CPU build

- Score: 229 | [HN](https://news.ycombinator.com/item?id=47389696) | Link: https://willwarren.com/2026/03/12/building-my-own-cpu-part-3-from-simulation-to-hardware/

### TL;DR

The WCPU-1 is an 8-bit homebrew CPU carried from Logisim into breadboards and custom PCBs. Its builder fixed inverted enables, missing decoupling, floating pins, poor clock edges, EEPROM glitches, and RAM writes corrupted by asynchronous control. It now runs at 1 MHz for days, implements 23 instructions and three addressing modes, and executes Fibonacci loops with 256 bytes of RAM. An Arduino loader, Python microcode generator, and two-pass assembler support it; HN readers admired how physical construction exposes assumptions hidden by simulation.

### Comment pulse

- Parallel 74x574 registers could separate indicator LEDs from tri-state bus driving without eight discrete buffers.
- The project revived interest in medium-scale logic such as the 74181, though surface-mount availability complicates hobbyist prototyping.
- Readers valued building an obsolete architecture because direct manipulation teaches more than emulation or polished abstraction.

### LLM perspective

- **View:** The most instructive failures occurred at analog boundaries that digital simulation abstracts away.
- **Impact:** Learners gain practical intuition about signal integrity, timing phases, bus contention, and test instrumentation.
- **Watch next:** Output, halt, reset, overflow, the ROM/RAM redesign, final PCB, and promised source release.
