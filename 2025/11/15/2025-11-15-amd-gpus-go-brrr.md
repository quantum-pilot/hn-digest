# AMD GPUs Go Brrr

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45934416) | Link: https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr

### TL;DR

Hazy Research presents HipKittens, tile-based primitives and scheduling patterns intended to unlock AMD CDNA3 and CDNA4 GPU performance without raw assembly. The authors argue Nvidia-style wave specialization fits AMD poorly because registers cannot be reallocated between producer and consumer waves. Their alternatives use eight-wave ping-pong or four-wave interleaving, plus layouts tailored to AMD memory instructions and chiplet-aware grid ordering. Reported kernels lead AMD baselines across tested workloads and, in some cases, compete with Nvidia Blackwell results, according to the project.

### Comment pulse

- Readers debated whether AMD should solve its software gap internally or leave room for independent research tooling.
- Experiences with ROCm ranged from effortless recent deployments to persistent consumer-GPU frustration.

### LLM perspective

- View: Portable GPU performance still requires architecture-specific abstractions rather than copying Nvidia’s execution model.
- Impact: Better primitives could turn AMD’s hardware capacity into practical AI competition without hiding its distinct design.
- Watch next: Whether HipKittens techniques enter mainstream frameworks and survive across more workloads and hardware generations.
