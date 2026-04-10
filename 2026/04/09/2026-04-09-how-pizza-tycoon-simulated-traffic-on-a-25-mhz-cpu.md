# How Pizza Tycoon simulated traffic on a 25 MHz CPU

- Score: 263 | [HN](https://news.ycombinator.com/item?id=47703123) | Link: https://pizzalegacy.nl/blog/traffic-system.html

- TL;DR  
Pizza Legacy’s author dissects how Pizza Tycoon’s bustling traffic ran on a 25 MHz 386 by radically simplifying the problem: road tiles encode one-way directions, cars advance one pixel per tick, intersections are random choices with a couple of cheap rules, and collision detection is naïve O(n²) but dominated by fast early exits. The HN thread digs into the idea that cars have no destinations, the power of lane-based reasoning, and nostalgia for clever, constraint-pushing games and exploits.

- Comment pulse  
  - Players recall abusing economy quirks—illegal-weapon “ice cream” trading, zero-cost tomato pizzas—and hope the open-source reimplementation fixes old crash bugs.  
  - Readers latch onto the “lanes, not intersections” abstraction and note cars lack destinations, simplifying logic—counterpoint: more realistic sims need pathfinding and stateful agents.  
  - Some compare the system to conveyor belts or Factorio optimizations, while others brainstorm jams and examples of games that wildly over-delivered on weak hardware.

- LLM perspective  
  - View: Encoding behavior into tile types shows how data-driven design plus randomness can replace complex AI for ambient life.  
  - Impact: Modern devs can often trade realism for perceived richness, using cheap heuristics and early exits instead of heavy simulations.  
  - Watch next: Test these minimalist traffic rules in modern city games, profiling CPU cost against more realistic physics and pathfinding.
