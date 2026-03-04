# Claude's Cycles [pdf]

- Score: 413 | [HN](https://news.ycombinator.com/item?id=47230710) | Link: https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf

### TL;DR
Knuth describes how an open combinatorics problem about decomposing a 3D Cayley digraph into three directed Hamiltonian cycles was cracked for all odd m by collaboration with Anthropic’s Claude 4.6. Guided by a human “coach,” Claude iteratively searched, reformulated the problem (fibers, serpentine/Gray-code patterns), and produced a working constructive algorithm. Knuth then supplied rigorous proofs, classified all relevant 3×3×3 Hamiltonian cycles, and showed exactly 760 “Claude‑like” constructions work for every odd m>1. The even-m case remains open, but Knuth’s stance on LLMs clearly shifts.

---

### Comment pulse
- LLMs as reusable “probability distributions of workflows” → RL, logging, and larger context windows may let models continuously absorb frontier reasoning—counterpoint: expensive and architecturally tricky.  
- Knuth had been publicly dismissive of GPT‑4; people highlight this as Bayesian updating in action: strong priors revised by striking new evidence.  
- Debate on “who solved it” → Claude explored and found a general construction; humans provided direction, checking, and proofs, exemplifying tight human–LLM research synergy and exposing context limits (“dumb zone”).

---

### LLM perspective
- View: This is a concrete example of LLMs doing genuine mathematical discovery, not just regurgitation, when scaffolded with tools and discipline.  
- Impact: Changes how serious researchers may use LLMs—as exploratory co-authors for conjectures, constructions, and search over combinatorial spaces.  
- Watch next: Stronger tool-use agents, formal proof integration, and attacks on the remaining even‑m case will test how far this paradigm scales.
