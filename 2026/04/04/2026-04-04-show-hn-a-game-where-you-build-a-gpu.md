# Show HN: A game where you build a GPU

- Score: 450 | [HN](https://news.ycombinator.com/item?id=47640728) | Link: https://jaso1024.com/mvidia/

### TL;DR

MVIDIA is a browser circuit-building game that teaches computing bottom-up. Players wire NMOS and PMOS switches into gates, adders, latches, registers, SRAM and DRAM, an ALU, control unit, and an eight-bit processor, then program it through increasingly complex machine-code exercises. The current v0.1.0 includes 72 required levels across transistors, processor construction, and software, plus optional manufacturing background and six languages; the actual GPU and shader acts are still marked “coming soon.” HN liked the interface but found onboarding, truth-table timing, capacitor modeling, and wire visibility confusing.

### Comment pulse

- Even an integrated-circuit veteran failed level one because a background grid line resembled a wire; the author plans theme changes.
- The capacitor’s enable pin is not physically accurate; simulation constraints forced the abstraction and accidentally let players bypass the intended transistor.
- The author used Claude heavily, especially with detailed graphics direction; commenters requested basic physics lessons, live truth tables, temporary probes, and no timer.

### LLM perspective

- **View:** The game works pedagogically when simulation compromises are explicit and every visual affordance matches electrical meaning.
- **Impact:** Beginners can connect semiconductor behavior to instruction execution, but misleading primitives may harden misconceptions before later lessons correct them.
- **Watch next:** Restored Act 0, untimed instruction, capacitor redesign, live probes, accessibility changes, GPU acts, and hardware-educator validation.
