# Pokemon Emerald Ported to WebAssembly (100k FPS)

- Score: 259 | [HN](https://news.ycombinator.com/item?id=48423762) | Link: https://pokeemerald.com/

- TL;DR  
Browser-based WebAssembly port of Pokémon Emerald runs the GBA game locally at extremely high frame rates via an 11.6 MiB wasm binary. Players use keyboard controls mapped to Game Boy buttons, with some friction around discovering the mappings. Early testers treat the post as a live playtest, reporting crashes in specific battle menus and odd text-rendering issues. The thread focuses on usability polish, bug reports, and curiosity about how far this approach can go for fully in-browser retro gaming.

- Comment pulse  
  - Control discoverability is weak → on-screen buttons hide that Z/X/Enter/Shift are mapped; users request remappable keys and Start key — counterpoint: emulator veterans expect Z/X.  
  - Early testers surface correctness bugs → battle menu can crash, some item or reward texts show raw numbers instead of names, requiring further debugging.  
  - Core features extend beyond a toy demo → saving works reliably, people hope for link-style trading, and compare efforts with other recent WASM game ports and static recompilers.

- LLM perspective  
  - View: Fan-made WASM ports plus decompilation projects hint at a browser-native retro ecosystem, bypassing traditional emulators and installations.  
  - Impact: If performance and compatibility improve, classrooms, tournaments, and casual play could shift to self-contained URLs instead of ROM managers.  
  - Watch next: Benchmarking networked features like trading or multiplayer in WASM ports will show whether browser-based retro gaming can support social mechanics.
