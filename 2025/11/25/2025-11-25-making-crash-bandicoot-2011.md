# Making Crash Bandicoot (2011)

- Score: 190 | [HN](https://news.ycombinator.com/item?id=46045039) | Link: https://all-things-andy-gavin.com/video-games/making-crash/

### TL;DR

This page collects Andy Gavin’s multipart retrospective on how a two-person Naughty Dog grew around a PlayStation mascot opportunity. The linked summaries span character design, custom engine and tools, repeated control rewrites, box-heavy level design, naming, launch, localization, and GOOL, an in-house Lisp dialect. HN discussion supplied the sharpest technical detail: the game’s linear route let developers pre-sort polygons and arrange disc data offline, overcoming the console’s missing z-buffer, two megabytes of RAM, slow optical seeks, and limited compute.

### Comment pulse

- Linear levels enabled visual density → offline polygon sorting avoided a z-buffer and scheduled assets along the player’s expected path.
- Hardware constraints shaped tooling → artists’ SGI workstations formed a makeshift cluster because each level’s preprocessing took about an hour.
- The retrospective foregrounds iteration → controls were rewritten repeatedly, while art, engine, enemy density, naming, and localization evolved together.

### LLM perspective

- View: The celebrated look came from designing game structure and build tooling around hardware limitations.
- Impact: Constraint-aware architecture let a tiny studio compete visually and establish a durable console franchise.
- Watch next: Linked chapters on GOOL, streaming layout, Japanese localization, control tuning, and production tradeoffs.
