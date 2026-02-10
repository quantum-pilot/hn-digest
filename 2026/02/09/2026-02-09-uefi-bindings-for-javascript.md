# UEFI Bindings for JavaScript

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46945348) | Link: https://codeberg.org/smnx/promethee

- TL;DR  
Promethee is a proof‑of‑concept UEFI application that embeds a JavaScript engine so your bootloader logic lives in script.js, with direct bindings to UEFI services like graphics. It demonstrates “JavaScript all the way down” rather than aiming to be practical. HN commenters oscillate between delight at the low‑level control, jokes about Gary Bernhardt’s Metal talk and Electron bloat, and curiosity about whether a full OS could be written in JS atop minimal C/assembly bootstrapping.

- Comment pulse  
  - Metal stage gag → Feels like Gary Bernhardt’s “everything becomes JS” prophecy; Electron bloat shows costs — counterpoint: RAM is plentiful, experimentation is fun.  
  - OS in JS? → JS bootloader is feasible; a real kernel still needs C/assembly to touch hardware, but hobby JS kernels and asm.js Linux exist.  
  - Joy versus horror → Some celebrate firmware control and Prometheus quotes; others recoil at JavaScript in firmware, joking about bundling npm, is-odd at boot.

- LLM perspective  
  - View: Neat demonstration of moving boot-time logic into a high-level language, blurring firmware, OS, and application boundaries.  
  - Impact: Useful as an educational or prototyping tool for UEFI, not a production path given attack surface and performance constraints.  
  - Watch next: Safer sandboxing, minimal JS runtimes, and measurements of boot time, memory overhead, and firmware security implications.
