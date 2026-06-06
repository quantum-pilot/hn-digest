# 80386 microcode disassembled

- Score: 215 | [HN](https://news.ycombinator.com/item?id=48247004) | Link: https://www.reenigne.org/blog/80386-microcode-disassembled/

### TL;DR
An enthusiast team has fully extracted and disassembled the Intel 80386’s hardwired microcode from die photographs, revealing how every x86 instruction is implemented at the μ-op level. Using stitched microscope images, they located ROM bit cells, trained a CNN to classify 0/1 transistors, then reconstructed and decoded the 94,720‑bit control store. The work uncovers 215 microcode entry points, hardware “accelerators” for multiply/divide, shifting, protection, and a likely long‑undocumented I/O‑permission bug, and it feeds new educational write‑ups and open‑hardware 386 efforts.

### Comment pulse
- Microcode bits sit in a regular ROM array; team marked bit locations, used a CNN to classify transistor/no‑transistor cells, then hand‑verified and reassembled words.  
- HN wants identification of the exact 80386 stepping so future emulators can swap different microcode images and faithfully reproduce historical bugs and errata.  
- Readers highlight this as exceptional reverse‑engineering, point to microprogramming textbooks and prior 8086 die analyses, and connect it to an open‑source 386‑clone microcode project.

### LLM perspective
- View: Disassembling commercial microcode shows vendor‑independent ground truth for instruction semantics, beyond architecture manuals and incomplete errata documents.  
- Impact: Emulator authors, OS historians, and security researchers gain a detailed model of 386 behavior, including faults and protection logic.  
- Watch next: Compare microcode across steppings, formalize it into machine‑readable specs, and validate suspected I/O‑permission bugs on real hardware.
