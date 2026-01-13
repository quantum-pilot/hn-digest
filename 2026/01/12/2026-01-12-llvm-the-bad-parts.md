# LLVM: The bad parts

- Score: 266 | [HN](https://news.ycombinator.com/item?id=46588837) | Link: https://www.npopov.com/2026/01/11/LLVM-The-bad-parts.html

### TL;DR
LLVM’s lead maintainer outlines systemic pain points not as reasons to avoid LLVM, but as targets for improvement. Social/organizational issues dominate: too many patches and too few qualified reviewers, unstable CI with flaky buildbots, heavy builds, and limited end‑to‑end and performance testing—especially across all backends. Technically, LLVM IR still has problematic constructs (like `undef`), incomplete formal semantics, messy constraint and floating‑point modeling, long‑running partial migrations (new pass manager, GlobalISel), and ad‑hoc handling of ABIs, libcalls, and LICM-induced register pressure.  
*Content available; summarizing article and comments.*

### Comment pulse
- Many users experience LLVM IR as fairly stable across versions → churn still real, but better managed than reputation suggests—counterpoint: different tools expect subtly different “dialects” of IR.  
- Practitioners want better out‑of‑the‑box toolchains → today, sanitizers, libc++, and compiler runtimes are fragmented across macOS/Linux distros, forcing people to build custom LLVM stacks.  
- Backend authors request IR‑origin executable tests and clearer SelectionDAG/GlobalISel semantics → current documentation and tests make it easy to implement subtly wrong backends.

### LLM perspective
- View: The biggest leverage is in infrastructure and specs: CI hygiene, public perf dashboards, and a precise formal IR model.  
- Impact: Toolchain vendors, language implementers, and backend authors would ship more reliable compilers with less duplicated “tribal knowledge.”  
- Watch next: Progress of the formal specification WG, ABI-lowering library, GlobalISel adoption, and any unified public performance+regression tracking for LLVM.
