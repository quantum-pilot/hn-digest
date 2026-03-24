# Can you get root with only a cigarette lighter? (2024)

- Score: 173 | [HN](https://news.ycombinator.com/item?id=47453462) | Link: https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html

### TL;DR
Buchanan shows you can do practical electromagnetic fault injection (EMFI) with a €1 cigarette‑lighter piezo igniter instead of lab gear. The piezo’s high‑voltage spike, aimed near DDR memory lines, occasionally corrupts or blocks individual writes. By arranging sensitive data structures (e.g., JavaScript engine objects, kernel metadata) at precise physical addresses and repeatedly glitching, he turns rare bitflips into powerful exploit primitives (addrof/fakeobj, kernel pwn). It works on LPDDR4/5 and ARM, but newer consoles with memory encryption blunt simple bitflip attacks.

---

### Comment pulse
- Research scope → Works on LPDDR4/5, ARM; piezo is a cheap EMFI source; electronic version via fast mux ICs or commercial tools like ChipSHOUTER.  
- Consoles & mitigations → Switch kernel can be pwned; Switch 2’s memory encryption makes single‑bit flips useless—counterpoint: full‑write blocking glitches might still be exploitable.  
- Culture & standards → People reminisce about “glitching” vending machines; others gripe that JEDEC paywalls the DDR specs needed to study and harden against these attacks.

---

### LLM perspective
- View: This turns “lab‑only” EMFI into a kitchen‑table attack, shrinking the gap between academic hardware hacking and real‑world exploitation.  
- Impact: SoC vendors and browser/console teams must treat low‑cost physical attackers as realistic, not hypothetical, especially for jailbreak and DRM scenarios.  
- Watch next: Compare EMFI robustness of memory encryption schemes, evaluate ECC/rowhammer defenses against targeted glitches, and standardize affordable EMFI test setups for product security reviews.
