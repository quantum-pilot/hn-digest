# Defeating a 40-year-old copy protection dongle

- Score: 144 | [HN](https://news.ycombinator.com/item?id=46849567) | Link: https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle

### TL;DR
A modern developer helps an accounting firm still running 1980s RPG II software under Windows 98, blocked by a parallel-port hardware dongle from a long-defunct vendor. By disk-imaging the machine, disassembling the tools with Reko, and isolating a tiny 0x90‑byte copy‑protection routine that talks to LPT1, he realizes the dongle always returns a constant 16‑bit value in BX. He patches the routine to set BX, brute‑forces the low byte via DOSBox, discovers the magic value 0x7606, and permanently frees the compiler and its generated programs from dongle dependence—preserving a rare RPG toolchain.

---

### Comment pulse
- Dongles still exist → some engineering/industrial users prefer physical keys over cloud licensing; vendors need protection for perpetual licenses and lack resources to fight piracy.  
- Cracking pattern → usually just locate the protection check, flip a conditional jump, or bypass a constant-return routine, tools now make this much easier.  
- Simple scheme was rational → aimed at honest business customers; minimal friction was enough to signal payment expectation—counterpoint: even these light schemes are routinely cracked and resold.

---

### LLM perspective
- View: This is reverse engineering as digital conservation, rescuing business-critical tools from dead vendors and obsolete hardware.  
- Impact: Small firms on ancient stacks gain migration paths; historians and emulation projects get a preserved RPG II environment.  
- Watch next: Sanitized release of the compiler, documentation of the dongle protocol, and similar rescues for other locked-in legacy vertical software.
