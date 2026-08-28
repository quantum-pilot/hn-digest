# Building a DOOM-like multiplayer shooter in pure SQL

- Score: 240 | [HN](https://news.ycombinator.com/item?id=45183050) | Link: https://cedardb.com/blog/doomql/

### TL;DR

DOOMQL is a terminal multiplayer shooter that stores maps, players, inputs, sprites, and configuration in CedarDB, then implements raycasting, sprite projection, occlusion, HUDs, and minimaps through SQL views. A shell script runs transactional game logic near 30 ticks per second, while roughly 150 lines of Python handle keyboard input and display. The author reports a 128-by-64 player view in about 33 milliseconds. Direct superuser SQL deliberately enables a cheating metagame, showcasing database synchronization while remaining explicitly unsuitable as production game architecture.

### Comment pulse

- The earlier DuckDB demo’s author praised the multiplayer extension and minimap view cone.
- Commenters admired the SQL work while disputing “pure SQL” and whether the simple raycaster is meaningfully Doom-like.

### LLM perspective

- View: The renderer is a stunt, but transactional shared state is a serious demonstration of database strengths.
- Impact: Treating game entities as relations makes concurrency and live modification unusually concise, though security is intentionally absent.
- Watch next: Scaling across players, role-based access, higher tick rates, optimizer behavior, and more conventional client boundaries.
