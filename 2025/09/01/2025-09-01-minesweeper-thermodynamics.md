# Minesweeper thermodynamics

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45093966) | Link: https://oscarcunningham.com/792/minesweeper-thermodynamics/

### TL;DR

When Minesweeper forces a guess, locally valid mine arrangements are not equally probable because they consume different numbers of the board's remaining mines. Each local state should be weighted by the number of compatible arrangements elsewhere, expressed with a binomial coefficient. The author compares this “mine bath” to statistical mechanics: for a small boundary region, weights approximately follow a Boltzmann-like exponential in local mine count, producing a board-dependent “mine temperature.” The approximation captures scale but is noticeably inaccurate on an ordinary expert board.

### Comment pulse

- Readers discussed forgiving or guaranteed-solvable variants, versus preserving forced guesses as part of the game's character.
- Suggested solvers combine mine probabilities, information gain, particle filtering, and limited game-tree lookahead.

### LLM perspective

- View: The thermodynamic analogy makes a practical counting correction memorable without replacing the exact combinatorics.
- Impact: Proper weighting can radically reorder candidate clicks compared with treating locally valid states equally.
- Watch next: A solver could compare exact weighting, the Boltzmann approximation, and information-aware strategies across real boards.
