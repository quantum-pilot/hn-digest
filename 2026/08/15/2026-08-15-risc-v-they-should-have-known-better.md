# RISC-V: They Should Have Known Better

- Score: 224 | [HN](https://news.ycombinator.com/item?id=49298035) | Link: https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV

### TL;DR

A critique argues RISC-V's extreme optionality prevents a dependable common target, while its base and compressed encodings omit routine operations, scatter immediates, slow interrupts, and sometimes reuse bytes for incompatible meanings. Later extensions and RVA23 profiles address gaps but create another standardization layer and leave boards behind. The author nevertheless expects RISC-V to win cheap embedded controllers and AI-accelerator support roles because licensing and cores can be free, not because the ISA excels, while remaining uncompetitive for top desktops. Commenters emphasized tooling, customization, and legal freedom as sufficient practical advantages.

### Comment pulse

- Practitioners value GCC/LLVM support, legal implementability, price, and customization—counterpoint: overlapping encodings and missing mandatory features cannot always be repaired downstream.
- Some dispute the narrow microcontroller model, while others say deep-embedded buyers mainly need something better-supported than 8051.

### LLM perspective

- View: The tradeoff is technical coherence versus licensing freedom and customization; adoption can reward the latter despite architectural debt.
- Impact: Profiles may stabilize general-purpose software, but they strand early hardware and cannot repair conflicting instruction meanings.
- Watch next: Compare RVA23 implementations on code density, interrupts, decode width, tooling, compatibility, and real workloads against Arm.
