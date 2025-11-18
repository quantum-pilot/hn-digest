# GCC 16 considering changing default to C++20

- Score: 92 | [HN](https://news.ycombinator.com/item?id=45953202) | Link: https://inbox.sourceware.org/gcc/aQj1tKzhftT9GUF4@redhat.com/

- TL;DR
  - GCC 16 may switch its default C++ mode to C++20. HN welcomes modernization but warns about breaking builds that rely on old defaults, toolchain bootstrapping constraints (especially for distros), and still-incomplete support for parts of C++20/23. Many advocate always passing -std for reproducibility. Modules remain contentious and likely won’t be enabled by default. Open questions include coroutine interoperability/ABI across GCC and Clang. Side chatter notes the site’s anime-style gate.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Pin the standard with -std → reproducible builds across SDKs/compilers; big shops do this — counterpoint: default shifts still break transitive dependencies you don’t control.
  - Bleeding-edge defaults are risky → compilers must bootstrap with older toolchains; distros plan releases that way; C++23 support remains incomplete.
  - Modules raise concerns → seen as broken by some and unlikely to be enabled by default.

- LLM perspective
  - View: Defaulting to C++20 is reasonable; teams should explicitly set -std and audit flags to avoid surprise feature/behavior changes.
  - Impact: Biggest impact on distro builds, cross-compilers, and libraries with implicit assumptions about pre-C++20 defaults.
  - Watch next: Track GCC cxx-status, modules default policy, and interop tests for coroutine ABI between GCC and Clang.
