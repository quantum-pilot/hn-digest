# I replaced Animal Crossing's dialogue with a live LLM by hacking GameCube memory

- Score: 805 | [HN](https://news.ycombinator.com/item?id=45192655) | Link: https://joshfonseca.com/blogs/animal-crossing-llm

### TL;DR

The project gives emulated GameCube Animal Crossing villagers live LLM dialogue without changing the original game's source. A Python process scans and reads Dolphin memory, uses fixed RAM addresses as a mailbox, and writes responses encoded with the game's control codes. Separate Writer and Director models generate character text and add pauses, colors, expressions, and sounds; news and shared gossip provide context. HN admired the playful reverse engineering but noted latency tricks, cloud dependence, lore leakage, invented world details, and limited narrative reliability.

### Comment pulse

- A loading dialogue hides inference latency → the player advances text while the external model prepares a response.
- Dynamic NPCs improve novelty but weaken boundaries → models can import modern references or invent places the game cannot support.
- Scripted repetition has design value → it signals exhausted interactions and protects authored story consistency.

### LLM perspective

- View: The memory mailbox is the enduring insight; the model is a replaceable component behind a clean legacy bridge.
- Impact: Modders can reinterpret old virtual worlds, though remote inference threatens preservation and offline play.
- Watch next: Local models, real-hardware networking, latency measurements, lore constraints, safety controls, and integration with game state.
