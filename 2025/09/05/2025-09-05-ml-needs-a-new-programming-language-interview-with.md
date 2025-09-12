# ML needs a new programming language – Interview with Chris Lattner

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45137373) | Link: https://signalsandthreads.com/why-ml-needs-a-new-programming-language/

- TL;DR
  - Chris Lattner argues ML needs a language built for today’s accelerators. Mojo pairs a Pythonic surface with type-safe metaprogramming to expose hardware details (tensor cores) while retaining productivity and portability across GPUs/TPUs. It underpins Modular’s stack (Mojo + MAX + Mammoth) to unify fragmented AI software. Compile-time execution enables library-driven specialization; AI coding lowers adoption friction. HN reactions: Python ecosystem inertia, licensing/governance skepticism, and doubts about “Python superset” maturity; alternatives like Elixir/Nx or plain C++ seen as viable for services/inference.

- Comment pulse
  - Python dominates ML apps → richest ecosystem and FFIs for data/orchestration/visualization outweigh kernel languages — counterpoint: Elixir/Nx or pure C++ can rival for services/inference.
  - License/governance worry → company-controlled language and MAX licensing per accelerator feels risky for vendors and enterprises.
  - Mojo maturity skepticism → “Python superset” messaging vs missing features (e.g., classes) creates doubt — counterpoint: long-term goal; OOP intentionally deprioritized.

- LLM perspective
  - View: Mojo’s unification bet hinges on library-first metaprogramming that targets tensor cores while staying Pythonic enough for adoption.
  - Impact: If it delivers parity beyond Nvidia, pressure shifts to CUDA/ROCm and PyTorch extensions; hardware vendors lose some software gatekeeping.
  - Watch next: Clear, liberal license; reproducible cross-vendor benchmarks; class/type system roadmap; PyTorch/vLLM interop; stable MAX/Mammoth releases on AMD, Nvidia, and TPUs.
