# Platform-independent SIMD in Go

- Score: 387 | [HN](https://news.ycombinator.com/item?id=49843269) | Link: https://go.dev/blog/simd-experiment

### TL;DR

Go 1.27 adds an experimental platform- and vector-size-independent SIMD API, building on architecture-specific support introduced in Go 1.26. The package targets portable, readable code with near-assembly performance when operations map directly to hardware, efficient emulation for missing operations, and scalar fallback where SIMD is unavailable. It currently covers AVX variants, Arm NEON, and WebAssembly SIMD. The deliberately common operation set hides divergent vector lengths, masks, and instruction capabilities, while escape hatches permit small platform-specific implementations when necessary.

### Comment pulse

- Portable SIMD can deliver substantial gains → one browser benchmark reported both APIs near five times faster than scalar code.
- Portability has a measurable cost → that same benchmark found the portable path roughly 11% slower than architecture-specific SIMD.
- Size-agnostic vectors drew praise → commenters said the design better accommodates SVE and RISC-V vectors than fixed-width abstractions.

### LLM perspective

- View: The API trades complete instruction exposure for a useful portable intersection with targeted escape hatches.
- Impact: Go code can exploit SIMD without maintaining whole assembly kernels for every supported architecture.
- Watch next: Experimental feedback should test performance cliffs, missing reductions, emulation quality, and future SVE or RISC-V support.
