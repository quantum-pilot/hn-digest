# Saying goodbye to asm.js

- Score: 299 | [HN](https://news.ycombinator.com/item?id=48206340) | Link: https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html

## TL;DR
Firefox 148 disables SpiderMonkey’s asm.js optimizations and will remove the compiler, while continuing to run asm.js as regular JavaScript. Mozilla frames asm.js as a successful prototype that proved native-speed web execution and directly paved the way for WebAssembly, which is now faster, smaller, and better maintained. HN discussion mixes nostalgia for the “alternative web timeline” of NaCl/PNaCl and Gary Bernhardt’s prophecy with pragmatic acceptance that WebAssembly won, even as its ecosystem still feels immature.

## Comment pulse
- Alternate history nostalgia → Some wish NaCl/PNaCl had survived, blaming today’s bloated Electron apps and slow WASM tooling—counterpoint: NaCl was too big; asm.js shipped first.
- Pragmatists → asm.js was a stepping-stone compilation target; sad only in a “sunset of an era” sense, since WASM cleanly supersedes it.
- Concrete impact → Figma and Unreal-in-the-browser show asm.js proved serious C++ apps could run on the web, de‑risking later WASM bets.

## LLM perspective
- View: This is classic tech succession: a successful prototype retires once its standardized, safer replacement dominates.
- Impact: Web devs with legacy asm.js builds gain performance by recompiling to WASM; browser vendors reduce complexity and attack surface.
- Watch next: Better WASM tooling, debugging, and sandboxes for untrusted code (including AI runtimes) will determine whether WASM becomes a true universal web ISA.
