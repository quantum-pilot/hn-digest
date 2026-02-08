# SectorC: A C Compiler in 512 bytes

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46925741) | Link: https://xorvoid.com/sectorc.html

### TL;DR
SectorC is a fully working C compiler squeezed into a 512‑byte x86 boot sector, written in 16‑bit assembly. It compiles a tightly constrained “Barely C” dialect that regular C compilers also accept, using space-delimited “mega-tokens” and the `atoi` integer parser as both tokenizer and hash for identifiers. With ~300 bytes for tokenizer/parser/codegen and ~200 for control flow, operators, comments, and inline `asm`, it supports real programs like VGA graphics and PC speaker demos. HN discussion centers on minimalism, nostalgia, and bootstrapping potential.

---

### Comment pulse
- Nostalgic low-level fun → Boot-sector compilers recall when tiny binaries and hand-tuned assembly were a skill showcase—counterpoint: today’s AI/codegen ecosystem can overshadow such work’s perceived value.  
- Subset C vs “real” C → This is a clever, strict subset sharing C syntax; full compilers (TCC, GCC) remain needed for general programs and architectures.  
- Hash-as-token love → Using `atoi` as hash/symbol table index is admired; people suggest bootstrapping chains from such tiny, auditable binaries.

---

### LLM perspective
- View: Smart abuse of parsing and hashing shows how far careful constraints and “cheats” can compress a language toolchain.  
- Impact: Useful as an educational artifact and as a verifiable seed in compiler/OS bootstrapping and provenance chains.  
- Watch next: Experiments chaining SectorC-like tools into progressively richer compilers, plus formal analyses of such minimal front-ends.
