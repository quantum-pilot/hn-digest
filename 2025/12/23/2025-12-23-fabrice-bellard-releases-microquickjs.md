# Fabrice Bellard Releases MicroQuickJS

- Score: 332 | [HN](https://news.ycombinator.com/item?id=46367224) | Link: https://github.com/bellard/mquickjs/blob/main/README.md

### TL;DR

MicroQuickJS is an MIT-licensed JavaScript engine for embedded systems that can run in roughly 10 kB RAM and occupy about 100 kB ROM while approaching QuickJS speed. It trades compatibility for a mostly ES5, always-strict subset, uses UTF-8 strings, persistent ROM-friendly bytecode, a bounded-stack VM, and a compacting tracing collector over a caller-supplied memory buffer. HN readers praised these restrictions and debated whether familiar JavaScript could displace Lua in small embedded scripting roles.

### Comment pulse

- Restrictions fit embedded systems → forbidding holes, direct eval, boxing, and other costly constructs simplifies predictable execution.
- JavaScript familiarity competes with Lua's design → syntax may lower onboarding friction, while Lua retains tail calls and proven embeddability.
- Browser builds show the footprint → one WebAssembly playground transferred 120 kB versus 675 kB for QuickJS.

### LLM perspective

- View: MicroQuickJS treats language compatibility as a resource budget, preserving useful JavaScript while rejecting expensive semantics.
- Impact: Firmware teams gain a recognizable scripting option for devices where conventional runtimes cannot fit.
- Watch next: Benchmark execution, worst-case pauses, C API safety, bytecode size, and real microcontroller integrations against Lua.
