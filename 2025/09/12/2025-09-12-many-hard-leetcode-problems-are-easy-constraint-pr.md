# Many hard LeetCode problems are easy constraint problems

- Score: 391 | [HN](https://news.ycombinator.com/item?id=45222695) | Link: https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/

### TL;DR

Hillel Wayne argues that many interview puzzles become straightforward when expressed for a constraint solver such as MiniZinc. Coin change, stock-profit optimization, three-number satisfaction, and largest-histogram-rectangle examples replace bespoke dynamic programming or bookkeeping with variables, objectives, and constraints. Solvers may be slower and have less predictable complexity than tailored algorithms, but adapt easily when requirements change. Commenters disputed interview relevance: some saw solver knowledge as practical engineering breadth, while others said such questions intentionally test algorithm construction, memorized patterns, communication, or cleverness.

### Comment pulse

- Several commenters criticized automated screening where candidates cannot clarify ambiguous questions or explain their reasoning.
- Others said constraint solvers are underused professionally and would treat recognizing the tool as a positive signal.

### LLM perspective

- View: Modeling skill and algorithm-writing skill overlap, but an interview should state which one it intends to measure.
- Impact: Solvers trade optimal runtime for rapid, adaptable correctness when requirements are complex or changing.
- Watch next: Benchmark solver formulations against bespoke solutions and test how each responds to added constraints.
