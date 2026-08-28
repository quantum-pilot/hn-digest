# Eternal Struggle

- Score: 680 | [HN](https://news.ycombinator.com/item?id=45086020) | Link: https://yoavg.github.io/eternal/

### TL;DR

This code-only interactive sketch renders a black-and-white circular arena whose two moving balls reshape their shared boundary on collision. The program maintains boundary-point density, constrains motion to the outer circle, starts after mouse movement or a delay, and lets a click randomize ball direction. Pressing `p` toggles boundary points, while `w` accelerates repeated update-and-render cycles. Commenters describe an apparent balancing mechanism, because the ball in the smaller region encounters the boundary more often, but they also report crossings, glitches, and stable unequal configurations.

### Comment pulse

- A community fork added a speed slider, though users reported it could not slow the animation after reaching 64×.
- Discussion treated the equilibrium explanation as an observation, not a guarantee; several readers found counterexamples.

### LLM perspective

- View: The sketch turns a simple collision rule into an evocative, imperfect model of competing regions.
- Impact: Visible glitches are part of the experiment’s interest but weaken strong claims about self-balancing behavior.
- Watch next: Boundary-crossing fixes and reproducible tests of unequal equilibria would clarify what the rules actually guarantee.
