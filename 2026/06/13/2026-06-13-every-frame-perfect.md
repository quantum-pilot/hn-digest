# Every Frame Perfect

- Score: 844 | [HN](https://news.ycombinator.com/item?id=48516251) | Link: https://tonsky.me/blog/every-frame-perfect/

### TL;DR

An interface should remain coherent at every instant, the author argues, because users infer software quality and trust from visible polish. That means avoiding flashes, partial loads, layout shifts, contradictory states, and animations whose components move out of sync or imply changes that never occurred. Safari, Photos, YouTube, and Preview illustrate transitions that work only at their endpoints. HN agreed janky motion erodes quality but challenged screenshot-by-screenshot evaluation: perception is temporal, motion blur can be correct in context, and many animations should simply be removed.

### Comment pulse

- A frozen frame is an incomplete test → motion blur and in-betweens can improve real-time perception — counterpoint: logically contradictory states still expose careless implementation.

- Animation needs purpose → motion can preserve spatial continuity and mask delays, but decorative transitions add latency, distraction, and cognitive load.

- Critique should demonstrate alternatives → commenters wanted corrected clips and user-impact explanations, while others defended the essay as a useful design heuristic.

### LLM perspective

- **View:** Treat frame coherence as a diagnostic, not an absolute; evaluate transitions at normal speed, slowed down, and when interrupted.

- **Impact:** Designers and engineers gain a shared way to inspect synchronization bugs before users interpret them as unreliable behavior.

- **Watch next:** Prototype alternatives, test comprehension and latency, respect reduced-motion settings, and measure frame drops, layout shifts, and task completion.
