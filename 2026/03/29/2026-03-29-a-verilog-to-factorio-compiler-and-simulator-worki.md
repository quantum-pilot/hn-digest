# A Verilog to Factorio Compiler and Simulator (Working RISC-V CPU)

- Score: 142 | [HN](https://news.ycombinator.com/item?id=47528853) | Link: https://github.com/ben-j-c/verilog2factorio

### TL;DR

v2f turns Verilog hardware descriptions into JSON blueprints for Factorio 2.0 combinator circuits, using Yosys for synthesis and a Rust backend for placement and simulation. It also exposes Rust and Lua design APIs, renders annotated SVGs, and offers a limited browser GUI. Its showpiece is a fully functional RV32IM RISC-V processor, wrapped with programmable RAM and display output, that runs compiled C programs inside the game. HN’s reaction was mostly delight at the improbable toolchain, tempered mainly by warnings that Factorio consumes weekends and sleep.

### Comment pulse

- Verilog-to-game compilers were celebrated as playful demonstrations that automation systems can implement general computation.
- The browser demo omits Yosys, so the complete Verilog flow still needs Codespaces, Docker, or a manual toolchain.
- The frowning smiley caused by an ASCII-font bug became an endearing sign that the in-game CPU truly ran.

### LLM perspective

- **View:** The project is valuable less as a practical CPU than as a bridge from HDL semantics to physical placement.
- **Impact:** Factorio builders can iterate on large circuits in code, simulate them, and import reproducible layouts.
- **Watch next:** Synthesis coverage, timing semantics, blueprint size, placement quality, simulator parity, browser Yosys, and Factorio update compatibility.
