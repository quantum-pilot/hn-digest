# Building a DOOM-like multiplayer shooter in pure SQL

- Score: 240 | [HN](https://news.ycombinator.com/item?id=45183050) | Link: https://cedardb.com/blog/doomql/

TL;DR (70–90 words)
An engineer built DOOMQL: a multiplayer, DOOM‑like shooter whose state, logic, and 2.5D raycasting renderer run entirely as SQL views and transactions in CedarDB. A tiny Python client only sends inputs and fetches frames; a shell loop ticks ~30 Hz. Views assemble walls/sprites/minimap; frames are text rows. Single‑player render: ~33 ms at 128×64 (~30 FPS). Transactions synchronize players and blunt some cheats. HN applauds the stunt (and DuckDB‑DOOM inspiration), debates “pure SQL” purity and whether it’s DOOM—or more Wolf3D—and worth the attention.

Comment pulse
- Applause for creativity → Multiplayer, minimap cone, and SQL-only rendering impress; DuckDB‑DOOM author chimes in positively.
- “Pure SQL” caveat → Client uses ~150 lines of Python for input/loop. — counterpoint: Core state, renderer, and game loop logic are SQL transactions/views.
- Is it DOOM? → Feels closer to Wolfenstein 3D; some see “Does it run Doom?” stunts as distractors from richer mods or artful projects.

LLM perspective
- View: Databases can act as real-time game servers; ACID ensures consistent multiplayer state, though SQL rendering is a purposeful overreach.
- Impact: Shows CedarDB’s optimizer/predicate-pushdown and performance; validates ECS-like modeling of entities as rows with transactional updates.
- Watch next: Benchmark across Postgres, DuckDB, SQLite; decouple tick from movement; add RLS/auth to curb cheats; try WAD import or sprite packs.
