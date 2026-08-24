# Helping Valve to power up Steam devices

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46006616) | Link: https://www.igalia.com/2025/11/helpingvalve.html

### TL;DR

Igalia details the open-source stack enabling Valve’s ARM-based Steam Frame to run desktop games. FEX translates x86 machine code to ARM64, while Mesa Turnip supplies Vulkan support for the Adreno 750 GPU, including new hardware coverage, optimizations, extensions, and rendering fixes. Turnip passes more than 2.8 million conformance tests, yet engineers also capture game frames because real rendering regressions can evade generic suites. Related work covers an energy-aware Linux scheduler and HDR support; improvements also reach Android gamers and older Snapdragon hardware.

### Comment pulse

- Open development compounds Valve’s investment → third-party users expose bugs and inherit faster, more correct drivers — counterpoint: broader compatibility expands Valve’s storefront.
- An ARM handheld remains speculative → the Frame proves software readiness, but commenters doubt current non-Apple chips deliver Valve’s desired performance leap.

### LLM perspective

- View: The durable product is shared compatibility infrastructure, not one device.
- Impact: ARM Linux gaming gains viable translation and graphics layers, benefiting vendors beyond Valve.
- Watch next: Frame benchmarks, FEX compatibility, Turnip regressions, battery efficiency, and future handheld architecture.
