# All elementary functions from a single binary operator

- Score: 784 | [HN](https://news.ycombinator.com/item?id=47746610) | Link: https://arxiv.org/abs/2603.21852

### TL;DR
The paper shows that a single smooth binary operator, eml(x, y) = exp(x) − ln(y), plus the constant 1, can generate all “elementary” functions a scientific calculator uses: arithmetic, exponentials, logs, trig, roots, and even constants like e, π, and i. Any such expression becomes a uniform binary tree over eml, enabling gradient-based training on the tree’s node parameters to perform symbolic regression. HN discussion contrasts this with older algebraic universality results and proposes it as a neat LLM benchmark.

---

### Comment pulse
- Universal single operators already exist in algebra (e.g., 1/(x−y)) → but they typically don’t yield standard constants or closed forms as finite expressions.
- Key novelty: finite eml trees give exact expressions (no limits) for usual elementary functions and constants—counterpoint: some think this is more encoding trick than deep math.
- People test LLMs by asking for explicit EML-only formulas → responses vary wildly, making this a useful, precise capabilities benchmark.

---

### LLM perspective
- View: EML gives a compact, homogeneous basis for continuous math, analogous to NAND for Boolean circuits.
- Impact: Could standardize symbolic-regression search spaces and enable differentiable “formula compilers” over a single operator.
- Watch next: depth/size bounds for representing real formulas, numerical stability analyses, and comparisons with other universal analytic operators.
