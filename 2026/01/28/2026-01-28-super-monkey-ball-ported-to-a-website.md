# Super Monkey Ball ported to a website

- Score: 271 | [HN](https://news.ycombinator.com/item?id=46789961) | Link: https://monkeyball-online.pages.dev/

## TL;DR
Fan developers have recreated Super Monkey Ball’s GameCube-era gameplay in the browser using TypeScript/WebGL, driven by a decompilation of the original games rather than emulation. The site offers full stage/difficulty selection, controller and keyboard support, gyro controls, and audio settings, closely matching the original feel (minus the visible monkey model). HN discussion focuses on how capable plain JS/WebGL now is, the reliance on reverse engineering, and why games of this quality remain rare on the web despite being technically feasible.

---

## Comment pulse
- Implementation is a TypeScript port atop decompiled SMB1/2 logic → shows JS JIT + WebGL can handle console-style 3D without WebAssembly—counterpoint: some suspect heavy AI assistance in the code.
- Web vs native: originally Monkey Ball showcased iPhone-native power “beyond web apps” → commenters note today’s web still lacks robust tools like RenderDoc, limiting mainstream high-end titles.
- Rarity of polished web games puzzles devs → a few share their own ports and lament that simple, quick, non-monetized casual games are hard to find nowadays.

---

## LLM perspective
- View: High-fidelity web ports of classics are becoming a preservation and distribution channel independent of app stores and platform gatekeepers.
- Impact: Encourages hobbyists to reuse decompilation work, lowering barriers for accurate, legal-ish remakes that run everywhere with just a URL.
- Watch next: Better WebGL/WebGPU debugging, standardized controller/gyro APIs, and open decomp projects will decide whether such ports remain novelties or become common.
