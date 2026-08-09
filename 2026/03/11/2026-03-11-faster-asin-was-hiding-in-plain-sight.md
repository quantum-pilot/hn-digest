# Faster asin() was hiding in plain sight

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47336111) | Link: https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/

### TL;DR

While optimizing a ray tracer, the author replaced std::asin with Taylor and Padé approximations, gaining about 5% but finding no extra speed from Padé. A Gemini query then surfaced an old Nvidia Cg minimax formula using a branchless polynomial and square root. It cut the sample render from roughly 111 to 101 seconds; microbenchmarks showed 1.47–1.90× gains on Intel, but only 1.02–1.05× on Apple M4. HN stressed interval-wide error analysis and recommended minimax, Remez, or Chebyshev methods over Taylor-centered approximations.

### Comment pulse

- Approximation needs maximum or relative error over a defined interval → visual similarity and aggregate sums are insufficient guarantees.
- Old numerical references remain valuable → the formula's exact provenance prompted debate, but it clearly predates modern AI tools.
- Library implementations may already be highly tuned → speedups depend on hardware, compiler, precision, and domain tolerance.

### LLM perspective

- **View:** Research the objective and prior art before inventing custom numerical code.
- **Impact:** Graphics hot paths can gain speed where carefully bounded approximation error is acceptable.
- **Watch next:** Maximum-ULP measurements, AMD and SIMD tests, float-versus-double results, and compiler sensitivity.
