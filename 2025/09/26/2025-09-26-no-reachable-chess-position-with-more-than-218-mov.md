# No reachable chess position with more than 218 moves

- Score: 337 | [HN](https://news.ycombinator.com/item?id=45382755) | Link: https://lichess.org/@/Tobs40/blog/there-is-no-reachable-chess-position-with-more-than-218-moves/a5xdxeqs

### TL;DR

The result concerns branching, not game length: 218 is claimed as the maximum number of legal next moves available in any chess position reachable from the standard start. The author modeled pieces, squares, attacks, and move counts as a mixed-integer optimization problem, using relaxed fractional solutions and added constraints to prune an enormous search. Gurobi proved an upper bound of 218, while a constructed proof game establishes reachability. The work also reports 144 as the promotion-free maximum, 271 for legal but unreachable positions, and 288 for an illegal arrangement.

### Comment pulse

- Many readers initially misunderstood “218 moves” as game length, prompting calls for “possible next moves” in the title.
- Discussion clarified that an optimizer supplies a global bound, assuming correct modeling, implementation, and solver behavior.

### LLM perspective

- View: The clever step is translating chess legality into bounds strong enough to turn computation into a proof.
- Impact: Optimization solvers can settle finite combinatorial records when both an upper-bound certificate and matching construction exist.
- Watch next: Independent model verification and whether similar formulations can solve maxima for checks, captures, or mating moves.
