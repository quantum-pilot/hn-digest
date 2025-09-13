# Many hard LeetCode problems are easy constraint problems

- Score: 391 | [HN](https://news.ycombinator.com/item?id=45222695) | Link: https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/

- TL;DR
  - The author shows many “hard” LeetCode problems become simple when modeled as constraints and solved with MiniZinc/Z3/OR-Tools (coin change, max stock profit, 3-number sum-with-signs, largest histogram rectangle). Solvers shine when requirements change—fast to rephrase—though runtimes are unpredictable and often worse than bespoke O(n) algorithms (capability/tractability tradeoff). HN debates interview fit: critics say LC rewards memorization and blocks clarifying questions; some would reward solver literacy, but many interviewers still expect hand-rolled algorithms.

- Comment pulse
  - LC process criticized: no clarifying questions, favors memorization; anxiety and surprise live-tests reported — counterpoint: pattern recognition is learnable, and GPT/explainers help.
  - Solver-in-interview split: some expect bespoke algorithms or even writing a solver; others consider solver modeling rare, valuable signal despite potential slowness.
  - What to test: “cleverness” vs real-world skills; suggestions include progressive, interactive problems and language-appropriate tools; claim DP ability predicts competence — counterpoint: mostly memorization.

- LLM perspective
  - View: Use solvers to prototype and validate; then migrate to specialized algorithms when performance predictability matters.
  - Impact: Hiring loops could reward correct modeling plus discussion of complexity trade-offs instead of single “textbook” solutions.
  - Watch next: Benchmarks on LC sets comparing MiniZinc/Z3/OR-Tools vs hand-coded; guides teaching constraint modeling and symmetry breaking to practitioners.
