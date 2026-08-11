# Reversed engineered game Starflight (1986)

- Score: 98 | [HN](https://news.ycombinator.com/item?id=47022943) | Link: https://github.com/s-macke/starflight-reverse

### TL;DR

Starflight-Reverse reconstructs the 1986 sandbox game's unusual internals and transpiles much of its Forth bytecode into compilable C-style code. Rather than ordinary x86 assembly, over 90% of the executable consists of 16-bit pointers implementing indirect-threaded words; machine code occupies under 5%, about 2,000 of 6,000 encrypted word names survive, and a functioning interpreter remains embedded. The project identifies 6,256 code and data words plus overlay and disk structures. HN celebrated both the technical archaeology and Starflight's persistent, free-form storytelling.

### Comment pulse

- The save disk doubled as mutable game memory → players had to use a copy because play rewrote state with no reset.
- Preserving technical artifacts remains fragile → portions of an original author's online source and design archive may already be missing.
- Forth defeated normal disassemblers → its unoptimized threaded structure nevertheless preserved enough high-level shape to enable a custom transpiler.

### LLM perspective

- **View:** The same implementation that wastes CPU cycles made source reconstruction unusually tractable four decades later.
- **Impact:** Preservationists gain readable structure, while emulator and VM authors gain a basis for faithful ports.
- **Watch next:** Missing archives, interpreter-based live debugging, completion of generated C, and derivative VM projects.
