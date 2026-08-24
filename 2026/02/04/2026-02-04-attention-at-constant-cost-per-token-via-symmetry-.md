# Attention at Constant Cost per Token via Symmetry-Aware Taylor Approximation

- Score: 144 | [HN](https://news.ycombinator.com/item?id=46886265) | Link: https://arxiv.org/abs/2602.00294

### TL;DR

Researchers propose approximating softmax self-attention with symmetry-reduced Taylor polynomial features whose accumulated key-value state has fixed size, making inference cost per generated token independent of context length at a chosen truncation order. They report four terms reproduce conventional attention near Float16 elementwise precision and publish replication code. Commenters identified the crucial associative, incremental-state step, but questioned theoretical lower bounds, memory compression, sharp needle retrieval, and missing downstream model evaluations. Defenders stressed that increasing polynomial degree targets arbitrary precision, distinguishing it from first-order linear attention.

### Comment pulse

- Fixed state removes growing KV cache → Taylor feature sums update incrementally, exchanging context-dependent storage for a potentially large constant representation.
- Precision claim divides readers → four terms reportedly match Float16 error — counterpoint: sharp attention, exponent range, and long-context retrieval remain untested.
- Correctness is not usefulness → algebraic replication and code help, but pretrained conversions, fresh training, downstream quality, and wall-clock benchmarks are missing.

### LLM perspective

- View: The paper offers a technically distinct exactness path, but fixed-order efficiency and task-level fidelity are separate claims.
- Impact: If validated, long-context generation could use constant per-token compute and memory, with head dimension governing a steep fixed cost.
- Watch next: Independent replication, adversarial retrieval, higher precision, truncation by layer, pretrained model surgery, training stability, latency, and energy measurements.
