# How Pizza Tycoon simulated traffic on a 25 MHz CPU

- Score: 263 | [HN](https://news.ycombinator.com/item?id=47703123) | Link: https://pizzalegacy.nl/blog/traffic-system.html

### TL;DR

Pizza Tycoon’s 1994 traffic looked convincing on a 25 MHz 386 by simulating appearance, not destinations. Each road tile encoded permitted directions; cars moved one pixel per tick, ran heavier routing logic only every 16 pixels, chose turns randomly, and paused ten ticks when blocked. Pairwise collision checks were nominally O(n²), but direction and lane tests rejected most pairs immediately. Cars spawned probabilistically from visible roads and recycled at screen edges. HN emphasized that no pathfinding was needed because cars were not going anywhere.

### Comment pulse

- Readers recognized a conveyor-belt model → road lanes own movement, though stopped cars mean spacing is not static.
- The key simplification was questioned precisely → no pathfinding works because traffic has no destination, not merely because tiles encode directions.
- Nostalgia centered on the remake → players recalled economic exploits, crashes, and retro games that achieved startling results on limited hardware.

### LLM perspective

- **View:** The design succeeds by matching simulation fidelity to its visual purpose instead of modeling real traffic.
- **Impact:** Game developers can trade generality for deterministic map rules, sparse updates, and aggressive early exits.
- **Watch next:** Whether Pizza Legacy reproduces long-running intersection quirks while keeping the new engine maintainable and open.
