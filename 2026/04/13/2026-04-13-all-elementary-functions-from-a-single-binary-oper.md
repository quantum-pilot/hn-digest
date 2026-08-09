# All elementary functions from a single binary operator

- Score: 784 | [HN](https://news.ycombinator.com/item?id=47746610) | Link: https://arxiv.org/abs/2603.21852

### TL;DR

Andrzej Odrzywołek defines EML(x,y)=exp(x)−ln(y) and claims that this one binary operator plus constant 1 can construct a scientific calculator’s elementary repertoire: e, π, i, arithmetic, powers, logarithms, trigonometric functions, and algebraic functions. Every expression becomes a binary tree under the grammar S→1|EML(S,S). Found through exhaustive search, the construction also supports trainable symbolic-regression trees; shallow depth-4 experiments recovered exact formulas from data. Commenters noted older universal operators exist, but debated whether they likewise yield constants and transcendental closed forms without limits.

### Comment pulse

- A reciprocal-difference operator may already generate arithmetic, invoking older universality results — counterpoint: its ability to express π, e, and transcendental functions remained disputed.
- Readers connected EML trees to FRACTRAN, concatenative languages, Iota, and compact encodings where a tiny primitive system generates surprising complexity.
- An informal LLM benchmark asked models to express 2x+y in EML; results ranged from immediate success to circularity claims and hallucinated terminology.

### LLM perspective

- **View:** The contribution is less operational efficiency than a constructive normal form unifying elementary expressions into one repeatable tree architecture.
- **Impact:** Uniform nodes could simplify symbolic search and differentiable program synthesis, though derived expressions may be deep and numerically fragile.
- **Watch next:** Independent proof review, minimal-depth catalogs, conditioning tests, comparisons with earlier universal operators, and symbolic-regression benchmarks beyond depth four.
