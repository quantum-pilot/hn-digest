# Inside the M4 Apple Neural Engine, Part 1: Reverse Engineering

- Score: 247 | [HN](https://news.ycombinator.com/item?id=47208573) | Link: https://maderix.substack.com/p/inside-the-m4-apple-neural-engine

### TL;DR

A human–Claude team reverse-engineered the M4 Neural Engine’s private software path, bypassing CoreML through _ANEClient to compile MIL graphs, load E5 programs, and execute them using IOSurface buffers. They characterize the 16-core H16G as a fixed-function graph engine with a 127-request queue, independent power management, tiny parameterized binaries, and an imperfectly in-memory compiler route. The work prepares later performance and training experiments rather than fully exposing the ISA. Commenters praised the depth but questioned AI-assisted verification and noted that mainstream open-source numerical libraries rarely target Apple’s NPU.

### Comment pulse

- Prior Asahi and M1/M2 work covered fundamentals; readers valued M4 confirmation and deeper exploration of private frameworks.
- For large matrix multiplications, commenters say CoreML overhead may already be small, limiting direct-access gains for some workloads.
- Skeptics distrust AI-written analysis — counterpoint: others argue reverse engineering always requires independent reproduction, regardless of authorship.

### LLM perspective

- **View:** The strongest contribution is a runnable interface map that converts opaque hardware into testable hypotheses.
- **Impact:** Direct access could unlock specialized local inference and research, but private APIs impose fragility and distribution barriers.
- **Watch next:** Reproducible benchmarks, training results, operation coverage, OS-version stability, and third-party validation of claimed throughput and power.
