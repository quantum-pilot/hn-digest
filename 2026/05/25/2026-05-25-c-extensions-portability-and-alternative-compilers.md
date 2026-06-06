# C extensions, portability, and alternative compilers

- Score: 132 | [HN](https://news.ycombinator.com/item?id=48267126) | Link: https://lemon.rip/w/6-c-extensions-compilers/

- TL;DR
    - C compiler authors trying to support real-world code quickly discover that “ISO C” is overshadowed by GCC/Clang-specific extensions baked into libc and popular libraries. The post walks through glibc, SDL, OpenBSD, and Android bionic examples where headers assume particular compilers, inline semantics, or attributes, making alternative compilers fragile unless they impersonate GCC. Commenters add more horror stories from ImportC and slimcc, debate platform obligations, and argue for better feature-test macros instead of compiler-name checks.

- Comment pulse
    - Many C projects "just work on my Linux"; Windows/FreeBSD users hit GCC/Clang assumptions, systemd, non-POSIX features—counterpoint: maintainers needn't support every platform.
    - Compiler authors (ImportC, slimcc) report effort fighting libc headers: GCC-only attributes, inline semantics, VLAs, visibility, SIMD defaults, buggy fallbacks, even headers that #error on non-GCC.
    - People suggest GLIBC_COMPILER_SUPPORTS_ATTRIBUTES or __has_* feature flags; others note devs gravitate to compiler/version checks, postponing flags until pain forces costly refactors.

- LLM perspective
    - View: Real-world C is a de facto dialect: GCC/Clang extensions plus platform headers; standards conformance alone won't compile major software.
    - Impact: Alternative compilers must emulate GCC/Clang quirks or ship header shims, limiting innovation and increasing maintenance for small teams.
    - Watch next: Broader adoption of standardized feature-test macros and portability libraries could decouple code from specific compilers without demanding heroic multi-compiler testing.
