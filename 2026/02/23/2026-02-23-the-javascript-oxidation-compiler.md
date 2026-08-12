# The JavaScript Oxidation Compiler

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47117459) | Link: https://oxc.rs/

### TL;DR

Oxc is a Rust-based JavaScript and TypeScript toolchain spanning linting, formatting, parsing, transformation, module resolution, and minification. The project reports substantial speedups over established tools, broad ESLint compatibility, hundreds of lint rules, and growing React, TypeScript, and Tailwind integrations. However, Oxfmt and the minifier remain alpha-stage, so benchmark claims and compatibility need workload-specific testing. Commenters praised fast, statically linked distribution and reported large-repository gains, while one user objected that Oxfmt’s no-argument mode recursively reformatted files by default.

### Comment pulse

- One anecdote put linting roughly 100,000 TypeScript files at three seconds, reinforcing interest in replacing slower JavaScript tooling.
- Some called recursive formatting surprising and unsafe; others viewed it as normal formatter behavior and stressed using version control.
- Readers also questioned how VoidZero will fund sustained development, with paid services around the ecosystem mentioned as one possibility.

### LLM perspective

- **View:** Toolchain consolidation reduces startup and compatibility overhead, but also expands the blast radius of immature defaults.
- **Impact:** Large repositories gain immediate CI time; formatter mistakes can rewrite entire trees much faster.
- **Watch next:** Stable formatter and minifier releases, dry-run defaults, compatibility corpora, funding model, and measured migration costs.
