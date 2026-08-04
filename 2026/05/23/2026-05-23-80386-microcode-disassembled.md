# 80386 microcode disassembled

- Score: 215 | [HN](https://news.ycombinator.com/item?id=48247004) | Link: https://www.reenigne.org/blog/80386-microcode-disassembled/

### TL;DR

Researchers reconstructed the 80386’s 94,720-bit microcode ROM from a die photograph, using image processing, a CNN, and days of manual checking, then inferred micro-op layout, fields, sequencing, decoder mappings, and accelerator interfaces. The result exposes 215 decoder entry points and shows every 386 instruction executes microcode. It also suggests an unconfirmed I/O-permission bug: a four-byte port access may check only three permission bits. HN readers praised the reverse engineering, unpacked how visible transistor patterns encode ROM bits, and stressed that the unknown CPU stepping limits conclusions about bugs.

### Comment pulse

- ROM geometry makes recovery tractable → row-column intersections locate bits, while transistor presence distinguishes ones from more-common zeros.
- Stepping identity is essential → 80386 revisions changed errata and even instructions, so one die cannot represent every chip.
- Reverse engineering enables faithful emulation → commenters want microcode-selectable models reproducing historical stepping-specific bugs.

### LLM perspective

- **View:** This combines computer vision, circuit archaeology, and architecture inference; none alone would make the bit array intelligible.
- **Impact:** Emulator and open-core developers gain implementation evidence beyond architectural manuals, especially for protection and memory behavior.
- **Watch next:** Identify the donor die’s stepping, test the proposed I/O flaw on hardware, and compare additional ROM revisions.
