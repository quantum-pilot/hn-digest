# Ghostty – Terminal Emulator

- Score: 581 | [HN](https://news.ycombinator.com/item?id=47206009) | Link: https://ghostty.org/docs

- TL;DR  
  Ghostty is a GPU‑accelerated, cross‑platform terminal whose real long‑term bet is libghostty, a reusable core already powering many other terminals. The project has become a non‑profit with transparent finances and paid contributors, and the GUI gets ~1M macOS downloads weekly. HN discussion centers on missing but imminent features like scrollback search and Cmd‑F, SSH/terminfo rough edges, comparisons with WezTerm/Kitty/Foot, and how AI tools like Claude Code are driving a renaissance in terminal usage and expectations.

- Comment pulse  
  - Libghostty is the star → already used by dozens of free/commercial terminals; shared core should improve stability and diversify terminal UX experiments.  
  - Feature gaps block adoption → lack of stable search/scrollback and SSH/terminfo hassles push users to WezTerm, Kitty, Foot—counterpoint: tip builds and 1.3 address many.  
  - Emergent AI workflows reshape needs → new terminal‑centric users juggle 15–25 windows and want editor‑like text interaction, per‑window themes, and better window discovery.

- LLM perspective  
  - View: A strong embeddable terminal core plus thin UIs mirrors game engines; likely to standardize advanced VT behavior across platforms.  
  - Impact: TUI authors can target libghostty once, gaining GPU rendering and modern features without per-terminal quirks and patches.  
  - Watch next: benchmarks vs WezTerm/Kitty, broader Linux packages, and improved SSH/terminfo story to make Ghostty safer as a primary terminal.
