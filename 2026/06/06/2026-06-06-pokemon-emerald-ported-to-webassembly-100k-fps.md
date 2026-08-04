# Pokemon Emerald Ported to WebAssembly (100k FPS)

- Score: 259 | [HN](https://news.ycombinator.com/item?id=48423762) | Link: https://pokeemerald.com/

### TL;DR

pokeemerald-wasm packages the game into an 11.6 MiB WebAssembly build playable in a browser, with on-screen directional and A/B/Start/Select controls, keyboard input, and selectable speed. The page exposes separate display and game FPS counters, but the supplied content does not substantiate the title’s 100,000-FPS figure or explain the porting approach. HN users confirmed that saves persist and welcomed fast-forwarding, while reporting a Pokémon combat-menu crash, item names rendered as numbers, and failed trading attempts. Requests focused on visible key instructions, remapping, and more ergonomic defaults; the author promised fixes.

### Comment pulse

- Core persistence works → users verified saving, making the browser build usable beyond a demonstration.
- Input needs discoverability → Z/X mappings were guesswork for newcomers, and fixed Enter/arrow layouts motivated remapping requests.
- Compatibility remains incomplete → selecting Pokémon during battle can crash, some item names become numbers, and trading attempts failed.

### LLM perspective

- **View:** The practical milestone is stateful browser play; an unexplained headline FPS number contributes little.
- **Impact:** A compact browser build lowers launch friction for players and creates an accessible target for porting experiments.
- **Watch next:** Publish build methodology, benchmark definitions, source availability, save-storage behavior, compatibility tests, and networking plans.
