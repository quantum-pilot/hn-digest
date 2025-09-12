# Minesweeper thermodynamics

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45093966) | Link: https://oscarcunningham.com/792/minesweeper-thermodynamics/

- TL;DR
    - The author shows that in ambiguous Minesweeper positions you should weight each local mine pattern by the number of global completions consistent with total remaining mines (a binomial factor), yielding sharply different cell-safety probabilities. They connect this to the Boltzmann distribution, deriving a “mine temperature” T≈1/log(M/(C−M)); it’s a useful small-m approximation but not exact. HN discusses solvable/forgiving variants and first-click safety, NP-hardness and guessing, unit choices around Boltzmann’s k, and probabilistic solvers and pure-logic alternatives.

- Comment pulse
    - Enforce no-guess play → supply safe moves or generate unambiguous boards; improves fairness — counterpoint: removes essential uncertainty; guessing teaches tradeoffs.
    - First move is usually forced safe; extending safety globally may require exponential checks, hinting at NP-complete subproblems.
    - Particle-filter solvers maintain mine distributions, maximize expected information gain, and simulate lookahead to pick safer, higher-yield moves.

- LLM perspective
    - View: Treat local patterns as microstates; use weighted counting or MCMC sampling when counts are intractable.
    - Impact: Improves bot win rates and human heuristics on expert boards, especially under forced-guess scenarios.
    - Watch next: Benchmark solvers: naive equal-pattern vs combinatorial weighting vs particle filters; report win rate, clicks-to-win, and time per move.
