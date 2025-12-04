# 1D Conway's Life glider found, 3.7B cells long

- Score: 286 | [HN](https://news.ycombinator.com/item?id=46137253) | Link: https://conwaylife.com/forums/viewtopic.php?&p=222136#p222136

## TL;DR
A Life enthusiast (Hippo.69) has finished a “unidimensional spaceship” in Conway’s Game of Life: a pattern that starts as a single horizontal line about 3.7 billion cells long, evolves into a vast 2D construction spanning roughly 10¹⁰×10¹⁰ cells, and then returns to a (shifted) single line after 133,076,755,768 generations, effectively acting as a 1D glider. Building it required elaborate engineered components (corderships, ECCA2 circuitry, tape-reading logic), careful seed debugging, and custom big‑integer stepping scripts to drive Golly/hashlife.

---

## Comment pulse
- Jargon overload → Readers are stunned by the dense “cellular automata” vocabulary (ECCA, corderships, agnosticized recipes) and head to LifeWiki / the free book to decode it.  
- Structure intuition → Yes, the 1D line blows up into a huge 2D machine and later re-collapses into a slightly shifted sparse line (<1% live cells).  
- Big-picture questions → Discussion drifts to random initial conditions, self-replicating Life “organisms,” superstable patterns, and what counts as “life” or intelligence in cellular automata.  

---

## LLM perspective
- View: This is extreme engineering in a mathematically simple system, showing how far manual design plus automation can push Life constructions.  
- Impact: Gives Life researchers a flagship 1D spaceship, plus reusable techniques for debugging and fast-simulating enormous engineered patterns.  
- Watch next: Simplified explanations, visualizations, and higher-level “compiler” tools that assemble such ships from modular components automatically.
