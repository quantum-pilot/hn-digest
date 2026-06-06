# Ratty – A terminal emulator with inline 3D graphics

- Score: 595 | [HN](https://news.ycombinator.com/item?id=48093100) | Link: https://ratty-term.org/

- TL;DR  
Ratty is a GPU-accelerated terminal emulator that can display inline 3D graphics and other rich visuals alongside traditional text. The project taps into a broader push to make terminals more like interactive canvases, borrowing ideas from notebooks, IDEs, VR-style interfaces, and old Lisp/Xerox systems. HN discussion ranges from excitement about practical uses like 3D previews and data-science workflows to skepticism about complexity, historical déjà vu, and terminal-bloat concerns. Underlying question: can such rich terminals stay fast, simple, and remote-friendly?

- Comment pulse  
  - 3D terminals as shallow XR spaces → devs imagine layered, depth-separated UIs, inline 3D glyphs, and VR/AR displays for code—counterpoint: colors/fonts already prototype UX cheaper.  
  - Not entirely new → commenters recall Xerox workstations, Lisp machines, TempleOS, and the Mother of All Demos showing inline graphics and richer REPLs decades ago.  
  - Practical angle → links to Kitty protocol, euporie, and hacks rendering 3D via terminals; people want notebook-style workflows, thumbnails, yet worry about SSH and portability.

- LLM perspective  
  - View: Playful but serious exploration of terminals as rich canvases, potentially unifying code, visualization, and REPLs without full GUI overhead.  
  - Impact: Most useful for power users, data scientists, graphics developers; mainstream adoption hinges on ergonomics, discoverability, and backward-compatible escape sequences.  
  - Watch next: Watch for standardizing terminal graphics protocols, headless/SSH behavior, and concrete workflows that beat existing IDEs or notebook-plus-viewer setups.
