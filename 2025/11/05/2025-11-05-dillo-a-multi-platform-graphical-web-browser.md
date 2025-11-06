# Dillo, a multi-platform graphical web browser

- Score: 278 | [HN](https://news.ycombinator.com/item?id=45826266) | Link: https://github.com/dillo-browser/dillo

- TL;DR
    - Dillo is a long-running, ultra-light, FLTK-based browser still actively maintained in 2025 (e.g., OAuth redirect-cookie support, mouse back/forward, CI, Arch FLTK 1.3 handling, fixes). The maintainer is migrating to a JS-free, self-hosted site/repos/bug tracker, with GitHub to be archived after a transition. HN mixes nostalgia for speed on old/weak hardware, questions about future HTML/CSS support and release notifications, critiques of web bloat, and a plug for Blitz, a modern lightweight engine.

- Comment pulse
    - JS-free, self-hosted workflow → enables dogfooding; CI via git hooks; GitHub mirror now, archive later — counterpoint: why leave, and how to track releases?
    - Excels on old hardware → fast FLTK and minimal features; users cite Puppy Linux and PineTab 2; strategy: bookmark lightweight sites.
    - Alternative engine Blitz pitched → modern CSS (Flexbox/Grid/vars), working on floats; questions about Servo components, Wasm, and JS engine.

- LLM perspective
    - View: Active, ultra-light browser with pragmatic OAuth cookie handling still matters for retro, kiosk, and constrained systems.
    - Impact: Autonomy shift may shrink GitHub-driven contributions; clarity on feeds, mirrors, and how to submit bugs will determine community health.
    - Watch next: Publish release RSS/Atom, document HTML/CSS support targets, and benchmark against NetSurf and Blitz on low-end devices.
