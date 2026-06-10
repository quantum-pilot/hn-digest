# Porting the ThinkPad X61 to Coreboot

- Score: 163 | [HN](https://news.ycombinator.com/item?id=48456245) | Link: https://blog.aheymans.xyz/post/thinkpad_x61/

- TL;DR  
  - A long-time coreboot contributor finally ports the “missing generation” ThinkPad X61 (GM965/ICH8) by reverse‑engineering Lenovo’s Phoenix BIOS, heavily assisted—but not replaced—by an LLM (Claude + Ghidra-cli/radare2 tools). The model sped up pattern-spotting and code drafting, but required deep chipset knowledge to correct wrong register sizes, timings, CAS semantics, and multiple RAM init paths. After intensive human review and bug‑fixing, the work was upstreamed, suggesting LLMs now make previously prohibitive firmware reverse engineering (e.g., Intel FSP) realistically attainable.

- Comment pulse  
  - Retro ThinkPad modding thrives: X61/X62/X60 Tablet/T430 users praise 4:3 screens, rugged chassis, and upgrades—yet still long for full coreboot on tablet variants.  
  - Vibe-coded drivers (e.g., Wacom tablets) show LLMs can quickly yield working hardware support—counterpoint: article emphasizes success still depends on an expert guiding the model.  
  - Readers hope similar techniques free more proprietary firmware via LVFS/fwupd and inspire stalled reverse‑engineering projects; others discuss lightweight Linux options for X61-era hardware.

- LLM perspective  
  - View: LLMs are strong accelerators for experts doing firmware RE, but far from push-button replacements for understanding chipsets.  
  - Impact: Low-level platforms (coreboot targets, routers, tablets) become more approachable, reducing vendor leverage through opaque binary blobs.  
  - Watch next: Community FSP reimplementations, standard AI+Ghidra workflows, and legal clarification around firmware reverse engineering rights.
