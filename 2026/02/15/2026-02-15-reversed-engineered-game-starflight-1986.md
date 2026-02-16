# Reversed engineered game Starflight (1986)

- Score: 98 | [HN](https://news.ycombinator.com/item?id=47022943) | Link: https://github.com/s-macke/starflight-reverse

- TL;DR  
This project deeply reverse‑engineers the 1986 space‑exploration classic Starflight, whose DOS executable turned out to be essentially a Forth VM with threaded bytecode, minimal x86, and encrypted word names. The author built a custom disassembler/transpiler that converts those Forth “words” and pointers into C‑style code and maps the game’s complex on‑disk structure of overlays, tables, and assets. HN comments focus on Starflight’s groundbreaking open‑world design, disk‑as‑save‑state persistence, partial loss of original docs, and the surprisingly strong Sega Genesis version.

- Comment pulse  
  - Starflight’s design was revolutionary → a huge, persistent, clue‑driven galaxy where the save game literally rewrote the disk; failure meant no reset.  
  - Reverse engineering was unusually fun → Forth VM, embedded interpreter, encrypted symbols, elaborate overlays; inspired a Starflight VM project and comparisons to other hard‑to‑decompile 80s games.  
  - Preservation regret → only partial design docs/source survived; people now actively mirror and archive any remaining technical material—counterpoint: some argue what exists is all that was ever released.  

- LLM perspective  
  - View: This is a rare, high‑quality case study in reversing a non‑C, threaded‑code commercial game.  
  - Impact: Useful reference for emulator/VM writers, game historians, Forth enthusiasts, and anyone tackling legacy binaries without symbols.  
  - Watch next: Structured documentation of the recovered C‑like code, automated test harnesses, and comparisons with Sega Genesis internals would amplify its educational value.
